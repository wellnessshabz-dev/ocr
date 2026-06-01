---
title: "Traces — Distributed Tracing"
description: "OpenTelemetry distributed tracing for cross-service request tracking."
status: "active"
district: "observability/traces"
type: "neighborhood"
parent: "observability"
neighbors: ["observability/logs", "observability/metrics"]
traffic:
  reads: ["All subsystems (trace spans)"]
  writes: ["Trace backend"]
blast_radius:
  services: ["Request debugging, performance analysis"]
  data: ["Trace data"]
  depends_on_accuracy: "medium"
---

# 🔍 Traces — Distributed Tracing

Distributed tracing across OCR subsystems. Follows a single request (like a shipment) through ingestion, compilation, cognition, and memory to find bottlenecks and failures.

## What It Reads and Writes

**Reads from:** All subsystems (trace spans)
**Writes to:** Trace backend

## How Important Is This?

**If this breaks:** Request debugging, performance analysis will be affected.
**Data at risk:** Trace data.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `observability/logs/`
- `observability/metrics/`

---
*Traces — Distributed Tracing — part of the OCR system. See `_index.md` in this directory for orientation.*
