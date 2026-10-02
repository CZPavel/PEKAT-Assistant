# Getting started

## Direct reading

Start with:

1. [Practical runtime rules](PRACTICAL_RUNTIME_RULES.md)
2. [Evidence and validation status](EVIDENCE_AND_VALIDATION_STATUS.md)
3. [Capabilities](CAPABILITIES.md)
4. [Extended user scenarios](USER_SCENARIOS_EXTENDED.md)
5. [Version matrix](VERSION_MATRIX.md)
6. [Knowledge index](../knowledge/INDEX.md)

Supply a sanitized inspection objective, exact PEKAT version, available evidence and measurable acceptance criterion.

## Codex skill

Copy the complete .github/skills/pekat-assistant folder, including references, into your Codex skills directory. Keep the folder name pekat-assistant. Invoke the skill explicitly or use normal skill discovery.

The public skill does not connect to PEKAT or equipment.

## Custom GPT

Follow [GPT setup](../gpt/README.md). Use the builder instructions plus the generated public knowledge. Review data handling before uploading private project information.

## Useful first prompts

- Explain this sanitized FLOW and separate active execution from retained module inventory.
- Why can this visually acceptable frame still become NOK? List the evidence needed to identify the deciding branch.
- I observed this behavior on PEKAT 4.0.1. What can and cannot be carried to 4.0.3?
- Compare Detector and Classifier routing semantics.
- Design an external sensor gate and include freshness, invalid data and restart behavior.
- Review this training history without assuming that progress 100 means a usable model.

See [Advisory workflow example](../examples/advisory-workflow.md) and the [public behavior benchmark](../benchmarks/assistant_behavior_v0_2.yaml).
