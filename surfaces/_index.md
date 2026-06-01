---
title: "Town Square — Executive Surfaces"
description: "Human-facing outputs: executive dashboard, ontology viewer, replay browser, shipment tracker."
status: "active"
district: "surfaces"
type: "district"
child_districts: ["executive", "ontology", "replay", "shipments"]
neighbors: ["src", "gbrain", "cognition", "observability"]
traffic:
  reads: ["gbrain/ (memory state)", "cognition/ (decision state)", "ledger/ (audit data)"]
  writes: ["WebSocket streams", "HTTP responses (via src/)"]
blast_radius:
  services: ["All user-facing surfaces"]
  data: ["Presentation state, WebSocket connections"]
  depends_on_accuracy: "medium (display issues don't corrupt core state)"
connections:
  - direction: "upstream"
    to: "gbrain/ + cognition/ + ledger/"
    via: "Service calls"
    purpose: "Surfaces query subsystems for display data"
  - direction: "downstream"
    to: "src/"
    via: "Route definitions"
    purpose: "Surfaces define what the API serves"
naming:
  pattern: "snake_case"
  rules:
    - "One module per surface type"
partitioning:
  rule: "By surface type: executive, ontology, replay, shipments"
maintainers: ["shadabkhan"]
---

# 🖥️ Town Square — Executive Surfaces

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📊 `executive/`** — Executive — Executive Dashboard
- **🗺️ `ontology/`** — Ontology — Ontology Surface
- **⏮️ `replay/`** — Replay — Replay Surface
- **📦 `shipments/`** — Shipments — Shipment Surface

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** gbrain/ + cognition/ + ledger/ (via Service calls) — Surfaces query subsystems for display data
- ➡️ **Sends to** src/ (via Route definitions) — Surfaces define what the API serves

## What It Reads and Writes

**Reads from:** gbrain/ (memory state), cognition/ (decision state), ledger/ (audit data)
**Writes to:** WebSocket streams, HTTP responses (via src/)

## How Important Is This?

**If this breaks:** All user-facing surfaces will be affected.
**Data at risk:** Presentation state, WebSocket connections.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Quick Reference

- `surfaces/executive/`
- `surfaces/ontology/`
- `surfaces/replay/`
- `surfaces/shipments/`

## Related Directories

- `src/`
- `gbrain/`
- `cognition/`
- `observability/`

---
*Town Square — Executive Surfaces — part of the OCR system. See `_index.md` in this directory for orientation.*
