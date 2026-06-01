---
title: "Executive — Executive Dashboard"
description: "Executive dashboard, strategic question engine, cognition log, and live WebSocket updates."
status: "active"
district: "surfaces/executive"
type: "neighborhood"
parent: "surfaces"
neighbors: ["surfaces/ontology", "surfaces/replay", "surfaces/shipments", "observability"]
traffic:
  reads: ["cognition/ (decision state)", "gbrain/ (memory state)", "observability/ (health)"]
  writes: ["WebSocket streams", "HTTP responses"]
blast_radius:
  services: ["Executive user experience"]
  data: ["Dashboard presentation state"]
  depends_on_accuracy: "medium"
---

# 📊 Executive — Executive Dashboard

This directory contains 1 file.

## What It Reads and Writes

**Reads from:** cognition/ (decision state), gbrain/ (memory state), observability/ (health)
**Writes to:** WebSocket streams, HTTP responses

## How Important Is This?

**If this breaks:** Executive user experience will be affected.
**Data at risk:** Dashboard presentation state.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Quick Reference

- `surfaces/executive/index.html`

## Related Directories

- `surfaces/ontology/`
- `surfaces/replay/`
- `surfaces/shipments/`
- `observability/`

---
*Executive — Executive Dashboard — part of the OCR system. See `_index.md` in this directory for orientation.*
