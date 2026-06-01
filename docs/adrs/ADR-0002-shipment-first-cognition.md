# ADR-0002: Shipment-First Cognition

## Status

Accepted

## Context

OCR needs a universal primitive for organizational work. Prompts, tasks, and chat messages are ephemeral and unauditable. Every cognitive action must be traceable, replayable, and governable.

## Decision

All work enters the system as a **Shipment** — an atomic unit of organizational cognition with:

- Unique ID (`shipment_id`)
- Source and type provenance (`source_type`, `source_ref`)
- Ontology anchors (`ontology_refs`)
- Trajectory binding (`trajectory_id`)
- Lifecycle status (`pending → compiling → deliberating → committed → surfaced`)

No cognitive operation occurs outside a shipment context.

## Consequences

- Every decision is traceable to its originating signal
- Replay is a first-class operation (re-execute a shipment)
- Governance can inspect, halt, or escalate individual shipments
- Additional overhead to wrap all input into shipment envelopes

## Supersedes

None.
