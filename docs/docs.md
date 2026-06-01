# OCR — Documentation Map

## Root

| File | Size | Description |
|------|------|-------------|
| `README.md` | ~1KB | Project overview, quick start, services table, rules |
| `AGENTS.md` | ~8KB | Architecture summary document — system layers, deployment, ingestion, cognition, GBrain, governance |
| `opencode_terminal_commands.md` | ~? | OpenCode terminal workflow notes |

## Build & Planning

| File | Size | Description |
|------|------|-------------|
| `docs/build/v1_plan.md` | ~3KB | Phase 1-3 build plan with execution rules, directory structure, and first success demo criteria |

## ADRs (Architectural Decision Records)

| File | Status | Description |
|------|--------|-------------|
| `docs/adrs/ADR-0001-agent-agnostic-runtime.md` | accepted | All agents implement `AgentAdapter` — no direct provider API calls |
| `docs/adrs/ADR-0002-shipment-first-cognition.md` | accepted | Shipments are the primary runtime primitive (not prompts/tasks/chats) |
| `docs/adrs/ADR-0003-ontology-lifecycle-governance.md` | accepted | Ontology nodes have a lifecycle: candidate → confirmed → dormant → archived |
| `docs/adrs/ADR-0004-replayability-requirements.md` | accepted | Every decision is replayable via session snapshots |
| `docs/adrs/ADR-0005-governance-before-autonomy.md` | accepted | Governance gates before autonomous execution — not deferred |

## Architecture Specification (`raw/bronze-docs/`)

### Monolithic Source

| File | Size | Description |
|------|------|-------------|
| `raw/bronze-docs/ocr_kimi_2.6_raw_1.md` | ~80KB | Full architecture spec — the canonical source document |
| `raw/bronze-docs/skill_router_v1.md` | ~? | Skill router design for the GStack runtime |

### Partitioned Reference (`raw/bronze-docs/ocr_kimi_2.6_raw_1/`)

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
| `raw/images/images.md` | Index of all 24 architecture diagrams with source references to partitioned files |

## Skills (`raw/skills/`)

| Directory | Description |
|-----------|-------------|
| `SKILL_MAPPING.md` | Master index of all installed skills |
| `algorithmic-art/` | Generative art with Processing/p5.js |
| `brand-guidelines/` | Brand identity design |
| `canvas-design/` | Image generation with HTML Canvas |
| `claude-api/` | Claude API integration (Python, Ruby, PHP, Java, Go, C#, curl) |
| `doc-coauthoring/` | Collaborative doc editing |
| `docx/` | DOCX generation |
| `frontend-design/` | Frontend/UI design |
| `internal-comms/` | Internal communications templates |
| `mcp-builder/` | MCP server builder (Python, Node.js references) |
| `pdf/` | PDF generation (forms, references) |
| `pptx/` | PowerPoint generation (pptxgenjs) |
| `skill-creator/` | Meta-skill for creating new skills |
| `slack-gif-creator/` | Slack GIF creation |
| `theme-factory/` | Theme/color palette generation (10 themes) |
| `web-artifacts-builder/` | Web artifacts builder |
| `webapp-testing/` | Webapp testing |
| `xlsx/` | Excel/spreadsheet generation |

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
| `agents/claude/adapter.py` | Claude stub implementatiton |
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
