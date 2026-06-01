---
title: "Skills — Skill Protocol Registry"
description: "Protocol definitions for cognitive skills: Strategic Analyst, Technical Architect, Risk Assessor, etc."
status: "active"
district: "cognition/skills"
type: "neighborhood"
parent: "cognition"
neighbors: ["cognition/councils", "agents", "raw/skills"]
traffic:
  reads: ["agents/ (persona defs)", "raw/skills (templates)"]
  writes: ["cognition/councils (skill registrations)"]
blast_radius:
  services: ["All skill behavior and reasoning"]
  data: ["Skill definitions, protocol schemas"]
  depends_on_accuracy: "critical (skills = the reasoning engine)"
---

# 🔧 Skills — Skill Protocol Registry

Defines the available skill personas — Strategic Analyst, Technical Architect, Risk Assessor, Customer Advocate, Devil Advocate, and others. Each skill has a jurisdiction (what topics it covers), reasoning protocol, and output format.

## What It Reads and Writes

**Reads from:** agents/ (persona defs), raw/skills (templates)
**Writes to:** cognition/councils (skill registrations)

## How Important Is This?

**If this breaks:** All skill behavior and reasoning will be affected.
**Data at risk:** Skill definitions, protocol schemas.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `cognition/councils/`
- `agents/`
- `raw/skills/`

---
*Skills — Skill Protocol Registry — part of the OCR system. See `_index.md` in this directory for orientation.*
