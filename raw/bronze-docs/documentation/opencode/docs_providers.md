# docs_providers

Source: https://opencode.ai/docs/providers/

# Providers

OpenCode supports 75+ LLM providers via AI SDK and Models.dev. Most popular providers are preloaded — add credentials via `/connect`.

## Custom Provider

```json
{
  "provider": {
    "my-custom": {
      "baseUrl": "https://my-provider.com/v1",
      "apiKey": "{env:MY_API_KEY}",
      "models": { "my-model": {} }
    }
  }
}
```

## Local Models (LM Studio)

```json
{
  "provider": {
    "lmstudio": {
      "baseUrl": "http://localhost:1234/v1",
      "models": { "model-name": {} }
    }
  }
}
```

## Authentication

`/connect` walks through provider setup. Supports API keys, OAuth, and `{env:VAR}` references.
