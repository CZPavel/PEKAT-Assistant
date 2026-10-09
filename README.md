# PEKAT Assistant — public preview

Independent, version-aware advisory knowledge and Codex/GPT guidance for PEKAT VISION inspection design, supplied project/FLOW explanation, datasets, ML, troubleshooting and industrial integration.

This repository is a sanitized public derivative of a separately maintained private development project. It intentionally excludes customer data, raw forensic evidence, private transport contracts, runtime controllers and project/device writers.

Start here:

- [Getting started](docs/GETTING_STARTED.md)
- [Practical runtime rules](docs/PRACTICAL_RUNTIME_RULES.md)
- [Capabilities](docs/CAPABILITIES.md)
- [Evidence and validation status](docs/EVIDENCE_AND_VALIDATION_STATUS.md)
- [Extended user scenarios](docs/USER_SCENARIOS_EXTENDED.md)
- [Version matrix](docs/VERSION_MATRIX.md)
- [Validation model](docs/VALIDATION.md)
- [Knowledge index](knowledge/INDEX.md)
- [Standalone Codex skill](.github/skills/pekat-assistant/SKILL.md)
- [Custom GPT guidance](gpt/README.md)
- [Publication model](docs/PUBLICATION_MODEL.md)

## What the public preview is

The public edition is primarily a knowledge and reasoning layer. It helps a user:

- separate documented behavior, static structure, runtime observation and writer authority;
- reason about actual FLOW execution rather than module inventory alone;
- keep image raster, native PEKAT results and custom Context/shared state distinct;
- preserve exact-version boundaries;
- interpret Detector, Classifier, OCR and training evidence without collapsing their semantics;
- design safe PEKAT integrations with Basler, IFM IO-Link, KEYENCE LJ-X/LJ-S and embedded platforms;
- identify the smallest useful check when evidence is incomplete.

Historical upstream work covered narrow exact-4.0.3 runtime and authoring subsets. Those controllers and writers are not distributed here.

## What it does not do

This preview does not automatically connect to PEKAT, open a project database, operate cameras, train a model, mutate annotations, author arbitrary FLOW or control hardware. It does not expose undocumented PEKAT frontend transports or raw forensic catalogs.

The public skill therefore fails closed for unsupported execution and should provide an evidence-bound explanation, plan or bounded verification proposal instead.

## Practical evidence already captured

The public edition retains useful engineering conclusions while keeping raw private evidence out of the repository. Examples include:

- execution topology is not the same as registry membership;
- branch-local exit semantics must not be generalized to the whole FLOW;
- GlobalData is process-lifetime shared state, not durable storage;
- Classifier candidate lists must not be treated as Detector object instances;
- native overlays/results, image pixels and custom Context can behave differently across branches;
- training acknowledgement/progress does not by itself prove a usable saved model;
- a static read representation does not authorize a writer;
- a historical exact-version writer does not transfer automatically to another PEKAT patch.

See [Practical runtime rules](docs/PRACTICAL_RUNTIME_RULES.md) and [Evidence and validation status](docs/EVIDENCE_AND_VALIDATION_STATUS.md).

## Codex, GPT and specialist skills

Copy the complete .github/skills/pekat-assistant directory for Codex use. For a Custom GPT use the builder instructions and generated knowledge package under gpt/.

Optional public specialist skills provide narrower vendor/device knowledge:

- Basler cameras
- IFM IO-Link
- KEYENCE LJ-X/LJ-S

They are independent dependencies; PEKAT Assistant owns only the PEKAT-side composition boundary. See [Specialist skill status](docs/SPECIALIST_SKILL_STATUS.md).

## Public validation and releases

Public CI checks structure, syntax, links, forbidden evidence families, secrets/credentials, local paths, private repository references, generated package drift and the behavior-benchmark schema.

Release packaging creates standalone skill and GPT archives, checksums and a validation note. Release packages pin repository links to the release ref rather than relying on mutable main.

See [Validation](docs/VALIDATION.md).

## Longer-term direction

The architecture target is:

User / chat / agent
→ PEKAT Assistant knowledge + capability routing
→ typed Core / safe transaction boundary
→ supported exact-version PEKAT interfaces
→ PEKAT VISION

A future official PEKAT MCP can fit as a transport/adapter over the same boundary. It is not assumed to exist or to authorize operations today.

**Unofficial community project / not affiliated with or officially supported by the PEKAT VISION vendor.** Original project contributions are licensed under Apache-2.0; external vendor material retains its own ownership.

## October update

[Ten practical intent routes](knowledge/assistant/DECISION_GUIDE_403.md) cover Czech/English requests, frame freshness, image channels, crop coordinates and unsupported writer variants. This remains an advisory edition.
