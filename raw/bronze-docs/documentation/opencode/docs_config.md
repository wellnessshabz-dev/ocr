# docs_config

Source: https://opencode.ai/docs/config/

# Config

Configure opencode via `opencode.json` (project) or `~/.config/opencode/opencode.json` (global).

## Precedence

1. CLI flags
2. Project config (`opencode.json`)
3. Global config (`~/.config/opencode/opencode.json`)
4. Built-in defaults

## Key Config Options

| Option | Description |
|--------|-------------|
| `model` | Default model (e.g., `anthropic/claude-sonnet-4-20250514`) |
| `agent` | Agent definitions with permissions |
| `permission` | Tool access control |
| `mcp` | MCP server configs |
| `lsp` | LSP server configs |
| `formatter` | Formatter configs |
| `command` | Custom slash commands |
| `instruction` | Additional instruction files |
| `plugin` | NPM plugins to load |
| `share` | Sharing mode (`manual`, `auto`, `disabled`) |
| `experimental.policies` | Provider access policies |
| `provider` | Provider/model configuration |
| `theme` | UI theme (in `tui.json`) |

## Schemas

- Config: `https://opencode.ai/config.json`
- TUI: `https://opencode.ai/tui.json`
