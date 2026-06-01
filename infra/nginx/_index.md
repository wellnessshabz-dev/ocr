---
title: "Nginx — Reverse Proxy Configs"
description: "nginx configuration files for reverse proxying OCR services."
status: "active"
district: "infra/nginx"
type: "neighborhood"
parent: "infra"
neighbors: ["infra/compose", "src"]
traffic:
  reads: ["Service endpoints"]
  writes: ["HTTP routing table"]
blast_radius:
  services: ["HTTP routing, TLS termination"]
  data: ["Request routing state"]
  depends_on_accuracy: "critical (misrouting = service unavailable)"
---

# 🌐 Nginx — Reverse Proxy Configs

This directory contains 1 file.

## What It Reads and Writes

**Reads from:** Service endpoints
**Writes to:** HTTP routing table

## How Important Is This?

**If this breaks:** HTTP routing, TLS termination will be affected.
**Data at risk:** Request routing state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `infra/nginx/nginx.conf`

## Related Directories

- `infra/compose/`
- `src/`

---
*Nginx — Reverse Proxy Configs — part of the OCR system. See `_index.md` in this directory for orientation.*
