# docs_acp

Source: https://opencode.ai/docs/acp/

# ACP

Agent Communication Protocol — allows multiple AI agents to discover, negotiate with, and delegate tasks to each other.

## Features

- Agent discovery and capability advertisement
- Task negotiation and delegation
- Result aggregation
- Multi-agent workflows

## Configuration

```json
{
  "acp": {
    "enabled": true,
    "port": 4097
  }
}
```

## Protocol

ACP agents advertise capabilities and accept delegated tasks. The orchestrator agent negotiates task assignment based on capability matching.

## Use Cases

- Multi-agent code review
- Parallel task execution
- Specialized agent delegation
