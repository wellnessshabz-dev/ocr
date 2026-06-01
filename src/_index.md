---
title: "City Center — Source Code"
description: "The FastAPI application: API routes, middleware, dependency injection, server entry point."
status: "active"
district: "src"
type: "district"
child_districts: ["api", "routers"]
neighbors: ["surfaces", "cognition", "orchestration", "ledger"]
traffic:
  reads: ["cognition/ (query results)", "ontology/ (concept data)"]
  writes: ["surfaces/ (API responses)", "ledger/ (via middleware)"]
blast_radius:
  services: ["OCR API server"]
  data: ["Request/response state, live connections"]
  depends_on_accuracy: "high (API is the entry point for all queries)"
connections:
  - direction: "upstream"
    to: "External HTTP clients"
    via: "FastAPI routes"
    purpose: "All external queries enter here"
  - direction: "downstream"
    to: "cognition/ + ontology/ + gbrain/"
    via: "Service layer"
    purpose: "API queries dispatch to the appropriate subsystem"
naming:
  pattern: "snake_case"
  rules:
    - "API routes map 1:1 to domain resources"
    - "Routers named after resource (executive.py, ontology.py, etc.)"
partitioning:
  rule: "By API concern: api/ (core logic), routers/ (route handlers)"
maintainers: ["shadabkhan"]
---

# 💻 City Center — Source Code

This directory contains 1 file.

**Code:**
- `main.py`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **🔌 `api/`** — API — Core API Logic
- **🚦 `routers/`** — Routers — API Route Handlers

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** External HTTP clients (via FastAPI routes) — All external queries enter here
- ➡️ **Sends to** cognition/ + ontology/ + gbrain/ (via Service layer) — API queries dispatch to the appropriate subsystem

## What It Reads and Writes

**Reads from:** cognition/ (query results), ontology/ (concept data)
**Writes to:** surfaces/ (API responses), ledger/ (via middleware)

## How Important Is This?

**If this breaks:** OCR API server will be affected.
**Data at risk:** Request/response state, live connections.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `src/api/`
- `src/routers/`
- `src/main.py`

## Related Directories

- `surfaces/`
- `cognition/`
- `orchestration/`
- `ledger/`

---
*City Center — Source Code — part of the OCR system. See `_index.md` in this directory for orientation.*
