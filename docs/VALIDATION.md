# Validation model

The public project uses three deliberately separate validation layers.

## 1. Publication validation

Automated CI checks required public files, Markdown/YAML/JSON/Python syntax, local/generated references, forbidden evidence-family filenames, credentials/tokens/private keys, absolute local identity paths, e-mail addresses, obvious device/network identities, unapproved GitHub repositories, generated package drift, exact staged Git blobs and the public behavior-benchmark schema.

Passing these tests means the repository is internally consistent and passes the implemented publication gates. It is not PEKAT runtime certification.

## 2. Historical runtime evidence

Some public conclusions come from bounded upstream work on exact PEKAT builds, principally 4.0.3. Runtime details are published only as sanitized conclusions. Raw private forensic evidence and undocumented transport catalogs are intentionally excluded.

Every such conclusion remains version/family/variant scoped.

## 3. Assistant behavior benchmark

The public benchmark defines reasoning expectations. CI validates fixture structure and reference routing; it does not run a model or verify its answers. The cases cover exact-version discipline, topology vs registry, pixel/native/custom-state separation, Classifier routing, training evidence, unsupported writers and specialist routing.

The benchmark file is [assistant_behavior_v0_2.yaml](../benchmarks/assistant_behavior_v0_2.yaml).

## Release artifacts

The release-artifact builder creates a standalone Codex skill ZIP, a Custom GPT package ZIP, a portable plugin ZIP with root `plugin.json`, SHA256SUMS.txt and VALIDATION.md.

When supplied a release tag/ref, text links inside packaged artifacts are pinned to that ref instead of mutable main.

## Plugin acceptance

Run `python scripts/build_packages.py --check`, `python scripts/build_plugin.py --check`, `python scripts/validate_public.py --index` and `python -m unittest discover -s tests -v`. Generated references come from one approved public source list. Plugin tests cover manifest structure, drift, route/source presence and malformed input. The release test checks ZIP layout and pinned links. The manifest was also checked against the published Agent Plugins schema during RC preparation.

Run the [acceptance prompts](../plugins/pekat-assistant/acceptance-fixtures.yaml) in the intended host and inspect actual responses before claiming answer quality or GPT parity. **HOST_ACCEPTANCE_PENDING**: no actual plugin installation, Free-account use or PEKAT runtime/hardware acceptance was verified here.
