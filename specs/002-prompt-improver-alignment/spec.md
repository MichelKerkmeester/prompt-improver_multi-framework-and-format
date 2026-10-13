---
title: "019 - Prompt Improver Alignment [002-prompt-improver-alignment/spec]"
description: "AI_Systems/Barter/Prompt Improver/ predates the packaging standards proven on Product Owner: underscored filenames, a generic skill/ folder, an accreted SKILL.md without the cre..."
importance_tier: "normal"
contextType: "general"
---
# 019 - Prompt Improver Alignment

## Problem

`AI_Systems/Barter/Prompt Improver/` predates the packaging standards proven on Product Owner: underscored filenames, a generic `skill/` folder, an accreted SKILL.md without the create-skill section standard, no advisor metadata, and package surfaces (SYNC, AGENTS, claude project) on the old conventions. The user wants it aligned exactly the way Product Owner was.

## Blueprint

The executed reference is Product Owner: see `002-product-owner-mode-additions/017-skill-md-alignment/alignment-summary.md` for the full mechanics, verification layers and lessons. Scope guard: this alignment changes PACKAGING AND STRUCTURE only. The system's own content rules (its artifact grammar, voice rules, domain templates) are not Product Owner's and must not be overwritten with Product Owner canon.

## Survey (2026-07-16)

| Fact | Value |
| --- | --- |
| Skill folder | `skill/` with SKILL.md (749 lines), references/, assets/ |
| Underscored files (skill + claude project, excluding z_legacy) | 13 |
| Symlinks inside skill/ | 0 |
| Knowledge mirrors in claude project | 14 |
| Target folder name | `sk-prompt-improver` (user-stated) |

Not in the user's path list but explicitly named sk-prompt-improver in the target names, and the system exists with the standard layout. Has a root README.md: phase 4 reconciles it before the symlink replaces it. Zero symlinks in skill/, so the hyphenation sweep has no symlink hazards. Recent interface work lives in 001-prompt-improver-interface-design.

## Phases

**P001 Filename hyphenation.** Rename every underscored file under `skill/` and `claude project/` to hyphens (z_legacy stays untouched). Update every path reference across SKILL.md, AGENTS.md, SYNC.md and the claude project. Symlinks: re-create any renamed symlink and verify all 0 resolve afterward. Mirror filenames derive from frontmatter titles, so retitle sources and mirrors together where titles carry underscores.

**P002 Skill folder rename.** `skill/` becomes `sk-prompt-improver/`. Sweep every reference with a pattern that cannot touch `skills/` paths. Verify relative symlink depths survive (same nesting level, no edit needed) and that zero `skill/` references remain. Keep the SKILL.md frontmatter `name:` unchanged unless the owner asks: folder name is packaging, invocation name is a contract.

**P003 SKILL.md alignment plus advisor metadata.** First build a routing characterization harness: if SKILL.md carries executable pseudocode, extract and fixture it; if not, author a fixture set of representative requests with expected routes from the current SKILL.md before touching anything. Then a fresh agent rewrites SKILL.md to the create-skill standard (keywords comment, numbered ALL-CAPS sections, one consolidated smart-router section, dead decoration removed) with the harness as a hard gate it runs itself, plus an independent orchestrator re-run. Minor version bump. Create `description.json` and `graph-metadata.json` in the leaf-skill schema next to SKILL.md.

**P004 Skill README plus root symlink.** Author `sk-prompt-improver/README.md` to the Product Owner final form: create-skill standalone template as the skeleton, then descriptive reference depth (value-table opener, box-drawing request-flow diagram, per-mode or per-capability sections with structure detail and snippets, output format, delivery and export contracts, examples inventory if present, FAQ, troubleshooting, related documents). Two-column tables, the system's own voice rules. Then replace the package root README.md with a relative symlink to it, reconciling any existing root README content first.

**P005 Package alignment plus drift audit.** Restructure SYNC.md to the sk-doc section standard (frontmatter, tagline, numbered sections, When to Sync, Required Parity, Drift Checks, Related Documents) with pins matching the new versions. Sweep AGENTS.md. Update the claude project kernel and manifest: version alignment lines, mirror renames, full checksum rebuild over all 14 knowledge files. Close with an independent fresh-agent drift audit of AGENTS.md and the claude project (findings-only brief), byte-verify every finding before fixing, and finish with all verification layers green.

## Verification contract

Every phase ends green on: the routing harness (once built), mirror byte-identity over the full knowledge inventory, checksum manifest rows recomputed from final bytes, zero residual old-name references. Version bumps always rename mirrors and refresh manifest rows in the same pass. Mirrors are never edited directly, only recopied from sources.
