# PFM-001 turn 1 transcript

**User:** $improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".

**Tool call:** `ls` `{"path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001", "limit": 100}`

**Tool call:** `find` `{"path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001", "pattern": "**/*.md", "limit": 100}`

**Tool result:** `ls`

```text
Custom Instructions.md
knowledge/
```

**Tool result:** `find`

```text
Custom Instructions.md
knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md
knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md
knowledge/Prompt Improver - Assets - Video Mode Library - v0.101.md
knowledge/Prompt Improver - Assets - Visual Mode Library - v0.110.md
knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md
knowledge/Prompt Improver - Format Guide JSON - v0.142.md
knowledge/Prompt Improver - Format Guide Markdown - v0.141.md
knowledge/Prompt Improver - Format Guide YAML - v0.142.md
knowledge/Prompt Improver - Image Mode - v0.123.md
knowledge/Prompt Improver - Interactive Mode - v0.700.md
knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md
knowledge/Prompt Improver - Video Mode - v0.123.md
knowledge/Prompt Improver - Visual Mode - v0.301.md
```

**Tool call:** `read` `{"path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md", "offset": 1, "limit": 400}`

**Tool call:** `read` `{"path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Format Guide JSON - v0.142.md", "offset": 1, "limit": 400}`

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
# Prompt Improver - Format Guide JSON - v0.142

Formatting guide for JSON output structure in prompt engineering with RCAF/CRAFT frameworks, file delivery standards, syntax validation, and format-specific best practices.

---

## 1. OVERVIEW

### Purpose

Reusable JSON format rules for exported Prompt Improver deliverables. Defines JSON syntax specifications, structure patterns, validation rules, and file delivery standards for prompt engineering output, covering JSON fundamentals, RCAF/CRAFT JSON structures, file delivery standards, syntax validation, format conversions, advanced patterns, and best practices.

### Usage

- Read for the routed `$json` command or when the final prompt must be valid JSON

---

## 2. FORMAT RATIONALE

### Why JSON Format?

JSON provides structured, machine-parseable prompt engineering with consistent field access and programmatic integration capabilities.

**JSON Format Benefits:**
- **Structured Data:** Clear field separation and hierarchy
- **API Integration:** Direct compatibility with systems
- **Consistent Parsing:** Reliable field extraction
- **Type Safety:** Explicit data types
- **Validation:** Schema-based verification

- **Readability**
  - Markdown: Natural language
  - JSON: Structured data
  - YAML: Human-friendly structure
- **Token Usage**
  - Markdown: Baseline
  - JSON: +5-10%
  - YAML: +3-7%
- **Best For**
  - Markdown: Human interaction
  - JSON: API/System integration
  - YAML: Configuration
- **Framework Fit**
  - Markdown:
```

**Tool call:** `read` `{"limit": 400, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md"}`

**Tool call:** `read` `{"limit": 400, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md"}`

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

**Tool call:** `read` `{"limit": 300, "offset": 1, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Interactive Mode - v0.700.md"}`

**Tool call:** `read` `{"limit": 200, "offset": 400, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md"}`

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

**Tool result:** `read`

```text
  input: [prompt, mode]  # mode: "image" or "video"

  dimensions:
    vivid: {weight: 15, checks: [specific_subject, concrete_details, sensory_elements]}
    intentional: {weight: 10, checks: [defined_composition, clear_hierarchy, purpose_evident]}
    styled: {weight: 10, checks: [art_style_defined, consistent_aesthetic, technique_mentioned]}
    unambiguous: {weight: 10, checks: [no_conflicting_styles, single_interpretation, consistent_mood]}
    atmospheric: {weight: 10, checks: [lighting_defined, mood_conveyed, color_palette_implied]}
    layered: {weight: 5, checks: [foreground_background, depth_of_field, spatial_relationships]}
    motion: {weight: 10, video_only: true, checks: [camera_movement, subject_motion, temporal_pacing]}

  process:
    - determine_mode
    - score_each_dimension: [0-max_weight]
    - calculate_total
    - apply_threshold: 48 (image) or 56 (video)
```

### Common VISUAL Fixes

- **Vague subject**
  - Impact: -5 Vivid
  - Fix: Specific subject with details
- **No composition**
  - Impact: -4 Intentional
  - Fix: Shot type + framing
- **Missing style**
  - Impact: -4 Styled
  - Fix: Art style or medium
- **Conflicting terms**
  - Impact: -5 Unambiguous
  - Fix: Choose dominant style
- **No lighting**
  - Impact: -4 Atmospheric
  - Fix: Lighting direction + quality
- **No motion (video)**
  - Impact: -6 Motion
  - Fix: Camera movement + action verbs

---

The kernel points here for the quality gate detail:

Scoring scales are calibrated per domain
```

**Tool call:** `read` `{"limit": 200, "offset": 301, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Interactive Mode - v0.700.md"}`

**Tool result:** `read`

```text
  $text: { aliases: [$t], energy: standard }
  $json: { aliases: [$j], set_format: json }
  $yaml: { aliases: [$y], set_format: yaml }
  $markdown: { aliases: [$md, $m], set_format: markdown }
process:
  - scan_input_for_command
  - if_found: route_to_appropriate_state
  - if_not_found: use_comprehensive_question
  - wait_for_response (except $raw)
```

### Trigger Detection Logic

```yaml
trigger_detection:
  step_1_scan_input:
    - Check for: command shortcuts, mode keywords, format keywords, prompt content

  step_2_classify:
    command_detected: route_to_command_state
    keywords_detected: infer_mode_from_keywords
    prompt_only: use_comprehensive_question
    ambiguous: ask_clarifying_question

  step_3_acknowledge:
    - Confirm detected intent, ask only what is missing
```

---

## 5. CONVERSATION LOGIC

### Processing Pipeline

```yaml
process_input:
  1_detect_intent: [scan_for_commands, scan_for_keywords, extract_intent_and_prompt]
  2_apply_cognitive_rigour: [multi_perspective_analysis, perspective_inversion, assumption_audit]
  3_route: { improve/short: format_question, refine: refinement_focus, visual: library_question, image/video: mode_processing, text/none: comprehensive_question }
  4_wait_and_parse: [wait_for_response, parse_information, validate_completeness]
  5_process_and_deliver: [apply_DEPTH, show_updates, deliver_artifact, show_report]

intelligent_parser:
  detect: [complexity, task_type, domain, clarity_level]
  extract: [core_functionality, suc
```

**Tool call:** `read` `{"limit": 180, "offset": 501, "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/prompt-improver/project/PFM-001/knowledge/Prompt Improver - Interactive Mode - v0.700.md"}`

**Tool result:** `read`

```text

22. ALWAYS surface critical assumptions as `[Assumes: ...]`.

## 8. FORMATTING RULES

### Critical Requirements

**MUST:**
1. Use markdown dashes `-` for bullets (never emoji bullets)
2. Each bullet on separate line (never compress to single line)
3. Preserve multi-line structure
4. Bold headers followed by content: **Header:**
5. Empty lines between sections
6. No emojis in questions
7. Proper capitalisation throughout
8. Defaults in brackets: [default: Markdown]

**MUST NOT:** Emoji bullets (PROHIBITED), single-line compression, self-answer questions, stack questions without separation, skip waiting for input (except $raw), chatty filler language.

Question-formatting rules the kernel points here for:

14. NEVER use emoji bullets in question or validation text.
15. NEVER compress a required multi-line clarifying question into one line.

### Formatting Enforcement

```yaml
enforcement:
  critical_violations:
    - emoji_bullets_detected: reject_and_reformat
    - single_line_compression: reject_and_expand
  major_violations:
    - missing_line_breaks: add_proper_breaks
  action: automatic_rejection_before_sending
```

See Format Guide for JSON, YAML, and Markdown output standards.

---

## 9. QUICK REFERENCE

### Command Summary

**Energy Levels:**

- **$raw**
  - Alias: -
  - Perspectives: 0
  - Energy: raw
  - Validation: None
  - Output: Prompt only
- **$short**
  - Alias: $s
  - Perspectives: 3-5
  - Energy: quick
  - Validation: Standard
  - Output: + Brief report
- **
```

**Assistant:**

```
Mode: $improve | Complexity: Low (2/10) | Framework: RCAF | Format: JSON

---

{
  "role": "Meeting analyst who turns raw meeting transcripts into an accurate action-item list with named owners and due dates",
  "context": {
    "input": "A meeting transcript supplied in full by the user, with the meeting date when the user provides one",
    "why_it_matters": "Owners and due dates are what make action items accountable, so a fabricated owner or date is worse than an empty one, and every item the reader cannot trace back to the transcript weakens their trust in the whole list",
    "situation": "Transcripts are conversational: commitments are scattered across turns, stated indirectly, and are sometimes left with no owner or no date at all",
    "constraints": [
      "Draw on the transcript only; never add an action item, owner or date the text does not support",
      "Extract every action item in the transcript once, merging repeated references to the same task",
      "Keep decisions, opinions and general discussion out of the list"
    ]
  },
  "action": {
    "primary": "Read the transcript end to end, then list each action item with its owner and due date",
    "requirements": [
      "State each action as a concrete task to be done, not a topic or a discussion point",
      "Name the owner as the transcript names them; where no owner is stated, use \"Unassigned\" and keep the item",
      "Give each due date as a calendar date in YYYY-MM-DD form, converting relative wording such as \"next Friday\" against the meeting date; where the meeting date is unavailable or no date is stated, use \"No date set\" and keep the item"
    ]
  },
  "format": {
    "structure": "JSON object with one top-level key \"action_items\" whose value is an array of objects",
    "fields": {
      "action": "string, the task to be done, phrased as an instruction",
      "owner": "string, the person or team responsible, or \"Unassigned\"",
      "due_date": "string, a calendar date as YYYY-MM-DD, or \"No date set\""
    },
    "requirements": [
      "Return valid JSON only, with no text before or after it",
      "Use these exact field names and add no other keys",
      "If the transcript contains no action items, return {\"action_items\": []}"
    ]
  }
}

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide JSON] | assumptions = [transcript pasted in full as the next message; JSON is consumed by a person or system; "Unassigned"/"No date set" sentinels acceptable; meeting date supplied when relative dates need resolving] | format = JSON | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-meeting-transcript-action-items.json`

**Score and gate status:** CLEAR 45/50 | Perspectives: 5 | Gate passed (floors met: C 9, L 9, E 14, A 9, R 4)

**Token overhead:** JSON runs roughly +8% versus the Markdown baseline, consistent with the +5-10% band for this format.

**Summary:** The original one-liner left the model free to invent owners and dates. The enhanced prompt fixes the role, states the faithful-to-transcript rule, and settles the three cases that otherwise produce garbage: tasks with no stated owner, tasks with no stated date and relative dates. It also closes the output shape, so the result parses as JSON with a single `action_items` array.

**Assumptions flagged:** the transcript arrives in full as the next message; a meeting date is provided when relative dates appear; `Unassigned` and `No date set` sentinels are acceptable placeholders; JSON is the intended hand-off format rather than a document for reading. No mode conflict arose, so no clarifying question was needed.
