# docs_permissions

Source: https://opencode.ai/docs/permissions/

# Permissions

Control tool access with three levels: `allowed`, `disabled`, or `approval` (confirm per use).

## Configuration

```json
{
  "permission": {
    "bash": "allowed",
    "write": "approval",
    "edit": "approval",
    "delete": "disabled",
    "glob": "allowed",
    "grep": "allowed",
    "read": "allowed",
    "web": "allowed"
  }
}
```

## Scopes

Permissions can be scoped per-agent in agent definitions, or globally.

## Permission Bypass

In `--dangerously-skip-permissions` mode, all permissions are allowed.

## Approval Flow

When set to `approval`, you get a prompt: "Allow tool X?" with option to approve once, approve always, or deny.
