---
title: "Schemas — Database Schema Definitions"
description: "SQL schema definitions for the audit ledger tables."
status: "active"
district: "ledger/schemas"
type: "neighborhood"
parent: "ledger"
neighbors: ["ledger/migrations", "ledger/seeds"]
traffic:
  reads: ["Source of truth for table structures"]
  writes: ["ledger/migrations (inspiration for migration files)"]
blast_radius:
  services: ["Data model definition"]
  data: ["Table structure definitions"]
  depends_on_accuracy: "critical"
---

# 📋 Schemas — Database Schema Definitions

This directory contains 2 files.

**Code:**
- `001_init.sql`
- `002_web_ingestion.sql`

## What It Reads and Writes

**Reads from:** Source of truth for table structures
**Writes to:** ledger/migrations (inspiration for migration files)

## How Important Is This?

**If this breaks:** Data model definition will be affected.
**Data at risk:** Table structure definitions.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `ledger/schemas/001_init.sql`
- `ledger/schemas/002_web_ingestion.sql`

## Related Directories

- `ledger/migrations/`
- `ledger/seeds/`

---
*Schemas — Database Schema Definitions — part of the OCR system. See `_index.md` in this directory for orientation.*
