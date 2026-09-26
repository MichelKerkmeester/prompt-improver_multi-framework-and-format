# Prompt Improver Examples

> Eight enhanced prompts written through the skill, one for each mode and format the playbook run's deliverables do not show.

---

## 1. OVERVIEW

These files show what Prompt Improver writes for `$deep`, `$short`, `$refine`, `$raw`, `$yaml`, `$markdown`, `$video` and `$vibe`. The deliverables in `../skill/` and `../claude project/` come from a graded playbook run and cover only `$text`, `$image` and `$json`.

Each example answers the exact Turn 1 input of one skill scenario in the manual testing playbook, so a later run of that scenario can be compared with it. They were written through the skill on 2026-09-26 by an agent that loaded `AGENTS.md`, `SKILL.md` and the routed references.

⚠️ No playbook run has graded these examples. Each score below is the writer's own reading of the routed rubric, and no independent scorer has checked it.

---

## 2. EXAMPLES

| File | Command | Format | Framework | Writer's score |
| --- | --- | --- | --- | --- |
| `STX-002 - 001 - enhanced-helpdesk-triage-system-prompt.md` | `$deep` | Markdown | TIDD-EC | CLEAR 44/50 |
| `STX-003 - 001 - enhanced-linkedin-head-of-design-hire-post.md` | `$short` | Markdown | COSTAR | CLEAR 42/50 |
| `STX-004 - 001 - enhanced-webshop-product-description-prompt.md` | `$refine` | Markdown | COSTAR | CLEAR 45/50 |
| `STX-005 - 001 - enhanced-quarterly-sales-report-summary-prompt.md` | `$raw` | Markdown | None | Not scored, Raw mode skips scoring |
| `SFM-002 - 001 - enhanced-invoice-extraction-prompt.yaml` | `$text $yaml` | YAML | RCAF | CLEAR 44/50 |
| `SFM-003 - 001 - enhanced-code-review-prompt.md` | `$improve $markdown` | Markdown | RCAF | CLEAR 44/50 |
| `SCR-002 - 001 - enhanced-veo-water-bottle-product-shot.yaml` | `$video $yaml` | YAML | MOTION | VISUAL 61/70 |
| `SCR-003 - 001 - enhanced-bakery-morning-dashboard-v0.md` | `$vibe` | Markdown | VIBE | EVOKE 43/50 |

Each score clears its gate: CLEAR 40/50, VISUAL 56/70 and EVOKE 40/50.

---

## 3. WHAT EACH INPUT ASKED FOR

| Example | Input in short |
| --- | --- |
| `STX-002` | A system prompt for a B2B helpdesk triage bot with five categories, three SLA tiers, three escalation triggers and a ban on promising refunds or dates |
| `STX-003` | A warm LinkedIn post announcing Priya Nair as the new head of design, starting October 14 |
| `STX-004` | A webshop product-description prompt that contradicts itself on tone and length |
| `STX-005` | A rough ChatGPT instruction to summarise a quarterly sales report for the exec team |
| `SFM-002` | An extraction prompt for supplier invoices with named fields, where a missing field is null and never a guess |
| `SFM-003` | A one-line code review prompt that should check security, missing tests and naming like a senior reviewer |
| `SCR-002` | An 8 second Veo product shot of a matte black bottle beside a mountain stream, with no people and no text |
| `SCR-003` | A calm v0 dashboard for a bakery owner checking three shops on an iPad at 6am |

The full inputs are the Turn 1 prompts in [the playbook](../../../sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md).

---

## 4. HOW THEY WERE WRITTEN

- **Questions.** Every example delivers without a question, except `SCR-003`. `$vibe` must ask which component library to use, and the writer answered it with option C, no library, which adds nothing to the prompt.
- **Format questions.** The writer skipped the format question `$short` would ask and delivered Markdown, the default. `$refine` would ask which kind of refinement to make, and the input already named it: too salesy and too long.
- **YAML header.** Both YAML files open with `# Mode: $yaml | ...`, a YAML comment. The literal header in the YAML format guide, a line starting with `Mode:`, does not parse as YAML, so the comment form keeps the whole file valid. `SFM-002` and `SCR-002` accept either form as the single-line header.
- **Added by rule.** `SCR-003` carries the UX-floor constraints the `$vibe` rules add to every UI brief. `SCR-002` carries an `audio:` line because the video rules tell a Veo prompt to add audio cues, and it limits the sound to the stream. Both scenarios record these and never grade them, because the rules that add them and the scope test point different ways.
- **Review edits.** An independent review against the scenarios made three small edits after writing. `SFM-003` lost an "Other problems" catch-all, since the scenario asks for exactly the three named checks. `SCR-002` names the bottle as new again. `STX-005` names ChatGPT in its header.

---

## 5. RELATED

- [The playbook run's README](../../../benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/README.md) covers the graded deliverables in `../skill/` and `../claude project/`
- [The manual testing playbook](../../../sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md) holds the scenario behind each example
