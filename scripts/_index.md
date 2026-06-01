---
title: "Maintenance Shed — Scripts"
description: "Utility scripts for development, deployment, maintenance, and data operations."
status: "active"
district: "scripts"
type: "district"
child_districts: []
neighbors: ["infra", "src"]
traffic:
  reads: ["Environment state"]
  writes: ["File system, databases"]
blast_radius:
  services: ["Development environments, CI/CD"]
  data: ["Transient (script outputs)"]
  depends_on_accuracy: "low (scripts are tools, not core logic)"
connections:
  - direction: "peer"
    to: "infra/"
    via: "Deployment scripts call infra configs"
    purpose: "Scripts automate what infra defines"
naming:
  pattern: "snake_case"
  rules:
    - "Scripts named after their function (seed_data.py, migrate.sh, etc.)"
partitioning:
  rule: "Flat directory, one script per concern"
maintainers: ["shadabkhan"]
---

# 🛠️ Maintenance Shed — Scripts

This directory contains 1 file.

**Code:**
- `generate_dashboard.py`

## How Data Flows Through Here

- ➡️ **Sends to** infra/ (via Deployment scripts call infra configs) — Scripts automate what infra defines

## What It Reads and Writes

**Reads from:** Environment state
**Writes to:** File system, databases

## How Important Is This?

**If this breaks:** Development environments, CI/CD will be affected.
**Data at risk:** Transient (script outputs).
**Accuracy:** Low — not very sensitive.

## Quick Reference

- `scripts/generate_dashboard.py`

## Related Directories

- `infra/`
- `src/`

---
*Maintenance Shed — Scripts — part of the OCR system. See `_index.md` in this directory for orientation.*
