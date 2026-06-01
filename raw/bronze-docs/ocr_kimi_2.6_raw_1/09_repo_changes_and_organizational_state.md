## Part IX — Repo Changes and Organizational State (Q9)



### GitHub MCP → Org State Pipeline



```mermaid

sequenceDiagram

    participant GH as GitHub MCP

    participant ING as Ingestion DAG (n8n)

    participant OE as Ontology Extractor

    participant SC as Shipment Compiler

    participant TM as Trajectory Modeler

    participant GB as GBrain

    participant SQ as Strategic Question Engine



    GH->>ING: Commit event (diff, message, author, PR)

    ING->>OE: Extract: files changed, concepts mentioned, dependencies modified

    OE->>OE: Resolve to ontology nodes (component, feature, person, decision)

    OE->>SC: Ontology diff + commit metadata



    alt Structural change detected (new module, deleted service, API change)

        SC->>SC: Classify as architectural shipment

        SC->>GB: Query: what decisions depend on this component?

        GB->>SC: Dependent decision graph

        SC->>CO: High-priority council: Architect + Risk + Execution

    else Documentation change

        SC->>SC: Classify as knowledge shipment

        SC->>OE: Update LLM Wiki with new semantic content

    else Feature commit

        SC->>TM: Emit tactical trajectory delta

        TM->>SQ: Check: does this commit contradict a strategic decision?

    end



    GB->>GB: Update component state in ontology

    TM->>TM: Record: org is executing on [concept cluster]

```



**Key insight:** Not every commit should trigger a full council. The Shipment Compiler uses a **significance classifier** (deterministic rules + lightweight LLM for edge cases) to route commits to:

- **Architectural Shipments** → Full council deliberation

- **Tactical Shipments** → Lightweight logging + ontology update

- **Knowledge Shipments** → Wiki + ontology update only

- **Signal Shipments** → Trajectory logging only



This keeps the system from drowning in noise.



---
