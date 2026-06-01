---
title: "API — Core API Logic"
description: "Core FastAPI server logic: middleware, dependencies, models, and application setup."
status: "active"
district: "src/api"
type: "neighborhood"
parent: "src"
neighbors: ["src/routers", "surfaces"]
traffic:
  reads: ["All subsystems (via service layer)"]
  writes: ["HTTP responses (via routers)"]
blast_radius:
  services: ["OCR API server core"]
  data: ["API state, middleware state"]
  depends_on_accuracy: "critical"
---

# 🔌 API — Core API Logic

FastAPI application entry point. Defines the REST API routes, middleware, authentication, and server configuration. This is the HTTP interface to the OCR system.

## What It Reads and Writes

**Reads from:** All subsystems (via service layer)
**Writes to:** HTTP responses (via routers)

## How Important Is This?

**If this breaks:** OCR API server core will be affected.
**Data at risk:** API state, middleware state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `src/routers/`
- `surfaces/`

---
*API — Core API Logic — part of the OCR system. See `_index.md` in this directory for orientation.*
