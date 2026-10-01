# PIR-001 turn 2 transcript

**User:** Use short mode. The prompt I want improved is: "Plan seven dinners for a family of four with one vegetarian night and a shared shopping list".

**Tool call:** `read` `{"limit": 300, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PIR-001/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md"}`

**Tool call:** `read` `{"limit": 400, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PIR-001/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md"}`

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

**Tool call:** `read` `{"limit": 200, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PIR-001/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md"}`

**Tool call:** `read` `{"limit": 150, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PIR-001/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md"}`

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
Mode: $short | Complexity: Low (3/10) | Framework: RCAF

---

**Role:** You are a practical home meal planner who builds realistic dinners for households with mixed diets.

**Context:** The household has four people. Seven dinners will be cooked at home across seven consecutive days. Exactly one of those dinners must be fully vegetarian. All ingredients for the week are bought in one shop and come from a single shared list.

**Action:** Plan seven dinners, one for each day of the week, each serving four people, with exactly one dinner fully vegetarian. State which day the vegetarian dinner falls on. Then build one shared shopping list that covers all seven dinners, so that no ingredient appears twice and nothing is missed.

**Format:**
- Seven dinners, Monday through Sunday, each as one line: day, dish name, main ingredients.
- One "Shopping List" section covering all seven dinners, grouped by store section (produce, protein, dairy, pantry, other), with item and quantity for a four-person household per line.
- Dinners and short ingredient notes only. No full recipes, no cooking instructions, no per-day shopping lists.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [format defaulted to Markdown, no format command given; vegetarian night day left to the model to assign and state; dinners are home-cooked and shop bought in one weekly trip; quantities scaled to four servings] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-weekly-meal-plan-generator-prompt.md`

**Score and gate status:** CLEAR 44/50 (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4) | Perspectives: 2 (Prompt Engineering Expert, AI Interpretation Specialist) | Gate passed (threshold 40+, all floors met)

**Summary:** Your one-line request is now an RCAF prompt that keeps exactly what you asked for — seven dinners, four people, one vegetarian night, one shared list — and fixes the two gaps that made the original ambiguous: who the dinners are for in quantity terms, and how the shopping list relates to the dinners (one consolidated list, not seven separate ones). Quick energy meant no new sections were added, so the output stays lean.

Mode conflict resolved as `$short` per your confirmation. Want me to run a `$deep` pass on the same prompt, or extend it with dietary or budget constraints?
