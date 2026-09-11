"""Package shape checks for the short kernel and host adapters."""

from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from validate_package import validate


class ValidatePackage(unittest.TestCase):
    def test_current_package_passes(self):
        self.assertEqual(validate(ROOT), [])

    def test_kernel_must_not_bind_codex_without_generic_jobs(self):
        temp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temp)
        pkg = (temp / "pkg").resolve()
        shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns(".git"))
        skill = pkg / "SKILL.md"
        text = skill.read_text()
        skill.write_text(text.replace("references/generic-delivery.md", "references/codex-delivery.md", 1))
        errors = validate(pkg)
        self.assertTrue(any("generic host jobs" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
