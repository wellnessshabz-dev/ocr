---
title: "Vibe Coding to Agentic Engineering — Andrej Karpathy"
source_type: "youtube"
channel: "Sequoia Capital"
speaker: "Andrej Karpathy"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Interview with Andrej Karpathy (OpenAI co-founder, former Tesla AI leader, coined 'vibe coding') on Sequoia Capital's channel. Covers Software 3.0, jagged intelligence, vibe coding vs agentic engineering, verifiability, and LLM Wiki."
tags: ["software-3.0", "vibe-coding", "agentic-engineering", "jagged-intelligence", "verifiability", "ghosts-vs-animals", "llm-wiki", "agent-native", "understanding-bottleneck"]
---

# Vibe Coding to Agentic Engineering — Andrej Karpathy

Source: Sequoia Capital YouTube channel. Interview with Andrej Karpathy, OpenAI
co-founder, former head of AI at Tesla, creator of the LLM Wiki pattern and
microGPT, coined "vibe coding" and "Software 3.0."

## Core Thesis

We are in a transition from **Software 2.0** (programming by creating datasets
and training neural networks) to **Software 3.0** (programming by prompting and
managing context). The programming paradigm has shifted from "writing code" to
"writing the text to copy-paste to your agent." But with this power comes a new
discipline: **agentic engineering**, which is about preserving the quality bar
while going faster.

## Software 3.0

| Era | Paradigm | What You Write | Who Executes |
|-----|----------|----------------|--------------|
| 1.0 | Explicit rules | Code | CPU |
| 2.0 | Learned weights | Datasets + architectures | Neural net (training) |
| 3.0 | Context as program | Prompts + context | LLM (inference) |

The OpenClaw installation example: instead of a shell script that enumerates
every platform variation, the "installer" is a blob of text you copy-paste to
your agent. The agent uses its own intelligence to figure out your environment
and adapt. This is qualitatively different — the code doesn't enumerate cases;
the agent handles them.

The MenuGen example: the Software 1.0/2.0 version is an app (upload photo →
OCR → generate images → render). The Software 3.0 version is: upload photo to
Gemini, say "use Nanobanana to overlay the things onto the menu," and Gemini
returns the modified image. The app shouldn't exist. **New things are now
possible that weren't possible before.**

## Vibe Coding vs Agentic Engineering

Karpathy distinguishes two modes:

| | Vibe Coding | Agentic Engineering |
|---|-------------|-------------------|
| **Purpose** | Raises the floor | Preserves the quality bar |
| **Who** | Everyone | Professional engineers |
| **Goal** | Make anything | Make anything *that doesn't break* |
| **Risk** | Vulnerabilities, slop | None (gates prevent it) |
| **Tool** | Prompts | Context engineering + validation |

Vibe coding is the democratization effect. Agentic engineering is the
professional discipline that ensures quality at speed.

## Jagged Intelligence

Models are not uniformly capable. They have "peaks" (code, math) and "valleys"
(car wash distance, strawberry letter counting). This jaggedness comes from:

1. **RL training distribution** — labs train on what's verifiable AND valuable
2. **Pre-training data** — what happens to be in the dataset (chess in GPT-4)
3. **Lab priorities** — what the labs decide to focus on

The practical upshot: you need to **explore the model** to find where the peaks
are for your specific use case. There's no manual. The jaggedness is a
fundamental property — you cannot assume uniform capability.

**For OCR**: This is the strongest argument for gates. The model is not
uniformly reliable. Gates catch the valleys.

## Verifiability

What gets automated fastest = what is verifiable. Code and math are verifiable
(you can check if they work). This is why the labs have focused there.

Karpathy's insight: if you're in a domain that is verifiable but the labs
haven't focused on it, you can **build your own RL environments** and
fine-tune. Verifiability is a lever you can pull yourself.

But the flip side: even non-verifiable domains (writing, design) can be made
verifiable through proxy means (council of LLM judges). "Everything is
automatable" — it's just a question of how hard.

## Ghosts vs Animals

Karpathy's philosophical framing: LLMs are not animal-like intelligences.
They don't have intrinsic motivation, curiosity, or empowerment. They are
**statistical simulation circuits** with RL bolted on — "ghosts summoned from
data," not animals shaped by evolution.

This matters because:
- Yelling at them doesn't help
- They don't learn from mistakes in the way a human would
- Their capabilities are determined by training distribution, not intrinsic drive
- You need to treat them as tools with known failure modes

**For OCR**: Confirms the gate-based approach. Don't trust the model to
self-correct — build external verification.

## Understanding is the Bottleneck

Karpathy's most quoted line from this talk: **"You can outsource thinking, but
you can't outsource understanding."**

Even as agents get more capable, the human must still understand what the
system is doing, why it's worth doing, and how to direct the agents. This is
the fundamental bottleneck.

His LLM Wiki pattern is explicitly about this: use LLMs to process information,
build persistent knowledge bases, and enhance understanding. The wiki is not
just a reference — it's a tool for the human to maintain understanding of a
complex system.

**For OCR**: OCR's ontology is the organizational understanding layer. It's not
just a graph for agents to query — it's a tool for the humans in the
organization to maintain understanding of the decision landscape.

## Agent-Native Infrastructure

Karpathy's strongest practical opinion: **everything should be written for
agents first.** Documentation should tell you what to copy-paste to your agent,
not what to click in a UI. APIs should be structured for LLM legibility. Data
structures should be agent-native.

The MenuGen deployment example: most of the work was not writing the app —
it was configuring Vercel, DNS, Stripe, Google OAuth. Agent-native
infrastructure would handle all of this from a prompt.

**For OCR**: The shipment pipeline should be agent-native. Every gate produces
structured artifacts that are legible to both agents and humans. The ontology
graph is an agent-native data structure.

## Code Quality Concerns

Karpathy's honest assessment of AI-generated code: "Sometimes I get a little
bit of a heart attack because it's not super amazing code. It's very bloated,
a lot of copy-paste, awkward abstractions that are brittle."

The microGPT project: he tried to get an LLM to simplify code and it
fundamentally couldn't. This felt like being "outside the RL circuits" — the
model was not trained for simplification.

**For OCR**: This validates Matt Pocock's "Code is NOT cheap" thesis from the
model's own creator. Even Karpathy struggles to get models to write clean code.

## Hiring for Agentic Engineering

The old hiring paradigm: puzzles, algorithms, leetcode.
The new hiring paradigm: "Give me a really big project and see someone
implement it. Build a Twitter clone for agents. Make it secure. Have agents
try to break it."

Hiring for taste, judgment, design, and the ability to coordinate agents.

## Relevance to OCR

### What Karpathy Adds That No One Else Does

| Insight | Unique to Karpathy | OCR Application |
|---------|-------------------|-----------------|
| **Software 3.0** | Theoretical foundation for the paradigm shift | OCR is a Software 3.0 system — it programs through context management |
| **Vibe coding vs agentic engineering** | Two distinct modes with different quality bars | OCR is agentic engineering — gates preserve the quality bar |
| **Jagged intelligence** | Models are not uniformly capable; peaks from RL distribution + data | Gates catch the valleys; don't trust uniform capability |
| **Ghosts vs animals** | LLMs are statistical circuits, not living intelligences | Design systems for tools with known failure modes, not apprentices |
| **Understanding as bottleneck** | You can outsource thinking but not understanding | OCR's ontology is the organizational understanding layer |
| **Agent-native infrastructure** | Everything should be written for agents first | Shipment pipeline should be agent-native; every gate produces legible artifacts |
| **Verifiability determines automation speed** | Labs focus on what's verifiable AND valuable | Build verifiability into every gate |
| **You can build your own RL** | If domain is verifiable but lab hasn't focused on it | Eval pipeline is OCR's RL environment |

### Confirms Existing Decisions

- **Gates > agents** (Nick Nisi): Jagged intelligence proves models need external verification
- **Code is NOT cheap** (Matt Pocock): Confirmed by Karpathy's own experience with bloated code
- **Don't outsource the thinking** (Dex Horthy): "You can outsource thinking but not understanding" — same message
- **LLM Wiki pattern** (documented in architecture synthesis): Karpathy confirms the pattern is about enhancing understanding
- **Evals as precondition** (Patrick Debois): Verifiability determines automation speed

### Conflicting Viewpoints

- Karpathy says "everything is automatable" (just a question of effort). This is
  more optimistic than Matt Pocock's "code is NOT cheap" or Nick's "gates are
  the bottleneck." The resolution: Karpathy is describing the *potential*;
  Matt and Nick are describing the *practice required to realize it*. OCR
  implements the practice.

- Karpathy's vibe coding mode is compatible with speed but not quality. OCR
  is explicitly about agentic engineering — preserving quality. Both modes
  are valid but for different contexts.

## Comparison with Other Speakers

| Dimension | Nick Nisi | Matt Pocock | Luke Alvoeiro | Patrick Debois | Dex Horthy | Karpathy | Boris Cherny |
|-----------|-----------|-------------|---------------|----------------|------------|----------|--------------|
| **Core frame** | Gates + measurement | Workflow + design | Production architecture | Lifecycle management | Context window management | **Paradigm shift (SW 3.0)** | **Product overhang + org process** |
| **Key concept** | State machine | Grill Me, deep modules | Orchestrator/worker/validator | CDLC | RPI | **Software 3.0** | **Loops, routines** |
| **Why gates exist** | Enforce transitions | Prevent cheating | Validate contracts | Error budgets | Keep in smart zone | **Models are jagged** | **Model capability grows, harness shrinks** |
| **Testing model** | SHA/video proof | TDD | Validation contracts | Layered evals | Plan verification | **Verifiability lever** | **Auto loops (CI patrol)** |
| **Org scope** | Team | Individual + team | Team + product | Team + org | Team + org | **Industry-wide** | **Company-wide** |
| **Biggest insight** | Gates > intelligence | Code is NOT cheap | Serial beats parallel | Context needs lifecycle | Don't outsource thinking | **Can't outsource understanding** | **Org process > technology** |

Karpathy is the **theoretical foundation** for everything the other speakers
build on. He explains WHY the paradigm has shifted (Software 3.0).
He explains WHY agents are jagged (training distribution). He explains WHY
agentic engineering is needed (vibe coding without quality is dangerous).
Boris is the **living proof** at scale — 100% AI-generated codebase,
thousands of concurrent agents, zero manually written code.
