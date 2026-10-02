# Extended PEKAT Assistant user scenarios

This is the public human-facing scenario catalog. Status refers to historical upstream capability maturity, not executable tools included in this public repository.

Status meanings:

- AVAILABLE_NOW: a verified narrow upstream capability existed.
- PARTIALLY_AVAILABLE: useful pieces existed but the complete workflow had a gap.
- PLANNED: product goal without a complete verified workflow.
- FUTURE_VISION: depended on later interfaces, history, hardware or multimodal capability.

| ID | Goal | Minimum prerequisite | Assistant output / workflow | Status / main gap |
|---|---|---|---|---|
| US-02 | Understand a new inspection problem | Representative part/image and acceptance criterion | Clarify visibility, defect semantics, acquisition and tool family | PARTIALLY_AVAILABLE — complete experiment loop is future |
| US-03 | Explain an existing project | Exact version and sanitized project/FLOW evidence | Reconstruct active topology, state, models and outputs with unknowns | PARTIALLY_AVAILABLE — full runtime/output reconstruction incomplete |
| US-04 | Safely modify FLOW | Exact target and supported writer | Inspect, plan smallest change, bounded apply/readback/restore | PARTIALLY_AVAILABLE — only narrow writers existed |
| US-05 | Capture a bounded image set | Ready selected project/camera | Bounded acquisition checklist and identity/readback | AVAILABLE_NOW upstream; no public controller |
| US-06 | Audit a dataset | Dataset/model inventory | Coverage, imbalance, provenance and obvious QA gaps | PARTIALLY_AVAILABLE |
| US-07 | Select useful images | Large dataset plus scoring signals | Rank uncertainty/rarity/diversity/duplicates | PLANNED |
| US-08 | Bootstrap Detector | Reviewed seed annotations | Safe seed → train → identify/select candidate | PARTIALLY_AVAILABLE — full review/retrain loop incomplete |
| US-09 | Teach by pointing | Image plus multimodal pointing input | Resolve target, confirm, propose/persist reviewed annotation | FUTURE_VISION |
| US-10 | Teach OK/NOK state | Stable identity and class/state semantics | Build consistent state dataset without conflating labels | PLANNED |
| US-11 | Correct target conversationally | Prior candidate and preserved image | Revise target while retaining audit/context | FUTURE_VISION |
| US-12 | Smart Mask proposal | Exact image/module and valid prompt | Compute suggestion, validate geometry, convert deliberately | PARTIALLY_AVAILABLE — interactive review/mask persistence gap |
| US-13 | Automatic annotation review | Accepted model and image selection | Pre-annotate, rank uncertain cases, preserve provenance | PLANNED |
| US-14 | Compare model iterations | Stable validation basis | Compare metrics/error buckets/provenance/runtime | PARTIALLY_AVAILABLE |
| US-15 | Champion/challenger | Verified model identities and approval | Compare/select candidate while preserving baseline | PARTIALLY_AVAILABLE |
| US-16 | Preprocessing experiment | Baseline, fixed images and metric | Run bounded comparable variants | PARTIALLY_AVAILABLE |
| US-17 | Training campaign | Dataset provenance and lifecycle | Track independent family-specific runs | PARTIALLY_AVAILABLE |
| US-18 | Decide whether to keep iterating | Comparable experiment history | Evaluate marginal gain, new data and cost | FUTURE_VISION |
| US-19 | OCR label refinement | Privacy-approved source and existing OCR region | Review transcription/partition then train | PARTIALLY_AVAILABLE |
| US-20 | OCR error mining | OCR results plus ground truth/history | Group verified errors and propose retraining data | PARTIALLY_AVAILABLE |
| US-21 | Diagnose gradual image degradation | Comparable historical images/config | Compare image health and recipe state | FUTURE_VISION |
| US-22 | Diagnose shared confidence loss | Multi-module time series | Test shared camera/light/FOV/timing causes first | FUTURE_VISION |
| US-23 | Explain unexpected NOK | Evaluated frame, active configuration and results | Trace decision evidence and smallest discriminating check | PARTIALLY_AVAILABLE |
| US-24 | Capture manual production feedback | Exact result/image and user identity | Preserve model verdict separately from human override | PLANNED |
| US-25 | Retrospective defect search | Defined defect and historical archive | Bounded historical inference plus review | FUTURE_VISION |
| US-26 | Production sampling for retraining | Result/image stream and storage policy | Select uncertainty/novelty/rare failure with dedup | FUTURE_VISION |
| US-27 | Voice tag data | Speech intent plus exact image/tag IDs | Route voice to same typed operation/policy as text | PARTIALLY_AVAILABLE — voice UI missing |
| US-28 | Voice review dataset | Speech intent and tag scope | Resolve reproducible selection/provenance plan | FUTURE_VISION |
| US-29 | Voice FLOW change | Speech intent and supported patch | Route through same approval/readback policy | PARTIALLY_AVAILABLE |
| US-30 | Operator next-step guidance | Readable process state | Present next expected action without mutation | PLANNED |
| US-31 | Multi-step assembly | Identity, sequence and reset semantics | Design debounce/order/removal/reset state machine | PLANNED |
| US-32 | Distributed vision process | Explicit peer identities and state keys | Transfer state with identity/freshness rules | PARTIALLY_AVAILABLE — reconnect/timeout/duplicates gap |
| US-33 | Multi-camera aggregate result | Shared item identity and synchronized results | Define partial/timeout/conflict/stale aggregation | FUTURE_VISION |
| US-34 | External sensor Gate | Device identity, validity and freshness | Compose sensor state with a vision decision | PLANNED |
| US-35 | TCP measurement plus camera | Exact framing/device contract | Define timeout/parsing/validity/idempotency semantics | PLANNED |
| US-36 | Preserve clean image plus native results | Known branch semantics | Keep raster and native result/overlay roles explicit | PARTIALLY_AVAILABLE |
| US-37 | Selective NOK/borderline collection | Result classes and retention policy | Separate inspection result from saver trigger/delivery | PARTIALLY_AVAILABLE |
| US-38 | Whole-system health | Acquisition/result/communication telemetry | Correlate readiness, confidence, failures and stale state | FUTURE_VISION |
| US-39 | Compare one camera with peers | Matched conditions and identities | Compare image health, recipe, timing and distributions | FUTURE_VISION |
| US-40 | Bounded camera optimization | Exact camera/features and approval | Baseline/variants/readback/restore with image metrics | FUTURE_VISION |
| US-41 | Embedded Python compatibility | Exact embedded build/ABI/package | Compatibility analysis plus bounded import proposal | PARTIALLY_AVAILABLE |
| US-42 | Closed-loop improvement | Monitoring, review, training, comparison, approval | Detect drift → select/review → train challenger → approve deployment | FUTURE_VISION |
| US-43 | Safe refusal of unknown writer | Requested operation plus capability lookup | Explain gap and propose bounded validation | AVAILABLE_NOW policy |
| US-44 | Exact-version boundary | Source and target versions | Treat old evidence as hypothesis, not target writer authority | AVAILABLE_NOW policy |

A scenario becomes available only when its relevant identity, preconditions, operation, durable readback and failure boundaries are supported at the required evidence level.
