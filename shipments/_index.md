---
title: "Cargo Depot — Shipment Pipeline"
description: "The shipment lifecycle: context building, compilation, validation, storage, and replay."
status: "active"
district: "shipments"
type: "district"
child_districts: ["compiler", "replay", "schemas", "storage", "validator"]
neighbors: ["ingestion", "cognition", "gbrain", "ontology"]
traffic:
  reads: ["ingestion/ (raw events)", "ontology/ (concept resolution)"]
  writes: ["cognition/ (compiled shipments)", "gbrain/ (memory consolidation)"]
blast_radius:
  services: ["All shipment processing"]
  data: ["Shipment state, compilation artifacts"]
  depends_on_accuracy: "critical (shipments are the atomic unit of org action)"
connections:
  - direction: "upstream"
    to: "ingestion/"
    via: "Normalized event stream"
    purpose: "Ingestion feeds the compiler"
  - direction: "downstream"
    to: "cognition/councils"
    via: "Compiled shipments"
    purpose: "Shipments trigger council deliberation"
  - direction: "peer"
    to: "ontology/"
    via: "Ontology extractor in compiler"
    purpose: "Shipment entities resolved against ontology"
naming:
  pattern: "snake_case"
  rules:
    - "One module per shipment pipeline stage"
partitioning:
  rule: "By pipeline stage: compiler, replay, schemas, storage, validator"
maintainers: ["shadabkhan"]
---

# 📦 Cargo Depot — Shipment Pipeline

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **⚙️ `compiler/`** — Compiler — Shipment Compiler
- **⏮️ `replay/`** — Replay — Shipment Replay
- **📋 `schemas/`** — Schemas — Shipment Schemas
- **🗄️ `storage/`** — Storage — Shipment Storage
- **✅ `validator/`** — Validator — Shipment Validator

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** ingestion/ (via Normalized event stream) — Ingestion feeds the compiler
- ➡️ **Sends to** cognition/councils (via Compiled shipments) — Shipments trigger council deliberation
- ➡️ **Sends to** ontology/ (via Ontology extractor in compiler) — Shipment entities resolved against ontology

## What It Reads and Writes

**Reads from:** ingestion/ (raw events), ontology/ (concept resolution)
**Writes to:** cognition/ (compiled shipments), gbrain/ (memory consolidation)

## How Important Is This?

**If this breaks:** All shipment processing will be affected.
**Data at risk:** Shipment state, compilation artifacts.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `shipments/compiler/`
- `shipments/replay/`
- `shipments/schemas/`
- `shipments/storage/`
- `shipments/validator/`

## Related Directories

- `ingestion/`
- `cognition/`
- `gbrain/`
- `ontology/`

---
*Cargo Depot — Shipment Pipeline — part of the OCR system. See `_index.md` in this directory for orientation.*
