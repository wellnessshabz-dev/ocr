---
title: "Chairman — Synthesis Engine"
description: "Contradiction detection, consensus mapping, and synthesis draft generation from council deliberations."
status: "active"
district: "cognition/chairman"
type: "neighborhood"
parent: "cognition"
neighbors: ["cognition/councils", "cognition/governance"]
traffic:
  reads: ["cognition/councils (skill positions)"]
  writes: ["cognition/governance (synthesis drafts)"]
blast_radius:
  services: ["Decision synthesis quality"]
  data: ["Synthesis state, draft versions"]
  depends_on_accuracy: "critical (synthesis = the output of cognition)"
---

# 👤 Chairman — Synthesis Engine

The synthesis engine. After skills deliberate independently, the chairman collects their positions, detects contradictions, maps areas of agreement, and produces a synthesized decision. Runs iterative rounds when contradictions exceed threshold.

## What It Reads and Writes

**Reads from:** cognition/councils (skill positions)
**Writes to:** cognition/governance (synthesis drafts)

## How Important Is This?

**If this breaks:** Decision synthesis quality will be affected.
**Data at risk:** Synthesis state, draft versions.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `cognition/councils/`
- `cognition/governance/`

---
*Chairman — Synthesis Engine — part of the OCR system. See `_index.md` in this directory for orientation.*
