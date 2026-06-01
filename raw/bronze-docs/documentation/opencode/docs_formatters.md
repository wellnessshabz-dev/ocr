# docs_formatters

Source: https://opencode.ai/docs/formatters/

# Formatters

Format output using formatters — shell commands that transform tool output before display.

## Configuration

```json
{
  "formatter": {
    "json": { "command": "jq ." },
    "xml": { "command": "xmllint --format -" }
  }
}
```

## Usage

Formatters apply to specific file types. The agent detects the file type and applies the matching formatter.

## Available Formatters

- Built-in: markdown, diff
- Custom: any shell command

## Pipe Behavior

Output is piped through the formatter's stdin. Formatter's stdout replaces the original output.
