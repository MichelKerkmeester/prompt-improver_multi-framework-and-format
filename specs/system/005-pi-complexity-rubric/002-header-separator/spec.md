---
title: "Feature Specification: Prompt Improver header divider"
description: "Prompt Improver's exports and Deliverable Blocks put the Mode, Complexity and Framework header line directly on top of the prompt, so a reader copying the prompt can take the header with it. This phase puts a blank line, a --- divider and a blank line between the two on the skill, in the Claude Project, in the playbook, in the linter and in the 66 benchmark exports."
trigger_phrases:
  - "prompt improver header divider"
  - "header separate from prompt"
  - "export header separator"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Prompt Improver header divider

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-27 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 2 of 2 |
| **Predecessor** | 001-complexity-rubric |
| **Successor** | None |
| **Handoff Criteria** | The skill and the Project state the same layout, the parity gate passes on the commit, and every export in `export/benchmark/` carries the divider |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 2** of the Prompt Improver complexity rubric and export layout specification.

**Scope Boundary**: the layout of the delivered file and of the Deliverable Block. The header's fields, framework selection and scoring stay as they are.

**Dependencies**:
- Phase 001 committed and pushed, so the rule files start from a clean tree

**Deliverables**:
- The divider rule in `SKILL.md` and the three format guides, mirrored in the kernel and the three Project format guides
- Playbook wording and line citations that match the new layout
- A `deliverable_lint.py` check for the divider
- The 66 benchmark exports edited by hand, and the edit recorded in both run READMEs
- Skill 0.6.2, kernel v0.7.1, changelog and `SYNC.md` note

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Every Prompt Improver deliverable opens with a header line such as `Mode: $image | Complexity: 3/10 | Framework: FRAME | Platform: Midjourney`, and the prompt follows after one blank line, or directly on the next line in two of the 66 benchmark exports. The rules call this "a single-line header plus enhanced prompt content" (`sk-prompt-improver/SKILL.md` lines 499 and 558), so nothing marks where the metadata ends and the prompt begins, and a reader copying the prompt can take the header with it.

### Purpose
Every file and every Deliverable Block keeps its header visibly apart from the prompt: the header line, a blank line, `---`, a blank line, then the prompt.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The layout rule in `SKILL.md`, the three skill format guides and their examples
- The kernel's rule 7 and DELIVERY PROTOCOL template, and the three Project format guides
- Playbook scenarios that describe the file layout, and their line citations into the changed files
- `benchmark/grader/deliverable_lint.py` and the READMEs that list its checks
- The 33 skill and 33 Project exports in `export/benchmark/`, edited by hand
- Version records: skill 0.6.2, kernel v0.7.1, changelog, `SYNC.md`, READMEs

### Out of Scope
- The header's fields, including the `Platform:` field some creative exports carry - the operator asked for the layout only
- A rerun of the benchmark - the exports are edited by hand, as the operator asked
- The attestation footer's own divider, which already exists

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-prompt-improver/SKILL.md` | Modify | Format lock, rule 23 and Output File Rules name the divider; version 0.6.2 |
| `sk-prompt-improver/assets/format-guide-{markdown,json,yaml}.md` | Modify | Header section, allowed-content table, examples and checklists |
| `claude project/Custom Instructions.md` | Modify | Rule 7, DELIVERY PROTOCOL template, H1 v0.7.1 |
| `claude project/knowledge/Prompt Improver - Format Guide {Markdown,JSON,YAML} - v0.14x.md` | Modify | Same edits as the skill guides |
| `sk-prompt-improver/manual-testing-playbook/` | Modify | Layout wording and remapped line citations |
| `benchmark/grader/deliverable_lint.py` | Modify | A `header_divider_missing` check |
| `export/benchmark/skill/*`, `export/benchmark/claude project/*` | Modify | The divider added after each header |
| `benchmark/reports/2026-09-25--*/README.md`, `benchmark/reports/2026-09-27--*/README.md` | Modify | Record the hand edit |
| `sk-prompt-improver/changelog/v0.6.2.0.md`, `SYNC.md`, `README.md`, `sk-prompt-improver/README.md`, `claude project/README.md`, `sk-prompt-improver/description.json` | Create, Modify | Version and layout records |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The skill states the layout: header line, blank line, `---`, blank line, prompt |
| REQ-002 | The kernel and the Project format guides state the same layout, and the Deliverable Block template shows it |
| REQ-003 | JSON and YAML payloads below the divider still parse |
| REQ-004 | Every one of the 66 benchmark exports carries the divider, with the header and prompt text otherwise unchanged |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | Playbook scenarios describe the new layout and cite the right lines |
| REQ-006 | `deliverable_lint.py` reports a block whose header is not followed by the divider |
| REQ-007 | Versions, changelog, `SYNC.md` and both run READMEs record the change |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A scan of the 66 exports finds line 1 a `Mode:` header, line 2 blank, line 3 `---` and line 4 blank in every file
- **SC-002**: Residency, parity, router fixtures and the playbook validator all pass after the change
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A YAML reader treats `---` as a document start | Low | The header line was never valid YAML, and the rule already says the payload below the header parses. `---` only makes that boundary explicit |
| Risk | The Project block has two `---` lines, one above the prompt and one above the attestation | Med | The linter strips the leading divider before it strips the attestation, and the kernel template shows both |
| Risk | Inserted example lines shift playbook citations | Med | A HEAD-to-working line map applied to every citation into the changed files |
| Dependency | Residency-declared kernel statements | High | `run_residency.sh prompt-improver` after each kernel edit |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The divider adds two lines and three characters to each file, no token cost worth reporting

### Security
- **NFR-S01**: No secret or private data enters a rule, scenario or export

### Reliability
- **NFR-R01**: A reader can split header from prompt at the first `---` line in every export
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A prompt whose own body contains `---`: the divider is the first `---` after the header, so a later one belongs to the prompt
- A JSON export whose `{` sat on line 2: it moves to line 5
- A creative export with no blank line after the header: it gains both blank lines

### Error Scenarios
- A header with an extra field such as `Platform:` keeps it, and the divider goes after the whole line

### State Transitions
- The Project block keeps its attestation divider, so it now carries two `---` lines
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 15/25 | About 15 rule and tool files, 78 playbook scenarios, 66 exports, two repos |
| Risk | 12/25 | A shared output contract on both runtimes, residency-declared kernel text |
| Research | 4/20 | The layout is set by the operator |
| **Total** | **31/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator set the layout, chose a phase under 079 and asked for both export folders
<!-- /ANCHOR:questions -->

---
