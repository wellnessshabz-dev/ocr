# docs_keybinds

Source: https://opencode.ai/docs/keybinds/

# Keybinds

Keyboard shortcuts for the TUI. Customizable in `~/.config/opencode/tui.json`.

## Default Keybinds

| Key | Action |
|-----|--------|
| `Ctrl+N` | New conversation |
| `Ctrl+D` | Delete conversation |
| `Ctrl+L` | Clear conversation |
| `Tab` | Toggle Act/Plan mode |
| `Ctrl+P` | Toggle preview |
| `z` | Toggle zen mode |
| `Ctrl+K` | Command palette |
| `Ctrl+O` | Open file |
| `Ctrl+Shift+F` | Find in files |
| `Ctrl+B` | Toggle sidebar |
| `Esc` | Focus input |
| `Ctrl+C` | Cancel / interrupt |
| `Ctrl+W` | Close panel |

## Customization

```json
{
  "keys": {
    "new-conversation": ["ctrl+n"],
    "toggle-mode": ["tab", "ctrl+m"]
  }
}
```

Key names follow standard terminal key names.
