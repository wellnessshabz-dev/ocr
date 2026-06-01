---
title: "Filesystem — File System Ingestion"
description: "Watches and ingests filesystem events into the OCR pipeline."
status: "active"
district: "ingestion/filesystem"
type: "neighborhood"
parent: "ingestion"
neighbors: ["ingestion/github", "ingestion/obsidian", "ingestion/web"]
traffic:
  reads: ["Local filesystem"]
  writes: ["shipments/compiler"]
blast_radius:
  services: ["File-based signal ingestion"]
  data: ["File events"]
  depends_on_accuracy: "medium"
---

# 📁 Filesystem — File System Ingestion

Watches the local filesystem for changes and turns file events (create, modify, delete) into OCR signals. Useful for integrating with local tools and watching directories for new content.

## What It Reads and Writes

**Reads from:** Local filesystem
**Writes to:** shipments/compiler

## How Important Is This?

**If this breaks:** File-based signal ingestion will be affected.
**Data at risk:** File events.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `ingestion/github/`
- `ingestion/obsidian/`
- `ingestion/web/`

---
*Filesystem — File System Ingestion — part of the OCR system. See `_index.md` in this directory for orientation.*
