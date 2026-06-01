# docs_share

Source: https://opencode.ai/docs/share/

# Share

Share your opencode conversations via URL or pastebin-style pages.

## Modes

| Mode | Behavior |
|------|----------|
| `manual` | `/share` to upload (default) |
| `auto` | Share after every message |
| `disabled` | No sharing |

## Config

```json
{
  "share": "manual"
}
```

## Server

Self-host the share server:

```bash
opencode serve --share-server --port 4096
```

Sets `OPENCODE_SHARE_SERVER` env variable.

## Privacy

Share uploads contain your conversation text and file diffs. Code is not stored — only what appears in the conversation.
