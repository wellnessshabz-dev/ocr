# Skill-to-OCR Architecture Mapping

Maps each of the 17 installed skills against the layers of the Organizational Cognition Runtime (OCR) defined in `agents.md`.

## OCR Architecture Layers (ref: agents.md)

1. **Ingestion Layer** — GitHub MCP, Obsidian Vault, LLM Wiki, External Signals
2. **Shipment Compiler** — Context Builder, Ontology Extractor, Context Bounding, Validator
3. **Cognition Runtime** — GStack Skill Runtime, Council Orchestrator, Chairman, Perspective Agents
4. **GBrain Memory Substrate** — Ontology Manager, Semantic/Trajectory/Replay memory, Graph/Vector/Temporal indices
5. **Executive Surfaces** — Dashboard, Podcast Synthesizer, Strategic Question Engine, Cognition Log
6. **Governance & Auditability** — Audit Ledger, Lineage Index, Access Control, Observability Bus
7. **Orchestration (n8n)** — Ingestion/Shipment/Council/Memory/Governance DAGs

---

## Directly Useful Skills (core OCR build)

### mcp-builder
**OCR Layer: Ingestion**
OCR's Ingestion layer already references "GitHub MCP" as a source. MCP servers are the protocol bridge between LLMs and external services. This skill enables building MCP servers for any ingestion source — not just GitHub, but Obsidian, wikis, ticketing systems, CRMs, etc. Every external signal connector in OCR could be an MCP server built with this skill.

### skill-creator
**OCR Layer: Cognition Runtime**
OCR's Cognition Runtime has a "GStack Skill Runtime" with "Perspective Agents" — each council role (Strategic Analyst, Technical Architect, Risk Assessor, Customer Advocate, Financial Modeler, etc.) is fundamentally a skill. This skill provides the end-to-end workflow to create, evaluate, and iterate on each council skill with test prompts, benchmarking, and grading. It is the meta-tool for populating the entire council registry.

### claude-api
**OCR Layer: Cognition Runtime, Shipment Compiler**
The entire Cognition Runtime runs on LLM calls. This skill covers prompt caching, adaptive thinking, tool use, structured outputs (JSON mode), streaming, batch processing, and file uploads — all essential for building the council orchestration, chairman synthesis, and ontology extraction. Prompt caching alone is critical for the "independent reasoning" phase where multiple skills run in parallel with overlapping context.

### frontend-design
**OCR Layer: Executive Surfaces**
The Executive Dashboard, Strategic Question Engine, and Trajectory Browser are web UIs that need to be "distinctive, production-grade" — exactly what this skill is built for. It emphasizes bold aesthetics, cohesive color, and memorable design over generic patterns.

### webapp-testing
**OCR Layer: Executive Surfaces, Governance**
Playwright-based testing for the executive dashboard and other web surfaces. Essential for QA before shipping UI changes. Also useful for governance-driven UI validation.

---

## Report/Output Generation Skills

### doc-coauthoring
**OCR Layer: Executive Surfaces (Cognition Log)**
Co-authored decision documents, technical specs, and strategic proposals are natural outputs of the Cognition Runtime. Every council synthesis could be co-authored as a structured document using this workflow — especially the "Reader Testing" phase (testing the doc with a fresh agent) to catch blind spots in decision communication.

### pptx
**OCR Layer: Executive Surfaces**
PowerPoint decks from council syntheses, strategic reviews, or trajectory reports. The Cognition Log → slide deck pipeline.

### pdf
**OCR Layer: Executive Surfaces**
PDF reports, governance documents, audit snapshots. The "Governance & Auditability" layer captures append-only shipment snapshots — these could be output as PDFs for external review.

### docx
**OCR Layer: Executive Surfaces**
Word documents from the Cognition Log or strategic analysis. Alternative format for delivering council findings.

### xlsx
**OCR Layer: Executive Surfaces, GBrain (analytics)**
Spreadsheet exports from trajectory data, ontology metrics, or financial modeling from the Financial Modeler skill. The skill's financial-modeling conventions (blue inputs, black formulas, green cross-references) align with the "Financial Modeler" council role.

### slack-gif-creator
**OCR Layer: Executive Surfaces (Notifications)**
Animated GIF notifications for Slack — useful for alerting executives to new shipments, council outcomes, or governance flags in a lightweight, glanceable format.

---

## Design & Branding Skills

### brand-guidelines
**OCR Layer: Executive Surfaces**
Consistent brand identity across all executive surfaces — dashboard, reports, slides, cognition log. This skill bakes in a specific brand (Anthropic) but the pattern applies to any organization running OCR.

### theme-factory
**OCR Layer: Executive Surfaces**
10 pre-built visual themes for consistently styling dashboard, reports, and slide decks. Complements brand-guidelines by providing the actual theme palette and font pairing application.

### canvas-design
**OCR Layer: Executive Surfaces (visual assets)**
Poster/print-quality static visual art for executive dashboards or strategic communications. Could create cover images for cognition log entries or visual summaries of trajectories.

### algorithmic-art
**OCR Layer: Executive Surfaces (data viz)**
Generative art with p5.js — could be used for live data visualizations on the executive dashboard (flow fields for decision trajectories, particle systems for organizational dynamics, noise fields for risk surfaces).

### web-artifacts-builder
**OCR Layer: Executive Surfaces**
Complex React 18 + Tailwind HTML artifacts. Could build interactive decision-tree explorers, trajectory browsers, or ontology graph visualizations as self-contained HTML artifacts for the executive surfaces.

---

## Interaction & Documentation Skills

### internal-comms
**OCR Layer: Executive Surfaces (Cognition Log)**
Internal communication templates — 3P updates (Progress, Plans, Problems), company newsletters, incident reports. The Cognition Log output could be formatted using these templates to produce organization-readable updates: "This week's strategic decisions (3P)", "Ontology change log (newsletter)", "Governance incident report".

---

## Summary

| Skill | OCR Layer | Use Case |
|---|---|---|
| mcp-builder | Ingestion | Build MCP servers for every signal source |
| skill-creator | Cognition Runtime | Create/evaluate every council perspective agent |
| claude-api | Cognition Runtime, Compiler | LLM calls for council, chairman, ontology extraction |
| frontend-design | Executive Surfaces | Dashboard, Strategic Question Engine UI |
| webapp-testing | Executive Surfaces | Playwright QA for dashboard/surfaces |
| doc-coauthoring | Executive Surfaces | Co-author council decision documents |
| pptx | Executive Surfaces | Slide decks from syntheses |
| pdf | Executive Surfaces | Audit snapshots, reports |
| docx | Executive Surfaces | Decision docs, cognition log |
| xlsx | Executive Surfaces, GBrain | Financial models, trajectory data exports |
| slack-gif-creator | Executive Surfaces | Slack notifications |
| brand-guidelines | Executive Surfaces | Brand identity across all surfaces |
| theme-factory | Executive Surfaces | Visual theme application |
| canvas-design | Executive Surfaces | Static visual assets |
| algorithmic-art | Executive Surfaces | Generative data visualizations |
| web-artifacts-builder | Executive Surfaces | Interactive HTML artifacts |
| internal-comms | Executive Surfaces | Cognition Log formatting, org updates |
