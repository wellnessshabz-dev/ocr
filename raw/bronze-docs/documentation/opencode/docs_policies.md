# docs_policies

Source: https://opencode.ai/docs/policies/

# Policies

Policies enforce provider access rules — route requests through specific gateways, restrict models, and enforce data residency.

## Configuration

```json
{
  "experimental": {
    "policies": [
      {
        "name": "only-internal",
        "match": { "model": "*" },
        "action": "block",
        "reason": "Must use internal gateway"
      }
    ]
  }
}
```

## Rules

Each policy has:
- `match` — conditions (model pattern, provider, etc.)
- `action` — `allow`, `block`, or `reroute`
- `reason` — displayed to user when blocked

## Use Cases

- Force all traffic through internal AI gateway
- Block specific models
- Route certain teams to specific providers
- Encode data residency requirements
