---
title: OpenCode Documentation Maintenance Guide
description: Rules and conventions for maintaining the opencode documentation files in this directory.
status: active
maintainer: shadabkhan
update_frequency: monthly
source_url: https://opencode.ai/docs/
update_command: "opencode --scrape https://opencode.ai/docs/"
city_district: "raw/bronze-docs/documentation/opencode"
city_parent: "raw"
city_neighbors: ["raw/images", "raw/skills"]
blast_radius: "Stale opencode docs cause confusion. Outdated skill references cause agent misbehavior."
connections:
  - direction: "upstream"
    to: "agents/"
    via: "SKILL.md loading from raw/skills"
    purpose: "Skills define agent behavior; raw/skills is the source"
  - direction: "peer"
    to: "docs/"
    via: "Reference links"
    purpose: "Raw opencode docs are referenced by project documentation"
---

# OpenCode Documentation Maintenance

## City Context

This directory is part of the **Archive** district (`raw/`). It stores reference documentation — not runtime code. Changes here do not affect running services but may confuse agents that load this content for context.

## Directory Convention

All opencode documentation files live flat in `raw/bronze-docs/documentation/opencode/`. Every directory in this path has an `_index.md` describing its contents (see city architecture in root `_index.md`).

## Naming

- Docs pages: `docs_<topic>.md` (e.g., `docs_cli.md`, `docs_providers.md`)
- GitHub metadata: `github_<file>.md` (e.g., `github_readme.md`)
- Domain pages: `opencode.<suffix>.md` (e.g., `opencode.ai.md`)
- Meta files: `_<purpose>.md` (e.g., `_maintenance.md`)

## File Format

```markdown
# docs_<topic>

Source: <url>

# <Title>

<content>
```

- No YAML frontmatter in content files (only meta files have it)
- Line 1: `# docs_<topic>` matching the filename
- Line 3: `Source: <canonical-url>` — the exact URL this was scraped from
- Remaining content: clean markdown, no HTML, no navigation chrome

## When to Update

1. When the opencode CLI/API changes
2. Monthly as part of routine maintenance
3. When tracking an opencode issue that references docs

## Update Process

1. Fetch the page from `https://opencode.ai/docs/<topic>/`
2. Save as `raw/bronze-docs/documentation/opencode/docs_<topic>.md`
3. Preserve format: title → source → content
4. Strip navigation, headers, footers, and chrome
5. Keep only the core documentation content
