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

## Evidence and capability labels

- **PUBLIC KNOWLEDGE:** documented reasoning and examples available in this repository.
- **PUBLIC OFFLINE TOOL:** included and runnable in the separately published standalone skill, within its documented input/version scope.
- **UPSTREAM VERIFIED, NOT DISTRIBUTED:** a bounded capability has development evidence but its controller, runtime or installation is not included in this public repository.
- **PARTIAL:** some necessary functions or evidence exist, but the full user scenario is not validated.
- **PLANNED:** intended development, not a present feature.
- **UNSUPPORTED/UNKNOWN:** do not invent parameters or imply execution.

"Verified" requires evidence for the exact version and workflow. Static checking, a simulated example, a successful command response and a physical measurement are different verification levels.

## Privacy and safe sharing

Share only sanitized screenshots, example images, FLOW diagrams, code snippets or diagnostic excerpts for which you have permission. Remove customer names, personal data, real production identifiers, credentials, host addresses and any sensitive production configuration. The public edition should describe **observable function and safe usage**, not reproduce private product implementation details or proprietary material.

## Related reading

- [Getting started](GETTING_STARTED.md)
- [Capabilities and historical scope](CAPABILITIES.md)
- [Extended scenarios](USER_SCENARIOS_EXTENDED.md)
- [Evidence and validation](EVIDENCE_AND_VALIDATION_STATUS.md)
- [Roadmap](ROADMAP.md)
- [Public skill](https://github.com/CZPavel/codex-skill-pekat-vision)

**Independent community project, not affiliated with or officially supported by the PEKAT VISION vendor.**
