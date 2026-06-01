---
title: "Inspection Yard — Tests"
description: "Unit and integration tests for all OCR subsystems. Mirrors the source directory structure."
status: "active"
district: "tests"
type: "district"
child_districts: ["integration", "unit"]
neighbors: ["All source districts"]
traffic:
  reads: ["All source code"]
  writes: ["Test artifacts, coverage reports"]
blast_radius:
  services: ["CI/CD pipelines, quality gates"]
  data: ["Test state only"]
  depends_on_accuracy: "high (false positives break trust in CI)"
connections:
  - direction: "peer"
    to: "Every source district"
    via: "Import mirroring"
    purpose: "Tests mirror the structure of the code they validate"
naming:
  pattern: "snake_case, mirror source file name + _test suffix"
  rules:
    - "test_<module>.py for unit tests"
    - "test_<feature>.py for integration tests"
partitioning:
  rule: "By scope: unit/ (isolated), integration/ (end-to-end)"
maintainers: ["shadabkhan"]
---

# 🧪 Inspection Yard — Tests

This directory contains 1 file.

**Code:**
- `conftest.py`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **🔗 `integration/`** — Integration Tests — End-to-End Tests
- **🔬 `unit/`** — Unit Tests — Module-Level Tests

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ➡️ **Sends to** Every source district (via Import mirroring) — Tests mirror the structure of the code they validate

## What It Reads and Writes

**Reads from:** All source code
**Writes to:** Test artifacts, coverage reports

## How Important Is This?

**If this breaks:** CI/CD pipelines, quality gates will be affected.
**Data at risk:** Test state only.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `tests/integration/`
- `tests/unit/`
- `tests/conftest.py`

## Related Directories

- `All source districts/`

---
*Inspection Yard — Tests — part of the OCR system. See `_index.md` in this directory for orientation.*
