"""Install, drift and entry-pointer behavior of the host installer in a temporary home."""

import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
import install_hosts


class InstallHosts(unittest.TestCase):
    def setUp(self):
        temp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, temp)
        self.home = temp / "home"
        self.source = self.home / "src/hippo-spec"
        shutil.copytree(ROOT, self.source, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        for args in (["init", "-q"], ["add", "-A"],
                     ["-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "s"]):
            subprocess.run(["git", "-C", str(self.source), *args], check=True)
        self.profile = self.home / "profile.json"
        self.profile.write_text(json.dumps({"source": "~/src/hippo-spec", "hosts": {
            "codex": {}, "cursor": {}, "claude-code": {}, "kimi-code": {}, "grok": {}}}))

    def run_installer(self, **flags):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = install_hosts.run(self.profile, self.home, flags.get("apply", False),
                                     flags.get("check", False), False)
        return code, out.getvalue()

    def test_dry_run_writes_nothing_and_check_reports_drift(self):
        self.assertEqual(self.run_installer()[0], 0)
        self.assertFalse((self.home / ".codex").exists())
        self.assertEqual(self.run_installer(check=True)[0], 1)

    def test_apply_installs_every_file_host_and_is_idempotent(self):
        self.run_installer(apply=True)
        self.run_installer(apply=True)
        self.assertEqual(self.run_installer(check=True)[0], 0)
        for host in ("codex", "cursor", "claude", "kimi-code"):
            pkg = self.home / f".{host}/skills/hippo-spec"
            self.assertTrue((pkg / "SKILL.md").is_file(), host)
            self.assertTrue((pkg / install_hosts.PIN).is_file(), host)
        claude = (self.home / ".claude/CLAUDE.md").read_text()
        self.assertEqual(claude.count(install_hosts.START), 1)

    def test_ui_hosts_print_pointer_and_grok_names_the_source(self):
        _, out = self.run_installer(apply=True)
        self.assertIn("Cursor Settings", out)
        self.assertIn(f"Hippo Spec package: {self.source}/SKILL.md", out)

    def test_local_edits_are_kept_before_reinstall(self):
        self.run_installer(apply=True)
        skill = self.home / ".codex/skills/hippo-spec/SKILL.md"
        skill.write_text("edited")
        self.assertEqual(self.run_installer(check=True)[0], 1)
        self.run_installer(apply=True)
        kept = list((self.home / ".codex/skills").glob("hippo-spec.local-edits-*"))
        self.assertEqual(len(kept), 1)
        self.assertEqual((kept[0] / "SKILL.md").read_text(), "edited")
        self.assertNotEqual(skill.read_text(), "edited")

    def test_unmanaged_mention_is_not_duplicated(self):
        entry = self.home / ".codex/AGENTS.md"
        entry.parent.mkdir(parents=True)
        entry.write_text("# Project delivery with Hippo Spec\nhand-written\n")
        _, out = self.run_installer(apply=True)
        self.assertIn("merge by hand", out)
        self.assertNotIn(install_hosts.START, entry.read_text())


if __name__ == "__main__":
    unittest.main()
