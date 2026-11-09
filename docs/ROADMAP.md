# Public roadmap — PEKAT Assistant

Updated 2026-11-09. This is an **ordered direction**, not a promised delivery schedule. The private application and this publicly distributed knowledge package are distinct.

## Current public baseline

The public Assistant provides version-aware knowledge, engineering decision support, examples, user scenarios and a GPT/Codex knowledge route. The separate public PEKAT Vision skill also offers bounded offline diagnostic scripts. Neither repository grants control of a running PEKAT installation simply by being installed.

## Stage A — unify and maintain public knowledge

**Goal:** the public Assistant and the standalone skill explain the same current observable PEKAT behavior without competing as independent sources of truth.

- Publish task-oriented capability documentation, examples and version/evidence labels.
- Carry forward useful older PEKAT 3.19.3 and 4.0.1 observations while retaining their exact scope.
- Curate newer 4.0.3 findings about Code/Form/PTool, FLOW decisions, images, results, datasets, training, outputs, and device integration.
- Keep vendor/device-specific claims routed to appropriate model-specific sources.
- Exclude customer material, private execution details and unapproved implementations.

**Acceptance:** matching terms and version boundaries across the two repositories; checked public links, examples and privacy gates.

## Stage B — practical public tools and examples

**Goal:** retain and improve the existing standalone skill's offline scripts, then add only portable capabilities with clear inputs and tests.

Potential work: sanitized log and training-history reports, supplied project explanation, semantic comparisons, dataset/model QA, FLOW decision examples, Code/PTool templates and version-transition checks.

**Acceptance:** each shipped tool has a documented entry point, sample input/output, offline test and explicit supported-version scope. New tools must not be advertised before they actually ship.

## Stage C — public assisted workflows

**Goal:** turn common engineering tasks into understandable end-to-end user journeys: describe a defect, choose image acquisition, draft FLOW, inspect evidence, diagnose a failure and verify an improvement.

A possible later integration may connect these journeys to supported, permissioned PEKAT interfaces. Approval, bounded scope, readback and failure handling are prerequisites. Native GUI capability does not by itself mean a public automated action exists.

**Acceptance:** real workflow tests, clear error states and safe behavior when a target version or interface is unsupported.

## Stage D — separate Windows application release track

A Windows Assistant application is under private development and bounded private acceptance. A **public Windows beta remains a separate planned release**, subject to distribution rights, packaging, installer/dependency review, safe handling of local data, tool permissions, version mapping, reproducible validation and explicit release checks.

This roadmap does not announce that installer, its date or any public production acceptance.

## Longer-term research and product directions

Explore representative-image selection, assisted annotation review, model/experiment comparison, user-guided FLOW construction, historical image-health analysis, multi-camera and sensor result composition, multimodal interaction and a human-approved iterative improvement loop.

An official PEKAT MCP, if published by the vendor, may become another supported interface. It is not assumed to exist or to make previously unsupported actions safe.

## How work is promoted

Every feature moves separately through **proposed → implemented → tested on a stated scope → publicly packaged → usable by a public user**. The roadmap never upgrades a capability merely by describing it.

See [public capability guide](PUBLIC_CAPABILITY_GUIDE.md), [extended scenarios](USER_SCENARIOS_EXTENDED.md) and [validation](VALIDATION.md).
