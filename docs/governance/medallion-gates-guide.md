# Medallion Gates Guide

What governance gates are, why they matter, and how OCR's Bronze→Silver→Gold architecture implements them.

---

## What's a Governance Gate?

A governance gate is a **checkpoint that runs BEFORE something happens**. It asks "should we?" before "can we?" — and enforces the answer deterministically (code, not prompts).

**Without a gate:**

```
Agent wants to send email → Model says okay → 150K emails sent → Oops
```

**With a gate:**

```
Agent wants to send email → Gate checks policy → DENY (over daily limit) → Blocked
```

The gate doesn't ask the model nicely. The gate **blocks in code** before the model's intent reaches the wire. This matters because prompt injection has a **100% attack success rate** on GPT-4o, Claude 3, and Llama-3 (ICLR 2025). Asking a model to "follow the rules" is a polite request to a stochastic system.

> **"Actions the gate denies are not 'unlikely.' They are structurally impossible."**
> — Microsoft Agent Governance Toolkit docs

---

## The Market: Who's Paying and Why

Companies pay **$1,000–$25,000/month** for governance gates because:

| Problem | Cost of ignoring |
|---------|-----------------|
| Agent sends 150K emails | Reputation + deliverability blacklist |
| Agent drops a production table | Data loss + recovery cost |
| Agent leaks PII in output | GDPR fine up to €20M |
| EU AI Act violation | Fine up to €35M or 7% of global revenue |
| Shadow agents (unknown AI running) | No inventory = no control |

**Competitors solving this:**

| Product | Price | What they do |
|---------|-------|-------------|
| **Rends** | $1,500–$25,000/mo | Runtime interception, kill switch, 37 compliance frameworks, shadow agent detection. Installs as SDK in 5 min. |
| **Sekuire** | $1,000–$5,000/mo | Policy-as-code (YAML), offline-first enforcement, Ed25519 signed audit trail, kill switch. |
| **Microsoft AGT** | Free (MIT) | 3,500+ GitHub stars, 100 contributors, 10/10 OWASP, 7 language SDKs, sandboxing, 992 conformance tests. Ships to Copilot CLI, Claude Code, OpenCode. |

These all solve the same problem: **"agent does something bad at runtime."**

---

## What OCR Does Differently

OCR's gates solve a **different problem**: **"organization believes something wrong."**

| Gate type | Prevents | Example |
|-----------|----------|---------|
| **Runtime gate** (Rends/Sekuire) | Agent calling a tool it shouldn't | Claude Code pushing to prod without approval |
| **OCR Gate 1** (Bronze→Silver) | Garbage data entering your thinking | PII in a scraped article, hallucinated stats |
| **OCR Gate 2** (Silver→Gold) | Bad decisions reaching humans | Council synthesis contradicts past decision, unsupported claims slip through |

Same architectural pattern — **pre-execution enforcement** — but applied to data/decisions instead of tool calls.

Rends blocks bad agent actions. OCR blocks bad organizational beliefs. They're complementary:

```
┌─────────────────────────────────────────────────────┐
│                  YOUR ORGANIZATION                   │
│                                                      │
│  Agents (Claude Code, GPT, etc.)                     │
│       │                                              │
│       ▼                                              │
│  RENDS GATE ─── blocks bad tool calls                │
│       │                                              │
│       ▼                                              │
│  OCR GATE 1 ─── blocks bad data from entering        │
│       │                                              │
│       ▼                                              │
│  COUNCILS ─── deliberate, synthesize                 │
│       │                                              │
│       ▼                                              │
│  OCR GATE 2 ─── blocks bad decisions from surfacing  │
│       │                                              │
│       ▼                                              │
│  HUMANS ─── act on trusted decisions                 │
└─────────────────────────────────────────────────────┘
```

---

## OCR's Bronze → Silver → Gold

### Layer 1: Bronze (the trash bin)

Everything lands here raw. Append-only, never edited, never trusted.

**Currently working:** Web scraper (Firecrawl + Playwright) dumps scrapes here.

**Example item:**

```
Title: "GPT-5 Launch"
URL: https://example.com/gpt5
Raw content: "GPT-5 costs $0.01/token... Sam Altman's email is sam@... +1-555-0199"
```

PII (email, phone) mixed in with content. Not yet trusted.

### Gate 1: Bronze → Silver (the janitor)

A deterministic code check runs before anything leaves Bronze. Built in `shipments/compiler/` + `shipments/validator/`.

**What it checks:**

- Strip PII (emails, phones, credit cards)
- Validate schema (title, date, source, content all present?)
- Reject malformed input (empty body, error page, binary garbage)
- Resolve entities against ontology (is "GPT-5" a known concept?)
- Log structured errors on rejection

**Example flow:**

```
Raw scrape arrives
  → PII scanner runs: found "sam@..." and "+1-555-0199" → stripped
  → Schema check: title ✓, date ✓, source ✓, body ✓ → pass
  → Entity resolution: "GPT-5" → matched ontology node "frontier-model"
  → Emit clean shipment to Silver
```

**If it fails:**

```
Raw scrape arrives
  → Body is empty (scraper hit a 404)
  → Rejected. Error logged to ledger.
  → Never reaches Silver.
```

### Layer 2: Silver (the think tank)

Cleaned shipments go through cognition. Councils deliberate, chairman synthesizes, ontology extracts, GBrain stores.

**Not yet built.** This is the cognition runtime — the core differentiator.

### Gate 2: Silver → Gold (the auditor)

Before any decision reaches humans, another deterministic check runs. Built in `cognition/governance/`.

**What it checks:**

- Verify evidence (does the cited source actually say that?)
- Check contradictions (did a past decision say something opposite?)
- Confirm all required perspectives were represented (strategic, technical, risk)
- Validate confidence threshold (score >= 0.7)
- Escalate to human if risk threshold exceeded
- Three consecutive failures → permanent human escalation

**Example flow:**

```
Council synthesis arrives
  → Evidence check: cited "10x cheaper" but source says "2x cheaper" → FAIL
  → Contradiction check: past decision said "GPT-5 not a threat" → CONTRADICTION
  → Rejected. Sent back to Silver for rework.
  → Second attempt passes all checks → promoted to Gold.
```

### Layer 3: Gold (the dashboard)

Only verified, governed decisions reach here. Executive surfaces, strategic questions, podcast, cognition log. This is the trusted output that people act on.

**Currently:** Static HTML dashboard (placeholder).

---

## What We Can Build NOW

We have a working scraper (Bronze). We can build **Gate 1** in ~2 weeks.

### Gate 1 MVP — Scraper Output Validator

```python
# Pseudocode for Gate 1
class BronzeToSilverGate:
    def process(self, raw: RawContent) -> Shipment | Rejection:
        # 1. Strip PII
        cleaned = pii_stripper.strip(raw.content)
        
        # 2. Validate schema
        if not self.validate_schema(cleaned):
            return Rejection("missing required fields")
        
        # 3. Check content quality
        if len(cleaned.body) < 50:
            return Rejection("content too short (likely error page)")
        
        # 4. Resolve entities
        entities = self.ontology.resolve(cleaned)
        
        # 5. Emit shipment
        return Shipment(
            source=raw.url,
            content=cleaned,
            entities=entities,
            timestamp=now()
        )
```

This is valuable on its own. Teams that scrape lots of web content need:
- PII stripped before content enters their RAG pipeline
- Malformed content rejected before it pollutes vector stores
- Entities extracted and linked to known concepts

**The pitch:** "Feed us URLs. We return clean, schema-validated, entity-resolved shipments — never garbage, never PII, always auditable."

---

## What We SHOULDN'T Build

**Do not build a Rends/Sekuire competitor.**

The runtime agent governance market is crowded, well-funded, and led by Microsoft (free, 3.5K stars, production-grade). OCR cannot win there.

**What OCR should build:**

1. **Gate 1 (Bronze→Silver)** — Content validation for AI pipelines. Shippable in weeks, taps real pain (dirty data in → garbage out).
2. **Gate 2 (Silver→Gold)** — Decision validation for organizational cognition. The core differentiator. Longer build but defensible.
3. **The full cognition runtime** — Councils, ontology, GBrain. Only after gates are proven.

### The Revenue Path

| Phase | Product | Price signal | Timeline |
|-------|---------|-------------|----------|
| 1 | Gate 1 as standalone API | $500–$1,000/mo for clean web content pipeline | 2–3 weeks |
| 2 | Gate 1 + basic shipment API | $1,000–$2,500/mo for structured, auditable content | 6–8 weeks |
| 3 | Gate 2 + councils | $5,000–$15,000/mo for organizational decision quality | 4–6 months |
| 4 | Full OCR (GBrain + ontology + surfaces) | Enterprise custom | 8–12 months |

---

## Key Documents

- [ADR-0006: Medallion Gates Before Agents](../adrs/ADR-0006-medallion-gates-before-agents.md) — The architectural decision
- [ADR-0005: Governance Before Autonomy](../adrs/ADR-0005-governance-before-autonomy.md) — Governance philosophy
- [Scraper Router](../../ingestion/web/scraper.py) — The working Bronze ingestion
- [YouTube Silver Synthesis](../../raw/bronze-docs/youtube/_silver_synthesis.md) — Third-party validation of gates-over-agents thesis

---

## References

- [Rends.ai](https://rends.ai) — Runtime agent governance, $1,500–$25,000/mo
- [Sekuire.ai](https://sekuire.ai) — Policy-as-code governance, $1,000–$5,000/mo
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) — Open source (MIT), 3,500★, 100 contributors
- [Cordum: Pre-Dispatch Governance](https://cordum.io/blog/pre-dispatch-governance-ai-agents) — Technical deep dive on agent governance architecture
- [OAP: Open Agent Passport](https://arxiv.org/pdf/2603.20953) — Academic paper on pre-action authorization (53ms median, 0% bypass rate)
- [GitHub Agentic Workflows Security](https://github.blog/ai-and-ml/generative-ai/under-the-hood-security-architecture-of-github-agentic-workflows/) — GitHub's security architecture for agents in CI/CD
- [CAIS: Controlled Agentic AI Systems](https://www.mdpi.com/2504-4990/8/5/125) — Academic paper formalizing governance as a deterministic projection operator
