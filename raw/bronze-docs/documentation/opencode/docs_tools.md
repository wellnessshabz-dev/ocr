# docs_tools

Source: https://opencode.ai/docs/tools/

# Tools

OpenCode provides tools that the AI agent can use to interact with your codebase.

## Available Tools

| Tool | Description |
|------|-------------|
| Read | Read file contents |
| Write | Create/overwrite files |
| Edit | Edit files with string replacement |
| Glob | Pattern-based file search |
| Grep | Regex content search |
| Bash | Execute shell commands |
| WebFetch | Fetch web URLs |
| WebSearch | Search the web |
| Question | Ask you questions |
| Task | Delegate subtasks to agents |
| Skill | Load specialized skills |

## Tool Permissions

Each tool can be: `allowed`, `disabled`, or require approval per use. Configured in `permission` section of config.

## Custom Tools

Tools can be added via MCP servers and plugins. See `docs_custom-tools.md`.
