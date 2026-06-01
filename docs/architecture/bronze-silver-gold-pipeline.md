# Bronze → Silver → Gold Pipeline

## What This Architecture Is

This is a data pipeline borrowed from data engineering (Databricks' Medallion
Architecture) and adapted for organizational cognition. Data flows through
three layers, getting cleaner and more valuable at each step.

```
Bronze (raw data)
    │  Consume EVERYTHING — commits, web pages, repos, docs, transcripts
    ▼
gate 1 → gbrain ingest (normalize, dedup, entity extraction)
    │
Silver (processed knowledge)
    │  Knowledge graph, entity enrichment, auto-linking, dream cycle
    ▼
gate 2 → gbrain query (synthesis with citations, gap analysis)
    │
Gold (answers with citations)
    │  Ask questions, get answers. The brain did the reading.
```

---

## The Three Layers

### Bronze — Raw Ingestion Layer

**Goal:** Consume everything possible. The more data we put in, the smarter
the brain gets.

**What lives here:**

| Source | Tool | What it produces |
|--------|------|-----------------|
| GitHub commits | `ingestion/github/` (GitHubAdapter) | Commit data: message, author, files, diff |
| Web pages | `ingestion/web/` (ScraperRouter + ScraplingAdapter) | Clean markdown from any URL |
| Reference repos | `raw/repos/gstack/` (cloned garrytan/gstack) | 104K★ skill runtime source |
| Reference repos | `raw/repos/gbrain/` (cloned garrytan/gbrain) | 20K★ brain/memory system source |
| Architecture docs | `raw/bronze-docs/` | Design docs, YouTube transcripts, research |
| ... | (future) | Whatever we want to feed the brain |

**Rules for bronze:**

- **Append-only.** Never edit in place. New versions go alongside old ones.
- **No validation.** Accept everything. Let the Silver layer clean it.
- **Keep everything.** The original is the source of truth.

### Silver — Processing Layer (handled by gbrain)

**Goal:** Turn raw data into connected knowledge. gbrain ingests pages from
bronze, extracts entities, builds a knowledge graph, and runs a "dream cycle"
to consolidate everything overnight.

**What gbrain does to your data:**

```
Raw page (markdown, json, whatever)
    │
    ▼
gbrain put_page → stored in database (PGLite or Postgres)
    │
    ▼
Auto-link: regex parses markdown links, Obsidian wikilinks → typed edges
   (zero LLM calls — 3 regexes, one SQL batch insert)
    │
    ▼
Entity enrichment: page is linked to people, companies, concepts it mentions
    │
    ▼
Dream cycle (cron): consolidate related pages, fix citations, prune stale data
```

**Search in the Silver layer:**

gbrain uses 4 search strategies fused together:

```
  1. Vector search (pgvector HNSW) — semantic similarity
  2. BM25 keyword — exact phrase matching
  3. RRF fusion — merges both rankings without weighing one over the other
  4. Knowledge graph traversal — follows typed edges (works_at, founded, etc.)

  Combined: 49.1% P@5, 97.9% R@5 (vs ~18% for vector-only or keyword-only)
```

### Gold — Query Layer (handled by gbrain)

**Goal:** Ask questions, get answers with citations.

**What it looks like:**

```
You ask: "What do I need to know before meeting Alice tomorrow?"

gbrain answers:
  Alice runs engineering at Acme (series-B fintech). You last spoke
  April 22 in a pricing chat. Three things open:
    1. She owes you the security review (deadline was May 1)
    2. You committed to 500-seat pricing (sent April 25, no reply)
    3. She's hiring a CISO — you said you'd intro someone

  Heads up: nothing added about Alice or Acme since April 22.
  She may have replied through email/Slack — channels the brain
  doesn't see.
```

Every claim has a source page citation. The "heads up" at the end is gap
analysis — the brain tells you what it *doesn't* know, so you can ask.

---

## How This Changes OCR's Original Design

OCR's original design (in `raw/bronze-docs/`) planned to build its own
GBrain memory substrate from scratch — a cognitive state engine with 5
memory layers, custom ontology graph, custom activation protocol.

The new architecture is simpler and faster:

| Before (OCR build it all) | After (use gbrain) |
|--------------------------|-------------------|
| Build custom GBrain memory substrate (planned Sep-Oct 2026) | Use garrytan/gbrain — already built, 20K★, running on 146K pages |
| Build custom ontology graph from scratch | gbrain's auto-link extracts typed edges from markdown — zero LLM calls |
| Build custom search (vector + graph + temporal) | gbrain's hybrid search: 49.1% P@5, 97.9% R@5 |
| Build dream cycle consolidation | gbrain already has cron-based dream cycle |
| Build MCP interface for memory | gbrain has MCP server in src/mcp/ |
| 85-90% of architecture is aspirational | Working system, running in production |

### What OCR still builds

| Component | What it does | Status |
|-----------|-------------|--------|
| Bronze ingestion: GitHub MCP | Feeds commits into gbrain | Built |
| Bronze ingestion: Web scraper | Feeds web pages into gbrain | Built |
| Bronze ingestion: raw/repos/ | Cloned reference repos for gbrain to study | Cloned gstack + gbrain |
| gstack skill activation | gstack's SKILL.md format + OCR's activation engine | Design only |
| Council/Chairman | Parallel skill deliberation | Design only |
| Executive surfaces | Dashboard, podcast, strategic questions | One HTML file |

### What gbrain handles

| Function | gbrain component |
|----------|-----------------|
| Store pages | PGLite or Postgres + pgvector |
| Search | Hybrid (vector + BM25 + RRF + graph) |
| Entity extraction | Auto-link (regex, zero LLM) |
| Knowledge graph | Typed edges (works_at, founded, invested_in, etc.) |
| Synthesis | Query → answer with citations |
| Gap analysis | "Heads up: the brain doesn't know..." |
| Consolidation | Dream cycle (cron) |
| Multi-tenant | Brain × Source two-axis isolation |
| MCP access | stdio MCP server for any agent |

---

## Pipeline Flow (Complete)

```
                    ┌──────────────────────────────────────┐
                    │      BRONZE (raw ingestion)           │
                    │                                      │
                    │  GitHub MCP  ──→  commit pages        │
                    │  Web scraper ──→  markdown pages      │
                    │  raw/repos/  ──→  source code pages   │
                    │  raw/bronze-docs/ → design doc pages  │
                    │  YouTube     ──→  transcript pages    │
                    │  (future)    ──→  whatever             │
                    └────────────────┬─────────────────────┘
                                     │
                                     │ gbrain put_page (ingest)
                                     ▼
                    ┌──────────────────────────────────────┐
                    │      SILVER (gbrain processing)       │
                    │                                      │
                    │  Store in DB (PGLite / Postgres)      │
                    │  Auto-link entities (regex graph)     │
                    │  Enrich pages with links              │
                    │  Dream cycle: consolidate, fix, prune │
                    │  Index: vector + BM25 + graph         │
                    └────────────────┬─────────────────────┘
                                     │
                                     │ gbrain query (question)
                                     ▼
                    ┌──────────────────────────────────────┐
                    │      GOLD (gbrain answers)            │
                    │                                      │
                    │  "What do I need to know about X?"    │
                    │  → synthesized answer + citations     │
                    │  → gap analysis ("what I don't know") │
                    │                                      │
                    │  Used by:                             │
                    │  - gstack skills (/review, /qa, etc.) │
                    │  - OCR executive surfaces             │
                    │  - Any MCP-capable agent              │
                    └──────────────────────────────────────┘
```

---

## What This Becomes

This architecture turns OCR from "a system we build" into "a system we
assemble." The hard parts (memory, search, entity extraction, synthesis)
are handled by gbrain — a working, production-tested system. OCR provides:

1. **The ingestion pipeline** that feeds data INTO the brain (GitHub MCP,
   web scraper, etc.)
2. **The skill activation layer** (based on gstack's SKILL.md format) that
   makes the brain useful — ask questions, run reviews, get briefings
3. **The governance layer** that controls who sees what

The brain gets smarter over time as we feed it more bronze data. Every
GitHub commit, every web page scraped, every repo cloned — it all goes
into the same brain, linked together by the knowledge graph.
