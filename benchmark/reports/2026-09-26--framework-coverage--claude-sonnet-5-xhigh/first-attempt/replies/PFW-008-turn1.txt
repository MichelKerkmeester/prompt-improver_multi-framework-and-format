```markdown
Mode: $improve | Complexity: 6/10 | Framework: CIDI

**Context:** You are producing the onboarding setup guide the platform team runs with Claude in Cursor, with direct read access to this monorepo. The single reader is a new backend engineer on a fresh laptop (macOS or Ubuntu) who must reach a green local test run within one afternoon. The repository's `README`, `Makefile`, and CI configuration file(s) are the only permitted sources of truth for every command, tool name, and version — never supplement from general knowledge, similar tools, or memory of how "this kind of stack" usually works. This guide will be committed and run verbatim by future engineers, not read as a narrative explainer.

**Instructions:**
1. Read the README, Makefile, and CI config in full before drafting anything. Note every command, tool reference, and version string exactly as written in those files.
2. Derive the stage sequence (for example: prerequisites, clone, dependency install, environment/secrets setup, build, service bootstrap, run tests) from what the Makefile targets and CI job steps actually do — not from a generic onboarding template. Order stages so a fresh laptop reaches a passing local test run.
3. For any stage where macOS and Ubuntu steps differ (package managers, paths, install commands), give two explicit, separately labeled command blocks — **macOS** and **Ubuntu** — each using only commands and package names found in the source files. Where a stage is OS-agnostic (e.g., a single `make` target), say so once instead of duplicating identical blocks.
4. Close every stage with a **Verify** line: a command or observable output, sourced only from the input files, that confirms the stage succeeded before the reader continues.
5. Build the Troubleshooting section using only failure messages or error strings that literally appear in the README or the CI config (not the Makefile). For each: quote the error, name the stage it belongs to, and give the fix using only remedies stated in those same two files. Do not include generic or hypothetical errors.
6. Wherever a secret, API key, or credential is required, name the 1Password vault/item to fetch it from (as referenced in the README/CI config) and the environment variable or config field it populates. Never display, placeholder-fill, or fabricate an actual secret value.
7. Copy every command verbatim, character-for-character, from the source files. Do not reformat, "clean up," or reconstruct a command from familiarity with similar tools.

**Details:**
- Prerequisites list: exact tool names and version numbers exactly as pinned across the README, Makefile, and CI config (language runtime, package manager, containers, etc.). If a required tool has no version pinned anywhere in the three files, list it as "version unspecified in source files" rather than guessing one.
- Scope: this includes everything from an empty laptop through a passing local test run. This excludes deployment, staging/production configuration, and CI-only steps that do not run locally.
- Keep the macOS and Ubuntu paths fully separated wherever install commands, package managers, or paths differ; never merge them into one ambiguous instruction.
- If the one-afternoon target is at risk because a stage's duration isn't documented anywhere in the source files, flag that stage as time-unknown rather than estimating a duration.
- Deliver the guide as a single, self-contained Markdown document the reader can follow top to bottom: one heading per stage (with macOS/Ubuntu subheadings where needed), a bold **Verify:** line closing each stage, and a closing `## Troubleshooting` section.

**Input:** This monorepo's `README`, `Makefile`, and CI configuration file(s) (e.g., `.github/workflows/*.yml`, `.gitlab-ci.yml`, or whichever CI config exists in this repo) are the complete and only authoritative input. If the guide needs information the task requires but none of the three files supply it, flag the gap explicitly in the guide rather than inventing a value.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = downstream AI has direct repo read access to the three named files; "green local test run" means the primary test target/job defined in those files passes; undocumented versions or durations are flagged rather than estimated | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-onboarding-setup-guide.md`

**Score and gate status:** CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimization) | Gate passed, all dimension floors met

**Summary:** The rewrite locks your one-line ask into a CIDI-structured prompt that separates *what to source* (README/Makefile/CI config, verbatim only) from *how to structure* (OS-split stages, per-stage verification, README/CI-only troubleshooting, 1Password-reference-not-value secrets). Two gaps you didn't specify — what to do when a version or stage duration is undocumented — are filled with an explicit "flag it, don't guess" default rather than invented values, consistent with your verbatim-only constraint.

Since this session has no Canvas panel, the deliverable above is rendered as a fenced block per the no-panel protocol rather than a side-panel artifact.