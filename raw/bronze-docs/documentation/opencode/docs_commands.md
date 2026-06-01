# docs_commands

Source: https://opencode.ai/docs/commands/

# Commands

Slash commands available in the TUI.

## Built-in Commands

| Command | Description |
|---------|-------------|
| `/help` | Show help |
| `/init` | Create/update AGENTS.md |
| `/connect` | Configure AI provider |
| `/model` | Switch model |
| `/compact` | Compact conversation context |
| `/clear` | Clear conversation |
| `/undo` | Undo last change |
| `/redo` | Redo last undone change |
| `/share` | Share conversation |
| `/zen` | Toggle zen mode |
| `/cost` | Show token usage/cost |

## Custom Commands

Define in config:

```json
{
  "command": {
    "deploy": "npm run deploy"
  }
}
```

Run with `/deploy`.
