## Part XX — Deployment Architecture



```mermaid

graph TB

    subgraph VPS["VPS - Single Node Bootstrap"]

        subgraph SERVICES["Core Services"]

            N8N[n8n - Orchestration]

            OL[Ollama - OSS LLM host]

            PG[PostgreSQL - Audit, Shipments, Ontology]

            NEO[Neo4j CE - Graph index]

            RED[Redis - Working memory cache]

            OBV[Obsidian Vault sync]

        end



        subgraph APP["Application Layer"]

            API[OCR API - FastAPI]

            WS[WebSocket - Executive surface live updates]

            AUTH[Auth - Keycloak OSS]

        end



        subgraph STORAGE["Storage"]

            VOL[Persistent volumes - all state]

            BAK[Nightly backup to S3-compatible]

        end

    end



    subgraph CLIENTS["Clients"]

        EX[Executive web surface]

        GHW[GitHub webhooks]

        OBW[Obsidian plugin]

    end



    GHW --> N8N

    OBW --> N8N

    N8N --> API

    API --> OL & PG & NEO & RED

    EX --> WS & API

    SERVICES --> BAK

```



**Bootstrap cost estimate:**

| Component | Cost |

|---|---|

| VPS (8 core, 32GB, 500GB NVMe) | ~$40-80/month |

| OSS LLM (Llama 3 8B on-device) | $0 extra |

| n8n (self-hosted) | $0 |

| Neo4j Community Edition | $0 |

| PostgreSQL | $0 |

| Obsidian + plugin | ~$10/month |

| **Total** | **~$50-100/month** |



This is enterprise organizational intelligence for under $100/month to start.



---
