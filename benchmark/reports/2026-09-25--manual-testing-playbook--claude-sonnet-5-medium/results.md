# Results: Prompt Improver playbook run, 2026-09-25, claude-sonnet-5 at effort medium

Every row below is printed from `results.csv`. The twin classes come from the adjudications in `grading-notes.md`. The counts in `README.md` come from `results.csv` by the command named there.

## All 14 scenarios

| ID | Runtime | Verdict | Turns run | Facts intact | Reason |
|---|---|---|---:|---|---|
| PCR-001 | project | PASS | 2/2 | yes | Turn 1 fenced block opens the reply with header and attestation, VISUAL 54/60 gate passed, Midjourney kept, share-back invite, [###] path, no save claimed |
| PFM-001 | project | PASS | 2/2 | yes | Turn 1 fenced block opens the reply, header Mode: $improve, payload between header and attestation parses, CLEAR 43/50, 5-10% overhead reported, no save claimed |
| PID-001 | project | PASS | 2/2 | yes | Turn 1 carries Canvas Artifact verbatim, fenced block opens the reply with header and attestation, [###] path, no save claimed, identity answer after the block |
| PIR-001 | project | PASS | 2/2 | yes | Turn 1 one consolidated question and no block, Turn 2 Short at Quick energy on the supplied prompt, CLEAR 43/50, block under a bold label before any commentary |
| PIR-002 | project | FAIL | 2/2 | yes | Turn 2 opens with a route disclosure and a no-Canvas note before the block, so under the stand-in rule the panel reads empty and no Canvas Artifact was delivered |
| PSB-001 | project | PASS | 2/2 | n-a | Turn 1 reframes once as a prompt offer, Turn 2 refuses, no email copy and no Deliverable Block on either turn |
| PTX-001 | project | PASS | 2/2 | yes | Turn 1 fenced header and prompt open the reply with the attestation directly below, CLEAR 44/50, [###] path, no save claimed, summary over the band (advisory) |
| SCR-001 | skill | PASS | 2/2 | yes | Turn 1 path-first, export/001 exists with header and Midjourney prompt, VISUAL 54/60 gate passed, share-back invite, Turn 2 saved 002 |
| SFM-001 | skill | FAIL | 2/2 | yes | Turn 1 delivery holds (header, payload parses, overhead) but the Turn 2 revision adds a risks_and_blockers extraction plus priority and dependencies fields, a blocking scope expansion |
| SID-001 | skill | PASS | 2/2 | yes | Turn 1 path-first, export/001 exists with header and prompt, no Canvas or no-save claim, identity phrase paraphrased (support only) |
| SIR-001 | skill | PASS | 2/2 | yes | Turn 1 one consolidated question and no file, Turn 2 bound Short at Quick energy, CLEAR 43/50, export/001 path-first on the supplied prompt |
| SIR-002 | skill | PASS | 2/2 | yes | Turn 1 one consolidated question and no file, Turn 2 export/001 built from Turn 2 facts only, CLEAR 44/50, path-first |
| SSB-001 | skill | PASS | 2/2 | n-a | Turn 1 reframes once as a prompt offer, Turn 2 refuses, no email copy and an empty ledger on both turns |
| STX-001 | skill | FAIL | 2/2 | yes | Graded Turn 1 file asks for a meta description and a subheadings list the user never requested (scope expansion), and Turn 2 edited export/001 in place instead of saving 002 |

## Twins

| Pair | Skill | Skill verdict | Project | Project verdict | Agreement | Class and deciding rule |
|---|---|---|---|---|---|---|
| ID-001 | SID-001 | PASS | PID-001 | PASS | agree | none |
| IR-001 | SIR-001 | PASS | PIR-001 | PASS | agree | none |
| IR-002 | SIR-002 | PASS | PIR-002 | FAIL | disagree | runtime fault: kernel lines 319, 321 and 401 put the block before any commentary, the Project model opened with a route disclosure and a no-Canvas note |
| TX-001 | STX-001 | FAIL | PTX-001 | PASS | disagree | runtime fault: the same scope ban on both sides (SKILL.md lines 507 to 508, kernel line 335), and only the skill model wrote an unrequested meta description output. Its Turn 2 in-place edit of 001 has no Project counterpart and is logged as a follow-up |
| FM-001 | SFM-001 | FAIL | PFM-001 | PASS | disagree | runtime fault: the same scope ban (SKILL.md lines 507 to 508, kernel line 335), the skill Turn 2 revision added a risks_and_blockers extraction |
| CR-001 | SCR-001 | PASS | PCR-001 | PASS | agree | none |
| SB-001 | SSB-001 | PASS | PSB-001 | PASS | agree | none |
