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

- 🧭 **Smart Router** - 9 mode commands and 3 format commands matched as exact tokens, keyword scoring on word boundaries and one question when the intent is unclear
- 🧠 **DEPTH Thinking** - Discover, Engineer, Prototype, Test and Harmonize, run at one of 5 energy levels from Raw passthrough to Deep with all 5 named perspectives
- 🎯 **Framework Library** - 11 frameworks: RCAF by default, 6 more text structures and 4 creative ones (VIBE, VIBE-MP, FRAME, MOTION)
- 🧮 **Quality Scoring** - CLEAR passes text at 40/50, EVOKE passes UI briefs at 40/50 (42 for MagicPath), VISUAL passes images at 48/60 and video at 56/70
- 🎨 **Creative Prompt Modes** - UI briefs for 5 design tools, image prompts for 9 generators and video prompts for 10 video models, each in that platform's own syntax
- 📦 **Format Lock** - Markdown, JSON or YAML, with one `Mode:` header line and the prompt body as the only content in the file
- 📤 **Verified Delivery** - saved to `export/` and checked on disk before the reply names the path, or rendered as a Deliverable Block inside a claude.ai Project

**Why it earns a place**

- **Scope stays fixed:** ask it to write an email and it reframes the job once as a prompt for that email, then refuses if you insist. The benchmark's safety scenario passed on both runtimes
- **Structure follows the task:** a framework wins on fit, so an ordinary task gets RCAF and a precision-critical compliance prompt gets TIDD-EC
- **Quality is a number:** every scored prompt reports its gate result, and a prompt under any dimension floor goes back for up to 3 repair cycles

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

**Prerequisites**

- Git to clone the repository
- An agent CLI that reads `AGENTS.md` and accepts your model
- Bash and Python 3 for the router check, standard library only
- For claude.ai, a Project that accepts custom instructions and knowledge files

Clone the repository and open it in your agent CLI:

```bash
git clone https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format.git
cd prompt-improver_multi-framework-and-format
```

Point the model at `AGENTS.md`. It loads `sk-prompt-improver/SKILL.md` plus the two references every request needs, `sk-prompt-improver/references/depth-framework.md` and `sk-prompt-improver/references/interactive-mode.md`. From then on the model works as Prompt Improver and loads the rest only when a route calls for it.

### Verify Installation

Run the router fixture check from the repository root:

```bash
bash benchmark/router/run_fixtures.sh
```

Expected output:

```text
PASSED 25/25 fixtures
```

The check needs no model and no network. To see how one request routes, pass it in single quotes so the shell leaves `$short` alone:

```bash
python3 benchmark/router/route_contract.py '$short but this needs a deep and complex multi-step strategic rewrite'
```

```json
{
  "intent": "SHORT",
  "energy": "quick",
  "scorer": "CLEAR",
  "format": "markdown",
  "source": "command",
  "needs_disambiguation": false,
  "resources": [
    "references/depth-framework.md",
    "references/interactive-mode.md",
    "references/patterns-evaluation.md",
    "assets/framework-pattern-library.md",
    "assets/format-guide-markdown.md"
  ]
}
```

The Deep keywords in that request score 15, and the `$short` command still wins.

### First Use

Try one of these requests once the CLI has read `AGENTS.md`:

| Request | Route | What happens first |
|---|---|---|
| `$improve tighten this onboarding email prompt` | Improve, Standard energy, CLEAR | Asks for the output format if none is set, then delivers |
| `$short shorten this support-macro prompt without losing meaning` | Short, Quick energy, CLEAR | A lighter DEPTH pass with 1 or 2 perspectives |
| `$improve $json tighten this onboarding email prompt` | Improve, JSON locked | Writes a `.json` file and reports the token overhead |
| `$vibe design a fintech dashboard concept` | Visual, Creative energy, EVOKE | Asks which component library the brief should name |
| `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` | Image, Creative energy, VISUAL | Delivers a FRAME prompt in Midjourney syntax |
| `$video a Runway clip of rain on a windshield` | Video, Creative energy, VISUAL | Delivers a MOTION prompt with a camera prefix |
| `$raw just fix the grammar` | Raw, no DEPTH | Cleans the text with no questions and no score |

The `$image` row is a scenario from the 2026-09-17 benchmark run. Its complete chat reply:

```text
Saved: `export/001 - enhanced-midjourney-forest-cabin-prompt.md`

VISUAL 53/60 | Gate: passed (Vivid 14, Intentional 9, Styled 9, Unambiguous 9, Atmospheric 9, Layered 5)

Built with FRAME for Midjourney v6.1: a specific cabin/forest subject with clear composition (F), cinematic film-still rendering with lens and film-stock cues (R), layered dawn mist/light atmosphere (A), `--ar 16:9 --s 450 --style raw` plus a light `--no` exclusion list for Midjourney's partial negative support (M/E). Share the generated image if you want another refinement pass.
```

Path first, then the gate line with a per-dimension breakdown, then a short summary that closes with the share-back invitation every creative mode ends on. The prompt itself stays in the file.

### Use It in a claude.ai Project

The Project package gives claude.ai the same router and rules through custom instructions plus knowledge files.

1. Create or open a Project named **Prompt Improver**
2. Paste `claude project/Custom Instructions.md` (kernel v1.4.7, aligned to skill v1.3.0) into its custom instructions
3. Upload all 13 files in `claude project/knowledge/` with their filenames unchanged
4. Smoke-test all ten routed intents plus the Interactive fallback and confirm that each delivered prompt arrives as a Deliverable Block with its attestation footer and an export-equivalent path

Update the instructions and the knowledge files together when the package changes. See [the Project README](claude%20project/README.md) for the file list and the full smoke-test list.

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

| Command | Aliases | Locks |
|---|---|---|
| `$markdown` | `$md`, `$m` | Markdown, the default when no format command appears |
| `$json` | `$j` | JSON |
| `$yaml` | `$y` | YAML |

A format command never competes with the mode. A bare `$json` still routes the mode to Interactive, with JSON locked for whatever comes next.

#### How the Router Picks a Mode

1. **Tokenize.** Every `$word` in the lowercased request is pulled out whole and checked against the command table by exact membership. `$imgur` is not `$img`
2. **Let one command win.** A single mode command selects its intent outright, whatever the wording says. Two aliases of the same mode (`$s $short`) count as one. Two different mode commands (`$short $deep`) route to Interactive, which asks which one you meant
3. **Score keywords when there is no command.** Each keyword that matches on a word boundary adds its intent's weight, and the highest total wins. `\bask\b` matches "ask a question" but not "basket", and `\bprompt\b` matches "write me a prompt" but not "promptly"
4. **Lock the format on its own axis.** The first `$json`, `$yaml` or `$markdown` token sets the file format. No token means Markdown
5. **Load one lane.** The two always-loaded references, the bound intent's files and, for JSON, YAML or an explicit `$markdown`, the matching format guide. `$improve $json` loads six files: the two DEPTH and interactive references, patterns and evaluation, the framework library and both the Markdown and JSON format guides

With no command and no keyword hit, the request routes to Interactive with `needs_disambiguation` set to true.

#### Keyword Weights

Every keyword below matches on word boundaries only.

| Intent | Weight per hit | Keywords |
|---|---:|---|
| MagicPath | 7 | magicpath, magic path, magicpath.ai, multi-page flow, user journey, pathfinding |
| Raw | 6 | raw mode, passthrough, no validation |
| Visual | 6 | visual concepting, design vibe, ui design, lovable, aura, bolt, v0, v0.dev |
| Image | 6 | image prompt, picture, photo, midjourney, dall-e, dalle, stable diffusion, sdxl, flux, flux 2, imagen, nano banana, seedream, ideogram, leonardo, firefly, runway image |
| Video | 6 | video prompt, clip, animation, runway, gen-4, sora, kling, veo, pika, luma, ray3, minimax, hailuo, seedance, omnihuman, wan, motion |
| Text | 5 | text mode, prompt mode, prompt, rcaf, costar |
| Improve | 5 | improve prompt, make better, enhance prompt |
| Refine | 5 | refine this, optimise, optimize, feedback |
| Short | 5 | shorten, concise, quick, fast, minor |
| Deep | 5 | complex, strategic, multi-step, comprehensive, system |
| Framework | 4 | framework, rcaf, costar, tidd-ec, craft, race, cidi, crispe, risen, template, structure |
| Scoring | 4 | clear, evoke, visual, score, quality, rating, evaluate, assessment, points |
| Interactive | 3 | question, clarify, conversation, dialog, gather, ask, interactive |
| Thinking | 3 | depth, phases, energy, cognitive, rigour, rigor, analysis |

#### Precedence, By Example

Every row below is the route contract's own output.

| Request | Routes to | Why |
|---|---|---|
| `$short but this needs a deep and complex multi-step strategic rewrite` | Short, Quick energy | Deep keywords score 15, and a command always wins |
| `$short $deep pick one energy level for me` | Interactive | Two different mode commands conflict |
| `$improve $json tighten this onboarding email prompt` | Improve, format JSON | Format sits on its own axis |
| `$json` | Interactive, format JSON | A format lock alone names no mode |
| `a complex, strategic prompt for our board deck` | Deep | Deep scores 10 against Text's 5 |
| `write a prompt for a moody film-noir portrait photo` | Image | Image scores 6 against Text's 5 |
| `a runway clip of rain on a windshield` | Video | "runway" and "clip" score 12 |
| `design a magicpath multi-page user journey flow` | MagicPath, EVOKE | "magicpath" and "user journey" score 14 |
| `$vibe a magicpath onboarding flow` | Visual by command | Inside Visual mode the MagicPath context selects VIBE-MP and the 42/50 gate |
| `design a fintech dashboard concept` | Interactive | No keyword matches, since the Visual keyword is "ui design" |
| `give me this as yaml` | Interactive, format Markdown | The word "yaml" is not a format command |
| `Please put this in your basket before you leave` | Interactive | "ask" inside "basket" does not match |

#### Confidence Bands

The route contract only records how a route was found: `command`, `semantic` or `fallback`. On top of that, `SKILL.md` gives the model advisory bands for talking about a keyword-based route:

| Mode confidence | Behavior |
|---|---|
| 80% or higher | Selects the mode and explains briefly if useful |
| 50% to 79% | Suggests the mode and asks for confirmation |
| Below 50% | Asks one clarifying question, up to 3 attempts, then uses smart defaults with each assumption flagged as `[Assumes: description]` |

A second set, document-routing confidence, uses high at 0.85, medium at 0.60, low at 0.40 and fallback below that. Neither set changes which files load.

#### Interactive Mode

When a request is unclear, the model asks one comprehensive question and waits. It never answers its own question.

- **No command, no signal:** the question opens with a depth choice, **Quick** or **Think longer and read more context**, and defaults to Standard when you only send a prompt
- **Complexity 5 or 6:** a framework choice between RCAF, COSTAR (about 5 percent more tokens) and TIDD-EC (about 8 percent more)
- **Complexity 7 or higher:** a choice between Streamline and Comprehensive
- **No format command:** a choice between Markdown, JSON and YAML
- **`$vibe`:** a component library choice between Untitled UI, shadcn/ui and no library
- **`$raw`:** no questions at all

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

| Phase | What happens | Exit gate |
|---|---|---|
| Discover | Maps what you gave, finds vagueness and scope gaps, rates complexity 1 to 10, runs the perspectives and surfaces assumptions | Perspectives per energy level, inversion applied, assumptions flagged, framework selected |
| Engineer | Generates 8 or more enhancement approaches, applies constraint reversal and keeps the one with the best CLEAR outlook | 8+ approaches evaluated, requirements mapped |
| Prototype | Builds the draft in the chosen framework and format, with the WHY stated before the WHAT | Structure built, mechanism first, format applied |
| Test | Scores with the routed gate and checks that your intent survived | Total and every floor pass |
| Harmonize | Final polish, format check and a recount of perspectives, which sends the work back to Discover if short | Output metadata present, ready to deliver |

#### Energy Levels

| Energy | Trigger | Phases | Perspectives | Techniques | Scoring |
|---|---|---|---|---|---|
| Raw | `$raw` | None | 0 | None | None |
| Quick | `$short`, `$s` | D → P → H | 1 or 2 | Pick 1 | CLEAR 40/50 |
| Standard | Default, `$text`, `$improve`, `$refine` | D → E → P → T → H | 3 minimum, target 5 | 1 or 2 relevant | CLEAR 40/50 |
| Deep | `$deep`, `$d` or a complex prompt | Extended D → E → P → T → H | All 5 | All 5 | CLEAR 40/50 |
| Creative | `$vibe`, `$image`, `$video` | Abbreviated D → E → P → T → H | Mode-specific | 1 or 2 relevant | EVOKE or VISUAL |

The perspective minimums are blocking: a Standard pass with 2 perspectives or a Deep pass with 4 does not ship.

#### The Five Perspectives

Named exactly as `references/depth-framework.md` defines them.

| # | Perspective | Focus | Required at |
|---:|---|---|---|
| 1 | Prompt Engineering Expert | Frameworks, best practices, patterns, structural optimisation | Standard and Deep |
| 2 | AI Interpretation Specialist | Model understanding, ambiguity detection, token efficiency | Standard and Deep |
| 3 | End-User Experience Designer | Comprehension, usability, reusability, clarity | Standard and Deep |
| 4 | Framework Architecture Expert | RCAF, COSTAR, RACE, CIDI, structural patterns, framework fit | Deep |
| 5 | Token Optimisation Specialist | Conciseness, cost efficiency, minimal overhead | Deep |

Standard needs the first three and aims for all five. Creative energy uses mode-specific perspectives in place of these five.

#### The Five Cognitive Techniques

| Technique | What it does |
|---|---|
| Multi-Perspective Analysis | Reads the prompt from the required perspectives and merges what they find |
| Perspective Inversion | Argues against the chosen approach, then keeps what survives |
| Constraint Reversal | Asks whether the opposite approach works better and applies the smallest useful flip |
| Assumption Audit | Classes each hidden assumption as validated, questionable or unknown, then flags it as `[Assumes: description]` |
| Mechanism First | Puts the WHY before the HOW and the WHAT inside the prompt |

Quick picks one technique, Standard and Creative use 1 or 2 and Deep applies all 5.

#### Framework Library

| Framework | Elements | Pick it for | Complexity band |
|---|---|---|---|
| RCAF | Role, Context, Action, Format | Ordinary tasks, the default | 1 to 4 |
| RACE | Role, Action, Context, Execute | Urgent work and fast iteration | 1 to 3 |
| COSTAR | Context, Objective, Style, Tone, Audience, Response | Audience-specific content and tone | 3 to 6 |
| CIDI | Context, Instructions, Details, Input | Tutorials and process documentation | 4 to 6 |
| CRISPE | Capacity, Insight, Statement, Personality, Experiment | Strategy and exploration | 5 to 7 |
| TIDD-EC | Task, Instructions, Do's, Don'ts, Examples, Context | Precision and compliance | 6 to 8 |
| CRAFT | Context, Role, Action, Format, Target | Complex work with several stakeholders | 7 to 10 |
| VIBE | Vision, Inspiration, Behavior, Experience | Visual UI concepts | Visual mode |
| VIBE-MP | VIBE with MagicPath calibration | MagicPath.ai multi-page flows | Visual mode |
| FRAME | Focus, Rendering, Atmosphere, Modifiers, Exclusions | Image generation | Image mode |
| MOTION | Movement, Origin, Temporal, Intention, Orchestration, Nuance | Video generation | Video mode |

The complexity bands come from the quick-select card in `references/patterns-evaluation.md`.

#### How a Framework Wins

`assets/framework-pattern-library.md` scores candidates from the task's traits and keeps the highest total. The selector returns a primary pick, a confidence, an alternative and its reasoning.

| Framework | Base | Adds | Subtracts |
|---|---:|---|---|
| RCAF | 5 | +5 when complexity is 6 or lower, +3 when not audience-specific | |
| COSTAR | 3 | +7 when audience-specific, +5 with a creative element | |
| RACE | 2 | +8 when urgent, +5 when complexity is 3 or lower | 5 when precision-critical |
| TIDD-EC | 3 | +7 when precision-critical, +5 with compliance needs | |
| VIBE | 2 | +10 for visual UI concepting | 10 when precision-critical |
| VIBE-MP | 2 | +12 when MagicPath is detected, +5 for a multi-page flow, +3 for user journey design | 10 when precision-critical |

An ordinary task of complexity 4 with no audience angle gives RCAF 13 against COSTAR's 3, which is why RCAF is the usual answer.

&nbsp;

## 6. 🧮 SCORING GATES

Each mode family has its own scorer, and using the wrong one is a rule violation: CLEAR never scores a UI brief, EVOKE never scores text or images and VISUAL never scores text or UI briefs.

#### CLEAR, for Text, Improve, Refine, Short and Deep

| Dimension | Points | Weight | Floor | Measures |
|---|---:|---:|---:|---|
| Correctness | 10 | 20% | 7 | Accuracy, no contradictions, valid assumptions |
| Logic | 10 | 20% | 7 | Reasoning flow, cause and effect, conditionals |
| Expression | 15 | 30% | 10 | Clarity, specificity, minimal ambiguity |
| Arrangement | 10 | 20% | 7 | Structure, ordering, hierarchy |
| Reusability | 5 | 10% | 3 | Parameters, template potential |
| **Total** | **50** | | **34** | Pass at 40, excellence at 45 |

| Total | Status | What happens |
|---|---|---|
| 40 to 50 | Pass | On to Harmonize |
| 30 to 39 | Revision needed | Back to Prototype, weakest dimension first |
| 20 to 29 | Rejected | Restart from Engineer |
| 0 to 19 | Rejected | Complete restart |

A total of 40 or more with any dimension under its floor still goes back for revision. The repair cycle runs at most three times: first the weakest dimension, then the remaining gaps, then an alternative framework. If the prompt still misses, the best version ships with a note like `Best result after 3 improvement cycles. CLEAR: [before] to [after].`

#### EVOKE, for Visual

A grounding pre-check runs first and cannot be skipped. Any failed check scores the brief 0, however well it reads.

| Check | Requirement |
|---|---|
| Subject | A concrete, named subject rather than a category label |
| Audience | A specific audience with a role and a context |
| Single Job | One falsifiable primary action |
| Anti-Default | The category default is named, and the brief steers away from it |

Once grounding passes, five dimensions share the 50 points. MagicPath reweights them toward motion and spatial clarity.

| Dimension | Standard points | Standard floor | MagicPath points |
|---|---:|---:|---:|
| Evocative | 15 | 12 | 12 |
| Visual | 10 | 8 | 12 |
| Open | 10 | 8 | 8 |
| Kinetic | 10 | 8 | 13 |
| Emotional | 5 | 4 | 5 |

Standard EVOKE passes at 40. MagicPath passes at 42 and adds three gate checks: Kinetic at least 8 of 13, Visual at least 8 of 12 and Kinetic plus Visual at least 18 of 25.

| EVOKE total | Reading | Action |
|---|---|---|
| 45 to 50 | Excellent | Output after the critique gate |
| 42 to 44 | Good | Output after the critique gate, with minor suggestions |
| 38 to 41 | Adequate | Offer refinement options |
| 30 to 37 | Weak | Iterate |
| 0 to 29 | Insufficient | Block and ask for more input |

After scoring, an anti-default critique gate asks: "Does any part read like the generic default you would produce for any similar brief?" Any part that does gets revised, with a note on what changed.

#### VISUAL, for Image and Video

| Dimension | Points | Floor | Checks for |
|---|---:|---:|---|
| Vivid | 15 | 12 | A specific subject, concrete details |
| Intentional | 10 | 8 | Defined composition, clear purpose |
| Styled | 10 | 8 | A named art style or medium |
| Unambiguous | 10 | 8 | One interpretation, no conflicting styles |
| Atmospheric | 10 | 8 | Lighting, mood, color |
| Layered | 5 | 4 | Foreground, background, depth |
| Motion (video only) | 10 | 8 | Camera movement, subject motion, pacing |

Image prompts total 60 and pass at 48. Video prompts total 70 and pass at 56, and a video prompt with no camera or subject motion fails whatever its other scores.

| Common miss | Cost | Fix |
|---|---|---|
| Vague subject | -5 Vivid | A specific subject with details |
| No composition | -4 Intentional | Shot type and framing |
| Missing style | -4 Styled | An art style or medium |
| Conflicting terms | -5 Unambiguous | Pick the dominant style |
| No lighting | -4 Atmospheric | Light direction and quality |
| No motion (video) | -6 Motion | A camera move and action verbs |

&nbsp;

## 7. 🧾 OUTPUT FORMATS

A format command locks the file's syntax without touching the mode. Every saved file opens with one header line, and nothing follows it but the prompt.

#### Format Options

| Format | Command | Header line | Token overhead | Syntax rules |
|---|---|---|---|---|
| Markdown | Default, `$markdown`, `$md`, `$m` | `Mode: $[mode] \| Complexity: [level] \| Framework: [RCAF/CRAFT]` | Baseline | Bold field labels such as `**Role:**` |
| JSON | `$json`, `$j` | `Mode: $json \| Complexity: [level] \| Framework: [RCAF/CRAFT]` | About 5 to 10% | Double quotes only, no trailing commas, no comments, no Markdown |
| YAML | `$yaml`, `$y` | `Mode: $yaml \| Complexity: [level] \| Framework: [RCAF/CRAFT]` | About 3 to 7% | Two-space indents, no tabs, `key: value` and `- item` |

The mode carries its `$` prefix. Complexity is either a word (Low, Medium or High) or a number from 1 to 10. The header never carries a score.

What a file may hold and what stays in chat:

| In the file | In chat, never in the file |
|---|---|
| The single header line | CLEAR, EVOKE or VISUAL breakdowns |
| The enhanced prompt in the locked syntax | Processing notes and applied steps |
| | Format options and explanations |

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

| Anchor | Not this | This |
|---|---|---|
| Subject | "a dashboard" | "a cold-chain logistics monitoring dashboard for warehouse shift supervisors" |
| Audience | "users" | "shift supervisors during a 2am temperature excursion alert" |
| Single Job | "manage data" | "decide within 30 seconds whether to escalate the alert or dismiss it" |

If any anchor is missing, the model stops and asks rather than moving on to VIBE.

| Pillar | Core question |
|---|---|
| Vision | What should this look like? |
| Inspiration | What should this feel like? |
| Behavior | How should this move? |
| Experience | How should users feel? |

Eight category defaults exist to be named and then deliberately left behind. They are not a style menu, and a direction set reused unchanged across subjects counts as a preset, which is not allowed.

| Category default | Typical references | Deviation question |
|---|---|---|
| Precision & Density | Linear, Raycast | What about this subject makes the compact default wrong? |
| Warmth & Approachability | Notion, Coda | Where does the subject demand edge that comfort would blunt? |
| Sophistication & Trust | Stripe, Mercury | What about this audience means restraint tips into cold? |
| Boldness & Clarity | Vercel | When does bold become brittle for this subject's job? |
| Utility & Function | GitHub, VS Code | Where does pure utility hide the insight this audience needs first? |
| Data & Analysis | Mixpanel, Amplitude | What story does the data tell that a card grid buries? |
| Journey & Flow | Duolingo, Headspace | Where does gamification distract from the single job? |
| Narrative & Story | Apple Pages, Stripe Atlas | What if the subject's story is told best in a single glance, not a scroll? |

The avoid-list is always active. Every brief names the median it steers away from:

- A generic SaaS gradient, purple to blue across the hero
- A centered hero above three feature cards
- An untouched component-library surface, such as shadcn/ui or Untitled UI with no customization
- Warm cream (about #F4F1EA) with a high-contrast serif and a terracotta accent
- Near-black with one acid-green or vermilion accent
- Broadsheet hairline rules, zero border-radius and dense columns

The pipeline also strips praise words that give no direction (beautiful, modern, trending, stunning, sleek) and build terms that describe how to build rather than what to experience (React, Tailwind, hex codes, pixel values). Every brief gets four UX floors whether you ask or not: responsive layout, visible keyboard focus, respect for `prefers-reduced-motion` and WCAG AA text contrast.

| Platform | Strength | Prompt length |
|---|---|---|
| MagicPath.ai | Multi-page flows and iteration | 150 to 400 words |
| Lovable | Full-stack apps | 100 to 250 words |
| Aura | No-code, no-design contexts | 50 to 150 words |
| Bolt | Rapid prototyping | 50 to 150 words |
| v0.dev | UI components | 100 to 300 words |

MagicPath gets the VIBE-MP calibration and eight required elements: Product Type, Layout, Interactions, User Context, Visual Style, Constraints, the Avoid-List and a Single Aesthetic Risk justified by the grounding. When you ask for two or more variations, a seed step (a random 12-character string, its ASCII sum, mod N) picks each variation's starting angle from facets of the subject rather than from a style palette.

`assets/visual-mode-library.md` carries a worked MagicPath rewrite. Its input:

```text
dashboard, beautiful, modern, trending, professional, 240px sidebar,
64px header, React, Tailwind CSS, #3B82F6 primary, 8px border-radius
```

The output is a narrative brief for a marketing analytics dashboard, with no pixel values, framework names or hex codes left. It scores 46/50 under MagicPath calibration: Evocative 11/12, Visual 11/12, Open 7/8, Kinetic 12/13 and Emotional 5/5.

#### Image Mode (`$image`, `$img`)

FRAME structures image prompts, and each pillar carries a weight in the mode reference:

| Pillar | Weight | Core question |
|---|---:|---|
| Focus | 30% | What is the viewer looking at? |
| Rendering | 20% | How should it be visualized? |
| Atmosphere | 20% | What feeling does it evoke? |
| Modifiers | 15% | What constraints apply? |
| Exclusions | 15% | What should be avoided? |

`assets/image-mode-library.md` backs the pillars with 30 vocabulary sub-categories, among them shot types, Kelvin lighting temperatures, aspect ratios and positive rephrasing.

| Platform | Detected by | Negative prompts | Strength | Words |
|---|---|---|---|---|
| Flux 2 Pro | "flux", "bfl" | No, ignored | Photorealism, natural language | 15 to 75 |
| Imagen 4 / Nano Banana Pro | "imagen", "nano banana", "gemini image" | No, ignored | Text rendering, multi-reference | 30 to 100 |
| Runway | "runway", "gen-4 image" | No | Video frame consistency | 30 to 80 |
| Midjourney v6.1 | "midjourney", "mj", `--ar` | Partial, through `--no` | Artistic, stylized | 20 to 60 plus parameters |
| DALL-E 3 | "dall-e", "dalle", "openai" | No, rephrase positively | Prompt following, text | 50 to 150 |
| Stable Diffusion 3 | "sd", "sdxl", "stable diffusion" | Yes, always include one | Control, LoRA | 20 to 75 plus negative |
| Seedream | "seedream", "bytedance image" | No | Speed, consistency | 30 to 80 |
| Leonardo | "leonardo" | Yes | Stylized art, characters | Not listed |
| Ideogram 3.0 | "ideogram" | No | Text rendering, logos | 30 to 80 |

A negative prompt never goes to a platform that ignores it. Quality tags such as "4K, 8K, masterpiece" and "trending on artstation" come out on modern platforms. One of the library's worked examples turns the input `dragon` into this Midjourney prompt, scored VISUAL 50/60:

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

MOTION structures video prompts around what moves:

| Pillar | Weight | Core question |
|---|---:|---|
| Movement | 30% | How does everything move? |
| Origin | 15% | What is the visual anchor? |
| Temporal | 15% | How does time flow? |
| Intention | 15% | What story is being told? |
| Orchestration | 15% | How do elements interact? |
| Nuance | 10% | What refinements are needed? |

The mode's rules: camera movement comes first, clips stay at 5 to 10 seconds for consistency and negative prompts are left out because most video models ignore them. Text-to-video prompts run 50 to 120 words and image-to-video prompts 20 to 40.

| Platform | Max length | Native audio | Camera syntax | Strength |
|---|---|---|---|---|
| Runway Gen-4/4.5 | 10 s | No | Prefix required, such as `Dolly forward:` | Camera control, image-to-video |
| Sora | 20 s | No | Natural language | Cinematography, physics |
| Kling 2.5/2.6 | 5 min | 2.6 only | Brackets, reversed pan and tilt terms | Long duration |
| Veo 3.1+ | 148 s | Yes, as an `Audio:` section at the end | Natural language | Audio, cinematography |
| Pika 2.5 | 10 s | No | Scene ingredients | Modifications, lip-sync |
| Luma Ray3 | 10 s | No | Keyframes plus `[Camera:]` | Speed, keyframes |
| Minimax/Hailuo | 6 s | No | Brackets | Quality, director mode |
| Seedance 1.5 Pro | 10 s | Yes | Multi-shot syntax | Audio-visual sync |
| OmniHuman 1.5 | 30 s | Driven by an uploaded audio file | Audio-driven | Full-body avatar animation |
| Wan 2.1/2.2 | 5 s | No | Natural language | Text rendering, FLF2V |

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

After a creative prompt ships, the model asks you to run it and share what came back. Each round has a focus:

| Round | Visual | Image | Video |
|---|---|---|---|
| 1st | Direction | Composition | Motion |
| 2nd | Spatial, color and type detail | Style | Pacing and duration |
| 3rd | Polish | Atmosphere | Consistency |
| 4th and later | Variations | Detail | Detail and audio |

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

The chat side prints in fixed shapes so a transcript stays easy to scan:

| Line | Format |
|---|---|
| Progress | `Phase [D/E/P/T/H] - [name]: [concise finding]` |
| Validation | `[CLEAR\|EVOKE\|VISUAL] [score]/[max] \| Gate: [passed/revising/best-effort]` |
| Assumption | `[Assumes: description]` |
| Delivery | `Saved: export/[###] - enhanced-[description].[md/json/yaml]` |
| Creative follow-up | `Share the generated result when you want refinement.` |

Beyond the mode and framework in the file's header, the chat reports the perspectives used and the score as proof that the thinking ran. The perspectives and the score never enter the file.

#### Claude Project Delivery

A claude.ai Project cannot write files, so `claude project/Custom Instructions.md` swaps the export for a Deliverable Block rendered as a Canvas Artifact before any commentary.

| Part | Content |
|---|---|
| Header | The same single `Mode:` line as a saved file |
| Body | The enhanced prompt, in the locked format |
| Attestation footer | Docs consulted, assumptions, the format, `execution = did not occur` and `save = did not occur` |

The header and footer sit outside the JSON or YAML lock, which applies only to the body. After the block, chat carries the export-equivalent path `export/[###] - enhanced-[description].[md|json|yaml]`, the score and gate status, the token overhead for JSON or YAML, a short summary and, for creative modes, the share-back invitation. The Project never claims it saved, exported or verified anything.

#### Local Output

Generated prompts stay on your machine. The root `.gitignore` ignores everything in `export/` except `.gitkeep` and `export/benchmark/`.

&nbsp;

## 10. 🧪 BENCHMARKS AND CHECKS

Two checks run from a fresh clone with nothing but Bash and Python 3. The rest need a shared toolkit that lives only in the parent monorepo this repository sits inside.

#### Router Fixtures

```bash
bash benchmark/router/run_fixtures.sh
```

```text
PASSED 25/25 fixtures
```

| Group | Fixtures | What they pin down |
|---|---:|---|
| Mode commands | 9 | Each `$` mode command binds its intent, energy and scorer |
| Format commands | 4 | `$json` alone, `$markdown` alone, `$yaml` with a sentence and `$deep $json` together |
| Natural language | 8 | Keyword routes to Text, Framework, Scoring, MagicPath, Thinking, Interactive, Image and Video |
| Edge cases | 4 | A command beating Deep keywords, "ask" inside "basket", the `$short $deep` conflict and a greeting with no signal |

The runner exits 0 only when every fixture matches field for field, and it rejects route objects with unknown or duplicate fields.

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

Each of these 13 files has a hand-written counterpart in `claude project/knowledge/` carrying the same version number.

| File | Version | Loaded for | Carries |
|---|---|---|---|
| [`references/depth-framework.md`](sk-prompt-improver/references/depth-framework.md) | v0.200 | Every request | Phases, energy levels, perspectives, techniques, CLEAR rubric |
| [`references/interactive-mode.md`](sk-prompt-improver/references/interactive-mode.md) | v0.700 | Every request | One-question flow, 6 response templates, state machine, error recovery |
| [`references/patterns-evaluation.md`](sk-prompt-improver/references/patterns-evaluation.md) | v0.212 | Every route but Raw and Interactive | Enhancement patterns, CLEAR, EVOKE and VISUAL rubrics, REPAIR protocol |
| [`references/visual-mode.md`](sk-prompt-improver/references/visual-mode.md) | v0.301 | Visual, MagicPath | Step 0 grounding, VIBE, category defaults, EVOKE, 5 platforms |
| [`references/image-mode.md`](sk-prompt-improver/references/image-mode.md) | v0.123 | Image | FRAME, VISUAL image scoring, 9 platforms, anti-patterns |
| [`references/video-mode.md`](sk-prompt-improver/references/video-mode.md) | v0.123 | Video | MOTION, VISUAL video scoring, anti-patterns |
| [`assets/framework-pattern-library.md`](sk-prompt-improver/assets/framework-pattern-library.md) | v0.100 | Text routes, Framework | 11-framework matrix, selection algorithm, fusion patterns |
| [`assets/format-guide-markdown.md`](sk-prompt-improver/assets/format-guide-markdown.md) | v0.141 | Text routes, `$markdown` | Header contract, RCAF and CRAFT in Markdown |
| [`assets/format-guide-json.md`](sk-prompt-improver/assets/format-guide-json.md) | v0.142 | `$json` | Header contract, JSON syntax rules |
| [`assets/format-guide-yaml.md`](sk-prompt-improver/assets/format-guide-yaml.md) | v0.142 | `$yaml` | Header contract, YAML syntax rules |
| [`assets/visual-mode-library.md`](sk-prompt-improver/assets/visual-mode-library.md) | v0.110 | Visual, MagicPath | Vocabulary banks, 10 named style clichés, platform templates, MagicPath example |
| [`assets/image-mode-library.md`](sk-prompt-improver/assets/image-mode-library.md) | v0.101 | Image | 30 FRAME sub-category banks, platform syntax, 7 worked examples |
| [`assets/video-mode-library.md`](sk-prompt-improver/assets/video-mode-library.md) | v0.101 | Video | 10 platform profiles, mental models, audio syntax, 6 worked examples |

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

| What you see | Cause | Fix |
|---|---|---|
| A plain-language request gets a question instead of a mode | No router keyword matched. "design a fintech dashboard concept" has none, since the Visual keyword is "ui design" | Add the command, such as `$vibe`, or a keyword from the table in section 4 |
| The mode does not match your request | Another intent's keywords scored higher | Use an exact mode command, which always wins |
| `$short $deep` gets a question back | Two different mode commands conflict | Send one mode command |
| You asked for JSON or YAML in words and got Markdown | Only `$json`, `$j`, `$yaml` or `$y` lock a format | Add the format command |
| `route_contract.py` ignores the `$short` at the start of a request | The shell expanded `$short` to nothing inside double quotes | Wrap the request in single quotes |
| A JSON or YAML file contains Markdown syntax | The wrong format guide ran | Repeat the request with an explicit `$json` or `$yaml` |
| A Visual brief scores zero | A grounding check failed | Name the subject, audience, single job and deliberate deviation |
| A Video prompt fails its gate | Camera and subject motion are both missing | Add a camera move and an action verb |
| A Flux or Imagen prompt has no negative prompt | Both platforms ignore negatives | Expected. State what to avoid as a positive description |
| No path or score appears in CLI mode | The export did not verify | Treat the prompt as undelivered, check that `export/` is writable and rerun |
| The model writes the content instead of a prompt | The request read as a task | Ask for "a prompt that asks an AI to do X" |
| `deliverable-lint.csv` shows a diff after a grader run | `check_report.sh` rewrites it in place | Restore it from git and run the grader on a copy |
| `run_parity.sh` says `can't open file`, or `rule_parity.py` says `no declared pairs` | Both need the shared toolkit in the parent monorepo | Use the router fixtures and report checks, which run standalone |

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
