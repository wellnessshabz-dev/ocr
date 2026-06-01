---
title: "Claude Agent — Claude Code Persona"
description: "Claude Code-specific agent definitions, configurations, and persona settings."
status: "active"
district: "agents/claude"
type: "neighborhood"
parent: "agents"
neighbors: ["agents/adapters", "agents/codex", "agents/kimi"]
traffic:
  reads: ["raw/skills", "agents/adapters"]
  writes: ["cognition/skills (skill registrations)"]
blast_radius:
  services: ["Claude Code agent behavior"]
  data: ["Claude-specific configs"]
  depends_on_accuracy: "high"
---

# 🟣 Claude Agent — Claude Code Persona

This directory contains 1 file.

**Code:**
- `adapter.py`

## What It Reads and Writes

**Reads from:** raw/skills, agents/adapters
**Writes to:** cognition/skills (skill registrations)

## How Important Is This?

**If this breaks:** Claude Code agent behavior will be affected.
**Data at risk:** Claude-specific configs.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `agents/claude/adapter.py`

## Related Directories

- `agents/adapters/`
- `agents/codex/`
- `agents/kimi/`

---
*Claude Agent — Claude Code Persona — part of the OCR system. See `_index.md` in this directory for orientation.*
