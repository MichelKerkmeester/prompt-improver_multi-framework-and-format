# PTX-004 turn 1 transcript

**User:** $refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."

**Assistant:**

I'll start by reading the routed knowledge docs for a `$refine` request (Refine Mode → CLEAR scorer, standard energy), plus the DEPTH and Interactive docs that always load.

**Tool call:** `ls` `{"path": "."}`

**Tool call:** `ls` `{"path": "knowledge"}`

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

**Tool call:** `read` `{"limit": 200, "offset": 301, "path": "knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md"}`

**Tool call:** `read` `{"limit": 250, "offset": 1, "path": "knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md"}`

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

**Tool call:** `read` `{"limit": 200, "offset": 1, "path": "knowledge/Prompt Improver - Format Guide Markdown - v0.141.md"}`

**Tool call:** `read` `{"limit": 200, "offset": 251, "path": "knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md"}`

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

**Tool result:** `read`

```text
    primary: "[Main task]"
    method: "[How to accomplish]"
    outcome: "[Expected result]"
  format:
    structure: "[Organization pattern]"
    style: "[Tone and approach]"
    deliverables: "[Specific outputs]"
```

**RCAF Pattern Summary:**

- **Layered RCAF**
  - Key Feature: Multi-level context stacking
  - When to Use: Complex multi-audience prompts
- **RCAF + Metrics**
  - Key Feature: Embedded success criteria
  - When to Use: Measurable outcome prompts
- **Conditional RCAF**
  - Key Feature: If-then role variations
  - When to Use: Context-dependent responses

### COSTAR Enhancement Techniques

**Style-Tone Matrix:**

- **Formal + Empathetic**
  - Use For: Crisis communication
  - Balance: Authority with understanding
- **Technical + Enthusiastic**
  - Use For: Product launches
  - Balance: Expertise with excitement
- **Casual + Authoritative**
  - Use For: Educational content
  - Balance: Approachability with credibility
- **Creative + Professional**
  - Use For: Marketing materials
  - Balance: Innovation with reliability

### TIDD-EC Excellence: Cascading Examples

- **Basic**
  - Description: Simple case
  - Key Elements: Input → output with explanation
- **Intermediate**
  - Description: Typical case
  - Key Elements: Standard input → output
- **Advanced**
  - Description: Complex case
  - Key Elements: Complex input → output
- **Edge Case**
  - Description: Unusual scenario
  - Key Elements: Special handling considerations
- **Anti-Pattern**
  - Description:
```

**Assistant:**

```
Mode: $refine | Complexity: Low (4/10) | Framework: COSTAR

---

**Role:** You are a product copywriter for a webshop. You write understated, fact-led product descriptions that sell through specificity rather than enthusiasm.

**Context:**
- This is a reusable template. `{product_name}` and `{materials}` are the only product facts you are given.
- Earlier runs of this brief came out salesy and too long. Both faults have one cause: praise adjectives and padded sentences filling gaps where no fact exists.
- Why the rules below are hard bans rather than preferences: once hype vocabulary is in a draft it cannot be graded away, and an unverifiable claim cannot be removed without removing the sentence carrying it. Do not generate it in the first place.
- If a detail is needed and not supplied, omit it. Never fill a gap with praise and never invent a fact.

**Objective:** Write one product description for `{product_name}` that helps a shopper understand what the product is and what its materials mean for them, in the fewest words that do the job.

**Style:**
- Professional and understated. Plain declarative sentences, one idea per sentence, no sentence over 20 words.
- Concrete nouns and verbs over adjectives. At most one adjective per noun.
- Every adjective must be traceable to `{materials}` or `{product_name}`. An adjective you cannot source from the inputs is deleted, not softened.
- Prefer a fact to an adjective: "brushed organic cotton" beats "incredibly soft".

**Tone:**
- Calm, factual, quietly confident. Zero hype.
- No exclamation marks, ever.
- Never flatter the shopper's taste or address their emotions.

**Audience:**
- `{target_audience}` — currently "everyone". Assume a general shopper who does not know the product and is deciding quickly. No jargon, no assumed expertise.
- Because the audience is broad, the copy cannot lean on a shared in-group vibe. It has to work through facts alone.

**Response (output requirements):**
1. Length: 80-120 words total, hard cap 120. No paragraph longer than two sentences. This is a mobile-first description read on a phone before the decision.
2. Structure: one factual opening line saying what `{product_name}` is; one or two sentences stating the materials from `{materials}` and what they practically mean for the buyer (durability, feel, care, use); one short closing line.
3. The closing line is the call to action. Keep it plain and low-pressure: name the next step, do not push it.
4. State `{materials}` explicitly, as fact.

**Banned outright (any instance fails the output):**
- Hype vocabulary: amazing, incredible, stunning, revolutionary, game-changing, must-have, ultimate, perfect, premium-quality, best-in-class, unbeatable, luxury, elevate, transform.
- Superlatives and unverifiable claims: "the best", "world-class", "unlike anything else".
- Urgency or scarcity: "limited time", "act now", "don't miss out", "while stocks last".
- Emotional appeals: "you'll love it", "you deserve this", "treat yourself".
- Exclamation marks, rhetorical questions, punchy sales fragments after a dash.
- Any sentence whose only job is to praise the product.

**Check before you output:** count the words; if over 120, cut the weakest claim rather than compressing every sentence. Scan for every banned item. If a claim is not supported by `{product_name}` or `{materials}`, delete it.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = understated tone wins the contradiction; 80-120 word cap chosen as the "too long" fix; audience parameterised with "everyone" as default | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/004 - enhanced-webshop-product-description-prompt.md` (this Project cannot write files; the block above is the deliverable).

**Score and gate status:** CLEAR 44/50 (C 9, L 9, E 13, A 9, R 4) | Floors passed | Perspectives: 4 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture) | Complexity: Low (4/10) | Gate passed

**Token overhead:** not applicable — Markdown is the baseline format.

**What changed and why.** The prompt contained the source of both symptoms: "Be enthusiastic and exciting!! Use lots of adjectives" directly contradicted "Keep it professional and understated", and "around 300 words but short enough to read on mobile" gave no usable cap, so the model defaulted to the largest number it saw. Three moves fix it: the contradictory instruction is deleted so the tone has one voice, adjectives are now sourced from facts or removed (hype is what reads as salesy, and the model generates it when it has no facts to work with), and the length is one countable number with a mobile constraint attached. The banned list is deliberately concrete because "don't be salesy" is a preference the model can satisfy in its own judgment, while "no exclamation marks, no superlatives" is checkable.

**Assumptions to confirm or overturn[Assumes: ...]:**
1. **[Assumes: the understated half of the instruction is what you want]** You gave both "enthusiastic and exciting" and "professional and understated", and complained the output is salesy, so the enthusiasm instruction was cut rather than reworded. If you want energy back, the replacement is specific facts stated with confidence, not adjectives.
2. **[Assumes: 80-120 words is the right length]** You said "around 300 words" in the old prompt and "too long" in your message. 300 was cut decisively; changing the single number in Response item 1 tunes it back toward 150-200 if that is closer to your page layout.
3. **[Assumes: audience stays "everyone"]** `{target_audience}` is parameterised with your current value as the default, so nothing about your targeting changed — but a general audience is the reason the copy cannot lean on insider tone, and naming a segment here would quicken the copy further.
4. Not added: benefits, differentiators or feature fields. Those would have changed your input schema, so instead the prompt forbids inventing them and lets the wording stay inside `{product_name}` and `{materials}`.
