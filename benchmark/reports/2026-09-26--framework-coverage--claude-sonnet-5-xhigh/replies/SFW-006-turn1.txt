**Saved:** `export/001 - enhanced-outage-communication-prompt.md`
**CLEAR:** 46/50 | Gate: passed | Framework: COSTAR | Perspectives: 5 (Deep)

Rebuilt as a reusable COSTAR prompt for Gemini 2.5 Pro: shared Context/Objective/Style/Tone carry the outage rules (known/unknown/next-update, no cause-guessing, no data-exposure mentions unless confirmed, phone number always present), then Audience and Response are broken out per channel (SMS, email, phone script) exactly as requested, with a bracketed incident-facts block for repeat use.

Two judgment calls worth flagging:
`[Assumes: the 300-character SMS cap applies per language, i.e., two separate texts (NL, EN), not one combined bilingual message]`
`[Assumes: the direct clinic phone number is one network-wide number; if each of the 14 clinics has its own line, that field should become a per-clinic list before running]`