---
title: "Activation — Memory Activation Protocol"
description: "The protocol that activates memory when a shipment arrives: ontology anchor, trajectory walk, contradiction surfacing."
status: "active"
district: "gbrain/activation"
type: "neighborhood"
parent: "gbrain"
neighbors: ["gbrain/episodic", "gbrain/temporal", "ontology"]
traffic:
  reads: ["ontology/ (concept resolution)", "gbrain/temporal (trajectories)"]
  writes: ["gbrain/episodic (activation results)"]
blast_radius:
  services: ["Memory activation quality"]
  data: ["Activation state"]
  depends_on_accuracy: "critical"
---

# ⚡ Activation — Memory Activation Protocol

The "wake-up" layer of GBrain memory. When a shipment arrives, this component activates relevant memories — finding connected concepts, pulling up related decisions, and checking what the system already knows. It decides what information is relevant context.

## What It Reads and Writes

**Reads from:** ontology/ (concept resolution), gbrain/temporal (trajectories)
**Writes to:** gbrain/episodic (activation results)

## How Important Is This?

**If this breaks:** Memory activation quality will be affected.
**Data at risk:** Activation state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `gbrain/episodic/`
- `gbrain/temporal/`
- `ontology/`

---
*Activation — Memory Activation Protocol — part of the OCR system. See `_index.md` in this directory for orientation.*
