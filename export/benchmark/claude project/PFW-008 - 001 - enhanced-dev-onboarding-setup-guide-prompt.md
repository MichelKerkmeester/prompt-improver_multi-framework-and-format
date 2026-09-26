Mode: $improve | Complexity: 7/10 | Framework: CIDI

**Context:** You are writing a new-developer onboarding guide for the platform team's backend monorepo. The reader is a brand-new backend engineer starting on a fresh laptop with no dev tooling installed, and must reach a green local test run within a single afternoon (roughly 4 hours), so every instruction must be immediately actionable and verifiable — no step the engineer has to guess at. Your only sources of truth are the three files supplied below: the monorepo README, the Makefile, and the CI configuration file. Treat them as the sole authority for tool versions, commands, and known error conditions; do not draw on general knowledge of "typical" monorepo setups. The team stores all secrets in 1Password, so credentials must never appear as literal values anywhere in the guide — only as retrieval instructions. The engineer may be on macOS or Ubuntu, and install mechanisms diverge between the two, so every OS-specific step needs a parallel, clearly labeled path.

**Instructions:**
1. Read the README, Makefile, and CI config first and extract every tool, language runtime, package manager, and service dependency that has an exact version pin stated in those files. List these in a Prerequisites section, citing where each version came from (e.g. "README §Setup," "Makefile target X," "CI job Y") so the list stays auditable. Never invent, round, or assume a version that isn't explicitly stated in the files.
2. Sequence the rest of the guide as ordered stages carrying the engineer from a bare laptop to a passing local test run (for example: clone → toolchain install → secrets retrieval → dependency install → build → test). Follow the stage order implied by the README/Makefile/CI rather than an arbitrary one.
3. Within each stage, present two labeled command tracks, "macOS" and "Ubuntu," showing only the OS-specific commands (e.g. `brew` vs `apt`) where the source files actually diverge. Where a command is OS-agnostic (e.g. a `make` target), show it once and label it shared, so the two tracks stay easy to compare stage-for-stage.
4. Copy every command character-for-character from the README, Makefile, or CI config. Never paraphrase, "clean up," or substitute an equivalent command — an invented command breaks traceability back to the source of truth even if it would technically work.
5. Immediately after each stage, add a "Verify" step with the exact check command(s) from the source files (a version-check command, `make test`, a CI-equivalent step, etc.) plus the exact success signal the files describe. If the files don't state a success signal for a stage, write "[Not specified in source — confirm expected output with the team]" instead of guessing one; never omit the Verify step entirely.
6. Wherever a stage requires a secret or credential, name the exact 1Password vault/item reference given in the README or CI config and instruct the engineer to fetch and inject it locally. Never print, placeholder-fill, or example-fill an actual secret value.
7. Build the Troubleshooting section strictly from error messages, failure conditions, or known-issue notes that appear explicitly in the README or CI config. Pair each documented error text with its documented cause/fix. Do not add plausible-sounding errors that aren't in the source files.

**Details:**
- Do keep macOS and Ubuntu tracks numbered identically stage-for-stage.
- Do scope the guide to exactly three sections — Prerequisites, OS-specific staged setup with verification, Troubleshooting — and nothing else (no culture/process content, no architecture overview, no security-policy summary).
- Do order stages so the final verified step is the green local test run, since that is the afternoon's success criterion.
- Don't invent or "helpfully" add a command, version, or troubleshooting entry not literally present in the README, Makefile, or CI config.
- Don't show or synthesize any secret value, including realistic-looking placeholders — reference the 1Password location only.
- Don't skip a Verify step, even where the source files only imply a check rather than state one outright; use the "[Not specified…]" flag instead.

**Input:**
- [Monorepo README — attach full contents]
- [Makefile — attach full contents]
- [CI configuration file — attach full contents]
- Target reader: new backend engineer, Day 1, macOS or Ubuntu laptop, one afternoon to a green local test run.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = "green local test run" means the repo's primary test command exits successfully; default stage order is clone→toolchain→secrets→dependencies→build→test unless source files imply otherwise; 1Password references are assumed to be named somewhere in the README/CI (if absent, the guide should surface that gap rather than invent a vault name) | format = Markdown | execution = did not occur | save = did not occur
