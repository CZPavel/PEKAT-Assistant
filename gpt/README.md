# Custom GPT setup

Use [Builder instructions](BUILDER_INSTRUCTIONS.md) and the generated [public knowledge aggregate](knowledge/PEKAT_ASSISTANT_KNOWLEDGE.md). They supply advisory reference content, not actions, credentials or hardware connections.

Create the GPT in your own environment, add instructions and upload only generated public knowledge. Review data handling before uploading private project information.

Test with the [advisory example](../examples/advisory-workflow.md). Confirm that the assistant preserves exact versions, states unknowns and never claims to have operated PEKAT.

## Update handoff

Build the validated public package using the existing release-artifact builder with the reviewed commit ref. In the GPT editor, replace the builder instructions and knowledge with the generated package, verify the four FLOW cases in the public behavior benchmark, then save using the intended visibility. A generated ZIP and passing publication checks do not deploy or update a hosted GPT. This repository contains no supported automatic GPT deployment mechanism.
