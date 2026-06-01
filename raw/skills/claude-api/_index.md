---
title: "claude-api — Skill Template"
description: 'Build, debug, and optimize Claude API / Anthropic SDK apps.'
status: "active"
district: "raw/skills/claude-api"
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

# 📂 claude-api — Skill Template

This directory contains 2 files.

**Documentation:**
- `SKILL.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📂 `csharp/`** — csharp
- **📂 `curl/`** — curl
- **📂 `go/`** — go
- **📂 `java/`** — java
- **📂 `php/`** — php
- **📂 `python/`** — python
- **📂 `ruby/`** — ruby
- **📂 `shared/`** — shared
- **📂 `typescript/`** — typescript

Explore each subdirectory to learn more about that part of the system.

## What It Reads and Writes

**Reads from:** cognition/skills (protocol definitions)
**Writes to:** agents/ (persona behavior via skill loading)

## How Important Is This?

**If this breaks:** Agent behavior when this skill is loaded will be affected.
**Data at risk:** Skill-specific templates and instructions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `raw/skills/claude-api/csharp/`
- `raw/skills/claude-api/curl/`
- `raw/skills/claude-api/go/`
- `raw/skills/claude-api/java/`
- `raw/skills/claude-api/php/`
- `raw/skills/claude-api/python/`
- `raw/skills/claude-api/ruby/`
- `raw/skills/claude-api/shared/`
- `raw/skills/claude-api/typescript/`
- `raw/skills/claude-api/LICENSE.txt`
- `raw/skills/claude-api/SKILL.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*claude-api — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
