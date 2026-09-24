# Twin divergence sampling, Prompt Improver, 2026-09-17 run

Measures whether the one twin divergence this report directory carries, `STX-001` PASS beside `PTX-001` FAIL, is a packaging property or a sampling draw. Every scenario in the committed run executed once per packaging, and four independent measurements have since shown some turn types returning both verdicts from one configuration, so a one-against-one comparison cannot separate the two. Report only, nothing repaired, nothing committed. Paths are relative to `AI Systems/Prompt Improver/` unless stated otherwise.

`adjudication.md` in this directory is untouched. It classed this pair a runtime fault on the ordering defect and reclassed the missing `Score:` header field as a rule gap that was never a co-cause. This file tests only whether the ordering defect survives sampling.

---

## 1. Pre-registered discriminator

Written before any sampling run. Not revised afterwards.

### The test

**One mechanical test decides the verdict: in the reply that delivers, is the packaging's own required-first element the first content in the reply.**

The required-first element differs by packaging because the two scenario files require different things, so the anchor is side-specific and the rule applied to it is identical.

| Side | Required-first element | Anchor offset, taken as the earliest of |
|---|---|---|
| project | the Deliverable Block | the literal `<DELIVERABLE>`, a line matching `^[ \t]*\*{0,2}Mode:`, a line whose first non-blank characters are a triple backtick fence opener |
| skill | the saved-path line | a line matching `^[ \t]*\*{0,2}\s*(Saved\|Exported\|Export path\|Export-equivalent path)\b`, the literal `export/` |

Then, on both sides:

- **PASS** when the text before that offset is empty after stripping whitespace
- **FAIL** when it is not empty
- **NO-DELIVERY** when no anchor exists, which is how a turn 1 that asks the permitted consolidated question is recognised rather than graded

The scored reply is the first reply in the conversation chain that is not `NO-DELIVERY`. Turn 2 exists only when turn 1 asked, so this selects the delivery event on either branch without a choice being made by hand.

The whitespace-strip rule is not invented here. It is what `benchmark/grader/deliverable_lint.py:160` already does for `deliverable_not_first`, which is this system's own committed check, so the discriminator and the repo's existing check cannot disagree about what a prefix is.

### Where it comes from

- `sk-prompt-improver/manual-testing-playbook/project-text-modes/improve-flow-clear-canvas.md:32` and `:67` fail the Project side on "commentary precedes the block" and "Commentary before the block"
- `sk-prompt-improver/manual-testing-playbook/skill-text-modes/improve-flow-clear-export.md:32` and `:67` fail the skill side on "output appears before saving" and "Output shown before saving", and its pass line at `:66` asks for "the path-first compact reply shape"
- the committed verdict, `results.csv`, decided `PTX-001` on "a full transparency summary rendered before the Mode and prompt and Attestation block, this scenario's own contract names commentary before the block as a fail condition"

### It reproduces the committed verdicts

| Committed reply | Anchor found | Prefix, characters after stripping | Discriminator | Committed verdict |
|---|---|---:|---|---|
| `replies/PTX-001.md` | `<DELIVERABLE>` at line 11 | 729 | FAIL | FAIL |
| `replies/STX-001-turn2.md` | `Saved:` at line 1 | 0 | PASS | PASS |
| `replies/STX-001-turn1.md` | none | n/a | NO-DELIVERY | not the graded turn |

Both committed verdicts are reproduced, so the discriminator stands as written.

### What is tracked but decides nothing

Three columns are recorded alongside and none of them enters the verdict.

- **header field count** and **`Score:` present**, counted by splitting the `Mode:` line on `|`. `adjudication.md` section 4 reclassed the missing field as a rule gap: this scenario's fail line fails on an absent score, the score is present in chat at `replies/PTX-001.md:30`, and the Project's own `knowledge/Prompt Improver - Format Guide Markdown - v0.141.md:104` specifies a three-field header while `claude project/Custom Instructions.md:375` specifies four. The committed reply scores 3 fields with no `Score:`
- **prefix contains transparency reporting**, a fixed literal search of the prefix for `CLEAR`, `Score`, `Perspective`, `Assum`, `Framework`, `Complexity`, `docs consulted`, `DEPTH`, `Phase`, `energy`, `Gate`, `COSTAR`, `RCAF`. This separates a prefix that is the transparency report `Custom Instructions.md:323` places after the block from a prefix that is a bare heading or an environment disclosure. It is descriptive because the ordering rule forbids both

---

## 2. The runs

### Harness and configuration

From the `AI Systems` directory, per sample, one fresh session:

```
"z — Parity Gate/run_packaging.sh" "Prompt Improver" <skill|project> '<prompt>' --noweb --session $(uuidgen)
```

then `--resume <that uuid>` with the turn 2 prompt when turn 1 did not deliver. Prompts are the conversation chain's exact cells:

- turn 1, both sides: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- turn 2, both sides: `For a general audience blog post, markdown is fine.`

`--noweb` matches the committed run, recorded in `evidence/PTX-001.md:4` and `evidence/STX-001.md:4`. Model and effort are the harness defaults, `claude-sonnet-5` at medium, which is what the committed run used. The Project retrieval line is left on its default, present. Write tools are withheld from a Project run by default now, and the committed `PTX-001` Project run held them, so the new Project samples differ from the committed run on that point and match the fresh Project run `adjudication.md` made under an explicit `--no-write`.

### Sample counts

Five new samples per side, plus one reused sample per side carried over from the runs `adjudication.md` section 1 recorded, giving six per cell.

| Cell | New | Reused | Total |
|---|---:|---:|---:|
| skill | 5 | 1 | 6 |
| project, write tools withheld | 5 | 1 | 6 |

The reused pair are the sessions `EB01B26F-633E-4738-8A75-E3E67837584C` (skill) and `268C2720-D75B-4B8E-928F-C719D3396776` (Project, explicit `--no-write`). They ran under `run_packaging.sh` at commit `0f66565`, whose `--no-write` deny list is byte-identical to the current default's and whose `REBUILD=0` on resume is unchanged, so the model-facing configuration matches. The one thing not recorded for them is whether `--noweb` was passed. Neither transcript contains a `WebFetch` or `WebSearch` call and neither turn of this scenario has a web dependency, so they are carried as reused observations rather than as part of the registered five, and the five new samples per cell stand on their own.

---

## 3. Distribution

### Every sample, scored by the pre-registered test

The delivering reply is the one scored. Turn 2 exists on the branch where turn 1 asked, which is the permitted fork the conversation chain's turn 1 row allows on both sides.

| Cell | Sample | Source | Delivering turn | Prefix, characters | Prefix is transparency reporting | Discriminator |
|---|---|---|---|---:|---|---|
| skill | 1 | new | 2 | 0 | no | PASS |
| skill | 2 | new | 2 | 0 | no | PASS |
| skill | 3 | new | 2 | 0 | no | PASS |
| skill | 4 | new | 2 | 0 | no | PASS |
| skill | 5 | new | 2 | 0 | no | PASS |
| skill | reused `EB01B26F` | reused | 2 | 0 | no | PASS |
| project | 1 | new | 2 | 13 | no, a bare `# Deliverable` heading | FAIL |
| project | 2 | new | 2 | 522 | yes | FAIL |
| project | 3 | new | 1 | 17 | no, a bare `# Enhanced Prompt` heading | FAIL |
| project | 4 | new | 2 | 0 | no | PASS |
| project | 5 | new | 2 | 0 | no | PASS |
| project | reused `268C2720` | reused | 2 | 606 | yes | FAIL |

The two committed replies, for reference and not counted in either cell: `PTX-001.md` prefix 729 characters, transparency reporting, FAIL, and `STX-001-turn2.md` prefix 0 characters, PASS.

### Totals

| Cell | New | Reused | Total | PASS | FAIL |
|---|---:|---:|---:|---:|---:|
| skill | 5 | 1 | 6 | 6 | 0 |
| project, write tools withheld | 5 | 1 | 6 | 2 | 4 |

The skill cell is invariant. The project cell straddles the verdict boundary.

### Two things the distribution shows that the single run could not

**The committed defect is the minority of the Project failures.** Of the four Project samples that fail, two carry transparency reporting before the block, which is the defect the committed verdict named, and two fail on a bare markdown heading and nothing else. So "commentary before the block" fires in 4 of 6, and the specific transparency-report-first shape fires in 2 of 6. A repair aimed only at the transparency ordering would leave a third of the Project failures standing.

**The turn 1 branch is a within-packaging draw, now measured rather than argued.** One of five new Project samples delivered on turn 1 and four asked the consolidated question first. All five skill samples asked. `adjudication.md` section 2 called that branch within-packaging variance at a permitted fork on two runs, and six Project observations agree with it: the branch taken does not predict the verdict, since the one turn 1 delivery failed on a bare heading while two turn 2 deliveries passed outright.

### The separately tracked column, which decides nothing

Header field count on the `Mode:` line, with `Score:` present or absent:

| Cell | Sample | Header fields | `Score:` present |
|---|---|---:|---|
| project | 1 | 4 | yes |
| project | 2 | 3 | no |
| project | 3 | 4 | yes |
| project | 4 | 4 | yes |
| project | 5 | 4 | yes |
| project | reused `268C2720` | 4 | yes |

One Project sample of six drops the field, and the committed `PTX-001.md` is a second instance at 3 fields. The skill side renders no header line in chat at all, so the column is empty there by design. This is the shape `adjudication.md` section 4 predicted from the document conflict: a rule the same runtime satisfies most of the time and drops the rest of the time, under a document set that states it both ways. Sampling supports that reading and it still decides nothing, because the score is in chat where the scenario's own expected signals put it.

---

## 4. Verdict

**The `STX-001` / `PTX-001` divergence is a draw at the level the committed run measured it, and the packaging asymmetry underneath it is unsettled at six samples per side.**

Two claims have to be separated, because the single run conflated them.

**The committed Project FAIL does not reproduce deterministically, so it is a draw.** Two of six Project samples put the Deliverable Block first with nothing before it and pass the same mechanical test the committed reply fails. One configuration returns both verdicts, which is exactly the condition that makes a one-against-one twin comparison unable to tell a packaging difference from a draw. The committed `PTX-001` FAIL is a real observation of a real defect, and it is one draw from a biased coin rather than a property the packaging always exhibits.

**The rate asymmetry between the packagings is real in the sample and short of settled.** Zero of six on the skill side against four of six on the Project side is a two-sided Fisher exact p of 0.061. That is the direction `adjudication.md` section 3 predicted from the rule text, where `AGENTS.md:38` to `:42` sequences the file write ahead of any chat token and the Project carries the same substance as preferences in a numbered ALWAYS list, and the sample agrees with it without yet clearing a conventional threshold.

**What would settle it.** Two more samples per side at the same configuration. Holding the observed rates, seven per side gives a two-sided Fisher p of 0.021 and nine per side gives 0.009. The measurement is cheap, it is the same two harness calls per sample, and nothing else about the configuration needs to change. Until then the honest statement is that the skill side never failed in six tries, the Project side failed in four of six, and the single committed pair could not have distinguished those two facts from each other.

**What this does not touch.** The class `adjudication.md` assigned, runtime fault, is not regraded here. Sampling changes how often the fault fires, not whether the Project packaging's own five statements forbid the ordering the runtime chose. The `Score:` field stays a rule gap, and section 5 of that file is unaffected.


---

## 5. Evidence on disk

Every sample turn is preserved in `samples/` beside this file, so the counts in section 3 can be checked by walking that directory rather than by rerunning anything.

Naming: `TX-001-<arm>-<NN>-turn<N>.txt`, with `<arm>` one of `skill` or `project`, and `reused` in place of the number for the two carried-over samples.

Counted by walking the directory:

| What | Files |
|---|---:|
| turn 1 replies | 12 |
| turn 2 replies | 11 |
| **total** | **23** |

Twelve turn 1 files is twelve samples, which is the twelve rows section 3 counts, six per cell. Eleven turn 2 files rather than twelve is `TX-001-project-03`, the one sample whose turn 1 delivered, so the conversation chain's conditional turn 2 never fired. The table count and the file count agree.

No transcript extracts are kept here, and that is deliberate rather than an omission. The pre-registered discriminator reads reply text only, so no verdict in this file turns on a file write or a tool call, and an extract would be evidence for a claim nothing here makes. The `samples/` replies plus the discriminator are enough to reproduce every row of section 3.
