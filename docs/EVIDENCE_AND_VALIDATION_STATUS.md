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

See [Validation](VALIDATION.md).
