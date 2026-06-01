# ADR-0003: Ontology Lifecycle Governance

## Status

Accepted

## Context

Without governance, the ontology accumulates noise — duplicate concepts, contradictory relationships, stale nodes. The architecture doc specifies a promotion pipeline (candidate → confirmed → archived) but does not define who governs it.

## Decision

The ontology follows a governed lifecycle with explicit states:

```
Signal arrives → Candidate Node (3+ references to promote)
                                → Discarded (0 references, 30 days)
             → Confirmed Node (1+ reference to maintain)
                                → Dormant (low use, 90 days)
             → Archived Node (never deleted, always queryable)
```

Promotion and archival require a council decision. A single signal cannot self-promote.

## Consequences

- Ontology quality is maintained without manual curation
- Council deliberation cost for every promotion (acceptable for quality)
- Historical queries still resolve archived nodes
- Requires a scheduled ontology maintenance council

## Supersedes

None.
