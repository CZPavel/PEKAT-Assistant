"""Build reproducible skill references and GPT knowledge."""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import stat
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ".github/skills/pekat-assistant/references"
GPT = "gpt/knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md"
EXCLUDED_PARTS = {".git", "__pycache__", ".venv", ".pytest_cache", "dist"}


def safe_path(root: Path, name: str) -> Path:
    path = root / name
    if Path(name).is_absolute() or ".." in Path(name).parts or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Package path outside root: " + name)
    for component in [root, *(root / Path(*Path(name).parts[:i]) for i in range(1, len(Path(name).parts) + 1))]:
        try:
            attributes = os.lstat(component)
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(attributes.st_mode) or bool(getattr(attributes, "st_file_attributes", 0)
                                                   & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)):
            raise ValueError("Linked package path: " + name)
    return path


def files(root: Path) -> list[Path]:
    result = []
    for p in sorted(root.rglob("*")):
        if any(x in EXCLUDED_PARTS for x in p.relative_to(root).parts):
            continue
        safe_path(root, p.relative_to(root).as_posix())
        if p.is_file():
            result.append(p)
    return result


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(value: object) -> bytes:
    return yaml.safe_dump(value, sort_keys=True, allow_unicode=True).encode("utf-8")


def expected_packages(root: Path) -> dict[str, bytes]:
    config = yaml.safe_load(safe_path(root, "public-package.yaml").read_text(encoding="utf-8"))
    sources = config["knowledge_sources"]
    if len(sources) != len(set(sources)):
        raise ValueError("Duplicate package source")
    outputs: dict[str, bytes] = {}
    sections = ["# PEKAT Assistant public knowledge\n\nGenerated from canonical public sources; do not edit.\n"]
    entries = []
    for source in sources:
        path = safe_path(root, source).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError("Invalid package source: " + source)
        data = path.read_bytes()
        text = data.decode("utf-8")

        def absolute_link(match: re.Match) -> str:
            label, target = match.groups()
            if re.match(r"[a-zA-Z]+:|#", target):
                return match.group(0)
            clean, _, anchor = target.partition("#")
            resolved = (path.parent / clean).resolve()
            if not resolved.is_relative_to(root.resolve()):
                raise ValueError("Link outside package")
            url = "https://github.com/CZPavel/PEKAT-Assistant/blob/main/" + resolved.relative_to(root.resolve()).as_posix()
            return f"[{label}]({url}" + ("#" + anchor if anchor else "") + ")"

        def portable_link(match: re.Match) -> str:
            _, target = match.groups()
            if re.match(r"[a-zA-Z]+:|#", target):
                return match.group(0)
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if resolved.is_relative_to(root.resolve()) and resolved.relative_to(root.resolve()).as_posix() in sources:
                return match.group(0)
            return absolute_link(match)

        outputs[f"{SKILL}/{source}"] = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", portable_link, text).encode("utf-8")
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", absolute_link, text)
        sections.append(f"\n---\n\nSource: " + chr(96) + source + chr(96) + f"\n\n{text.rstrip()}\n")
        entries.append({"source": source, "sha256": digest(data)})

    outputs[GPT] = "\n".join(sections).encode("utf-8")
    outputs["gpt/KNOWLEDGE_MANIFEST.yaml"] = dump({
        "schema": "pekat-public-gpt/1",
        "generated": True,
        "files": [{"path": GPT, "sha256": digest(outputs[GPT]), "sources": entries}],
    })
    return outputs


def build(root: Path = ROOT, check: bool = False) -> list[str]:
    packages = expected_packages(root)
    drift = []
    expected_refs = {name for name in packages if name.startswith(SKILL + "/")}
    ref_dir = root / SKILL
    if ref_dir.exists():
        extra = {p.relative_to(root).as_posix() for p in ref_dir.rglob("*") if p.is_file()} - expected_refs
        if extra:
            raise ValueError("Unexpected generated references: " + ", ".join(sorted(extra)))
    for name, data in sorted(packages.items()):
        path = safe_path(root, name)
        if not path.is_file() or path.read_bytes() != data:
            drift.append(name)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    return drift


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changes = build(check=args.check)
    if args.check and changes:
        raise SystemExit("Generated drift: " + ", ".join(changes))
    print("Packages: " + ("MATCH" if args.check else "built"))
