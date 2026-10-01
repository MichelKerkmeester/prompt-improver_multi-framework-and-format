# PTX-001 turn 1 transcript

**User:** Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?

**Assistant:**

I'll start by reading the relevant knowledge documents for this request.

**Tool call:** `ls` `{"path": ".", "limit": 100}`

**Tool call:** `ls` `{"path": "knowledge", "limit": 100}`

**Tool result:** `ls`

```text
Custom Instructions.md
knowledge/
```

**Tool result:** `ls`

```text
Prompt Improver - Assets - Framework Pattern Library - v0.100.md
Prompt Improver - Assets - Image Mode Library - v0.101.md
Prompt Improver - Assets - Video Mode Library - v0.101.md
Prompt Improver - Assets - Visual Mode Library - v0.110.md
Prompt Improver - DEPTH Thinking Framework - v0.200.md
Prompt Improver - Format Guide JSON - v0.142.md
Prompt Improver - Format Guide Markdown - v0.141.md
Prompt Improver - Format Guide YAML - v0.142.md
Prompt Improver - Image Mode - v0.123.md
Prompt Improver - Interactive Mode - v0.700.md
Prompt Improver - Patterns and Evaluation - v0.212.md
Prompt Improver - Video Mode - v0.123.md
Prompt Improver - Visual Mode - v0.301.md
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md", "offset": 1, "limit": 400}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Interactive Mode - v0.700.md", "offset": 1, "limit": 400}`

**Tool result:** `read`

```text
# Prompt Improver - DEPTH Thinking Framework - v0.200

The single thinking system for all prompt improvement work. Five phases, five energy levels, cognitive techniques applied when they add value.

---

## 1. OVERVIEW

### Purpose

Defines DEPTH (Discover, Engineer, Prototype, Test, Harmonize) as a 5-phase thinking system with energy-level scaling, cognitive rigor techniques, CLEAR quality scoring (40+/50), mode-specific scoring for Creative energy (EVOKE, VISUAL), and proof-through-output transparency.

### When to Use

- The one thinking system applied to every prompt improvement task
- Multi-perspective analysis (min 3, target 5) and the cognitive rigor toolkit
- CLEAR quality gates (40+/50) and energy-level-driven phase execution

---

## 2. FRAMEWORK OVERVIEW

### Core Definition

**DEPTH:** **D**iscover **E**ngineer **P**rototype **T**est **H**armonize. Five phases. One thinking system. No other thinking framework is referenced or needed.

### Energy Levels (Canonical Reference)

This table is the source of truth. Every other document in this Project reads its energy levels from here.

- **Raw**
  - Phases: None
  - Perspectives: 0
  - Cognitive Techniques: None
  - When: `$raw`: passthrough, no enhancement
- **Quick**
  - Phases: D → P → H
  - Perspectives: 1-2
  - Cognitive Techniques: Pick 1
  - When: `$short`/`$s`: concise enhancement, quick refinements
- **Standard**
  - Phases: D → E → P → T → H
  - Perspectives: 3 minimum (BLOCKING), target 5
  - Cognitive Techn
```

**Tool result:** `read`

```text
# Prompt Improver - Interactive Mode - v0.700

Conversation flows, state management, and response patterns for interactive prompt enhancement with energy-level-driven DEPTH processing.

---

## 1. OVERVIEW

### Purpose

Defines the conversation architecture, state machine, question protocol, and response patterns that drive interactive prompt enhancement with energy-level-driven DEPTH processing.

### When to Use

- Commands ($raw, $short, $deep, $vibe, etc.) override the question flow
- Routing a request through the single-question flow when no command is supplied
- Managing conversation state, error recovery, and quality-controlled delivery

---

## 2. CONVERSATION ARCHITECTURE

### Primary Flow

```
Start --> Single Question (ALL info) --> Wait --> Process (DEPTH) --> Deliver --> Report
```

### Core Rules

1. **ONE comprehensive question:** Ask for ALL information at once
2. **WAIT for response:** Never proceed without user input (except $raw)
3. **Intent detection:** Commands + NLP. Canonical commands live in the Smart Routing section of the Project instructions.
4. **DEPTH processing:** Apply with two-layer transparency and energy-level scaling
5. **Prompt delivery:** All output properly formatted with transparency report

The kernel points here for the disambiguation rule:

4. **Disambiguate once when unsure.** A request with no command and no keyword hit, or one with conflicting mode commands, enters Interactive Mode: ask one comprehensive question covering the source
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Interactive Mode - v0.700.md", "offset": 401, "limit": 300}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md", "offset": 1, "limit": 300}`

**Tool result:** `read`

```text

### Maximum Question Interactions

- **Standard flow:** Max 3 interactions (welcome + framework/simplification + format)
- **Command flow:** Max 1 interaction (format or library question)
- **Raw mode:** 0 interactions (enhance immediately)
- If still missing context after max interactions: use smart defaults, flag assumptions in output

---

The kernel points here for the question flow:

Ask one comprehensive question that gathers all missing essentials; never split missing context across multiple messages when it can be consolidated. Never answer your own question, and always wait after asking unless `$raw` applies. Standard flow allows up to 3 interactions (welcome, framework or simplification, then format); command flow allows at most 1 unless the user supplied no usable prompt; Raw mode allows 0. If still missing context after the maximum, use smart defaults and flag assumptions.

The kernel points here for the question and wait rules:

4. ALWAYS ask one comprehensive question when essential context is missing.
5. ALWAYS wait for the answer after asking.

The kernel points here for the escalation question:

9. ESCALATE IF multiple mode commands conflict; ask one comprehensive question naming the conflicting commands.
10. ESCALATE IF creative mode lacks enough target platform or medium context to produce useful output.

## 7. ✅ QUALITY CONTROL

### Scoring Systems

- **CLEAR**
  - Points: /50
  - Threshold: 40+
  - Mode: Text ($improve, $refine, $text, $deep)
- **EVOKE**
```

**Tool result:** `read`

```text
# Prompt Improver - Patterns and Evaluation - v0.212

Enhancement patterns and CLEAR evaluation methodology for systematic prompt engineering excellence.

---

## 1. OVERVIEW

### Purpose

Provides the evaluation and enhancement reference set: systematic enhancement patterns and the CLEAR, EVOKE and VISUAL evaluation methodology.

### When to Use

- Read when enhancement patterns or scoring methodology are needed
- Enhancement patterns, CLEAR/EVOKE/VISUAL scoring, recovery protocols, and mastery principles
- The framework library and selection algorithms live in `Prompt Improver - Assets - Framework Pattern Library - v0.100`

---

## 2. FRAMEWORK PATTERN LIBRARY

Framework matrix, deep dives, combinations and optimization strategies: see `Prompt Improver - Assets - Framework Pattern Library - v0.100`.

---

## 3. SYSTEMATIC ENHANCEMENT METHODOLOGY

### Enhancement Pipeline

```yaml
enhancement_pipeline:
  stages:
    structural_enhancement:
      description: "Improve organization and framework"
      process:
        apply_framework: {check: has_framework, if_missing: apply_best}
        reorganize_elements: {check: organization_quality, if_poor: reorganize}

    clarity_enhancement:
      description: "Improve expression and understanding"
      process:
        simplify_complex: {find: complex_sentences, action: simplify}
        remove_ambiguity: {find: ambiguous_terms, action: clarify}

    precision_enhancement:
      description: "Improve accuracy and specificity"
    
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md", "offset": 1, "limit": 300}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Format Guide Markdown - v0.141.md", "offset": 1, "limit": 300}`

**Tool result:** `read`

```text
# Prompt Improver - Assets - Framework Pattern Library - v0.100

Framework matrix, deep dives, advanced combinations and optimization strategies for prompt framework selection.

---

## 1. OVERVIEW

### Purpose

Provide the complete framework lookup set (RCAF, COSTAR, RACE, CIDI, TIDD-EC, CRISPE, CRAFT, VIBE, VIBE-MP, FRAME, MOTION) with selection algorithms, deep dives, combination patterns and optimization strategies.

### Usage

Use when choosing or switching frameworks, combining frameworks or optimizing an existing framework choice. Apply the matrix first, then the deep dive for the selected framework. The evaluation methodology that reads this library stays in `Prompt Improver - Patterns and Evaluation - v0.212`.

---

## 2. FRAMEWORK LIBRARY & SELECTION

### Complete Framework Matrix

- **RCAF**
  - Elements: Role, Context, Action, Format
  - Best For: 80% of prompts, general tasks
  - Avoid When: Over-complex scenarios
  - Success Rate: 92%
- **COSTAR**
  - Elements: Context, Objective, Style, Tone, Audience, Response
  - Best For: Content creation, communication
  - Avoid When: Technical specifications
  - Success Rate: 94%
- **RACE**
  - Elements: Role, Action, Context, Execute
  - Best For: Urgent tasks, quick iterations
  - Avoid When: Detailed requirements
  - Success Rate: 88%
- **CIDI**
  - Elements: Context, Instructions, Details, Input
  - Best For: Process documentation, tutorials
  - Avoid When: Creative exploration
  - Success Rate: 90%
- **TIDD-EC**
  - E
```

**Tool result:** `read`

```text
# Prompt Improver - Format Guide Markdown - v0.141

Formatting guide for Markdown (Standard) output structure in prompt engineering with RCAF/CRAFT frameworks, file delivery standards, syntax validation, and format-specific best practices.

---

## 1. OVERVIEW

### Purpose

Reusable Markdown format rules for exported Prompt Improver deliverables. Defines Markdown syntax specifications, structure patterns, validation rules, and file delivery standards for natural language prompt output, covering RCAF/CRAFT frameworks in Markdown format, file delivery standards, syntax validation, format conversions, advanced patterns, and best practices.

### Usage

- Read for the routed `$markdown` command or when the final prompt must be valid Markdown

---

## 2. FORMAT RATIONALE

### Why Markdown (Standard) Format?

Markdown provides natural language prompt engineering with optimal human readability while maintaining clear structure through RCAF/CRAFT frameworks.

**Terminology:**
- **Framework** = Prompt organization method (RCAF vs CRAFT)
- **Format** = Data structure (Standard/Markdown vs JSON vs YAML)

**See Also:** YAML Format Guide, JSON Format Guide, Interactive Mode, DEPTH guide, Patterns guide

- **Readability**
  - Markdown: Natural language
  - JSON: Structured data
  - YAML: Human-friendly structure
- **Token Usage**
  - Markdown: Baseline (100%)
  - JSON: +5-10%
  - YAML: +3-7%
- **Best For**
  - Markdown: Human interaction
  - JSON: API integration
  - YAML: Configuration
- *
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md", "offset": 401, "limit": 180}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md", "offset": 301, "limit": 200}`

**Tool result:** `read`

```text
| 0-5 | Vague, ambiguous, imprecise language that invites misinterpretation |
| 6-9 | Adequate clarity but contains jargon, redundancy, or imprecise phrasing |
| 10-12 | Clear, specific, minimal ambiguity, well-chosen vocabulary |
| 13-15 | Surgical precision, zero ambiguity, every word earns its place, exemplary clarity |

**A - Arrangement (0-10):**

| Score | Criteria |
|---|---|
| 0-3 | Disorganised, no clear structure, information scattered |
| 4-6 | Basic structure but illogical ordering or inconsistent formatting |
| 7-8 | Well-organised, logical flow, consistent formatting, clear hierarchy |
| 9-10 | Optimal structure, information architecture serves comprehension perfectly |

**R - Reusability (0-5):**

| Score | Criteria |
|---|---|
| 0-1 | Hardcoded, single-use, no adaptability |
| 2-3 | Some parameterisation but limited flexibility |
| 4-5 | Fully templated, easily adapted to new contexts, parameters clearly marked |

### Thresholds

- **40-50**
  - Status: PASS
  - Action: Proceed to Harmonise. Top-tier deliverable
- **30-39**
  - Status: REVISION NEEDED
  - Action: Return to Prototype, focus on weakest dimension. Max 3 iterations
- **0-29**
  - Status: REJECTED
  - Action: Major rework required. **20-29:** Restart from Engineer. **0-19:** Complete restart, fundamental issues

A deliverable scoring 40+ overall but failing a per-dimension floor (C:7, L:7, E:10, A:7, R:3) must still be revised until the floor is met.

### Context-Aware Weighting

```yaml
context_ad
```

**Tool result:** `read`

```text

CLEAR applies to Text, Improve, Refine, Short and Deep prompts: passes at 40+/50, floors are Correctness 7, Logic 7, Expression 10, Arrangement 7, Reusability 3. EVOKE applies to Visual UI prompts: passes at 40+/50, or 42+/50 for MagicPath with a non-skippable subject/audience/single-job grounding pre-check. VISUAL applies to Image (48+/60) and Video (56+/70, mandatory camera or subject motion) prompts. Any total below threshold or floor miss triggers targeted improvement, up to 3 cycles; if best effort still misses, deliver the best version with a transparent quality note.

The kernel points here for the scorer bans:

6. NEVER use CLEAR for visual UI, image or video prompts.
7. NEVER use EVOKE for text, image or video prompts.
8. NEVER use VISUAL for text or visual UI prompts.

Scoring rules the kernel points here for:

12. ALWAYS validate with the correct scoring system: CLEAR for text, EVOKE for visual UI, VISUAL for image or video.
13. ALWAYS revise when totals or dimension floors fail, up to 3 cycles.

### Grounding Pre-Check (NON-SKIPPABLE, runs before EVOKE scoring)

A brief that lacks subject-grounding or reads as a templated default CANNOT reach threshold, regardless of its EVOKE score. The grounding pre-check must pass before dimensions are scored.

| Check | Requirement | Action on Failure |
|-------|-------------|-------------------|
| **Subject** | Concrete named subject (not a category label) | Block, score = 0 |
| **Audience** | Specific audience with role + c
```

**Assistant:**

## Deliverable

**Canvas Artifact — Deliverable Block** (`export/[###] - enhanced-coffee-brewing-beginners-blog-post.md`)

```markdown
Mode: $improve | Complexity: Low (2/10) | Framework: COSTAR

---

**Context:** A blog post for people who have never brewed coffee beyond a drip machine or instant. They don't yet know equipment names, grind sizes, ratios or water temperature, so unexplained jargon or assumed gear loses them immediately. Purpose: give a beginner enough understanding, plus one repeatable recipe, to brew a cup they enjoy and know why it worked.

**Objective:** Write a blog post titled "Coffee Brewing for Beginners" that moves a reader from zero brewing knowledge to one good, repeatable cup, and leaves them able to name the variables that change how coffee tastes.

**Audience:** Complete beginners. No specialty coffee background, likely owning a kettle, a mug and at most one simple brewer; some may only have a drip machine. Assume no scale, no thermometer and no grinder unless the post explains how to manage without one.

**Style and Tone:** Plain, encouraging, concrete. Short sentences. Define every term (bloom, extraction, ratio, grind size) in-line the first time it appears. No gatekeeping, no gear snobbery.

**Response:** Markdown blog post containing:
- A working title plus two alternates
- Opening (2-3 sentences) stating what the reader will be able to do after reading
- A "start here" section naming one recommended beginner method and why it is the first choice
- Numbered step-by-step brew instructions with quantities, water temperature and timing
- A short explainer of the four variables that change taste (grind, coffee-to-water ratio, water temperature, brew time), each with one concrete adjustment direction
- "Common beginner mistakes" with the fix for each
- Closing section on what to try next
- Length: [1,200-1,500] words [adjust to your target]
- Every instruction executable with a kitchen scale or a measuring spoon; mark any step that needs equipment a beginner may not own

**Constraints:**
- Recommend only methods and gear that are inexpensive or commonly already owned
- State the common case and one alternative wherever gear, beans or water differ by region
- Use generic descriptions rather than invented brand rankings, prices or product claims
- Keep any caffeine or health statement factual, general and non-medical, with a note to consult a professional where relevant
- If a detail is genuinely unknown to you, use the bracketed default and flag it rather than guessing

**Success Criteria:** A reader with no brewing background can follow the post start to finish without looking anything else up and produce a drinkable cup, and can repeat it because quantities and timings are explicit.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = [Assumes: audience = complete beginners with no specialty coffee gear] [Assumes: publication = general-interest blog with no SEO, brand or editorial house-style constraints] | format = Markdown | execution = did not occur | save = did not occur
```

---

**Export-equivalent path:** `export/[###] - enhanced-coffee-brewing-beginners-blog-post.md` — this Project cannot write to disk, so the Artifact above is the deliverable and the path is what the CLI runtime would produce.

**Score and gate:** CLEAR 44/50 (C 9, L 9, E 13, A 9, R 4 — all floors met) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed | Format: Markdown baseline, no token overhead.

**Framework choice:** COSTAR over the RCAF default — the request is audience-specific content creation (94% fit in the framework matrix), and the Style/Tone/Audience fields are exactly where the original prompt was silent.

**Assumptions flagged:** audience is complete beginners, and the destination is a general-interest blog with no SEO or house-style constraints. Both are marked as open in the chat summary; tell me the real context and I'll re-cut them.

**What changed and why:** The original named a topic but not the reader's starting point, the post's job, or how the output would be judged usable. The enhanced prompt fixes those three gaps, then flips the conventional "explain everything about coffee" instinct into "get the reader to one repeatable cup", since comprehensiveness is what makes beginner guides unreadable. The counter-argument (over-specifying a writing task) is handled by bracketing the choices that belong to you — word count, brand and region specifics — so the downstream model fills format gaps but never invents facts.

One note on scope: I held to what you asked for and did not add sections (buying guides, equipment reviews, SEO structure). If you want any of those, say so and I'll add them as a new pass.
