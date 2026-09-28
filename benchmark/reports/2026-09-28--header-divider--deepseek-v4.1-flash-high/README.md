# Prompt Improver: header-divider check, 2026-09-28, deepseek-v4.1-flash at thinking high

## 1. OVERVIEW

Skill 1.5.2 and kernel v1.6.1 put a blank line, `---` and a blank line between the `Mode:` header and the prompt in every file and every Deliverable Block. This run checks whether a model other than the one the rules were tuned on writes that layout unprompted. It sends 22 scenarios to DeepSeek V4.1 Flash: the five text modes, the three format modes and the three creative modes, each on the skill and in the Project, two turns each.

**What this run checks and what it does not.** It checks the header and the divider in every deliverable, and that each JSON and YAML payload below the divider parses. It does not grade the scenarios against their Pass/fail lines, so the other defects in section 4 are observations, not verdicts.

---

## 2. RESULTS

Every deliverable that carries a header carries the divider, with a blank line on each side.

| Side | Deliverables | Header and divider | No header |
|---|---|---|---|
| Skill | 21 | 21 | 0 |
| Project | 19 | 18 | 1 |

The one Project block with no header is PFM-001 turn 2, whose input reads "Valid JSON only, the action items are for a project manager." The model moved the header, the divider and the attestation into chat and said so, offering to restore them. The kernel keeps the header and the attestation outside the JSON lock, so "valid JSON only" binds the payload and the framing should have stayed. Turn 1, the graded delivery, carries the divider. The skill twin, SFM-001, kept the header and the divider on both turns.

All 16 JSON and YAML payloads parse below the divider: 8 skill files and 8 Project blocks.

`benchmark/grader/deliverable_lint.py` reports no `header_divider_missing` on any of the 22 Project replies.

| ID | Deliverables | Header and divider |
|---|---|---|
| SCR-001 | 2 | divided, divided |
| SCR-002 | 2 | divided, divided |
| SCR-003 | 1 | divided |
| SFM-001 | 2 | divided, divided |
| SFM-002 | 2 | divided, divided |
| SFM-003 | 2 | divided, divided |
| STX-001 | 2 | divided, divided |
| STX-002 | 2 | divided, divided |
| STX-003 | 2 | divided, divided |
| STX-004 | 2 | divided, divided |
| STX-005 | 2 | divided, divided |
| PCR-001 | 2 | divided, divided |
| PCR-002 | 2 | divided, divided |
| PCR-003 | 0 | none, see section 4 |
| PFM-001 | 2 | divided, then no header on turn 2 |
| PFM-002 | 2 | divided, divided |
| PFM-003 | 2 | divided, divided |
| PTX-001 | 1 | divided |
| PTX-002 | 2 | divided, divided |
| PTX-003 | 2 | divided, divided |
| PTX-004 | 2 | divided, divided |
| PTX-005 | 2 | divided, divided |

SCR-003 and PTX-001 have one deliverable because their second turn changed nothing that needed a new file or block.

---

## 3. HOW THE RUN WAS MADE

- **Rules under test:** `sk-prompt-improver/SKILL.md` 1.5.2 and `claude project/Custom Instructions.md` v1.6.1, at Prompt Improver commit `8600c74`
- **Engine:** Pi 0.87.1, model `llmgateway/deepseek-v4.1-flash`, thinking `high`, 6 parallel sessions. The gateway served every turn from `runware/deepseek-v4.1-flash`, and the event streams name the model `deepseek-v4.1-flash`
- **Runner:** `run/playbook_runner.py`, the 2026-09-27 runner (sha1 `a0315dcd5b`), called from this folder as `python3 run/playbook_runner.py --system ../../.. --out . --engine pi --model llmgateway/deepseek-v4.1-flash --effort high --ids <22 IDs> --jobs 6`. All 22 sessions ended `ok` on their first attempt, 44 turns, 0.21 USD, 876,582 input and 111,923 output tokens, 20.7 minutes of session time
- **Manifest:** the runner writes all 78 playbook scenarios into `manifest.json`, which was narrowed to the 22 that ran
- **Run check:** `python3 run/check_run.py . --model deepseek-v4.1-flash` prints `22 scenarios, 44 declared turns, 44 event streams read, 0 finding(s)` and exits 0
- **Collection:** `python3 -B run/collect_exports.py . deliverables`, the 2026-09-27 collector (sha1 `0f39e06b72`), into this folder's `deliverables/` rather than `export/benchmark/`, so the export pack stays the Sonnet example pack. The collector cut both PTX-002 blocks at the first code fence inside the prompt. Those two files were replaced by hand with the block exactly as the reply wrote it, from the `Mode:` line through the attestation line
- **Divider check:** a script classified line 1 to 4 of each collected file and parsed each JSON and YAML payload below the divider

---

## 4. FINDINGS

None of these concern the divider. They were seen while checking it and are not graded.

1. **"Valid JSON only" read as dropping the framing.** PFM-001 turn 2, above. The 2026-09-25 Sonnet run's SFM-001 revision dropped its header for the same instruction. A line in the JSON and YAML guides saying the header, divider and attestation stay when a user asks for valid JSON or YAML only would close it
2. **PCR-003 never delivered.** Both turns ask the component-library question and build nothing. Its skill twin, SCR-003, delivered on turn 1
3. **PFM-003 has no attestation line.** Both turns carry the header and the divider and end without `Attestation:`
4. **Nested code fences in PTX-002.** The prompt inside the fenced block has its own fences, so the outer fence closes early wherever the reply is rendered as Markdown
5. **Commentary before the block in PFM-001 turn 1.** The reply opens with a bold `Deliverable Block` label and a note about the missing Canvas panel, which the Canvas stand-in rule counts as commentary

---

## 5. DELIVERABLES

The 40 deliverables sit in [`deliverables/skill/`](deliverables/skill/) and [`deliverables/claude project/`](deliverables/claude%20project/) under `<ID> - <number> - <name>`, as the collector names them. They are run output as written, apart from the two PTX-002 files described in section 3. The raw event streams, transcripts and per-scenario export copies stay local, as in earlier runs.

---

## 6. NEXT STEPS

1. **Decide finding 1.** Whether the format guides should say that "valid JSON only" or "valid YAML only" binds the payload and keeps the header, divider and attestation
2. **A full grading.** Grading the 22 against their Pass/fail lines would turn findings 2 to 5 into verdicts
3. **Teach the collector nested fences.** A fence count that pairs an opening fence with its own close would extract PTX-002 without a hand fix

**Item 1 was decided on 2026-09-28.** The operator chose to keep the framing. Skill 1.5.3 ends the Divider paragraph of the JSON and YAML guides, and of their Project twins, with a sentence saying a request for valid JSON or YAML only binds the payload, so the header, the divider and the attestation footer stay.
