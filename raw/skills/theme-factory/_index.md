---
title: "theme-factory — Skill Template"
description: "Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly."
status: "active"
district: "raw/skills/theme-factory"
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

# 📂 theme-factory — Skill Template

This directory contains 3 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `themes/`** — themes

Explore each subdirectory to learn more about that part of the system.

## What It Reads and Writes

**Reads from:** cognition/skills (protocol definitions)
**Writes to:** agents/ (persona behavior via skill loading)

## How Important Is This?

**If this breaks:** Agent behavior when this skill is loaded will be affected.
**Data at risk:** Skill-specific templates and instructions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `raw/skills/theme-factory/themes/`
- `raw/skills/theme-factory/LICENSE.txt`
- `raw/skills/theme-factory/SKILL.md`
- `raw/skills/theme-factory/theme-showcase.pdf`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*theme-factory — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
