# docs_rules

Source: https://opencode.ai/docs/rules/

# Rules

Rules define automated guardrails and policies for your project. They are JavaScript files that run alongside each agent action.

## Structure

```javascript
// .opencode/rules/check-secrets.js
export default function rule({ action, context }) {
  if (action.type === 'write' && action.content.includes('API_KEY')) {
    return { allow: false, reason: 'Potential secret exposure' };
  }
}
```

## API

Each rule receives:
- `action` — the tool invocation object
- `context` — project metadata, agent info, session state

Returns:
- `{ allow: true }` — allowed
- `{ allow: false, reason }` — blocked with reason
- `{ allow: false, reason, notify: true }` — blocked + user notified

## Location

Place rules in `.opencode/rules/*.js` or `.opencode/rules/**/*.js`.

## Rules vs Permissions

- **Permissions**: Static allow/deny/approve per tool
- **Rules**: Dynamic, context-aware checks (e.g., "block writes to /secrets/")
