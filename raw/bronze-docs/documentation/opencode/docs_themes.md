# docs_themes

Source: https://opencode.ai/docs/themes/

# Themes

Themes customize the TUI appearance. Configurable in `~/.config/opencode/tui.json`.

## Configuration

```json
{
  "theme": {
    "primary": "#7C3AED",
    "secondary": "#3B82F6",
    "background": "#0F172A",
    "surface": "#1E293B",
    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "border": "#334155"
  }
}
```

## Built-in Themes

- Dark (default)
- Light
- High contrast

## Custom Theme

Create a theme in `~/.config/opencode/themes/` and reference it in `tui.json`.
