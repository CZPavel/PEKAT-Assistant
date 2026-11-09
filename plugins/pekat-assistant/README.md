# PEKAT Assistant public plugin

A portable Agent Plugins package providing evidence-bound PEKAT VISION advisory guidance. It contains one skill and generated public references; it does not contain a PEKAT runtime, MCP server, project writer, or device controller.

## Install and try

After the marketplace change is merged to `main`, add the repository source with `codex plugin marketplace add CZPavel/PEKAT-Assistant --ref main`. For local testing, add the local repository root as the marketplace source using the host's supported workflow. Restart the app, select the marketplace source and install PEKAT Assistant, then start a new conversation. Host availability and exact UI steps may vary; adding a source does not itself install the plugin.

Ask, for example, “Does a registered FLOW module necessarily execute?” The expected guidance distinguishes module inventory from active topology and asks for relevant evidence. Try the other prompts and expected guidance in [acceptance fixtures](acceptance-fixtures.yaml). See the [GPT and plugin migration guide](https://github.com/CZPavel/PEKAT-Assistant/blob/main/docs/GPT_PLUGIN_MIGRATION.md).

**HOST_ACCEPTANCE_PENDING:** the package has not yet been installed and exercised in a supported host. Static checks and fixtures do not measure model quality or prove host acceptance.

## Build, validate and update

In the public repository, install development dependencies and run `python scripts/build_plugin.py` to regenerate references from canonical public sources. Run `python scripts/build_plugin.py --check` and `python -m unittest discover -s tests -p test_plugin.py -v` for static validation. Do not edit generated references. For an update, obtain a newer validated release and use your host's supported update or reinstall workflow; then repeat the new-conversation checks. The plugin folder can be used independently after generation, without the private Assistant Core.

The format follows [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins), [skills](https://developers.openai.com/plugins/build/skills), and the [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). Exact product, device and version claims require appropriate evidence; design advice does not establish runtime or hardware validation.
