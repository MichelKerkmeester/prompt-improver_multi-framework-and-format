```markdown
Mode: $deep | Complexity: Complex (10/10) | Framework: COSTAR

**Context:**
Barter runs 14 physiotherapy clinics. When the shared booking platform fails, clinic staff need to notify patients and prepare front-desk teams fast, using only the facts known at that moment. Before each use of this prompt, supply the three inputs below; treat the incident facts as the only source of truth for what is "known" and "not yet known." Do not add, infer, or reference any detail — cause, scope, systems affected, or data exposure — that is not stated in the pasted facts.

`[INCIDENT FACTS: paste the latest known details — what happened, when it started, what is affected, what is confirmed, what is still being investigated]`
`[NEXT UPDATE COMMITMENT: the specific time or window your team commits to, e.g. "within 2 hours" or "14:00 CET"]`
`[DIRECT CLINIC PHONE NUMBER: the number patients should call]`

Patients range from teenage athletes to patients in their 80s, so every version — English and Dutch, every channel — must be understandable to a reader with plain (CEFR B1) reading ability.

**Non-negotiable ground rules for every one of the six outputs below:**
- State only what the pasted facts confirm as known.
- State plainly what is not yet known or confirmed.
- State the next-update commitment.
- Never speculate about or name a cause; if the facts do not state one, say only that the cause is not yet confirmed.
- Never mention data exposure, a breach, or compromised data unless the pasted facts explicitly say so.
- Always include the direct clinic phone number.
- If a Dutch version risks exceeding a stated length limit, shorten wording before dropping any of the above elements; never drop the phone number or the next-update commitment.

**Objective:**
First, parse the incident facts into two buckets — confirmed/known and not yet known — and pair them with the separately supplied next-update commitment and phone number, so every channel and language stays consistent with the same underlying facts. Then draft six labeled outputs from those buckets: an SMS (English and Dutch), an email (English and Dutch), and a front-desk phone script (English and Dutch). Each language pair within a channel must say the same substantive things, scaled to that channel's length and reading context, so patients and staff never receive contradictory information about the same outage.

**Style:**
Plain language at CEFR B1 level in both English and Dutch: short sentences, common vocabulary, no technical or system jargon beyond what the facts state, no speculation, no filler phrases.

**Tone:**
Formal but empathetic in both languages: acknowledge the disruption without over-apologizing or alarming the reader. In Dutch, use the formal register (u/uw), never the informal je/jij.

**Audience — SMS:**
Patients with a confirmed appointment in the next 48 hours. They are reading on a phone, often between other activities, with no context beyond the message itself — ages span teenage athletes to patients in their 80s.

**Response — SMS:**
Produce "SMS – English" and "SMS – Dutch," each a maximum of 300 characters including spaces. Order within the limit: what's known → what's not yet known → next-update commitment → direct clinic phone number. Show the character count after each version. If a version cannot fit all four elements even after removing filler and using contractions, shorten the "not yet known" phrase last; never omit the phone number or the next-update commitment.

**Audience — Email:**
All active patients across the 14 clinics, including those with no appointment in the immediate future. They may read this on any device, at any time, and may include parents or guardians of teenage patients.

**Response — Email:**
Produce "Email – English" and "Email – Dutch," each with: a subject line under 60 characters, a brief greeting, three short labeled sections ("What we know," "What we don't know yet," "When we'll update you next"), the direct clinic phone number, and a brief empathetic sign-off. Target 120–180 words per language version.

**Audience — Phone Script:**
Front-desk staff at all 14 clinics, who will read or paraphrase this aloud to patients calling in. They need a version in each language to match the caller, and enough guidance to stay calm and consistent.

**Response — Phone Script:**
Produce "Phone Script – English" and "Phone Script – Dutch," each structured as: an opening acknowledgment of the outage, "what we know" talking points, "what we don't know yet" talking points, the next-update commitment, a line reconfirming the direct clinic phone number for the caller's reference, and a closing line. End each script with a short "Do not say" reminder for staff: never guess at or name a cause, never mention data exposure unless the facts confirm it, and if a caller asks something the facts don't cover, acknowledge the question and repeat the "not yet known" and "next update" language rather than improvising.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = direct clinic phone number and next-update commitment are supplied per use as single values, separate from the pasted incident facts | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-outage-communication-prompt.md`

**Score and gate status:** CLEAR 44/50 (C9 · L9 · E13 · A9 · R4 — all floors cleared) | Perspectives: 5 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer, Framework Architecture Expert, Token Optimisation Specialist) | Gate passed on first pass.

**Assumptions flagged:** `[Assumes: "direct clinic phone number" is one number supplied per use for the affected clinic, not a list of all 14]` · `[Assumes: the next-update commitment is a business decision your team sets at drafting time, not derived from the incident facts]`.

**Summary:** The rebuilt prompt keeps your full scope — three channels, two languages, six labeled outputs — under a single COSTAR structure with a shared Context/Objective/Style/Tone and a dedicated Audience/Response pair per channel. It forces a parse-facts-first step so SMS, email and phone-script versions can never contradict each other, hard-caps the SMS at 300 characters with an explicit compression priority order, and encodes your never-guess-the-cause and conditional-data-exposure rules as non-negotiable ground rules rather than suggestions.