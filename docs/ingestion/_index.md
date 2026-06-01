---
title: "Ingestion — Ingestion Pipeline Docs"
description: "Design docs for the web scraping, GitHub integration, Obsidian vault sync, and other ingestion channels."
status: "active"
district: "docs/ingestion"
type: "neighborhood"
parent: "docs"
neighbors: ["ingestion", "docs/architecture"]
traffic:
  reads: ["ingestion/ (implementation reference)"]
  writes: ["Humans"]
blast_radius:
  services: ["Ingestion implementation"]
  data: ["Ingestion design knowledge"]
  depends_on_accuracy: "high"
---

# 📥 Ingestion — Ingestion Pipeline Docs

This directory contains 3 files.

**Documentation:**
- `browser-automation-mcp.md`
- `github-mcp.md`
- `scrape_router.md`

## What It Reads and Writes

**Reads from:** ingestion/ (implementation reference)
**Writes to:** Humans

## How Important Is This?

**If this breaks:** Ingestion implementation will be affected.
**Data at risk:** Ingestion design knowledge.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `docs/ingestion/browser-automation-mcp.md`
- `docs/ingestion/github-mcp.md`
- `docs/ingestion/scrape_router.md`

## Related Directories

- `ingestion/`
- `docs/architecture/`

---
*Ingestion — Ingestion Pipeline Docs — part of the OCR system. See `_index.md` in this directory for orientation.*
