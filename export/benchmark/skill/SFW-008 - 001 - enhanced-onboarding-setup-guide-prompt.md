Mode: $improve | Complexity: 6/10 | Framework: CIDI

**Context:** You are a technical writer working from Claude in Cursor inside the platform team's monorepo. Produce a single onboarding guide, built strictly from the three attached source files (README, Makefile, CI config), that takes a new backend engineer from a completely fresh laptop to a green local test run within one afternoon (~4 hours). Engineers will copy commands directly from this guide, so every command, version number, and error must trace back to the source files rather than general knowledge of similar stacks — inventing a plausible-looking command or version is worse than omitting it. Secrets and credentials are managed in 1Password, so the guide must direct engineers to the correct vault/item without ever exposing a value.

**Instructions:**
1. Read the attached README, Makefile, and CI config fully before drafting; extract every command, environment variable, dependency, and version number they contain.
2. Structure the guide as sequential, numbered stages covering, at minimum: prerequisite installation, repository setup, dependency/toolchain install, secrets retrieval, build, and running the local test suite to green.
3. Wherever a stage has OS-specific steps, write two fully separate sub-paths — "macOS" and "Ubuntu" — using the exact package manager and commands implied by the source files (e.g., Homebrew vs apt); state OS-agnostic steps once, outside the split.
4. End every stage with a "Verify" step: the exact command to run and the exact success signal (output, exit code, or artifact produced) that confirms the stage worked before moving on.
5. Build a Prerequisites list (table or bullets) of every required tool, runtime, or service with its exact version, copied only from what the README, Makefile, or CI config state; never state a version that is not written in one of those files.
6. Copy every command verbatim from the source files; never invent, paraphrase, add flags to, or "clean up" a command. If a necessary step has no literal command in the sources, mark it `[Assumes: <what you inferred and why>]` instead of fabricating one.
7. For every secret or credential referenced anywhere in the sources (API keys, tokens, `.env` values, CI-only variables), name the exact 1Password vault/item to fetch it from; never print, guess, or reconstruct the underlying value.
8. Build a "Troubleshooting" section at the end containing only errors, failure messages, or failure conditions explicitly named or described in the README or CI config; do not invent plausible-sounding errors that are not in the sources.
9. Preserve full scope: include every Makefile target and CI step that contributes to reaching a passing local test run; do not compress, summarize away, or drop steps for brevity.

**Details:**
- Output as Markdown: one H1 title, one H2 per stage, and a Prerequisites section before Stage 1.
- Sequence and scope the guide so a fresh-laptop engineer can realistically finish in one afternoon; flag any stage likely to exceed 30-45 minutes with a one-line reason.
- Where an OS-specific package name or path is implied but not literally written in the sources, infer the standard equivalent and mark it `[Assumes: ...]` rather than presenting it as sourced fact.
- Never display a secret value, a placeholder that looks like a real value, or an example token — reference only the 1Password vault/item name to retrieve it from.
- Use direct, procedural language; no narrative padding or motivational framing.
- Do not add sections beyond Prerequisites, the numbered Stages (each ending in Verify), and Troubleshooting.

**Input:**
- Full contents of the monorepo README — paste below
- Full contents of the Makefile — paste below
- Full contents of the CI config file(s) — paste below

[Paste README here]
[Paste Makefile here]
[Paste CI config here]
