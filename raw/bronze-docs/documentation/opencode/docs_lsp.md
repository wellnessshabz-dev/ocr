# docs_lsp

Source: https://opencode.ai/docs/lsp/

# LSP

Language Server Protocol integration for intelligent code navigation.

## Configuration

```json
{
  "lsp": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "enabled": true
    },
    "python": {
      "command": "pyright-langserver",
      "args": ["--stdio"],
      "enabled": false
    }
  }
}
```

## Features

- Go to definition
- Find references
- Hover documentation
- Diagnostics (errors/warnings)
- Completion

## Enabling/Disabling

Per-language in config. Disable LSP for languages you don't need to reduce overhead.

## Requirements

LSP servers must be installed separately (e.g., `npm install -g typescript-language-server`).
