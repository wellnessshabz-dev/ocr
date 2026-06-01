---
title: "webapp-testing — Skill Template"
description: "Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs."
status: "active"
district: "raw/skills/webapp-testing"
type: "neighborhood"
parent: "raw/skills"
neighbors: ["cognition/skills", "agents"]
traffic:
  reads: ["cognition/skills (protocol definitions)"]
  writes: ["agents/ (persona behavior via skill loading)"]
blast_radius:
  services: ["Agent behavior when this skill is loaded"]
  data: ["Skill-specific templates and instructions"]
  depends_on_accuracy: "high"
---

# 📂 webapp-testing — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `examples/`** — examples
- **🛠️ `scripts/`** — scripts

Explore each subdirectory to learn more about that part of the system.

## What It Reads and Writes

**Reads from:** cognition/skills (protocol definitions)
**Writes to:** agents/ (persona behavior via skill loading)

## How Important Is This?

**If this breaks:** Agent behavior when this skill is loaded will be affected.
**Data at risk:** Skill-specific templates and instructions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `raw/skills/webapp-testing/examples/`
- `raw/skills/webapp-testing/scripts/`
- `raw/skills/webapp-testing/LICENSE.txt`
- `raw/skills/webapp-testing/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*webapp-testing — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
