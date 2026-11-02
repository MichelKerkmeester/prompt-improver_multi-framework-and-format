---
title: "Feature Specification: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit"
description: "A pasted prompt could pick Prompt Improver's mode, a request that carried everything still drew a question before the deliverable, and a claude.ai reply rendered the prompt where its copy button copied a header and footer too. This packet fixes all three."
trigger_phrases:
  - "deal templates upgrades"
  - "deal templates upgrades user word routing deliver first"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-18 |
| **Branch** | `main` (no commit, the operator commits) |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The router read the whole message, so the words inside a pasted prompt could choose the mode: a text prompt about photo editing routed to Image with VISUAL scoring. The interactive flow asked framework, simplification, format and component library questions before writing anything, and assumptions lived in four places. On claude.ai the prompt sat in a Canvas Artifact with a header and an attestation footer, so copying it copied those too and a JSON or YAML payload stopped parsing.

### Purpose
The mode comes from the user's own words, the improved prompt arrives in the first reply with every default listed as a numbered open item, and the claude.ai copy unit is the prompt alone.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- R1: set the pasted prompt aside before routing, in the skill router prose and pseudocode, `route_contract.py`, the fixtures and the kernel's Section 2 and Router Code
- R2: deliver first, numbered open items in the Deal Templates shape, the A/B/C framework question dropped, one home for assumptions, questions only for what cannot be defaulted
- R3: the claude.ai reply opens with one bare code fence holding only the prompt, with the reason recorded in the changelog
- The doc sweep: AGENTS.md, READMEs, playbook scenarios, the reply linter, SYNC.md and a changelog

### Out of Scope
- Whole-reply examples and an example lint - not needed for R1 to R3 to hold together, and a new knowledge file would need a new declared pair
- Rewriting the interactive-mode success statistics - not approved
- Editing `systems.py` or the shared validator - shared files; the resync pairs are reported instead
- Renaming `*-canvas.md` scenario files - IDs and links stay stable

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-prompt-improver/SKILL.md` | Modify | Router prose and pseudocode, interaction rules, open items, Project delivery override, rules |
| `sk-prompt-improver/references/*.md`, `assets/format-guide-*.md` | Modify | Deliver-first flow, open items, library default, bare-fence Project lines |
| `claude project/Custom Instructions.md` | Modify | Kernel v1.0.1: delivery rule, routing, rules, delivery protocol, checklist, Router Code |
| `claude project/knowledge/*.md` (7 files) | Modify | Hand-written mirrors of the changed skill sources |
| `benchmark/router/route_contract.py`, `fixtures.json`, `README.md` | Modify | `strip_source_prompt()` and seven fixtures |
| `benchmark/grader/deliverable_lint.py`, `README.md`, `twin_divergence.py` | Modify | Fence contract checks and docs |
| `benchmark/gates/rule_parity.py` | Modify | Comment names the renamed DEPTH principle |
| `AGENTS.md`, `README.md`, `sk-prompt-improver/README.md`, `claude project/README.md`, `SYNC.md` | Modify | Doc sweep and dated note |
| `sk-prompt-improver/manual-testing-playbook/**` | Modify | Deliver-first and bare-fence grading, versions |
| `sk-prompt-improver/changelog/v1.0.1.0.md` | Create | Release notes |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Mode routing reads only the user's own words: fenced blocks, quoted spans of three or more words and lead-in text are set aside, and the skill and kernel router code stay equal |
| REQ-002 | A request that carries a prompt or a task is delivered in the first reply, and every default is listed after it as a numbered open item with `Situation:` and `Open:` bullets and no blank lines |
| REQ-003 | The claude.ai reply opens with one bare code fence holding only the improved prompt, with the header, path, score, summary and open items in chat after it |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | Every doc, playbook scenario and linter that described the old behavior is updated, versions move by patch steps, and SYNC.md and the changelog record the change and the approved removal of the framework question |
| REQ-005 | Every residency statement whose home text changed is reported as a resync pair with its statement key |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The photo and video-clip probes route to TEXT, the one-word quote and explicit image controls stay IMAGE, and all fixtures pass
- **SC-002**: The router fixtures, kernel parity, rule parity, pair divergence and playbook validator pass, and `validate_document.py` is no worse than HEAD on any changed doc
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | `systems.py` residency declarations | Residency fails until the declared statements are resynced | Resync pairs reported with keys; the coordinator applies them |
| Risk | A one- or two-word quote that is really a pasted prompt still routes | Low | The three-word floor is pinned by a fixture and named in the router prose |
| Risk | The live claude.ai Project runs the old kernel until it is pasted again | Med | SYNC.md and the changelog name the kernel and the seven knowledge files to upload |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The kernel stays readable in one paste; it grew from 24,233 to 27,104 bytes

### Security
- **NFR-S01**: No secrets, credentials or environment values enter any file

### Reliability
- **NFR-R01**: No model runs; every check is static and repeatable
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Empty input: routes to Interactive with one comprehensive question, as before
- A message that is only a fenced prompt: routes to Improve through `semantic`
- A one-word quote such as `"midjourney"`: kept, so it still routes to Image

### Error Scenarios
- Two conflicting mode commands: still one question naming both
- A non-prompt request: one reframe as prompt work, then a refusal

### State Transitions
- A user answering an open item: the next reply is a revision under the next export number
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | About 110 files, mostly playbook scenarios, one Python router and one linter |
| Risk | 12/25 | Behavior change for live users, mirrored contract, shared declaration downstream |
| Research | 8/20 | Comparison with Deal Templates done in the read-only phase |
| **Total** | **38/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Whether the coordinator applies the reported resync pairs through `resync_statement.py`, since some pairs span a line break in the raw statement
- Whether the CLI JSON and YAML guides' "downloadable file, never inline" core rule should gain a Project-side clause, since the Project now renders the payload in a chat fence
<!-- /ANCHOR:questions -->

---
