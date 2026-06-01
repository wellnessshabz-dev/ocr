"""
skill_router.py — OCR Skill Activation Engine

Implements the ActivationScore formula from agents.md:
    ActivationScore(skill, shipment) =
        w1 * OntologyOverlap(skill.jurisdiction, shipment.entities) +
        w2 * TrajectoryRelevance(skill.history, shipment.trajectory) +
        w3 * CouncilBalance(current_council, skill.perspective) +
        w4 * PriorContribution(skill.id, similar_shipments)

Two routing levels:
    1. Council activation: which perspective agents sit on the council
    2. Skill binding: which implementation skills each agent may invoke

Usage:
    router = SkillRouter(skills_dir="raw/skills")
    council = router.activate(shipment)
    # council.agents -> ranked list of (agent, score)
    # council.synthesis -> chairman's summary (once implemented)
"""

from __future__ import annotations

import re
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class SkillMetadata:
    """Parsed from SKILL.md frontmatter + SKILL_MAPPING.md overlay."""
    id: str
    name: str
    description: str
    ocr_layer: str                 # Ingestion | Compiler | Cognition | GBrain | Surfaces | Governance
    jurisdiction: List[str]        # ontology concepts this skill covers
    perspective: Optional[str]     # council role if this is a perspective agent
    priority: int = 0              # dispatch priority (higher = earlier)


@dataclass
class Shipment:
    """Atomic organizational action — the unit of cognition work."""
    shipment_id: str
    type: str                      # architectural | knowledge | feature | governance
    entities: List[str]            # ontology nodes touched
    trajectory: List[str]          # recent decision steps / context
    urgency: float = 1.0           # multiplier (0..2)


@dataclass
class ActivationRecord:
    skill_id: str
    score: float
    components: Dict[str, float]   # breakdown for audit / explainability


@dataclass
class Council:
    """Result of activation — the set of agents that will deliberate."""
    shipment_id: str
    agents: List[Tuple[str, float]]    # (skill_id, activation_score)
    records: List[ActivationRecord]    # full audit trail
    synthesis: Optional[str] = None    # chairman's output


# ---------------------------------------------------------------------------
# Skill registry loader
# ---------------------------------------------------------------------------

class SkillRegistry:
    """Scans a skills directory and builds an index of available skills.

    Sources:
        - SKILL.md frontmatter (name, description, triggers)
        - SKILL_MAPPING.md (ocr_layer, use_case overlay)
        - Directory convention: each subdirectory is a skill
    """

    def __init__(self, skills_dir: str):
        self._skills: Dict[str, SkillMetadata] = {}
        self._load_all(Path(skills_dir))

    def _load_all(self, root: Path) -> None:
        for skill_dir in sorted(root.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                continue
            meta = self._parse_skill(skill_dir, skill_file)
            if meta:
                self._skills[meta.id] = meta

    def _parse_skill(self, path: Path, skill_file: Path) -> Optional[SkillMetadata]:
        text = skill_file.read_text()
        sid = path.name

        name = sid
        description = ""
        perspective = None

        frontmatter = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if frontmatter:
            block = frontmatter.group(1)
            name = self._extract_yaml_field(block, "name") or sid
            description = self._extract_yaml_field(block, "description") or ""

        jurisdiction = self._infer_jurisdiction(name, description)
        ocr_layer = self._infer_layer(name, description, jurisdiction)

        return SkillMetadata(
            id=sid,
            name=name,
            description=description[:200],
            ocr_layer=ocr_layer,
            jurisdiction=jurisdiction,
            perspective=perspective,
        )

    @staticmethod
    def _extract_yaml_field(block: str, field: str) -> Optional[str]:
        m = re.search(rf"^{field}:\s*[\"']?(.+?)[\"']?\s*$", block, re.MULTILINE)
        if m:
            return m.group(1).strip()
        return None

    @staticmethod
    def _infer_jurisdiction(name: str, desc: str) -> List[str]:
        """Map skill to ontology concepts based on name + description keywords."""
        text = f"{name} {desc}".lower()
        concepts = []
        mappings = {
            "dashboard": "executive_dashboard",
            "ui": "user_interface",
            "frontend": "user_interface",
            "mcp": "mcp_server",
            "api": "api",
            "claude": "llm",
            "llm": "llm",
            "pdf": "document",
            "docx": "document",
            "pptx": "presentation",
            "xlsx": "spreadsheet",
            "slide": "presentation",
            "gif": "notification",
            "slack": "notification",
            "brand": "brand_identity",
            "theme": "brand_identity",
            "design": "visual_design",
            "canvas": "visual_design",
            "art": "visual_design",
            "algorithmic": "visual_design",
            "skill": "skill_management",
            "test": "testing",
            "playwright": "testing",
            "webapp": "testing",
            "internal": "communication",
            "comms": "communication",
            "coauthor": "document",
            "ontology": "ontology",
            "extract": "ontology",
        }
        for keyword, concept in mappings.items():
            if keyword in text:
                concepts.append(concept)
        return list(set(concepts)) if concepts else ["general"]

    @staticmethod
    def _infer_layer(name: str, desc: str, jurisdiction: List[str]) -> str:
        text = f"{name} {desc}".lower()
        if any(w in text for w in ["mcp", "ingest", "github", "obsidian", "wiki"]):
            return "Ingestion"
        if any(w in text for w in ["ontology", "extract", "valid", "shipment", "compile"]):
            return "Compiler"
        if any(w in text for w in ["skill", "council", "perspective", "agent", "claude", "llm"]):
            return "Cognition"
        if any(w in text for w in ["memory", "brain", "graph", "neo4j", "trajectory"]):
            return "GBrain"
        if any(w in text for w in ["dashboard", "frontend", "ui", "podcast", "report"]):
            return "Surfaces"
        if any(w in text for w in ["audit", "govern", "policy", "lineage"]):
            return "Governance"
        return "Surfaces"  # default

    def get(self, skill_id: str) -> Optional[SkillMetadata]:
        return self._skills.get(skill_id)

    def all(self) -> List[SkillMetadata]:
        return list(self._skills.values())

    def by_layer(self, layer: str) -> List[SkillMetadata]:
        return [s for s in self._skills.values() if s.ocr_layer == layer]

    def __len__(self) -> int:
        return len(self._skills)


# ---------------------------------------------------------------------------
# Activation engine
# ---------------------------------------------------------------------------

class ActivationEngine:
    """Computes ActivationScore with the 4-component formula from agents.md.

    Weights are intentionally configurable. The defaults reflect:
        - OntologyOverlap is the strongest signal (domain fit)
        - TrajectoryRelevance and CouncilBalance are secondary
        - PriorContribution is a long-term tuning signal

    Each component is normalized to [0, 1] before weighting.
    """

    def __init__(self, registry: SkillRegistry):
        self._registry = registry

    # Default weights — should be tuned via GBrain reinforcement
    W1_ONTOLOGY = 0.35
    W2_TRAJECTORY = 0.25
    W3_COUNCIL_BALANCE = 0.25
    W4_PRIOR = 0.15

    def activate(
        self,
        shipment: Shipment,
        current_council: Optional[List[str]] = None,
        prior_history: Optional[Dict[str, float]] = None,
        weights: Optional[Dict[str, float]] = None,
    ) -> Council:
        """Run activation for a shipment against the full skill registry.

        Args:
            shipment: The incoming organizational action.
            current_council: Skill IDs already on the council (for balance boost).
            prior_history: Map of skill_id -> historical contribution score.
            weights: Override the default W1-W4 weights.

        Returns:
            Council with ranked agents and full audit records.
        """
        w = weights or {}
        w1 = w.get("ontology", self.W1_ONTOLOGY)
        w2 = w.get("trajectory", self.W2_TRAJECTORY)
        w3 = w.get("council_balance", self.W3_COUNCIL_BALANCE)
        w4 = w.get("prior", self.W4_PRIOR)

        results: List[ActivationRecord] = []

        for skill in self._registry.all():
            onto = self._ontology_overlap(skill, shipment)
            traj = self._trajectory_relevance(skill, shipment)
            bal = self._council_balance(skill, current_council or [])
            pri = self._prior_contribution(skill.id, prior_history or {})

            score = w1 * onto + w2 * traj + w3 * bal + w4 * pri
            score *= shipment.urgency

            results.append(ActivationRecord(
                skill_id=skill.id,
                score=round(score, 4),
                components={"ontology": onto, "trajectory": traj,
                            "balance": bal, "prior": pri},
            ))

        results.sort(key=lambda r: r.score, reverse=True)

        top_k = results[:5]  # council size is configurable

        return Council(
            shipment_id=shipment.shipment_id,
            agents=[(r.skill_id, r.score) for r in top_k],
            records=results,
        )

    # ------------------------------------------------------------------
    # Component scorers
    # ------------------------------------------------------------------

    def _ontology_overlap(self, skill: SkillMetadata, shipment: Shipment) -> float:
        """OntologyOverlap: Jaccard similarity between skill jurisdiction
        and shipment entities. If neither has entities, returns 0.5 (neutral).

        agents.md: "ensures domain relevance"
        """
        if not skill.jurisdiction or not shipment.entities:
            return 0.5
        s_set = set(skill.jurisdiction)
        e_set = set(shipment.entities)
        if not s_set and not e_set:
            return 0.5
        intersection = s_set & e_set
        union = s_set | e_set
        return len(intersection) / len(union)

    def _trajectory_relevance(self, skill: SkillMetadata, shipment: Shipment) -> float:
        """TrajectoryRelevance: How many of the skill's jurisdiction concepts
        appear in the shipment's trajectory (recent decision context).

        agents.md: "ensures historical context"

        Decay: concepts matched earlier in the trajectory list are weighted
        more heavily (recency).
        """
        if not skill.jurisdiction or not shipment.trajectory:
            return 0.3
        s_concepts = set(skill.jurisdiction)
        total = 0.0
        for i, step in enumerate(shipment.trajectory):
            step_lower = step.lower()
            matches = sum(1 for c in s_concepts if c.replace("_", " ") in step_lower)
            if matches:
                recency_weight = 1.0 / (i + 1)  # earlier steps (more recent) weigh more
                total += matches * recency_weight
        max_possible = sum(1.0 / (i + 1) for i in range(len(shipment.trajectory)))
        return min(total / max_possible, 1.0) if max_possible > 0 else 0.3

    def _council_balance(self, skill: SkillMetadata, current: List[str]) -> float:
        """CouncilBalance: Boost skills whose perspective is missing
        from the current council.

        agents.md: "prevents echo chambers by boosting missing perspectives"

        If the skill has no assigned perspective, it gets a neutral score.
        If it has a perspective already present on the council, it gets a
        small penalty to encourage diversity.
        """
        if not skill.perspective:
            return 0.5
        already_seated = any(
            skill.perspective == self._registry.get(sid).perspective
            for sid in current
            if self._registry.get(sid)
        )
        return 0.2 if already_seated else 0.9

    @staticmethod
    def _prior_contribution(skill_id: str, history: Dict[str, float]) -> float:
        """PriorContribution: Normalized historical contribution score.

        agents.md: "rewards skills with relevant past input"

        If no history exists, returns a default 0.3 to avoid cold-start
        exclusion while still favoring proven skills.
        """
        if not history:
            return 0.3
        return history.get(skill_id, 0.3)


# ---------------------------------------------------------------------------
# Skill Router (public API)
# ---------------------------------------------------------------------------

class SkillRouter:
    """Top-level router that connects shipments to skills.

    Two-phase flow:
        1. Activate:    compute ActivationScore for each skill, select council
        2. Dispatch:    run selected skills in parallel (thread pool)

    The router is stateless by design — state lives in GBrain. This keeps
    routing deterministic and replayable for audit.
    """

    def __init__(self, skills_dir: str = "raw/skills"):
        self._registry = SkillRegistry(skills_dir)
        self._engine = ActivationEngine(self._registry)

    @property
    def registry(self) -> SkillRegistry:
        return self._registry

    def activate(self, shipment: Shipment, **kwargs) -> Council:
        """Phase 1: Score all skills and return a ranked council."""
        return self._engine.activate(shipment, **kwargs)

    def route(self, shipment: Shipment, **kwargs) -> Council:
        """Alias for activate — clearer name in calling code."""
        return self.activate(shipment, **kwargs)

    def skills_for_layer(self, layer: str) -> List[SkillMetadata]:
        """Query: which skills serve a given OCR layer?"""
        return self._registry.by_layer(layer)


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    router = SkillRouter(skills_dir=Path(__file__).parent.as_posix())

    print(f"Loaded {len(router.registry)} skills\n")

    test_shipment = Shipment(
        shipment_id="test-001",
        type="architectural",
        entities=["mcp_server", "api", "llm", "document"],
        trajectory=[
            "evaluated mcp_server performance",
            "identified llm integration gaps",
            "reviewed documentation pipeline",
        ],
        urgency=1.2,
    )

    council = router.activate(test_shipment)

    print(f"Shipment: {council.shipment_id} ({test_shipment.type})")
    print(f"Council top-5:\n")
    for skill_id, score in council.agents:
        record = next(r for r in council.records if r.skill_id == skill_id)
        meta = router.registry.get(skill_id)
        layer = meta.ocr_layer if meta else "?"
        print(f"  {skill_id:30s}  {score:.3f}  [{layer:12s}]  "
              f"onto={record.components['ontology']:.2f}  "
              f"traj={record.components['trajectory']:.2f}  "
              f"bal={record.components['balance']:.2f}  "
              f"prior={record.components['prior']:.2f}")
