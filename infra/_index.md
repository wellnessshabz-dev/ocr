---
title: "Utilities — Infrastructure & Deployment"
description: "Docker compose, Dockerfiles, nginx configs — everything needed to deploy and run the OCR stack."
status: "active"
district: "infra"
type: "district"
child_districts: ["compose", "docker", "nginx"]
neighbors: ["orchestration", "src", "ledger"]
traffic:
  reads: ["Docker images from registry"]
  writes: ["Deployed services state"]
blast_radius:
  services: ["All OCR services (API, n8n, DBs, auth)"]
  data: ["Deployment state, environment configs"]
  depends_on_accuracy: "critical (misconfig = service outage)"
connections:
  - direction: "downstream"
    to: "orchestration/n8n"
    via: "Docker networking"
    purpose: "n8n runs inside the infra-defined network"
  - direction: "peer"
    to: "ledger/"
    via: "Postgres connection string"
    purpose: "Infra defines the database that ledger/ migrates"
naming:
  pattern: "kebab-case for docker files, snake_case for compose"
  rules:
    - "Dockerfiles named Dockerfile.service"
partitioning:
  rule: "By concern: compose (orchestration configs), docker (per-service images), nginx (reverse proxy)"
maintainers: ["shadabkhan"]
---

# ⚙️ Utilities — Infrastructure & Deployment

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📋 `compose/`** — Compose — Docker Compose Configs
- **🐳 `docker/`** — Docker — Per-Service Dockerfiles
- **🌐 `nginx/`** — Nginx — Reverse Proxy Configs

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ➡️ **Sends to** orchestration/n8n (via Docker networking) — n8n runs inside the infra-defined network
- ➡️ **Sends to** ledger/ (via Postgres connection string) — Infra defines the database that ledger/ migrates

## What It Reads and Writes

**Reads from:** Docker images from registry
**Writes to:** Deployed services state

## How Important Is This?

**If this breaks:** All OCR services (API, n8n, DBs, auth) will be affected.
**Data at risk:** Deployment state, environment configs.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `infra/compose/`
- `infra/docker/`
- `infra/nginx/`

## Related Directories

- `orchestration/`
- `src/`
- `ledger/`

---
*Utilities — Infrastructure & Deployment — part of the OCR system. See `_index.md` in this directory for orientation.*
