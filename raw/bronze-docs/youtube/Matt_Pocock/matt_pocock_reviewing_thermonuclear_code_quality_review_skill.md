---
title: "Reviewing the Thermonuclear Code Quality Review Skill (Matt Pocock)"
source_type: "youtube"
channel: "Matt Pocock"
speaker: "Matt Pocock"
date: "2026-05"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Matt Pocock's personal YouTube channel. He reviews the Cursor team's 'Thermonuclear Code Quality Review' skill, tests it on 5 real PRs, and evaluates what makes a good agent code review prompt."
tags: ["code-review", "thermonuclear", "ambitious-review", "code-judo", "file-size", "agent-navigation", "governance", "testing", "false-positives"]
---

# Reviewing the Thermonuclear Code Quality Review Skill (Matt Pocock)

Source: Matt Pocock's personal channel. He reviews the Cursor team's
"Thermonuclear Code Quality Review" skill and evaluates its effectiveness
on 5 real PRs to his Sandcastle project.

## The Cursor Skill: Thermonuclear Code Quality Review

A single `skill.md` file designed for unusually strict code review focused on
implementation quality, maintainability, abstraction quality, and codebase
health. The hallmark: **ambition** — the reviewer is told to look for "code
judo moves" throughout the codebase, not just within the diff.

### Key Rules

| Rule | Purpose |
|------|---------|
| **Be ambitious about structural simplification** | Don't treat the diff as bounds — look across the whole codebase |
| **Don't push files past 1000 lines** | Large files are hard for agents to navigate (context window cost) |
| **No random spaghetti growth** | If statements in random places = design problem, not style nit |
| **Bias towards cleaning design** | Don't accept working code if the structure is poor |
| **Prefer direct, boring, maintainable code** | Over hacky/magical code |
| **Question unnecessary optionality** | Always-required props added as optional is a pattern LLMs default to |
| **Keep logic in canonical layer** | Reuse existing helpers, avoid bespoke one-offs |
| **Unnecessary sequential orchestration = design smell** | Parallelize independent work |
| **Code judo** | Can you reframe to delete whole categories of complexity? |
| **Split large files into smaller modules** | File names as context pointers are more efficient |
| **Escalate findings** | When a cleaner reframing could delete complexity |

### Review Prioritization (Findings Order)

1. Structural code quality regressions (top priority)
2. Legibility and maintainability concerns (lower)
3. Approval/rejection of the PR based on conditions

### Review Tone

"Be direct, serious, and demanding about quality. Do not be rude."

## Matt's Critique

### What's Good

- **Ambition works**: The review found 5/7 valid issues across 5 PRs,
  including real file size problems, duplication, swallowed errors, and
  half-finished refactoring
- **Code judo framing**: Pushing the reviewer to think about deleting
  complexity rather than polishing it is powerful
- **Prioritization**: Ordering findings by severity prevents flooding with
  low-value nits
- **Results were useful**: "The codebase is meaningfully messier than it was
  a week ago" — an honest assessment

### What's Missing

1. **No mention of testing or seams** — "the entire point of having a good
   codebase is improving feedback loops." Tests are where design meets reality.
2. **Too much duplication** — The skill repeats itself multiple times. A
   shorter, more DRY version would be more effective.
3. **Word salad** — "Treat unnecessary sequential orchestration and non-atomic
   updates as design smells" — this is hard for the agent to parse.
4. **False positives** — 2/7 findings were wrong (one based on inaccurate
   understanding, one disagreed with the design intent). Acceptable tradeoff.

### Matt's Verdict

> "Getting the review to be super ambitious and getting it to push a lot of
> different options will give you more false positives, but those false
> positives are pretty easy just to say no to. It's the ones that you miss,
> that you never know about, the opportunity for improvement that you never
> see — those are the dangerous ones."

Worth pulling down and experimenting with, but needs cleanup:
- Remove duplication
- Add testing focus
- Sharpen the language (replace word salad with direct instructions)

## Key Insight: Large Files as Agent Tax

The 1000-line rule isn't about readability for humans — it's about agent
**context efficiency**. Agents need to ingest the entire file into context to
find what they need. File names act as context pointers — a well-named file
tells the agent whether to open it without scanning the contents.

This implies:
- **File structure is context management** — not just code organization
- **Splitting files is a performance optimization for agents**
- **Agents navigate by file name, not by reading everything**

## Relevance to OCR

### Code Review = Governance Verification

OCR's governance layer is a code review for organizational decisions. The
Thermonuclear skill provides a template for what governance should check:

| Review Skill | OCR Governance |
|--------------|----------------|
| Diff bounds vs codebase-wide | Governance should check systemic effects, not just the shipment |
| Structural regressions | Ontology contradictions, decision conflicts |
| Code judo (delete complexity) | Governance should ask: can this be simpler? |
| Prioritize findings | Governance should surface critical issues first |
| Approve/reject | Governance outcome: Validated / HumanReview / Rejected |

### The Ambition Rule

OCR's governance should be ambitious — not just checking that the decision
was valid, but looking for opportunities to improve the ontology, the council
composition, or the decision itself. **The cost of a false positive
(HumanReview escalation) is lower than a missed systemic regression.**

### File Size as Agent Performance

OCR's ontology graph and context slices should follow the same principle:
small, well-named, navigable units. A context slice that's too large (over
1000 lines or equivalent) is expensive for agents to process. Split ontology
nodes instead of letting them grow.

### Testing/Seams Gap

Matt's strongest criticism: no testing focus. OCR's governance should include
evaluation of test quality, not just code quality. If a shipment touches code,
did the tests change? Are the seams testable?

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **False positives < missed regressions** | "Dangerous ones are the ones you never see" |
| **Governance should be ambitious** | Code judo thinking applies to organizational decisions |
| **Small files for agent performance** | File names as context pointers = efficient agent navigation |
| **Deterministic guardrails** (Daniel/Tejas) | Code review is a deterministic gate before merge |
| **Prioritization in governance** | Findings must be ordered by severity |
| **Eval pipeline** (Phil Hetzel) | Code review findings = eval data for improvement |
| **Don't outsource understanding** | Human must say no to false positives — can't delegate taste |

### What Matt Adds

| Insight | OCR Application |
|---------|-----------------|
| **Ambitious review > bounded review** | Governance should look beyond the shipment's edges |
| **Code judo as review framing** | Governance question: does this delete or add complexity? |
| **File size = agent context cost** | Ontology nodes should be small and focused |
| **False positives are acceptable** | Don't optimize governance for zero false positives |
| **Testing is missing from most review prompts** | OCR governance must evaluate test quality |
| **Skill needs to be DRY** | Governance rules should be non-duplicative and prioritized |
