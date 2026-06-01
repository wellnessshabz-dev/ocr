# docs_models

Source: https://opencode.ai/docs/models/

# Models

OpenCode supports 75+ LLM providers and 300+ models through AI SDK and Models.dev.

## Model Format

```
provider/model-id
```

Examples:
- `anthropic/claude-sonnet-4-20250514`
- `openai/gpt-4o`
- `google/gemini-2.5-pro`
- `groq/llama-4`

## Provider Prefixes

Common providers are preconfigured. Custom providers need a `provider` entry in config.

## Default Model

Set via `model` in config, or interactively via `/connect`.

## Models.dev

All Models.dev models are available. List them with `/models`.
