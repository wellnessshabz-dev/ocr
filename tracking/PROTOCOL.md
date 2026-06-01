# Agent Protocol — Session Log & Checkpoint System

## Overview

Every agent session in the OCR project produces:
1. A **session summary** in SESSION.md (the "compact") — goal, progress, decisions, context
2. A **log entry** in LOG.md (append-only chronological history)
3. **Decision records** in DECISIONS.md (append-only with rationale)
4. **Git checkpoints** via ckpt (hidden branches for rollback)

This protocol defines how agents interact with the system.

---

## Prerequisites

- **ckpt** installed globally: `npm install -g @mohshomis/ckpt`
- Git repository initialized at project root

---

## Session Lifecycle

### 1. Start

Read existing state, begin tracking.

```bash
./tools/session.sh start "Implement X"
```

This:
- Reads `SESSION.md` to understand any existing state
- Creates a fresh SESSION.md with the given goal
- Runs `ckpt start` to begin git checkpoint tracking
- Writes `STATE.json` with machine-readable initial state

### 2. Snap (Work Loop)

Before each significant change, create a checkpoint.

```bash
./tools/session.sh snap "adding auth middleware"
```

This:
- Runs `ckpt snap "message"` to create a git checkpoint
- Prompts the agent to update the progress section in SESSION.md
- Updates `CHECKPOINTS.md` with the new step hash
- Updates `STATE.json`

Frequency: before every tool call that modifies files (writes, edits, moves).

### 3. Sync

Manually sync the checkpoint registry with ckpt's internal state.

```bash
./tools/session.sh sync
```

This:
- Runs `ckpt steps` to get all checkpoint data
- Rewrites `CHECKPOINTS.md` with the current mapping
- Rewrites `STATE.json` from SESSION.md

Useful when you need an up-to-date CHECKPOINTS.md without creating a new snapshot.

### 4. Log a Decision

Append to DECISIONS.md when an architectural or implementation decision is made.

```bash
./tools/session.sh decide "Decision title" "Rationale" "Alternatives considered"
```

Or write the entry manually using the format:

```markdown
## 2026-06-02 — Decision title

**Decision:** ...
**Rationale:** ...
**Alternatives considered:** ...
**Consequences:** ...
**Related:** ADR-XXXX
```

### 5. End

Finalize the session.

```bash
./tools/session.sh end
```

This:
- Syncs ckpt state to CHECKPOINTS.md
- Appends the current SESSION.md content to LOG.md
- Runs `ckpt end --squash` to squash checkpoint branch into main
- Resets SESSION.md to empty template
- Writes final STATE.json

---

## SESSION.md Format

```markdown
## Goal
What we're trying to accomplish this session

## Progress
### Done
- [x] Task description — detail
### In Progress
- [ ] Task description — detail
### Blocked
- [ ] Task description — why blocked

## Key Decisions
| # | Decision | Rationale | Alternatives |
|---|----------|-----------|--------------|
| 1 | Use X | Because Y | Z was slower |

## Critical Context
Things the next agent absolutely needs to know

## Relevant Files
| File | Purpose | Status |
|------|---------|--------|
| src/x.py | Handles Y | Modified |
```

## LOG.md Entry Format

```markdown
## 2026-06-02 — Short title

- **Duration:** 2h
- **Goal:** Implement X
- **Done:**
  - Thing 1 — detail
  - Thing 2 — detail
- **Decisions:**
  - Decision 1 — brief rationale
- **Next steps:** Thing 3
```

## DECISIONS.md Entry Format

```markdown
## 2026-06-02 — Decision title

**Decision:** ...
**Rationale:** ...
**Alternatives considered:** ...
**Consequences:** ...
**Related:** ADR-XXXX, path/to/file.py
```

---

## Rules

1. **SESSION.md resets per session.** Never carry state across sessions — LOG.md is the permanent record.
2. **LOG.md and DECISIONS.md are append-only.** Never edit past entries. Supersede with new entries.
3. **CHECKPOINTS.md and STATE.json are machine-generated.** Never hand-edit. Use `session.sh sync`.
4. **Snap before every file write.** If a change touches disk, it deserves a checkpoint.
5. **ckpt is the git layer.** Never run `ckpt restore` directly — always via `session.sh` if a wrapper is added.
6. **Restore is for rollback only.** If you restore to a checkpoint, note it in LOG.md.
