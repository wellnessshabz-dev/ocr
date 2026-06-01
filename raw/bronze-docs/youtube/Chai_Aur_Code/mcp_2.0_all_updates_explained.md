---
title: "MCP 2.0 — All Updates Explained (Chai Aur Code)"
source_type: "youtube"
channel: "Chai Aur Code"
speaker: "Chai Aur Code (Hitesh Choudhary)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Hindi tech channel Chai Aur Code by Hitesh Choudhary. Deep dive into MCP 1.0 → 2.0 (v2026) updates — stateless protocol, extensions/apps, OAuth, caching, tracing, and deprecation policy. Release candidate available now, final release July 28."
tags: ["mcp", "model-context-protocol", "stateless", "oauth", "extensions", "apps", "caching", "tracing", "task-extensions", "protocol-evolution"]
---

# MCP 2.0 — All Updates Explained (Chai Aur Code)

Source: Chai Aur Code (Hitesh Choudhary). Comprehensive walkthrough of all
MCP updates in the v2026 release (called MCP 2.0 due to magnitude of changes).

## Context: What is MCP?

Model Context Protocol — a standardized protocol for AI agents to communicate
with external systems (tools, databases, documentation, APIs). Think of it as
a **USB-C port for AI applications** — a common language so any agent (Claude,
Cursor, Gemini) can connect to any service (hosting, databases, APIs).

MCP is not just documentation delivery — it carries tools, functions for
database connections, search tools, calculators, and complex integrations.

## Update 1: Stateless Protocol (Breaking Change)

### Before (Stateful)
- MCP servers issued **session IDs** for each connection
- Servers stored session state in databases
- Like a kirana store giving you a token/slip — only works with that specific
  shopkeeper, only that shop, lost if the shopkeeper is on leave
- Scaling required shared state infrastructure (database bottleneck)

### After (Stateless)
- Each request is self-contained — all data needed is in the request itself
- No session IDs, no server-side state storage
- Like web requests (HTTP is stateless) — any server instance can handle any
  request
- Benefits: simple round-robin load balancing, high availability, easy scaling
- Breaking change: ALL existing MCP servers must update (session ID removed)

## Update 2: Server-to-Client Communication (Ellicitation)

Problem: Without sessions, how does the server ask the client questions mid-
request? (e.g., "Should I delete these 3 files?")

### Two Rules

1. **In-Flight Rule**: Server can only ask client questions while actively
   processing a client's request. No unsolicited popups or background queries.

2. **Special Response Rule**: Server sends a special response containing:
   - A **question** (e.g., "Can I delete 3 files?")
   - A **request state** (how much work is done so far — algorithm progress,
     image processing status, etc.)
   - A **request ID** for continuity

### How It Works (Stateless Elicitation)

1. Client sends initial request ("delete 3 files")
2. Server processes, hits a decision point, sends special response:
   - Question: "Confirm deletion?"
   - Request state: encoded work-in-progress
   - Request ID
3. Client shows question to user (not the request ID — just the question)
4. User answers (yes/no/detailed)
5. Client resends: answer + request state + request ID
6. **Any server instance** can pick up the retry because the state is in the
   request, not on the server

This enables **parallel agents** — the original agent can go do other work
while any free agent instance continues the task. Previously, the agent that
asked the question had to wait for the answer.

## Update 3: Traffic/Routing — Headers for Load Balancing

MCP method and name are now included in HTTP headers, not just the body.

- Load balancers can read headers and route without parsing the full request
- Like a security guard checking a badge without opening the bag
- Multiple client instances can be routed efficiently
- Enables easy load balancing and request distribution

This is a sign of protocol maturity — raw protocol becoming infrastructure-
ready with standard header-based routing.

## Update 4: Caching

Servers can now declare:
- **TTL (Time To Live)**: How long a result should be cached
- **Cache Scope**: Per-user or global (all users)

Like Swiggy app — you download your city's menu, not all of India's menus.
When new restaurants are added, the cache expires. Reduces server load,
improves response times.

## Update 5: Monitoring & Tracing Layer

Distributed tracing using **W3C trace context**:

- Headers carry vendor information, service IDs, and trace context
- Like UPI transactions — if a payment fails, tracing shows which bank
  (HDFC → SBI) had the issue
- Enables debugging across the entire MCP chain
- Industry trend: many companies are pivoting to tracing tools

## Update 6: Extensions, Tasks, and Apps (Platform Play)

MCP is moving from a protocol to a **platform** (like Android):

> "You don't use MCP — you use apps built on MCP."

### Naming Convention
- Extensions identified by **reverse domain name order** (like Android package
  names: `com.example.mcp.extension`)
- Conflict-free naming, no UID management needed
- Separate from MCP server code — independent repos, independent versioning

### Apps (Full Extensions)
- Interactive **HTML interfaces** that display in the agent
- Approval popups, selection dialogs, multi-step workflows
- Example: hotel booking app shows 3-4 options, user taps to select, next
  popup shows available rooms, user confirms → agent handles payment
- Use case: non-coding desktop app patterns within agent sessions

### Task Extensions (Long-Running Tasks)
- Was previously experimental, now a formal extension
- Stateless model: client sends request → gets a **task handle ID**
- Client polls on `/subscribe` with the ID to check status
- Use case: Excel processing, batch repository evaluation, any background job
- No full app UI needed — just poll/subscribe pattern

### Authorization & Security
- MCP now integrates with **OAuth 2.0** and **OpenID Connect**
- Standard login flows (Login with Google, GitHub, etc.)
- Application verification, client ID/secret registration
- Refresh tokens, scope accumulation (same as any web OAuth flow)
- Makes MCP accessible to non-technical users (Google login > token pasting)

### Deprecation Policy
Standardized process with timeline:
1. **Roots** → Moving from resource URIs to simple URLs
2. **Sampling** → Direct LLM provider API integration replaces it
3. **Login** → Still in progress, more clarity coming
4. **OpenTelemetry** — monitoring which functions execute, how long they take,
   CPU usage, database call timing — all via OpenTelemetry integration

## Release Timeline
- **Now**: Release candidate available for testing
- **July 28**: Final release
- **Breaking changes**: All existing MCP servers need updating

## The Platform Vision

MCP is evolving from a narrow protocol to an ecosystem:
- Rules, regulations, headers, caching — infrastructure-level concerns
- Apps, extensions, tasks — user-facing capabilities
- OAuth — accessible to non-technical users
- The speaker predicts an **MCP App Store** will emerge (similar to Android
  but for AI agent capabilities)
- Previous attempts (OpenAI GPT apps, plugins) weren't successful, but the
  need for connectors and apps is real

## Relevance to OCR

### MCP as OCR's External Connectivity Layer

OCR's ontology, GBrain, and tools should expose MCP interfaces. Every
component that an agent needs to interact with (ontology graph, governance
ledger, skill registry) should be MCP servers.

### Stateless Design

OCR's shipment pipeline is already stateless — each gate receives a complete
context slice and produces a complete output. The stateless MCP model confirms
this design: no session state between gates, full context in each shipment.

### Task Extensions = Long-Running Evaluations

OCR's eval pipeline (Phil Hetzel's eval flywheel) is a long-running task —
perfect for MCP task extension pattern. Submit a batch of evaluations, get a
task handle, poll for completion.

### Elicitation Pattern = Human-in-Loop Governance

MCP's server-to-client elicitation (question + state + request ID) maps to
OCR's governance HumanReview outcome. The governance gate sends a question
("Should this shipment proceed?"), includes the current state (shipment
context + positions + synthesis), and any reviewer can pick it up.

### Authorization = Keycloak Alignment

OCR uses Keycloak OSS for authentication. MCP's OAuth 2.0 / OpenID Connect
integration means OCR's MCP servers can use the same Keycloak instance for
auth — unified identity across the entire system.

### Extensions/Apps = OCR Skills Marketplace

MCP apps/extensions map to OCR's skills and perspective agents. The reverse
domain naming, independent repos, SemVer versioning — this is exactly how
OCR's skill registry should work. A "skill store" on top of MCP.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Stateless pipeline gates** | MCP stateless = each request complete, no session |
| **Standard protocols > custom** | MCP is becoming the standard — OCR should use it |
| **OAuth for auth** (Keycloak) | MCP aligns with OAuth 2.0 / OpenID Connect |
| **Human-in-loop governance** | Elicitation pattern = question + state + resume |
| **Long-running tasks as separate concern** | Task extensions = dedicated pattern for background work |
| **Distributed tracing** | W3C trace context for debugging OCR's pipeline |
| **Hot-reloadable extensions** (Mario/Pi) | MCP extensions in separate repos with SemVer |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **MCP as platform (not just protocol)** | MCP is becoming the Android of AI — OCR should build on it |
| **Elicitation pattern** | Formal pattern for agent-to-human and agent-to-agent questions mid-task |
| **Stateless + retry with state** | Any instance can pick up a paused task — enables fault tolerance |
| **App store prediction** | OCR should prepare for an ecosystem of MCP-based skills |
| **Deprecation policy** | OCR needs a formal deprecation process for its own APIs |
| **Caching with scope** | Per-user vs global cache for ontology lookups and tool results |
