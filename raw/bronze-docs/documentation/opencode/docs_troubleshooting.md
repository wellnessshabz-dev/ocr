# docs_troubleshooting

Source: https://opencode.ai/docs/troubleshooting/

# Troubleshooting

Common issues and solutions.

## Installation

- Ensure Node.js/Bun dependencies are available
- Reinstall: `curl -fsSL https://opencode.ai/install | bash`
- Check `~/.local/share/opencode/` permissions

## Connection

- Provider not connecting? Run `/connect` again
- Behind a proxy? Set `HTTP_PROXY` / `HTTPS_PROXY`
- Firewall? Ensure outbound access to your AI provider

## Performance

- Large context? Use `/compact`
- Too many MCP servers? Each adds context — disable unused
- LSP using too much memory? Consider disabling

## Common Errors

- "Model not found" — Check ID format `provider/model`
- "Permission denied" — Check tool permissions
- "API key not configured" — Run `/connect`
