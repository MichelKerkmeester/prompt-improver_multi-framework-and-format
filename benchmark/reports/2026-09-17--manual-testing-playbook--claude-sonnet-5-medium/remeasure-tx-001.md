# Re-measurement of the header-field repair, Prompt Improver TX-001

Commit `076133a` removed a fourth field, `Score:`, from the kernel's delivery-protocol header template and dropped the same field from `benchmark/grader/deliverable_lint.py`'s required-field list. No post-repair measurement existed. This file is that measurement. Report only, nothing repaired, nothing committed. Paths are relative to `AI Systems/Prompt Improver/` unless stated otherwise.

`sampling.md`, `adjudication.md`, `verdict.md`, `results.csv` and `deliverable-lint.csv` in this directory are untouched. The scenario files are untouched. Section 8 states how the `deliverable-lint.csv` overwrite trap was avoided and proves the file is byte-identical to HEAD.

---

## 1. What changed, read from the files rather than from any prose

The complete model-facing delta on the Project side between the commit the pre-repair samples ran under and HEAD is four hunks in one file, `claude project/Custom Instructions.md`, obtained with `git diff 076133a~1 HEAD` on that path:

| Hunk | Change | Source commit | Behavioural |
|---|---|---|---|
| header line | `v1.4.4` to `v1.4.6` | three commits | no |
| `:291` Claude Projects Delivery Override | one sentence added, "Whatever file tools appear to be available, never hand back a path or a save confirmation in place of the rendered Artifact" | `fb08df0`, a fleet change, not this repair | possibly, see section 7 |
| `:375` DELIVERY PROTOCOL template | `Mode: $[mode] \| Complexity: [level] \| Framework: [Framework] \| Score: [CLEAR/EVOKE/VISUAL score]` to `Mode: $[mode] \| Complexity: [level] \| Framework: [Framework]` | `076133a`, the repair | yes |
| `:387` export-equivalent path | `export/NNN`, "where `NNN` is a placeholder" to `export/[###]`, "where `[###]` is a placeholder" | `076133a`, the repair | yes |

`git diff 076133a~1 HEAD` over `claude project/knowledge/` and `sk-prompt-improver/` returns nothing, so no knowledge document and no skill file changed between the two measurements. That makes the skill arm a genuine control rather than an assumed one.

The lint's required-field list now reads `REQUIRED_HEADER_FIELDS = ("Complexity:", "Framework:")` at `benchmark/grader/deliverable_lint.py:68`, three fields expected with `Score:` deliberately absent.

Counts checked by parsing, not by reading a report:

- `grep -n "Mode:"` on `sk-prompt-improver/assets/format-guide-markdown.md` returns seven lines, of which `:112` is `**CLI/Agent Mode:** Save to /Export folder`, a save instruction and not a header, leaving six three-field header statements at `:118`, `:139`, `:149`, `:177`, `:221`, `:258`
- the same grep on `claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md` returns the same shape, six three-field header statements at `:104`, `:125`, `:135`, `:163`, `:207`, `:244`
- `grep -rn "| Score:"` across the whole system returns hits only inside this report directory, all of them historical replies and prose about the conflict, so no live document states the four-field form any more
- the kernel contains exactly one `Mode: $[mode]` occurrence, at `:375`

So the six-places-each claim holds, and the outlier is gone rather than propagated.

---

## 2. The two pre-registered discriminators

Both written before any post-repair run. Neither revised afterwards. Both read reply text only, so no verdict here turns on a tool call or a file write.

### Discriminator O, ordering

Transcribed unchanged from `sampling.md` section 1, because a re-measurement that redefines the test measures a different thing. Side-specific anchor, identical rule applied to it:

| Side | Anchor offset, taken as the earliest of |
|---|---|
| project | the literal `<DELIVERABLE>`, a line matching `^[ \t]*\*{0,2}Mode:`, a line whose first non-blank characters are a triple backtick fence opener |
| skill | a line matching `^[ \t]*\*{0,2}\s*(Saved\|Exported\|Export path\|Export-equivalent path)\b`, the literal `export/` |

Then on both sides, PASS when the text before that offset is empty after stripping whitespace, FAIL when it is not, NO-DELIVERY when no anchor exists. The scored reply is the first reply in the chain that is not NO-DELIVERY.

### Discriminator H, header field count

The method `sampling.md` section 3 used for its separately tracked column: find the header line, split it on `|`, count the non-empty fields, and record whether any field's label is `Score`. Formally, the first line matching `^[ \t]*\*{0,2}\s*Mode:.*$`, `**` stripped, split on `|`.

H is reported alongside the committed lint's own `header_malformed` verdict, computed twice per reply by importing `lint_reply` and swapping `REQUIRED_HEADER_FIELDS` in memory, once with the repaired two-field requirement and once with the pre-repair three-field requirement. That gives the check-facing observable under both rule sets on the same text.

### Both reproduce the prior recorded outcomes on the persisted pre-repair samples

Walked from `samples/` by splitting each filename on `-`, not by a glob. Twenty-three files, twelve arms, matching `sampling.md` section 5.

| Cell | Sample | Prior prefix chars | Measured prefix chars | Prior discriminator | Measured | Prior header fields | Measured H | Prior `Score:` | Measured |
|---|---|---:|---:|---|---|---:|---:|---|---|
| skill | 1 to 5, reused | 0 | 0 | PASS | PASS | none rendered | none | n/a | n/a |
| project | 1 | 13 | 13 | FAIL | FAIL | 4 | 4 | yes | yes |
| project | 2 | 522 | 522 | FAIL | FAIL | 3 | 3 | no | no |
| project | 3 | 17 | 17 | FAIL | FAIL | 4 | 4 | yes | yes |
| project | 4 | 0 | 0 | PASS | PASS | 4 | 4 | yes | yes |
| project | 5 | 0 | 0 | PASS | PASS | 4 | 4 | yes | yes |
| project | reused `268C2720` | 606 | 606 | FAIL | FAIL | 4 | 4 | yes | yes |

The two committed replies reproduce as well: `replies/PTX-001.md` prefix 729 characters, FAIL, H = 3, no `Score:`, and `replies/STX-001-turn2.md` prefix 0, PASS, with `STX-001-turn1.md` NO-DELIVERY. Twelve of twelve arms and three of three committed replies match. Both discriminators stand as written.

### The lint half of the repair, validated on a controlled pair

Built in the scratchpad, two headers differing in one field:

| File | Fields | Pre-repair check | Repaired check |
|---|---:|---|---|
| a correct three-field header, `Mode: $improve \| Complexity: 3/10 \| Framework: RCAF` | 3 | `header_malformed` x1 | clean |
| a header missing its `Framework` field, `Mode: $improve \| Complexity: 3/10` | 2 | `header_malformed` x1 | `header_malformed` x1 |

One violation each before, so the old check could not distinguish a correct header from a malformed one and its finding carried no information. The repaired check passes the correct one and still catches the malformed one. The repair commit's stated basis reproduces.

---

## 3. Which observable the repair should move, and why

The repair changed one rule and one check. It changed nothing about ordering. So:

**It should move the header field count the Project runtime produces, from predominantly four to three.** The kernel was the only document in either packaging that ever specified four fields. Twelve statements of the three-field form stood against it, six in each markdown format guide. With the outlier removed there is no document left that asks for a `Score:` field in the header, and `ALWAYS 18` at `:323` already puts score, assumptions and docs consulted in chat after the block. This is the observable with a causal path from the edited bytes to the reply.

**It should also drive the check's spurious `header_malformed` finding to zero.** That is the finding `adjudication.md` section 4 identified as carrying no information and `README.md:58` mistook for a second independent defect. Two halves are needed for it, and this is the part worth saying plainly: had only the kernel been repaired, the spurious finding would have got five times worse rather than better, because every correct three-field header the new kernel produces trips the old check. Section 6 measures exactly that counterfactual.

**The ordering rate is expected to be untouched.** `ALWAYS 16` at `:321` and `ALWAYS 18` at `:323` are byte-identical across the diff. The ordering defect is recorded as a runtime fault, deliberately unrepaired, at `z — Parity Gate/episodes/hand-run/011-fleet-capability-leak/runtime-faults-recorded.md:92`, and that record's own reason for attempting nothing is that only two of the four Project failures carried transparency reporting while the other two failed on a bare markdown heading. Nothing in this repair addresses either shape. Ordering is carried as the pre-registered null.

---

## 4. The runs

From the `AI Systems` directory, one fresh session per arm:

```
"z — Parity Gate/run_packaging.sh" "Prompt Improver" <skill|project> '<turn 1 prompt>' --noweb --session $(uuidgen)
```

then `--resume <that uuid>` with the turn 2 prompt on the branch where turn 1 asked rather than delivered, which is the fork the conversation chain's turn 1 row permits on both sides. Prompts are the chain's exact cells:

- turn 1, both sides, `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- turn 2, both sides, `For a general audience blog post, markdown is fine.`

`--noweb` matches the committed run and the prior sampling. Model and effort are the harness defaults, `claude-sonnet-5` at medium. The Project retrieval line is left on its default, present. Write tools are withheld from a Project run by default, which matches the prior sampling's Project cell.

Five arms per side. All ten asked the consolidated question on turn 1 and delivered on turn 2, so all ten arms have both declared turns.

| Cell | Arms | Turn 1 files | Turn 2 files |
|---|---:|---:|---:|
| skill, post-repair | 5 | 5 | 5 |
| project, post-repair | 5 | 5 | 5 |

### One pilot run, reported and not counted

A first skill arm was launched with `HARNESS_SCRATCH` pointed at this session's scratchpad rather than left at the harness default. It is persisted as `samples/TX-001-skill-postpilot-x-turn*.txt` and excluded from the five, because the five must all sit on one configuration and the prior sampling ran on the default root.

It is reported rather than dropped, because what it did is worth knowing. That run did not bind the skill identity at all. Its transcript shows one `Skill` tool call, then `find / -maxdepth 6 -iname "SKILL.md" -path "*prompt-improver*"`, then a second bounded find, none of which reached `sk-prompt-improver/SKILL.md` because the scratch tree sits deeper than the bound. It then wrote a plain improved prompt with no export, no path-first shape and no scoring gate. Discriminator O returns NO-DELIVERY on both of its turns, so it has no graded reply under the pre-registered test. The depth bound would have defeated that same `find` under the default root too, so this is the model choosing a bounded absolute search over a relative read rather than an artifact of the override. None of the five registered skill arms repeated it. All five read `SKILL.md` directly.

---

## 5. Before and after

Pre-repair rows are the persisted samples, re-scored here rather than copied from `sampling.md` prose. `blockH` is a second header column added after the runs and labelled as such, described in section 6.

### Skill cell, the control

| Cell | Sample | Graded turn | Prefix chars | Prefix is transparency | ORDERING | H | `Score:` | `header_malformed`, repaired check |
|---|---|---|---:|---|---|---|---|---|
| skill | pre 1 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | pre 2 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | pre 3 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | pre 4 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | pre 5 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | pre reused | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | post-01 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | post-02 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | post-03 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | post-04 | 2 | 0 | no | PASS | none rendered | n/a | 0 |
| skill | post-05 | 2 | 0 | no | PASS | none rendered | n/a | 0 |

Every skill reply is path-first, the first line being `Saved:` or `**Saved:**` followed by the export path. The chat reply renders no `Mode:` header on this side, before or after, so the H column is empty by design exactly as `sampling.md` recorded.

### Project cell

| Cell | Sample | Graded turn | Prefix chars | Prefix shape | ORDERING | H | blockH | `Score:` | `header_malformed`, pre-repair check | `header_malformed`, repaired check |
|---|---|---|---:|---|---|---:|---:|---|---:|---:|
| project | pre 1 | 2 | 13 | bare `# Deliverable` heading | FAIL | 4 | 4 | yes | 0 | 0 |
| project | pre 2 | 2 | 522 | DEPTH phase summary | FAIL | 3 | 3 | no | 1 | 0 |
| project | pre 3 | 1 | 17 | bare `# Enhanced Prompt` heading | FAIL | 4 | 4 | yes | 0 | 0 |
| project | pre 4 | 2 | 0 | none | PASS | 4 | 4 | yes | 0 | 0 |
| project | pre 5 | 2 | 0 | none | PASS | 4 | 4 | yes | 0 | 0 |
| project | pre reused | 2 | 606 | DEPTH phase summary | FAIL | 4 | 4 | yes | 0 | 0 |
| project | post-01 | 2 | 0 | see the note below | PASS | 1 | 3 | no | 1 | 0 |
| project | post-02 | 2 | 0 | none | PASS | 3 | 3 | no | 1 | 0 |
| project | post-03 | 2 | 13 | bare `# Deliverable` heading | FAIL | 3 | 3 | no | 1 | 0 |
| project | post-04 | 2 | 13 | bare `# Deliverable` heading | FAIL | 3 | 3 | no | 1 | 0 |
| project | post-05 | 2 | 335 | environment disclosure naming assumptions | FAIL | 3 | 3 | no | 1 | 0 |

The committed replies, for reference and counted in neither cell: `replies/PTX-001.md` prefix 729 characters of transparency reporting, FAIL, H = 3, no `Score:`, `header_malformed` under the pre-repair check and clean under the repaired one. `replies/STX-001-turn2.md` prefix 0, PASS.

### Totals

| Observable | Cell | Before | After |
|---|---|---|---|
| ORDERING FAIL | skill | 0 of 6 | 0 of 5 |
| ORDERING FAIL | project | 4 of 6 | 3 of 5 |
| header carries a `Score:` field | project | 5 of 6, and 5 of 7 counting the committed reply | 0 of 5 |
| header field count is three | project | 1 of 6 | 5 of 5 by `blockH`, 4 of 5 by the pre-registered H |
| `header_malformed`, repaired check | project | 0 of 6 | 0 of 5 |
| `header_malformed`, pre-repair check applied to the same replies | project | 1 of 6 | 5 of 5 |

---

## 6. Was the changed text in context, and which file carried it

Confirmed per sample from the transcript, not assumed. The Project side's system prompt is stored verbatim in the transcript at `attachment.systemPrompt[0]`, so the test is a literal string search of the bytes the model was given.

The file carrying the changed text is `claude project/Custom Instructions.md`. `run_packaging.sh` rsyncs it into the scratch root and passes its contents as `--system-prompt`, so on the Project side the repaired lines are in context by construction and the transcript confirms it.

| Cell | Sample | System prompt chars | Three-field template present | Four-field template present | `[###]` present | `NNN` present | Knowledge documents read, in order |
|---|---|---:|---|---|---|---|---|
| project | post-01 | 23014 | yes | no | yes | no | Interactive Mode, DEPTH, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown |
| project | post-02 | 23014 | yes | no | yes | no | Interactive Mode, DEPTH, Framework Pattern Library, Format Guide Markdown |
| project | post-03 | 23014 | yes | no | yes | no | none |
| project | post-04 | 23014 | yes | no | yes | no | none |
| project | post-05 | 23014 | yes | no | yes | no | none |
| skill | post-01 to post-05 | 8257 | no | no | no | no | `SKILL.md` first, then two or three references |

The skill side's system prompt is `AGENTS.md`, and neither template appears in it, which is correct because the repair touched no skill file. The skill arm therefore tests that nothing moved where nothing changed.

**The read-order confound the prior adjudication identified is gone, and the transcripts show why.** `adjudication.md` section 4 established that the committed `PTX-001` read `Format Guide Markdown - v0.141.md` last and followed its three-field template over the kernel's four-field one. That mechanism cannot operate now, because the two documents agree. The evidence is stronger than agreement alone: three of five Project samples read no knowledge document at all, had only the kernel in context, and produced the three-field header anyway. The kernel alone now yields it.

**The pre-repair side of that claim is checkable too, and checks out.** Six Project transcripts from the prior sampling survive on disk. All six carry a 22921-character system prompt containing the four-field template and not the three-field one. Their headers, matched back to the persisted replies, are the five with `Score:` and the one without. The one without, session `112C43C5`, read the Format Guide last, which is the same mechanism `adjudication.md` named for the committed reply. So the before and after differ on exactly the bytes the repair changed, in the direction the repair intended, with the confounding document read now inert.

### Two honest notes on the discriminators

**Discriminator H has a blind spot that post-01 exposed.** That reply opens with `**Mode:** Text detected via keyword ("prompt") · **Framework:** COSTAR ... · **Complexity:** 3/10 · **Energy:** Standard`, a transparency line separated by `·` rather than `|`. H matches it, splits on `|`, and returns one field. The reply's actual block header three lines later is `Mode: $text | Complexity: 3/10 | Framework: COSTAR`, three fields with no `Score:`. The `blockH` column in section 5 reads the block header using the lint's own unbolded `^\s*Mode:` anchor. It is declared here as a post-hoc second column, not as a revision of H, and it changes no pre-repair number: H and `blockH` agree on all twelve pre-repair arms and both committed replies, and differ on post-01 alone.

**Discriminator O returns a false PASS on that same reply, and it is reported as PASS anyway.** The project anchor accepts `^[ \t]*\*{0,2}Mode:`, the transparency line matches it at offset zero, and the prefix is therefore empty. Anchored instead on the fence that opens the real block, the prefix is 450 characters of transparency reporting, which is what `project-text-modes/improve-flow-clear-canvas.md:32` fails on as "commentary precedes the block". The pre-registered verdict is kept because changing a discriminator after seeing the data is how a null gets manufactured. The consequence is stated instead: the project ORDERING FAIL count is 3 of 5 as pre-registered, and 4 of 5 read against the scenario's own fail line. Section 7 gives both.

---

## 7. Did each observable move

**The header field count moved, in the direction the repair intended.** The `Score:` field went from 5 of 6 Project samples to 0 of 5, or 5 of 7 to 0 of 5 counting the committed reply as a seventh pre-repair observation. Two-sided Fisher exact is p = 0.015 on the first framing and p = 0.028 on the second. The three-field form went from 1 of 6 to 5 of 5. The mechanism is confirmed rather than inferred: the four-field template was in the system prompt of every pre-repair sample and is in none of the post-repair ones, and three post-repair samples reached the three-field header with the kernel as their only context.

**The spurious check finding is gone, and the lint half of the repair was load-bearing rather than cosmetic.** Under the repaired check, `header_malformed` is 0 of 5 after and was 0 of 6 before, so that column alone shows nothing. The informative number is the counterfactual on the same text: the pre-repair check applied to the five post-repair replies fires on 5 of 5. Had the kernel been repaired and the lint left alone, the spurious finding would have gone from 1 in 6 to 5 in 5, because the check would have been failing every correct header the new kernel produces. Both halves were needed and the pair is consistent.

**The ordering rate did not move.** Project FAIL is 4 of 6 before and 3 of 5 after, a two-sided Fisher exact of p = 1.0 between them, which is no detectable movement at this size. Skill FAIL is 0 of 6 before and 0 of 5 after. The packaging asymmetry is 0 of 5 against 3 of 5 after, p = 0.167, weaker than the 0.061 the prior sampling measured at six per side purely because the cells are smaller. Read against the scenario's fail line rather than the pre-registered anchor, the asymmetry is 0 of 5 against 4 of 5, p = 0.048. Either way the ordering fault still fires and still fires only on the Project side, which is what the unrepaired record predicts.

**The failure shapes stayed split, and the split shifted the wrong way for a future ordering repair.** Before, two of four Project failures carried transparency reporting and two failed on a bare markdown heading. After, two of three fail on a bare `# Deliverable` heading and one on an environment disclosure that names its assumptions. Counting post-01 as the fourth failure it behaviourally is, one of four is a transparency-report-first prefix. A repair aimed at the transparency ordering would now leave three of four standing rather than two of four. That is worth recording before anyone attempts one.

**Nothing moved in a direction the repair did not intend, with one thing that did not move at all.** The placeholder half of the repair, `NNN` to `[###]`, is unmeasurable on this scenario at this size. Every Project sample, before and after, reports a guessed `export/001 - ...` rather than emitting either literal placeholder, so the change is invisible in behaviour. Separately, the scenario's expected signals at `improve-flow-clear-canvas.md:30` still ask for "the `NNN` placeholder" while the kernel now says `[###]`, so the repair moved a document away from the scenario's prose. No pass or fail line turns on it, on either side of the change, so no verdict here moves either. It is flagged because it is a new disagreement the repair created and nothing in the tree records it.

**One co-change the ordering null cannot separate from the repair.** `fb08df0` added one sentence to the kernel at `:291`, "Whatever file tools appear to be available, never hand back a path or a save confirmation in place of the rendered Artifact." It is a delivery-shape sentence, so an ordering effect from it is conceivable. The ordering rate did not move, so whatever that sentence did, it did not produce a measurable ordering change here either. It cannot affect the header column, which names no field it mentions.

---

## 8. How the `deliverable-lint.csv` overwrite trap was avoided

`verdict.md` records the trap. `benchmark/grader/check_report.sh` runs `lint_replies.py`, which writes `deliverable-lint.csv` into the report directory as a side effect, and since the repair landed after the report was committed the regenerated file disagrees with the committed one on the `PTX-001.md` line.

Avoided by never running either tool against this directory. `check_report.sh` was read and not executed. `lint_replies.py` was read and not executed. The lint verdicts in section 5 come from importing `lint_reply` out of `deliverable_lint.py` inside a scratchpad script and calling it on reply text in memory. That function reads a string and returns a list. It opens no file for writing and `lint_replies.py`, the only writer, was never on the call path.

Proved rather than asserted. The csv was hashed before any measurement began and again after every run:

```
57773eaea241018b7fb57f18ab9a440eacb27eac88640203b3a28e84e61caa7c  deliverable-lint.csv
```

Identical both times, and `git diff` on that path is empty. `git status --short` over `AI Systems/Prompt Improver/` shows no modified tracked file, only the untracked sample files this measurement added.

The disagreement `verdict.md` describes was confirmed without regenerating anything: running the repaired `lint_reply` on `replies/PTX-001.md` in memory returns `deliverable_not_first` x1 alone, against the committed row's `header_malformedx1, deliverable_not_firstx1`. That is the one line, reproduced from the same code the script would have run, with nothing written.

Two further write checks, because a write tool takes an absolute path and a clean scratch tree proves nothing about the rest of the disk. The skill arms keep their write tools by design and all five wrote an export. `git status` over the repository shows no file created anywhere under `Prompt Improver/` except the samples, and `export/` in the repository still holds only `.gitkeep`. Walking the harness scratch root confirms all five exports landed inside their own session directory, one per registered skill session id.

---

## 9. Evidence on disk

Every turn of every arm is persisted in `samples/` beside this file, so section 5 can be checked by walking that directory rather than by rerunning anything.

Naming: `TX-001-<arm>-post-<NN>-turn<N>.txt`, with `post` marking the post-repair set, alongside the pre-repair `TX-001-<arm>-<NN>-turn<N>.txt` files the prior sampling left. The pilot uses `postpilot-x` so it cannot be mistaken for one of the five.

Counted by walking the directory, not by a glob that would stop at the space in the path above it:

| What | Files |
|---|---:|
| pre-repair, already present | 23 |
| post-repair, registered, turn 1 | 10 |
| post-repair, registered, turn 2 | 10 |
| post-repair, pilot | 2 |
| **added by this measurement** | **22** |
| **directory total** | **45** |

Ten turn 1 files and ten turn 2 files is ten arms with both declared turns, which is the ten post-repair rows section 5 counts, five per cell. The table count and the file count agree.

Session ids, so a reader can find the transcripts under `~/.claude/projects/` and repeat section 6:

| Cell | Sample | Session |
|---|---|---|
| skill | post-01 | `5159FAC6-F7A0-4B85-BFA8-480C47F5476A` |
| skill | post-02 | `4E4BEB36-874D-45DB-80FC-83CAD3B7B530` |
| skill | post-03 | `2A127BA0-521E-4FA1-BB55-5A477C962A82` |
| skill | post-04 | `8DC43E65-E00A-4C51-843E-F7E90E2E8DFF` |
| skill | post-05 | `DB538DBD-2A79-416A-8571-E1D6108C4069` |
| project | post-01 | `07D7707D-8B22-4DD6-828D-44306D741256` |
| project | post-02 | `32425CF8-FA3A-48A0-A22D-379627E41EBE` |
| project | post-03 | `7C5D1CE0-EABC-4582-BA16-0BE4F9260A9F` |
| project | post-04 | `D8E7F40F-200B-4CE7-B97D-6EBCDB9FC222` |
| project | post-05 | `B9B367AB-D24C-42DE-B269-EADB58DDDEAE` |
| skill, pilot | postpilot | `89CF1F66-72E6-4C27-B149-0BE5971E0BC2` |

One further Project session, `B51EFF18-14EE-4C58-8083-1EB7F1465B71`, sits in the same transcript directory carrying the post-repair kernel and is not one of these. Its prompt and purpose are not recorded here, it is almost certainly a concurrent peer session's run per this tree's own convention about peer work, and it is excluded rather than guessed at.

---

## 10. What these numbers support, and what would settle the rest

**Supported.** The header field count moved, decisively for a sample this size, and the mechanism is confirmed from the transcripts rather than inferred from the rate. The spurious check finding is gone, and the counterfactual shows the lint edit was necessary rather than tidy. The skill arm, where nothing changed, moved on nothing.

**Not supported, and five per side cannot support it.** That the ordering rate is unchanged. A null is not certified by failing to reject it at five per side. What the numbers do support is narrower and worth stating exactly: the ordering fault still fires on the Project side after the repair, it still never fired on the skill side, and no evidence here suggests the repair improved or worsened it. The p = 1.0 between the before and after Project rates means the two samples are consistent with one rate, not that the rate is equal.

**One thing these samples settle that neither report settles alone.** The ordering text is byte-identical across the diff, so the eleven Project observations and eleven skill observations either side of the repair are draws on one rule. Pooled, the packaging asymmetry is 0 of 11 skill against 7 of 11 Project, two-sided Fisher exact p = 0.004, and 0 of 11 against 8 of 11 with post-01 read against the scenario's fail line, p = 0.001. That clears the threshold `sampling.md` section 4 could not reach at six per side. It is offered as a pooled read rather than a pre-registered one, and it carries the one caveat section 7 names, that `fb08df0` added a delivery-shape sentence to the kernel between the two halves of the pool.

**What would settle the rest.**

- the ordering asymmetry, if it is to be settled inside one configuration rather than pooled, needs seven per side at the observed rates for p = 0.021 and nine per side for p = 0.009, computed here rather than carried over, and those are the same two figures `sampling.md` section 4 gave
- the ordering null across the repair needs materially more than five per side, because distinguishing a 4-in-6 rate from a 3-in-5 rate at any useful confidence is a much larger measurement than detecting the header shift was, and it is worth deciding first whether that null is worth the runs given the fault is recorded unrepaired
- the header result would be strengthened cheaply by three or four more Project samples, which would take the `Score:` count from 0 of 5 to 0 of 8 or 0 of 9 and put the pre-repair comparison well under p = 0.01
- Discriminator O's false PASS on a `·`-separated bolded transparency line should be settled in `sampling.md`'s own pre-registration before the next round rather than patched per report, because two reports now score the same anchor and only one has met the variant
- the placeholder half of the repair needs a scenario whose pass line actually reads the placeholder, since no sample on either side of the change emits either form, and the scenario prose at `improve-flow-clear-canvas.md:30` should be reconciled with the kernel either way
