"""Regression tests for publication gates using synthetic, temporary inputs."""
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_packages import build, expected_packages, files
import build_packages
from build_release_artifacts import build as build_release
from validate_public import benchmark_issues, index_issues, link_issues, text_issues, validate


class PublicGates(unittest.TestCase):
    def setUp(self):
        self.policy = yaml.safe_load((ROOT / "public-package.yaml").read_text(encoding="utf-8"))["validation"]

    def clone(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        target = Path(directory.name)
        for path in files(ROOT):
            out = target / path.relative_to(ROOT)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(path.read_bytes())
        return target

    def test_current_release_valid(self):
        self.assertEqual(validate(ROOT), [])

    def test_secret_is_rejected(self):
        value = "gh" + "p_" + "a" * 36
        self.assertIn("GitHub token", text_issues(value, self.policy))

    def test_credential_assignment_rejected(self):
        self.assertIn("credential assignment", text_issues("pass" + "word = " + "opaquevalue123", self.policy))

    def test_local_identity_rejected(self):
        value = "C" + ":" + chr(92) + "Users" + chr(92) + "synthetic"
        self.assertIn("absolute Windows path", text_issues(value, self.policy))

    def test_email_rejected(self):
        self.assertIn("email address", text_issues("person" + "@" + "example.org", self.policy))

    def test_unapproved_repository_rejected(self):
        value = "https://" + "github.com/" + "example/unreviewed"
        self.assertIn("unapproved GitHub repository", text_issues(value, self.policy))

    def test_policy_contains_no_private_identity_hashes(self):
        self.assertNotIn("blocked_identity_hashes", self.policy)

    def test_broken_link_rejected(self):
        self.assertTrue(link_issues(ROOT, ROOT / "README.md", "[missing](missing-document.md)"))

    def test_packages_are_deterministic(self):
        self.assertEqual(expected_packages(ROOT), expected_packages(ROOT))

    def test_generated_reference_drift_rejected(self):
        target = self.clone()
        ref = next((target / ".github/skills/pekat-assistant/references").rglob("*.md"))
        ref.write_text("Unexpected edit\n", encoding="utf-8")
        self.assertTrue(any("drift" in error for error in validate(target)))

    def test_database_file_rejected(self):
        target = self.clone()
        (target / "accidental.db").write_bytes(b"synthetic")
        failures = validate(target)
        self.assertTrue(any("forbidden file type" in error for error in failures))

    def test_new_markdown_does_not_require_self_referential_inventory(self):
        target = self.clone()
        (target / "docs/NEW_PUBLIC_NOTE.md").write_text("# Safe note\n", encoding="utf-8")
        self.assertFalse(any("manifest file set" in error for error in validate(target)))

    def test_package_path_escape_rejected(self):
        target = self.clone()
        config = yaml.safe_load((target / "public-package.yaml").read_text(encoding="utf-8"))
        config["knowledge_sources"] = ["../outside.md"]
        (target / "public-package.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
        with self.assertRaises(ValueError):
            expected_packages(target)

    def test_generated_reparse_point_rejected_before_write(self):
        target = self.clone()
        refs = target / ".github/skills/pekat-assistant/references"
        original = os.lstat

        class Attributes:
            st_mode = stat.S_IFDIR
            st_file_attributes = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 1024)

        def lstat(path, *args, **kwargs):
            if Path(path) == refs:
                return Attributes()
            return original(path, *args, **kwargs)

        with patch.object(build_packages.os, "lstat", side_effect=lstat):
            with self.assertRaisesRegex(ValueError, "Linked package path"):
                build(target)

    def test_standalone_skill_links(self):
        target = self.clone()
        skill = target / ".github/skills/pekat-assistant"
        for path in skill.rglob("*.md"):
            self.assertEqual(link_issues(skill, path, path.read_text(encoding="utf-8")), [])

    def test_force_added_local_directory_rejected(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        target = Path(directory.name)
        subprocess.run(["git", "init", "-q", str(target)], check=True)
        (target / ".venv").mkdir()
        (target / ".venv/payload.md").write_text("Synthetic text\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(target), "add", "-f", ".venv/payload.md"], check=True)
        self.assertTrue(any("excluded generated/local path" in issue for issue in index_issues(target, self.policy)))

    def test_behavior_benchmark_schema(self):
        self.assertEqual(benchmark_issues(ROOT), [])

    def test_release_artifacts_are_ref_pinned(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        out = Path(directory.name)
        artifacts = build_release("v-test", out)
        self.assertTrue(all(path.is_file() for path in artifacts))
        self.assertIn("v-test", (out / "VALIDATION.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
