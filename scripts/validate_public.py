"""Offline public-release gates. Reject unsafe files and package drift."""
from __future__ import annotations

import argparse
import ast
import io
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

from build_packages import ROOT, EXCLUDED_PARTS, build, files

REQUIRED = [
    "README.md", "LICENSE", "DISCLAIMER.md", "SECURITY.md", "CONTRIBUTING.md",
    "THIRD_PARTY_NOTICES.md", "CHANGELOG.md", "knowledge/INDEX.md",
    "docs/ARCHITECTURE.md", "docs/GETTING_STARTED.md", "docs/USER_SCENARIOS.md",
    "docs/USER_SCENARIOS_EXTENDED.md", "docs/CAPABILITIES.md", "docs/EVIDENCE_MODEL.md",
    "docs/EVIDENCE_AND_VALIDATION_STATUS.md", "docs/VERSION_SUPPORT.md", "docs/VERSION_MATRIX.md",
    "docs/SPECIALIST_SKILLS.md", "docs/SPECIALIST_SKILL_STATUS.md",
    "docs/PRACTICAL_RUNTIME_RULES.md", "docs/VALIDATION.md", "docs/PUBLICATION_MODEL.md",
    ".github/skills/pekat-assistant/SKILL.md", "gpt/README.md",
    "gpt/BUILDER_INSTRUCTIONS.md", "gpt/KNOWLEDGE_MANIFEST.yaml",
    "benchmarks/assistant_behavior_v0_2.yaml",
    "scripts/build_packages.py", "scripts/build_release_artifacts.py",
    ".github/workflows/validate-public.yml", ".github/workflows/release-public.yml",
    "requirements-dev.txt", "public-package.yaml"
]
EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
SPECIAL_FILES = {"LICENSE", ".gitignore", ".gitattributes"}
PATTERNS = {
    "absolute Windows path": r"(?i)\b[A-Z]:[\\/]",
    "absolute Unix identity path": r"/(?:home|Users|mnt|opt|var)/[A-Za-z0-9_]",
    "email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "private key": r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b",
    "API token": r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b|\bAKIA[A-Z0-9]{16}\b",
    "credential assignment": r'''(?i)(?:password|passwd|api[_-]?key|(?:auth|access)[_-]?token|(?:client[_-]?)?secret|license[_-]?key)["']?[ \t]*[=:][ \t]*(?:"[^"\r\n]{8,}"|'[^'\r\n]{8,}'|[^\s"';,]{8,})''',
    "bearer credential": r"(?i)\bBearer\s+[A-Za-z0-9._/-]{16,}",
    "JWT credential": r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b",
    "network identity": r"(?i)\b(?:\d{1,3}\.){3}\d{1,3}\b|\bhttps?://[^/\s]+\.(?:local|internal|corp)\b",
    "device serial": r'''(?i)\b(?:serial(?:number|_number)?|device[_-]?sn)\s*[=:]\s*["']?[A-Za-z0-9-]{6,}''',
    "test-project identity": r"(?i)\bAUTO_TEST_FOR_[A-Z0-9_]+\b",
    "private transport": r"(?i)\bset_" r"store\b|\bsocket\.io\b|\bimage" r"Rectangles\b|\bcodeItems\.db\b",
}
FORBIDDEN_NAMES = re.compile(
    r"(?i)(?:PRE_" r"A4|FORENSIC|pekat_gui_api_(?:catalog|coverage)|browser[-_](?:dump|state|trace)|"
    r"network[-_]trace|frontend[-_]bundle|\.min\.js$|(?:^|/)(?:auth\.json|cookies(?:\.json)?|credentials[^/]*|\.env(?:\.[^/]*)?)$)"
)


def text_issues(text: str, policy: dict) -> list[str]:
    issues = [name for name, pattern in PATTERNS.items() if re.search(pattern, text)]
    for target in re.findall(r"https?://[^\s<>\)\]\"']+", text):
        parsed = urlparse(target)
        if parsed.username or parsed.password:
            issues.append("URL credentials")
        if (parsed.hostname or "").casefold().removeprefix("www.") == "github.com":
            parts = parsed.path.strip("/").split("/")
            allowed = {repo.casefold() for repo in policy["public_github_repositories"]}
            if len(parts) < 2 or "/".join(parts[:2]).casefold() not in allowed:
                issues.append("unapproved GitHub repository")
    return sorted(set(issues))


def index_issues(root: Path, policy: dict) -> list[str]:
    if not (root / ".git").exists():
        return []
    output = subprocess.check_output(["git", "-C", str(root), "ls-files", "--stage", "-z"])
    entries = []
    issues = []
    for entry in output.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, oid, stage = metadata.decode("ascii").split()
        rel = name.decode("utf-8")
        if stage != "0" or mode not in {"100644", "100755"}:
            issues.append("index: non-regular/conflicted path: " + rel)
        if any(part in EXCLUDED_PARTS for part in Path(rel).parts):
            issues.append("index: excluded generated/local path: " + rel)
        entries.append((rel, oid))
    if not entries:
        return issues + ["index: no staged public files"]

    blobs = subprocess.run(
        ["git", "-C", str(root), "cat-file", "--batch"],
        input="".join(oid + "\n" for _, oid in entries).encode("ascii"),
        stdout=subprocess.PIPE,
        check=True,
    ).stdout
    stream = io.BytesIO(blobs)
    for rel, oid in entries:
        header = stream.readline().decode("ascii").split()
        if len(header) != 3 or header[1] != "blob":
            issues.append("index: unreadable blob: " + rel)
            break
        data = stream.read(int(header[2]))
        stream.read(1)
        path = root / rel
        if not path.is_file() or path.read_bytes().replace(b"\r\n", b"\n") != data:
            issues.append("index/worktree mismatch: " + rel)
        try:
            issues.extend("index " + rel + ": " + issue for issue in text_issues(data.decode("utf-8"), policy))
        except UnicodeError:
            issues.append("index: binary blob: " + rel)
    return issues


def link_issues(root: Path, path: Path, text: str) -> list[str]:
    issues = []
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).split(' "', 1)[0].strip("<>")
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        clean = unquote(target.split("#", 1)[0])
        resolved = (path.parent / clean).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            issues.append("broken/outside link: " + target)
    for target in re.findall(r"(?m)^\[[^\]]+\]:\s+(\S+)", text):
        if not re.match(r"[a-zA-Z]+:|#", target):
            resolved = (path.parent / unquote(target.split("#")[0])).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                issues.append("broken reference link: " + target)
    return issues


def benchmark_issues(root: Path) -> list[str]:
    path = root / "benchmarks/assistant_behavior_v0_2.yaml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        cases = data["cases"]
    except (OSError, KeyError, TypeError, yaml.YAMLError) as exc:
        return ["benchmark: invalid: " + str(exc)]
    issues = []
    ids = []
    for case in cases:
        if not isinstance(case, dict):
            issues.append("benchmark: case is not a mapping")
            continue
        missing = {"id", "prompt", "must", "must_not"} - set(case)
        if missing:
            issues.append("benchmark: missing fields: " + ",".join(sorted(missing)))
        ids.append(case.get("id"))
        if not case.get("must") or not case.get("must_not"):
            issues.append("benchmark: empty expectation list")
    if len(ids) != len(set(ids)):
        issues.append("benchmark: duplicate id")
    return issues


def validate(root: Path = ROOT, check_index: bool = False) -> list[str]:
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append("missing: " + name)
    if errors:
        return errors

    try:
        config = yaml.safe_load((root / "public-package.yaml").read_text(encoding="utf-8"))
        policy = config["validation"]
    except (ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        return ["invalid release metadata: " + str(exc)]

    try:
        paths = files(root)
    except ValueError as exc:
        return ["filesystem boundary: " + str(exc)]

    for p in root.rglob("*"):
        if any(x in EXCLUDED_PARTS for x in p.relative_to(root).parts):
            continue
        attributes = os.lstat(p)
        if stat.S_ISLNK(attributes.st_mode) or bool(
            getattr(attributes, "st_file_attributes", 0)
            & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        ):
            errors.append("link/junction forbidden: " + p.relative_to(root).as_posix())

    for path in paths:
        rel = path.relative_to(root).as_posix()
        if path.suffix not in EXTENSIONS and rel not in SPECIAL_FILES:
            errors.append(rel + ": forbidden file type")
        if FORBIDDEN_NAMES.search(rel):
            errors.append(rel + ": forbidden evidence family")
        try:
            text = path.read_text(encoding="utf-8")
            if "\x00" in text:
                errors.append(rel + ": binary data")
            if path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(text)
            elif path.suffix == ".json":
                json.loads(text)
            elif path.suffix == ".py":
                ast.parse(text)
            if path.name == "SKILL.md":
                front = yaml.safe_load(text.split("---", 2)[1])
                if front.get("name") != "pekat-assistant" or not front.get("description"):
                    errors.append(rel + ": invalid skill frontmatter")
            errors.extend(rel + ": " + issue for issue in text_issues(text, policy))
            if path.suffix == ".md":
                errors.extend(rel + ": " + issue for issue in link_issues(root, path, text))
        except (ValueError, IndexError, AttributeError, SyntaxError, UnicodeError, yaml.YAMLError) as exc:
            errors.append(rel + ": invalid syntax/text: " + str(exc))

    errors.extend(benchmark_issues(root))
    try:
        errors.extend("generated drift: " + name for name in build(root, check=True))
    except (ValueError, KeyError, OSError, yaml.YAMLError) as exc:
        errors.append("package failure: " + str(exc))
    if check_index:
        errors.extend(index_issues(root, policy))
    return sorted(set(errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--index", action="store_true", help="Also scan exact staged Git blobs before publication")
    args = parser.parse_args()
    failures = validate(args.root.resolve(), check_index=args.index)
    if failures:
        print("\n".join(failures))
        sys.exit(1)
    print("PASS: structure, syntax, references, sensitive/secret scan, benchmark schema and generated drift")
