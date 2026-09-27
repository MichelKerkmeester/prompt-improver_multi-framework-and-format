Mode: $improve | Complexity: High (8/10) | Framework: CIDI

---

**Context:** You are writing the local dev environment setup guide our platform team hands to every new backend engineer. The reader starts on a fresh laptop (macOS or Ubuntu, unknown which) with none of the monorepo's tooling installed, and must reach a passing local test run (`green`) within one afternoon. Guessed commands, invented version numbers, or fabricated error messages break trust and cost the reader real time, so every instruction must trace back to the three source files provided below — nothing paraphrased, simplified, or assumed. Secrets are managed in 1Password, never in plaintext, so the guide must point to where a credential lives without ever displaying its value.

**Instructions:**
1. Read the full README, Makefile, and CI config below before writing anything.
2. Build a **Prerequisites** section listing every tool, language runtime, package manager, and service version pinned in the source files. Quote each version exactly as written in its source (for example, a Makefile variable, a CI config version key, or a README badge). If a tool has no pinned version anywhere in the source, list it and mark it `[version not pinned in source]` instead of guessing one.
3. Write two complete, independently followable setup paths, each fully self-contained: **macOS Setup** and **Ubuntu Setup**. Never merge steps that use different package managers, shells, or installers.
4. After every step or stage in both paths, add a `Verify:` line containing a command that confirms that stage succeeded before moving on. Pull verification commands from the Makefile targets or CI config steps (for example, an existing `make check` or lint/test target); never invent a check that is not present in or directly derivable from the source files.
5. Copy every shell command exactly as it appears in the README, Makefile, or CI config, in a fenced code block. Do not alter flags, paths, or wording. When a command's purpose is not obvious, name its source file in a short note beside it.
6. Build a **Troubleshooting** section containing only failure modes drawn from the source files: error strings, named CI check failures, or problems the README explicitly calls out. Do not invent plausible-sounding errors that are not grounded in the source. If the source files mention no errors at all, state that explicitly rather than filling the section with guesses.
7. Wherever a secret, API key, token, or credential is needed, name the 1Password vault/item to fetch it from (using the name given in the README or CI config if one is given) and describe how to load it locally (for example, into an env file or shell export). Never print, generate, or approximate the credential's value.
8. End with a final verification stage confirming the full local test suite passes (`green`), using the exact test command found in the Makefile or CI config.

**Details:**
- Target outcome: a new backend engineer with zero prior context reaches a green local test run within one afternoon.
- Keep the full requested scope intact: Prerequisites, both OS paths, per-stage verification, source-grounded Troubleshooting, and 1Password-referenced secrets handling must all appear — do not compress or drop any of these to shorten the guide.
- Order sections: Prerequisites → macOS Setup → Ubuntu Setup → Secrets (1Password) → Troubleshooting → Final Verification.
- Number steps within each OS path; place the matching `Verify:` line directly under each step, not batched at the end.
- Where the source files leave a genuine gap (missing version, missing verification target, no documented errors), say so plainly in that section instead of inventing content.

**Input:**
- README: [paste full monorepo README.md content here]
- Makefile: [paste full Makefile content here]
- CI config: [paste full CI configuration file content here]
