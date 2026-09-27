```markdown
Mode: $improve | Complexity: High (8/10) | Framework: CIDI

**Context:** You are a senior platform engineer writing the onboarding setup guide that lives in this monorepo. The reader is a new backend engineer on day one, starting from a completely fresh laptop, and the guide must get them to a green local test run within a single afternoon — so every step has to be fast to execute and easy to verify, with no dead ends. You are working inside Cursor and will be given the monorepo's actual README, Makefile and CI config as your only sources of truth for tool versions, commands and known failure modes; do not supplement them with general knowledge of the toolchain.

**Instructions:**
1. Read the attached README, Makefile and CI config in full before drafting anything.
2. Write one setup guide, sequenced as stages from "fresh laptop" to "green local test run," so the engineer always knows which stage they're in and what "done" looks like for that stage.
3. Split the guide into two fully separate command paths — one for macOS, one for Ubuntu — anywhere a step differs by OS, because a merged path is where new hires copy the wrong command and lose time.
4. Open with a prerequisites list giving the exact tool and runtime versions, pulled only from version strings that literally appear in the README, Makefile or CI config.
5. After every stage, add a verification step the engineer runs before moving on, so a failure is caught at the stage that caused it rather than surfacing three stages later as a mystery.
6. Close with a Troubleshooting section containing only the errors, failure messages or known issues explicitly mentioned in the README or CI config — keep it short (or note none were found) rather than inventing plausible-sounding ones.
7. Copy every command verbatim from the input files, character for character; never invent, autocorrect or "clean up" a command, flag or version number that isn't present in the sources.
8. Wherever a secret, token, key or credential is required, name the exact 1Password vault and item to fetch it from; never print, generate or placeholder-fake the value itself, since this guide will be read and re-shared by every future hire.

**Details:**
- Do: reproduce version numbers and commands as exact quotes from the source files, including capitalisation and flags.
- Do: keep the macOS and Ubuntu paths separate end-to-end, not just at the install step, whenever the source files diverge by OS.
- Do: place each verification check immediately under the stage it validates, not batched at the end.
- Don't: add a troubleshooting entry that isn't traceable to explicit wording in the README or CI config.
- Don't: show, generate or approximate any secret value, API key or token — a vault/item reference is always sufficient.
- Don't: shorten the guide by dropping prerequisites, either OS path, per-stage verification or the troubleshooting section — full scope is required even if the guide runs long.
- If a command or step is identical on both platforms, state it once and note that it applies to both, rather than duplicating it under both OS paths.

**Input:** Three files, provided as attachments or pasted context: (1) the monorepo README, (2) the Makefile, (3) the CI config. Treat these as the complete and only source of setup commands, version numbers and known errors.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = 2 flagged | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-onboarding-setup-guide-prompt.md`

**Score and gate status:** CLEAR 43/50 (C9, L8, E13, A9, R4) | Perspectives: 4 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture) | Gate passed

**Assumptions flagged:**
- [Assumes: "CI config" is a single primary pipeline definition file, not several pipeline files across services]
- [Assumes: the version numbers a new engineer needs are literal version strings present somewhere in the three input files, not values requiring inference from lockfiles not supplied]

**Summary:** Restructured the one-line request into a CIDI prompt (Context, Instructions, Details, Input) that locks in every constraint you named — separate macOS/Ubuntu paths, version-exact prerequisites, per-stage verification, source-only troubleshooting, verbatim commands, and 1Password references without secret values — while explicitly forbidding scope-trimming so the full guide survives even under time pressure. Note this environment has no Canvas side panel, so the deliverable above is the fenced block per the no-panel delivery rule; nothing was saved or executed.