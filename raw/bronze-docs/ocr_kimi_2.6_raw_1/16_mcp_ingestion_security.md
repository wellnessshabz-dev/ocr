## Part XVI — MCP Ingestion Security (Q15)



```mermaid

flowchart TD

    GH[GitHub MCP endpoint] --> VER[Webhook signature verification]

    VER --> |valid| SAN[Payload sanitization]

    VER --> |invalid| DROP[Drop + alert]

    SAN --> SCOPE[Scope check: is this repo in org manifest?]

    SCOPE --> |in scope| RATE[Rate limiting: max N events per minute]

    SCOPE --> |out of scope| QUARANTINE[Quarantine + manual review]

    RATE --> STRIP[Strip PII: emails, tokens, secrets]

    STRIP --> NORM[Normalize to OCR event schema]

    NORM --> SIGN[Sign event with org key]

    SIGN --> ING[Ingestion DAG]

```



**Security principles for MCP ingestion:**

1. **Webhooks are verified** at the transport layer before any processing

2. **Scope manifests** define exactly which repos OCR is allowed to ingest — no default-allow

3. **Secret scanning** runs on every payload before ontology extraction — accidentally committed secrets are quarantined, not ingested into organizational memory

4. **Rate limiting** prevents ingestion floods from triggering runaway council activity

5. **Event signing** creates a trust chain from source to audit ledger



---
