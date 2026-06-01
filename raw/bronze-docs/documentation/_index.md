---
title: "Documentation — Scraped Service Documentation"
description: "Bronze layer: scraped documentation from external services and tools, ready for agent context. Each service gets a subdirectory."
status: "active"
district: "raw/bronze-docs/documentation"
type: "neighborhood"
parent: "raw/bronze-docs"
neighbors: ["raw/bronze-docs", "raw/bronze-docs/youtube", "raw/bronze-docs/architecture_synthesis.md"]
traffic:
  reads: ["Agents loading service context", "Architecture Synthesis (cross-referencing)"]
  writes: ["Documentation scraper cron job", "Human (manual scrape)"]
blast_radius:
  services: ["All agent context loads"]
  data: ["Service documentation, API references, SDK patterns"]
  depends_on_accuracy: "medium (stale docs degrade agent performance)"
---

# Documentation — Scraped Service Documentation

Bronze layer for scraped documentation from external services. Each service
gets its own subdirectory with relevant docs, scrape metadata, and freshness
tracking.

## Reference to Architecture Synthesis

Each service documented here should be cross-referenced in
`raw/bronze-docs/architecture_synthesis.md` — the Silver layer that reasons on all
Bronze content. When adding a new service:
1. Scrape docs → store in `raw/bronze-docs/documentation/<service>/`
2. Update `raw/bronze-docs/architecture_synthesis.md` to note the service and its role

## Current Contents

- **opencode/** — OpenCode CLI documentation (docs_intro.md, docs_config.md,
  docs_skills.md, docs_agents.md, etc.)

## Ingestion Pipeline (Future Cron Job)

1. **Identify** — Determine which services need docs (new service in stack, version bump)
2. **Scrape** — Use ScraperRouter (Firecrawl → Playwright fallback) to fetch docs
3. **Store** — Save to `raw/bronze-docs/documentation/<service>/` with source URL and scrape date
4. **Reference** — Architecture Synthesis reads from here; agents load docs when context includes the service

## Doc Rot Management

Per Matt Pocock's insight: stale docs degrade agent performance more than
missing docs. Each scrape records:
- `scraped_at` timestamp in YAML frontmatter
- `version` of the documented service
- `url` source for re-scraping

When a doc exceeds its freshness window, re-scrape or flag as stale.

## Related Directories

- `raw/bronze-docs/youtube/`
- `raw/bronze-docs/architecture_synthesis.md`
- `raw/bronze-docs/`
- `ingestion/web/` — ScraperRouter handles the scraping
