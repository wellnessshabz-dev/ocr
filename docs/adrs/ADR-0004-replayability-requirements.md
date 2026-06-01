# ADR-0004: Replayability Requirements

## Status

Accepted

## Context

Replayability is OCR's institutional learning mechanism. Every cognitive event must be re-executable from any point in the past. This requires preserving context windows, skill inputs, council positions, and synthesis versions.

## Decision

Every shipment lifecycle stores:

1. **Shipment snapshot** — frozen input at time of compilation
2. **Context window snapshot** — the GBrain memory context provided to each skill
3. **Council position snapshots** — each skill's raw output per round
4. **Chairman synthesis versions** — v1, v2, ..., vN
5. **Governance decision** — validated / human_review / rejected with rationale

Replay sessions are stored in the `replay_sessions` table with a diff against the original run.

## Consequences

- Storage grows linearly with shipments (predictable, not exponential)
- Counterfactual analysis becomes possible ("what if I used a different council?")
- Debugging is a first-class operation
- Audit trail is complete by construction

## Supersedes

None.
