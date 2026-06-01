# docs_custom-tools

Source: https://opencode.ai/docs/custom-tools/

# Custom Tools

Extend the agent's capabilities with custom tools via MCP servers, plugins, or inline definitions.

## Via MCP Server

Write a stdio-based MCP server in any language:

```javascript
// tools/weather-mcp.js — MCP server providing a weather tool
const readline = require('readline');
// ... JSON-RPC handler
```

Add to config:

```json
{
  "mcp": {
    "weather": {
      "command": "node",
      "args": ["tools/weather-mcp.js"]
    }
  }
}
```

## Via Plugin

NPM plugins can register tools:

```bash
npm install -g @opencode/plugin-custom-tools
```

## Tool Discovery

The agent discovers available tools from:
1. Built-in tools
2. MCP server registrations
3. Plugin registrations
