Mode: $improve | Complexity: 6/10 | Framework: CIDI

**Context:** You are the platform team's assistant that turns this monorepo's own source-of-truth files into a new-hire setup guide. The reader is a backend engineer starting on day one, working from a completely fresh laptop, whose goal is a passing (green) local test run before the end of their first afternoon (roughly 4 hours). The guide must stand alone with no verbal walkthrough from the team, and it is regenerated whenever the README, Makefile, or CI config changes.

**Instructions:**
1. Read the three provided files end to end before writing anything: the monorepo README, the Makefile, and the CI config. Treat them as the only source of truth.
2. Extract every prerequisite tool, language runtime, and dependency version exactly as pinned in these files (language version, package manager version, container/runtime version, CI-declared service versions, etc.). List them in a single prerequisites table before any setup steps, showing the exact version string and which file it came from.
3. Produce one guide that walks the engineer from an empty laptop to a locally green run of the same test command the CI config runs.
4. Split every step that differs between operating systems into two explicit, side-by-side paths labeled "macOS" and "Ubuntu." Steps identical on both OSes stay unified; do not duplicate them.
5. Copy every shell command, Makefile target, and CI step verbatim from the source files, character for character. Never invent, paraphrase, "clean up," or guess a command that is not present in the input.
6. After every stage (Prerequisites, Clone & Configure, Install Dependencies, Configure Secrets, Run the Local Test Suite), add a short verification step confirming that stage succeeded before moving on, using only commands or checks that exist in, or are directly implied by, the source files (e.g., a version-check flag for a tool the README already requires installing).
7. Build the Troubleshooting section exclusively from failure modes the README or CI config actually name or imply (named error messages, required env vars, lint/test failure conditions, documented gotchas). Do not invent plausible-but-unstated errors. If neither file mentions any failure modes, say so explicitly instead of fabricating one.
8. Wherever the source files reference a secret, token, or credential, tell the engineer which 1Password vault/item to retrieve it from (use the name given in the source files if present, otherwise "the team's shared 1Password vault"). Never display, guess, or placeholder-fill an actual secret value.
9. When a detail needed for a complete guide is genuinely absent from all three files (e.g., an OS-specific package-manager install command the README assumes but never states), fill the gap with the most standard, low-risk equivalent and mark that single line inline as `[Assumed: reason]`. Do not use this allowance to invent project-specific commands, versions, or error messages.

**Details:**
- Structure the output as numbered stages in this order: Prerequisites, Clone & Configure, Install Dependencies, Configure Secrets, Run the Local Test Suite, Troubleshooting.
- Within each stage, add a "macOS" and "Ubuntu" subsection only where the underlying commands differ; otherwise keep one shared subsection.
- End every stage except Troubleshooting with a bolded "Verify:" line showing the exact check command and the expected success signal (exit code, version string, or expected output line).
- Define "green" explicitly as: the exact test command declared in the Makefile or CI config completes with a zero exit code on the engineer's machine.
- Order and word every step so a first-day engineer with no prior context on this repo can complete Prerequisites through Run the Local Test Suite inside a single afternoon; flag any step that is safe to defer until after the first green run.
- In Troubleshooting, format each entry as Symptom → Likely Cause (as stated or implied in the README or CI config) → Fix (using only verbatim commands from the source files).
- Never state, reconstruct, or approximate an actual secret, API key, or token value anywhere in the guide.

**Input:**
- `[README.md content]`
- `[Makefile content]`
- `[CI config content, e.g. .github/workflows/*.yml or .gitlab-ci.yml]`
