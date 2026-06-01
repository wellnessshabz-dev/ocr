---
title: "How Zed 2 Was Trained — Edit Prediction Model (Ben Kunkel / AI Engineer)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Ben Kunkel (Zed)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference talk. Ben Kunkel (Edit Predictions Lead, Zed) presents the training pipeline for Zed 2 — a small specialized model for edit prediction that runs on every keystroke."
tags: ["zed", "edit-prediction", "model-training", "distillation", "teacher-student", "settled-data", "evals", "production-experiments"]
---

# How Zed 2 Was Trained — Edit Prediction Model

Source: AI Engineer conference. Ben Kunkel (Edit Predictions Lead, Zed)
presents the training pipeline for Zed 2's edit prediction model.

## Edit Prediction Task

Given a region of code around the cursor, predict the next edit. Inputs:
recent edits, cursor position, type definitions, variable definitions,
diagnostics/errors. Runs on **every keystroke** → must be very fast → small
specialized fine-tuned model.

## Training Pipeline

### 1. Data Collection (Production Opt-In)
Snapshots capture related types, definitions, and all context around the
cursor at prediction time.

### 2. Distillation (Teacher → Student)
Frontier model (teacher) receives the input and predicts what the user will
type. Problem: teacher is noisy — 100,000 requests → 100,001 different answers.
The prompt must be finely tuned.

### 3. Repair Step (Offline Eval Heuristics)
Heuristics detect bad predictions: is it just undoing what you just typed?
Is it ignoring the editable region boundary? If bad, send to **another**
frontier model with "fix this" prompt to repair the prediction.

### 4. Prompt Formatting (Experiment-Specific)
Each experiment varies the prompt format: include diagnostics vs not, how much
edit history, etc. The teacher's raw prediction is reformatted into the
specific experiment's prompt format.

### 5. Train Student Model (Zed 2)
Train on repaired, formatted teacher predictions.

### 6. Offline Evaluations
Run on held-out test set. Metrics:
- **Delta carf**: Levenshtein variant with n-gram comparison
- **Reversal ratio**: undoing exactly what you just typed
- **Kept rate**: in production
- **Diagnostic error count**: before vs after prediction

## The Teacher-Student Loop

Once the student approaches teacher quality:
- Run the **student** (cheap) 50 times instead of the teacher (expensive)
- Measure Levenshtein distance to the settled state
- Filter: too far = noise, too close = obvious, **in the middle = ideal** training examples (new functions past training cutoff, things the model has never seen)
- This generates ideal training data at low cost

## Settled Data Concept

Wait 10 seconds after user stops editing a region, then snapshot. Problem:
very noisy — user could change mind, agent could rewrite. The settled state
might be completely different from what the prediction looked like.

Filter: generate 50 student predictions, check Levenshtein distance to settled
state. If none are close → noise, discard. If some are close with moderate
distance → ideal training example (the model almost got it).

## Production Experiments

- Dashboard for experiment tracking: acceptance rate, latency, etc.
- Deploy at 15% traffic → sample up → promote to live model
- Newly trained model replaces previous in production

## Relevance to OCR

### Teacher-Student Loop Pattern

| ML Concept | OCR Equivalent |
|------------|----------------|
| Teacher model (frontier, expensive) | Frontier LLM for council deliberation |
| Student model (specialized, cheap) | Specialized perspective agent (fine-tuned or routed) |
| Distillation | Skill registry — encode council patterns into reusable skills |
| Repair step (bad prediction → fix) | Governance rejection → HumanReview or re-deliberation |
| Production experiments (15% traffic) | A/B test governance policies on shipment sample |

### Settled Data for OCR

The "wait 10 seconds for stability" concept could apply to OCR's ontology
extraction — don't extract ontology from mid-edit documents or mid-thought
messages. Wait for the signal to settle.

> "If none are close to the settled state → noise, discard."

### New Insights

| Insight | OCR Application |
|---------|-----------------|
| **Noisy teacher problem** | Frontier models as judges are noisy — don't rely on single LLM judgment for governance; use multi-vote |
| **Middle-distance examples are most valuable** | OCR training data (from audit ledger) should prioritize near-miss governance decisions over obvious passes or noise |
| **Small specialized model beats general** | Zed 2 is tiny and fast because it does one thing. OCR perspective agents should be similarly narrow |
| **Cost shifts from teacher to student over time** | As skills mature, route to cheaper models. Start with frontier, converge to efficient |
| **Experiments at 15% traffic** | OCR governance policies should be tested on shipment samples before full rollout |
