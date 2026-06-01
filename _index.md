---
title: "OCR — City Hall Index"
description: "Root index for the Organizational Cognition Runtime codebase. This is the zoning map for the entire city."
status: "active"
district: "root"
type: "landmark"
child_districts:
  - "agents"
  - "cognition"
  - "docs"
  - "gbrain"
  - "infra"
  - "ingestion"
  - "ledger"
  - "observability"
  - "ontology"
  - "orchestration"
  - "raw"
  - "replay"
  - "scripts"
  - "shipments"
  - "src"
  - "surfaces"
  - "tests"
neighbors: []
traffic:
  reads: ["All agents and tools entering the codebase"]
  writes: ["n8n orchestration", "human developers", "opencode agent"]
blast_radius:
  services: ["Entire OCR runtime"]
  data: ["All ontology, memory, audit state"]
  depends_on_accuracy: "critical"
connections:
  - direction: "upstream"
    to: "External signals (GitHub, Obsidian, Web)"
    via: "ingestion/ layer"
    purpose: "Raw signals enter the city here"
  - direction: "downstream"
    to: "Executive surfaces"
    via: "surfaces/ -> src/ -> cognition/ pipeline"
    purpose: "Processed cognition surfaces to humans"
naming:
  pattern: "snake_case for directories, snake_case for Python files, kebab-case for config"
  rules:
    - "Directories are singular nouns (agent/, not agents/)"
    - "Python modules use snake_case"
    - "Config files use kebab-case or YAML"
partitioning:
  rule: "Domain-driven: one directory per bounded context"
  exceptions:
    - "raw/ holds unstructured reference data, not runtime code"
    - "tests/ mirrors the source structure one-to-one"
maintainers: ["shadabkhan"]
update_frequency: "monthly"
primary_index: "agents.md"
---

# 🏙️ OCR City — Zoning Map

> **Every directory is a district. Every `_index.md` is a neighborhood signpost. AGENTS.md is the constitution.**

## The City Layout

```
ocr/                              ← City Hall (you are here)
├── agents.md                     ← Constitution (architecture, rules, philosophy)
├── agents/                       ← Embassy Row (definitions of each agent persona)
├── cognition/                    ← Parliament (deliberation, skills, governance)
├── docs/                         ← Library (architecture docs, ADRs, build guides)
├── gbrain/                       ← Memory Palace (semantic, episodic, temporal memory)
├── infra/                        ← Utilities (Docker, n8n, nginx, compose)
├── ingestion/                    ← Port Authority (GitHub, Obsidian, Web scraping)
├── ledger/                       ← Treasury (audit log, schemas, migrations)
├── observability/                ← Watchtower (logs, metrics, traces, audits)
├── ontology/                     ← Map Room (concept graph, extraction, lifecycle)
├── orchestration/                ← Transit Authority (n8n DAGs, triggers)
├── raw/                          ← Archive (reference docs, raw extracts, skills)
├── replay/                       ← Timekeeper (replay manager)
├── scripts/                      ← Maintenance Shed (utility scripts)
├── shipments/                    ← Cargo Depot (compilation, validation, storage)
├── src/                          ← City Center (API, routers)
├── surfaces/                     ← Town Square (executive dashboard, ontology viewer)
└── tests/                        ← Inspection Yard (unit, integration)
```

## Transit (Data Flow)

```
Ingestion → Shipments → Cognition → GBrain → Surfaces
     ↑          ↑           ↑           ↑
     └──── n8n Orchestration ───────────┘
                     ↓
              Governance & Audit (ledger/ + observability/)
```

## Rules of the City

1. **Every district has an `_index.md`** — describes what's inside, blast radius, connections
2. **No file touches another district without passing through its `_index.md` contract**
3. **AGENTS.md is the constitution** — all agents and skills defer to it
4. **Naming is consistent** — snake_case for code, kebab-case for config, descriptive for docs
5. **Blast radius is documented** — if you modify a district, you know who gets flooded
