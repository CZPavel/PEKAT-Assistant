# PEKAT Assistant public knowledge

Generated from canonical public sources; do not edit.


---

Source: `knowledge/INDEX.md`

# Knowledge index

Original advisory topics; no vendor manuals or runtime controller. Historical observations retain exact-version limits.

- [Inspection design](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/VISION_DESIGN.md)
- [Camera acquisition](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CAMERA_ACQUISITION.md)
- [FLOW interpretation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/FLOW_AUTHORING.md)
- [Context and shared state](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CONTEXT_CODE_GLOBALDATA.md)
- [Detector, Classifier and OCR](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DETECTOR_CLASSIFIER_OCR.md)
- [Detector annotation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DETECTOR_ANNOTATION_403.md)
- [Anomaly learning](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/ANOMALY_UNSUPERVISED.md)
- [Supervised masks](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/SUPERVISED_MASK_LIFECYCLE.md)
- [OCR annotation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/OCR_ANNOTATION.md)
- [Data and model portability](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DATA_MODEL_PORTABILITY.md)
- [PTool and Form](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PTOOL_PMODULE_FORM.md)
- [Embedded Python and ML](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/RUNTIME_PYTHON_ML.md)
- [External-model example](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/EXTERNAL_TORCHVISION_PTOOL_403.md)
- [External teacher to native Detector](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/EXTERNAL_TEACHER_DETECTOR_BOOTSTRAP_403.md)
- [Project explanation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PROJECT_ANALYSIS.md)
- [Semantic project comparison](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/SEMANTIC_PROJECT_DIFF.md)
- [Modernization advice](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/MODERNIZATION_ADVISOR.md)
- [Product-version comparison](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PEKAT_VERSION_CAPABILITY_DELTA.md)
- [Log diagnosis](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/LOG_DIAGNOSTICS.md)
- [Training history](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/TRAINING_HISTORY_DIAGNOSTICS.md)
- [HTTP output](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/HTTP_OUTPUT_403.md)
- [Cross-project communication](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CROSS_PEKAT_403.md)
- [REST, SDK and communication](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/REST_SDK_CROSS_PEKAT.md)
- [Projects and operator presentation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PROJECTS_OPERATOR_STATISTICS.md)
- [Troubleshooting](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/TROUBLESHOOTING.md)
- [Version-aware reasoning](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/VERSION_ROUTING.md)
- [Basler to PEKAT](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/bridges/BASLER_PEKAT_BRIDGE.md)
- [IFM IO-Link to PEKAT](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/bridges/IFM_IOLINK_PEKAT_BRIDGE.md)
- [KEYENCE LJ-X/LJ-S to PEKAT](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/bridges/KEYENCE_LJX_PEKAT_BRIDGE.md)
- [MX-G2000 reasoning](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/bridges/MX_G2000_OPERATIONAL_ROUTE.md)

- [October decision guide and contract gaps](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md)


---

Source: `knowledge/assistant/ANOMALY_UNSUPERVISED.md`

# Anomaly learning

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Module-specific OK/NG labels differ from tags and other annotations. Unlabeled is not a confirmed negative. Evaluate representative variants; missing loss history is a limitation, not proof of quality.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/CAMERA_ACQUISITION.md`

# Camera acquisition

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Distinguish a saved PEKAT recipe, live camera features and persistent camera User Sets. Selecting a recipe does not prove the device applied every value; a live read does not prove restart persistence. Clarify stream, evaluate, save or manual capture intent. API-provider inference need not require a camera. For physical acquisition plans establish trigger source, exposure, motion, frame count, image identity and one active camera owner; inspect newly acquired images rather than only a running indicator.

Streaming, evaluation and saving are independent states. Project readiness does not prove physical acquisition, camera model or feature configuration.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/CONTEXT_CODE_GLOBALDATA.md`

# Context and shared state

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Code performs custom computation while Context carries an evaluation's data. GlobalData resets at project-server restart; it is neither durable storage nor an automatic parallel merge. Specify branch-owned keys, item identity, writers, readers, reset and stale-value rules. A previous item's valid value must not silently decide the next item. Native results, raster pixels and custom metadata need separate review. Historical 4.0.3 persistent Python state can be a legitimate cache; shared readers/writers establish a dependency, not an automatic collision.

Separate per-evaluation state from process-lifetime shared state and durable history. Restart-sensitive state needs explicit reset and ownership. Persistent Python state is not automatically defective; matching names do not prove a collision.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/CROSS_PEKAT_403.md`

# Cross-project communication

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Historical upstream evidence established a narrow embedded happy path in exact 4.0.3, not a standalone client or reconnect guarantee. Distributed decisions need item identity, freshness, timeout, duplicates and restart handling.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/DATA_MODEL_PORTABILITY.md`

# Data and model portability

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Keep original source, Image Library, native exported raster and model-package identities separate. Names can route files without proving original identity. Check dimensions and coordinate basis: upstream exported Detector rasters could differ from corresponding library rasters despite equal dimensions. Do not infer the transformation or rebuild labels against a guessed basis. Inventory tags, splits, labels, annotations and bindings individually. Clean-target transfer does not establish safe merge/reimport, partial-failure rollback or cross-version compatibility.

Image export, Detector COCO transfer and model-package transfer are separate contracts. Check archive structure, raster basis, class mapping and geometry. Names do not prove original identity; similar ZIPs are not interchangeable.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/DETECTOR_ANNOTATION_403.md`

# Detector annotation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Preserve existing annotations during insertion. First-create, additive insertion and replacement have distinct semantics. Review geometry on the correct raster. Teacher absence is not automatically a negative label.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/DETECTOR_CLASSIFIER_OCR.md`

# Detector, Classifier and OCR

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Detector answers where objects are and their classes. Classifier answers the inspected input's class/state; a winner is not an object-instance list. OCR answers text within supported region/partition semantics. Preserve these meanings rather than using one generic threshold. Record image, family/module, class/transcription, geometry and raster basis. Smart Mask proposals and accepted boxes are not the same representation. Model comparison needs a stable validation basis, variant coverage and relevant miss/false-reject objectives.

Object geometry, classification and recognition require separate annotation and training semantics. Smart Mask suggestion is not persistence; a bounding box is not a segmentation mask.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/EXTERNAL_TEACHER_DETECTOR_BOOTSTRAP_403.md`

# External teacher to native Detector

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Teacher compatibility, reviewed labels and native training success are independent gates. Preserve the original raster when labels target it. Teacher misses need not be negative labels. Historical success required saved model artifacts and selection evidence, not merely a completed label; production accuracy remained unproven.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/EXTERNAL_TORCHVISION_PTOOL_403.md`

# External-model example

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Historical exact-4.0.3 upstream evidence established local LRASPP/Torchvision CPU/CUDA inference in a PTool, raster modification and process-lifetime caching. Coverage was partial; this proves neither universal human-part recall nor privacy compliance, arbitrary model support or another-version portability. No weights are distributed.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/FLOW_AUTHORING.md`

# FLOW interpretation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Explain actual execution and branches rather than module inventory. Image raster, native results and custom state have different branch behavior. Historical Gate and native-tool evidence covered narrow subsets.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/HTTP_OUTPUT_403.md`

# HTTP output

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Historical upstream exact-4.0.3 evidence covered narrow local delivery. General retry, ordering, failure and trigger guarantees were not established. Define receiver identity, failure handling and idempotency independently.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/LOG_DIAGNOSTICS.md`

# Log diagnosis

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Correlate identity, version and timestamps. Find the first root error before repeated symptoms. Separate live state from history; redact private paths and identifiers. Log evidence grants no database repair authority.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/MODERNIZATION_ADVISOR.md`

# Modernization advice

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Preserve working semantics. A native replacement needs exact feature evidence, preconditions and a concrete benefit. Native feature availability and writer support differ. Advice is not an applied refactor or proof of runtime equivalence.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/OCR_ANNOTATION.md`

# OCR annotation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Separate region geometry, transcription and character partition. Historical upstream changes concerned an existing region; new-region authoring and external transcription service policy remained gaps. Require human review and appropriate privacy handling.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/PEKAT_VERSION_CAPABILITY_DELTA.md`

# Product-version comparison

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Compare product evidence separately from project changes. Packages, resources and frontend labels are discovery candidates, not working-feature or writer proof. Keep historical contracts version-scoped.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/PROJECTS_OPERATOR_STATISTICS.md`

# Projects and operator presentation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Separate project lifecycle, operator layouts, kiosk settings and statistics. Historical Operator evidence was Input-only; kiosk recovery remained manual. A layout does not establish an operator state machine.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/PROJECT_ANALYSIS.md`

# Project explanation

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Begin with supplied version and source state. Describe executed branches and where pixels, detections, custom state and outputs change. A retained record can be inactive history. Inventory model bindings, dependencies and shared-state readers/writers without executing Code. Review findings are not native verdicts. Explaining an unexpected NOK requires the evaluated image, active configuration and path results; stored structure alone cannot reconstruct external or asynchronous state. This preview reasons about supplied sanitized representations.

Separate executed FLOW from inventory and retained history. Unused-looking modules are not permission to delete. Review dependencies and shared state without executing supplied Code. Static findings do not establish runtime outputs.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/PTOOL_PMODULE_FORM.md`

# PTool and Form

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

PTool reusable computation and its user-facing Form must agree on key identity and value types. Displayed defaults do not prove the values used in an evaluation. Do not assume PModule and PTool packaging or lifecycle are interchangeable. Record the actual artifact, source/target builds, Form values, dependencies and representative input/output behavior. An archive does not reproduce Python ABI, external weights or device access. A successful round trip is narrow package evidence, distinct from generic native authoring.

Separate Form defaults from execution values. Tool packages do not include all third-party dependencies. Exact-version round trips establish narrow compatibility, not arbitrary portability.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/REST_SDK_CROSS_PEKAT.md`

# REST, SDK and communication

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

An independently authorized implementation should use exact official public REST/SDK documentation. Image inference differs from lifecycle and shared-state transfer; raw images need explicit dimensions/layout. Never substitute undocumented frontend events or database edits. Separate process reachability, provider readiness and inference before interpreting failure. A connection does not prove the intended model evaluated the intended frame. Embedded transfer does not establish external-client compatibility; preserve item identity and freshness.

Image inference, project lifecycle and shared-state transfer are separate operations. An independently authorized implementation should use its exact documented public interface. Connectivity is not an inspection result.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/RUNTIME_PYTHON_ML.md`

# Embedded Python and ML

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Check exact Python, ABI and dependency compatibility. Package presence, model construction, GPU visibility and actual inference are different evidence. Propose bounded checks instead of assuming arbitrary installations are compatible.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/SEMANTIC_PROJECT_DIFF.md`

# Semantic project comparison

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Match conceptual roles using multiple signals, not IDs alone. Separate structural facts from inferred behavior and preserve ambiguous matches. A clean static comparison cannot prove timing, model quality or output equivalence.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/SUPERVISED_MASK_LIFECYCLE.md`

# Supervised masks

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Review image/module/class identity and preserve unrelated masks. Supervised annotation, Detector Smart Mask and static FLOW Mask are separate. Historical training evidence concerned a selected variant, not every backend.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/TRAINING_HISTORY_DIAGNOSTICS.md`

# Training history

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

## Practical guidance

Separate run identity, split provenance, status, saved artifacts, selected model and validation outcome. Connect these identities durably rather than relying on terminal status. Families differ: some upstream examples lacked per-step history and some Supervised columns had unknown meanings. Keep unknown columns unknown and binary weights inventory-only. Compare iterations on stable validation data and the inspection objective; error buckets and variant coverage matter. Historical training completion does not prove production quality.

Preserve family-specific run identity, data provenance, status and saved artifacts. Do not invent undocumented metric meanings or compare incompatible validation sets. Completed status without saved weights is insufficient.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/TROUBLESHOOTING.md`

# Troubleshooting

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Identify exact target and symptom. Separate readiness, source state, acquisition, evaluation, model loading and delivery. Choose the smallest discriminating check; stored configuration is not current runtime proof.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/VERSION_ROUTING.md`

# Version-aware reasoning

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Start with the installed build. Keep common conceptual advice separate from exact observations. Earlier-version success is a hypothesis for another target, not inherited authority.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/assistant/VISION_DESIGN.md`

# Inspection design

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Define defect semantics and measurable acceptance first. Establish field of view, pixels per feature, lighting contrast, motion blur and triggering before selecting a tool. A plausible FLOW is not physical validation.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/bridges/BASLER_PEKAT_BRIDGE.md`

# Basler to PEKAT

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Identify exact camera, interface, acquisition mode and SDK version. Camera features and provider readiness differ. Area/line scan and encoder behavior require exact-model evidence. No physical acquisition or persistent device changes are validated by this bridge.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/bridges/IFM_IOLINK_PEKAT_BRIDGE.md`

# IFM IO-Link to PEKAT

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Identify master, port, device, firmware and IODD. Preserve direction, scaling, special values, quality and freshness. Transport success does not prove physical meaning. The advisory bridge includes no device/master writer.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/bridges/KEYENCE_LJX_PEKAT_BRIDGE.md`

# KEYENCE LJ-X/LJ-S to PEKAT

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Keep LJ-X8000, LJ-X8000A and LJ-S8000 distinct. Separate command response, scalar measurement and profile data. Preserve validity and freshness. Program selection is not creation; catalog repeatability is not application accuracy. No controller transport is included.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `knowledge/bridges/MX_G2000_OPERATIONAL_ROUTE.md`

# MX-G2000 reasoning

Version scope: advisory; historical runtime observations exact 4.0.3 only.
Evidence level: original synthesis of curated upstream evidence; no new runtime test.
Known limitations: no included runtime controller, parser, writer or hardware acceptance.

Establish platform identity, PEKAT version and symptom. Separate host/process/network trouble from provider readiness and FLOW. Do not infer unobserved hardware status or recovery requirements. Service and I/O changes need separate exact procedures.

Scope: advisory public rewrite. Runtime conclusions refer only to bounded historical upstream evidence, principally exact PEKAT VISION 4.0.3. No runtime tool or hardware validation is included.


---

Source: `docs/ARCHITECTURE.md`

# Architecture

Human documentation, topic-oriented knowledge and a Codex skill share the same advisory boundaries. Custom GPT guidance uses curated public knowledge. Packaging produces standalone views and adds no control capability.

The skill follows intent → exact version/model → relevant topic → evidence-qualified advice. Device-specific facts belong to reviewed specialist sources; PEKAT reasoning maps valid, fresh information into an inspection design.

Historical upstream analysis and accepted changes used separate interfaces. This preview publishes concepts, not those parsers, controllers or contracts. See [Evidence model](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/EVIDENCE_MODEL.md).

## Control architecture concept

```text
User / chat / agent
       |
PEKAT Assistant knowledge + capability routing
       |
Typed Core + safe transaction boundary
       |
Supported, exact-version PEKAT interfaces
       |
PEKAT VISION
```

The public preview supplies the knowledge and routing layer. The lower control
layers describe an engineering architecture; they are not included dependencies.
A typed operation constrains target identity, parameters, preconditions and
expected readback. Knowledge that an operation exists is separate from permission
and a supported executable implementation for that exact version.

For an independently supplied and authorized control implementation, use
inspect → plan → bounded action → durable readback → verify, with restoration
of temporary state where supported. A transaction cannot guarantee crash recovery
or physical safety merely because its normal path was tested. Human approval and
site policy remain an explicit boundary for target, side effects and deployment.

A future official PEKAT MCP could be a transport/adapter over this same typed
boundary. It is a possible future integration, not a current dependency or a
claim that an official MCP is available. Chat, voice or a different transport
must preserve the same capability and policy boundaries.

Version scope: architecture concept; historical runtime conclusions exact 4.0.3.
Evidence level: curated engineering synthesis, not a new runtime verification.
Known limitations: no public controller, generic writer or crash-recovery engine.


---

Source: `docs/CAPABILITIES.md`

# Capabilities

## Included preview scope

Advisory inspection design, supplied project/FLOW explanation, annotation/dataset review, training evidence interpretation, comparison, modernization planning and integration boundaries. Includes knowledge, a Codex skill and GPT instructions.

## Historical upstream evidence

Exact-4.0.3 upstream work established bounded project/source lifecycle, camera capture, selected FLOW authoring, Code/PTool/Form, image/tag handling, family-specific ML lifecycles, additive Detector rectangles and Smart Mask-to-bbox proposals, HTTP delivery, embedded cross-project state transfer and Operator Input layouts. None of those controllers or writers is included here.

Narrow FLOW evidence covered CUT, static Mask, one-object Unifier, universal X-axis Line Find, Euclidean Relation Measure and boolean Conditional Gate. It does not establish whole-family coverage. ML families had separate identity, annotation, status, artifact and selection contracts.

Upstream read-only tools covered project explanation, semantic comparison, modernization advice, logs and training history. This preview publishes concepts rather than those parsers.

## Gaps

No generic database/store/event writer, arbitrary configuration/module change, general annotation bulk deletion, generalized Detector Stop/model deletion, Kiosk writer, auto-deployment, arbitrary external-model compatibility, complete reconnect orchestration or physical device acceptance.

[User scenarios](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/USER_SCENARIOS.md) retain available/partial/planned/future distinctions. Historical runtime conclusions are narrow exact-4.0.3 upstream evidence.

## Capability status table

Version scope: historical upstream exact 4.0.3 where stated. Evidence level: curated upstream summary, not new execution. Public functionality is advisory only.

| Capability | Version | Evidence status | Public status | Current limitation |
|---|---|---|---|---|
| Vision design | Conceptual | KNOWLEDGE_ONLY | KNOWLEDGE_ONLY | Physical acceptance remains application-specific |
| Project explanation/comparison | Observed versions | PARTIAL | KNOWLEDGE_ONLY | No parser or runtime equivalence proof |
| Source/capture/FLOW subsets | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | KNOWLEDGE_ONLY | No controller or writer |
| Family-specific ML | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | KNOWLEDGE_ONLY | No annotation/training runner; partial family coverage |
| HTTP/cross-project transfer | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | KNOWLEDGE_ONLY | No sender; general failure/reconnect unknown |
| External PTool model example | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | KNOWLEDGE_ONLY | One architecture/checkpoint; partial coverage |
| Hardware bridges | Exact identity required | KNOWLEDGE_ONLY | KNOWLEDGE_ONLY | No transport or physical acceptance |
| Active learning/annotation review | Upstream roadmap | PLANNED | PLANNED | No completed workflow |
| Voice/multimodal/closed loop | Future vision | PLANNED | UNSUPPORTED | Not an included feature |
| Generic DB/store/event writer | Any | UNSUPPORTED | UNSUPPORTED | Intentionally absent |

## October advisory update

[Decision guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md) adds exact-4.0.3 state/freshness boundaries and short intent routing. No executable capability or writer authority is added.


---

Source: `docs/EVIDENCE_MODEL.md`

# Evidence model

| Evidence | Supports | Limit |
|---|---|---|
| Official documentation | Vendor-described behavior in stated scope | Does not prove local execution |
| Supplied observation | What the user observed | May be incomplete or stale |
| Static evidence | Structure, configuration or resource presence | Does not establish runtime behavior or writer support |
| Historical runtime evidence | A bounded upstream execution | Only the tested exact build/case |
| Inference | An explanation consistent with evidence | State uncertainty and a discriminating check |
| Unknown | Missing or contradictory information | Preserve the gap |

Native product features, upstream implemented tools and included preview features are separate claims. This preview includes advisory content only.

Distinguish proposals, authorization, acknowledgement, durable readback and verified outcome. Progress 100, a completed label or GPU visibility alone cannot establish saved model artifacts, inference or inspection quality.


---

Source: `docs/VERSION_SUPPORT.md`

# Version support

This preview provides version-aware advice, not executable support certification. Historical upstream runtime evidence principally concerns exact PEKAT VISION 4.0.3. Retained 4.0.1 and observed migration comparisons provide context only.

Do not inherit writer, package, model or schema behavior across patches by name. Establish the exact build and separate conceptual guidance from observed behavior. Future versions require fresh target-specific evidence.

Project comparison and product capability comparison answer different questions. Neither proves runtime equivalence or authorizes an upgrade. No live PEKAT version was tested by this preview.


---

Source: `docs/USER_SCENARIOS.md`

# User scenarios

These statuses describe the historical upstream requirements catalog, not tools included in this preview. The public pack can advise from supplied evidence; it cannot execute these workflows.

- `AVAILABLE_NOW`: a verified narrow upstream capability existed.
- `PARTIALLY_AVAILABLE`: useful pieces existed, with explicit end-to-end gaps.
- `PLANNED`: a product goal without a completed workflow.
- `FUTURE_VISION`: depended on later interfaces, hardware, history or multimodal development.

| ID | Goal | Historical upstream status |
|---|---|---|
| US-02 | Understand a new inspection problem | PARTIALLY_AVAILABLE |
| US-03 | Explain an existing PEKAT project | PARTIALLY_AVAILABLE |
| US-04 | Safely modify FLOW | PARTIALLY_AVAILABLE |
| US-05 | Capture a bounded image set | AVAILABLE_NOW |
| US-06 | Dataset audit before training | PARTIALLY_AVAILABLE |
| US-07 | Select useful images | PLANNED |
| US-08 | Bootstrap Detector | PARTIALLY_AVAILABLE |
| US-09 | Teach by pointing | FUTURE_VISION |
| US-10 | Teach OK/NOK state | PLANNED |
| US-11 | Correct target conversationally | FUTURE_VISION |
| US-12 | Smart Mask proposal | PARTIALLY_AVAILABLE |
| US-13 | Automatic Annotations review | PLANNED |
| US-14 | Compare model iterations | PARTIALLY_AVAILABLE |
| US-15 | Champion/challenger deployment | PARTIALLY_AVAILABLE |
| US-16 | Preprocessing experiment | PARTIALLY_AVAILABLE |
| US-17 | Training campaign | PARTIALLY_AVAILABLE |
| US-18 | Stop iterating | FUTURE_VISION |
| US-19 | External multimodal OCR annotation | PARTIALLY_AVAILABLE |
| US-20 | OCR error mining | PARTIALLY_AVAILABLE |
| US-21 | Diagnose gradual degradation | FUTURE_VISION |
| US-22 | Shared confidence loss | FUTURE_VISION |
| US-23 | Explain unexpected NOK | PARTIALLY_AVAILABLE |
| US-24 | Manual production feedback | PLANNED |
| US-25 | Retrospective defect search | FUTURE_VISION |
| US-26 | Production sampling | FUTURE_VISION |
| US-27 | Voice tag data | PARTIALLY_AVAILABLE |
| US-28 | Voice review dataset | FUTURE_VISION |
| US-29 | Voice FLOW change | PARTIALLY_AVAILABLE |
| US-30 | Operator next-step guidance | PLANNED |
| US-31 | Multi-step assembly | PLANNED |
| US-32 | Distributed vision process | PARTIALLY_AVAILABLE |
| US-33 | Multi-camera aggregate result | FUTURE_VISION |
| US-34 | External sensor Gate | PLANNED |
| US-35 | TCP measurement plus camera | PLANNED |
| US-36 | Preserve clean image and native results | PARTIALLY_AVAILABLE |
| US-37 | Selective NOK/borderline collection | PARTIALLY_AVAILABLE |
| US-38 | Whole system health | FUTURE_VISION |
| US-39 | Compare one camera | FUTURE_VISION |
| US-40 | Bounded camera optimization | FUTURE_VISION |
| US-41 | Embedded Python compatibility | PARTIALLY_AVAILABLE |
| US-42 | Closed-loop vision lifecycle | FUTURE_VISION |
| US-43 | Safe refusal | AVAILABLE_NOW |
| US-44 | Exact-version boundary | AVAILABLE_NOW |

Full output reconstruction, arbitrary rewiring, automatic annotation review, comparative deployment, reconnect/freshness orchestration, voice/visual grounding and durable multi-camera history remain incomplete goals. Narrow atomic evidence does not establish a complete scenario. See [Capabilities](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/CAPABILITIES.md).

## Representative advisory workflows

| Scenario | Sanitized prerequisite | Useful public output | Remaining boundary |
|---|---|---|---|
| US-03 Explain a project | Exact version and supplied FLOW/Code/result description | Execution and decision map with unknowns | Supplied inventory alone does not reconstruct all outputs or persistent state |
| US-05 Capture images | Selected ready project and camera; capture policy | Checklist for a bounded image set and identity/readback | Historical 4.0.3 capture evidence does not provide a public capture tool |
| US-08 Bootstrap Detector | Reviewed seed labels and original image basis | Seed/geometry/training/artifact checklist | Full automatic review, retraining and comparison loop remains partial |
| US-12 Smart Mask proposal | Target and reviewed proposal geometry | Explain suggestion versus accepted annotation | Suggestion is not a persisted annotation or an accuracy guarantee |
| US-23 Explain unexpected NOK | Matched image, evaluated results and acceptance rule | Evidence-based hypothesis and smallest discriminating check | A screenshot or static module list cannot establish the full decision path |
| US-34 External sensor Gate | Exact device data, units, identity and freshness rules | PEKAT integration design with invalid/stale handling | Complete sensor-to-Gate execution is planned, not provided |
| US-41 Python compatibility | Exact embedded build, ABI and candidate package | Compatibility assessment and bounded import-test proposal | Arbitrary package installation is not automated |

Version scope: source catalog snapshot with narrow historical 4.0.3 evidence.
Evidence level: reconciled requirements and curated capability conclusions.
Known limitations: catalog statuses are historical upstream statuses; this public
preview provides advice rather than executing those workflows.

## Short Czech and English intents

Use the [decision guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md) for ten practical intents, preflight/readback questions and unsupported variants. Workflow names describe separately authorized upstream implementations; this edition provides advice only.


---

Source: `docs/SPECIALIST_SKILLS.md`

# Specialist skills

Specialist sources are optional; no hardware skill or transport is bundled. Use a separately reviewed specialist or exact official documentation for device facts.

| Domain | Required identity | Boundary |
|---|---|---|
| Basler | Model, interface, pylon/pypylon version | Camera features differ from PEKAT provider state |
| IFM / IO-Link | Master, port, device, firmware, IODD revision | Preserve scaling, validity, quality and freshness |
| KEYENCE | Controller family, head, operating mode | LJ-X8000, LJ-X8000A and LJ-S8000 remain distinct |
| MX-G2000 | Platform identity and PEKAT version | Host/service state differs from FLOW |

A reference does not authorize triggering, reset, program changes, firmware, process-data writes or persistent settings. See [bridge topics](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/INDEX.md).

Reviewed optional public sources:

- [Basler](https://github.com/CZPavel/codex-skill-basler-cameras), snapshot `6ccc9c09845effb5d746041696e556fee7f6b64a`.
- [IFM IO-Link](https://github.com/CZPavel/codex-skill-ifm-io-link), snapshot `4bb94a1910cf71207953c39825acd52b875d21de`.
- [KEYENCE LJ-X/LJ-S](https://github.com/CZPavel/keyence-ljx-s-skill), snapshot `b5c39334479f93109cf2c7283f36e97294dac210`.

Each source has its own MIT license and independent scope. Review upstream changes before replacing these snapshots. The historical legacy PEKAT skill is not the default route.


---

Source: `knowledge/assistant/DECISION_GUIDE_403.md`

# PEKAT 4.0.3 decision guide — October update

This advisory card summarizes sanitized upstream observations from 2026-10-09. It distributes no runtime controller. Current official PEKAT 4.x documentation, exact-4.0.3 observations and offline recipes are separate evidence classes; none grants execution authority.

## Choose the function before the tool

Interpret short Czech or English requests by the object, intended result and variant, even when word order or accents differ. Prefer an existing closed workflow in an separately installed authorized controller. This package can explain its preconditions and checks; it cannot execute it. Confirm exact version, required arguments, project state, side effects, preflight and readback before proposing execution.

| Request / intent | Advisory route | Boundary and useful check |
|---|---|---|
| Smaž jen tento detekovaný obdélník / delete one rectangle | Detector annotation editor | Generic delete-by-ID/relabel writer remains a contract gap. Image-wide clear is a different operation; never substitute it. |
| Ulož snímek s heatmapou / save with heatmap | Image Saver overlay/heatmap settings | Documentation describes this option; no public writer. Verify the saved raster, not just preview appearance. |
| Ulož originální snímek bez heatmapy / save original | Acquisition image and Image Saver | Original, current raster and overlay-free output can differ after crop/scale. Require explicit image provenance. |
| Kamera je vypnutá, proč nejde FLOW? / camera off | Camera acquisition preconditions | Live Stream OFF can coexist with service OPEN. Explain the state mismatch; do not bypass the FLOW guard. |
| Přidej filtr pro zvýšení kontrastu / add contrast | Preprocess GUI | Sixteen GUI choices were observed; upstream writer is CUT-only. Contrast writer is a gap. |
| Vyřízni oblast podle součástky / crop detected part | Unifier or explicit crop recipe | Accepted upstream one-object contract is narrow. Rotation/multi-anchor behavior remains unverified. |
| Neukládej snímek pod předchozím názvem / avoid stale name | Context freshness and Image Saver | Carry current frame identity with results; reject missing/stale identity. JPEG/JSON atomic pairing remains unproven. |
| Spusť analýzu jednoho snímku přes API / analyze one image | Closed single-image analysis workflow | Prefer that workflow over improvised calls where a verified controller exists. Validate response identity and inspection outcome separately from transport success. |
| Přidej vstupní hodnotu do Operator View / Operator input | Closed Operator Input workflow | Identify name, type, default and ownership; compare configured and runtime values. Public pack offers guidance only. |
| Vyhodnoť vítěznou třídu / Classifier winner | Classifier decision semantics | Use the winning class and threshold; label presence in a candidate list is insufficient. |

## State and image evidence

Context describes the evaluated frame; GlobalData is shared process-lifetime state. Restart resets process-lifetime state and does not make it durable. Initialize/reset frame-local collectors, attach current frame identity and reject missing or stale inputs. Two sequential upstream evaluations had internally consistent identities; this does not establish concurrent correctness or atomic output persistence.

Image pixels, native overlays/results and custom Context are independent channels. A final raster can have no native overlay while custom results still describe the original image. A heatmap preview is not proof that a saved raster includes heatmap pixels. Check each requested channel explicitly.

An offline axis-aligned crop/scale fixture verified bbox restoration and raster bounds within one pixel. Store crop origin and independent x/y scale with the result. This does not validate rotation, perspective, native Unifier/Parallelism transforms, percentage annotations or physical metrology.

## Product, upstream and public support

Current official 4.x prose describes broader Unifier and Detector GUI behavior than the narrow accepted upstream 4.0.3 writer contracts. Preserve the one-object Unifier limit and annotation editor versus generic writer distinction. Preprocess GUI/schema observation proves discoverability, not every filter's runtime behavior.

A completed, saved, selected Detector model was observed upstream. No independent test dataset was available for that observation. Training completion, artifact presence, selection and generalization are four separate claims. Request independent representative validation before judging production quality.

Image Saver documentation describes all/OK/NG filtering, Context JSON, overlay/heatmap, Local/FTP and naming options. Sequential identity checks support a bounded freshness conclusion only. Pair image and JSON by explicit identity and account for partial writes; concurrency, crash recovery and atomic pairing remain open gaps.

No new native writer capability was promoted by the October mapping. The public edition contains this explanation, references and offline validation tooling; it contains no controller, private Core, raw evidence or hardware operation. Deterministic private routing tests are not a live small-model evaluation. SMALL_MODEL_LIVE_EVAL_NOT_RUN applies unless a separately recorded model run establishes otherwise.
