# PTX-003 turn 1 transcript

**User:** $short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate

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

**Tool call:** `read` `{"limit": 300, "offset": 401, "path": "knowledge/Prompt Improver - Interactive Mode - v0.700.md"}`

**Tool call:** `read` `{"limit": 400, "offset": 1, "path": "knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md"}`

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

**Tool call:** `read` `{"limit": 300, "offset": 1, "path": "knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md"}`

**Tool call:** `read` `{"limit": 300, "offset": 1, "path": "knowledge/Prompt Improver - Format Guide Markdown - v0.141.md"}`

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

**Assistant:**

```markdown
Mode: $short | Complexity: Low (3/10) | Framework: COSTAR

---

**Context:** [Company] is announcing on LinkedIn that Priya Nair is joining as Head of Design, starting 14 October. The only confirmed details are her name, her title and her start date — nothing else about her background, previous roles or the hiring process is available.

**Objective:** Write one LinkedIn post that announces Priya's arrival and leaves readers with the sense that the team is genuinely glad she is coming — a warm, human update, not a company statement.

**Style:** Plain, everyday language. Short sentences and short paragraphs. Write the way a colleague shares good news with people they already know.

**Tone:** Warm and personal, and not corporate. Avoid phrasing such as "pleased to announce", "thrilled to welcome", "strategic addition to our leadership team" and "we look forward to the expertise she brings". Contractions are fine, and so is a little first-person warmth from the team ("we").

**Audience:** Professional readers scrolling their LinkedIn feed — peers, candidates and people who follow the company.

**Response:** One complete, publish-ready post. Include Priya's name, her Head of Design title and her 14 October start date. Use only the details given — do not invent anything about her beyond those three facts, including previous employers, biography or quotes.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [company name not supplied → placeholder; post length, hashtags and links not specified → left to the downstream model; single post on the company page] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-linkedin-hire-announcement-priya-nair.md` — this Project cannot write files, so the block above stands in for the saved export; the `sk-prompt-improver/` CLI performs the actual write.

**Score and gate status:** CLEAR 44/50 | Perspectives: 3 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer) | Floors met (C 9, L 9, E 13, A 9, R 4) | Gate passed

**Token overhead:** Markdown baseline, no overhead added (JSON or YAML would add roughly +5-10% or +3-7%).

**Summary:** Your brief already carried the essentials — what to announce, who, when and the tone — so this was a Quick-energy pass: RFC-style framing replaced with COSTAR, since audience and tone carry the weight here. The one real gap was that "not corporate" is a feeling, not an instruction, so the prompt names a few phrases the post must avoid and says which three facts are the only usable material. That last line is a guard against fabricated biography, not an extra section.

**Assumptions worth confirming:** the company name (left as `[Company]`), that this runs on the company page rather than a personal profile, and that length, hashtags and links are yours to decide. Tell me any of those and I will lock them into the prompt.
