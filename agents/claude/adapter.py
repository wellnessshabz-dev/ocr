"""Claude adapter implementation."""

from agents.adapters.base import AgentAdapter, Reasoning, Shipment, Replay, Trace


class ClaudeAdapter(AgentAdapter):

    async def ingest_context(self, context: dict) -> None:
        pass

    async def produce_reasoning(self, prompt: str) -> Reasoning:
        return Reasoning(content="", confidence=0.0)

    async def emit_shipment(self, shipment: Shipment) -> None:
        pass

    async def request_replay(self, replay_id: str) -> Replay:
        return Replay()

    async def emit_trace(self, trace: Trace) -> None:
        pass
