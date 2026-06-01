# Organizational Cognition Runtime (OCR)

A cognitive operating system for organizations — shipments, councils, memory, ontology, and governance on a single-node stack.

## Quick Start

```bash
docker compose up -d
python scripts/generate_dashboard.py
open surfaces/executive/index.html
```

## Services

| Service | Port | Purpose |
|---------|------|---------|
| Postgres | 5432 | Cognition ledger |
| Adminer | 8080 | DB management |
| Redis | 6379 | Working memory cache |
| Ollama | 11434 | OSS LLM host |
| FastAPI | 8100 | OCR API |
| Nginx | 80 | Gateway |

## Project Structure

See `docs/build/v1_plan.md` for the full directory reference.

## Architecture

OCR treats the organization as a cognitive entity with persistent memory, shared ontology, structured deliberation (councils), and replayable decision history (shipments).

Read `raw/bronze-docs/ocr_kimi_2.6_raw_1.md` or the partitioned version in `raw/bronze-docs/ocr_kimi_2.6_raw_1/` for the full architecture specification.

## ADRs

Architectural Decision Records live in `docs/adrs/`. Start with ADR-0001.

## Rules

1. Never let architecture outrun the runtime.
2. Postgres ledger is canonical state (never filesystem).
3. Shipments are the primary primitive — not prompts, not tasks.
4. All agents are replaceable through the `AgentAdapter` interface.
