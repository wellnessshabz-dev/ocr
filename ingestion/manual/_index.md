---
title: "Manual — Manual Signal Injection"
description: "Allows humans to manually inject signals into the OCR pipeline."
status: "active"
district: "ingestion/manual"
type: "neighborhood"
parent: "ingestion"
neighbors: ["ingestion/filesystem", "ingestion/obsidian"]
traffic:
  reads: ["Human input"]
  writes: ["shipments/compiler"]
blast_radius:
  services: ["Manual signal injection"]
  data: ["Ad-hoc signal state"]
  depends_on_accuracy: "low (human-owned)"
---

# ✍️ Manual — Manual Signal Injection

Lets humans inject signals directly. Provides an API endpoint or CLI tool for sending one-off signals to the system — useful for testing, emergency updates, and ad-hoc inputs.

## What It Reads and Writes

**Reads from:** Human input
**Writes to:** shipments/compiler

## How Important Is This?

**If this breaks:** Manual signal injection will be affected.
**Data at risk:** Ad-hoc signal state.
**Accuracy:** Low — not very sensitive.

## Related Directories

- `ingestion/filesystem/`
- `ingestion/obsidian/`

---
*Manual — Manual Signal Injection — part of the OCR system. See `_index.md` in this directory for orientation.*
