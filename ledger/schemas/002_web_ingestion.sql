-- OCR V1 — Web Ingestion Schema
-- Tracks every web fetch, crawl, and scrape operation
-- Part of the ingestion layer audit trail

-- ============================================================
-- WEB_SESSIONS — every web fetch operation
-- ============================================================
CREATE TABLE web_sessions (
    session_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tool            VARCHAR(50) NOT NULL,        -- firecrawl, playwright, fetch
    operation       VARCHAR(50) NOT NULL,        -- scrape, crawl, search, extract, interact
    source_url      TEXT,
    query           TEXT,
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
                    -- pending → active → completed → failed
    page_count      INT DEFAULT 0,
    error_message   TEXT,
    duration_ms     INT,
    metadata        JSONB DEFAULT '{}',          -- tool-specific params, headers, etc.
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at    TIMESTAMPTZ
);

CREATE INDEX idx_web_sessions_tool ON web_sessions(tool);
CREATE INDEX idx_web_sessions_status ON web_sessions(status);
CREATE INDEX idx_web_sessions_created ON web_sessions(created_at DESC);

-- ============================================================
-- WEB_PAGES — content fetched from each URL
-- ============================================================
CREATE TABLE web_pages (
    page_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID NOT NULL REFERENCES web_sessions(session_id) ON DELETE CASCADE,
    url             TEXT NOT NULL,
    title           TEXT,
    description     TEXT,
    markdown        TEXT,                        -- cleaned content (primary output)
    raw_html        TEXT,                        -- original HTML (for debugging)
    metadata        JSONB DEFAULT '{}',          -- status code, headers, content-type, etc.
    word_count      INT DEFAULT 0,
    checksum        VARCHAR(64),                 -- SHA-256 for dedup
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_web_pages_session ON web_pages(session_id);
CREATE INDEX idx_web_pages_url ON web_pages(url);
CREATE INDEX idx_web_pages_checksum ON web_pages(checksum);

-- ============================================================
-- ONTOLOGY_FEED — how web content feeds the ontology
-- ============================================================
CREATE TABLE ontology_feeds (
    feed_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    page_id         UUID NOT NULL REFERENCES web_pages(page_id) ON DELETE CASCADE,
    node_ids        UUID[],                      -- ontology nodes created/updated from this page
    concepts        TEXT[],                      -- concepts extracted from the content
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
                    -- pending → processed → skipped
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_ontology_feeds_page ON ontology_feeds(page_id);
CREATE INDEX idx_ontology_feeds_status ON ontology_feeds(status);
