# Validation model

The public project uses three deliberately separate validation layers.

## 1. Publication validation

Automated CI checks required public files, Markdown/YAML/JSON/Python syntax, local/generated references, forbidden evidence-family filenames, credentials/tokens/private keys, absolute local identity paths, e-mail addresses, obvious device/network identities, unapproved GitHub repositories, generated package drift, exact staged Git blobs and the public behavior-benchmark schema.

Passing these tests means the repository is internally consistent and passes the implemented publication gates. It is not PEKAT runtime certification.

## 2. Historical runtime evidence

Some public conclusions come from bounded upstream work on exact PEKAT builds, principally 4.0.3. Runtime details are published only as sanitized conclusions. Raw private forensic evidence and undocumented transport catalogs are intentionally excluded.

Every such conclusion remains version/family/variant scoped.

## 3. Assistant behavior benchmark

The public benchmark verifies reasoning expectations rather than PEKAT execution. It checks exact-version discipline, topology vs registry, pixel/native/custom-state separation, Classifier routing, training evidence, unsupported writers and specialist routing.

The benchmark file is [assistant_behavior_v0_2.yaml](../benchmarks/assistant_behavior_v0_2.yaml).

## Release artifacts

The release-artifact builder creates a standalone Codex skill ZIP, a Custom GPT package ZIP, SHA256SUMS.txt and VALIDATION.md.

When supplied a release tag/ref, text links inside packaged artifacts are pinned to that ref instead of mutable main.
