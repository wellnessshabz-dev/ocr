---
title: "Codex Agent — Codex Persona"
description: "Codex-specific agent definitions, configurations, and persona settings."
status: "active"
district: "agents/codex"
type: "neighborhood"
parent: "agents"
neighbors: ["agents/adapters", "agents/claude", "agents/kimi"]
traffic:
  reads: ["raw/skills"]
  writes: ["cognition/skills"]
blast_radius:
  services: ["Codex agent behavior"]
  data: ["Codex-specific configs"]
  depends_on_accuracy: "high"
---

# 🟢 Codex Agent — Codex Persona

Configuration and persona definition for the Codex AI agent. Defines how Codex behaves when operating in the OCR context.

## What It Reads and Writes

**Reads from:** raw/skills
**Writes to:** cognition/skills

## How Important Is This?

**If this breaks:** Codex agent behavior will be affected.
**Data at risk:** Codex-specific configs.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `agents/adapters/`
- `agents/claude/`
- `agents/kimi/`

---
*Codex Agent — Codex Persona — part of the OCR system. See `_index.md` in this directory for orientation.*
