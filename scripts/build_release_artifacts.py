"""Build standalone, ref-pinned public release artifacts."""
from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def safe_ref(value: str) -> str:
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
    result = "".join(ch if ch in allowed else "-" for ch in value).strip("-")
    if not result:
        raise ValueError("Empty release ref")
    return result


def pin_text(text: str, ref: str) -> str:
    return text.replace(
        "https://github.com/CZPavel/PEKAT-Assistant/blob/main/",
        "https://github.com/CZPavel/PEKAT-Assistant/blob/" + ref + "/",
    )


def write_zip(source: Path, output: Path, prefix: str = "") -> None:
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                rel = path.relative_to(source).as_posix()
                archive.write(path, (prefix + "/" + rel).strip("/"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build(ref: str, output: Path) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    name = safe_ref(ref)

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        skill_src = ROOT / ".github/skills/pekat-assistant"
        skill_dst = temp / "skill/pekat-assistant"
        shutil.copytree(skill_src, skill_dst)
        for path in skill_dst.rglob("*.md"):
            path.write_text(pin_text(path.read_text(encoding="utf-8"), ref), encoding="utf-8")
        skill_zip = output / f"pekat-assistant-skill-{name}.zip"
        write_zip(temp / "skill", skill_zip)

        gpt_dst = temp / "gpt"
        (gpt_dst / "knowledge").mkdir(parents=True)
        for rel in ["README.md", "BUILDER_INSTRUCTIONS.md"]:
            text = (ROOT / "gpt" / rel).read_text(encoding="utf-8")
            (gpt_dst / rel).write_text(pin_text(text, ref), encoding="utf-8")
        source_knowledge = ROOT / "gpt/knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md"
        pinned = pin_text(source_knowledge.read_text(encoding="utf-8"), ref)
        target_knowledge = gpt_dst / "knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md"
        target_knowledge.write_text(pinned, encoding="utf-8")
        manifest = {
            "schema": "pekat-public-gpt-release/1",
            "release_ref": ref,
            "files": [{
                "path": "knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md",
                "sha256": hashlib.sha256(pinned.encode("utf-8")).hexdigest(),
            }],
        }
        (gpt_dst / "KNOWLEDGE_MANIFEST.yaml").write_text(
            yaml.safe_dump(manifest, sort_keys=True, allow_unicode=True), encoding="utf-8"
        )
        gpt_zip = output / f"pekat-assistant-gpt-{name}.zip"
        write_zip(gpt_dst, gpt_zip, prefix="pekat-assistant-gpt")

    artifacts = [skill_zip, gpt_zip]
    sums = output / "SHA256SUMS.txt"
    sums.write_text("".join(f"{sha256(path)}  {path.name}\n" for path in artifacts), encoding="utf-8")
    validation = output / "VALIDATION.md"
    validation.write_text(
        "# Public release validation\n\n"
        f"Release ref: {ref}\n\n"
        "Artifacts are generated from the validated public repository. "
        "Repository links inside packaged text are pinned to this ref. "
        "SHA256SUMS.txt covers the ZIP artifacts.\n",
        encoding="utf-8",
    )
    return artifacts + [sums, validation]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    for artifact in build(args.ref, args.output):
        print(artifact)
