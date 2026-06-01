# Skill Router v1 — Design & Rationale

## Step 1: What problem are we even solving?

OCR is a system that receives **signals** (a GitHub commit, a new Obsidian note, a strategy document) and needs to figure out what to do with them. The architecture doc (`agents.md`) calls each signal a **"shipment"** — an atomic piece of organizational work.

When a shipment arrives, the system needs to answer: **"Who should work on this?"**

You have 17 skills installed (pdf, pptx, claude-api, mcp-builder, etc.). Each one can do something different. How does the system decide which ones to wake up?

That's the **routing problem**.

---

## Step 2: What does agents.md say about routing?

The architecture doc gives us a formula:

```
ActivationScore(skill, shipment) =
    w1 * OntologyOverlap +
    w2 * TrajectoryRelevance +
    w3 * CouncilBalance +
    w4 * PriorContribution
```

This is the **specification** — it tells us *what* to compute but not *how*. Think of it like a recipe that says "combine flour, eggs, sugar" but doesn't tell you the oven temperature.

The formula has 4 ingredients:

1. **OntologyOverlap** — Does this skill understand the concepts in this shipment? If the shipment mentions "MCP server" and the skill is `mcp-builder`, that's a good match.

2. **TrajectoryRelevance** — Has the organization been working on related things recently? If the last 3 decisions were about LLM integration, skills that know about LLMs should get a boost.

3. **CouncilBalance** — Is this perspective already represented? If you already have 3 technical people on a council, you probably don't need a 4th — you need a customer advocate or a risk person instead. This prevents groupthink.

4. **PriorContribution** — Has this skill been useful on similar shipments before? Past performance is a signal.

---

## Step 3: Where does SKILL_MAPPING.md fit?

The current `SKILL_MAPPING.md` answers the question: **"Which OCR layer does this skill serve?"**

It's a lookup table:

```
mcp-builder      → Ingestion layer
claude-api       → Cognition Runtime
frontend-design  → Executive Surfaces
pdf              → Executive Surfaces
...
```

This is **useful documentation for a human** reading the codebase. But it's **not executable** — no computer program can read "mcp-builder → Ingestion" and turn it into a routing decision. A markdown file is passive data.

---

## Step 4: So what does skill_router.py add that the markdown can't?

Three things that only code can do:

### A) It reads the skills at runtime

```python
class SkillRegistry:
    def _load_all(self, root: Path):
        for skill_dir in sorted(root.iterdir()):
            skill_file = skill_dir / "SKILL.md"
            meta = self._parse_skill(skill_dir, skill_file)
```

Every skill has a `SKILL.md` file with frontmatter (name, description, trigger keywords). The router **reads these files automatically** — it discovers what skills exist without being told. If you add a new skill folder tomorrow, the router picks it up. No config changes needed.

The markdown file doesn't do this — you have to manually update it when skills change.

### B) It computes the ActivationScore formula

The formula in agents.md is mathematical notation:

```
ActivationScore(skill, shipment) = w1 * OntologyOverlap + ...
```

The Python file turns this into actual numbers:

```python
score = w1 * onto + w2 * traj + w3 * bal + w4 * pri
```

Each component is a **measurable function**:

- `_ontology_overlap`: Takes the skill's jurisdiction concepts and the shipment's entities, computes Jaccard similarity (intersection divided by union). If skill knows about {mcp, api} and shipment mentions {mcp, llm, document}, overlap = 1/4 = 0.25.

- `_trajectory_relevance`: Checks each step of recent decision history against the skill's concepts. Earlier steps (more recent) get higher weight due to `1/(i+1)` decay.

- `_council_balance`: If the skill's perspective is already seated, score = 0.2. If missing, score = 0.9.

- `_prior_contribution`: Looks up the skill's historical track record. No history? Default 0.3.

A markdown table can't compute `1/(i+1)` decay or Jaccard similarity.

### C) It produces a machine-readable decision

The output is a `Council` dataclass:

```python
@dataclass
class Council:
    shipment_id: str
    agents: List[Tuple[str, float]]     # "call mcp-builder with score 0.496"
    records: List[ActivationRecord]     # why? onto=0.50, traj=0.27, ...
```

This is **structured data** that another part of the system (the Council Orchestrator, the Chairman, the audit ledger) can consume. A markdown table produces human-readable text, not machine-consumable data.

---

## Step 5: Putting it all together — the data flow

```
                    ┌──────────────────┐
                    │  agents.md       │
                    │  "The spec"      │
                    │  ActivationScore │
                    │  formula +       │
                    │  architecture    │
                    └────────┬─────────┘
                             │ defines the contract
                             ▼
┌──────────────────┐    ┌──────────────────┐
│  SKILL_MAPPING.md│───▶│  skill_router.py │───▶ CouncilOrchestrator
│  "The map"       │    │  "The engine"    │      (parallel execution)
│  skill → layer   │    │                  │
│  human reference │    │  reads SKILL.md  │
└──────────────────┘    │  at runtime      │
                        │  computes scores │
                        │  returns Council │
                        └──────────────────┘
```

Each file has one job:

| File | Role | For whom |
|---|---|---|
| `agents.md` | Architectural specification | Humans building the system |
| `SKILL_MAPPING.md` | Human-readable index of what each skill does | Developers navigating the codebase |
| `skill_router.py` | Executable routing logic | The runtime (Python interpreter) |

You need all three. The spec tells you *what to build*. The map tells you *what exists*. The engine *makes decisions* at runtime.

---

## Step 6: Why not put everything in one place?

Two reasons:

1. **Markdown is for humans, code is for machines.** A formula like `len(intersection) / len(union)` is easy to write in Python but impossible to execute from a `.md` file. Conversely, a paragraph explaining *why* CouncilBalance prevents echo chambers is easy to read in markdown but meaningless to Python.

2. **The map changes at a different cadence than the engine.** `SKILL_MAPPING.md` changes every time you add or reclassify a skill (maybe weekly). The routing algorithm (`ActivationScore`) changes when you discover a better way to route (maybe monthly or yearly). Keeping them separate means you can add a skill without touching the routing code, and improve the routing algorithm without rebuilding the skill index.

---

## Step 7: What happens next?

The router returns a council — a ranked list of skills to activate. But that's just **Phase 1**. The architecture says Phase 2 is **dispatch**: running those skills in parallel threads with isolated context slices.

Currently the router doesn't implement dispatch yet. The `Council` dataclass has an empty `synthesis` field waiting for the Chairman's output. These are the natural next pieces: a thread-pool executor that runs the selected skills, and a synthesis function that collects their positions and produces a verdict.

The router is a skeleton of the full cognition runtime — it does the routing piece correctly, but the execution and synthesis pieces still need building. The next step would be implementing `run_council(council)` — the parallel dispatch — and `synthesize(council)` — the chairman.
