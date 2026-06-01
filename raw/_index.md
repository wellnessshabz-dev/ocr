---
title: "Bronze — Raw Ingestion Layer"
description: "The entire Bronze layer of the Medallion architecture. Everything consumed — commits, web pages, cloned repos, docs, transcripts — fed into gbrain for Silver processing and Gold query."
status: "active"
district: "raw"
type: "district"
child_districts: ["bronze-docs", "images", "skills", "repos"]
neighbors: ["docs", "ingestion", "cognition/skills", "gbrain"]
traffic:
  reads: ["gbrain (ingests pages)", "docs/ (reference links)"]
  writes: ["Humans (periodic updates)", "Ingestion pipelines (automated)"]
blast_radius:
  services: ["gbrain ingestion pipeline"]
  data: ["All raw reference knowledge, source code snapshots, skill templates"]
  depends_on_accuracy: "medium (stale refs cause stale brain answers)"
connections:
  - direction: "downstream"
    to: "gbrain/"
    via: "gbrain put_page"
    purpose: "Every file here gets ingested into the brain for Silver processing"
  - direction: "peer"
    to: "ingestion/"
    via: "Same Bronze layer"
    purpose: "ingestion/ produces live data, raw/ holds reference data"
naming:
  pattern: "Descriptive, underscores for spaces"
partitioning:
  rule: "By content type: bronze-docs, images, skills, repos"
maintainers: ["shadabkhan"]
---

# Bronze — Raw Ingestion Layer

## What Lives Here

This is the **Bronze layer** of OCR's Medallion architecture. Everything here
is append-only and immutable. It feeds into gbrain (Silver layer) for
processing.

| Subdirectory | What's in it |
|-------------|-------------|
| `bronze-docs/` | Architecture design docs, YouTube transcripts, research |
| `images/` | Architecture diagrams (PNG format) |
| `skills/` | Skill templates (opencode skills reference) |
| `repos/gstack/` | Cloned garrytan/gstack (104K★ skill runtime) |
| `repos/gbrain/` | Cloned garrytan/gbrain (20K★ agent brain) |

## How It Gets Into the Brain

All data here eventually gets ingested into gbrain via:

| Source | Ingestion method | gbrain source |
|--------|-----------------|---------------|
| GitHub commits | `ingestion/github/` (GitHubAdapter) | `--source github` |
| Web pages | `ingestion/web/` (ScraperRouter) | `--source web` |
| Cloned repos | Manual `gbrain put_page` | `--source repos` |
| Bronze docs | Manual `gbrain put_page` | `--source docs` |
| YouTube transcripts | Manual `gbrain put_page` | `--source youtube` |

## Medallion Role — Bronze Layer

This is the **Bronze layer**. Rules:

- **Append-only.** Never edit in place. New versions go alongside old ones.
- **No validation.** Accept everything. Let Silver clean it.
- **Keep everything.** The original is the source of truth.

gbrain (Silver layer) reads from here, extracts entities, builds the
knowledge graph, and answers questions. See `docs/architecture/bronze-silver-gold-pipeline.md`
for the full architecture.

## Related Directories

- `docs/architecture/bronze-silver-gold-pipeline.md` — Full architecture doc
- `ingestion/` — Live ingestion pipelines (same Bronze layer)
- `raw/repos/gbrain/_index.md` — gbrain reference understanding
- `raw/repos/gstack/_index.md` — gstack reference understanding
