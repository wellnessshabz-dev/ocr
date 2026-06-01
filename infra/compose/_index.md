---
title: "Compose — Docker Compose Configs"
description: "Docker Compose orchestration files for the full OCR stack."
status: "active"
district: "infra/compose"
type: "neighborhood"
parent: "infra"
neighbors: ["infra/docker", "infra/nginx"]
traffic:
  reads: ["infra/docker (Dockerfiles)"]
  writes: ["Deployed services"]
blast_radius:
  services: ["All OCR services depends on compose being correct"]
  data: ["Service orchestration state"]
  depends_on_accuracy: "critical"
---

# 📋 Compose — Docker Compose Configs

Docker Compose configuration files for running the full OCR stack locally. Defines services, networks, volumes, and environment variables. Run `docker compose up` to spin up the entire system for development.

## What It Reads and Writes

**Reads from:** infra/docker (Dockerfiles)
**Writes to:** Deployed services

## How Important Is This?

**If this breaks:** All OCR services depends on compose being correct will be affected.
**Data at risk:** Service orchestration state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `infra/docker/`
- `infra/nginx/`

---
*Compose — Docker Compose Configs — part of the OCR system. See `_index.md` in this directory for orientation.*
