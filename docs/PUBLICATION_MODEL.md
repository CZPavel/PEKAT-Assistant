# Publication model

Public content is a curated derivative of a separately maintained private development project. Publication uses an allowlist/rewrite model rather than copying a private tree and trying to blacklist sensitive files afterward.

Private paths, customer evidence, proprietary contracts, runtime artifacts and raw forensic material stay outside the release.

## Public repository validation

Run:

    python scripts/build_packages.py --check
    python scripts/validate_public.py
    python -m unittest discover -s tests

After staging reviewed files with Git, run:

    python scripts/validate_public.py --index

The public validator intentionally contains only generic detection rules. Customer/project-specific deny lists belong to the private publication layer and are not published as hashes or reversible clues.

## Generated packages

Standalone skill references and the committed GPT aggregate are generated from approved public knowledge sources. Edit maintained public sources, not generated copies.

Release packaging is separate and pins links to the supplied release ref.

## Source-of-truth boundary

The private development repository remains authoritative for implementation/runtime evidence. This public repository is authoritative for the public sanitized edition.

A public update should inspect the private checkpoint, classify changes, update maintained public sources, validate generated packages and publication gates, review the diff, then merge and tag a release.
