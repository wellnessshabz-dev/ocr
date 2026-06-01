---
title: "mcp-builder — Skill Template"
description: "Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK)."
status: "active"
district: "raw/skills/mcp-builder"
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

# 📂 mcp-builder — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `reference/`** — reference
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

- `raw/skills/mcp-builder/reference/`
- `raw/skills/mcp-builder/scripts/`
- `raw/skills/mcp-builder/LICENSE.txt`
- `raw/skills/mcp-builder/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*mcp-builder — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
