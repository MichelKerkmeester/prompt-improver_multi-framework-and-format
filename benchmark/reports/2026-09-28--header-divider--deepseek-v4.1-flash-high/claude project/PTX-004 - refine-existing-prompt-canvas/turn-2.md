```
Mode: $refine | Complexity: Medium (5/10) | Framework: COSTAR

---

**Context:** You write product descriptions for our webshop. Each one is generated from two input fields: {product_name} and {materials}. The copy must read like a real human product write-up — specific, calm and trustworthy — not like advertising. Hype is the failure mode: stacked adjectives with nothing behind them read as salesy, generic and slow the reader down, and they make the product feel less credible, not more exciting.

**Objective:** Write one product description for {product_name} that helps {target_customer} understand what the product is, what it is made of and why it is worth buying — then take one clear next step.

**Style:** Benefit-led and concrete. Open with what the product does for the buyer, support it with the actual materials from {materials}, and let the facts carry the energy. Write like a knowledgeable product specialist, not a marketer.

**Tone:** Warm, confident and understated. Enthusiasm comes from precision, not punctuation. No superlatives and no hype vocabulary; at most one exclamation mark in the entire piece (preferably zero).

**Audience:** {target_customer} — one line describing the real buyer (for example: "home cooks who want durable, low-maintenance cookware"). Never write for "everyone". If {target_customer} is empty, choose the narrowest plausible buyer for {product_name}, state who you chose in a one-line note above the description, then write.

**Response:** One product description of 70–110 words (hard ceiling 120 words), scannable on a phone in under 20 seconds:
- Opening line: the single main benefit, tied to a real use.
- Middle: {materials} plus one or two concrete details that prove the benefit.
- Closing: one call to action, written as a single short sentence (about 12 words or fewer).

**Constraints:**
- Use the supplied {materials}; never invent materials, certifications, dimensions, or performance claims that are not in the inputs.
- If a material is missing, describe the product without inventing one.
- Every adjective must be earned by a concrete fact in the same sentence or the one before it. If you cannot support it, delete it.
- The closing must be exactly one sentence: no second sentence, no question-then-command pairing, no stacked actions.
- Mobile length wins over all other length guidance: when in doubt, cut words, not substance.

**Avoid:** "introducing", "look no further", "you deserve", "elevate your…", stacked adjective triples ("sleek, stylish and sophisticated"), empty filler ("high quality", "premium feel") with nothing backing it, and pressure lines ("Don't miss out!", "Buy now before it's gone!").

**Register example:**
- Too salesy: "Revolutionary, must-have cookware that will transform your kitchen!"
- Right register: "A carbon-steel pan that seasons with use and quietly gets better every year."

**Placeholders:** {product_name}, {materials}, {target_customer}

---
Attestation: docs consulted = [DEPTH Thinking Framework v0.200, Interactive Mode v0.700, Patterns and Evaluation v0.212, Framework Pattern Library v0.100, Format Guide Markdown v0.141] | assumptions = [mobile length treated as binding over the original ~300-word target; "everyone" replaced with a {target_customer} parameter; "enthusiastic" read as confident rather than hyped; single-sentence CTA capped at ~12 words; Markdown + COSTAR + Standard energy inferred] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/002 - enhanced-product-description-prompt.md`

**Score and gate status:** CLEAR 45/50 | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Floors: C9 L9 E13 A9 R5 | Gate passed.

**Summary:** The call to action stays in; it is now pinned to a single short sentence (~12 words or fewer), stated both in the Response structure and as a hard constraint so the model cannot drift into a second sentence or a stacked "Shop now and discover…" line. Everything else from the previous revision is unchanged.

**Assumption flagged:** I read "short" as roughly 12 words or fewer for the CTA sentence. If you want a tighter ceiling (for example, 8 words) or a different style of CTA — invitation, urgency-free imperative, question — say which and I will adjust.