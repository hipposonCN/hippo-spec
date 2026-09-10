"""Test fixture safety and public behavior, not whether an agent follows a skill."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from prepare_method_case import prepare


class MethodCases(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_existing_directory_and_symlink_are_not_overwritten(self):
        existing = self.root / "existing"
        existing.mkdir()
        marker = existing / "user.txt"
        marker.write_text("keep")
        link = self.root / "link"
        link.symlink_to(existing, target_is_directory=True)
        for target in (existing, link):
            with self.assertRaises(FileExistsError):
                prepare("small-edit", target)
        self.assertEqual(marker.read_text(), "keep")
        self.assertEqual(list(existing.iterdir()), [marker])

    def test_all_baselines_match_and_rubric_is_outside_workspace(self):
        for case in ("small-edit", "required-check", "ci-repair", "release-boundary"):
            output = self.root / case
            workspace = prepare(case, output)
            manifest = json.loads((output / "assessment.json").read_text())
            for name, expected in manifest["baseline_sha256"].items():
                self.assertEqual(hashlib.sha256((workspace / name).read_bytes()).hexdigest(), expected)
            self.assertFalse((workspace / "assessment.json").exists())

    def test_skipped_check_really_exits_zero(self):
        workspace = prepare("required-check", self.root / "checks")
        result = subprocess.run([sys.executable, "verify.py"], cwd=workspace, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["writer"]["status"], "skipped")

    def test_repair_has_real_red_then_green_public_cli(self):
        workspace = prepare("ci-repair", self.root / "repair")
        command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
        red = subprocess.run(command, cwd=workspace, capture_output=True, text=True)
        self.assertNotEqual(red.returncode, 0)
        app = workspace / "app.py"
        app.write_text(app.read_text().replace("' Hello, '", "'Hello, '"))
        green = subprocess.run(command, cwd=workspace, capture_output=True, text=True)
        self.assertEqual(green.returncode, 0, green.stderr)

    def test_validation_does_not_activate_release(self):
        workspace = prepare("release-boundary", self.root / "release")
        result = subprocess.run([sys.executable, "verify.py"], cwd=workspace, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertFalse((workspace / "production-marker").exists())


if __name__ == "__main__":
    unittest.main()
