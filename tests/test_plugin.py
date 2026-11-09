"""Static package/fixture checks; these are not model or host acceptance tests."""
import sys
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_plugin


class PluginChecks(unittest.TestCase):
    def test_repository_marketplace_resolves_plugin_from_repo_root(self):
        catalog = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        entries = [x for x in catalog["plugins"] if x["name"] == "pekat-assistant"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["source"]["source"], "local")
        self.assertEqual((ROOT / entries[0]["source"]["path"]).resolve(), (ROOT / build_plugin.PLUGIN).resolve())

    def test_manifest_and_generated_references(self):
        self.assertEqual(build_plugin.validate(ROOT), [])
        self.assertEqual(build_plugin.build(ROOT, check=True), [])

    def test_representative_acceptance_fixtures_have_routed_sources(self):
        fixtures = yaml.safe_load((ROOT / "plugins/pekat-assistant/acceptance-fixtures.yaml").read_text(encoding="utf-8"))
        benchmark = yaml.safe_load((ROOT / "benchmarks/assistant_behavior_v0_2.yaml").read_text(encoding="utf-8"))
        benchmark_ids = {case["id"] for case in benchmark["cases"]}
        self.assertEqual({x["topic"] for x in fixtures["cases"]}, {"documentation", "tool-choice", "flow", "code-ptool", "classifier-detector-ocr", "diagnosis", "context-globaldata", "industrial-integration", "unsupported-operation"})
        skill = (ROOT / "plugins/pekat-assistant/skills/pekat-assistant/SKILL.md").read_text(encoding="utf-8")
        for case in fixtures["cases"]:
            with self.subTest(topic=case["topic"]):
                self.assertTrue(case["prompt"] and case["expected"])
                self.assertIn(case["benchmark"], benchmark_ids)
                self.assertIn(case["reference"], skill)
                self.assertTrue((ROOT / "plugins/pekat-assistant/skills/pekat-assistant" / case["reference"]).is_file())

    def test_detects_stale_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            relative = build_plugin.REFS + "/sample.md"
            with patch.object(build_plugin, "expected_references", return_value={relative: b"current"}):
                self.assertEqual(build_plugin.build(root, check=True), [relative])
                build_plugin.build(root)
                self.assertEqual(build_plugin.build(root, check=True), [])
                (root / relative).write_bytes(b"stale")
                self.assertEqual(build_plugin.build(root, check=True), [relative])

    def test_malformed_manifest_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = root / build_plugin.PLUGIN / "plugin.json"
            manifest.parent.mkdir(parents=True)
            for value in ([], {"$schema": build_plugin.SCHEMA, "name": None},
                          {"$schema": build_plugin.SCHEMA, "name": "ok", "extra": True}):
                with self.subTest(value=value):
                    manifest.write_text(json.dumps(value), encoding="utf-8")
                    self.assertTrue(build_plugin.validate(root))


if __name__ == "__main__":
    unittest.main()
