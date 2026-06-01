---
title: "Port Authority — Ingestion Layer"
description: "All signal intake: GitHub events, Obsidian vault changes, LLM wiki updates, web scraping, manual inputs."
status: "active"
district: "ingestion"
type: "district"
child_districts: ["filesystem", "github", "manual", "obsidian", "web"]
neighbors: ["shipments", "ontology", "orchestration"]
traffic:
  reads: ["External sources (GitHub API, Obsidian vault, web pages)"]
  writes: ["shipments/compiler (normalized events)", "ontology/extraction (candidate nodes)"]
blast_radius:
  services: ["All downstream processing stops if ingestion fails"]
  data: ["Raw incoming signals", "Normalized OCR events"]
  depends_on_accuracy: "high (garbage in = garbage out)"
connections:
  - direction: "upstream"
    to: "External world"
    via: "GitHub MCP, Obsidian sync, web scrapers"
    purpose: "Signals enter the city here"
  - direction: "downstream"
    to: "shipments/compiler"
    via: "Normalized OCR events"
    purpose: "Raw signals become structured shipments"
  - direction: "downstream"
    to: "ontology/extraction"
    via: "Entity candidate extraction"
    purpose: "New concepts discovered in signals"
naming:
  pattern: "snake_case"
  rules:
    - "One module per signal source"
    - "Web scraper files named after the target type"
partitioning:
  rule: "By signal source: filesystem, github, manual, obsidian, web"
maintainers: ["shadabkhan"]
---

# 📥 Port Authority — Ingestion Layer

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📁 `filesystem/`** — Filesystem — File System Ingestion
- **🐙 `github/`** — GitHub — GitHub MCP Integration
- **✍️ `manual/`** — Manual — Manual Signal Injection
- **📓 `obsidian/`** — Obsidian — Obsidian Vault Sync
- **🌐 `web/`** — Web — Web Scraping Engine

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** External world (via GitHub MCP, Obsidian sync, web scrapers) — Signals enter the city here
- ➡️ **Sends to** shipments/compiler (via Normalized OCR events) — Raw signals become structured shipments
- ➡️ **Sends to** ontology/extraction (via Entity candidate extraction) — New concepts discovered in signals

## What It Reads and Writes

**Reads from:** External sources (GitHub API, Obsidian vault, web pages)
**Writes to:** shipments/compiler (normalized events), ontology/extraction (candidate nodes)

## How Important Is This?

**If this breaks:** All downstream processing stops if ingestion fails will be affected.
**Data at risk:** Raw incoming signals, Normalized OCR events.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `ingestion/filesystem/`
- `ingestion/github/`
- `ingestion/manual/`
- `ingestion/obsidian/`
- `ingestion/web/`

## Related Directories

- `shipments/`
- `ontology/`
- `orchestration/`

---
*Port Authority — Ingestion Layer — part of the OCR system. See `_index.md` in this directory for orientation.*
