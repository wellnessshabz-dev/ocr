# Decision Log

> Append-only record of every architectural and implementation decision.
> Each entry: date, decision, rationale, alternatives considered, consequences.
> Links to ADRs where applicable.

---

## 2026-06-02 — Session tracking in `ocr/tracking/` not `.ocr/`

**Decision:** Place session tracking files in `ocr/tracking/` (a visible directory) instead of `.ocr/` (a hidden dot-directory).

**Rationale:** Hidden dot-directories are invisible to `ls` by default, confusing for new developers, and agents may not discover them without explicit instruction. A visible `ocr/tracking/` directory is self-documenting — its `_index.md` explains the system immediately.

**Alternatives considered:**
- `.ocr/` — hidden, gitignored by convention, keeps root clean
- `docs/tracking/` — tracking isn't documentation, it's operational state
- `tracking/` at root — adds noise to the 22-item root directory

**Consequences:**
- All tracking files are git-tracked (except STATE.json) — visible in `git log`
- Agents can discover `ocr/tracking/` via directory listing
- SESSION.md is ephemeral (resets per session) but git tracks it — old sessions are recoverable

**Related:** `ocr/tracking/PROTOCOL.md`

---

## 2026-06-02 — ckpt for git checkpoints + custom session.sh for context

**Decision:** Use `@mohshomis/ckpt` (npm package) for git-based checkpoints and build `ocr/tracking/tools/session.sh` as a thin wrapper that bridges ckpt mechanics with session context tracking.

**Rationale:** ckpt handles the hard part (hidden git branches, per-step commits, restore, squash). Building that from scratch would be fragile. But ckpt has no concept of "session goals" or "decision logs" — that's what the custom files provide.

**Alternatives considered:**
- Build everything from scratch — more control, more bugs
- Use only ckpt — misses session context (goal, decisions, progress)
- Use only markdown files — no rollback capability

**Consequences:**
- ckpt dependency: must be installed (documented in PROTOCOL.md)
- session.sh is the single entry point — agents don't call ckpt directly
- CHECKPOINTS.md bridges ckpt's git model to OCR's tracking model

**Related:** `ocr/tracking/PROTOCOL.md`, `ocr/tracking/tools/session.sh`

---

## 2026-06-02 — LOG.md and DECISIONS.md are append-only

**Decision:** LOG.md and DECISIONS.md are never edited after writing. New entries are appended. Old entries stand as written, even if superseded.

**Rationale:** Append-only history provides an immutable audit trail. If a decision is wrong, the correction is a new entry in DECISIONS.md (not an edit). This preserves context — future readers see the mistake AND the correction.

**Alternatives considered:**
- Editable — cleaner looking, loses audit trail
- Database-backed — overengineered for file-based tracking

**Consequences:**
- LOG.md grows forever (linear growth is fine — entries are small)
- Old decisions remain visible; corrected decisions link to their superseder
- gbrain ingestion gets the full history, not just the latest version

**Related:** `docs/adrs/ADR-0004-replayability-requirements.md`
