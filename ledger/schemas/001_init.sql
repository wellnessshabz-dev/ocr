-- OCR V1 — Cognition Ledger Schema
-- PostgreSQL 16
-- Run as: psql -U ocr -d ocr_ledger -f ledger/schemas/001_init.sql

BEGIN;

-- ============================================================
-- SHIPMENTS — atomic unit of organizational cognition
-- ============================================================
CREATE TABLE shipments (
    shipment_id     UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_type     VARCHAR(50) NOT NULL,       -- github_commit, obsidian_note, manual_entry, etc.
    source_ref      TEXT NOT NULL,               -- commit hash, note ID, external reference
    shipment_type   VARCHAR(50) NOT NULL,        -- architectural, tactical, knowledge, governance
    ontology_refs   UUID[] DEFAULT '{}',         -- linked ontology node IDs
    trajectory_id   UUID,                        -- optional trajectory binding
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
                    -- pending → compiling → deliberating → committed → surfaced
                    -- deliberating → human_review → committed
                    -- compiling → rejected
    confidence      REAL DEFAULT 0.0,
    payload         JSONB DEFAULT '{}',          -- raw input data (diff, note content, etc.)
    metadata        JSONB DEFAULT '{}',          -- author, repo, branch, etc.
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_shipments_type ON shipments(shipment_type);
CREATE INDEX idx_shipments_source ON shipments(source_type, source_ref);
CREATE INDEX idx_shipments_created ON shipments(created_at DESC);

-- ============================================================
-- COUNCILS — structured deliberation rounds
-- ============================================================
CREATE TABLE councils (
    council_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    shipment_id         UUID NOT NULL REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    round_number        INT NOT NULL DEFAULT 1,
    chairman_summary    TEXT,
    contradiction_score REAL DEFAULT 0.0,
    governance_status   VARCHAR(20) NOT NULL DEFAULT 'pending',
                        -- pending → deliberating → validated → human_review → rejected
    synthesis_v1        JSONB,
    synthesis_v2        JSONB,
    governance_decision VARCHAR(20),             -- validated, human_review, rejected
    governance_rationale TEXT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_councils_shipment ON councils(shipment_id);
CREATE INDEX idx_councils_governance ON councils(governance_status);

-- ============================================================
-- SKILL_OUTPUTS — each skill's position in a council
-- ============================================================
CREATE TABLE skill_outputs (
    skill_output_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    council_id      UUID NOT NULL REFERENCES councils(council_id) ON DELETE CASCADE,
    skill_name      VARCHAR(100) NOT NULL,
    perspective     VARCHAR(50),                 -- strategic, technical, risk, advocacy
    position        TEXT NOT NULL,
    confidence      REAL DEFAULT 0.0,
    evidence_refs   TEXT[],                      -- references to ontology, memory, or source
    reasoning_trace JSONB,
    round_number    INT NOT NULL DEFAULT 1,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_skill_outputs_council ON skill_outputs(council_id);

-- ============================================================
-- ONTOLOGY_NODES — the organization's shared concept graph
-- ============================================================
CREATE TABLE ontology_nodes (
    node_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    concept         VARCHAR(200) NOT NULL,
    node_type       VARCHAR(50) NOT NULL,        -- product, role, component, decision, objective, risk, dependency
    description     TEXT,
    confidence      REAL DEFAULT 0.5,
    status          VARCHAR(20) NOT NULL DEFAULT 'candidate',
                    -- candidate → confirmed → dormant → archived
    lineage_parent  UUID REFERENCES ontology_nodes(node_id),
    metadata        JSONB DEFAULT '{}',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_ontology_concept ON ontology_nodes(concept);
CREATE INDEX idx_ontology_status ON ontology_nodes(status);
CREATE INDEX idx_ontology_type ON ontology_nodes(node_type);

-- ============================================================
-- ONTOLOGY_EDGES — relationships between nodes
-- ============================================================
CREATE TABLE ontology_edges (
    edge_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_node_id  UUID NOT NULL REFERENCES ontology_nodes(node_id) ON DELETE CASCADE,
    target_node_id  UUID NOT NULL REFERENCES ontology_nodes(node_id) ON DELETE CASCADE,
    relation_type   VARCHAR(50) NOT NULL,        -- owns, blocks, enables, contradicts, supersedes, depends_on
    weight          REAL DEFAULT 1.0,
    metadata        JSONB DEFAULT '{}',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_edges_source ON ontology_edges(source_node_id);
CREATE INDEX idx_edges_target ON ontology_edges(target_node_id);

-- ============================================================
-- ADRS — Architectural Decision Records
-- ============================================================
CREATE TABLE adrs (
    adr_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title       VARCHAR(200) NOT NULL,
    status      VARCHAR(20) NOT NULL DEFAULT 'draft',
                -- draft → proposed → accepted → deprecated → superseded
    supersedes  UUID REFERENCES adrs(adr_id),
    content     TEXT NOT NULL,
    context     TEXT,
    decision    TEXT,
    consequences TEXT,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_adrs_status ON adrs(status);

-- ============================================================
-- REPLAY_SESSIONS — cognitive event replay
-- ============================================================
CREATE TABLE replay_sessions (
    replay_id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    shipment_id     UUID NOT NULL REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    replay_diff     JSONB,                       -- what changed vs original run
    model_version   VARCHAR(50),
    status          VARCHAR(20) NOT NULL DEFAULT 'completed',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_replay_shipment ON replay_sessions(shipment_id);

-- ============================================================
-- TRACES — observability for every operation
-- ============================================================
CREATE TABLE traces (
    trace_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parent_id   UUID REFERENCES traces(trace_id),
    shipment_id UUID REFERENCES shipments(shipment_id),
    component   VARCHAR(100) NOT NULL,
    operation   VARCHAR(100) NOT NULL,
    duration_ms INT,
    input_hash  VARCHAR(64),
    output_hash VARCHAR(64),
    metadata    JSONB DEFAULT '{}',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_traces_shipment ON traces(shipment_id);
CREATE INDEX idx_traces_component ON traces(component);
CREATE INDEX idx_traces_created ON traces(created_at DESC);

-- ============================================================
-- TRIGGERS
-- ============================================================
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_shipments_updated_at
    BEFORE UPDATE ON shipments
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trg_councils_updated_at
    BEFORE UPDATE ON councils
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trg_ontology_nodes_updated_at
    BEFORE UPDATE ON ontology_nodes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trg_adrs_updated_at
    BEFORE UPDATE ON adrs
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

COMMIT;
