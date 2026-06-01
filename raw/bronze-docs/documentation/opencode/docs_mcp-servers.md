# docs_mcp-servers

Source: https://opencode.ai/docs/mcp-servers/

# MCP Servers

Model Context Protocol (MCP) servers add new tools and capabilities to the agent.

## Configuration

```json
{
  "mcp": {
    "my-server": {
      "command": "node",
      "args": ["/path/to/mcp-server/index.js"],
      "env": {
        "API_KEY": "{env:MY_API_KEY}"
      }
    }
  }
}
```

## Stdio Transport

MCP servers communicate over stdio. The server process receives JSON-RPC messages on stdin and writes responses to stdout.

## Transport Options

- `stdio` (default) — spawn as subprocess
- `sse` — HTTP Server-Sent Events (planned)

## Environment Variables

Set `env` in the server config. Supports `{env:VAR}` references.
