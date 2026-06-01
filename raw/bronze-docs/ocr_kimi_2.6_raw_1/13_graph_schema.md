## Part XIII — Graph Schema (Q17 — GraphRAG)



### The OCR Graph is NOT a Knowledge Graph in the traditional sense



It is an **organizational cognitive graph** where the primary entities are *decisions, not facts*.



```mermaid

graph TB

    subgraph SCHEMA["Graph Node Types"]

        DN[Decision Node]

        CN[Concept Node]

        SN[Shipment Node]

        PN[Person-Role Node]

        RN[Repo Node]

        QN[Question Node]

        TN[Trajectory Node]

    end



    subgraph EDGES["Edge Types with Properties"]

        E1["resulted_in: weight, confidence, timestamp"]

        E2["evolved_from: diff, author, timestamp"]

        E3["contradicts: severity, resolved_by"]

        E4["depends_on: coupling_strength, verified"]

        E5["authored_by: role_at_time"]

        E6["surfaces_question: urgency, open_since"]

        E7["belongs_to_trajectory: position_index"]

    end



    DN -->|resulted_in| CN

    SN -->|resulted_in| DN

    CN -->|evolved_from| CN

    DN -->|contradicts| DN

    CN -->|depends_on| CN

    SN -->|authored_by| PN

    DN -->|surfaces_question| QN

    SN -->|belongs_to_trajectory| TN

```



### GraphRAG in OCR (Q17)



GraphRAG is used in OCR but with a **critical constraint:** graph traversal is *ontology-guided*, not *similarity-guided*.



**Standard GraphRAG**: "Find nodes similar to query, expand neighborhood."



**OCR GraphRAG**: "Anchor to named ontology nodes in query, traverse by *relation type*, not similarity."



This means a query about "the decision to adopt OSS LLMs" doesn't surface random similar decisions — it surfaces:

- **The shipment that made that decision**

- **The council positions that argued for and against**

- **The trajectory it belongs to**

- **Any subsequent decisions that `depends_on` or `contradicts` it**

- **The concepts it `evolved_from`**



That is organizational intelligence, not semantic search.



---
