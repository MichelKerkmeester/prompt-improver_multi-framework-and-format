# PIR-002 turn 1 transcript

**User:** Hey, I could use a hand with a draft I have been stuck on all week.

**Tool call:** `ls` `{"path": ".", "limit": 100}`

**Tool call:** `find` `{"pattern": "**/*.md", "path": ".", "limit": 100}`

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

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Interactive Mode - v0.700.md", "offset": 1, "limit": 300}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md", "offset": 1, "limit": 300}`

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

**Assistant:**

Welcome! I'll help enhance your prompt for maximum effectiveness — share the draft and we'll get unstuck.

**How much depth would you like?**
- **Quick** — lean enhancement with smart defaults, fast turnaround
- **Think longer and read more context** — deep, full DEPTH with maximum rigour
- (No preference defaults to Standard)

**Please share:**
- Your current draft prompt (paste it as-is, rough edges and all), or
- A description of what you need the AI to do, if there's no prompt yet

**Your depth choice (Quick / Think longer) and your draft or request:**
