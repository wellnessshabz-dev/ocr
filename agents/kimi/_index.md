---
title: "Kimi Agent — Kimi Persona"
description: "Kimi-specific agent definitions, configurations, and persona settings."
status: "active"
district: "agents/kimi"
type: "neighborhood"
parent: "agents"
neighbors: ["agents/adapters", "agents/claude", "agents/codex"]
traffic:
  reads: ["raw/skills"]
  writes: ["cognition/skills"]
blast_radius:
  services: ["Kimi agent behavior"]
  data: ["Kimi-specific configs"]
  depends_on_accuracy: "high"
---

# 🟡 Kimi Agent — Kimi Persona

Configuration and persona definition for the Kimi AI agent. Defines how Kimi behaves when operating in the OCR context.

## What It Reads and Writes

**Reads from:** raw/skills
**Writes to:** cognition/skills

## How Important Is This?

**If this breaks:** Kimi agent behavior will be affected.
**Data at risk:** Kimi-specific configs.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `agents/adapters/`
- `agents/claude/`
- `agents/codex/`

---
*Kimi Agent — Kimi Persona — part of the OCR system. See `_index.md` in this directory for orientation.*
