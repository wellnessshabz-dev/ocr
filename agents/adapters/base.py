"""Agent-agnostic interface for all reasoning backends.

Every AI model provider (Claude, Codex, Kimi, etc.) implements
this interface. The runtime never calls a provider API directly.
"""

from dataclasses import dataclass, field
from typing import Optional
from abc import ABC, abstractmethod
from uuid import UUID, uuid4


@dataclass
class Reasoning:
    content: str
    confidence: float
    evidence_refs: list[str] = field(default_factory=list)
    model: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass
class Shipment:
    shipment_id: UUID = field(default_factory=uuid4)
    source_type: str = ""
    source_ref: str = ""
    payload: dict = field(default_factory=dict)


@dataclass
class Replay:
    replay_id: UUID = field(default_factory=uuid4)
    shipment_id: UUID = field(default_factory=uuid4)
    replay_diff: Optional[dict] = None


@dataclass
class Trace:
    trace_id: UUID = field(default_factory=uuid4)
    component: str = ""
    operation: str = ""
    duration_ms: int = 0
    metadata: dict = field(default_factory=dict)


class AgentAdapter(ABC):

    @abstractmethod
    async def ingest_context(self, context: dict) -> None:
        ...

    @abstractmethod
    async def produce_reasoning(self, prompt: str) -> Reasoning:
        ...

    @abstractmethod
    async def emit_shipment(self, shipment: Shipment) -> None:
        ...

    @abstractmethod
    async def request_replay(self, replay_id: str) -> Replay:
        ...

    @abstractmethod
    async def emit_trace(self, trace: Trace) -> None:
        ...
