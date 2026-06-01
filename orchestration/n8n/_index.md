---
title: "n8n — n8n Workflow Exports"
description: "n8n workflow JSON exports and configuration for the orchestration layer."
status: "active"
district: "orchestration/n8n"
type: "neighborhood"
parent: "orchestration"
neighbors: ["orchestration/dags", "orchestration/triggers"]
traffic:
  reads: ["orchestration/dags (DAG definitions)"]
  writes: ["n8n runtime"]
blast_radius:
  services: ["n8n workflow deployment"]
  data: ["Workflow export state"]
  depends_on_accuracy: "high"
---

# 📂 n8n — n8n Workflow Exports

n8n configuration: credentials, webhook URLs, API keys, environment settings for the workflow automation layer that connects all OCR components.

## What It Reads and Writes

**Reads from:** orchestration/dags (DAG definitions)
**Writes to:** n8n runtime

## How Important Is This?

**If this breaks:** n8n workflow deployment will be affected.
**Data at risk:** Workflow export state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `orchestration/dags/`
- `orchestration/triggers/`

---
*n8n — n8n Workflow Exports — part of the OCR system. See `_index.md` in this directory for orientation.*
