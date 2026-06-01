---
title: OCR Architecture Diagrams
description: Index of 24 architecture diagrams for the Organizational Cognition Runtime (OCR)
source: ocr_kimi_2.6_raw_1.md (2333-line principal architecture document; also partitioned into 24 files at raw/bronze-docs/ocr_kimi_2.6_raw_1/)
coverage: Parts I-XXII of the OCR architecture specification
export_date: 2026-06-01
total_diagrams: 24
generated_with: mermaid-cli (mmdc)
note: Diagrams 20-24 were regenerated from mermaid blocks in ocr_kimi_2.6_raw_1.md after the original export omitted them
---

# OCR Architecture Diagrams

## Sequencing Flow

The 24 diagrams follow the OCR data flow: how a **signal** enters the system, becomes a **shipment**, gets deliberated by a **council**, commits to **memory**, and surfaces to **executives**. Read them in numeric order.

```
01-02  System Overview + Legend
   │
   ▼
03     Ontology Evolution (entity lifecycle)
04     Cognition Runtime State Machine
   │
   ▼
05     Shipment Flow Sequence
   │
   ▼
06     GStack Skill Activation
07     Council Deliberation Protocol
   │
   ▼
08-09  GBrain Memory Architecture + Ontology Structure
10     Trajectory Modeling
   │
   ▼
11     Commit Pipeline
12     Executive Surfaces
   │
   ▼
13-14  Trajectory Styling Legend + Section Header
   │
   ▼
15     n8n DAG Architecture
16     Graph Schema
   │
   ▼
17-18  Tenancy Legend + Podcast Flow
   │
   ▼
19     Deployment Architecture
   │
   ▼
20     Governance and Auditability
21     MCP Ingestion Security
22     Obsidian-Repo Linkage
23     Multi-Tenant Cognition
   │
   ▼
24     Roadmap Gantt (timeline)
```

---

## Diagram Index

### 01 — System Overview Architecture
- **Source:** `01_system_overview_architecture.md`, L5-L129
- **Type:** `graph TB` — 7-layer block diagram
- **Description:** Top-level view of the entire OCR stack. Shows 7 major subsystems: Ingestion Layer, Shipment Compiler, Cognition Runtime, GBrain Memory Substrate, Executive Surfaces, n8n Orchestration DAGs, and Governance & Auditability. Arrows show data flow from ingestion through compilation, cognition, memory, and surfaces. Orchestration wraps the middle layers; governance wraps everything.
- **Significance:** This is the entry point for understanding OCR. Every other diagram is a deep dive into one of these boxes.

### 02 — Sidebar Legend
- **Source:** Standalone legend (no mermaid block)
- **Description:** Visual legend for the architecture diagrams — node shapes, arrow styles, color coding, and symbol meanings. Used as a reference when reading all other diagrams.

### 03 — Ontology Evolution Flowchart
- **Source:** `07_ontology_architecture.md`, L119-L141
- **Type:** `flowchart LR`
- **Description:** Entity lifecycle management in the ontology. A signal arrives → Ontology Extractor classifies it as New Entity (→ Candidate Node) or Existing Entity (→ Confirm + strengthen edge). Candidate promoted to confirmed after 3+ references; discarded after 30 days with zero references. Contradictions trigger concept splits via council review. Dormant concepts archived but never deleted.
- **Significance:** Implements the "no ontology pollution" principle.

### 04 — Cognition Runtime State Machine
- **Source:** `02_cognition_runtime_architecture.md`, L9-L53
- **Type:** `stateDiagram-v2`
- **Description:** The complete lifecycle of the runtime as a state machine. Starts Dormant → Activated by shipment → ContextLoaded → OntologyAnchored → CouncilFormed → Deliberating → Synthesizing → Validated → Committed → Surfaced → back to Dormant. Error paths: Deliberating can escalate to HumanReview; Validated can Reject to Flagged.
- **Significance:** This is the heartbeat of OCR. Every cognitive event traces through these states.

### 05 — Shipment Flow Sequence
- **Source:** `03_shipment_architecture.md`, L29-L89
- **Type:** `sequenceDiagram`
- **Description:** Full end-to-end sequence from raw signal to committed cognition. Source sends signal → Shipment Compiler → Ontology Extractor (returns diff) → Context Bounding Engine (queries GBrain for relevant memory within token budget) → validates → emits frozen Shipment v1.0 → Council Orchestrator assigns seats → Chairman deliberates → Audit Ledger records → Trajectory Modeler updates → Result returned to source.
- **Significance:** The atomic unit of work in OCR. Every organizational action follows this path.

### 06 — GStack Skill Activation Runtime
- **Source:** `04_gstack_skill_activation_runtime.md`, L23-L93
- **Type:** `graph LR`
- **Description:** Three-column flow. Left: Skill Registry with 8 perspective agents (Strategic Analyst, Technical Architect, Risk Assessor, Customer Advocate, Financial Modeler, Execution Tracker, Ontologist, Devil Advocate). Middle: Activation Engine (Shipment Metadata → Ontology Anchor → Skill Router → Prerequisite Loader → Context Thread Allocator). Right: Runtime Threads executing in parallel (Strategic, Technical, Risk, Advocacy). All threads feed into the Chairman Synthesizer.
- **Significance:** Implements the multi-perspective deliberation. Skills are not prompts — they are cognitive roles with declared perspectives.

### 07 — Council Deliberation Protocol
- **Source:** `05_council_architecture.md`, L9-L83
- **Type:** `sequenceDiagram`
- **Description:** Orchestrator sends independent reasoning tasks to 4 skills in parallel (Strategic, Technical, Risk, Devil Advocate). Each returns Position + confidence + evidence refs. Chairman performs contradiction detection and consensus mapping → Synthesis v1. If contradiction threshold exceeded → second round targeted rebuttals → Synthesis v2. Final synthesis submitted to Governance Check → Approved/Escalate/Reject.
- **Significance:** This is OCR's core differentiator — structured deliberation, not round-robin prompting.

### 08 — GBrain Memory Architecture
- **Source:** `06_gbrain_memory_architecture.md`, L13-L131
- **Type:** `graph TB`
- **Description:** Three-column memory substrate. Left: 5 Memory Layers (Working Memory for active shipments, Episodic for history, Semantic for ontology graph, Procedural for skill protocols, Temporal for trajectories). Middle: 5 Memory Operations (Activation, Consolidation, Decay, Replay, Update). Right: 4 Index types (Vector for search fallback, Graph for primary navigation, Temporal for time-aware retrieval, Ontology for concept navigation).
- **Significance:** GBrain is intentionally NOT a vector store — it is a cognitive state engine.

### 09 — Ontology Architecture
- **Source:** `07_ontology_architecture.md`, L13-L83
- **Type:** `graph TB`
- **Description:** Three-part ontology structure. Top: Core Concepts (Products, People-Roles, Platform Components, Decisions, Objectives, Risks, Dependencies). Middle: Relation Types (owns, blocks, enables, contradicts, supersedes, depends_on, evolved_from, aligns_with, threatens). Bottom: Meta-Ontology (Temporal Versions, Confidence Scores, Source Citations, Author Attribution).
- **Significance:** The ontology is the shared cognitive substrate — not just a knowledge graph but the organization's meta-cognitive map.

### 10 — Trajectory Modeling
- **Source:** `08_trajectory_modeling.md`, L25-L57
- **Type:** `graph LR`
- **Description:** Horizontal decision timeline: T0 Org State → Decision (Platform v1) → T1 → Decision (API-first) with counterfactual branch (Monolith-first — NOT TAKEN, stored as counterfactual) → T2 → Decision (OSS LLM) → T3 (Current) → momentum → Projected trajectory → uncertainty cone → Future Decision Space.
- **Significance:** Trajectories enable counterfactual reasoning and strategic drift detection.

### 11 — Commit Pipeline Sequence
- **Source:** `09_repo_changes_and_organizational_state.md`, L9-L69
- **Type:** `sequenceDiagram`
- **Description:** GitHub MCP sends commit event → Ingestion DAG → Ontology Extractor resolves entities → Shipment Compiler. Three alt branches: Structural change (→ query GBrain for dependent decisions → high-priority council), Documentation change (→ update LLM Wiki), Feature commit (→ trajectory delta → check for strategic contradiction). GBrain updates component state; Trajectory Modeler records concept cluster execution.
- **Significance:** Not every commit triggers a full council — the significance classifier routes to the appropriate processing depth.

### 12 — Executive Cognition Surfaces
- **Source:** `10_executive_cognition_surfaces.md`, L23-L91
- **Type:** `graph TB`
- **Description:** Four-quadrant executive interface. Now View: Current State Snapshot, Active Questions, Escalations. Trajectory View: Decision Log (90 days), Momentum Map (concept heatmap), Counterfactual Browser. Deep Dive: Shipment Replay, Council Transcripts, Ontology Visualizer. Audio Synthesis: Weekly Cognition Podcast, Decision Briefing.
- **Significance:** Executives get narrative, not dashboards with 47 metrics.

### 13 — Trajectory Styling Legend
- **Source:** Standalone legend for the Trajectory diagram
- **Description:** Specific legend for the three styled elements in the Trajectory Modeling diagram: counterfactual stored branches (dark red / #2d1b1b), projected trajectory (dark green / #1b2d1b), future decision space (dark blue / #1b1b2d).

### 14 — Section Header Banner
- **Source:** Standalone decorative element
- **Description:** Decorative divider/header banner used between major sections of the architecture document.

### 15 — n8n DAG Architecture
- **Source:** `12_n8n_dag_architecture.md`, L13-L117
- **Type:** `graph TB`
- **Description:** Five orchestration DAGs. DAG 1 (Ingestion): GitHub webhook/Obsidian/Scheduled → Classify → Ontology Extractor → Route → Audit. DAG 2 (Shipment Lifecycle): New shipment → Activate skills → Fan-out → Wait → Chairman → Governance → Commit → Notify. DAG 3 (Memory Consolidation): Nightly decay → Promote nodes → Update vectors → Weekly summary. DAG 4 (Governance Audit): Shipment committed → Hash → Append log → Policy check → Alert. DAG 5 (Executive Pulse): Monday 08:00 → Trajectory report → Podcast → Strategic questions → Deliver.
- **Significance:** n8n is orchestration fabric only — NO cognitive logic lives in the DAGs.

### 16 — Graph Schema
- **Source:** `13_graph_schema.md`, L13-L73
- **Type:** `graph TB`
- **Description:** Seven node types (Decision, Concept, Shipment, Person-Role, Repo, Question, Trajectory) connected by seven edge types: resulted_in (weight, confidence, timestamp), evolved_from (diff, author, timestamp), contradicts (severity, resolved_by), depends_on (coupling_strength, verified), authored_by (role_at_time), surfaces_question (urgency, open_since), belongs_to_trajectory (position_index).
- **Significance:** This is NOT a standard knowledge graph — it is an organizational cognitive graph where the primary entities are decisions, not facts.

### 17 — Sidebar Legend (Tenancy)
- **Source:** Standalone legend
- **Description:** Visual legend for multi-tenancy notation used in the architecture diagrams.

### 18 — Podcast Generation Flow
- **Source:** `11_podcast_notebooklm_style_synthesis.md`, L17-L43
- **Type:** `flowchart TD`
- **Description:** Weekly cognition podcast pipeline: Weekly pulse triggers Podcast DAG → Retrieve all shipments → Trajectory Modeler (what moved?) → Strategic Question Engine (what's unresolved?) → Chairman (most significant decision) → Narrative Outliner (story arc) → Story beats (Setup/Tension/Decision/Implication) → Two-voice script generator (Host + Analyst personas) → TTS (OSS voice synthesis) → Audio stored in GBrain as episodic memory → Linked to all referenced shipments → Delivered to executive surface.
- **Significance:** Two-voice narration naturally surfaces the tension in decisions without requiring executives to read between the lines.

### 19 — Deployment Architecture
- **Source:** `20_deployment_architecture.md`, L5-L77
- **Type:** `graph TB`
- **Description:** Single-node VPS bootstrap. Three layers inside VPS. Core Services: n8n, Ollama (OSS LLM), PostgreSQL (audit/shipments/ontology), Neo4j CE (graph), Redis (cache), Obsidian Vault sync. Application Layer: FastAPI OCR API, WebSocket for live executive updates, Keycloak OSS auth. Storage: Persistent volumes for all state, nightly backups to S3-compatible. External Clients: Executive web surface, GitHub webhooks, Obsidian plugin.
- **Significance:** Enterprise organizational intelligence for ~$50-100/month to start.

### 20 — Governance and Auditability
- **Source:** `15_governance_and_auditability.md`, L5-L79
- **Type:** `graph TB`
- **Description:** Four-layer governance structure. Governance Layer contains three sub-systems: Policy Engine (shipment scope, council composition, escalation thresholds, data residency, human-in-loop), Audit System (append-only ledger, hash chain, tamper detection, export API), and Access Controls (RBAC, tenant separation, skill scopes, memory tiers). A separate Human Override Layer sits above with Executive Injection, Human Review Queue, Veto, and Annotation capabilities. Policy feeds into audit, audit controls access, humans override policy and audit.
- **Significance:** Implements the four governance rules: no orphan decisions, human override always wins, append-only audit, explainability before commitment.

### 21 — MCP Ingestion Security
- **Source:** `16_mcp_ingestion_security.md`, L5-L29
- **Type:** `flowchart TD`
- **Description:** Security pipeline for external signal ingestion. GitHub MCP endpoint → Webhook signature verification (valid→continue, invalid→drop+alert) → Payload sanitization → Scope check (in manifest→continue, out of scope→quarantine+review) → Rate limiting → PII stripping (emails, tokens, secrets) → Normalize to OCR event schema → Sign with org key → Ingestion DAG. Each stage is a security gate.
- **Significance:** Prevents injection attacks, data leaks, and ingestion floods. Every payload is verified, scoped, rate-limited, sanitized, and signed before reaching the cognitive runtime.

### 22 — Obsidian-Repo Evolution Linkage
- **Source:** `17_obsidian_repo_evolution_linkage.md`, L13-L69
- **Type:** `sequenceDiagram`
- **Description:** Bidirectional thinking-doing bridge. Top half: Obsidian Vault → Watcher → Ontology Extractor → GBrain (thinking trajectory). Bottom half: GitHub Repo → Ontology Extractor → GBrain queries for linked thinking doc → Trajectory Modeler (doing trajectory). Trajectory Modeler checks alignment: if misaligned → surfaces strategic question ("thinking says X, doing says Y"); if aligned → strengthens the note-commit link.
- **Significance:** Automatically detects strategy-execution drift. The org said it would do X (in RFCs/meeting notes), but the repos are doing Y — that is a strategic signal, not a bug.

### 23 — Multi-Tenant Cognition
- **Source:** `19_multi_tenant_cognition.md`, L5-L71
- **Type:** `graph TB`
- **Description:** Platform layer (Runtime Orchestrator, Shared Skill Registry, Shared Infrastructure) serves multiple isolated tenants. Tenant A and Tenant B each have their own GBrain, Ontology, Shipment Store, and Trajectory — fully isolated cognitive spaces. Isolation Guarantees: no cross-tenant memory activation, no cross-tenant ontology pollution, separate audit ledgers, separate encryption keys.
- **Significance:** Enforced at the memory layer, not the model layer. The same OSS LLM serves all tenants because the LLM is stateless — all organizational state lives in GBrain, which is tenant-isolated.

### 24 — Roadmap Gantt Chart
- **Source:** `22_roadmap_evolution.md`, L5-L73
- **Type:** `gantt`
- **Description:** 18-month implementation timeline across 5 phases. Foundation (Jun-Oct 2026): VPS setup, GitHub ingestion, Ontology Extractor, Shipment Compiler. Cognition Core (Sep 2026-Jan 2027): GStack, Council Orchestrator, Chairman, GBrain. Memory and Graph (Jan-Apr 2027): Neo4j, Trajectory Modeler, Obsidian Linkage, Strategic Questions. Executive Surface (Apr-Jul 2027): Dashboard, Podcast, Replay Manager. Enterprise Grade (Jul 2027-Jan 2028): Governance, Multi-tenant, Enterprise Auth, Ontology v2.
- **Significance:** The strategic build order — memory before intelligence, deliberation before synthesis, ontology before RAG.

---

## OCR Layer Mapping

Each diagram maps to one or more OCR architecture layers from `agents.md`:

| Diagram | Ingestion | Compiler | Cognition | GBrain | Surfaces | Governance | n8n |
|---|---|---|---|---|---|---|---|
| 01 System Overview | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 02 Legend | — | — | — | — | — | — | — |
| 03 Ontology Evolution | — | ✓ | — | ✓ | — | — | — |
| 04 State Machine | — | — | ✓ | — | — | — | ✓ |
| 05 Shipment Flow | ✓ | ✓ | ✓ | ✓ | — | ✓ | — |
| 06 GStack Activation | — | — | ✓ | — | — | — | — |
| 07 Council Protocol | — | — | ✓ | — | — | ✓ | — |
| 08 GBrain Memory | — | — | — | ✓ | — | — | — |
| 09 Ontology | — | ✓ | — | ✓ | — | — | — |
| 10 Trajectory | — | — | — | ✓ | — | — | — |
| 11 Commit Pipeline | ✓ | ✓ | — | ✓ | — | — | ✓ |
| 12 Executive Surfaces | — | — | — | ✓ | ✓ | — | — |
| 13 Trajectory Legend | — | — | — | ✓ | — | — | — |
| 14 Section Header | — | — | — | — | — | — | — |
| 15 n8n DAGs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 Graph Schema | — | — | — | ✓ | — | ✓ | — |
| 17 Tenancy Legend | — | — | — | — | — | ✓ | — |
| 18 Podcast Flow | — | — | ✓ | ✓ | ✓ | — | ✓ |
| 19 Deployment | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 Governance | — | — | — | — | ✓ | ✓ | ✓ |
| 21 MCP Security | ✓ | — | — | — | — | — | ✓ |
| 22 Obsidian-Repo | — | — | — | ✓ | — | — | ✓ |
| 23 Multi-Tenant | — | — | — | ✓ | — | ✓ | — |
| 24 Roadmap | — | — | — | — | — | — | — |


