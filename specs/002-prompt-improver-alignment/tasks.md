---
title: "Tasks: Prompt Improver Alignment (Parent)"
description: "Phase tracker for aligning Prompt Improver to the Product Owner packaging standard."
importance_tier: "high"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 3 -->
# Tasks: Prompt Improver Alignment (Parent)

- [x] P001 Filename hyphenation: 13 underscored files renamed with references updated and all 0 symlinks resolving. (`001-filename-hyphenation/`)
- [x] P002 Skill folder rename to `sk-prompt-improver` with a full reference sweep and zero residuals. (`002-skill-folder-rename/`)
- [x] P003 SKILL.md rewritten to the create-skill standard behind a routing characterization harness, advisor description.json and graph-metadata.json added. (`003-skill-md-alignment/`)
- [x] P004 Skill README authored to the Product Owner final form and the package root README replaced by a relative symlink. (`004-skill-readme/`)
- [x] P005 SYNC, AGENTS and claude project aligned (14 mirrors, checksum manifest rebuilt), closed by an independent drift audit with byte-verified findings. (`005-package-alignment/`)

## Executed 2026-07-16 (alignment wave, recovered lane complete)

Phases ran as staged Sonnet-xhigh agents with receipts-gated progression. This lane lost one agent to an API server error in the main wave and completed via the recovery workflow, which verified crashed-stage work against receipts before continuing.

- Verification: 14/14 mirrors byte-identical, 15/15 checksum rows.
- P6 audit: 4 findings, 4 confirmed and fixed.
- Recovered lane: P1 completed in the main wave, P2 through P6 ran in recovery. Renamed to sk-prompt-improver with the root README salvaged to z_legacy and replaced by the symlink.
- [x] F001 (2026-07-17) Changelog added at `sk-prompt-improver/changelog/` in the create-changelog format, documenting the alignment release.

- [x] F002 (2026-07-17) Changelog expanded to four entries with real version commits as anchors (v0.1.0.0, v0.2.1.0, v0.2.2.0 from the 2026-06-21 version commit, deepened v0.3.0.0).
