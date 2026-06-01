## Part V — Council Architecture (Q3, Q4)



### Council Deliberation Protocol



```mermaid

sequenceDiagram

    participant CO as Council Orchestrator

    participant S1 as Skill: Strategic

    participant S2 as Skill: Technical

    participant S3 as Skill: Risk

    participant S4 as Skill: Devil Advocate

    participant CH as Chairman

    participant GOV as Governance Check



    CO->>S1: Independent reasoning (context slice A)

    CO->>S2: Independent reasoning (context slice B)

    CO->>S3: Independent reasoning (context slice C)

    CO->>S4: Independent reasoning (context slice D)



    Note over S1,S4: All skills reason in parallel, NO cross-contamination



    S1->>CH: Position + confidence + evidence refs

    S2->>CH: Position + confidence + evidence refs

    S3->>CH: Position + confidence + evidence refs

    S4->>CH: Position + confidence + evidence refs



    CH->>CH: Contradiction detection (semantic diff)

    CH->>CH: Consensus mapping

    CH->>CH: Synthesis draft v1



    alt Contradiction threshold exceeded

        CH->>CO: Request second round (targeted)

        CO->>S1: Respond to S3 contradiction specifically

        S1->>CH: Rebuttal position

        S3->>CH: Counter-rebuttal

        CH->>CH: Synthesis draft v2

    end



    CH->>GOV: Submit synthesis for governance check

    GOV->>CH: Approved / Escalate / Reject

    CH->>CO: Final synthesis committed

```



### Chairman Synthesis (Q4)



The Chairman is **not the smartest LLM**. The Chairman is a **structured synthesis protocol** running on a reasoning-capable OSS model.



Its job is strictly:

1. **Map convergence** — Where do skills agree? This becomes high-confidence output.

2. **Map divergence** — Where do skills disagree? This becomes the *strategic question* (not an error).

3. **Weight by evidence** — Skills that reference ontology-anchored evidence > skills reasoning abstractly.

4. **Preserve dissent** — The synthesis document always contains a "minority position" section. Dissent is organizational memory, not noise.

5. **Declare unknowns** — If no skill can resolve a contradiction, the Chairman declares an explicit *open question* and routes it to the Strategic Question Engine.



**Chairman Output Schema:**

```json

{

  "shipment_id": "SHP-2026-0847",

  "synthesis": {

    "consensus_positions": [...],

    "minority_positions": [...],

    "open_questions": [...],

    "confidence": 0.82,

    "evidence_references": ["ONT-042", "MEM-8821", "REPO-commit-a4f3"]

  },

  "trajectory_delta": {

    "affected_concepts": [...],

    "position_shift": "vector",

    "decision_type": "strategic | tactical | architectural | operational"

  },

  "governance": {

    "requires_human_review": false,

    "risk_flags": [],

    "audit_hash": "sha256:..."

  }

}

```



---
