# docs_agents

Source: https://opencode.ai/docs/agents/

# Agents

Agents are reusable subagent definitions with tailored tool access, rules, and instructions.

## Define an Agent

```json
{
  "agent": {
    "my-linter": {
      "model": "anthropic/claude-sonnet-4-20250514",
      "instructions": [
        { "file": "AGENTS.md" },
        { "text": "Run linters after every write" }
      ],
      "permission": {
        "bash": "allowed",
        "write": "allowed",
        "read": "allowed",
        "edit": "allowed"
      },
      "rules": ["secrets-check"],
      "plugins": ["@opencode/plugin-eslint"]
    }
  }
}
```

## Using Agents

- The Task tool dispatches to subagents
- Agents get their own context slices
- Results are returned to the primary agent

## Agent Isolation

Agents run in isolated environments with:
- Dedicated context window
- Restricted tool access per definition
- Separate rule evaluation
- Independent plugin loading
