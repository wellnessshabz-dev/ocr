# docs_server

Source: https://opencode.ai/docs/server/

# Server Mode

Run OpenCode as a headless server to connect from the Desktop app, web UI, or remote clients.

## Start Server

```bash
opencode serve
```

## Options

| Flag | Description |
|------|-------------|
| `--port` | Port (default: 4096) |
| `--hostname` | Bind address (default: `localhost`) |
| `--password` | Set `OPENCODE_SERVER_PASSWORD` |
| `--mdns` | Enable mDNS discovery |
| `--mdns-domain` | mDNS domain (default: `opencode.local`) |
| `--share-server` | Also serve shared conversations |

## Connecting

Desktop app: File > Connect to Server > `http://localhost:4096`

WSL + Windows: Server in WSL, Desktop connects to `http://localhost:4096`.

## Security

- Default: localhost only
- Remote: requires `--hostname 0.0.0.0` and `OPENCODE_SERVER_PASSWORD`
- All traffic over WebSocket with optional TLS
