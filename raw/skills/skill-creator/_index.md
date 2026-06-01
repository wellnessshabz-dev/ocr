---
title: "skill-creator — Skill Template"
description: "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy."
status: "active"
district: "raw/skills/skill-creator"
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

# 📂 skill-creator — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **🤖 `agents/`** — agents
- **📂 `assets/`** — assets
- **📂 `eval-viewer/`** — eval-viewer
- **📂 `references/`** — references
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

- `raw/skills/skill-creator/agents/`
- `raw/skills/skill-creator/assets/`
- `raw/skills/skill-creator/eval-viewer/`
- `raw/skills/skill-creator/references/`
- `raw/skills/skill-creator/scripts/`
- `raw/skills/skill-creator/LICENSE.txt`
- `raw/skills/skill-creator/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*skill-creator — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
