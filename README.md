# Prompt Improver - Multi-Framework & Format

> Like it? https://buymeacoffee.com/michelkerkmeester

[![GitHub Stars](https://img.shields.io/github/stars/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&logo=github&color=fce566&labelColor=222222)](https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format/stargazers)
[![License](https://img.shields.io/github/license/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&color=7bd88f&labelColor=222222)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&color=5ad4e6&labelColor=222222)](https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format/commits/main)

## 1. SUMMARY

A prompt engineer in a folder: it rewrites a vague or underpowered request into a structured, scored prompt for another AI to run.

It delivers the prompt and never the work the prompt describes. Every prompt lands as a file, and the reply names that file only after it exists on disk.

Runs in any agent CLI that reads `AGENTS.md` and in a claude.ai Project through `claude project/`

**What's inside**

- **Smart Router** - 9 mode commands and 3 format commands matched as exact tokens, keyword scoring on word boundaries and one question when the intent is unclear
- **DEPTH Thinking** - Discover, Engineer, Prototype, Test and Harmonize, run at one of 5 energy levels from Raw passthrough to Deep with all 5 named perspectives
- **Framework Library** - 11 frameworks: RCAF by default, 6 more text structures and 4 creative ones (VIBE, VIBE-MP, FRAME, MOTION)
- **Quality Scoring** - CLEAR passes text at 40/50, EVOKE passes UI briefs at 40/50 (42 for MagicPath), VISUAL passes images at 48/60 and video at 56/70
- **Creative Prompt Modes** - UI briefs for 5 design tools, image prompts for 9 generators and video prompts for 10 video models, each in that platform's own syntax
- **Format Lock** - Markdown, JSON or YAML, with one `Mode:` header line and the prompt body as the only content in the file
- **Verified Delivery** - saved to `export/` and checked on disk before the reply names the path, or rendered as a Deliverable Block inside a claude.ai Project

**Why it earns a place**

- Ask it to write an email and it reframes the job once as a prompt for that email, then refuses if you insist. The benchmark's safety scenario passed on both runtimes
- A framework wins on fit, so an ordinary task gets RCAF and a precision-critical compliance prompt gets TIDD-EC
- Every scored prompt reports its gate result, and a prompt under any dimension floor goes back for up to 3 repair cycles

&nbsp;

## 2. 🎁 OVERVIEW

### THE FOUNDATION

Three building blocks carry a prompt from request to file:

1. **Routing** picks one mode and one output format, on two separate axes

2. **Prompt design** runs DEPTH at the energy the mode sets and builds the draft in the best-fitting framework

3. **Scoring and delivery** apply the mode's gate, keep the locked format and save the result

From request to delivered prompt:

```text
                         YOUR REQUEST
                              │
                              ▼
          ┌──────────────────────────────────────┐
          │             SMART ROUTER             │
          │                                      │
          │  $token exact match, command wins    │
          │  else keyword score, word boundary   │
          │  $json $yaml $markdown: own axis     │
          │  no signal or conflict: one question │
          └───────────────────┬──────────────────┘
                              │
                              ▼
          ┌──────────────────────────────────────┐
          │         DEPTH AND FRAMEWORK          │
          │                                      │
          │  Discover, Engineer, Prototype       │
          │  Test, Harmonize at routed energy    │
          │  3+ perspectives from Standard up    │
          │  RCAF unless another of 11 fits      │
          └───────────────────┬──────────────────┘
                              │
                              ▼
          ┌──────────────────────────────────────┐
          │          SCORE AND VALIDATE          │
          │                                      │
          │  CLEAR 40/50 or EVOKE 40/50          │
          │  VISUAL 48/60 image, 56/70 video     │
          │  a floor on every dimension          │
          │  up to 3 targeted repair cycles      │
          └───────────────────┬──────────────────┘
                              │
                              ▼
          ┌──────────────────────────────────────┐
          │         EXPORT AND READ BACK         │
          │                                      │
          │  export/### - enhanced-[name].md     │
          │  or .json or .yaml, then verified    │
          │  reply: path, score, short summary   │
          └───────────────────┬──────────────────┘
                              │
                              ▼
                      DELIVERED PROMPT
```

### Smart Routing

One request, one mode.

An exact `$` command always beats wording. Without one, keywords score on word boundaries and the highest total wins.

- `$improve`, `$vibe`, `$img` and the rest match only as whole tokens, so `$imgur` selects nothing
- `$improve $json` keeps Improve and writes JSON, because format is its own axis
- Two different mode commands in one request, or no signal at all, get one question instead of a guess

### DEPTH Thinking

Rigor matched to the request.

Five phases, Discover, Engineer, Prototype, Test and Harmonize, run as far as the energy level allows.

- Raw runs no phases and no score
- Quick runs Discover, Prototype and Harmonize with 1 or 2 perspectives
- Standard runs all five with at least 3 of the 5 named perspectives, and Deep requires all 5

### Framework Selection

The right structure, not the fanciest one.

The library holds 7 text frameworks and 4 creative ones.

- RCAF (Role, Context, Action, Format) is the default for ordinary work
- COSTAR, RACE, CIDI, TIDD-EC, CRISPE and CRAFT win when audience, urgency, precision or scale call for them
- Complexity for its own sake never picks a framework

### Creative Modes

Grounded briefs in each platform's syntax.

Visual, Image and Video modes each carry their own framework, platform list and scorer.

- Visual names a concrete subject, audience and single job before any style word, then steers away from the category default
- Image writes FRAME prompts in the syntax of Midjourney, Flux, Stable Diffusion and 6 other generators
- Video refuses a static scene: every MOTION prompt needs camera or subject movement

### Mode-Specific Scoring

A number the prompt has to earn.

Each mode family scores against the gate built for its output.

- CLEAR scores text out of 50, EVOKE scores UI briefs out of 50 and VISUAL scores images out of 60 and video out of 70
- Every dimension has a floor, and missing one triggers revision even when the total passes
- A failed gate gets targeted revision, capped at 3 cycles, then ships with a quality note

### Format Lock

Clean files a tool can load.

Markdown, JSON and YAML each have their own structure rules.

- A saved file holds one header line and the prompt body, nothing else
- Scores, notes and explanations stay in chat
- JSON and YAML get a syntax check before export, and the reply reports their token overhead

### Verified Delivery

Saved first, reported second.

In a CLI, the prompt goes to `export/` and is checked before the reply names it.

- The reply carries the path, the score where the mode has one and a 2 to 3 sentence summary
- The full prompt never appears in chat once the export succeeds
- A claude.ai Project renders a Deliverable Block instead and reports an export-equivalent path

&nbsp;

## 3. 🚀 QUICK START

### Installation

You need Git, Bash, Python 3 and an agent CLI that reads `AGENTS.md`.

```bash
git clone https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format.git
cd prompt-improver_multi-framework-and-format
```

Open the folder in your agent CLI and point the model at `AGENTS.md`. It loads `sk-prompt-improver/SKILL.md` and the two references every request needs, then the rest only when a route calls for it.

### Verify Installation

Run the router check from the repository root. It needs no model and no network.

```bash
bash benchmark/router/run_fixtures.sh
```

Expected output: `PASSED 25/25 fixtures`

### First Use

Start a request with a mode command:

- `$improve tighten this onboarding email prompt` asks for the output format if none is set, then delivers
- `$improve $json tighten this onboarding email prompt` keeps Improve and writes a `.json` file
- `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` delivers a FRAME prompt in Midjourney syntax

The reply names the saved file in `export/` first, then the score and a short summary. The prompt itself stays in the file.

### Use It in a claude.ai Project

1. Create or open a Project named **Prompt Improver**
2. Paste `claude project/Custom Instructions.md` into its custom instructions
3. Upload all 13 files in `claude project/knowledge/` with their filenames unchanged
4. Send a test request and confirm the prompt arrives as a Deliverable Block with an export-equivalent path. [The Project README](claude%20project/README.md) has the full smoke-test list

&nbsp;

## 4. 🧭 MODES AND ROUTING

`sk-prompt-improver/SKILL.md` section 2 is the router. [`benchmark/router/route_contract.py`](benchmark/router/route_contract.py) is its executable copy, and the two must not drift apart.

#### Mode Table

Nine modes have a `$` command. Each one fixes an energy level, a framework family and a scorer.

| Mode | Commands | Energy | Framework | Scorer, pass mark | Notes |
|---|---|---|---|---|---|
| Raw | `$raw` | Raw | none | none | Grammar cleanup only, no questions |
| Text | `$text`, `$t` | Standard | RCAF or COSTAR | CLEAR 40/50 | Standard prompt enhancement |
| Improve | `$improve`, `$i` | Standard | Auto-selected | CLEAR 40/50 | Asks for the format when none is set |
| Refine | `$refine`, `$r` | Standard | Auto-selected | CLEAR 40/50 | Asks what the refinement should focus on |
| Short | `$short`, `$s` | Quick | Auto-selected | CLEAR 40/50 | Shorter DEPTH pass, same gate |
| Deep | `$deep`, `$d` | Deep | Complexity-matched | CLEAR 40/50 | All 5 perspectives and all 5 techniques |
| Visual | `$vibe`, `$v` | Creative | VIBE or VIBE-MP | EVOKE 40/50, 42/50 for MagicPath | Asks for a component library first |
| Image | `$image`, `$img` | Creative | FRAME | VISUAL 48/60 | Platform syntax for 9 generators |
| Video | `$video`, `$vid` | Creative | MOTION | VISUAL 56/70 | Camera or subject motion required |

The route contract knows 14 intents in total. MagicPath has no command and is reached by keyword. Framework, Scoring, Interactive and Thinking are topic routes: they answer a question about the system, so they carry Standard energy and no scorer. Interactive is also the fallback for unclear or conflicting requests.

#### Format Commands

`$markdown` (`$md`, `$m`) locks Markdown, the default when no format command appears. `$json` (`$j`) locks JSON and `$yaml` (`$y`) locks YAML.

A format command never competes with the mode. A bare `$json` still routes the mode to Interactive, with JSON locked for whatever comes next.

#### How the Router Picks a Mode

1. **Tokenize.** Every `$word` in the lowercased request is pulled out whole and checked against the command table by exact membership. `$imgur` is not `$img`
2. **Let one command win.** A single mode command selects its intent outright, whatever the wording says. Two aliases of the same mode (`$s $short`) count as one. Two different mode commands (`$short $deep`) route to Interactive, which asks which one you meant
3. **Score keywords when there is no command.** Each keyword that matches on a word boundary adds its intent's weight, and the highest total wins. `\bask\b` matches "ask a question" but not "basket", and `\bprompt\b` matches "write me a prompt" but not "promptly"
4. **Lock the format on its own axis.** The first `$json`, `$yaml` or `$markdown` token sets the file format. No token means Markdown
5. **Load one lane.** The two always-loaded references, the bound intent's files and, for JSON, YAML or an explicit `$markdown`, the matching format guide. `$improve $json` loads six files: the two DEPTH and interactive references, patterns and evaluation, the framework library and both the Markdown and JSON format guides

With no command and no keyword hit, the request routes to Interactive with `needs_disambiguation` set to true.

Keyword weights run from 7 per hit for MagicPath down to 3 for Interactive and Thinking. The full keyword lists are `INTENT_KEYWORDS` in [`SKILL.md`](sk-prompt-improver/SKILL.md) section 2 and in `route_contract.py`.

#### Precedence, By Example

Every line below is the route contract's own output:

- `$short but this needs a deep and complex multi-step strategic rewrite` routes to Short. The Deep keywords score 15, and the command still wins
- `$short $deep pick one energy level for me` routes to Interactive, because two different mode commands conflict
- `a complex, strategic prompt for our board deck` routes to Deep, which scores 10 against Text's 5
- `design a fintech dashboard concept` routes to Interactive, since the Visual keyword is "ui design"
- `give me this as yaml` routes to Interactive with Markdown, because the word "yaml" is not a format command

To check a route yourself, pass the request in single quotes so the shell leaves `$short` alone:

```bash
python3 benchmark/router/route_contract.py '$short but this needs a deep and complex multi-step strategic rewrite'
```

It prints the route object: intent, energy, scorer, format, source, `needs_disambiguation` and the files the route loads.

#### Confidence Bands

The route contract only records how a route was found: `command`, `semantic` or `fallback`. On top of that, `SKILL.md` gives the model advisory bands for talking about a keyword-based route:

- At 80% mode confidence or higher, it selects the mode and explains briefly if useful
- At 50% to 79%, it suggests the mode and asks for confirmation
- Below 50%, it asks one clarifying question, up to 3 attempts, then uses smart defaults with each assumption flagged as `[Assumes: description]`

A second set, document-routing confidence, uses high at 0.85, medium at 0.60, low at 0.40 and fallback below that. Neither set changes which files load.

#### Interactive Mode

When a request is unclear, the model asks one comprehensive question and waits. It never answers its own question.

- With no command and no signal, the question opens with a depth choice, **Quick** or **Think longer and read more context**, and defaults to Standard when you only send a prompt
- At complexity 5 or 6, it asks for a framework choice between RCAF, COSTAR (about 5 percent more tokens) and TIDD-EC (about 8 percent more)
- At complexity 7 or higher, it asks for a choice between Streamline and Comprehensive
- With no format command, it asks for a choice between Markdown, JSON and YAML
- `$vibe` gets a component library choice between Untitled UI, shadcn/ui and no library
- `$raw` gets no questions at all

The standard flow allows up to 3 interactions (welcome, framework or simplification, then format). A command flow allows 1 and Raw allows none. When context is still missing after that, the prompt ships on smart defaults with every assumption flagged.

In the benchmark's `STX-001` scenario, the request `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` got one question covering depth, target tool, audience, must-include points and format. After the answer "For a general audience blog post, markdown is fine." the reply opened with:

```text
Saved: `export/001 - enhanced-coffee-brewing-blog-post-prompt.md`

CLEAR: 44/50 (target 40+) | Perspectives: 3 applied (Prompt Engineering, AI Interpretation, End-User Experience) | Framework: RCAF | Format: Markdown
```

&nbsp;

## 5. ⚡ DEPTH AND FRAMEWORKS

DEPTH is the only thinking system here: Discover, Engineer, Prototype, Test and Harmonize. The energy level decides how much of it runs, and every phase has an exit gate.

#### The Five Phases

- **Discover** maps what you gave, finds vagueness and scope gaps, rates complexity 1 to 10, runs the perspectives, surfaces assumptions and selects a framework
- **Engineer** generates 8 or more enhancement approaches, applies constraint reversal and keeps the one with the best CLEAR outlook
- **Prototype** builds the draft in the chosen framework and format, with the WHY stated before the WHAT
- **Test** scores with the routed gate and checks that your intent survived. It exits only when the total and every floor pass
- **Harmonize** polishes, checks the format and recounts the perspectives. A short count sends the work back to Discover

#### Energy Levels

- **Raw** (`$raw`) runs no phases, no perspectives and no score
- **Quick** (`$short`, `$s`) runs D → P → H with 1 or 2 perspectives and one technique, then scores with CLEAR
- **Standard** (the default, and `$text`, `$improve`, `$refine`) runs all five phases with at least 3 perspectives, targets 5 and uses 1 or 2 relevant techniques
- **Deep** (`$deep`, `$d` or a complex prompt) runs an extended pass with all 5 perspectives and all 5 techniques
- **Creative** (`$vibe`, `$image`, `$video`) runs an abbreviated pass with mode-specific perspectives and scores with EVOKE or VISUAL

The perspective minimums are blocking: a Standard pass with 2 perspectives or a Deep pass with 4 does not ship.

#### Perspectives and Techniques

[`references/depth-framework.md`](sk-prompt-improver/references/depth-framework.md) names five perspectives. Prompt Engineering Expert, AI Interpretation Specialist and End-User Experience Designer are required from Standard up. Deep also requires Framework Architecture Expert and Token Optimisation Specialist, and Standard aims for all five. Creative energy uses mode-specific perspectives in place of these five.

The same file defines five cognitive techniques: Multi-Perspective Analysis, Perspective Inversion, Constraint Reversal, Assumption Audit and Mechanism First. Quick picks one, Standard and Creative use 1 or 2 and Deep applies all 5. Assumption Audit is where the `[Assumes: description]` flags come from, and Mechanism First puts the WHY before the WHAT inside the prompt.

#### Framework Library

RCAF (Role, Context, Action, Format) is the default for ordinary tasks. Six more text frameworks win on fit: RACE for urgent work, COSTAR for audience-specific content, CIDI for tutorials, CRISPE for strategy, TIDD-EC for precision-critical tasks and CRAFT for complex work with several stakeholders. The four creative frameworks each belong to a mode: VIBE and VIBE-MP to Visual, FRAME to Image and MOTION to Video.

[`assets/framework-pattern-library.md`](sk-prompt-improver/assets/framework-pattern-library.md) lists every framework's elements, and the quick-select card in [`references/patterns-evaluation.md`](sk-prompt-improver/references/patterns-evaluation.md) gives each text framework its complexity band.

#### How a Framework Wins

The library scores candidates from the task's traits and keeps the highest total. The selector returns a primary pick, a confidence, an alternative and its reasoning. RCAF starts at 5 and gains 5 when complexity is 6 or lower and 3 more when the task is not audience-specific. An ordinary task of complexity 4 with no audience angle therefore gives RCAF 13 against COSTAR's 3, which is why RCAF is the usual answer.

&nbsp;

## 6. 🧮 SCORING GATES

Each mode family has its own scorer, and using the wrong one is a rule violation: CLEAR never scores a UI brief, EVOKE never scores text or images and VISUAL never scores text or UI briefs.

#### CLEAR, for Text, Improve, Refine, Short and Deep

CLEAR splits 50 points across Correctness 10, Logic 10, Expression 15, Arrangement 10 and Reusability 5. It passes at 40 and marks excellence at 45. The floors are Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3. Scoring 40 or more with any dimension under its floor still sends the prompt back for revision.

A total of 30 to 39 goes back to Prototype, weakest dimension first. A total of 20 to 29 restarts from Engineer, and anything lower is a complete restart.

The repair cycle runs at most three times: first the weakest dimension, then the remaining gaps, then an alternative framework. If the prompt still misses, the best version ships with a note like `Best result after 3 improvement cycles. CLEAR: [before] to [after].` [`references/depth-framework.md`](sk-prompt-improver/references/depth-framework.md) has the full rubric.

#### EVOKE, for Visual

A grounding pre-check runs first and cannot be skipped. The brief needs a concrete named subject, a specific audience with a role and a context, one falsifiable primary action and a named category default that it steers away from. Any failed check scores the brief 0, however well it reads.

Once grounding passes, Evocative 15, Visual 10, Open 10, Kinetic 10 and Emotional 5 share the 50 points, each with its own floor. Standard EVOKE passes at 40. MagicPath moves points toward Kinetic and Visual, passes at 42 and adds three gate checks: Kinetic at least 8 of 13, Visual at least 8 of 12 and Kinetic plus Visual at least 18 of 25. A total under 30 blocks the brief and asks you for more input. [`references/patterns-evaluation.md`](sk-prompt-improver/references/patterns-evaluation.md) has both weight splits.

After scoring, an anti-default critique gate asks: "Does any part read like the generic default you would produce for any similar brief?" Any part that does gets revised, with a note on what changed.

#### VISUAL, for Image and Video

Image prompts score Vivid 15, Intentional 10, Styled 10, Unambiguous 10, Atmospheric 10 and Layered 5, for 60 points and a pass at 48. Video adds Motion 10 for 70 points and a pass at 56. Every dimension has a floor, and a video prompt with no camera or subject motion fails whatever its other scores.

The usual misses are a vague subject, no composition, a missing style, conflicting terms and no lighting, plus no motion for video. [`references/patterns-evaluation.md`](sk-prompt-improver/references/patterns-evaluation.md) lists what each one costs and how to fix it.

&nbsp;

## 7. 🧾 OUTPUT FORMATS

A format command locks the file's syntax without touching the mode. Every saved file opens with one header line, and nothing follows it but the prompt. CLEAR, EVOKE or VISUAL breakdowns, processing notes and format explanations stay in chat.

#### Format Options

- **Markdown** (the default, or `$markdown`, `$md`, `$m`) uses bold field labels such as `**Role:**` and sets the token baseline
- **JSON** (`$json`, `$j`) takes double quotes only, with no trailing commas, no comments and no Markdown, for about 5 to 10% more tokens
- **YAML** (`$yaml`, `$y`) takes two-space indents, no tabs, `key: value` and `- item`, for about 3 to 7% more tokens

The header line per format:

```text
Markdown   Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT]
JSON       Mode: $json | Complexity: [level] | Framework: [RCAF/CRAFT]
YAML       Mode: $yaml | Complexity: [level] | Framework: [RCAF/CRAFT]
```

The mode carries its `$` prefix. Complexity is either a word (Low, Medium or High) or a number from 1 to 10. The header never carries a score.

#### Markdown

The RCAF example from `assets/format-guide-markdown.md`:

```text
Mode: $improve | Complexity: Medium | Framework: RCAF

**Role:** Financial analyst specializing in SaaS metrics and growth analysis.
**Context:** Q4 2024 revenue data from B2B platform with 10,000 customers, focusing on subscription trends.
**Action:** Calculate MRR growth rate, identify top 3 revenue trends, and provide actionable insights.
**Format:** Executive summary (500 words) with key metrics, trend charts, and 3-5 strategic recommendations.
```

CRAFT adds a `**Target:**` line for success metrics, and the format guides give each framework its own field set.

#### JSON, From a Real Run

The benchmark's `SFM-001` scenario sent this request to the skill:

```text
$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".
```

The router bound Improve by command and locked JSON on its own axis. The reply, in full:

```text
Saved: `export/001 - enhanced-meeting-action-items-prompt.json`
CLEAR: 44/50 | Gate: passed

Used RCAF (fit for this single-task extraction job, Standard energy, 3 perspectives: Prompt Engineering, AI Interpretation, End-User Experience). The prompt now specifies edge-case handling (unassigned owners, unresolved dates via `meeting_date` + relative phrasing, empty-array case), a fixed output schema with `source_context` for traceability, and parameterized `transcript`/`meeting_date` fields for reuse across meetings.
```

The file it saved:

```text
Mode: $json | Complexity: Low | Framework: RCAF

{
  "role": "Meeting operations analyst who converts raw meeting transcripts into structured, assignable action items",
  "context": "Input is a raw meeting transcript with multiple speakers, informal language, interruptions, and tangents. Action items may be stated explicitly (e.g. 'I'll send the report by Friday') or implied (e.g. 'someone should follow up with the client'). Owners are identified by name or role as mentioned in the transcript. Due dates may be explicit dates, relative references (e.g. 'by end of week'), or absent entirely.",
  "action": "Read the full transcript and extract every discrete action item. For each item: state the task as a single clear sentence in imperative mood, identify the owner by name or role exactly as referenced (use 'Unassigned' if no owner is stated or reasonably implied), and resolve the due date to an ISO 8601 date (YYYY-MM-DD) when explicit or inferable from meeting_date plus relative phrasing, otherwise use 'TBD'. Do not invent tasks, owners, or dates unsupported by the transcript. Exclude general discussion points, decisions with no follow-up action, and off-topic remarks.",
  "format": {
    "structure": "JSON array of action item objects",
    "fields": ["task", "owner", "due_date", "source_context"],
    "field_definitions": {
      "task": "Single sentence, imperative mood, describing the concrete action",
      "owner": "Name or role of the responsible person, or 'Unassigned'",
      "due_date": "ISO 8601 date (YYYY-MM-DD) or 'TBD'",
      "source_context": "Short quote or paraphrase from the transcript supporting the extraction"
    },
    "ordering": "Chronological order of first mention in the transcript",
    "empty_case": "If no action items are found, return an empty array"
  },
  "parameters": {
    "transcript": "[PASTE_MEETING_TRANSCRIPT]",
    "meeting_date": "[YYYY-MM-DD, used to resolve relative due dates]"
  }
}
```

A one-line request became a role, edge-case rules, a fixed output schema and two parameters for reuse. The body parses as JSON and passed CLEAR at 44/50. The playbook still marked the run FAIL, because a JSON or YAML deliverable must also report its token overhead in chat, and this reply did not. The benchmark grades the reply as well as the file.

#### YAML

The RCAF example from `assets/format-guide-yaml.md`:

```text
Mode: $yaml | Complexity: Medium | Framework: RCAF

role: Financial analyst specializing in SaaS metrics
context: Q4 2024 revenue data from B2B platform
action: Calculate MRR growth and identify top 3 trends
format:
  structure: executive_summary
  length: 500_words
  include:
    - metrics
    - charts
    - recommendations
```

When a JSON or YAML draft fails its syntax check, the model stops, regenerates in the locked format and checks again before saving.

&nbsp;

## 8. 🎨 CREATIVE MODES

Visual, Image and Video modes run at Creative energy with their own framework, platform list and scorer. All three end by inviting you to share the generated result for another refinement pass.

#### Visual Mode (`$vibe`, `$v`)

VIBE writes UI concept briefs for AI design tools. Before any style word, Step 0 names three grounding anchors. `references/visual-mode.md` shows the gap between a weak and a grounded answer:

- Subject: "a dashboard" becomes "a cold-chain logistics monitoring dashboard for warehouse shift supervisors"
- Audience: "users" becomes "shift supervisors during a 2am temperature excursion alert"
- Single Job: "manage data" becomes "decide within 30 seconds whether to escalate the alert or dismiss it"

If any anchor is missing, the model stops and asks rather than moving on to VIBE. The four VIBE pillars then ask what the design should look like (Vision), what it should feel like (Inspiration), how it should move (Behavior) and how users should feel (Experience).

The same file names eight category defaults, such as Precision & Density (Linear, Raycast) and Data & Analysis (Mixpanel, Amplitude), each paired with a question that pushes the brief away from it. They exist to be named and then deliberately left behind. They are not a style menu, and a direction set reused unchanged across subjects counts as a preset, which is not allowed.

The avoid-list is always active. Every brief names the median it steers away from:

- A generic SaaS gradient, purple to blue across the hero
- A centered hero above three feature cards
- An untouched component-library surface, such as shadcn/ui or Untitled UI with no customization
- Warm cream (about #F4F1EA) with a high-contrast serif and a terracotta accent
- Near-black with one acid-green or vermilion accent
- Broadsheet hairline rules, zero border-radius and dense columns

The pipeline also strips praise words that give no direction (beautiful, modern, trending, stunning, sleek) and build terms that describe how to build rather than what to experience (React, Tailwind, hex codes, pixel values). Every brief gets four UX floors whether you ask or not: responsive layout, visible keyboard focus, respect for `prefers-reduced-motion` and WCAG AA text contrast.

Visual briefs target five platforms: MagicPath.ai for multi-page flows, Lovable for full-stack apps, Aura for no-code contexts, Bolt for rapid prototyping and v0.dev for UI components. Each has its own prompt length, 150 to 400 words for MagicPath and 50 to 150 for Aura and Bolt.

MagicPath gets the VIBE-MP calibration and eight required elements: Product Type, Layout, Interactions, User Context, Visual Style, Constraints, the Avoid-List and a Single Aesthetic Risk justified by the grounding. When you ask for two or more variations, a seed step (a random 12-character string, its ASCII sum, mod N) picks each variation's starting angle from facets of the subject rather than from a style palette.

`assets/visual-mode-library.md` carries a worked MagicPath rewrite. Its input:

```text
dashboard, beautiful, modern, trending, professional, 240px sidebar,
64px header, React, Tailwind CSS, #3B82F6 primary, 8px border-radius
```

The output is a narrative brief for a marketing analytics dashboard, with no pixel values, framework names or hex codes left. It scores 46/50 under MagicPath calibration: Evocative 11/12, Visual 11/12, Open 7/8, Kinetic 12/13 and Emotional 5/5.

#### Image Mode (`$image`, `$img`)

FRAME structures image prompts around five weighted pillars: Focus 30%, Rendering 20%, Atmosphere 20%, Modifiers 15% and Exclusions 15%. `assets/image-mode-library.md` backs them with 30 vocabulary sub-categories, among them shot types, Kelvin lighting temperatures, aspect ratios and positive rephrasing.

The mode writes for 9 platforms: Flux 2 Pro, Imagen 4 / Nano Banana Pro, Runway, Midjourney v6.1, DALL-E 3, Stable Diffusion 3, Seedream, Leonardo and Ideogram 3.0. [`references/image-mode.md`](sk-prompt-improver/references/image-mode.md) lists the words that detect each one and its negative-prompt support. Stable Diffusion always gets a negative prompt, Leonardo accepts one and Midjourney takes a partial one through `--no`. A negative prompt never goes to a platform that ignores it, and quality tags such as "4K, 8K, masterpiece" and "trending on artstation" come out on modern platforms.

One of the library's worked examples turns the input `dragon` into this Midjourney prompt, scored VISUAL 50/60:

```text
Ancient dragon perched atop a crumbling stone tower,
wings folded against storm clouds at twilight,
scales gleaming with deep emerald and gold iridescence,
piercing amber eyes surveying the misty valley below,
epic fantasy illustration, dramatic volumetric lighting,
rain falling through god rays, detailed environment
--ar 16:9 --s 500 --style raw
```

#### Video Mode (`$video`, `$vid`)

MOTION structures video prompts around what moves. Movement carries 30% of the weight and Nuance carries 10%. Origin, Temporal, Intention and Orchestration carry 15% each.

The mode's rules: camera movement comes first, clips stay at 5 to 10 seconds for consistency and negative prompts are left out because most video models ignore them. Text-to-video prompts run 50 to 120 words and image-to-video prompts 20 to 40.

The mode writes for 10 video models: Runway Gen-4/4.5, Sora, Kling 2.5/2.6, Veo 3.1+, Pika 2.5, Luma Ray3, Minimax/Hailuo, Seedance 1.5 Pro, OmniHuman 1.5 and Wan 2.1/2.2. The shortest maximum clip is 5 seconds on Wan and the longest is 5 minutes on Kling. Runway needs a camera prefix such as `Dolly forward:`, and Veo takes audio as an `Audio:` section at the end. [`assets/video-mode-library.md`](sk-prompt-improver/assets/video-mode-library.md) has the full profile for each model.

A static description is a blocker, not a style: "A car on a road" becomes "A car drives along a winding road", and "Person walking" becomes "Tracking shot follows person". The library's Runway example turns `woman walking in forest` into this prompt, scored VISUAL 62/70:

```text
Dolly forward: A woman in a flowing white dress walks slowly through
an ancient redwood forest. Dappled sunlight filters through the canopy,
creating shifting patterns on the forest floor. Her bare feet step
carefully over moss-covered roots.

Camera follows at waist height, maintaining medium shot distance.
Soft morning mist drifts between the massive tree trunks.
Her hair sways gently with each step. Cinematic, dreamlike atmosphere.
```

#### The Share-Back Loop

After a creative prompt ships, the model asks you to run it and share what came back. Each round has a focus, starting with direction for Visual, composition for Image and motion for Video.

&nbsp;

## 9. 📤 EXPORT AND DELIVERY

`AGENTS.md` makes export a blocking step. In a CLI, the prompt is saved and verified before the reply says anything about it.

#### The Export Sequence

1. Generate the enhanced prompt internally
2. Validate it with the routed gate: CLEAR, EVOKE or VISUAL
3. Save it under the next free number in `export/`
4. Verify that the file exists, and for JSON or YAML that it parses
5. Reply with the path, the compact score and a 2 to 3 sentence summary

Showing the prompt before saving, asking whether to save, answering the prompt instead of improving it and pasting the full prompt into chat are all prohibited.

#### File Naming

Numbers are zero-padded and start at `001` in an empty folder:

```text
export/[###] - enhanced-[description].md
export/[###] - enhanced-[description].json
export/[###] - enhanced-[description].yaml
```

`AGENTS.md` gives these examples: `export/001 - enhanced-product-strategy-prompt.md`, `export/003 - enhanced-api-ready-prompt.json` and `export/004 - enhanced-video-motion-prompt.yaml`.

#### Response Lines

The chat side prints progress, validation, assumption, delivery and creative follow-up lines in fixed shapes, so a transcript stays easy to scan:

```text
Phase [D/E/P/T/H] - [name]: [concise finding]
[CLEAR|EVOKE|VISUAL] [score]/[max] | Gate: [passed/revising/best-effort]
[Assumes: description]
Saved: export/[###] - enhanced-[description].[md/json/yaml]
Share the generated result when you want refinement.
```

Beyond the mode and framework in the file's header, the chat reports the perspectives used and the score as proof that the thinking ran. The perspectives and the score never enter the file.

#### Claude Project Delivery

A claude.ai Project cannot write files, so `claude project/Custom Instructions.md` swaps the export for a Deliverable Block rendered as a Canvas Artifact before any commentary. The block has three parts:

- A header, the same single `Mode:` line as a saved file
- A body, the enhanced prompt in the locked format
- An attestation footer listing the docs consulted, assumptions, the format, `execution = did not occur` and `save = did not occur`

The header and footer sit outside the JSON or YAML lock, which applies only to the body. After the block, chat carries the export-equivalent path `export/[###] - enhanced-[description].[md|json|yaml]`, the score and gate status, the token overhead for JSON or YAML, a short summary and, for creative modes, the share-back invitation. The Project never claims it saved, exported or verified anything.

#### Local Output

Generated prompts stay on your machine. The root `.gitignore` ignores everything in `export/` except `.gitkeep` and `export/benchmark/`.

&nbsp;

## 10. 🧪 BENCHMARKS AND CHECKS

Two checks run from a fresh clone with nothing but Bash and Python 3. The rest need a shared toolkit that lives only in the parent monorepo this repository sits inside.

#### Router Fixtures

The router check from Quick Start runs 25 fixtures covering the 9 mode commands, 4 format-command cases, 8 natural-language keyword routes and 4 edge cases, among them a command beating Deep keywords, "ask" inside "basket" and the `$short $deep` conflict. The runner exits 0 only when every fixture matches field for field, and it rejects route objects with unknown or duplicate fields.

#### Report Checks

```bash
bash benchmark/grader/check_report.sh <report-folder>
```

This runs two checks over a captured run:

- `lint_replies.py` holds every reply to the Project's Deliverable Block contract: no claimed save or execution, an attestation footer with both "did not occur" fields, a `Mode:` header, the block before any commentary, no scoring inside the block and no emoji bullets
- `twin_divergence.py` pairs each skill scenario with its Project twin, `SID-001` with `PID-001` and so on, and fails on any pair whose verdicts disagree

The exit code is the number of checks with findings, from 0 to 2. It is 64 without an argument and 66 when the folder does not exist. The script rewrites `deliverable-lint.csv` inside the report folder, so point it at a copy when you want to keep the committed snapshot. Against a copy of the committed run it ends:

```text
        TX-001: skill PASS, Project FAIL
        6 twin(s) agreed, 1 disagreed, 0 not settled, 0 run on one runtime only
      FAILED 1 twin(s) disagreed across runtimes

2 of 2 report checks reported findings
```

The lint half also reports 20 of 21 replies as dirty. Most of that is expected: skill replies carry no Deliverable Block by design, so the Project contract flags every one of them. The run's own README walks through every finding and separates the expected ones from the real defects.

#### The 2026-09-17 Playbook Run

[`benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/`](benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/README.md) holds one run of the manual testing playbook: 14 scenarios, 7 per runtime, on claude-sonnet-5 at medium effort.

| Pair | Tests | Skill | Project |
|---|---|---|---|
| `SID-001` / `PID-001` | Identity handover and the runtime's own delivery contract | PASS | PASS |
| `SIR-001` / `PIR-001` | Two mode commands get one question | PASS | PASS |
| `SIR-002` / `PIR-002` | A no-signal request gets one comprehensive question | PASS | PASS |
| `STX-001` / `PTX-001` | Natural-language improve, CLEAR gate, delivery shape | PASS | FAIL |
| `SFM-001` / `PFM-001` | Independent `$json` lock | FAIL | FAIL |
| `SCR-001` / `PCR-001` | `$image`, FRAME, VISUAL gate, share-back invite | PASS | PASS |
| `SSB-001` / `PSB-001` | Reframe a direct content request once, then refuse | PASS | PASS |

That is 11 PASS and 3 FAIL: 6 of 7 on the skill and 5 of 7 on the Project. The three failures:

- `PTX-001`: the Project reply put a transparency summary before the Deliverable Block
- `SFM-001`: the skill reply left out the JSON token-overhead line, the example in section 7
- `PFM-001`: the Project reply dropped the `Mode:` header line from its JSON block

Four follow-up files sit in the same folder:

- `adjudication.md` classes the `PTX-001` ordering defect as a runtime fault and the missing `Score:` header field as a rule gap
- `sampling.md` scores that pair on 6 samples per side, 5 new runs plus 1 reused. The ordering test failed 0 of 6 skill replies and 4 of 6 Project replies, Fisher exact p = 0.061, which it records as not settled
- `remeasure-tx-001.md` checks the fix that dropped `Score:` from the kernel's header template. Project headers carrying `Score:` fell from 5 of 6 to 0 of 5. Pooled across both rounds, the ordering fault hit 0 of 11 skill replies and 7 of 11 Project replies (p = 0.004), offered as a pooled read rather than a pre-registered one
- `verdict.md` is an independent review that recounted every figure in the record

The scenarios live in [`sk-prompt-improver/manual-testing-playbook/`](sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md).

#### Maintainer Scripts

These compare the Claude Project package against the skill sources, and they do not run from a clone:

- `benchmark/parity/` holds 5 wrappers (`run_parity.sh`, `run_receipts.sh`, `run_receipt_write.sh`, `run_query.sh`, `run_residency.sh`) that exec into a shared sync toolkit in the parent monorepo
- `benchmark/gates/rule_parity.py` checks 6 named rules by counting their phrases on both sides of the 13 declared skill-to-Project pairs, reading that pair list from the same toolkit

From a clone, the wrappers fail with `can't open file` because the toolkit is not there, and `rule_parity.py` exits 2 with `no declared pairs, so no rule could be compared`. The router fixtures and the report checks above are the standalone checks.

&nbsp;

## 11. 🗂️ REPOSITORY STRUCTURE

The repository separates the skill source, the Project package, the checks and the local export folder.

```text
.
├── .gitignore                       keeps export/ local
├── AGENTS.md                        CLI entry point, export protocol, command registry
├── Favicon.jpg                      repository icon
├── LICENSE                          MIT license
├── README.md                        this front page
├── SYNC.md                          manual parity method and dated review notes
├── benchmark/
│   ├── gates/                       rule_parity.py, monorepo only
│   ├── grader/                      reply lint, twin comparison, check_report.sh
│   ├── parity/                      5 wrappers into the shared parity gate, monorepo only
│   ├── reports/                     one captured playbook run, 2026-09-17
│   └── router/                      route_contract.py, fixtures.json (25), run_fixtures.sh
├── claude project/
│   ├── Custom Instructions.md       claude.ai kernel v1.4.7, the Project's router
│   ├── README.md                    Project upload guide
│   ├── kernel-review.json           record of the 2026-07-17 kernel review, read by no tool
│   └── knowledge/                   13 knowledge files written by hand from the skill
├── export/                          generated prompts, kept local
└── sk-prompt-improver/
    ├── SKILL.md                     v1.3.0: identity, router, rules, delivery
    ├── README.md                    skill guide
    ├── description.json             skill metadata
    ├── graph-metadata.json          skill graph edges and intent signals
    ├── references/                  6 operating docs
    ├── assets/                      7 libraries and format guides
    ├── changelog/                   6 releases, v1.0.0.0 to v1.3.0.0
    └── manual-testing-playbook/     14 scenarios in 12 category folders
```

#### Key Files

The skill's 6 references and 7 assets each have a hand-written counterpart in `claude project/knowledge/` carrying the same version number. `references/depth-framework.md` and `references/interactive-mode.md` load on every request. The router loads the other 11 only when the route or the locked format calls for them.

`AGENTS.md` points an agent CLI at the skill. A claude.ai Project reads `claude project/Custom Instructions.md` and the files under `claude project/knowledge/` instead.

&nbsp;

## 12. ❓ FAQ

**Q: Does Prompt Improver do the task in my prompt?**

No. It writes instructions for another AI or tool to do that work. Ask it for an email and it reframes the job once as a prompt for that email, then refuses if you still want the email itself. Code, designs, strategy and content are all out of scope by design.

**Q: Which framework will it choose?**

RCAF for ordinary requests. Another framework wins when the task's traits score it higher, such as COSTAR for audience-specific content or TIDD-EC for precision-critical work. To steer it, name the framework alongside a mode command, as in `$improve use COSTAR for this launch email`. Without a mode command, a request built around framework words, such as "explain the RCAF framework structure", routes to the Framework topic, which explains rather than delivers a scored prompt.

**Q: Can a format command change the selected mode?**

No. Mode and format are separate axes. `$improve $json` keeps Improve and locks the prompt body to JSON.

**Q: I asked for YAML in plain words and got Markdown. Why?**

Only a `$yaml` or `$y` token locks YAML. The word "yaml" in a sentence scores nothing, so `give me this as yaml` routes to Interactive with Markdown as the default format.

**Q: Why did my Visual brief score zero?**

A grounding check failed. Name the concrete subject, the audience in a specific moment and one falsifiable job, then say how the direction departs from its category default.

**Q: Can Quick skip scoring or export?**

No. Quick runs a shorter DEPTH flow with 1 or 2 perspectives, then applies the same CLEAR gate and saves the prompt.

**Q: What happens when a prompt cannot pass after three repair cycles?**

The best version ships with a transparent quality note showing the score before and after, and the gate status reads `best-effort` rather than `passed`.

**Q: What does the claude.ai Project return?**

A Deliverable Block rendered as a Canvas Artifact, with an attestation footer stating that no execution and no save occurred, followed by an export-equivalent path in chat.

**Q: How does the Project package stay in step with the skill?**

By hand. `SYNC.md` sets a four-step method: list each skill file against its Project counterpart, decide which paragraphs apply inside a Project, check which skill files changed more recently than their counterparts and record each review as a dated note. No manifest, lock file or checksum ledger is kept.

&nbsp;

## 13. 🔧 TROUBLESHOOTING

**A plain-language request gets a question instead of a mode**

No router keyword matched: the Visual keyword is "ui design", so "design a fintech dashboard concept" has none. Add the command, such as `$vibe`, or a router keyword such as "ui design".

**The mode does not match your request**

Another intent's keywords scored higher. Use an exact mode command, which always wins.

**`$short $deep` gets a question back**

Two different mode commands conflict. Send one mode command.

**`route_contract.py` ignores the `$short` at the start of a request**

The shell expanded `$short` to nothing inside double quotes. Wrap the request in single quotes.

**A JSON or YAML file contains Markdown syntax**

The wrong format guide ran. Repeat the request with an explicit `$json` or `$yaml`.

**A Video prompt fails its gate**

Camera and subject motion are both missing. Add a camera move and an action verb.

**A Flux or Imagen prompt has no negative prompt**

Both platforms ignore negatives, so this is expected. State what to avoid as a positive description.

**No path or score appears in CLI mode**

The export did not verify. Treat the prompt as undelivered, check that `export/` is writable and rerun.

**The model writes the content instead of a prompt**

The request read as a task. Ask for "a prompt that asks an AI to do X".

**`deliverable-lint.csv` shows a diff after a grader run**

`check_report.sh` rewrites it in place. Restore it from git and run the grader on a copy.

**`run_parity.sh` says `can't open file`, or `rule_parity.py` says `no declared pairs`**

Both need the shared toolkit in the parent monorepo. Use the router fixtures and report checks, which run standalone.

&nbsp;

## 14. 📚 RELATED DOCUMENTS

**System guides**

- **[→ Agent Bootstrap](AGENTS.md)** - CLI entry point, export protocol and command registry
- **[→ Prompt Improver Skill](sk-prompt-improver/SKILL.md)** - router, DEPTH energy, rules, scoring gates and delivery
- **[→ Skill README](sk-prompt-improver/README.md)** - mode and asset guide for the skill folder
- **[→ DEPTH Framework](sk-prompt-improver/references/depth-framework.md)** - phases, energy levels, perspectives and the CLEAR rubric
- **[→ Interactive Mode](sk-prompt-improver/references/interactive-mode.md)** - one-question flow, state machine and templates
- **[→ Patterns and Evaluation](sk-prompt-improver/references/patterns-evaluation.md)** - enhancement patterns, CLEAR, EVOKE, VISUAL and REPAIR
- **[→ Framework Pattern Library](sk-prompt-improver/assets/framework-pattern-library.md)** - 11 frameworks and the selection algorithm
- **[→ Visual Mode](sk-prompt-improver/references/visual-mode.md)** - Step 0 grounding, VIBE, VIBE-MP and EVOKE
- **[→ Image Mode](sk-prompt-improver/references/image-mode.md)** - FRAME and image platform rules
- **[→ Video Mode](sk-prompt-improver/references/video-mode.md)** - MOTION and video platform rules
- **[→ Markdown Format Guide](sk-prompt-improver/assets/format-guide-markdown.md)** - header contract and RCAF and CRAFT in Markdown
- **[→ JSON Format Guide](sk-prompt-improver/assets/format-guide-json.md)** - JSON header and syntax rules
- **[→ YAML Format Guide](sk-prompt-improver/assets/format-guide-yaml.md)** - YAML header and syntax rules
- **[→ Latest Release Notes](sk-prompt-improver/changelog/v1.3.0.0.md)** - v1.3.0.0, the smart-routing hardening release

**Claude Project package**

- **[→ Project Setup](claude%20project/README.md)** - upload steps, file list and change checklist
- **[→ Custom Instructions](claude%20project/Custom%20Instructions.md)** - the claude.ai kernel and Deliverable Block protocol
- **[→ Parity Notes](SYNC.md)** - manual parity method and dated review notes

**Benchmarks and checks**

- **[→ Router Checks](benchmark/router/README.md)** - route object, decision rules and the 25 fixtures
- **[→ Report Grader](benchmark/grader/README.md)** - reply lint and twin comparison
- **[→ Rule Parity Gate](benchmark/gates/README.md)** - rule counts across the skill-to-Project pairs
- **[→ Parity Wrappers](benchmark/parity/README.md)** - wrappers into the shared parity gate
- **[→ 2026-09-17 Playbook Run](benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/README.md)** - results, failures and grader output
- **[→ Manual Testing Playbook](sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md)** - the 14 scenarios and their pass rules
