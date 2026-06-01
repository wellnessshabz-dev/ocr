# docs_go

Source: https://opencode.ai/docs/go/

# Go

OpenCode Go is a pure Go rewrite focused on zero-dependency portability, performance, and Docker-first deployment.

## Principles

- Zero runtime dependencies (no Node.js, no Bun)
- Fast startup (<50ms cold start)
- Docker-native (scratch image, 15MB)
- Compatibility with Node edition

## Installation

```bash
curl -fsSL https://opencode.ai/install | bash -s go
```

Or via Go: `go install github.com/anomalyco/opencode-go@latest`

## CLI Parity

All TUI and CLI features match the Node edition. The Go edition can read the same config files.

## Flags

`--go` flag on existing install selects the Go edition.
