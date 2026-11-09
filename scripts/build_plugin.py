"""Build and statically validate the standalone public Agent Plugin."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from build_packages import ROOT, SKILL, expected_packages, safe_path

PLUGIN = "plugins/pekat-assistant"
REFS = PLUGIN + "/skills/pekat-assistant/references"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def expected_references(root: Path) -> dict[str, bytes]:
    return {REFS + name[len(SKILL):]: data for name, data in expected_packages(root).items()
            if name.startswith(SKILL + "/")}


def build(root: Path = ROOT, check: bool = False) -> list[str]:
    expected = expected_references(root)
    refdir = safe_path(root, REFS)
    extra = {p.relative_to(root).as_posix() for p in refdir.rglob("*") if p.is_file()} - set(expected) if refdir.exists() else set()
    if extra:
        raise ValueError("Unexpected generated references: " + ", ".join(sorted(extra)))
    drift = []
    for name, data in sorted(expected.items()):
        path = safe_path(root, name)
        if not path.is_file() or path.read_bytes() != data:
            drift.append(name)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    return drift


def validate(root: Path = ROOT) -> list[str]:
    issues = []
    plugin = safe_path(root, PLUGIN)
    try:
        manifest = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
        allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
        if not isinstance(manifest, dict):
            return ["manifest: expected object"]
        if set(manifest) - allowed:
            issues.append("manifest: invalid properties")
        if manifest.get("$schema") != SCHEMA or not re.fullmatch(r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?", manifest.get("name", "")) or len(manifest.get("name", "")) > 64:
            issues.append("manifest: invalid schema or name")
        for key in ("version", "description", "homepage", "repository", "license"):
            if key in manifest and not isinstance(manifest[key], str):
                issues.append("manifest: invalid " + key)
        if "keywords" in manifest and (not isinstance(manifest["keywords"], list) or not all(isinstance(x, str) for x in manifest["keywords"])):
            issues.append("manifest: invalid keywords")
        if "author" in manifest and (not isinstance(manifest["author"], dict) or set(manifest["author"]) - {"name", "email", "url"} or not all(isinstance(x, str) for x in manifest["author"].values())):
            issues.append("manifest: invalid author")
        if "extensions" in manifest and (not isinstance(manifest["extensions"], dict) or not all(isinstance(x, dict) for x in manifest["extensions"].values())):
            issues.append("manifest: invalid extensions")
        skills = list((plugin / "skills").glob("*/SKILL.md"))
        if len(skills) != 1 or skills[0].parent.name != "pekat-assistant":
            issues.append("expected exactly one PEKAT skill")
        if (plugin / "mcp.json").exists() or (plugin / ".mcp.json").exists():
            issues.append("unexpected MCP configuration")
        issues.extend("generated drift: " + x for x in build(root, check=True))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        issues.append("invalid plugin: " + str(exc))
    return issues


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        build()
    failures = validate()
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: static plugin structure and generated references; HOST_ACCEPTANCE_PENDING")
