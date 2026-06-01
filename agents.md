# OCR Agents Architecture

## Purpose

This document captures the architecture of the Organizational Cognition Runtime (OCR) and the agent-level design implied by the workspace documentation and diagrams.

It is built from:
- `ocr_kimi_2.6_raw_1.md`
- local architecture diagrams in `raw/images`
- web search context for related cognitive/runtime architectures

> **🗺️ City Map:** See [`CITY_MAP.md`](CITY_MAP.md) for the complete district atlas — every directory's purpose, blast radius, transit lines, and naming conventions. `_index.md` files in each directory are the neighborhood signposts.

## High-level design

OCR is not a generic agent platform. It is an organizational intelligence runtime built around:
- **Shipments** as atomic organizational actions
- **Ontology** as the shared cognitive substrate
- **GBrain** as the live memory substrate
- **Councils** as structured deliberation
- **Trajectories** as decision history and future-state modeling

The system is organized into these major layers:

1. Ingestion
2. Shipment compilation
3. Cognition runtime
4. Memory substrate
5. Governance and auditability
6. Executive surfaces

## Architecture overview

```mermaid
graph TB
    subgraph INGESTION["Ingestion Layer"]
        GH[GitHub MCP]
        OB[Obsidian Vault]
        WIKI[LLM Wiki]
        WS[Web Scraper]
        EXT[External Signals]
    end

    subgraph COMPILER["Shipment Compiler"]
        SC[Shipment Context Builder]
        OE[Ontology Extractor]
        CB[Context Bounding Engine]
        SV[Shipment Validator]
    end

    subgraph COGNITION["Cognition Runtime"]
        GS[GStack Skill Runtime]
        CO[Council Orchestrator]
        CH[Chairman Synthesizer]
        PA[Perspective Agents]
    end

    subgraph MEMORY["GBrain Memory Substrate"]
        OM[Ontology Manager]
        SM[Semantic Memory]
        TM[Trajectory Modeler]
        RM[Replay Manager]
    end

    subgraph SURFACES["Executive Surfaces"]
        ED[Executive Dashboard]
        PD[Podcast Synthesizer]
        SQ[Strategic Question Engine]
        CL[Cognition Log]
    end

    subgraph ORCH["n8n Orchestration DAGs"]
        N1[Ingestion DAG]
        N2[Shipment DAG]
        N3[Council DAG]
        N4[Memory DAG]
        N5[Governance DAG]
    end

    subgraph GOV["Governance & Auditability"]
        AL[Audit Ledger]
        LI[Lineage Index]
        AC[Access Control]
        OB2[Observability Bus]
    end

    INGESTION --> COMPILER
    COMPILER --> COGNITION
    COGNITION --> MEMORY
    MEMORY --> SURFACES
    ORCH --> COMPILER
    ORCH --> COGNITION
    ORCH --> MEMORY
    COGNITION --> GOV
    MEMORY --> GOV
    GOV --> SURFACES
```

## Deployment architecture

The current design is centered on a single-node VPS bootstrap with these core services:
- `n8n` orchestration fabric
- `FastAPI` OCR API
- `WebSocket` executive surface live updates
- `Keycloak OSS` authentication
- `Ollama` OSS LLM host
- `PostgreSQL` for audit / shipment / ontology state
- `Neo4j CE` for graph-based ontology and decision navigation
- `Redis` working memory cache
- `Obsidian Vault sync`
- `Playwright` browser automation (Chromium headless)
- `Firecrawl` cloud scraping API
- Persistent volumes with nightly S3-compatible backups

## Ingestion and signal flow

Signals arrive from repository events, Obsidian notes, LLM wiki, external APIs, and **web scraping** (documentation, articles, research). They are normalized into OCR events and routed through `n8n`.

Web scraping uses an intelligent **ScraperRouter** that automatically picks between:
- **Firecrawl** — cloud API, clean markdown output, fast (~2s), best for documentation sites and articles
- **Playwright** — local browser, handles anything a real browser can (~5s), best for interactive pages, SPAs, and login walls

The router checks URL patterns first, defaults to Firecrawl, checks content quality, and falls back to Playwright if the content is blocked or empty.

Important constraints:
- `n8n` is orchestration fabric only — no cognitive logic belongs in DAGs
- Event signing and rate limiting protect ingestion
- Scope checks quarantine out-of-manifest repositories
- PII / secrets are stripped before normalization

### Example commit pipeline

```mermaid
sequenceDiagram
    participant GH as GitHub MCP
    participant ING as Ingestion DAG (n8n)
    participant OE as Ontology Extractor
    participant SC as Shipment Compiler
    participant TM as Trajectory Modeler
    participant GB as GBrain
    participant SQ as Strategic Question Engine

    GH->>ING: Commit event (diff, message, author, PR)
    ING->>OE: Extract: files changed, concepts mentioned, dependencies modified
    OE->>OE: Resolve to ontology nodes (component, feature, person, decision)
    OE->>SC: Ontology diff + commit metadata

    alt Structural change detected
        SC->>SC: Classify as architectural shipment
        SC->>GB: Query: what decisions depend on this component?
        GB->>SC: Dependent decision graph
        SC->>CO: High-priority council: Architect + Risk + Execution
    else Documentation change
        SC->>SC: Classify as knowledge shipment
        SC->>OE: Update LLM Wiki with new semantic content
    else Feature commit
        SC->>TM: Emit tactical trajectory delta
        TM->>SQ: Check: does this commit contradict a strategic decision?
    end

    GB->>GB: Update component state in ontology
    TM->>TM: Record: org is executing on [concept cluster]
```

## Cognitive activation and agents

OCR routes shipments into a council using an activation engine that computes:

```text
ActivationScore(skill, shipment) =
    w1 * OntologyOverlap(skill.jurisdiction, shipment.entities) +
    w2 * TrajectoryRelevance(skill.history, shipment.trajectory) +
    w3 * CouncilBalance(current_council, skill.perspective) +
    w4 * PriorContribution(skill.id, similar_shipments)
```

Key activation principles:
- `OntologyOverlap` ensures domain relevance
- `TrajectoryRelevance` ensures historical context
- `CouncilBalance` prevents echo chambers by boosting missing perspectives
- `PriorContribution` rewards skills with relevant past input

### Skill runtime

The skill registry can include roles such as:
- Strategic Analyst
- Technical Architect
- Risk Assessor
- Customer Advocate
- Financial Modeler
- Execution Tracker
- Ontologist
- Devil Advocate

Skills execute in parallel threads with isolated context slices. The chairman only receives position summaries, not raw internal reasoning.

## Council deliberation

Deliberation is a structured protocol with independent reasoning and synthesis.

```mermaid
sequenceDiagram
    participant CO as Council Orchestrator
    participant S1 as Skill: Strategic
    participant S2 as Skill: Technical
    participant S3 as Skill: Risk
    participant S4 as Skill: Devil Advocate
    participant CH as Chairman
    participant GOV as Governance Check

    CO->>S1: Independent reasoning (context slice A)
    CO->>S2: Independent reasoning (context slice B)
    CO->>S3: Independent reasoning (context slice C)
    CO->>S4: Independent reasoning (context slice D)

    Note over S1,S4: All skills reason in parallel, NO cross-contamination

    S1->>CH: Position + confidence + evidence refs
    S2->>CH: Position + confidence + evidence refs
    S3->>CH: Position + confidence + evidence refs
    S4->>CH: Position + confidence + evidence refs

    CH->>CH: Contradiction detection (semantic diff)
    CH->>CH: Consensus mapping
    CH->>CH: Synthesis draft v1

    alt Contradiction threshold exceeded
        CH->>CO: Request second round (targeted)
        CO->>S1: Respond to S3 contradiction specifically
        S1->>CH: Rebuttal position
        S3->>CH: Counter-rebuttal
        CH->>CH: Synthesis draft v2
    end
```

### Governance outcomes

Council synthesis is validated before commit:
- `Validated` → commit to GBrain and surface to executives
- `HumanReview` → executive input requested
- `Rejected` → audit log entry and flag

Governance rules include:
- No orphan decisions
- Explainability before commitment
- Backward lineage for every decision

## GBrain memory substrate

GBrain is intentionally not a vector store. It is a cognitive state engine with layered memory, operations, and indexed navigation.

```mermaid
graph TB
    subgraph GBRAIN["GBrain — Memory Substrate"]
        subgraph LAYERS["Memory Layers"]
            WM[Working Memory - Active Shipments]
            EM[Episodic Memory - Shipment History]
            SM[Semantic Memory - Ontology Graph]
            PM[Procedural Memory - Skill Protocols]
            TM[Temporal Memory - Trajectories]
        end

        subgraph OPERATIONS["Memory Operations"]
            MA[Memory Activation]
            MC[Memory Consolidation]
            MD[Memory Decay]
            MR[Memory Replay]
            MU[Memory Update]
        end

        subgraph INDEX["Index Layer"]
            VI[Vector Index - semantic search fallback]
            GI[Graph Index - primary navigation]
            TI[Temporal Index - time-aware retrieval]
            OI[Ontology Index - concept navigation]
        end
    end

    WM <--> MA
    EM <--> MC
    SM <--> MU
    TM <--> MR

    MA --> GI
    MC --> OI
    MD --> TI
    MR --> VI
```

### Activation protocol

When a shipment arrives, the memory activation protocol is:
1. Ontology Anchor: resolve named entities to graph nodes
2. Trajectory Walk: trace 3–5 prior decision steps
3. Contradiction Surface: locate contradicting or superseding edges
4. Recency Decay: weight recent decisions higher while preserving old lore
5. Confidence Propagation: degrade confidence through relays

## Ontology architecture

The ontology is the shared backbone with:
- Core concepts: Products, People/Roles, Platform Components, Decisions, Objectives, Risks, Dependencies
- Relation types: owns, blocks, enables, contradicts, supersedes, depends_on, evolved_from, aligns_with, threatens
- Meta properties: temporal versions, confidence scores, source citations, author attribution

Ontology evolution follows:
- Shipment-driven promotion of candidate nodes
- Contradiction-driven refinement and concept splitting
- Dormancy and archival for low-use concepts
- Executive-origin injection with higher scrutiny

```mermaid
flowchart LR
    SIG[Signal arrives] --> EXT[Ontology Extractor]
    EXT --> |New entity| CAND[Candidate Node]
    EXT --> |Existing entity| CONF[Confirm + strengthen edge]
    CAND --> |3+ references| PROM[Promoted to confirmed]
    CAND --> |0 references, 30 days| DISC[Discarded]
```

## Executive surfaces and outputs

OCR surfaces cognition through:
- Executive dashboard and live updates
- Strategic question engine
- Cognition log
- Podcast-style audio summarization
- Trajectory browser and decision timeline

## Governance and auditability

The audit layer is append-only with:
- shipment snapshots
- context window snapshots
- council input snapshots
- chairman synthesis versions
- governance decisions

Replay manager enables:
- audit reviews
- counterfactual comparison
- training / debugging

Governance also includes:
- policy engine for scope, council composition, escalation, data residency, human-in-loop
- access controls for roles, tenants, skills, and memory tiers

## Web search context

Web results confirm OCR is aligned with broader cognitive/runtime patterns such as:
- governed cognitive runtimes
- artifact-centric cognitive execution
- layered memory architectures
- explicit audit and policy control
- cognitive mesh / enterprise cognitive architecture

Examples found in search results:
- Dexter — Governed Cognitive Runtime Research
- Cognitive Runtime (structured AI runtime)
- Cognitive Mesh Architecture
- Layered Cognitive Architecture for organizational cognition

## Web scraping

OCR ingests web content through an intelligent two-tier scraper:

| Tool | Role | Latency | Best for |
|------|------|---------|----------|
| **Firecrawl** | Cloud scraping API | ~2s | Documentation, articles, static pages |
| **Playwright** | Local headless browser | ~5s | SPAs, login walls, interactive pages |

The **ScraperRouter** (`ingestion/web/scraper.py`) checks URL patterns first,
defaults to Firecrawl, validates content quality, and falls back to Playwright
when return content is empty, blocked, or boilerplate-only.

See `docs/ingestion/scraper.md` for the full routing design and
`docs/ingestion/browser-automation-mcp.md` for the landscape comparison.

The Firecrawl usage reference skill is at `~/.claude/skills/firecrawl/SKILL.md`
(Python SDK patterns, CLI commands, and OCR integration notes).

## Notes

This document is a workspace-level architecture summary and agent design guide. It is intended to be the reference for implementing or extending the OCR runtime.
