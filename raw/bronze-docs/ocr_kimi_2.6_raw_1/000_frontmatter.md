Layer	What it selects	Token budget

Ontological Core	The entities directly named in the shipment, their first-order relations	20%

Trajectory Context	Recent decisions on the same trajectory path	30%

Contradicting Evidence	Memory fragments that oppose the current signal	15%

Skill Prerequisites	What the assigned skills need to reason well	20%

Headroom	Reserved for council synthesis expansion	15%Component	Cost

VPS (8 core, 32GB, 500GB NVMe)	~$40-80/month

OSS LLM (Llama 3 8B on-device)	$0 extra

n8n (self-hosted)	$0

Neo4j Community Edition	$0

PostgreSQL	$0

Obsidian + plugin	~$10/month

Total	~$50-100/month# Organizational Cognition Runtime — Principal Architecture Document



> *Reasoning from first principles. This is not a generic agent platform. This is persistent organizational intelligence infrastructure.*



---



## Foundational Philosophy



Before touching a single diagram, the intellectual frame must be correct.



**Generic agent platforms** route tasks to LLMs and call it intelligence. That produces ephemeral, unreliable, unauditable noise.



**Organizational Cognition Runtime (OCR)** is different. It treats the organization as a *cognitive entity* with:

- **Memory** that persists and evolves (not RAG over docs)

- **Ontology** that represents what the org *knows it knows*

- **Shipments** as the atomic unit of intentional organizational action

- **Councils** as structured deliberation — not round-robin prompting

- **GBrain** as the live memory substrate — not a vector store

- **Trajectories** as the organization's path through decision space over time



The moat is **not the LLM**. The moat is the **accumulated, structured, replayable cognitive history** of the organization.



---
