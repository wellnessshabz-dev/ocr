---
title: "Embassy Row — Agent Definitions"
description: "Definitions, adapters, and configurations for every agent persona in the OCR system."
status: "active"
district: "agents"
type: "district"
child_districts: ["adapters", "claude", "codex", "kimi"]
neighbors: ["cognition", "raw/skills"]
traffic:
  reads: ["cognition/skills", "ontology/"]
  writes: ["shipments/compiler"]
blast_radius:
  services: ["All agent behaviors and personas"]
  data: ["Agent skill definitions, adapter configs"]
  depends_on_accuracy: "high"
connections:
  - direction: "downstream"
    to: "cognition/councils"
    via: "Skill definitions loaded into council orchestrator"
    purpose: "Agent personas participate in structured deliberation"
  - direction: "peer"
    to: "raw/skills"
    via: "SKILL.md references"
    purpose: "Raw skill templates inform agent behavior"
naming:
  pattern: "snake_case"
  rules:
    - "One agent type per subdirectory"
    - "Adapter files named after the tool they wrap"
partitioning:
  rule: "By agent platform: claude/, codex/, kimi/ each define that platform's agent"
  exceptions: ["adapters/ wraps external tool MCPs"]
maintainers: ["shadabkhan"]
---

# 🤖 Embassy Row — Agent Definitions

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **🔌 `adapters/`** — Adapters — External Tool MCP Wrappers
- **🟣 `claude/`** — Claude Agent — Claude Code Persona
- **🟢 `codex/`** — Codex Agent — Codex Persona
- **🟡 `kimi/`** — Kimi Agent — Kimi Persona

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ➡️ **Sends to** cognition/councils (via Skill definitions loaded into council orchestrator) — Agent personas participate in structured deliberation
- ➡️ **Sends to** raw/skills (via SKILL.md references) — Raw skill templates inform agent behavior

## What It Reads and Writes

**Reads from:** cognition/skills, ontology/
**Writes to:** shipments/compiler

## How Important Is This?

**If this breaks:** All agent behaviors and personas will be affected.
**Data at risk:** Agent skill definitions, adapter configs.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `agents/adapters/`
- `agents/claude/`
- `agents/codex/`
- `agents/kimi/`

## Related Directories

- `cognition/`
- `raw/skills/`

---
*Embassy Row — Agent Definitions — part of the OCR system. See `_index.md` in this directory for orientation.*
