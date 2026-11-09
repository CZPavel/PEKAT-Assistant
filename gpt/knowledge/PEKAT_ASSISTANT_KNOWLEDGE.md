# PEKAT Assistant public knowledge

Generated from canonical public sources; do not edit.


---

Source: `knowledge/INDEX.md`

# Knowledge index

Original advisory topics; no vendor manuals or runtime controller. Historical observations retain exact-version limits.

Start with the [practical domain guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_DOMAIN_GUIDE.md) for purpose, scenario, inputs, native functions, Assistant role and automation limits. See the [seven public capability classes](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification) and [version evidence matrix](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/VERSION_MATRIX.md) before treating a historical observation as current capability.

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

## Current bounded support — 2026-10-23

Exact 4.0.3 upstream C1 accepts ID-specific relabel, move, resize, stored-anchor rotation and delete of an existing Detector rectangle. Require an explicit existing rectangle ID, fresh preimage, sibling preservation and independent readback. Last-object deletion persists PRESENT_EMPTY, not ABSENT. Image-wide Clear and compatibility replacement are different operations. This advisory package includes no writer.


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

## User-guided functional design

Evidence: general design advice and a synthetic illustration. This public pack has no candidate validator, runtime integration or writer. Patterns are recommendations, not mandatory module templates.

Start with the user goal and functional hierarchy: whole object, regions, checks, dependencies and local/final outcomes. Preserve an explicitly supplied hierarchy where practical. If none is given, propose understandable groups and proceed when sufficient facts are known; clarification is not a compulsory approval gate. Explain departures using concrete dependencies, shared localization/inference, image transforms, copying cost, latency, uncertain joins or a more suitable native operation.

Reason from goal to functional groups, dependencies, image domains, native/Code operations, useful branches, results and final image. Keep observed execution topology separate from every recommended alternative. Module inventory does not establish execution order.

## Native-first alternatives and shared inference

Compare sequential, branched and hierarchical alternatives. Prefer suitable native operations when they simplify design, preserving requested or necessary Code. Conditional Gate may replace simple custom decisions only after exact-version semantics and equivalence are established. Parallelism may reduce auxiliary Code for image handling or native-result forwarding; branch count is not an optimization target.

Keep shared inference as one producer where input domain and requirements permit. Different preprocessing may justify a separate image branch without repeating shared inference. Explain rejected alternatives and tradeoffs: synchronization, Context ownership after joining, large-image copies, latency, module count and technician readability. Do not invent an empty branch as proof that the original image survives.

## Image, result and visualization lineage

Describe separately:

- Original capture, each transformed/preprocessed raster and coordinate mapping.
- Raster consumed by every check and the expected transfer at every join.
- Native result provenance, local decisions and the final result collector/report.
- Custom Context ownership, validity and freshness, separate from native results.
- Final raster, native overlays and custom annotation rendering, including mapping to original coordinates.

Merging decisions does not prove image merging or overlay transfer. A structurally consistent design proves neither runtime acceptance, model quality nor writer authority. Missing exact-version join/image/Context/overlay behavior remains an explicit open gap. Recommend the smallest separately authorized per-frame experiment that distinguishes competing behaviors; this advice does not execute it.

## Synthetic example

A fictional fixture has an upper symbol group and a lower fastener group. Preserve those user-facing groups, localize once and propose one shared object inference. One check consumes native results; another needs a contrast-adjusted raster. Discuss a separate preprocessing branch without automatically duplicating inference. Attribute each result to its producer and raster. Collect OK/NOK/UNKNOWN decisions explicitly.

For visualization in original coordinates, name the original capture as the intended final raster, record every transform and map annotations back before rendering. Whether raster and native overlays survive a particular join remains unverified until tested on the exact version. A sequential alternative may be simpler when branching adds copies or uncertain joins. Explain the choice; no project is changed.

## Current bounded support — 2026-10-23

Exact 4.0.3 C1 accepts editing an existing BRIGHTNESS_CONTRAST item: brightness integer -255..255 and finite contrast 0.01..4, preserving siblings. This is distinct from PREPROCESS CUT and Contrast equalisation. Arbitrary filter creation/chains remain outside this subset.

Conditional Gate accepted variants are Boolean EQUAL, finite numeric GlobalData comparisons, nested AND/OR Context/Result groups, and D1 Rectangle COUNT with strict integer operands and Any/Every/Together selectors. The historical float COUNT failure does not exclude that integer subset. Other Rectangle properties and explicit classes remain excluded. This package supplies advisory knowledge, not execution authority.


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

## Current bounded support — 2026-10-23

The historical existing-region-only observation above is superseded within the exact 4.0.3 C1/C2 authoring subset: region creation/deletion, normalized geometry, length-changing transcription, initial N-character partition and separator editing. Preserve whole-string rectangle → transcription → split-to-characters → boundary adjustment. Require fresh preimage, sibling preservation and readback. E1.1 center-preserving rotation at fixed geometry does not prove arbitrary interactive drag. External transcription privacy and service policy remain separate. No public writer is included.


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

Version scope: historical 3.19.3 migration lineage, exact 4.0.1 and 4.0.3 evidence anchors, and advisory routing for other versions.
Evidence level: original synthesis of retained upstream conclusions; no new runtime test or included runtime controller.

Start with the installed version/build and the user's task. Use shared 4.0.x conceptual knowledge before looking for a relevant exact delta; an exact observation does not imply that every other patch differs. Runtime/schema compatibility and writer acceptance still require their own evidence.

- **3.19.3:** controlled migration lineage informs comparison with a migrated 4.0.1 fixture. It is not a universal migration guarantee or a reason to restore historical database data.
- **4.0.1:** generated FLOW/Classifier and tested-machine embedded Python/ML observations remain useful in their original scope. Distinguish package presence, import, functional compute, model construction and inference; locally added packages are not clean-install features.
- **4.0.3:** principal bounded runtime evidence for selected workflow/tool families. Narrow success does not establish arbitrary variants, physical acceptance or another patch's writer support.
- **Other versions:** continue explanation, design and drafts using explicitly labeled candidate evidence; identify the smallest relevant compatibility check. Missing execution authority need not block advisory work.

Use [KB4](https://pekatvision.atlassian.net/wiki/spaces/KB4/overview?homepageId=1512243624) as the primary official functional documentation route for 4.x, preserving page scope/revision. Documentation, static/offline inspection, runtime observation and execution authority are different claims. A static project comparison does not prove equal timing, accuracy or OK/NOK behavior.

See the [version evidence matrix](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/VERSION_MATRIX.md) for concrete retained scopes and the [public capability classes](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification) for availability. This public edition supplies advice and publication utilities; it does not distribute a PEKAT or device writer.


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

Advisory inspection design, supplied project/FLOW explanation, annotation/dataset review, training evidence interpretation, comparison, modernization planning and integration boundaries. Includes knowledge, a Codex skill, a portable plugin RC and GPT migration guidance.

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
| Vision design | Conceptual | KNOWLEDGE_ONLY | PUBLIC_KNOWLEDGE | Physical acceptance remains application-specific |
| Project explanation/comparison | Observed versions | PARTIAL | PUBLIC_KNOWLEDGE | No parser or runtime equivalence proof |
| Source/capture/FLOW subsets | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | PUBLIC_KNOWLEDGE | No controller or writer |
| Family-specific ML | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | PUBLIC_KNOWLEDGE | No annotation/training runner; partial family coverage |
| HTTP/cross-project transfer | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | PUBLIC_KNOWLEDGE | No sender; general failure/reconnect unknown |
| External PTool model example | Historical 4.0.3 | VERIFIED_NARROW_SUBSET | PUBLIC_KNOWLEDGE | One architecture/checkpoint; partial coverage |
| Hardware bridges | Exact identity required | KNOWLEDGE_ONLY | PUBLIC_KNOWLEDGE | No transport or physical acceptance |
| Active learning/annotation review | Upstream roadmap | PLANNED | PLANNED | No completed workflow |
| Voice/multimodal/closed loop | Future vision | PLANNED | UNSUPPORTED | Not an included feature |
| Generic DB/store/event writer | Any | UNSUPPORTED | UNSUPPORTED | Intentionally absent |

## October advisory update

[Decision guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md) adds exact-4.0.3 state/freshness boundaries and short intent routing. No executable capability or writer authority is added.

## FLOW design advice

The public knowledge explains user-guided functional grouping, native-first topology alternatives, shared inference and separate image/result/overlay lineage. It offers synthetic examples and reasoning guidance. Private offline candidate-validation implementation is not shipped here; no public automated validator, runtime acceptance or FLOW writer is implied. See [FLOW guidance](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/FLOW_AUTHORING.md).


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

This advisory card separates current bounded support (2026-10-23) from the historical 2026-10-09 checkpoint. The older table below preserves historical gaps, not current blanket prohibitions. It distributes no runtime controller. Current official PEKAT 4.x documentation, exact-4.0.3 observations and offline recipes are separate evidence classes; none grants execution authority.

## Current bounded support and routing — 2026-10-23

The historical table below preserves the 2026-10-09 checkpoint. Later exact 4.0.3 accepted subsets qualify its historical gaps: [ID-specific Detector edits](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DETECTOR_ANNOTATION_403.md), [Brightness/Contrast and Gate variants](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/FLOW_AUTHORING.md), and [OCR region authoring](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/OCR_ANNOTATION.md). Brightness/Contrast is distinct from Contrast equalisation; a crop never substitutes for either.

| Current exact-4.0.3 subset | Accepted boundary in the separately authorized Assistant |
|---|---|
| Detector ID-specific edit | Existing rectangle ID: relabel/move/resize/stored-anchor rotate/delete; fresh preimage and sibling preservation. Last-object deletion is PRESENT_EMPTY, not ABSENT. Image-wide Clear is a different operation. |
| Brightness/Contrast | Edit an existing BRIGHTNESS_CONTRAST item: brightness integer -255..255, finite contrast 0.01..4. Filter creation/chains and Contrast equalisation are outside this subset; PREPROCESS CUT is different. |
| OCR authoring | Region creation/deletion, geometry, transcription, character partition and separator editing. Arbitrary interactive drag remains unaccepted. |
| Conditional Gate | Boolean EQUAL, finite numeric GlobalData comparisons, nested AND/OR Context/Result groups, strict integer Rectangle COUNT Any/Every/Together; other Rectangle properties and explicit classes remain excluded. |

These are bounded upstream accepted contracts. This public package contains no runtime controller or writer and grants no execution authority.

Prefer an existing closed workflow matching the requested outcome. Intent recognition is read-only and grants no writer authority. Confirm exact version, capability state, parameter schema, preflight and explicit authorization in the separately installed controller. Negated, ambiguous, unknown or unsupported requests must remain classified gaps; never substitute a similar destructive action.

Knowledge lookup must prefer applicable current evidence over explicitly superseded evidence while retaining history and do_not_repeat. Follow multi-step supersession only within matching version/contract/evidence scope. Cycles, conflicting relations or unclear scope require an explicit unresolved result rather than an inferred promotion. A newer date alone is insufficient.

## Choose the function before the tool

Interpret short Czech or English requests by the object, intended result and variant, even when word order or accents differ. Prefer an existing closed workflow in an separately installed authorized controller. This package can explain its preconditions and checks; it cannot execute it. Confirm exact version, required arguments, project state, side effects, preflight and readback before proposing execution.

## Historical checkpoint — 2026-10-09

The following table records the earlier checkpoint only. Its Detector delete/relabel and Contrast gap statements are qualified by the current bounded support above; use that current section for accepted exact-4.0.3 subsets.

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


---

Source: `docs/PUBLIC_CAPABILITY_GUIDE.md`

# Public PEKAT Assistant — capabilities and practical use

Updated: 2026-11-09. This guide describes the **public knowledge edition**. It is not a statement that a live PEKAT installation or private development runtime is available to the reader.

## Product editions and what is actually available

| Edition | Available to a public user | What it does not imply |
|---|---|---|
| This PEKAT Assistant repository | Curated guidance, examples, decision rules, public skill instructions and GPT knowledge package | No included PEKAT runtime controller or automatic project/device operations |
| Standalone PEKAT Vision Codex skill | Knowledge plus bundled **offline** diagnostic and validation scripts, subject to their version and input constraints | No automatic live edits, model training, camera operation or PLC control |
| Separately developed Assistant application | Historical and current bounded development evidence for chat, project context, analytical tools and guarded operations | Not part of this repository and **not** a publicly released Windows installer |
| Future integration | Potential official interfaces, reviewed workflows, additional providers and richer user interaction | No promised release date or implied permission to perform operations |

The public knowledge edition may explain how to use functions available in PEKAT VISION itself without having a programmatic tool that can invoke those functions. A PEKAT product feature, an implemented private tool and a shipped public capability are three separate claims.

## What the Assistant helps you do

| Area | Public use | Expected result |
|---|---|---|
| Design an inspection | Clarify the inspected feature, OK/NOK rules, image visibility, optics, light, trigger and minimal proof of concept | Testable inspection concept with assumptions and acceptance checks |
| Choose vision methods | Compare classical CV, geometry, Detector, Classifier, anomaly detection, surface detection, OCR and combinations | Justified method and dataset approach rather than a default model choice |
| Design FLOW | Explain sequential and parallel processing, Conditional Gates, image/overlay/result handling and shared state | Human-readable functional hierarchy and version-scoped FLOW proposal |
| Write Code, Form or PTool | Draft readable, parameterized code and declare inputs, outputs, errors and dependencies | Reviewable script/module proposal with a validation checklist |
| Understand an existing application | Interpret **user-provided, sanitized** FLOW, configuration, outputs and observations | Explanation of intent, dependencies and probable behavior, with unknowns identified |
| Improve or compare projects | Compare user-visible behavior and proposed changes; avoid replacing working logic without evidence | Minimal-change plan and required regression checks |
| Understand datasets and models | Evaluate dataset coverage, class/label quality, model-selection evidence, training history and portability requirements | Data-quality and model-review findings; no invented training success |
| Troubleshoot | Correlate version, acquisition, selected image, evaluation, logs, model state and output behavior | Ranked hypotheses with a low-risk test and expected observations |
| Image/result delivery | Explain filename provenance, image coordinates, annotations, overlays, local saving and incomplete deliveries | Consistency and freshness checks rather than unverified delivery claims |
| Industrial integration | Design bounded REST/SDK, camera, sensor, IO-Link and cross-system workflows | Integration responsibilities, ownership, timeouts and failure states |

All advice is tied to the stated PEKAT version, module or device identity and the evidence actually provided. Observations from 3.19.3, 4.0.1 or 4.0.3 are not automatically universal.

## Six practical user scenarios

### 1. New inspection in a few steps
**Ask:** "Check whether an assembled part is correctly seated. I have two example images."
**Assistant route:** define measurable defect and false-reject risk → check image quality and pose variation → compare camera/lighting/trigger options → compare native tools and model families → propose the smallest trial and acceptance set.
**Deliverable:** inspection concept, likely FLOW, required images and objective success criteria.

### 2. Explain a complex FLOW
**Ask:** "Why does this evaluation report NOK even though the object was detected?"
**Route:** use the supplied version and FLOW diagram → distinguish detection from decision logic → verify Gate conditions and result aggregation → separate image pixels, visual overlays and shared values → propose one discriminating test.
**Deliverable:** cause candidates and a safe diagnostic sequence.

### 3. Draft a Code or PTool module
**Ask:** "Create a parameterized computation for a measured distance and publish the result."
**Route:** declare Context/Form inputs, units and frame of reference → use a version-correct entry point → handle missing inputs explicitly → keep result and visualization outputs distinct → provide a small test.
**Deliverable:** editable code and an implementation checklist, not a claim of successful live deployment.

### 4. Diagnose inconsistent image filenames or outputs
**Ask:** "A saved image seems to have the previous image's identifier."
**Route:** identify input source and filename origin → check per-frame freshness and shared-state reuse → inspect save conditions and destination ownership → compare the image with its evidence metadata.
**Deliverable:** focused tests to separate naming, state-carryover and delivery failures.

### 5. Review Detector, Classifier or OCR results
**Ask:** "The predicted label appears in the class list but the Gate chose another output."
**Route:** establish the model family and representation → distinguish a Detector object class from a Classifier winner and other candidates → inspect threshold/ordering and confidence → verify exact-version behavior.
**Deliverable:** corrected logic or a bounded verification proposal.

### 6. Combine vision and an external measurement
**Ask:** "Use a distance sensor or line profile in an inspection decision."
**Route:** identify exact hardware and transport → define measurement time/quality/units → align it with the current frame and coordinate reference → distinguish stale, unknown and failed measurement states → map to a safe OK/NOK/REVIEW decision.
**Deliverable:** acquisition and data-flow architecture, not unapproved device commands.

## Public capability classification

Use these seven classes consistently. A class describes availability; the evidence class and exact version describe the strength and limits of the claim.

| Class | Meaning and boundary |
|---|---|
| `PUBLIC_KNOWLEDGE` | Original advisory explanations, design rules and examples included here. No live operation is implied. |
| `PUBLIC_OFFLINE_TOOL` | A shipped script for supplied local artifacts, within its stated input/version contract. State which public package actually contains it. |
| `PUBLIC_EXECUTABLE` | A runnable public entry point actually shipped in the named package, with documented dependencies and invocation. It does not imply a live PEKAT connector. In this repository this includes publication/build/validation utilities, not PEKAT runtime operations. |
| `PRIVATE_VERIFIED_NOT_DISTRIBUTED` | Historical bounded private verification exists; its controller/runtime is not included here and cannot be invoked from this public edition. |
| `PARTIAL` | Some required functions or evidence exist, but the complete scenario remains unvalidated. Name the missing part. |
| `PLANNED` | Intended development with no present implementation/acceptance claim. |
| `UNSUPPORTED` | No supported public route is established. Missing or conflicting evidence remains unknown; offer useful analysis or preparation without inventing execution. |

A **native PEKAT function** is a separate product fact: a user may operate it in an appropriately licensed PEKAT installation. Its existence does not establish a public Assistant tool, private writer acceptance or project-specific correctness. The [domain guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_DOMAIN_GUIDE.md) names native functions separately from the Assistant's role and automation boundary.

"Verified" requires evidence for the exact version and workflow. Static checking, a simulated example, a successful command response and a physical measurement are different verification levels. The [version matrix](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/VERSION_MATRIX.md) identifies retained 3.19.3, 4.0.1 and 4.0.3 evidence without distributing its private source artifacts.

## Privacy and safe sharing

Share only sanitized screenshots, example images, FLOW diagrams, code snippets or diagnostic excerpts for which you have permission. Remove customer names, personal data, real production identifiers, credentials, host addresses and any sensitive production configuration. The public edition should describe **observable function and safe usage**, not reproduce private product implementation details or proprietary material.

## Related reading

- [Getting started](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/GETTING_STARTED.md)
- [Capabilities and historical scope](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/CAPABILITIES.md)
- [Extended scenarios](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/USER_SCENARIOS_EXTENDED.md)
- [Evidence and validation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/EVIDENCE_AND_VALIDATION_STATUS.md)
- [Roadmap](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/ROADMAP.md)
- [Public skill](https://github.com/CZPavel/codex-skill-pekat-vision)

**Independent community project, not affiliated with or officially supported by the PEKAT VISION vendor.**
For version-scoped engineering notes on image layers, frame identity and delivered files, see [Image, Context, Result and Output](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/IMAGE_CONTEXT_OUTPUT_GUIDE.md).


---

Source: `docs/PUBLIC_DOMAIN_GUIDE.md`

# Practical domain guide

This guide maps user tasks to usable advice. All domain cards below are `PUBLIC_KNOWLEDGE`; native PEKAT functions require the user's own installation and version check. The public Assistant does not include a PEKAT connector or project/device writer. Historical bounded private capabilities are `PRIVATE_VERIFIED_NOT_DISTRIBUTED`, not executable public tools. See the [seven availability classes](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification).

Inputs mean sanitized material the user supplies voluntarily and has permission to share. A path, screenshot or module name alone does not supply the underlying project, data or runtime state. Start from the relevant card and linked topic; do not require a full project export for a small question.

## Inspection design and acquisition

### Inspection concept and vision-method selection

**Purpose/scenario:** detect a missing component or surface defect with measurable miss and false-reject objectives. **Inputs:** representative OK/NG images, defect size, material, pose variation, field of view, motion, cycle time and acceptance criteria.

**Native functions:** candidate preprocessing, geometry, Detector, Classifier, anomaly, supervised surface inspection and OCR; availability and fit require the exact version. **Assistant role:** compare native/classical/ML alternatives, propose optics/light/acquisition and the smallest discriminating trial. **Automation/limits:** a design or illustrative script is reviewable advice; image visibility, physical repeatability, accuracy and cycle time need independent trials. Start with [inspection design](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/VISION_DESIGN.md).

### Camera acquisition and triggering

**Purpose/scenario:** acquire one correctly exposed frame per inspected part. **Inputs:** exact camera/interface, lens, exposure, trigger source, motion, image format and ownership of acquisition.

**Native functions:** configured source, capture/live processing and image selection where supported. **Assistant role:** distinguish camera configuration, live feature values, stream state, processing state and saved images; route exact Basler facts to the specialist. **Automation/limits:** no public acquisition controller; no inferred physical frame freshness from a matching filename or HTTP response. One physical camera owner at a time. See [acquisition](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CAMERA_ACQUISITION.md) and [Basler bridge](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/bridges/BASLER_PEKAT_BRIDGE.md).

## FLOW, code and image meaning

### FLOW, Parallelism and Conditional Gate

**Purpose/scenario:** explain why a detected object still produces NOK, or group checks by component. **Inputs:** version, active topology, module types/settings, intended dependencies and representative results.

**Native functions:** sequential FLOW, Parallelism, Conditional Gate and preprocessing in the installed version. **Assistant role:** trace execution, preserve the user's functional hierarchy, compare sequential/branched alternatives and identify shared inference. **Automation/limits:** proposals do not author live FLOW; module inventory is not execution order, branch exit is not a universal stop, and joining decisions does not prove image/overlay merging. See [FLOW interpretation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/FLOW_AUTHORING.md).

### Code, Context and GlobalData

**Purpose/scenario:** calculate a custom measurement or diagnose a value left over from a previous frame. **Inputs:** source snippet, version, expected frame identity, input/output schema, reset rules and side effects.

**Native functions:** Code execution and its supported Context/shared-state mechanisms. **Assistant role:** declare producer, frame ownership, missing-input behavior, units, coordinates and lifetime; draft or review code. **Automation/limits:** generated code has not run in embedded PEKAT Python; process-lifetime state is not durable storage or evidence of current-frame validity. File, network and hardware effects require separate scope. See [Context/shared state](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CONTEXT_CODE_GLOBALDATA.md).

### Form, PTool and PModule

**Purpose/scenario:** expose technician parameters for a reusable computation. **Inputs:** exact artifact/version, entry point, stable parameter keys, values/defaults, units/ranges, dependencies and example input/output.

**Native functions:** supported Form controls and native import/export for the actual artifact family. **Assistant role:** prepare readable code and a module card stating purpose, FLOW placement, reads, writes, effects and validation status. **Automation/limits:** no public live import/metadata writer; defaults are not proven execution values, and a narrow package round trip does not prove dependency portability. See [PTool/Form](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PTOOL_PMODULE_FORM.md).

### Embedded Python and external models

**Purpose/scenario:** determine whether an external algorithm or pretrained model can run in Code/PTool. **Inputs:** PEKAT build, observed Python/package profile, CPU/GPU, model/license/weights, preprocessing and resource budget.

**Native functions:** embedded Python/Code in the installed runtime; installed dependencies must be established independently. **Assistant role:** propose a CPU reference, explicit dependency checks and bounded evaluation. **Automation/limits:** package presence, import, model construction and real inference are different evidence levels. A tested machine is not a clean installation, and one external-model example does not establish arbitrary-model compatibility. See [runtime profile](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/RUNTIME_PYTHON_ML.md) and [external-model example](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/EXTERNAL_TORCHVISION_PTOOL_403.md).

### Image, annotations, native Result and Output

**Purpose/scenario:** deliver the right image and result when a branch crops or changes its raster. **Inputs:** source image, transformations, producer/frame identity, result/context artifact, intended overlay basis and destination ownership.

**Native functions:** image display, native results/overlays, local Image Saver and output modules as individually supported. **Assistant role:** trace raster, geometry, native result and custom state separately; define freshness and complete-delivery checks. **Automation/limits:** no public saver/output writer; equal image dimensions do not prove alignment, configuration/ACK does not prove file delivery, and sequential evidence does not prove concurrency. Retention can delete foreign files in owned date folders. See [image/output guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/IMAGE_CONTEXT_OUTPUT_GUIDE.md).

## Dataset, annotation and model lifecycle

### Detector and annotation

**Purpose/scenario:** locate/count parts and review missing or incorrect boxes. **Inputs:** representative images, class definitions, box geometry/basis, module/model identity and independent validation examples.

**Native functions:** Detector labeling, training, inference and supported Smart Mask assistance. **Assistant role:** distinguish object instances from image-level class predictions, review dataset coverage and draft labeling/QA rules. **Automation/limits:** Smart Mask computation is not persisted annotation; a box is not a segmentation mask. No generic public annotation/model-delete writer is shipped. See [Detector annotation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DETECTOR_ANNOTATION_403.md).

### Classifier and result interpretation

**Purpose/scenario:** distinguish a correctly assembled input from an incorrect variant. **Inputs:** input domain/source, allowed classes, labels, selected model, predictions/confidence and validation split.

**Native functions:** family-specific labeling/training, class inference and available statistics. **Assistant role:** reason about winner versus other candidates, source/domain consistency, ambiguity and validation leakage. **Automation/limits:** candidate presence does not prove the winning class; current settings do not retroactively redefine a trained model, and TRAIN-inclusive statistics are not independent quality. See [Detector/Classifier/OCR](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DETECTOR_CLASSIFIER_OCR.md).

### Anomaly learning and supervised surface inspection

**Purpose/scenario:** detect an unusual surface or localize a known defect. **Inputs:** representative normal variation, module-specific OK/NG labels or masks, defect definitions, pixel basis and held-out evaluation set.

**Native functions:** anomaly and supervised surface workflows as separate model families. **Assistant role:** choose a family, review label/mask quality and propose threshold/coverage experiments. **Automation/limits:** tags, OK/NG labels and pixel masks are distinct; unlabeled does not mean confirmed normal. No shared generic annotation/training writer or inferred cross-family progress scale. See [anomaly](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/ANOMALY_UNSUPERVISED.md) and [supervised masks](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/SUPERVISED_MASK_LIFECYCLE.md).

### OCR and text annotation

**Purpose/scenario:** read a marking and compare it with an expected identifier. **Inputs:** image/region, transcription policy, charset/format, orientation, model/version and accepted error criteria.

**Native functions:** supported OCR regions/partitions, annotation, recognition and training. **Assistant role:** separate annotation text, recognized text, confidence and application-level format validation. **Automation/limits:** no public OCR writer; region geometry and transcription have their own contracts. Correct format alone does not prove the text is correct or belongs to the current frame. See [OCR annotation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/OCR_ANNOTATION.md).

### Training history, model selection and portability

**Purpose/scenario:** decide whether a trained model is usable or move data to another project. **Inputs:** family/version, dataset/splits, training terminal state, saved artifact, selected model identity, metrics and source/target export formats.

**Native functions:** family-specific training/status/selection, Image Library transfer, supported Detector COCO and native model-package transfer. **Assistant role:** distinguish command acknowledgement, terminal state, saved weights, selection and independent quality; plan an explicit transfer check. **Automation/limits:** progress 100 or a completed record does not alone prove saved usable weights. Export families are not interchangeable and clean import does not prove equal inference. See [training history](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/TRAINING_HISTORY_DIAGNOSTICS.md) and [portability](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DATA_MODEL_PORTABILITY.md).

## Project understanding and operation

### Project explanation, comparison and modernization

**Purpose/scenario:** understand a supplied project, identify a change between versions, or replace custom logic with a native feature. **Inputs:** sanitized snapshots/diagrams, exact builds, active topology, code/settings, known good behavior and intended delta.

**Native functions:** project management and installed native alternatives; the comparison itself is an advisory/offline task. **Assistant role:** separate active modules from recoverable history, match by meaning rather than only IDs, preserve working logic and identify the smallest regression check. **Automation/limits:** this repository includes no project parser/controller; name the separate public offline skill when recommending its scripts. Static similarity proves neither runtime equivalence, timing nor equal OK/NOK behavior. See [project analysis](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PROJECT_ANALYSIS.md), [semantic diff](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/SEMANTIC_PROJECT_DIFF.md) and [modernization](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/MODERNIZATION_ADVISOR.md).

### Logs, startup and troubleshooting

**Purpose/scenario:** diagnose apparent hangs, initial evaluation or missing results. **Inputs:** version, source/mode, timestamps, sanitized logs/stderr, readiness/model state, last successful action and repeatable symptom.

**Native functions:** project lifecycle/status and runtime logging in the installed version. **Assistant role:** rank hypotheses and propose one low-risk discriminating check; distinguish startup, server-ready, model-ready and actual processing. **Automation/limits:** a restart can trigger evaluation/effects; a native success result can coexist with a Code traceback. Do not classify every initial frame as faulty or call an execution-bearing reader a passive check. See [troubleshooting](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/TROUBLESHOOTING.md) and [log diagnosis](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/LOG_DIAGNOSTICS.md).

### Projects, Operator and statistics

**Purpose/scenario:** present inspection state to an operator and explain summary counts. **Inputs:** intended operator workflow, layout, data origin/reset rules, project lifecycle and recovery requirements.

**Native functions:** available Operator layout/input, kiosk and statistics facilities; each requires version-specific evidence. **Assistant role:** propose understandable status/UNKNOWN/error handling and distinguish a display from an operator state machine. **Automation/limits:** retained Operator runtime evidence was Input-only; kiosk recovery remained manual. No public UI automation or complete statistics writer is included. See [Operator/statistics](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/PROJECTS_OPERATOR_STATISTICS.md).

## Communication and industrial integration

### REST, official SDK, HTTP Output and Cross-PEKAT

**Purpose/scenario:** request inspection externally or forward a result to another system. **Inputs:** exact version/interface documentation, input/result schema, request/frame identity, timeouts, acknowledgement semantics and destination ownership.

**Native functions:** documented REST/SDK interfaces, HTTP Output and supported cross-project mechanisms have separate scopes. **Assistant role:** draft a bounded integration contract, distinguish request acceptance from processing/delivery, and define stale/duplicate/timeout behavior. **Automation/limits:** no public live client/controller is bundled; an SDK release does not establish a generic writer. Happy-path state transfer proves neither reconnect behavior nor atomic image/JSON delivery. See [REST/SDK](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/REST_SDK_CROSS_PEKAT.md), [HTTP Output](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/HTTP_OUTPUT_403.md) and [Cross-PEKAT](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/CROSS_PEKAT_403.md).

### Basler, IFM IO-Link, KEYENCE LJ-X/LJ-S and MX-G2000

**Purpose/scenario:** combine a camera, distance sensor or line profile with vision, or deploy onto an embedded platform. **Inputs:** exact model/family/firmware, interface, units/quality, timing, device ownership, coordinate calibration and PEKAT build.

**Native functions:** only those independently established for the named PEKAT source/transport and exact device. **Assistant role:** route vendor facts to the matching specialist and own PEKAT-side timestamp/frame/measurement composition. **Automation/limits:** specialist knowledge is an independent dependency, not a device writer; LJ-X/LJ-S families are not interchangeable, an installed SDK is not acquisition proof, and platform compatibility is not an industrial acceptance test. See the [hardware bridges](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/INDEX.md).

## How to finish a useful advisory task

Return a concrete explanation, code draft, inspection design, comparison or integration contract; list the inputs still missing only when they affect its use. Name the exact version and evidence level. State which artifact/tool is actually shipped and the smallest remaining offline, runtime or physical check. Unsupported execution does not block useful preparation. Public publication utilities are `PUBLIC_EXECUTABLE`; new live connectors, new writers and a public Windows installer remain separately reviewed work, not features implied by these cards.


---

Source: `docs/IMAGE_CONTEXT_OUTPUT_GUIDE.md`

# Image, Context, Result and Output — practical PEKAT VISION guidance

Public technical note, 2026-11-09. Evidence scope: **bounded PEKAT VISION 4.0.3 observations** and the explicitly stated comparison with 4.0.1; no assertion that every 4.x version or project behaves identically. This page is knowledge for user review, not an automation interface.

## Distinguish four independently meaningful things

1. **Image raster:** the actual pixels available at the current step, which may have been cropped, rescaled, masked or otherwise processed.
2. **Native recognition and measurement results:** rectangles, classes, OCR, heatmaps, lines and measurements returned by the relevant tools.
3. **Custom Context/shared values:** information passed between operations or held beyond a single evaluation; it may not have the same lifetime or merge behavior as image data.
4. **Visualization and persisted output:** what appears as an overlay in the UI, or what is actually saved to disk. Displaying a result and saving it are distinct outcomes.

A rectangle visible over an image is not proof that the rectangle has been drawn into the image pixels. A visually correct preview is not proof of successful file delivery.

## Frame identity, filenames and stale values

For the observed Folder-source recipe, the input filename is available as a filename-only value in Context. Its presence must be checked for the current input, not borrowed from a previous evaluation.

Shared GlobalData values may survive multiple evaluations but reset with project-server restart. Initialize each evaluation's result quality/validity before producers execute, and associate results with a current frame identity. When a producer fails or a branch is skipped, publish **UNKNOWN/INVALID** rather than silently reusing the previous positive result.

For multi-branch FLOW, avoid assuming that merging image pixels also automatically merges or replaces custom values and native results with equivalent rules. Assess each output channel separately.

## Coordinate systems and transformations

Always state the coordinate basis of a result: full original image, current module image, cropped region, scaled image or unknown. A result can have plausible numbers but still refer to the wrong image basis.

For one previously tested **axis-aligned application recipe** with crop origin (ox, oy), crop scale s and independent original-space scale (sx, sy):

- X = (ox + x × s) × sx
- Y = (oy + y × s) × sy
- W = w × s × sx
- H = h × s × sy

This equation is a scoped numerical mapping, **not** a general PEKAT rule for rotated rectangles, every Unifier mode, percentage-based coordinates, heatmaps or camera calibration. Check landmarks and image size against the actual current transform.

A non-destructive annotation conversion should preserve the original detections and associate any derived representation with its source frame and transformation. New geometry does not automatically establish improved physical accuracy.

## Image Saver and delivery correctness

A bounded 4.0.3 configuration/evaluation test established that an active local Saver needs an eligible execution path and an appropriate production-mode state. Observed selection was: **ALL** accepts True/False/None; **OK** accepts True; **NG** accepts False. These are observations for the tested path, not a universal guarantee across modes and versions.

Treat the following as separate checks:

- the relevant output module is reached and enabled;
- the intended image/overlay and filename basis is selected;
- the configured destination belongs to the intended producer;
- the file has actually appeared and can be opened;
- any accompanying JSON/meta evidence belongs to **the same current frame**, not a previously written image.

For tests, use a unique frame or request marker and check a fresh image plus matching metadata. Separate image and metadata writes are not inherently an atomic pair. A file with a plausible name can still belong to an earlier frame.

**Retention warning:** On the bounded tested configuration, automatic retention could delete **entire old date directories**, including unrelated nested content. Do not enable automatic deletion on a shared/customer directory without first isolating its root and testing the exact settings. Configuration rollback cannot restore files already deleted by a completed cleanup.

## Safe result policy

For a composite inspection, retain a confirmed NOK even if another required check is UNKNOWN. Confirm overall OK only when all required checks are OK, expected instances are covered and observations refer to the current item/frame. Otherwise emit REVIEW/UNKNOWN, while keeping communication and acquisition errors separately visible.

## Suggested acceptance checks

1. Reprocess two distinct, identifiable frames sequentially; verify that labels, images and result metadata do not cross over.
2. Test missing or skipped producers; verify no previous positive value leaks into the next result.
3. Use a visible landmark to verify crop/scale output coordinates.
4. Compare visible overlays with the saved raster; do not presume they are the same.
5. Verify the real delivery path with a unique marker, not only the configured Saver state.
6. If cleanup is used, test it exclusively in an isolated disposable directory.

This note does not claim production concurrency, camera metrological accuracy, rotated-geometry compatibility, general hardware acceptance or a publicly distributed Image Saver controller.

See [practical runtime rules](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PRACTICAL_RUNTIME_RULES.md), [capabilities](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/CAPABILITIES.md) and [public usage guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md).


---

Source: `docs/PRACTICAL_RUNTIME_RULES.md`

# Practical PEKAT runtime rules

Status: sanitized public engineering conclusions.
Primary historical runtime scope: PEKAT VISION 4.0.3 unless a narrower note says otherwise.
These rules do not expose or authorize private transport mechanisms.

## FLOW topology and lifecycle

A project registry and the executed FLOW are different representations. Explain recursive execution topology first. A module that exists in project storage may be inactive, retained history, recoverable state or otherwise outside active execution. Do not classify it as active merely because it exists, and do not recommend deletion from inventory alone.

A static project representation is suitable for explanation and comparison, but it is not a writer contract.

## Image, native results and custom state

Treat these as separate layers:

1. image raster/pixels;
2. PEKAT-native detections, measurements, heatmaps or result objects;
3. custom Context and shared process state.

An image operation can change pixels without erasing all native result semantics. Conversely, removing or replacing result structures is not the same as editing the image.

In parallel FLOWs, an unchanged branch can preserve an earlier raster while other branches produce native results. Do not assume that all branch outputs merge identically.

## Branch exit

Historical runtime evidence shows branch-local exit behavior. Therefore do not explain an exit flag as universally terminating the entire FLOW unless exact-version topology and runtime evidence establish that wider behavior.

## GlobalData and persistent state

GlobalData is shared process-lifetime state and resets when the relevant project server restarts. It is not durable database history.

Every shared value used for production decisions should have a producer, owner, item/product identity where relevant, freshness or timestamp semantics, reset behavior and invalid/stale handling.

A valid value from a previous item must not silently decide the next item.

Historical PEKAT Code can also use persistent Python/module state. Presence of persistent state is not automatically a defect. Treat it first as a dependency that needs ownership and reset analysis.

## Detector versus Classifier

Detector answers object/location questions. Classifier answers class/state questions about an inspected input. Do not treat a Classifier candidate list as detected object instances.

Historical PEKAT observations show that candidate class lists can contain more than the eventual winner. Therefore routing must identify the winner according to the exact family/version contract; testing whether a label appears anywhere in the candidate list is unsafe.

## Annotation representations

Keep these distinct: Smart Mask or segmentation suggestion, accepted segmentation mask, bounding box, persisted Detector rectangle and OCR region/partition information.

Conversion between representations is a deliberate operation with geometry/raster assumptions. A suggestion is not persistence.

## Training and model lifecycle

Training start acknowledgement, progress and terminal UI text are separate from durable artifact creation.

A defensible training conclusion should establish as much as the family supports: run/model identity, terminal state, artifact presence, active model binding/selection and relevant dataset/annotation provenance.

Do not generalize one family's lifecycle to Detector, Classifier, OCR, Anomaly and Supervised interchangeably.

## PTool, Form and Python

A Form control key, displayed default, serialized value and runtime value are separate concepts. Validate types and actual execution values.

Portable PTool/package artifacts do not automatically include external Python packages, ABI compatibility, model weights or device dependencies.

## REST, outputs and communication

Separate process/project reachability, provider/source readiness, image transport, inference, result semantics and outbound delivery.

A successful connection or HTTP response does not prove that the intended image was evaluated by the intended model.

Distributed/shared-state integrations need identity, freshness, timeout, duplicate and restart semantics.

## Version boundary

Version similarity is evidence for investigation, not writer authority.

A behavior observed on 4.0.1 may inform a 4.0.3 hypothesis. It does not prove a 4.0.3 writer or runtime contract. Future PEKAT versions should be treated as fresh version intake until bounded evidence exists.

## Current capability and knowledge boundaries — 2026-10-23

Use the [current decision-guide addendum](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md) for ID-specific Detector edits, Brightness/Contrast, OCR authoring and accepted Gate variants. Dated negative observations remain historical evidence. Supersession applies only to the matching exact-version contract and evidence scope; retain do_not_repeat and disclose cycles/conflicts. Workflow-first intent selection remains read-only and cannot authorize execution. Public main, released artifacts and hosted GPT knowledge are separate states; local generation does not update a hosted assistant.


---

Source: `docs/EVIDENCE_AND_VALIDATION_STATUS.md`

# Evidence and validation status

This document answers a different question from the capability list: what kind of evidence supports a public statement?

Public edition functionality is advisory. Historical upstream implementation is listed only to show which conclusions came from bounded runtime work rather than feature speculation.

| Area | Version scope | Evidence class | Public conclusion |
|---|---|---|---|
| Exact-version boundary | general policy | VERIFIED_POLICY | Evidence from one patch does not authorize another patch |
| Project/FLOW topology | historical 4.0.3 | STATIC + OFFLINE + bounded runtime context | Registry membership and active execution are separate |
| Context/GlobalData | historical 4.0.3; retained older context | BOUNDED_RUNTIME | Shared process state needs ownership, reset and freshness |
| Branch-local exit | historical tested scope | BOUNDED_RUNTIME | Do not generalize exit to whole FLOW |
| Parallel image/result reasoning | historical tested scope | BOUNDED_RUNTIME + curated synthesis | Pixels, native results and custom state are separate layers |
| Camera lifecycle/capture | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Narrow capture/control existed upstream; no public controller |
| Conditional Gate subset | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Narrow boolean gating existed upstream; not arbitrary gate authoring |
| FLOW native tool subsets | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Selected tool subsets existed upstream |
| Detector annotation | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Additive/first-create semantics were family-specific |
| Smart Mask | historical 4.0.3 | READ_ONLY_COMPUTE + bounded composition | Suggestion is not persistence; bbox conversion is explicit |
| Classifier routing | retained observed/runtime semantics | BOUNDED_RUNTIME | Candidate presence is not a safe winner test |
| Family-specific ML lifecycle | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Identity/status/artifact/selection are family-specific |
| PTool/Form | historical 4.0.3 | ROUND_TRIP_NARROW | Round trip does not prove arbitrary dependency portability |
| HTTP Output | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Narrow delivery existed; retries/order/general transports remain separate |
| Cross-project state | historical 4.0.3 | VERIFIED_NARROW_SUBSET | Happy-path transfer does not establish reconnect semantics |
| Project forensics/diff | historical upstream | OFFLINE_VERIFIED | Static explanation/comparison does not prove runtime equivalence |
| Generic project DB/store writer | any | INTENTIONALLY_UNSUPPORTED | Read representations must not be promoted into a generic writer |
| Hardware bridges | exact device required | KNOWLEDGE_ONLY unless specialist says otherwise | PEKAT-side composition does not prove device acceptance |

## Evidence vocabulary

- OFFICIAL_DOCUMENTATION: vendor-described behavior in stated scope.
- STATIC: structure, schema or source/configuration evidence.
- OFFLINE_VERIFIED: deterministic fixture/parser/semantic validation.
- BOUNDED_RUNTIME: exact target/version runtime observation.
- VERIFIED_NARROW_SUBSET: implemented and verified, but only for explicitly bounded variants.
- READ_ONLY_COMPUTE: computation/read path with no persistence authority.
- USER_OBSERVED: useful observation supplied by a user, not independently reproduced here.
- KNOWLEDGE_ONLY: advisory reasoning with no executable public tool.
- UNKNOWN: missing or contradictory evidence.

## What public tests prove

Repository tests prove packaging, sanitization, reference integrity and benchmark schema. They do not prove PEKAT runtime behavior.

See [Validation](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/VALIDATION.md).

## October evidence boundary

The [decision guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/knowledge/assistant/DECISION_GUIDE_403.md) separates current official 4.x descriptions, sanitized exact-4.0.3 upstream observations, offline axis-aligned recipes and open contracts. Sequential freshness is not concurrency or atomic JPEG/JSON proof; saved/selected model is not independently validated quality. SMALL_MODEL_LIVE_EVAL_NOT_RUN: public offline gates do not evaluate a language model.

## Historical version anchors in this public consolidation

The [version matrix](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/VERSION_MATRIX.md) distinguishes controlled 3.19.3 migration lineage, exact-4.0.1 generated-FLOW/Classifier and tested-machine Python/ML observations, and bounded exact-4.0.3 tool/workflow evidence. These are retained upstream conclusions, not new tests. Public sources remain sanitized rewrites; raw historical projects, database/transport details and third-party manuals are not distributed.

Availability uses the [seven public classes](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification). PUBLIC_EXECUTABLE applies to actually shipped runnable entry points such as publication utilities; it does not convert a native PEKAT function or historical private controller into a public live operation. Unknown or conflicting evidence stays explicit even when a route is classified UNSUPPORTED.


---

Source: `docs/VERSION_MATRIX.md`

# Version evidence matrix

This is an evidence map, not a support certification. No PEKAT runtime test was performed for this public consolidation. Retained upstream conclusions are summarized without raw private captures, database schemas or transport contracts.

| Exact version | Retained evidence and practical use | What it does not establish |
|---|---|---|
| 3.19.3 | A controlled pre-upgrade fixture supports historical project lineage and read-only comparison against its migrated 4.0.1 state. In that fixture, the pre-upgrade snapshot and retained old snapshot matched, and active execution topology was preserved through migration. | Universal upgrade safety, current runtime semantics, a public migration tool, or permission to restore old database data into a current project. |
| 4.0.1 | Retained generated-FLOW/Classifier runtime recipe and tested-machine Code/Python/ML observations support version-specific explanation. Selected CPU/GPU calculations and library functions were exercised; some model libraries were tested only for construction. | A clean-install dependency list, arbitrary-model inference, camera/PLC communication, or writer acceptance for 4.0.3. Locally added packages must remain identified as additions. |
| 4.0.3 | Principal bounded upstream runtime target: selected FLOW/Gate/native-tool, Context/image/result, family-specific annotation/model, PTool/Form, output and acquisition subsets. Public topics preserve the limits of those conclusions. | A complete feature matrix, universal join/image semantics, arbitrary authoring, physical timing/accuracy, concurrent freshness, or an included public controller. |
| Other/future versions | Common design concepts can guide analysis; explicitly label nearby-version evidence as a candidate and identify the relevant compatibility check. | Automatic runtime equivalence, schema equivalence, bundled dependency compatibility or inherited writer authority. |

## Common concepts and exact contracts

4.0.1 and 4.0.3 are evidence anchors within the 4.0.x maintenance family. They do not by themselves prove different schemas or incompatible behavior. Reuse common functional knowledge where appropriate, then overlay a known relevant delta or mark the exact behavior unverified. Avoid both inventing differences and assuming equivalence.

For official 4.x function descriptions start with [PEKAT Knowledge Base 4.0](https://pekatvision.atlassian.net/wiki/spaces/KB4/overview?homepageId=1512243624). A published page is documentation evidence for its stated scope/revision, not an exact-4.0.3 runtime test. KB3 is historical/supplementary for older-version questions. If documentation conflicts with a reproducible exact-version observation, state the conflict and scope instead of silently merging the claims.

For each concrete answer record the installed version/build, source of the claim, evidence level, relevant input/workflow and remaining uncertainty. Common read/design knowledge and exact execution acceptance are separate. Internal database formats and frontend transports are not public APIs; static access does not establish a writer.

## Availability is separate from evidence

All PEKAT-domain execution authority in this public knowledge edition is absent, including where upstream evidence was bounded and successful. Classify retained private operations as `PRIVATE_VERIFIED_NOT_DISTRIBUTED`, and explanations as `PUBLIC_KNOWLEDGE`. A separately shipped offline script is `PUBLIC_OFFLINE_TOOL` only in the package that actually includes it. See the [seven classes](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/PUBLIC_CAPABILITY_GUIDE.md#public-capability-classification) and [evidence model](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/EVIDENCE_MODEL.md).
