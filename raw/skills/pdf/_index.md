---
title: "pdf — Skill Template"
description: "Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill."
status: "active"
district: "raw/skills/pdf"
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

# 📂 pdf — Skill Template

This directory contains 4 files.

**Documentation:**
- `SKILL.md`
- `forms.md`
- `reference.md`

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

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

- `raw/skills/pdf/scripts/`
- `raw/skills/pdf/LICENSE.txt`
- `raw/skills/pdf/SKILL.md`
- `raw/skills/pdf/forms.md`
- `raw/skills/pdf/reference.md`

## Related Directories

- `cognition/skills/`
- `agents/`

---
*pdf — Skill Template — part of the OCR system. See `_index.md` in this directory for orientation.*
