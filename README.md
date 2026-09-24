# Prompt Improver - Multi-Framework & Format

> Turns rough requests into structured, scored prompts for another AI to run.

> Like it? https://buymeacoffee.com/michelkerkmeester

[![GitHub Stars](https://img.shields.io/github/stars/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&logo=github&color=fce566&labelColor=222222)](https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format/stargazers)
[![License](https://img.shields.io/github/license/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&color=7bd88f&labelColor=222222)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MichelKerkmeester/prompt-improver_multi-framework-and-format?style=for-the-badge&color=5ad4e6&labelColor=222222)](https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format/commits/main)

## 1. SUMMARY

A prompt engineer in a folder: it rewrites a vague or underpowered request into a structured, scored prompt for another AI to run.

It delivers the prompt and never the work the prompt describes. Every prompt lands as a file before the reply mentions it.

Built for any capable model in an agent CLI that reads `AGENTS.md`, and for claude.ai Projects through `claude project/`

**What's inside**

- 🧭 **Smart Router** - nine explicit modes plus an Interactive fallback for unclear requests
- 🧠 **DEPTH Thinking** - adjusts analysis steps and perspective count to the selected energy
- 🎯 **Framework Library** - 11 frameworks selected by task fit, with RCAF as the ordinary default
- 🧮 **Quality Scoring** - CLEAR, EVOKE or VISUAL checks the prompt against mode-specific thresholds
- 🎨 **Creative Prompt Modes** - creates UI, image and video prompts with platform-aware structures
- 📦 **Format Lock** - writes Markdown, JSON or YAML while keeping the chosen syntax
- 📤 **Verified Delivery** - saves the prompt and confirms the file before the chat response

**Why it earns a place**

- **Keeps scope clear:** the output is the prompt another AI uses to do the requested work
- **Matches structure to task:** framework choice follows the intended outcome and complexity
- **Makes quality visible:** mode-specific scores show whether a prompt clears its gate

---

## 2. 🎁 OVERVIEW

### THE FOUNDATION

Three building blocks carry a prompt from request to file:

1. **Routing** selects a prompt mode and output format independently.

2. **Prompt design** uses DEPTH and a fitting framework to shape the instructions.

3. **Scoring and delivery** apply the correct gate, preserve format and save the result.

From request to delivered prompt:

```text
                         YOUR REQUEST
                               │
                               ▼
                ┌────────────────────────────┐
                │       SMART ROUTER         │
                │                            │
                │  Exact command or signal   │
                │  One mode, one resource    │
                │  Format lock runs alone    │
                └──────────────┬─────────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │    DEPTH AND FRAMEWORK     │
                │                            │
                │  Discover, Engineer        │
                │  Prototype, Test           │
                │  Harmonize                 │
                └──────────────┬─────────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │    SCORE AND VALIDATE      │
                │                            │
                │  CLEAR, EVOKE or VISUAL    │
                │  Check the locked format   │
                │  Repair within the limit   │
                └──────────────┬─────────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │   EXPORT AND READ BACK     │
                │                            │
                │  Save .md, .json or .yaml  │
                │  Return path and score     │
                └──────────────┬─────────────┘
                               │
                               ▼
                       DELIVERED PROMPT
```

### Smart Routing

One request, one mode.

Exact commands win over wording, and keyword scoring handles the rest.

- `$improve`, `$vibe`, `$image` and the other commands match only as standalone tokens
- Format locks run on their own axis, so `$improve $json` keeps Improve and writes JSON
- Two modes that score within a point of each other get one question instead of a guess

### DEPTH Thinking

Rigor matched to the request.

Five phases run at the depth the energy level sets: Discover, Engineer, Prototype, Test and Harmonize.

- Raw is passthrough cleanup with no phases and no score
- Quick runs three phases with one or two perspectives
- Standard needs at least three perspectives and Deep needs all five

### Framework Selection

The right structure, not the fanciest one.

The library holds 11 frameworks for text, UI, image and video prompts.

- RCAF (Role, Context, Action, Format) is the ordinary default
- Another framework wins only when its structure fits the request better
- Complexity for its own sake never picks a framework

### Mode-Specific Scoring

A number the prompt has to earn.

Each mode family scores against the gate that fits its output.

- CLEAR scores text prompts, EVOKE scores UI briefs and VISUAL scores image and video prompts
- Every dimension has a floor, and one dimension under it triggers revision even when the total passes
- A failed gate triggers targeted revision, capped at three cycles

### Format Lock

Clean files a tool can load.

Markdown, JSON and YAML each have their own structure rules.

- A saved file holds one header line and the prompt body, nothing else
- Scores, notes and explanations stay in chat
- JSON and YAML outputs get a syntax check before export

### Verified Delivery

Saved first, reported second.

In a CLI, the prompt is saved to `export/` and checked before the response names it.

- The reply carries the path, the score where the mode has one and a two-to-three sentence summary
- The full prompt never appears in chat once the export succeeds
- A claude.ai Project returns a Deliverable Block with an export-equivalent path instead

---

## 3. 🚀 QUICK START

### Installation

**Prerequisites**

- Git to clone the repository
- An agent CLI that reads `AGENTS.md` and accepts your model
- Bash and Python 3 for the router check
- For claude.ai, a Project that accepts custom instructions and knowledge files

Clone the repository and open it in your agent CLI:

```bash
git clone https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format.git
cd prompt-improver_multi-framework-and-format
```

Point the model at `AGENTS.md`. It loads `sk-prompt-improver/SKILL.md`, and from then on the model works as Prompt Improver.

### Verify Installation

Run the router fixture check from the repository root:

```bash
bash benchmark/router/run_fixtures.sh
```

Expected output:

```text
PASSED 25/25 fixtures
```

The check runs without a model or a network connection.

### First Use

Try one of these requests once the CLI has read `AGENTS.md`:

| Request | Route | What comes back |
|---|---|---|
| `$improve tighten this onboarding email prompt` | Improve | Markdown prompt with CLEAR score and output path |
| `$short shorten this support-macro prompt without losing meaning` | Short | Concise prompt with CLEAR validation |
| `$vibe design a fintech dashboard concept` | Visual | Grounded UI brief scored by EVOKE |
| `$image a Midjourney portrait with rim lighting` | Image | Prompt scored by VISUAL |
| `$video a Runway clip of rain on a windshield` | Video | Motion-based prompt scored by VISUAL |

A CLI response carries the saved path, the relevant gate result and a short summary. The full prompt stays in the saved file.

Example path and validation line:

```text
Saved: export/001 - enhanced-onboarding-email-prompt.md
CLEAR 45/50 | Gate: passed
```

### Use It in a claude.ai Project

The Project package gives claude.ai the router, DEPTH rules and mode resources through its custom instructions and knowledge files.

1. Create or open a Project named **Prompt Improver**
2. Paste `claude project/Custom Instructions.md` into its custom instructions
3. Upload every file in `claude project/knowledge/` with its filename unchanged
4. Update the instructions and the knowledge files together when the package changes

The package contains 13 knowledge files. See [the Project README](claude%20project/README.md) for setup and its file list.

---

## 4. 🧭 MODES AND ROUTING

Nine explicit modes route text and creative requests. Interactive mode handles unclear intent.

#### Mode Table

| Mode | Commands | Output |
|---|---|---|
| Raw | `$raw` | Grammar cleanup with no DEPTH or scoring |
| Text | `$text`, `$t` | Standard prompt enhancement with CLEAR |
| Improve | `$improve`, `$i` | Framework selection and CLEAR scoring |
| Refine | `$refine`, `$r` | Refinement with CLEAR scoring |
| Short | `$short`, `$s` | Quick prompt enhancement with CLEAR |
| Deep | `$deep`, `$d` | Expanded analysis with CLEAR scoring |
| Visual | `$vibe`, `$v` | UI concept brief with EVOKE |
| Image | `$image`, `$img` | Image-generation prompt with VISUAL |
| Video | `$video`, `$vid` | Motion prompt with VISUAL |

Interactive mode asks one comprehensive question when no mode is clear or two mode commands conflict.

#### Routing Rules

| Signal | Behavior |
|---|---|
| Mode command | Selects the intent before keyword matches |
| Format command | Locks Markdown, JSON or YAML independently |
| Keyword score | Selects one mode when no explicit command appears |
| Conflicting commands | Asks which mode the user wants |
| Unclear request | Routes to Interactive mode |

Mode commands match complete tokens, so a longer word that contains `$img` does not trigger Image mode.

MagicPath signals take priority over general Visual terms. Platform and format references load only when the selected intent needs them.

#### Precedence, By Example

| Request | Routes to |
|---|---|
| `$vibe a magicpath onboarding flow` | Visual mode, VIBE-MP calibration |
| "design a fintech dashboard concept" | Visual mode, standard VIBE |
| "a midjourney portrait, moody lighting" | Image mode, Midjourney platform |
| "a runway clip of rain on a windshield" | Video mode, Runway platform |
| "shorten this without losing meaning" | Short mode, Quick energy |
| `$raw just fix the grammar` | Raw mode, no DEPTH, no scoring |
| "give me this as yaml" | Format lock: YAML, mode unchanged |
| "improve this" with no other signal | Interactive mode, depth-choice question |

At 80% mode confidence or higher the router auto-selects and explains briefly. Between 50% and 79% it suggests a mode and asks for confirmation. Below 50% it asks one clarifying question, up to three attempts, then falls back to smart defaults with the assumptions flagged.

---

## 5. ⚡ DEPTH AND FRAMEWORKS

DEPTH stands for Discover, Engineer, Prototype, Test and Harmonize. Energy controls which phases run and how many perspectives shape the draft.

#### Energy Levels

| Energy | Flow | Perspectives |
|---|---|---|
| Raw | Passthrough cleanup | None |
| Quick | Discover, Prototype and Harmonize | One or two |
| Standard | All five phases | At least three |
| Deep | Extended analysis across all phases | Five |
| Creative | Abbreviated phases with mode-specific analysis | Mode-specific |

Raw skips scoring. Other prompt modes use their assigned validation gate.

#### The Five DEPTH Phases

| Phase | Purpose |
|---|---|
| Discover | Understand the source prompt, goal and missing context |
| Engineer | Choose a framework and test possible approaches |
| Prototype | Build the structured prompt |
| Test | Apply the routed scoring gate |
| Harmonize | Polish, validate format and export |

#### Framework Library

The 11 frameworks combine seven text structures with four creative structures:

| Framework | Best fit |
|---|---|
| RCAF | Ordinary tasks and clear instructions |
| COSTAR | Audience-specific tone and content |
| RACE | Urgent work and fast iteration |
| CIDI | Tutorials and process documentation |
| TIDD-EC | Quality-critical and compliance prompts |
| CRISPE | Strategy and exploration |
| CRAFT | Complex work with multiple stakeholders |
| VIBE | Visual UI concepting |
| VIBE-MP | Multi-page MagicPath flows |
| FRAME | Image-generation prompts |
| MOTION | Video-generation prompts |

RCAF is the default for ordinary prompt work. Framework fit takes priority over complexity for its own sake.

#### RCAF Output Shape

```markdown
Mode: $improve | Complexity: Medium | Framework: RCAF

**Role:** Data analyst with expertise in SaaS metrics.
**Context:** Q4 revenue data from a B2B platform.
**Action:** Calculate revenue growth and identify the main trends.
**Format:** Executive summary with metrics, charts and recommendations.
```

#### Perspective and Revision Rules

Standard energy needs at least three perspectives: Prompt Engineering, AI Interpretation and User Clarity. It targets five by adding Framework and Token Efficiency. Deep requires all five.

A scoring failure triggers targeted revision. The normal repair limit is three cycles.

---

## 6. 🧾 OUTPUT FORMATS AND QUALITY GATES

The format command locks the output shape independently from mode selection.

#### Format Options

| Format | Command | Use |
|---|---|---|
| Markdown | Default, `$markdown`, `$md` or `$m` | Human-readable prompt files |
| JSON | `$json` or `$j` | Structured, machine-readable prompts |
| YAML | `$yaml` or `$y` | Configuration-shaped prompts |

JSON adds about 5 to 10 percent token overhead. YAML adds about 3 to 7 percent against Markdown.

#### Text Scoring with CLEAR

CLEAR scores text-family prompts out of 50:

| Dimension | Points | Floor |
|---|---:|---:|
| Correctness | 10 | 7 |
| Logic | 10 | 7 |
| Expression | 15 | 10 |
| Arrangement | 10 | 7 |
| Reusability | 5 | 3 |

The pass threshold is 40/50. The system targets 45/50 for excellent prompts.

#### Visual Scoring with EVOKE

EVOKE checks grounding first, then scores five dimensions out of 50.

| Grounding check | What it requires |
|---|---|
| Subject | A named and concrete subject |
| Audience | A role in a specific context |
| Single job | One falsifiable main action |
| Anti-default | A stated deviation from the category default |

A failed grounding check scores zero. A standard brief passes at 40/50. MagicPath passes at 42/50 with its mode-specific checks.

#### Image and Video Scoring with VISUAL

VISUAL scores image prompts out of 60 and video prompts out of 70.

| Target | Threshold | Extra condition |
|---|---:|---|
| Image | 48/60 | Image-specific structure and constraints |
| Video | 56/70 | Camera or subject motion is required |

A static video description fails regardless of its other scores.

#### Format Templates

Markdown carries one header followed by a structured prompt body:

```markdown
Mode: $improve | Complexity: Medium | Framework: RCAF

**Role:** Specific expertise needed.
**Context:** Essential background information.
**Action:** Clear, measurable task.
**Format:** Expected output structure.
```

JSON and YAML files open with the same single header line, then the body in the locked syntax:

```text
Mode: $json | Complexity: Medium | Framework: RCAF

{
  "role": "Specific expertise",
  "context": "Essential background",
  "action": "Clear task",
  "format": {
    "structure": "Expected output",
    "requirements": ["One requirement", "Another requirement"]
  }
}
```

```text
Mode: $yaml | Complexity: Medium | Framework: RCAF

role: Specific expertise
context: Essential background
action: Clear task
format:
  structure: Expected output
  requirements:
    - One requirement
    - Another requirement
```

Scoring detail and processing notes stay outside the saved prompt file.

---

## 7. 🎨 CREATIVE MODES

Creative modes use grounding and platform structure to turn visual ideas into runnable prompts.

#### Visual Mode

VIBE shapes UI concept prompts around Vision, Inspiration, Behavior and Experience.

Step 0 names a concrete subject, a specific audience and one falsifiable job. The brief must also depart from its category default before EVOKE scoring begins.

The Visual library supports MagicPath.ai, Lovable, Aura, Bolt and v0.dev. MagicPath context selects VIBE-MP for multi-page flows.

#### Image Mode

FRAME structures image prompts through Focus, Rendering, Atmosphere, Modifiers and Exclusions.

Platform detection covers Flux 2 Pro, Google Imagen 4 (Nano Banana Pro), Runway, Midjourney, DALL-E 3, Stable Diffusion, Seedream, Leonardo and Ideogram. Each has its own syntax and its own support for negative prompts.

#### Video Mode

MOTION structures video prompts through Movement, Origin, Temporal flow, Intention, Orchestration and Nuance.

Camera or subject movement is required before a video prompt can pass. Platform detection covers Runway Gen-4 and 4.5, Sora, Kling 2.5 and 2.6, Veo 3.1+, Pika 2.5, Luma Ray3, Minimax, Seedance, OmniHuman and Wan 2.1.

#### Platform Grounding

| Prompt type | What the mode contributes |
|---|---|
| Visual UI | Named subject, audience, primary job and a deliberate departure from the category default |
| Image | Subject, rendering choices, atmosphere and exclusions matched to platform syntax |
| Video | A visual anchor, temporal progression and camera or subject movement |

---

## 8. 📤 EXPORT AND DELIVERY

CLI delivery saves the prompt before returning a path or score.

#### File Naming

The next available number starts at 001:

```text
export/[###] - enhanced-[description].md
export/[###] - enhanced-[description].json
export/[###] - enhanced-[description].yaml
```

A saved response includes the path, the mode score when applicable, gate status and a short summary. It does not paste the full prompt.

Creative modes close with an invitation to share the generated result for another refinement pass.

#### Response Lines

The chat side prints in fixed shapes so a transcript stays easy to scan:

| Line | Format |
|---|---|
| Progress | `Phase [D/E/P/T/H] - [name]: [concise finding]` |
| Validation | `[CLEAR\|EVOKE\|VISUAL] [score]/[max] \| Gate: [passed/revising/best-effort]` |
| Assumption | `[Assumes: description]` |
| Delivery | `Saved: export/[###] - enhanced-[description].[md/json/yaml]` |
| Creative follow-up | `Share the generated result when you want refinement.` |

#### Claude Project Delivery

A claude.ai Project cannot write files. The Project version returns the prompt in a Deliverable Block and reports an export-equivalent path.

The block carries the selected format and the prompt itself. Processing notes and score details stay in chat.

#### Local Output Rules

Generated prompts stay local. The root `.gitignore` ignores everything in `export/` except `.gitkeep` and `export/benchmark/`.

---

## 9. 🧪 BENCHMARKS AND CHECKS

One check runs from a fresh clone, from the repository root, with no model involved:

| Command | What it checks | Expected result |
|---|---|---|
| `bash benchmark/router/run_fixtures.sh` | The route contract against its fixture set | `PASSED 25/25 fixtures` |

The router check covers exact-command routing, word-boundary keywords, independent format locks and the Interactive fallback. Inspect a single request with `python3 benchmark/router/route_contract.py "<request>"`.

#### Captured Runs

`benchmark/reports/` holds a manual-testing-playbook run with its results, verdicts and captured replies. `bash benchmark/grader/check_report.sh <report-folder>` lints a run's replies and flags any scenario where the skill and the Project reached different verdicts. The scenarios themselves live in `sk-prompt-improver/manual-testing-playbook/`.

#### Maintainer Scripts

`benchmark/parity/` and `benchmark/gates/` compare the Claude Project package against the skill sources. They call a shared sync toolkit that is not part of this repository, so they do not run from a clone.

---

## 10. 🗂️ REPOSITORY STRUCTURE

The repository separates the skill source, Project package, check scripts and local export folder.

```text
.
├── .gitignore                       ignores local export outputs
├── AGENTS.md                        CLI entry point
├── Favicon.jpg                      repository icon
├── LICENSE                          MIT license
├── README.md                        public repository guide
├── SYNC.md                          Project package parity notes
├── benchmark/
│   ├── gates/                       maintainer rule-parity check
│   ├── grader/                      reply and run-report checks
│   ├── parity/                      maintainer Project drift scripts
│   ├── reports/                     captured benchmark runs
│   └── router/                      route fixtures and contract
├── claude project/
│   ├── Custom Instructions.md       claude.ai Project instructions
│   ├── README.md                    Project upload guide
│   └── knowledge/                   13 Project Knowledge files
├── export/                          generated outputs, kept local
└── sk-prompt-improver/
    ├── README.md                    skill guide
    ├── SKILL.md                     routing and processing rules
    ├── assets/                      seven framework, mode and format libraries
    ├── changelog/                   skill release notes
    ├── manual-testing-playbook/     manual validation scenarios
    └── references/                  DEPTH, mode and scoring guides
```

`AGENTS.md` points an agent CLI at the skill. A claude.ai Project reads `claude project/Custom Instructions.md` and the files under `claude project/knowledge/` instead.

---

## 11. ❓ FAQ

**Q: Does Prompt Improver perform the task in my prompt?**

No. It writes instructions for another AI or tool to perform the requested work.

**Q: Which framework should I choose?**

Start without a framework command. The router selects RCAF for ordinary requests and uses another framework when its structure better fits the goal.

**Q: Can a format command change the selected mode?**

No. Mode and format are separate choices. `$improve $json` keeps Improve intent and locks the prompt body to JSON.

**Q: Does it write the code, design or content the prompt is for?**

No. That work is out of scope by design. The deliverable is always the prompt, never the downstream work.

**Q: Why did my Visual brief score zero?**

One grounding check may be missing. Name the subject, audience and falsifiable job, then state how the direction departs from its category default.

**Q: Can Quick skip scoring or export?**

No. Quick uses a shorter DEPTH flow, then applies its scorer and saves the prompt.

**Q: What does the Claude Project package return?**

It displays a Deliverable Block and an export-equivalent path because a Project has no filesystem export.

---

## 12. 🔧 TROUBLESHOOTING

| What you see | Cause | Fix |
|---|---|---|
| The mode does not match your request | A keyword may point to another intent | Use an exact mode command |
| The model asks for clarification | The source prompt or target use case lacks key context | Supply the missing goal and audience |
| A JSON or YAML file contains Markdown syntax | The wrong format guide ran | Repeat the request with an explicit `$json` or `$yaml` |
| A Visual brief scores zero | A grounding check failed | Name the subject, audience, main job and deliberate deviation |
| A Video prompt fails its gate | Camera and subject motion are both missing | Add a clear camera move or subject action |
| No path or score appears in CLI mode | The export did not verify | Treat the prompt as undelivered, check that `export/` is writable and rerun |
| The model answers the request instead of improving the prompt | The request read as a task, not a prompt | Rephrase as "write me a prompt that asks an AI to do X" |
| `run_parity.sh` fails with a missing file | The parity scripts need a sync toolkit outside this repo | Use the router check, which runs standalone |

---

## 13. 📚 RELATED DOCUMENTS

**System guides**

- **[→ Agent Bootstrap](AGENTS.md)** - CLI entry point and skill-loading rules
- **[→ Prompt Improver Skill](sk-prompt-improver/SKILL.md)** - modes, routing, DEPTH and delivery
- **[→ Prompt Improver README](sk-prompt-improver/README.md)** - detailed mode and asset guide
- **[→ DEPTH Framework](sk-prompt-improver/references/depth-framework.md)** - phases, energy levels and perspectives
- **[→ Interactive Mode](sk-prompt-improver/references/interactive-mode.md)** - one-question fallback
- **[→ Scoring and Evaluation](sk-prompt-improver/references/patterns-evaluation.md)** - CLEAR, EVOKE, VISUAL and repair rules
- **[→ Framework Pattern Library](sk-prompt-improver/assets/framework-pattern-library.md)** - 11 frameworks and selection guidance
- **[→ Visual Mode](sk-prompt-improver/references/visual-mode.md)** - VIBE, VIBE-MP and EVOKE
- **[→ Image Mode](sk-prompt-improver/references/image-mode.md)** - FRAME and image platform rules
- **[→ Video Mode](sk-prompt-improver/references/video-mode.md)** - MOTION and video platform rules
- **[→ Format Guides](sk-prompt-improver/assets/format-guide-markdown.md)** - Markdown structure and related JSON and YAML guides

**Claude Project package**

- **[→ Project Setup](claude%20project/README.md)** - Project instructions and knowledge file list
- **[→ Parity Notes](SYNC.md)** - hand-maintained package parity note

**Benchmark guides**

- **[→ Router Checks](benchmark/router/README.md)** - 25 router fixtures
- **[→ Parity Checks](benchmark/parity/README.md)** - read-only commit-date comparison
