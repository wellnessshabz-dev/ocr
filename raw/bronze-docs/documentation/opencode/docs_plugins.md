# docs_plugins

Source: https://opencode.ai/docs/plugins/

# Plugins

Extend OpenCode with NPM plugins that add tools, commands, formatters, themes, and more.

## Install Plugin

```bash
opencode plugin add @opencode/plugin-eslint
```

Or manually add to config:

```json
{
  "plugin": ["@opencode/plugin-eslint", "@opencode/plugin-prettier"]
}
```

## Plugin Capabilities

- Register tools
- Register commands
- Register formatters
- Register themes
- Provide MCP servers
- Hook into lifecycle events

## Ecosystem

See `docs_ecosystem.md` for available plugins and community contributions.
