---
title: "Migrations — Database Migrations"
description: "Alembic/DB migration files for the audit ledger schema."
status: "active"
district: "ledger/migrations"
type: "neighborhood"
parent: "ledger"
neighbors: ["ledger/schemas", "ledger/seeds"]
traffic:
  reads: ["ledger/schemas (target schema)"]
  writes: ["Postgres DB"]
blast_radius:
  services: ["Database schema evolution"]
  data: ["Schema migration state"]
  depends_on_accuracy: "critical (bad migration = data loss)"
---

# 🔄 Migrations — Database Migrations

Database migration files for the audit ledger (PostgreSQL). Each migration changes the schema in a controlled, reversible way. Follows standard migration conventions (timestamp_named files).

## What It Reads and Writes

**Reads from:** ledger/schemas (target schema)
**Writes to:** Postgres DB

## How Important Is This?

**If this breaks:** Database schema evolution will be affected.
**Data at risk:** Schema migration state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ledger/schemas/`
- `ledger/seeds/`

---
*Migrations — Database Migrations — part of the OCR system. See `_index.md` in this directory for orientation.*
