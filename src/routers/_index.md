---
title: "Routers — API Route Handlers"
description: "FastAPI route handlers organized by resource: executive, ontology, replay, shipments."
status: "active"
district: "src/routers"
type: "neighborhood"
parent: "src"
neighbors: ["src/api", "surfaces"]
traffic:
  reads: ["src/api (shared deps)", "surfaces/ (display logic)"]
  writes: ["HTTP responses"]
blast_radius:
  services: ["API endpoint availability"]
  data: ["Request/response state"]
  depends_on_accuracy: "high"
---

# 🚦 Routers — API Route Handlers

This directory contains 2 files.

**Code:**
- `__init__.py`
- `ingestion.py`

## What It Reads and Writes

**Reads from:** src/api (shared deps), surfaces/ (display logic)
**Writes to:** HTTP responses

## How Important Is This?

**If this breaks:** API endpoint availability will be affected.
**Data at risk:** Request/response state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `src/routers/__init__.py`
- `src/routers/ingestion.py`

## Related Directories

- `src/api/`
- `surfaces/`

---
*Routers — API Route Handlers — part of the OCR system. See `_index.md` in this directory for orientation.*
