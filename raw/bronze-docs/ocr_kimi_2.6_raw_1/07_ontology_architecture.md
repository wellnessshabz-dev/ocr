## Part VII — Ontology Architecture (Q6, Q17)



### Ontology is the Backbone, Not an Add-On



The ontology is the **shared cognitive substrate** of the entire organization. Without it, every LLM call is contextless. With it, every LLM call is anchored to the organization's actual world.



```mermaid

graph TB

    subgraph ONTO["Organizational Ontology"]

        subgraph CORE["Core Concepts"]

            PR[Products]

            PE[People - Roles]

            PL[Platform Components]

            DC[Decisions]

            OB[Objectives]

            RS[Risks]

            DP[Dependencies]

        end



        subgraph RELATIONS["Relation Types"]

            OW[owns]

            BL[blocks]

            EN[enables]

            CO[contradicts]

            SP[supersedes]

            DE[depends_on]

            EV[evolved_from]

            AL[aligns_with]

            TH[threatens]

        end



        subgraph META["Meta-Ontology"]

            TV[Temporal Versions]

            CF[Confidence Scores]

            SC[Source Citations]

            AU[Author Attribution]

        end

    end



    PR & PE & PL & DC & OB & RS & DP --> RELATIONS

    RELATIONS --> META

```



### Ontology Evolution Design (Q6)



Ontologies must evolve or they become stale organizational debt. OCR uses **4 evolution mechanisms**:



**1. Shipment-Driven Evolution**

Every committed Shipment runs through the Ontology Extractor. New entities are proposed as `candidate` nodes. After 3+ independent shipments reference the same candidate entity, it is promoted to `confirmed`. This prevents ontology pollution from one-off signals.



**2. Contradiction-Driven Refinement**

When a council deliberation surfaces a contradiction, the Ontologist skill examines whether the contradiction stems from *ontological ambiguity* (two different meanings for the same term). If so, it proposes a concept split.



**3. Decay and Archival**

Concepts not referenced in any Shipment for N days are flagged as `dormant`. Dormant concepts are archived (never deleted) and their relations are weakened. This keeps the active ontology relevant without losing history.



**4. Executive Injection**

Executives can directly inject new ontology concepts via the Executive Surface. These bypass the 3-shipment rule but are flagged as `executive-origin` and require higher council scrutiny when referenced.



```mermaid

flowchart LR

    SIG[Signal arrives] --> EXT[Ontology Extractor]

    EXT --> |New entity| CAND[Candidate Node]

    EXT --> |Existing entity| CONF[Confirm + strengthen edge]

    CAND --> |3+ references| PROM[Promoted to confirmed]

    CAND --> |0 references, 30 days| DISC[Discarded]

    CONF --> |Contradiction detected| SPLIT[Concept split proposed]

    SPLIT --> |Council review| REFINE[Refined ontology]

    CONF --> |No reference, N days| DORM[Dormant]

    DORM --> ARCH[Archived - never deleted]

```



---
