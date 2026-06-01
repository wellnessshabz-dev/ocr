---
title: "OCR City Map — Complete District Atlas"
description: "The full atlas of every district, neighborhood, transit line, and blast radius in the OCR codebase."
status: "active"
maintainer: "shadabkhan"
update_frequency: "monthly"
primary_index: "_index.md"
constitution: "agents.md"
districts: 17
neighborhoods: 52
total_index_files: 72
---

# 🏙️ OCR City Map

> **The codebase as a city. Every directory is a district. Every `_index.md` is a neighborhood signpost. `agents.md` is the constitution.**

## Quick Reference

| District | Alias | Type | Neighborhoods | Blast Radius | Status |
|----------|-------|------|---------------|-------------|--------|
| `agents/` | Embassy Row | Agent defs | 4 | Agent behavior | active |
| `cognition/` | Parliament | Reasoning engine | 4 | All decisions | active |
| `docs/` | Library | Documentation | 6 | None (docs) | active |
| `gbrain/` | Memory Palace | Memory substrate | 5 | All memory state | active |
| `infra/` | Utilities | Infrastructure | 3 | All services | active |
| `ingestion/` | Port Authority | Signal intake | 5 | All downstream processing | active |
| `ledger/` | Treasury | Audit trail | 3 | Audit integrity | active |
| `observability/` | Watchtower | Telemetry | 4 | Monitoring | active |
| `ontology/` | Map Room | Concept graph | 4 | All ontology state | active |
| `orchestration/` | Transit Authority | Workflow routing | 3 | All pipeline routing | active |
| `raw/` | Archive | Reference data | 3 | None (refs) | active |
| `replay/` | Timekeeper | Decision replay | 0 | Audit/debugging | active |
| `scripts/` | Maintenance Shed | Utilities | 0 | Dev environments | active |
| `shipments/` | Cargo Depot | Shipment pipeline | 5 | All shipment state | active |
| `src/` | City Center | FastAPI server | 2 | API availability | active |
| `surfaces/` | Town Square | User interfaces | 4 | Presentation | active |
| `tests/` | Inspection Yard | Quality | 2 | CI gates | active |

## Data Flow (Transit Lines)

### Primary Flow (Signal → Cognition → Surface)

```
External Signals
     │
     ▼
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌─────────┐    ┌──────────┐
│  ingestion/  │───▶│  shipments/  │───▶│ cognition/ │───▶│ gbrain/ │───▶│ surfaces/│
│  Port Auth   │    │  Cargo Depot │    │ Parliament │    │ Memory  │    │ Town Sq  │
└─────────────┘    └──────────────┘    └────────────┘    └─────────┘    └──────────┘
     │                   │                   │                │               │
     │     ┌─────────────┘                   │                │               │
     │     │     ┌────────────────────────────┘                │               │
     │     │     │     ┌───────────────────────────────────────┘               │
     ▼     ▼     ▼     ▼                                                       │
┌──────────────────────────────────────────────────────────────────────────────┘
│  orchestration/  (n8n — Transit Authority: routes everything)
└──────────────────────────────────────────────────────────────────────────────
     │
     ▼
┌──────────────┐    ┌─────────────────┐
│   ledger/    │    │ observability/  │
│   Treasury   │    │  Watchtower     │
└──────────────┘    └─────────────────┘
```

### District-Level Traffic Map

```
ingestion/github ──► shipments/compiler ──► cognition/councils ──► gbrain/episodic
ingestion/web    ──► shipments/compiler ──► cognition/skills    ──► gbrain/semantic
ingestion/obsidian──► ontology/extraction──► cognition/chairman ──► gbrain/temporal
                                       │                        │
                                       ▼                        ▼
                                ontology/graph            gbrain/activation
                                       │                        │
                                       ▼                        ▼
                                ontology/lifecycle       gbrain/replay
                                                                │
                                                                ▼
                                                          replay/
```

## Neighborhood Detail

### `agents/` — Embassy Row (4 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `adapters/` | MCP wrappers for external tools |
| `claude/` | Claude Code persona defs |
| `codex/` | Codex persona defs |
| `kimi/` | Kimi persona defs |

### `cognition/` — Parliament (4 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `chairman/` | Synthesis: contradiction detection, consensus, draft generation |
| `councils/` | Deliberation orchestrator: skill routing, round management |
| `governance/` | Validation, policy engine, access control, escalation |
| `skills/` | Skill protocol registry (Strategic, Technical, Risk, etc.) |

### `docs/` — Library (6 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `adrs/` | Architecture Decision Records (5 ADRs) |
| `architecture/` | Deep-dive architecture docs |
| `build/` | Build and dev guides |
| `governance/` | Governance policy docs |
| `ingestion/` | Ingestion pipeline design |
| `ontology/` | Ontology schema docs |

### `gbrain/` — Memory Palace (5 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `activation/` | Memory activation protocol |
| `episodic/` | Shipment/deliberation history |
| `replay/` | Memory snapshots and restore |
| `semantic/` | Live ontology graph state engine |
| `temporal/` | Trajectories, recency, decay |

### `infra/` — Utilities (3 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `compose/` | Docker Compose orchestration |
| `docker/` | Per-service Dockerfiles |
| `nginx/` | Reverse proxy configs |

### `ingestion/` — Port Authority (5 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `filesystem/` | Filesystem watcher |
| `github/` | GitHub MCP event handler |
| `manual/` | Manual signal injection |
| `obsidian/` | Obsidian vault sync |
| `web/` | Web scraping (ScraperRouter) |
| `web/_scrapling.md` | Scrapling integration analysis |

### `ledger/` — Treasury (3 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `migrations/` | DB migration files |
| `schemas/` | SQL schema definitions |
| `seeds/` | Seed data for dev/testing |

### `observability/` — Watchtower (4 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `audits/` | Audit-specific observability |
| `logs/` | Structured logging |
| `metrics/` | Prometheus metrics |
| `traces/` | OpenTelemetry tracing |

### `ontology/` — Map Room (4 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `contradictions/` | Contradiction detection |
| `extraction/` | Entity extraction from signals |
| `graph/` | Neo4j graph CRUD |
| `lifecycle/` | Node lifecycle (candidate→confirmed→archived) |

### `orchestration/` — Transit Authority (3 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `dags/` | n8n DAG definitions |
| `n8n/` | n8n workflow exports |
| `triggers/` | Event trigger patterns |

### `raw/` — Archive (3 neighborhoods + 17 skill subdirectories)

| Neighborhood | Purpose |
|-------------|---------|
| `raw/bronze-docs/` | Reference doc extracts (opencode, OCR raw) |
| `raw/images/` | 24 architecture diagrams |
| `raw/skills/` | 17 skill template directories |

### `shipments/` — Cargo Depot (5 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `compiler/` | Context building, entity extraction |
| `replay/` | Shipment replay for debugging |
| `schemas/` | Shipment data schemas |
| `storage/` | Shipment persistence |
| `validator/` | Scope, completeness, signature checks |

### `src/` — City Center (2 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `api/` | Core FastAPI logic, middleware, deps |
| `routers/` | Route handlers per resource |

### `surfaces/` — Town Square (4 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `executive/` | Dashboard, strategic Q engine |
| `ontology/` | Ontology graph browser |
| `replay/` | Timeline browser |
| `shipments/` | Shipment tracker |

### `tests/` — Inspection Yard (2 neighborhoods)

| Neighborhood | Purpose |
|-------------|---------|
| `unit/` | Module-level unit tests |
| `integration/` | End-to-end integration tests |

### `ocr/tracking/` — Session Log & Checkpoint System (1 neighborhood)

| Neighborhood | Purpose |
|-------------|---------|
| `tracking/` | Session tracking, decision log, checkpoint registry. See `ocr/tracking/PROTOCOL.md` |

**Traffic:** Agents read/write SESSION.md per session; LOG.md and DECISIONS.md are append-only; CHECKPOINTS.md maps ckpt steps to git hashes.

## Blast Radius Summary

| Severity | Districts | What breaks |
|----------|-----------|-------------|
| 🔴 **Critical** | `cognition/`, `gbrain/`, `ontology/`, `shipments/`, `ledger/`, `orchestration/`, `src/`, `infra/` | Data loss, service outage, wrong decisions |
| 🟡 **High** | `agents/`, `ingestion/`, `tests/` | Agent misbehavior, missing signals, false CI |
| 🟢 **Medium** | `observability/`, `replay/`, `surfaces/` | Blindness, can't debug, display bugs |
| 🟡 **Medium** | `ocr/tracking/` | Lost session context, confused agents on resume |
| ⚪ **Low** | `docs/`, `raw/`, `scripts/` | Confusion, wasted dev time |

## Naming Conventions

| Scope | Convention | Example |
|-------|-----------|---------|
| Directories | `snake_case`, singular noun | `shipments/`, `cognition/`, `ontology/` |
| Python files | `snake_case` | `scraper_router.py`, `firecrawl_adapter.py` |
| Config files | `kebab-case` or `YAML` | `docker-compose.yml`, `nginx.conf` |
| Markdown docs | Descriptive, `_` prefix for meta | `_index.md`, `_maintenance.md`, `images.md` |
| ADRs | `ADR-NNNN-<title>.md` | `ADR-0001-agent-agnostic-runtime.md` |
| Migrations | `NNN_<name>.sql` | `001_init.sql` |
| Tests | `test_<module>.py` | `test_scraper.py` |

## Maintenance Rules

1. **Every district gets an `_index.md`** — signpost with frontmatter (title, blast radius, traffic, connections)
2. **Every `_index.md` follows the same YAML schema** — no custom fields per district
3. **Deep reference maps (`*_map.md`, `images.md`, etc.)** supplement `_index.md` with detailed inventory — never replace it
4. **Blast radius must be honest** — if changing a file *could* break a service, document it
5. **CITY_MAP.md is the atlas** — update when districts are added/removed/renamed
6. **agents.md is the constitution** — it drives agent behavior; CITY_MAP.md is for navigation
7. **No cognitive logic in n8n** — orchestration routes only
8. **No orphan decisions** — every shipment must trace through governance
