---
title: "brand-guidelines — Skill Template"
description: "Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply."
status: "active"
district: "raw/skills/brand-guidelines"
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

# 📂 brand-guidelines — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What It Reads and Writes

**Reads from:** cognition/skills (protocol definitions)
**Writes to:** agents/ (persona behavior via skill loading)

## How Important Is This?

**If this breaks:** Agent behavior when this skill is loaded will be affected.
**Data at risk:** Skill-specific templates and instructions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `raw/skills/brand-guidelines/LICENSE.txt`
- `raw/skills/brand-guidelines/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*brand-guidelines — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
