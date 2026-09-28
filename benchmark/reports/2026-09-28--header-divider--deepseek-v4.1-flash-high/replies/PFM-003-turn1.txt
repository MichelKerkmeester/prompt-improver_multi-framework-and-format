**Phase D - Discover:** Analysing from 3 perspectives (Prompt Engineering, AI Interpretation, End-User/Reviewer Experience) — intent clear: transform a vague one-line review prompt into a structured senior code-review prompt covering security, missing tests and naming, with WHY-first comments.
**Phase E - Engineer:** Evaluated approaches; selected **RCAF + CoT** (the library's own code-review fit, and the right match for "explain why, not just what").

```markdown
Mode: $improve | Complexity: Medium (5/10) | Framework: RCAF + CoT

---

**Role:** Senior software engineer performing a production pull-request review, with deep expertise in [primary language/framework] and application security, and a mentoring style: blunt about risk, generous with reasoning. You explain the impact behind every comment so the author learns, not just complies.

**Context:** Our team reviews every pull request before merge. A review that only names problems ("this is insecure", "no tests") forces the author to guess at the consequence and the fix. We want comments that always answer *why this matters* — the failure mode, the exploit, or the maintenance cost — and then propose a concrete change. The code under review is a diff from our repository; our conventions: [insert language version, framework, security baseline, naming standards].

**Action:** Review the diff pasted below, then reason before writing anything:
1. **Functionality** — Does the change do what it claims? Any logic errors or edge cases missed?
2. **Security** — Check for injection, unvalidated input, hardcoded secrets, unsafe deserialization, auth/authorization gaps, and unsafe dependencies. Name the class of vulnerability and the failure path.
3. **Test coverage** — Identify behaviours the diff introduces or changes that have no corresponding test. Say which test is missing and what it should assert.
4. **Naming & maintainability** — Flag names that are misleading, ambiguous, or too vague to reveal intent; explain what the reader would misread.

For each finding, produce a comment that:
- Points to the exact location (file, line or hunk).
- States the issue in one line, then a **"Why this matters"** sentence describing the real consequence (the bug, the breach, the future cost).
- Offers a **concrete suggested fix** or rewrite.

**Format:** Group comments by severity, using these headers in order:
- **Blockers** — must fix before merge (security holes, broken behaviour)
- **Major** — should fix (missing tests, risky design)
- **Minor** — worth fixing (naming, clarity, style)

Each comment as:
`[category: Security|Tests|Naming|Other] file:line — one-line issue`
**Why this matters:** the consequence, in plain language.
**Suggested fix:** the specific change.

Close with a short summary: count of blockers, and one or two things the author did well.

---

**Pull request diff:**

```diff
[paste the diff here]
```
```

---

**Export-equivalent path:** `export/[###] - enhanced-ai-code-review-prompt.md`
**Score and gate status:** CLEAR 42/50 (C8 · L8 · E13 · A9 · R4) | Floors met | Perspectives: 3 | Gate passed
**Format:** Markdown (baseline tokens — no JSON/YAML overhead)
**Assumptions flagged:** `[Assumes: target language/framework is filled in at the placeholder]`, `[Assumes: the diff is pasted into the fenced block below the prompt]`, `[Assumes: severity grouping (Blocker/Major/Minor) matches your team's merge policy — adjust if you use a different scale]`
**Summary:** Your original prompt asks *what's wrong* but gives the model no role, no review dimensions and no output shape — which is why it produces flat, unexplained comments. The rewrite adds an RCAF structure, forces a reason-before-comment chain of thought, splits the three concerns you named (security, tests, naming) into explicit checks, and prescribes a WHY-first comment format so output reads like a senior reviewer.

Want me to also produce a companion PR-template prompt that lets the author self-review before requesting a human? Just say the word.