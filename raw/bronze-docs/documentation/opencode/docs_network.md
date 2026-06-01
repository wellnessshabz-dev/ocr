# docs_network

Source: https://opencode.ai/docs/network/

# Network

Network configuration for opencode.

## Proxy

Respects standard env vars: `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`.

## Offline Mode

Works offline with local models (LM Studio, Ollama). Only provider API calls need network.

## mDNS Discovery

```bash
opencode serve --mdns --mdns-domain opencode.local
```
