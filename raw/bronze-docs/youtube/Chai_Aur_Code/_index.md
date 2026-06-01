---
title: "Chai Aur Code — YouTube Videos"
description: "Videos from the Chai Aur Code (Hitesh Choudhary) YouTube channel — Hindi tech content about AI, coding, and protocols."
status: "active"
district: "raw/bronze-docs/youtube/Chai_Aur_Code"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs/youtube/AI_Engineer", "raw/bronze-docs/youtube/Sequoia_Capital", "raw/bronze-docs/youtube/Matt_Pocock", "raw/bronze-docs/youtube/mastra"]
traffic:
  reads: ["Architecture synthesis", "Protocol designers"]
  writes: ["Manual ingestion"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# Chai Aur Code — YouTube Videos

Collection of reasoned analyses from the Chai Aur Code channel about AI
protocols, MCP, and developer tools.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `mcp_2.0_all_updates_explained.md` | Hitesh Choudhary | MCP v2026 updates — stateless protocol, server-to-client elicitation, OAuth, extensions/apps, caching, tracing, deprecation policy | reasoned |

## Topic Tags

- `mcp` — Model Context Protocol for AI agent connectivity
- `stateless` — Stateful → stateless protocol evolution
- `oauth` — OAuth 2.0 / OpenID Connect integration
- `extensions` — Formal extension system for MCP
- `apps` — Interactive HTML interfaces within agents
- `caching` — TTL and scope-based result caching
- `tracing` — Distributed W3C trace context
- `task-extensions` — Long-running task pattern with polling
- `protocol-evolution` — Protocol maturing to platform infrastructure

## Naming Convention

`<topic>_<description>.md` — snake_case, descriptive of content.

## Related Directories

- `raw/bronze-docs/youtube/AI_Engineer/`
- `raw/bronze-docs/youtube/Sequoia_Capital/`
- `raw/bronze-docs/youtube/Matt_Pocock/`
- `raw/bronze-docs/youtube/mastra/`
- `docs/adrs/`
