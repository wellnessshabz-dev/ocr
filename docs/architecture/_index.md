---
title: "Architecture — System Architecture Docs"
description: "Deep-dive architecture documentation for OCR subsystems."
status: "active"
district: "docs/architecture"
type: "neighborhood"
parent: "docs"
neighbors: ["docs/adrs", "docs/build", "agents.md"]
traffic:
  reads: ["All agents (context loading)"]
  writes: ["Humans"]
blast_radius:
  services: ["None directly"]
  data: ["Architecture knowledge"]
  depends_on_accuracy: "high"
---

# 🏗️ Architecture — System Architecture Docs

Deep-dive architecture documentation explaining how each OCR subsystem works, the design decisions behind it, and how to extend it. These are reference docs for developers working on the system.

## What It Reads and Writes

**Reads from:** All agents (context loading)
**Writes to:** Humans

## How Important Is This?

**If this breaks:** None directly will be affected.
**Data at risk:** Architecture knowledge.
**Accuracy:** Important — mistakes here cause downstream issues.

## Documents

| File | What it covers |
|------|---------------|
| `bronze-silver-gold-pipeline.md` | **The full architecture**: Bronze (raw ingestion) → gate 1 → gbrain (Silver processing) → gate 2 → Gold (query answers). How OCR uses garrytan/gbrain as the Silver/Gold layer. |

## Related Directories

- `docs/adrs/`
- `docs/build/`
- `agents.md/`
- `raw/repos/gbrain/_index.md` — gbrain reference understanding
- `raw/repos/gstack/_index.md` — gstack reference understanding

---
*Architecture — System Architecture Docs — part of the OCR system. See `_index.md` in this directory for orientation.*
