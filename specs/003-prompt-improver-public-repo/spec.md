---
title: "Feature Specification: Publish Prompt Improver as its own public repo"
description: "Prompt Improver now has its own git repository and a public GitHub remote, but its front page is a symlink to the skill README and nothing keeps generated exports out of git. This packet gives the repo a real front-page README and export ignore rules, then makes the first push."
trigger_phrases:
  - "prompt improver public repo"
  - "prompt-improver_multi-framework-and-format"
  - "front-page readme"
  - "export gitignore"
importance_tier: "normal"
contextType: "specification"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Publish Prompt Improver as its own public repo

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete, pushed |
| **Created** | 2026-09-24 |
| **Branch** | `main` of the nested repo (packet only, no monorepo branch created) |
| **Systems touched** | Prompt Improver only |
| **Public repo** | https://github.com/MichelKerkmeester/prompt-improver_multi-framework-and-format |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`AI Systems/Prompt Improver/` now holds its own `.git` with a public GitHub remote, and its only commit is the GitHub-generated `LICENSE`. The root `README.md` is a symlink to `sk-prompt-improver/README.md`, so GitHub would show the skill README with its frontmatter as a table and with links that break from the repo root. Nothing ignores `export/`, where every enhanced prompt lands.

### Purpose
The public repo opens on a front-page README in the style of the Skilled repo README, keeps generated exports local apart from benchmark deliverables, and holds the whole system in its first pushed commit.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A real root `README.md` in the style of `Code_Environment/Public/README.md`, drafted by GPT-6 Luna at max effort on the fast tier through cli-codex, then verified and tuned
- A root `.gitignore` that ignores `.DS_Store` and all of `export/` except `export/.gitkeep` and `export/benchmark/`
- The `origin` remote pointed at the renamed repo
- One Conventional Commit of the system and a push to `origin/main`

### Out of Scope
- Editing `sk-prompt-improver/README.md`, `SKILL.md`, `AGENTS.md` or `SYNC.md`: the operator asked for the front page only. The skill README still calls the retired sync compiler the mirror writer, which is recorded as a follow-up
- Committing anything in the monorepo: the operator asked for commits in the public repo

### Follow-up Scope

The operator asked on 2026-09-24 to fix the follow-ups this packet recorded. That lifts both exclusions above for one file: `sk-prompt-improver/README.md` drops the retired sync compiler, and the change is committed in the public repo and in the monorepo.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Prompt Improver/README.md` | Replace symlink with file | Public front page |
| `AI Systems/Prompt Improver/.gitignore` | Create | Export and OS-file ignore rules |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The root `README.md` is a regular file that follows the Skilled README style and every local link in it resolves inside the repo |
| REQ-002 | `git check-ignore` ignores every `export/` entry except `export/.gitkeep` and `export/benchmark/` |
| REQ-003 | No committed symlink points outside the repo |
| REQ-004 | The pushed commit holds no credentials |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | Every count the README publishes matches the files |
| REQ-006 | The README passes the sk-doc validator and carries no em dash, en dash, prose semicolon or Oxford comma |
| REQ-007 | The commit follows sk-git: Conventional Commit subject, scoped staging, no hook bypass |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: GitHub shows the new front page on the repo root
- **SC-002**: `origin/main` equals the local commit and holds no file from `export/` apart from `.gitkeep`
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | codex CLI with `gpt-6-luna` | No draft if the dispatch fails | Write the README in session from the same sources |
| Risk | Public exposure of internal material | Medium | Keep `export/` ignored, scan the staged set for credentials before the commit |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The pushed tree stays under 2 MB
- **NFR-P02**: No single committed file approaches the GitHub 50 MB warning size

### Security
- **NFR-S01**: No token, key or `.env` value in the staged set
- **NFR-S02**: Generated prompts in `export/` stay local

### Reliability
- **NFR-R01**: The router fixtures still pass after the change
- **NFR-R02**: The push goes through the normal hooks
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Empty input: `export/` with only `.gitkeep` still keeps the folder in git
- Maximum length: none
- Invalid format: a symlinked `README.md` is removed before the writer runs so a write cannot land in the skill README

### Error Scenarios
- External service failure: a failed push leaves the local commit in place for a retry
- Network timeout: retry the push
- Concurrent access: the monorepo tree is shared, so only the nested repo is staged

### State Transitions
- Partial completion: the spec records which step stopped
- Session expiry: this packet carries the state
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 6/25 | Two files, one repo |
| Risk | 10/25 | First public push |
| Research | 6/20 | Style source, skill sources, ignore rules |
| **Total** | **22/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None open. The operator chose a real root README and one packet per repo on 2026-09-24
<!-- /ANCHOR:questions -->

---
