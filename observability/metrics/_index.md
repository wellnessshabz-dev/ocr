---
title: "Metrics — System Metrics"
description: "Prometheus/StatsD metric definitions and collection for the OCR runtime."
status: "active"
district: "observability/metrics"
type: "neighborhood"
parent: "observability"
neighbors: ["observability/logs", "observability/traces", "surfaces/executive"]
traffic:
  reads: ["All subsystems (metric values)"]
  writes: ["surfaces/executive (dashboard data)"]
blast_radius:
  services: ["Monitoring, alerting"]
  data: ["Metric aggregates"]
  depends_on_accuracy: "medium"
---

# 📈 Metrics — System Metrics

Performance and health metrics collection. Tracks things like shipment processing time, memory usage, API latency, and error rates. Data flows to monitoring dashboards.

## What It Reads and Writes

**Reads from:** All subsystems (metric values)
**Writes to:** surfaces/executive (dashboard data)

## How Important Is This?

**If this breaks:** Monitoring, alerting will be affected.
**Data at risk:** Metric aggregates.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `observability/logs/`
- `observability/traces/`
- `surfaces/executive/`

---
*Metrics — System Metrics — part of the OCR system. See `_index.md` in this directory for orientation.*
