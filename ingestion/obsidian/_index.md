---
title: "Obsidian — Obsidian Vault Sync"
description: "Synchonizes Obsidian vault notes into the OCR ingestion pipeline."
status: "active"
district: "ingestion/obsidian"
type: "neighborhood"
parent: "ingestion"
neighbors: ["ingestion/filesystem", "ingestion/manual", "raw/bronze-docs"]
traffic:
  reads: ["Obsidian vault filesystem"]
  writes: ["shipments/compiler"]
blast_radius:
  services: ["Obsidian-based knowledge ingestion"]
  data: ["Vault sync state"]
  depends_on_accuracy: "high"
---

# 📓 Obsidian — Obsidian Vault Sync

Syncs with an Obsidian vault. Watches for note changes and extracts knowledge from markdown notes. Bridges the gap between personal knowledge management and organizational memory.

## What It Reads and Writes

**Reads from:** Obsidian vault filesystem
**Writes to:** shipments/compiler

## How Important Is This?

**If this breaks:** Obsidian-based knowledge ingestion will be affected.
**Data at risk:** Vault sync state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `ingestion/filesystem/`
- `ingestion/manual/`
- `raw/bronze-docs/`

---
*Obsidian — Obsidian Vault Sync — part of the OCR system. See `_index.md` in this directory for orientation.*
