---
title: "Raw Docs — Reference Documentation"
description: "Raw reference documentation extracts from external sources (opencode docs, source material)."
status: "active"
district: "raw/bronze-docs"
type: "neighborhood"
parent: "raw"
neighbors: ["raw/images", "raw/skills", "docs"]
traffic:
  reads: ["All agents loading context", "docs/ (reference links)"]
  writes: ["Humans (periodic fetch/scrape)"]
blast_radius:
  services: ["None directly"]
  data: ["Reference knowledge, documentation extracts"]
  depends_on_accuracy: "medium"
---

# 📚 Raw Docs — Reference Documentation

This directory contains 6 files.

**Bronze YouTube layer:** `raw/bronze-docs/youtube/`
- `youtube/AI_Engineer/nick_nisi_building_ai_systems_that_ship.md` — Nick Nisi talk analysis
- `youtube/AI_Engineer/matt_pocock_building_ai_systems_that_ship.md` — Matt Pocock workshop analysis

**Bronze Documentation layer:** `raw/bronze-docs/documentation/` — scraped service docs (future)

**Architecture Synthesis (Silver layer):**
- `architecture_synthesis.md` — Cross-references all Bronze sources: YouTube, images, skills, documentation. Medallion overlay + LLM Wiki + Graphify + Evals as ETL.
- `ocr_kimi_2.6_raw_1.md`
- `skill_router_v1.md`

**Configuration:**
- `chairman_output_schema.json`
- `semantic_memory_fragment.json`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `ocr_kimi_2.6_raw_1/`** — OCR Kimi 2.6 Raw Export
- **📦 `documentation/opencode/`** — OpenCode Documentation (moved to documentation/)

Explore each subdirectory to learn more about that part of the system.

## What It Reads and Writes

**Reads from:** All agents loading context, docs/ (reference links)
**Writes to:** Humans (periodic fetch/scrape)

## How Important Is This?

**If this breaks:** None directly will be affected.
**Data at risk:** Reference knowledge, documentation extracts.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Quick Reference

- `raw/bronze-docs/ocr_kimi_2.6_raw_1/`
- `raw/bronze-docs/documentation/opencode/`
- `raw/bronze-docs/architecture_synthesis.md`
- `raw/bronze-docs/activation_score_formula.txt`
- `raw/bronze-docs/chairman_output_schema.json`
- `raw/bronze-docs/ocr_kimi_2.6_raw_1.md`
- `raw/bronze-docs/semantic_memory_fragment.json`
- `raw/bronze-docs/skill_router_v1.md`

## Related Directories

- `raw/images/`
- `raw/skills/`
- `docs/`

---
*Raw Docs — Reference Documentation — part of the OCR system. See `_index.md` in this directory for orientation.*
