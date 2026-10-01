# Prompt Improver: router-in-kernel check, 2026-10-01, deepseek-v4.1-flash at thinking high

## 1. OVERVIEW

Kernel v1.7.0 moves the Smart Router Pseudocode out of Section 2 and into Section 8, Router Code, at the end of the kernel, with its comments removed. Section 2 keeps its routing prose and points at the code. The skill is unchanged, so this run sends only Project scenarios. It checks that routing still behaves the same once the code sits at the end: the routing scenarios, the identity handover, all five text modes, one format mode and one creative mode, two turns each.

**What this run checks and what it does not.** It grades the routing outcome of every scenario: the mode bound, the question asked or the delivery made, and the Deliverable Block's header and attestation. It does not regrade every fact and wording criterion in each scenario's Pass/fail line, which this change does not touch.

---

## 2. RESULTS

10 of 10 route as their scenarios require.

| ID | Turn 1 | Turn 2 | Routing |
|---|---|---|---|
| PIR-001 | One question naming the `$short` and `$deep` conflict, no block | `$short` block with attestation on the supplied prompt | PASS |
| PIR-002 | One consolidated question, no block | `$text` block built on the Turn 2 prompt | PASS |
| PID-001 | `$improve` block, the Project-only `Canvas Artifact` marker in chat | `$improve` block | PASS |
| PTX-001 | `$improve` block | No new block, the answer closed an assumption | PASS |
| PTX-002 | `$deep` block | `$deep` block | PASS |
| PTX-003 | `$short` block | `$short` block | PASS |
| PTX-004 | `$refine` block | `$refine` block | PASS |
| PTX-005 | `$raw` block, no framework | `$raw` block | PASS |
| PFM-001 | `$improve` block with the JSON lock | `$improve` block with the JSON lock | PASS |
| PCR-001 | `$image` block | `$image` block | PASS |

PTX-001 delivered no second block on 2026-09-28 either, on kernel v1.6.1, for the same reason.

---

## 3. HOW THE RUN WAS MADE

- **Rules under test:** `claude project/Custom Instructions.md` v1.7.0 with `sk-prompt-improver/SKILL.md` 1.5.3, before commit
- **Engine:** Pi, model `opencode-go/deepseek-v4.1-flash`, thinking `high`, 5 parallel sessions
- **Runner:** `run/playbook_runner.py`, copied from the 2026-09-28 report, called from this folder as `python3 run/playbook_runner.py --system ../../.. --out . --engine pi --model opencode-go/deepseek-v4.1-flash --effort high --side project --ids PIR-001,PIR-002,PID-001,PTX-001,PTX-002,PTX-003,PTX-004,PTX-005,PFM-001,PCR-001 --jobs 5`. All 10 sessions ended `ok` on their first attempt
- **Replies:** `replies/<ID>-turn<N>.txt`. `run-status.json` and `run-log.jsonl` hold the session records
