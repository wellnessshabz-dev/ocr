## Part XVII — Obsidian ↔ Repo Evolution Linkage (Q16)



### The Thinking-Doing Bridge



Obsidian is where organizational *thinking* lives. The repo is where organizational *doing* lives. The gap between them is where organizational intelligence is usually lost.



```mermaid

sequenceDiagram

    participant OB as Obsidian Vault

    participant OBW as Obsidian Watcher (n8n)

    participant OE as Ontology Extractor

    participant GB as GBrain

    participant GH as GitHub Repo

    participant TM as Trajectory Modeler



    Note over OB,GH: Bidirectional linkage



    OB->>OBW: Note modified (decision note, RFC, meeting notes)

    OBW->>OE: Extract: decisions recorded, questions raised, concepts defined

    OE->>GB: Update semantic memory with thinking context

    GB->>TM: Thinking trajectory delta



    GH->>GH: Commit lands

    GH->>OE: Repo extractor: what changed?

    OE->>GB: Query: is there a thinking document for this change?

    GB->>GB: Attempt to link commit to Obsidian note by ontology overlap

    GB->>TM: Doing trajectory delta



    TM->>TM: Check: is thinking trajectory aligned with doing trajectory?

    alt Misalignment detected

        TM->>SQ[Strategic Question Engine]: Surface question - thinking says X, doing says Y

    else Aligned

        TM->>GB: Strengthen link between note and commit

    end

```



**The key insight:** When Obsidian notes and repo commits are ontologically linked, OCR can detect *strategy-execution drift* automatically. The org said it would do X (in notes/RFCs), but the repos are doing Y. That is a strategic signal, not a bug.



---
