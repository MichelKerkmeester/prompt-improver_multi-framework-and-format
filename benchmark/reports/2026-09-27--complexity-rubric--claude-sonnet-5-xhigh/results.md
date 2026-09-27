# Results: Prompt Improver complexity-rubric run, 2026-09-27, claude-sonnet-5 at effort xhigh

## 1. OVERVIEW

Every row below is printed from `results.csv`. The twin classes come from the adjudications in `grading-notes.md`. Each verdict applies the scenario's Pass/fail line as it stood at the run, Prompt Improver `4da1a1a`, so the six creative pairs are graded against their tiers before the re-tier.

---

## 2. ALL 48 SCENARIOS

| ID | Runtime | Verdict | Turns run | Facts intact | Reason |
|---|---|---|---:|---|---|
| PFW-001 | project | PASS | 1/1 | yes | Block first with header and attestation, RCAF at Medium (6/10), four labelled elements, CLEAR 43/50 passed, facts kept and no scope expansion |
| PFW-002 | project | FAIL | 1/1 | yes | The header complexity Complex (9/10) sits outside the High tier while every other item holds |
| PFW-003 | project | PASS | 1/1 | yes | Block first with header and attestation, RCAF at Complex (9/10), four labelled elements, CLEAR 44/50 passed, facts kept and no scope expansion |
| PFW-004 | project | FAIL | 1/1 | yes | The header complexity High (7/10) sits outside the Medium tier while every other item holds |
| PFW-005 | project | FAIL | 1/1 | no | The header complexity Complex (9/10) sits outside the High tier, the YAML payload does not parse and the invented year 2026 alters the 1 March date |
| PFW-006 | project | FAIL | 1/1 | no | The prompt rewrites the user's own clinics as Barter's clinics, an altered fact, while header, elements, CLEAR and delivery hold |
| PFW-007 | project | FAIL | 1/1 | yes | An environment note precedes the block, the header reads High (7/10) against the Medium tier, the YAML payload does not parse and a purpose statement plus a conditional approval marking are added outputs |
| PFW-008 | project | FAIL | 1/1 | no | The separate macOS and Ubuntu paths become a split only where steps differ, with identical steps stated once, which alters a supplied fact |
| PFW-009 | project | PASS | 1/1 | yes | Block first with header and attestation, CIDI at Complex (10/10), four labelled keys, CLEAR 44/50 passed, JSON parses, every fact kept and no scope expansion |
| PFW-010 | project | FAIL | 1/1 | no | A lead-in sentence precedes the block, the header reads High (7/10) against the Medium tier and our employment-law firm becomes the invented name Barter |
| PFW-011 | project | FAIL | 1/1 | no | The approved list of 38 EU-authorised health claims becomes up to 38, which alters a supplied number |
| PFW-012 | project | FAIL | 1/1 | yes | The prompt requires the structuring check result on every alert including not observed, an output the user did not ask for, so the scope test fails |
| PFW-013 | project | FAIL | 1/1 | no | Header complexity High (7/10) sits above the Medium tier and the 15% list-price premium is recast as 15% more per cup, with an added requirement that each test isolate the positioning story |
| PFW-014 | project | FAIL | 1/1 | no | Tier, block order, elements, gate and YAML parse hold but the prompt adds a one-depot-per-experiment rule and a conditional extra signal for a next cycle and alters route density to route density perceived as unmanageable |
| PFW-015 | project | FAIL | 1/1 | no | Tier and block order hold but the churn fact is recast as concentrated in small firms, an unsupplied hosting fact is added and invented example gaps such as GoBD, CAC and TAM seed the prompt |
| PFW-016 | project | FAIL | 1/1 | no | Commentary about mode detection and the missing Canvas panel precedes the block, the header complexity High (7/10) sits above the Medium tier, the pilot target gains an end-of-day deadline and unasked segments and checklist items are added |
| PFW-017 | project | FAIL | 1/1 | no | Tier and block order hold but phone-only field staff become phone or tablet users and the prompt adds a scope summary, per-phase execution summaries, a reconciliation check and a ticket monitoring and escalation step |
| PFW-018 | project | FAIL | 1/1 | yes | Header complexity High (8/10) sits below the Complex tier and the prompt adds an executive overview, per-workstream milestones, hypercare exit criteria and a named audience |
| PFW-019 | project | FAIL | 1/1 | no | Fails on commentary before the block, a Low (4/10) header outside the High tier and a dropped fact since Zeeland appears nowhere in the block, while the five FRAME labels, VISUAL 55/60, attestation, no-save and invitation hold |
| PFW-020 | project | FAIL | 1/1 | no | Fails on commentary before the block, a Medium (5/10) header outside the Complex tier, three unlabelled FRAME elements and altered facts since Leiden is dropped and the children are moved onto a rooftop terrace |
| PFW-021 | project | FAIL | 1/1 | yes | Fails only on tier because the header reads Medium (5/10) against the High band, with block-first delivery, six labelled MOTION elements, VISUAL ~64/70 passed, facts, scope and invitation holding |
| PFW-022 | project | FAIL | 1/1 | no | Fails on a Low (4/10) header outside the Complex tier, four of six MOTION elements with no key, the chime moved from the end to the clock start and no voices narrowed to no spoken dialogue |
| PFW-023 | project | FAIL | 1/1 | no | Fails on dropped facts since v0 is named in neither the header nor the body and the standing inspector is gone, while block order, High (7/10) tier, prose VIBE elements, EVOKE ~44/50, scope and invitation hold |
| PFW-024 | project | FAIL | 1/1 | yes | Fails only on tier because the header reads High (7/10) and the Complex tier needs 9 or 10 or a label above High, with every other item holding |
| SFW-001 | skill | FAIL | 1/1 | yes | The reply's first line is a verification note and not the saved export path, so path-first fails while header, elements, CLEAR, facts and scope all hold |
| SFW-002 | skill | FAIL | 1/1 | yes | The header complexity Complex (9/10) sits outside the High tier and the reply's first line does not name the saved path |
| SFW-003 | skill | PASS | 1/1 | yes | Path-first export with RCAF at Complex (10/10), four labelled elements, CLEAR 46/50 passed, facts kept and no scope expansion |
| SFW-004 | skill | PASS | 1/1 | yes | Path-first export with COSTAR at Medium (5/10), six labelled elements, CLEAR 44/50 passed, facts kept and no scope expansion |
| SFW-005 | skill | FAIL | 1/1 | no | The prompt states unsupplied facts as settled and requires the announcement to promise the allowance to everyone currently claiming it, and it adds a top-level placeholders section that holds no user fact |
| SFW-006 | skill | PASS | 1/1 | yes | Path-first export with COSTAR at Complex (9/10), all six elements labelled with Audience and Response per channel, CLEAR 45/50 passed, facts kept and no scope expansion |
| SFW-007 | skill | FAIL | 1/1 | yes | The reply opens with a parse note, not the saved path, so the path-first item fails while header, elements, CLEAR, YAML parse, facts and scope all hold |
| SFW-008 | skill | FAIL | 1/1 | no | The troubleshooting rule is widened from errors the CI config or README mention to failure modes drawn from all source files, which alters a supplied fact |
| SFW-009 | skill | FAIL | 1/1 | no | The reply opens with a validation note instead of the saved path and the process is narrowed from containers carrying lithium batteries to containers declared under UN3480 |
| SFW-010 | skill | FAIL | 1/1 | no | The user's one-line example note is recast as example input and its output becomes a five-line labelled block, so the supplied example is not kept |
| SFW-011 | skill | FAIL | 1/1 | yes | The reply opens with JSON body validated successfully instead of the saved path, so the path-first item fails while every other item holds |
| SFW-012 | skill | FAIL | 1/1 | no | The structuring flag is replaced by a ban on the word structuring and every claim cites a transaction ID is narrowed to claims drawn from transaction data |
| SFW-013 | skill | FAIL | 1/1 | no | Header complexity High (7/10) sits above the Medium tier and the prompt adds a trade-off or risk per route and a café-type justification the user did not ask for, with the cheap test narrowed to close to zero budget |
| SFW-014 | skill | FAIL | 1/1 | no | Tier, elements, gate and YAML parse hold but the prompt adds a risk-containment plan, a go or no-go criterion and a depot justification per experiment and narrows the pay assumption to pay per stop |
| SFW-015 | skill | FAIL | 1/1 | no | Header complexity High (8/10) sits below the Complex tier, the CFO route is tied to small-firm churn and the prompt adds evidence-to-close-each-gap and weakest-board-position outputs |
| SFW-016 | skill | FAIL | 1/1 | yes | Header complexity High (7/10) sits above the Medium tier and the prompt adds a welcome block, learning objectives, facilitation notes, per-session feedback capture and fixed table columns the user did not ask for |
| SFW-017 | skill | FAIL | 1/1 | no | The reply opens with File verified and saved instead of the path, the ticket target is rebased on 1,210 users and narrowed to migration-related tickets and the prompt adds an executive summary, sub-plans, a traceability section and a GDPR note |
| SFW-018 | skill | FAIL | 1/1 | yes | Header complexity High (7/10) sits below the Complex tier and the rollback section gains per-step time estimates the user did not ask for |
| SFW-019 | skill | FAIL | 1/1 | yes | Fails only on tier because the header reads Complexity Low (4/10) against the High band of 7 to 8, with export, path-first reply, five labelled FRAME elements, VISUAL 53/60, facts, scope and invitation all holding |
| SFW-020 | skill | FAIL | 1/1 | yes | Fails on a Medium (5/10) header outside the Complex tier, Focus, Rendering and Atmosphere having no labels, and a sampler suggestion the user did not ask for |
| SFW-021 | skill | FAIL | 1/1 | no | Fails on a Medium (5/10) header outside the High tier and a dropped fact since the 8 second close-up loses her thumbs smoothing the rim |
| SFW-022 | skill | FAIL | 1/1 | no | Fails on a reply that opens with a YAML check sentence instead of the saved path, a Low (3/10) header outside the Complex tier, the chime moved from the end to 8 seconds and a constraints section adding a no on-screen text or logos rule |
| SFW-023 | skill | FAIL | 1/1 | no | Fails on a reply that opens with a quality-check sentence instead of the saved path and on dropped facts since v0, the standing inspector and e-commerce are all missing from the file |
| SFW-024 | skill | FAIL | 1/1 | no | Fails on a Medium (6/10) header outside the Complex tier and on altered facts since MagicPath is named nowhere in the file and the app becomes a Dutch e-bike insurance app |

---

## 3. TWINS

| Pair | Skill | Skill verdict | Project | Project verdict | Agreement | Class and deciding rule |
|---|---|---|---|---|---|---|
| FW-001 | SFW-001 | FAIL | PFW-001 | PASS | disagree | runtime fault: path-first is a skill-only rule (`AGENTS.md` line 61, `SKILL.md` line 438), and the skill model opened with a verification note |
| FW-002 | SFW-002 | FAIL | PFW-002 | FAIL | agree | none |
| FW-003 | SFW-003 | PASS | PFW-003 | PASS | agree | none |
| FW-004 | SFW-004 | PASS | PFW-004 | FAIL | disagree | scenario tier: both twins read the same rubric, and the Project's High (7/10) matches both blind recounts (7 and 8) while the skill's Medium (5/10) matches the scenario tier |
| FW-005 | SFW-005 | FAIL | PFW-005 | FAIL | agree | none |
| FW-006 | SFW-006 | PASS | PFW-006 | FAIL | disagree | runtime fault with a package source: both packages carried "Barter" in the Interactive Mode closing line, and only the Project model wrote it into a prompt |
| FW-007 | SFW-007 | FAIL | PFW-007 | FAIL | agree | none |
| FW-008 | SFW-008 | FAIL | PFW-008 | FAIL | agree | none |
| FW-009 | SFW-009 | FAIL | PFW-009 | PASS | disagree | runtime fault: the same fact rule on both sides (`SKILL.md` line 478, kernel line 308), and the skill model narrowed the containers to UN3480 and opened with a validation note |
| FW-010 | SFW-010 | FAIL | PFW-010 | FAIL | agree | none |
| FW-011 | SFW-011 | FAIL | PFW-011 | FAIL | agree | none |
| FW-012 | SFW-012 | FAIL | PFW-012 | FAIL | agree | none |
| FW-013 | SFW-013 | FAIL | PFW-013 | FAIL | agree | none |
| FW-014 | SFW-014 | FAIL | PFW-014 | FAIL | agree | none |
| FW-015 | SFW-015 | FAIL | PFW-015 | FAIL | agree | none |
| FW-016 | SFW-016 | FAIL | PFW-016 | FAIL | agree | none |
| FW-017 | SFW-017 | FAIL | PFW-017 | FAIL | agree | none |
| FW-018 | SFW-018 | FAIL | PFW-018 | FAIL | agree | none |
| FW-019 | SFW-019 | FAIL | PFW-019 | FAIL | agree | none |
| FW-020 | SFW-020 | FAIL | PFW-020 | FAIL | agree | none |
| FW-021 | SFW-021 | FAIL | PFW-021 | FAIL | agree | none |
| FW-022 | SFW-022 | FAIL | PFW-022 | FAIL | agree | none |
| FW-023 | SFW-023 | FAIL | PFW-023 | FAIL | agree | none |
| FW-024 | SFW-024 | FAIL | PFW-024 | FAIL | agree | none |
