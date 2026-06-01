---
title: "slack-gif-creator — Skill Template"
description: 'Knowledge and utilities for creating animated GIFs optimized for Slack.'
status: "active"
district: "raw/skills/slack-gif-creator"
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

# 📂 slack-gif-creator — Skill Template

This directory contains 3 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `core/`** — core

Explore each subdirectory to learn more about that part of the system.

## What It Reads and Writes

**Reads from:** cognition/skills (protocol definitions)
**Writes to:** agents/ (persona behavior via skill loading)

## How Important Is This?

**If this breaks:** Agent behavior when this skill is loaded will be affected.
**Data at risk:** Skill-specific templates and instructions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `raw/skills/slack-gif-creator/core/`
- `raw/skills/slack-gif-creator/LICENSE.txt`
- `raw/skills/slack-gif-creator/SKILL.md`
- `raw/skills/slack-gif-creator/requirements.txt`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*slack-gif-creator — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
