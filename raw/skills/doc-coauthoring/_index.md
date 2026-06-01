---
title: "doc-coauthoring — Skill Template"
description: "Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks."
status: "active"
district: "raw/skills/doc-coauthoring"
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

# 📂 doc-coauthoring — Skill Template

This directory contains 1 file.

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

- `raw/skills/doc-coauthoring/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*doc-coauthoring — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
