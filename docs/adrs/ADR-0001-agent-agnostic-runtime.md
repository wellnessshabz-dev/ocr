# ADR-0001: Agent-Agnostic Runtime

## Status

Accepted

## Context

OCR must not depend on any single AI model or provider. The cognition runtime — shipments, councils, memory, ontology, replay — must survive provider changes, model deprecations, and shifts in the AI landscape.

## Decision

All reasoning agents implement a standard `AgentAdapter` interface:

```python
class AgentAdapter:
    def ingest_context(self, context: dict) -> None
    def produce_reasoning(self, prompt: str) -> Reasoning
    def emit_shipment(self, shipment: Shipment) -> None
    def request_replay(self, replay_id: str) -> Replay
    def emit_trace(self, trace: Trace) -> None
```

The runtime never calls a provider API directly. All provider interactions go through the adapter layer.

## Consequences

- New models can be swapped in without runtime changes
- Adapters can add provider-specific optimizations (prompt caching, batching)
- Testing can use a `NullAdapter` without any external dependency
- Slight indirection cost per call (negligible vs. LLM latency)

## Supersedes

None.
