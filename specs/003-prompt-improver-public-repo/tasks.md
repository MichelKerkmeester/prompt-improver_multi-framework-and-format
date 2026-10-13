---
title: "Tasks: Publish Prompt Improver as its own public repo"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "prompt improver public repo tasks"
  - "first push checklist"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Publish Prompt Improver as its own public repo

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Read the style source, sk-create-readme, sk-git, cli-codex and the current skill README (`Code_Environment/Public/README.md`, `sk-prompt-improver/README.md`)
- [x] T002 Inspect the nested repo: one `LICENSE` commit on `main`, remote, untracked tree, symlinks and sizes
- [x] T003 Create this packet by the scaffold method (`AI Systems/Prompt Improver/specs/003-prompt-improver-public-repo/`)
- [x] T004 Point `origin` at the renamed repo and confirm it answers (`git remote set-url`, `git ls-remote`)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T005 Confirm the only symlink in the tree is the root `README.md` (`find . -type l`)
- [x] T006 Write the ignore rules for `.DS_Store` and `export/` (`.gitignore`)
- [x] T007 Remove the root `README.md` symlink so no write can land in the skill README (`README.md`)
- [x] T008 Dispatch GPT-6 Luna at max effort on the fast tier to draft the front page (`README.md`)
- [x] T009 Verify the draft against the files and tune it (`README.md`)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Run the sk-doc validator, the HVR linter, the dash and semicolon scans and the link scan (`README.md`)
- [x] T011 Run the router fixtures (`benchmark/router/run_fixtures.sh`)
- [x] T012 Check the staged set: ignore rules, no symlink leaving the repo, no credentials, no large files
- [x] T013 Commit with a Conventional Commit subject and push to `origin/main`
- [x] T014 Confirm `origin/main` matches the local commit
- [x] T015 Fill the implementation summary and the acceptance criteria
<!-- /ANCHOR:phase-3 -->

---

## Phase 4: Follow-ups

- [x] T016 Rewrite the dual packaging section and the related documents rows so the skill README no longer names the retired sync compiler (`sk-prompt-improver/README.md`)
- [x] T017 Run the sk-doc validator, the HVR linter and the router fixtures (`sk-prompt-improver/README.md`)
- [x] T018 Commit and push the public repo and the monorepo

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
- **Sibling packet**: `AI Systems/Product Owner/specs/012-product-owner-public-repo/`
<!-- /ANCHOR:cross-refs -->

---

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Requirements documented in spec.md
- [x] CHK-002 [P0] Technical approach defined in plan.md
- [x] CHK-003 [P1] Dependencies identified and available
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] README passes the sk-doc validator
- [x] CHK-011 [P0] README carries no em dash, en dash or prose semicolon
- [x] CHK-012 [P1] Every local link in the README resolves
- [x] CHK-013 [P1] README follows the style source's structure
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met
- [x] CHK-021 [P0] Router fixtures pass
- [x] CHK-022 [P1] Ignore rules checked entry by entry
- [x] CHK-023 [P1] Every published count checked against the files
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Finding class for the README symlink: `instance-only`, the one file named by `find -type l`
- [x] CHK-FIX-002 [P0] Same-class inventory: `find . -type l` shows no other symlink. The benchmark parity and gates scripts reach outside the repo, recorded as a follow-up
- [x] CHK-FIX-003 [P0] Consumer inventory: links that pointed at the skill README reviewed
- [x] CHK-FIX-004 [P0] Not a security, path, parser or redaction fix: no adversarial table needed
- [x] CHK-FIX-005 [P1] Matrix axes: not applicable
- [x] CHK-FIX-006 [P1] Hostile env variant: not applicable
- [x] CHK-FIX-007 [P1] Evidence pinned to the pushed commit SHA `542207e`
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets in the staged set
- [x] CHK-031 [P0] No generated export content staged
- [x] CHK-032 [P1] Push uses the operator's own GitHub account
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized
- [x] CHK-041 [P1] Follow-ups recorded in the implementation summary
- [x] CHK-042 [P2] README updated
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in the session scratchpad only
- [x] CHK-051 [P1] scratch/ cleaned before completion
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 13 | 13/13 |
| P1 Items | 15 | 15/15 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-24
<!-- /ANCHOR:summary -->

---
