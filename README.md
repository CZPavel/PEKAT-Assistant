# PEKAT Assistant — public preview

Independent advisory knowledge and a Codex skill for PEKAT VISION inspection design, supplied project explanation, datasets, ML and integration boundaries.

This preview includes no runtime controller, project parser, annotation writer, training runner or hardware transport. Historical upstream tools are not distributed here.

Start with [Getting started](docs/GETTING_STARTED.md), [Capabilities](docs/CAPABILITIES.md), [User scenarios](docs/USER_SCENARIOS.md), [Evidence model](docs/EVIDENCE_MODEL.md) and [Version support](docs/VERSION_SUPPORT.md).

- [Knowledge index](knowledge/INDEX.md)
- [Standalone skill](.github/skills/pekat-assistant/SKILL.md)
- [Custom GPT guidance](gpt/README.md)
- [Advisory example](examples/advisory-workflow.md)
- [Publication model](docs/PUBLICATION_MODEL.md)

This is an independent public preview, not an official PEKAT product. Review [Disclaimer](DISCLAIMER.md), [Security](SECURITY.md), [Third-party notices](THIRD_PARTY_NOTICES.md) and the repository LICENSE.

## Why use it?

Inspection projects connect optics, lighting, acquisition, learned models, FLOW decisions and external measurements. This pack helps explain which layer the evidence supports, what remains unknown and what small check would resolve it. It avoids treating a feature list as a complete inspection workflow.

## What works today?

The public preview supports advisory reasoning from sanitized user evidence: requirements, project explanation, dataset review, training interpretation, comparison and integration planning. Historical upstream runtime work covered narrow exact-4.0.3 subsets. Those tools are not part of this release; broad automation, deployment, voice and multimodal scenarios retain their catalog gaps.

## How can I use it?

Read the Markdown directly, install the complete standalone Codex skill or upload the generated public knowledge to a Custom GPT. Neither interface connects to PEKAT automatically. Optional [specialist skills](docs/SPECIALIST_SKILLS.md) supply exact Basler, IFM or KEYENCE guidance; PEKAT-side mapping remains separate.

Vision design starts with a measurable acceptance criterion and physical image quality. Vendor documentation is the source for exact product specifications; this independent pack complements it with evidence-bound reasoning and never replaces vendor support or application validation.

## Evidence and longer-term direction

Exact-version evidence keeps documented features, static observations, bounded
runtime results and writer authority separate. A runtime conclusion from 4.0.1
does not establish support for 4.0.3. The skill states unknowns and fails closed
when executable control is unavailable; see the [evidence model](docs/EVIDENCE_MODEL.md).

The longer-term goal is an assistant that connects inspection reasoning to
supported typed operations with explicit policy, readback and verification.
The [architecture](docs/ARCHITECTURE.md) explains this boundary and how a future
official MCP could serve as an adapter. It is not a current dependency. The
[scenario catalog](docs/USER_SCENARIOS.md) preserves partial and future goals.

**Unofficial community project / not affiliated with or officially supported by
the PEKAT VISION vendor.** Original project contributions are licensed under
[Apache-2.0](LICENSE); external vendor material retains its own ownership.
