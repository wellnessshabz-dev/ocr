# ADR-0005: Governance Before Autonomy

## Status

Accepted

## Context

Autonomous cognitive systems risk runaway decisions — contradictory commitments, unaccountable actions, irreversible consequences. The architecture defines four governance rules (no orphan decisions, human override always wins, append-only audit, explainability before commitment) but does not enforce an implementation order.

## Decision

Governance is implemented BEFORE autonomous council execution. Specifically:

1. All council syntheses go through governance validation before commit
2. Human review is required for any shipment exceeding configurable risk thresholds
3. The audit ledger is append-only from day one
4. Every committed decision has a complete, human-readable lineage

The governance layer is not deferred to "Enterprise Grade" (Phase 2). It is built in Phase 1.

## Consequences

- Slower initial throughput (governance gates every commit)
- No unaccountable decisions in the ledger
- Governance rules can be relaxed later but never added retroactively
- Builds organizational trust in the system from the start

## Supersedes

None.
