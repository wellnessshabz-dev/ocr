---
title: "Documentation Map — Library Inventory"
description: "Complete inventory of all documentation files in the OCR library. Every file is tracked: location, size, purpose, and relationships."
status: "active"
district: "docs"
type: "map"
maintainer: "shadabkhan"
update_frequency: "monthly"
total_entries: 30
related_maps:
  - "CITY_MAP.md (district atlas)"
  - "raw/images/images.md (diagram index)"
  - "raw/bronze-docs/documentation/opencode/_maintenance.md (opencode docs)"
sources:
  - "agents.md"
  - "all files under docs/"
  - "raw/bronze-docs/ocr_kimi_2.6_raw_1/"
---

# 📚 Documentation Map — Library Inventory

> Every file in the Library district (`docs/`) tracked with location, purpose, and relationships. Supplemented by `CITY_MAP.md` for overall district atlas and `raw/images/images.md` for diagram provenance.

## Root Documents

| File | Size | Description |
|------|------|-------------|
| `README.md` | ~1KB | Project overview, quick start, services table, rules |
| `AGENTS.md` | ~8KB | Architecture constitution — system layers, deployment, ingestion, cognition, GBrain, governance |
| `CITY_MAP.md` | ~12KB | District atlas — every directory mapped with blast radius, transit lines, naming |
| `opencode_terminal_commands.md` | ~? | OpenCode terminal workflow notes |

## Build & Planning

| File | Size | Description |
|------|------|-------------|
| `docs/build/v1_plan.md` | ~3KB | Phase 1-3 build plan with execution rules, directory structure, and first success demo criteria |

## ADRs (Architecture Decision Records)

All ADRs are accepted. Each captures a foundational design decision.

| File | Description |
|------|-------------|
| `docs/adrs/ADR-0001-agent-agnostic-runtime.md` | All agents implement `AgentAdapter` — no direct provider API calls |
| `docs/adrs/ADR-0002-shipment-first-cognition.md` | Shipments are the primary runtime primitive (not prompts/tasks/chats) |
| `docs/adrs/ADR-0003-ontology-lifecycle-governance.md` | Ontology nodes have a lifecycle: candidate → confirmed → dormant → archived |
| `docs/adrs/ADR-0004-replayability-requirements.md` | Every decision is replayable via session snapshots |
| `docs/adrs/ADR-0005-governance-before-autonomy.md` | Governance gates before autonomous execution — not deferred |

## Architecture Specification (`raw/bronze-docs/`)

### Monolithic Source

| File | Size | Description |
|------|------|-------------|
| `raw/bronze-docs/ocr_kimi_2.6_raw_1.md` | ~80KB | Full architecture spec — the canonical source document |
| `raw/bronze-docs/skill_router_v1.md` | ~? | Skill router design for the GStack runtime |

### Partitioned Reference (`raw/bronze-docs/ocr_kimi_2.6_raw_1/`)

22 numbered files covering the full architecture from system overview through roadmap.

| # | File | Topic |
|---|------|-------|
| 000 | `000_frontmatter.md` | Title, author, status, toc |
| 01 | `01_system_overview_architecture.md` | High-level system architecture |
| 02 | `02_cognition_runtime_architecture.md` | Cognition runtime overview |
| 03 | `03_shipment_architecture.md` | Shipment as atomic cognition unit |
| 04 | `04_gstack_skill_activation_runtime.md` | GStack skill runtime + activation formula |
| 05 | `05_council_architecture.md` | Council deliberation protocol |
| 06 | `06_gbrain_memory_architecture.md` | GBrain memory substrate layers |
| 07 | `07_ontology_architecture.md` | Ontology graph + lifecycle |
| 08 | `08_trajectory_modeling.md` | Trajectory modeling (decision history) |
| 09 | `09_repo_changes_and_organizational_state.md` | Commit → org state mapping |
| 10 | `10_executive_cognition_surfaces.md` | Executive dashboard, podcast, Q engine |
| 11 | `11_podcast_notebooklm_style_synthesis.md` | Podcast-style audio synthesis |
| 12 | `12_n8n_dag_architecture.md` | n8n orchestration DAG design |
| 13 | `13_graph_schema.md` | Graph database schema (Neo4j) |
| 14 | `14_replayability_and_lineage.md` | Replayability and decision lineage |
| 15 | `15_governance_and_auditability.md` | Governance checks, audit ledger, policies |
| 16 | `16_mcp_ingestion_security.md` | MCP ingestion, security, scoping |
| 17 | `17_obsidian_repo_evolution_linkage.md` | Obsidian vault → repo evolution linkage |
| 18 | `18_semantic_persistence.md` | Semantic persistence patterns |
| 19 | `19_multi_tenant_cognition.md` | Multi-tenant cognition architecture |
| 20 | `20_deployment_architecture.md` | Single-node VPS deployment |
| 21 | `21_the_long_term_moat.md` | Long-term moat and differentiation |
| 22 | `22_roadmap_evolution.md` | Roadmap and evolution |
| 999 | `999_closing_principles.md` | Closing principles |

### Reference Data

| File | Description |
|------|-------------|
| `raw/bronze-docs/activation_score_formula.txt` | `ActivationScore(skill, shipment) = w1*OntologyOverlap + w2*TrajectoryRelevance + w3*CouncilBalance + w4*PriorContribution` |
| `raw/bronze-docs/chairman_output_schema.json` | JSON schema for council chairman synthesis output |
| `raw/bronze-docs/semantic_memory_fragment.json` | Example semantic memory record in GBrain |

### Diagram Index

| File | Description |
|------|-------------|
| `raw/images/images.md` | Index of all 24 architecture diagrams with source references, layer mapping, and reading order |

## Ingestion Design

| File | Description |
|------|-------------|
| `docs/ingestion/github-mcp.md` | Full GitHub MCP research: 19 toolsets breakdown, what one call returns, ontology mapping, OCR configuration, and the read-only ingestion pipeline |
| `docs/ingestion/browser-automation-mcp.md` | Browser control MCP landscape: Playwright vs Firecrawl vs alternatives, when to use which, what one call returns, and OCR's two-server strategy for documentation scraping |
| `docs/ingestion/scraper.md` | Intelligent Scraper Router design: URL pattern matching, quality checks, Firecrawl → Playwright fallback flow, and configuration |

## V1 Build Artifacts

| File | Description |
|------|-------------|
| `surfaces/executive/index.html` | Auto-generated HTML cognition map (run `python3 scripts/generate_dashboard.py`) |
| `ledger/schemas/001_init.sql` | PostgreSQL schema — 8 tables + triggers |
| `ledger/schemas/002_web_ingestion.sql` | Web ingestion schema — `web_sessions`, `web_pages`, `ontology_feeds` |
| `agents/adapters/base.py` | AgentAdapter ABC + dataclasses |
| `agents/claude/adapter.py` | Claude stub implementation |
| `ingestion/web/adapter.py` | WebAdapter ABC + dataclasses (scrape, crawl, search, extract, interact) |
| `ingestion/web/firecrawl.py` | FirecrawlAdapter stub for cloud web scraping |
| `ingestion/web/playwright.py` | PlaywrightAdapter stub for browser automation |
| `ingestion/web/scraper.py` | ScraperRouter — intelligent tool selector with URL pattern matching, quality checks, and Firecrawl → Playwright fallback |
| `src/main.py` | FastAPI application entry point |
| `src/routers/ingestion.py` | Web ingestion API: 5 POST endpoints |
| `infra/docker/fastapi.Dockerfile` | FastAPI container build |
| `infra/nginx/nginx.conf` | Nginx reverse proxy config |
| `docker-compose.yml` | 6 services (postgres, adminer, redis, ollama, fastapi, nginx) |
| `requirements.txt` | Python dependencies |
| `.env` | Environment variables (dev defaults) |
| `scripts/generate_dashboard.py` | Dashboard generator script |

## File Relationships

```
agents.md ─────────────────────────────────────────────────────────┐
   │                                                                │
   ├── references raw/bronze-docs/ocr_kimi_2.6_raw_1.md (source material)  │
   ├── references raw/images/images.md (diagrams)                    │
   ├── references CITY_MAP.md (city atlas)                           │
   └── is referenced by all agent definitions in agents/             │
                                                                     │
docs/adrs/ ─── 5 ADRs defining core architectural decisions          │
   └── are implemented by code in cognition/, shipments/, gbrain/    │
                                                                     │
docs/ingestion/ ─── design docs                                      │
   └── are implemented by code in ingestion/web/                     │
                                                                     │
raw/bronze-docs/ ─── raw reference material                                 │
   └── is the source from which agents.md was synthesized            │
                                                                     │
raw/images/images.md ─── diagram index                                │
   └── maps 24 diagrams back to their source files in raw/bronze-docs/      │
```

## Maintenance

When adding a new document:
1. Add the file to the appropriate `docs/` subdirectory
2. Update this map (`docs_map.md`) with the new entry
3. Update the neighborhood `_index.md` if it's a new type of document
4. Update `CITY_MAP.md` if a new district or significant neighborhood is added
