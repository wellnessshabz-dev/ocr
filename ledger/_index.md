---
title: "Treasury — Audit Ledger"
description: "Append-only audit log: migrations, schemas, seed data for the OCR audit trail."
status: "active"
district: "ledger"
type: "district"
child_districts: ["migrations", "schemas", "seeds"]
neighbors: ["cognition/governance", "observability", "surfaces"]
traffic:
  reads: ["cognition/governance (commit requests)"]
  writes: ["Postgres DB (audit records)"]
blast_radius:
  services: ["Audit queries, compliance reports"]
  data: ["All decisions, council inputs, governance outcomes"]
  depends_on_accuracy: "critical (audit is immutable by design)"
connections:
  - direction: "upstream"
    to: "cognition/governance"
    via: "Governance commit hook"
    purpose: "Validated council outcomes are appended here"
  - direction: "peer"
    to: "observability/"
    via: "Shared database"
    purpose: "Observability queries ledger for tracing"
naming:
  pattern: "snake_case"
  rules:
    - "Migrations are version-prefixed (001_*, 002_*)"
    - "Schemas named after the domain entity"
partitioning:
  rule: "By function: migrations (schema evolution), schemas (table defs), seeds (test data)"
maintainers: ["shadabkhan"]
---

# 📒 Treasury — Audit Ledger

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **🔄 `migrations/`** — Migrations — Database Migrations
- **📋 `schemas/`** — Schemas — Database Schema Definitions
- **🌱 `seeds/`** — Seeds — Seed Data

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** cognition/governance (via Governance commit hook) — Validated council outcomes are appended here
- ➡️ **Sends to** observability/ (via Shared database) — Observability queries ledger for tracing

## What It Reads and Writes

**Reads from:** cognition/governance (commit requests)
**Writes to:** Postgres DB (audit records)

## How Important Is This?

**If this breaks:** Audit queries, compliance reports will be affected.
**Data at risk:** All decisions, council inputs, governance outcomes.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `ledger/migrations/`
- `ledger/schemas/`
- `ledger/seeds/`

## Related Directories

- `cognition/governance/`
- `observability/`
- `surfaces/`

---
*Treasury — Audit Ledger — part of the OCR system. See `_index.md` in this directory for orientation.*
