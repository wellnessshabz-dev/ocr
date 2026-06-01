---
title: "web-artifacts-builder — Skill Template"
description: "Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts."
status: "active"
district: "raw/skills/web-artifacts-builder"
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

# 📂 web-artifacts-builder — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

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

- `raw/skills/web-artifacts-builder/scripts/`
- `raw/skills/web-artifacts-builder/LICENSE.txt`
- `raw/skills/web-artifacts-builder/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*web-artifacts-builder — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
