---
title: "Timekeeper — Replay Manager"
description: "Decision replay, counterfactual comparison, timeline navigation for audit and debugging."
status: "active"
district: "replay"
type: "district"
child_districts: []
neighbors: ["gbrain/replay", "surfaces/replay", "cognition"]
traffic:
  reads: ["gbrain/replay (memory snapshots)", "ledger/ (audit records)"]
  writes: ["surfaces/replay (replay results)"]
blast_radius:
  services: ["Replay queries, audit reviews, debugging"]
  data: ["Replay state, checkpoint data"]
  depends_on_accuracy: "high (wrong replay = wrong audit conclusions)"
connections:
  - direction: "upstream"
    to: "gbrain/replay"
    via: "Memory snapshot API"
    purpose: "Loads saved memory states for replay"
  - direction: "downstream"
    to: "surfaces/replay"
    via: "Replay output stream"
    purpose: "Replay results displayed in the timeline browser"
naming:
  pattern: "snake_case"
partitioning:
  rule: "Monolithic (single module for now)"
maintainers: ["shadabkhan"]
---

# ⏮️ Timekeeper — Replay Manager

The replay system. Handles replaying past shipments, memory states, and decisions. Essential for debugging, auditing, and testing how changes affect past decisions.

## How Data Flows Through Here

- ⬅️ **Receives from** gbrain/replay (via Memory snapshot API) — Loads saved memory states for replay
- ➡️ **Sends to** surfaces/replay (via Replay output stream) — Replay results displayed in the timeline browser

## What It Reads and Writes

**Reads from:** gbrain/replay (memory snapshots), ledger/ (audit records)
**Writes to:** surfaces/replay (replay results)

## How Important Is This?

**If this breaks:** Replay queries, audit reviews, debugging will be affected.
**Data at risk:** Replay state, checkpoint data.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `gbrain/replay/`
- `surfaces/replay/`
- `cognition/`

---
*Timekeeper — Replay Manager — part of the OCR system. See `_index.md` in this directory for orientation.*
