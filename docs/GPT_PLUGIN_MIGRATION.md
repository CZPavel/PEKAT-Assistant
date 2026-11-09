# Custom GPT to PEKAT Assistant plugin

Status, 2026-11-09: **WAITING_FOR_ACCOUNT_ACTION**. This repository contains a replacement foundation. The latest published GPT configuration, knowledge inventory, Custom Actions and account eligibility have not been retrieved through an authorized account interface. No hosted GPT was changed or migrated.

## Sources and mapping

Available public sources are the [Builder instructions](../gpt/BUILDER_INSTRUCTIONS.md), [generated aggregate](../gpt/knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md), [behavior benchmark](../benchmarks/assistant_behavior_v0_2.yaml) and [standalone PEKAT Vision skill](https://github.com/CZPavel/codex-skill-pekat-vision). These establish repository behavior, not the account's current configuration. Historical Agent material supplies migration candidates, not a parallel authority. Do not upload unreviewed historical files wholesale.

| Source or account item | Replacement | Verification / gap |
|---|---|---|
| Public Builder instructions | `plugins/pekat-assistant/skills/pekat-assistant/SKILL.md` | Compare actual published instructions before migration |
| Public knowledge files and manifest | Generated references from approved `public-package.yaml` inputs | Build/drift checks; compare account filenames and revisions separately |
| Older inspection-design, FLOW and diagnostic knowledge | Current public domain guide and topic references | Preserve exact versions and supersession |
| Legacy Code/Form/PTool drafts | Current advisory authoring route | Draft/offline review; no public deployment writer |
| Existing public offline diagnostics | Separate standalone PEKAT Vision skill and shipped scripts | Host must support files/execution; plugin installation does not install those scripts |
| Privately verified runtime abilities | `PRIVATE_VERIFIED_NOT_DISTRIBUTED` functional descriptions | No execution parity claimed; private Core is not required |
| Original scenarios and public behavior benchmark | Plugin acceptance prompts and human response review | Static fixtures are not model-answer evaluation |
| Custom Actions, if present | Existing compatible app/tool contract or explicit integration gap | Actual definitions unavailable; no fabricated MCP replacement |
| Model choice, audience and starters | Explicit account review | Do not assume settings or users transfer |

## Account checklist

1. In the owner account/workspace, record the original GPT URL/name and latest **published** configuration. Finish intended published edits before migration. Drafts are not the migration source; public sharing is not required.
2. Compare the actual instructions, starters, enabled capabilities, knowledge filenames/revisions and Action definitions with the mapping above. Credentials and customer files stay outside this repository. Unclear publication rights mean `PRIVATE_REVIEW_REQUIRED` and exclusion.
3. Resolve obsolete conclusions individually, keeping 3.19.3, 4.0.1 and 4.0.3 evidence separate. Keep unsupported Actions as explicit gaps.
4. Check **Migrate to plugin** in the creator account or authorized admin workspace. Migration eligibility is account-specific. The original GPT becomes read-only after migration, so finish essential changes first.
5. Review migrated instructions and files against this RC. Run plugin acceptance prompts, familiar real prompts and a harder compound request in the intended host. Record reference use, answer quality, unsupported-operation behavior and tool availability. Keep `HOST_ACCEPTANCE_PENDING` until tested.
6. Test every Action replacement separately. Prior conversations remain accessible in their existing history; they do not become plugin conversation context. Selected model settings do not carry over.
7. Confirm intended users can install and invoke the replacement. Migration does not grant existing GPT users access. Workspace sharing, repository distribution and public directory publication are separate operations.
8. Submit/publish only after the relevant rights, account and review gates. This task prepares an RC and does **not** submit it to the official directory.

## Distribution, Free accounts and region

GitHub distribution supplies files; it does not establish a Plugin Directory listing or account availability. [Official availability guidance](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) distinguishes directory access across plans from individual plugin access, which depends on plan, workspace, role, region and capabilities. [Troubleshooting guidance](https://help.openai.com/en/articles/20001497-troubleshooting-plugins-and-apps-in-chatgpt) limits extensions on Free/Go. This skills-only RC has no extensions, but that fact does not prove every Free account can install and invoke it. **Free-account acceptance remains unverified.**

No universal Czech/EEA inclusion or exclusion for this RC has been established. Check recipient account options and eventual listing country targeting. Do not apply restrictions for unrelated apps to this knowledge plugin.

The [submission workflow](https://developers.openai.com/plugins/deploy/submission) requires a verified developer identity and portal validation/review. Public publication needs a separate authorized submission. A future MCP addition needs its own contract and packaging decision; current guidance does not promise adding MCP to an existing skills-only listing. [Desktop-only guidance](https://developers.openai.com/plugins/deploy/desktop-only) adds conditions for local execution and approved local MCP submissions. This RC bundles neither MCP nor a required local executor.

## Official baseline

The [migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq) defines published-version migration, history retention, action gaps and sharing. Follow the account's retirement notice and exceptions. Standard announced retirement is 2026-12-11; qualifying deferred workspaces differ. Recheck before account migration.

The [portable packaging specification](https://developers.openai.com/plugins/build/plugins) and [skill authoring guidance](https://developers.openai.com/plugins/build/skills) define the replacement format. Static conformance does not prove host installation, answer quality, GPT parity or inspection acceptance.
