---
title: "AI Engineer (Channel) — YouTube Videos"
description: "Videos from the AI Engineer YouTube channel. Channel-based directory: the channel name is the directory name, not a topic category."
status: "active"
district: "raw/bronze-docs/youtube/AI_Engineer"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs", "docs/adrs"]
traffic:
  reads: ["Architecture synthesis", "Skill authors looking for reference patterns"]
  writes: ["YouTube ingestion cron job"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# AI Engineer — YouTube Videos

Collection of reasoned analyses from YouTube videos about building software
with AI agents. Each file is a self-contained analysis with source metadata.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `nick_nisi_building_ai_systems_that_ship.md` | Nick Nisi (WorkOS) | Gates over agents, skills as gotchas, evals, harness engineering | reasoned |
| `matt_pocock_building_ai_systems_that_ship.md` | Matt Pocock | Grill Me, vertical slices, TDD, deep modules, Kanban DAG | reasoned |
| `luke_alvoeiro_factory_missions_multi_agent_architecture.md` | Luke Alvoeiro (Factory) | Orchestrator/worker/validator, serial execution, validation contracts, Missions | reasoned |
| `patrick_debois_context_is_the_new_code.md` | Patrick Debois (Tessel) | Context Development Life Cycle, CDLC, layered evals, skills as packages, SBOM | reasoned |
| `dex_horthy_advanced_context_engineering.md` | Dex Horthy (HumanLayer) | Advanced Context Engineering, RPI (Research→Plan→Implement), dumb zone, intentional compaction, sub-agents for context | reasoned |
| `phil_hetzel_eval_maturity_for_agents.md` | Phil Hetzel (BrainTrust) | Eval maturity levels, eval flywheel, LLM-as-judge, stateful evals, production traces as datasets | reasoned |
| `daniel_zook_rust_for_vibe_coding.md` | Daniel Zook (Sentry) | Rust as ideal AI coding language, deterministic guardrails, compiler as gate, alien intelligence | reasoned |
| `tejas_art_of_ai_harness.md` | Tejas (IBM) | Harness > prompts, deterministic guardrails, verify step removes lying, outer loop around agent loop | reasoned |
| `tejas_ai_harnesses_stuff_around_the_model.md` | Tejas (IBM) | Deep-dive: harness components, verify step, login handler, zero prompt changes, harness maturity model | reasoned |
| `ben_kunkel_zed_2_edit_prediction_training.md` | Ben Kunkel (Zed) | How Zed 2 was trained — edit prediction, distillation pipeline, teacher-student loop, settled data, production experiments | reasoned |
| `steve_safe_intelligence_spec_driven_validation_agents.md` | Steve (Safe Intelligence) | Spec-driven validation — smart vs safe, rules, ontologies, robustness, agent card, implementation independence, jury-rigged RL | reasoned |

## Topic Tags

Videos are tagged with topics for searchability:
- `gates-over-agents` — Enforcement gates > agent intelligence
- `skills-as-gotchas` — Short gotcha skills beat comprehensive docs
- `tdd` — Test-driven development for AI workflows
- `vertical-slices` — Cross-layer implementation vs horizontal
- `deep-modules` — Small interface, large implementation design
- `evals` — Measurement and evaluation pipelines
- `workflow` — End-to-end development workflow with AI
- `cdlc` — Context Development Life Cycle (G-E-D-O-A)
- `context-lifecycle` — Full lifecycle management for context
- `serial-execution` — Serial beats parallel for agent execution
- `orchestrator-worker-validator` — Three-role production architecture
- `ubiquitous-language` — DDD shared vocabulary between human and AI
- `code-is-not-cheap` — Bad code is the most expensive it's ever been
- `context-lifecycle` — Context Development Life Cycle (Patrick Debois)
- `context-engineering` — Context window management (Dex Horthy)
- `rpi` — Research→Plan→Implement workflow
- `intentional-compaction` — Proactive context compression
- `mental-alignment` — Code review for shared understanding
- `eval-maturity` — Four levels of eval maturity (human → LLM-judge → trace → automated)
- `eval-flywheel` — Production traces → identify failures → offline eval → improve
- `stateful-evals` — Representing external system state during evaluation
- `deterministic-guardrails` — Compile-time enforcement > non-deterministic review
- `compiler-as-gate` — Rust compiler as the ultimate correctness gate
- `harness-engineering` — Harness > prompts, deterministic guardrails > LLM instruction
- `verify-step` — Deterministic post-execution verification to detect lying
- `deterministic-override` — Programmatic handlers for agent failure modes (login, auth)
- `outer-loop` — Retry loop around agent loop for fault tolerance
- `harness-maturity` — Levels of harness sophistication (Tejas's model)
- `zero-prompt-changes` — All improvements from harness structure, not prompt text

## Naming Convention

`<speaker>_<topic>.md` — snake_case, descriptive of content. Speaker
name first for attribution (all caps is typo convention from other files; use
lowercase for readability).

## Related Directories

- `raw/bronze-docs/youtube/`
- `docs/adrs/` — where synthesis of these videos is codified
