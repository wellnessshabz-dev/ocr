---
title: "Adapters — External Tool MCP Wrappers"
description: "MCP adapters that wrap external tools (GitHub, Obsidian, etc.) for the agent ecosystem."
status: "active"
district: "agents/adapters"
type: "neighborhood"
parent: "agents"
neighbors: ["agents/claude", "agents/codex", "agents/kimi"]
traffic:
  reads: ["External tool APIs"]
  writes: ["Agent context (tool results)"]
blast_radius:
  services: ["Agent-tool integration"]
  data: ["Tool authentication configs"]
  depends_on_accuracy: "high (wrong data breaks agent reasoning)"
---

# 🔌 Adapters — External Tool MCP Wrappers

This directory contains 1 file.

**Code:**
- `base.py`

## What It Reads and Writes

**Reads from:** External tool APIs
**Writes to:** Agent context (tool results)

## How Important Is This?

**If this breaks:** Agent-tool integration will be affected.
**Data at risk:** Tool authentication configs.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `agents/adapters/base.py`

## Related Directories

- `agents/claude/`
- `agents/codex/`
- `agents/kimi/`

---
*Adapters — External Tool MCP Wrappers — part of the OCR system. See `_index.md` in this directory for orientation.*
