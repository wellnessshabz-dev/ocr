# docs_windows-wsl

Source: https://opencode.ai/docs/windows-wsl/

# Windows (WSL)

Run OpenCode on Windows using WSL for best performance.

## Setup

1. Install WSL
2. Install in WSL: `curl -fsSL https://opencode.ai/install | bash`
3. Access Windows files via `/mnt/c/`, `/mnt/d/`

## Desktop + WSL Server

```bash
# WSL:
opencode serve --hostname 0.0.0.0 --port 4096
# Connect Desktop app to http://localhost:4096
```

Set `OPENCODE_SERVER_PASSWORD` for security with `--hostname 0.0.0.0`.

## Web + WSL

```bash
# In WSL (not PowerShell):
opencode web --hostname 0.0.0.0
# Access from Windows browser
```

## Tips

- Clone repos into WSL filesystem for best performance
- Use VS Code WSL extension alongside OpenCode
- Config stored in WSL at `~/.local/share/opencode/`
