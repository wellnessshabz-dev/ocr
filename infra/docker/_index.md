---
title: "Docker — Per-Service Dockerfiles"
description: "Individual Dockerfiles for each OCR service component."
status: "active"
district: "infra/docker"
type: "neighborhood"
parent: "infra"
neighbors: ["infra/compose", "infra/nginx"]
traffic:
  reads: ["Source code, system dependencies"]
  writes: ["Docker images"]
blast_radius:
  services: ["Container builds"]
  data: ["Image state"]
  depends_on_accuracy: "high"
---

# 🐳 Docker — Per-Service Dockerfiles

This directory contains 1 file.

## What It Reads and Writes

**Reads from:** Source code, system dependencies
**Writes to:** Docker images

## How Important Is This?

**If this breaks:** Container builds will be affected.
**Data at risk:** Image state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `infra/docker/fastapi.Dockerfile`

## Related Directories

- `infra/compose/`
- `infra/nginx/`

---
*Docker — Per-Service Dockerfiles — part of the OCR system. See `_index.md` in this directory for orientation.*
