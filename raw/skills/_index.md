---
title: "Raw Skills — Skill Template Library"
description: "The master library of skill definitions. Each skill has a SKILL.md and supporting files."
status: "active"
district: "raw/skills"
type: "neighborhood"
parent: "raw"
neighbors: ["cognition/skills", "agents"]
traffic:
  reads: ["cognition/skills (loading)", "agents (persona definitions)"]
  writes: ["Humans (skill authors)"]
blast_radius:
  services: ["Agent skill loading"]
  data: ["Skill definitions, templates, examples"]
  depends_on_accuracy: "high (wrong skills = wrong agent behavior)"
connections:
  - direction: "downstream"
    to: "agents/"
    via: "SKILL.md loading"
    purpose: "Skills are loaded into agent personas"
  - direction: "downstream"
    to: "cognition/skills"
    via: "Protocol definitions"
    purpose: "Skill templates define council skill protocols"
---

# 🛠️ Raw Skills

The master skill template library. Every directory here contains a skill with its own `SKILL.md`.

## Skills Inventory

> **⚠️ Nick Nisi Thesis — Skills as Gotchas**  
> Per the Nick Nisi analysis (`raw/bronze-docs/architecture_synthesis.md`), comprehensive skill
> definitions can *degrade* agent performance. Skills work best as **gotcha files**:
> 3-5 common failure modes per topic, not exhaustive references. Consider reframing
> these skills from "everything about X" to "watch out for Y when doing X."

| Skill | Purpose |
|-------|---------|
| `algorithmic-art/` | Generative art creation |
| `brand-guidelines/` | Brand identity enforcement |
| `canvas-design/` | Canvas/design skill |
| `claude-api/` | Claude API integration (multi-language) |
| `doc-coauthoring/` | Collaborative document writing |
| `docx/` | DOCX document generation |
| `frontend-design/` | Frontend design skill |
| `internal-comms/` | Internal communications |
| `mcp-builder/` | MCP server building |
| `pdf/` | PDF generation |
| `pptx/` | PowerPoint generation |
| `skill-creator/` | Meta-skill for creating new skills |
| `slack-gif-creator/` | Slack GIF creation |
| `theme-factory/` | Theme generation |
| `web-artifacts-builder/` | Web artifact building |
| `webapp-testing/` | Web app testing |
| `xlsx/` | Excel generation |
