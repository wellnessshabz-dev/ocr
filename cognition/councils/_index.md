---
title: "Councils — Deliberation Orchestrator"
description: "Routes shipments to skills, manages parallel deliberation rounds, and collects positions for the chairman."
status: "active"
district: "cognition/councils"
type: "neighborhood"
parent: "cognition"
neighbors: ["cognition/skills", "cognition/chairman", "shipments"]
traffic:
  reads: ["shipments/compiler (incoming)", "cognition/skills (registrations)"]
  writes: ["cognition/chairman (positions)", "ledger/ (audit trail)"]
blast_radius:
  services: ["Council deliberation, skill routing"]
  data: ["Council state, round history"]
  depends_on_accuracy: "critical"
---

# 🏛️ Councils — Deliberation Orchestrator

The deliberation orchestrator. When a shipment arrives, it decides which skills should participate, sends them their context slices, manages the parallel reasoning rounds, and collects position summaries for the chairman.

### Design Principle: Grill Me Pattern

Council deliberation should follow Matt Pocock's "Grill Me" pattern: the first
round is alignment — grilling the shipment's assumptions, testing contradictions,
and reaching shared understanding. The chairman's synthesis is a PRD-equivalent
(alignment summary), not a position paper. This replaces specification-reading
with adversarial alignment.

## What It Reads and Writes

**Reads from:** shipments/compiler (incoming), cognition/skills (registrations)
**Writes to:** cognition/chairman (positions), ledger/ (audit trail)

## How Important Is This?

**If this breaks:** Council deliberation, skill routing will be affected.
**Data at risk:** Council state, round history.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `cognition/skills/`
- `cognition/chairman/`
- `shipments/`

---
*Councils — Deliberation Orchestrator — part of the OCR system. See `_index.md` in this directory for orientation.*
