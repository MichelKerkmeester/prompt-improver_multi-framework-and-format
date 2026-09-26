```
Mode: $improve | Complexity: High (7/10) | Framework: TIDD-EC

{
  "task": "Audit the title, description and bullet points of one supplement marketplace listing against a supplied list of EU-authorised health claims, and flag every health claim in the text that is not covered by that list.",
  "instructions": [
    "Read the inputs supplied with this call: 'title' (string), 'description' (string), 'bullet_points' (array of strings), and 'approved_claims' (array of up to 38 EU-authorised health claim strings).",
    "Scan the title, the description, and each bullet point independently for health claims: any sentence or clause linking the product or an ingredient to a health benefit, bodily function, disease outcome, or recommended intake.",
    "For each health claim found, compare its meaning, not its exact wording, against every entry in 'approved_claims'. Treat a claim as compliant if it conveys the same nutrient-function relationship as an approved claim, even when phrased differently.",
    "If a claim is compliant, leave it untouched: do not flag it, do not rewrite it, and do not mention it anywhere in the output.",
    "If a claim is not covered by 'approved_claims', flag it and classify the violation as exactly one of 'unauthorised_claim', 'disease_claim', or 'dosage_promise' using the distinctions in 'dos'.",
    "For every flag, write a compliant rewrite that keeps the same underlying product fact or ingredient reference but reframes or removes the unapproved claim so the sentence would pass against 'approved_claims'.",
    "Do not evaluate or comment on non-health-claim text such as branding, size, flavor, price, or ingredient lists that carry no health claim.",
    "If no non-compliant claims are found anywhere in the listing, return an empty 'flags' array and set 'status' to 'pass'."
  ],
  "dos": [
    "Quote the flagged sentence exactly as it appears in the source field, with no paraphrasing, in 'exact_sentence'.",
    "Classify 'disease_claim' whenever text implies preventing, treating, or curing a disease or medical condition, even softened ('helps fight colds', 'keeps illness away').",
    "Classify 'dosage_promise' whenever text specifies or implies a quantity, frequency, or duration tied to a stronger or guaranteed effect ('take 2 daily for best results', 'more effective at higher doses').",
    "Classify 'unauthorised_claim' for any other health claim not covered by 'approved_claims' that is neither a disease claim nor a dosage promise.",
    "Preserve every verifiable product fact, such as ingredient name, form, or quantity, already present in the sentence when writing the compliant rewrite.",
    "Record which field each flag came from: 'title', 'description', or the specific bullet_points index."
  ],
  "donts": [
    "Do not flag, rewrite, or otherwise alter text that already matches or closely paraphrases an entry in 'approved_claims'.",
    "Do not state or imply whether the product actually works, is effective, or is recommended; only compare claim text to the approved list.",
    "Do not invent a fourth violation category; every flag must use exactly one of the three listed values.",
    "Do not add product facts, ingredients, or benefits that are not already present in the source text when writing a rewrite.",
    "Do not return prose, commentary, or explanation outside the defined 'output_schema'."
  ],
  "examples": [
    {
      "case": "unauthorised_claim",
      "input_sentence": "Boosts your immune system",
      "in_approved_list": false,
      "rule_broken": "unauthorised_claim",
      "compliant_rewrite": "Contains Vitamin C, which contributes to the normal function of the immune system",
      "explanation": "The generic 'boosts' language is not on the approved list; the rewrite maps the same ingredient to its actual approved wording."
    },
    {
      "case": "compliant, not flagged",
      "input_sentence": "Vitamin C contributes to the normal function of the immune system",
      "in_approved_list": true,
      "rule_broken": null,
      "compliant_rewrite": null,
      "explanation": "Matches an approved claim; must be left untouched and omitted from the flags output entirely."
    },
    {
      "case": "disease_claim",
      "input_sentence": "Helps prevent colds and flu",
      "in_approved_list": false,
      "rule_broken": "disease_claim",
      "compliant_rewrite": "Contains Vitamin C, which contributes to the normal function of the immune system",
      "explanation": "References prevention of named illnesses, which is a disease claim regardless of the approved-claims list content."
    },
    {
      "case": "dosage_promise",
      "input_sentence": "Take 2 capsules daily for maximum energy results",
      "in_approved_list": false,
      "rule_broken": "dosage_promise",
      "compliant_rewrite": "Take as directed on pack. Contains Vitamin B12, which contributes to normal energy-yielding metabolism",
      "explanation": "Prescribes a quantity and frequency tied to a stronger promised outcome, which is a dosage promise independent of the approved-claims list."
    }
  ],
  "context": {
    "domain": "EU supplement-brand marketplace listing compliance",
    "target_model": "GPT-4.1",
    "per_call_inputs": ["title", "description", "bullet_points", "approved_claims (38 EU-authorised health claims)"],
    "regulatory_basis": "EU Nutrition and Health Claims Regulation register, represented by the 38-item approved_claims list supplied with each call",
    "consumer": "Automated listing checker pipeline that gates listing text before publish",
    "out_of_scope": "Efficacy judgments about whether the product works, and any change to text already compliant"
  },
  "output_schema": {
    "status": "'pass' if no flags found, else 'flagged'",
    "flags": [
      {
        "field": "title | description | bullet_points[index]",
        "exact_sentence": "verbatim flagged text",
        "rule_broken": "unauthorised_claim | disease_claim | dosage_promise",
        "compliant_rewrite": "rewritten sentence keeping the product fact"
      }
    ]
  }
}

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide JSON] | assumptions = [input field names title/description/bullet_points/approved_claims inferred, claim matching is semantic (same nutrient-function meaning) not exact-string, output_schema (status/flags) invented to operationalize the four required per-flag outputs, two illustrative examples added for disease_claim and dosage_promise since only one worked example was supplied] | format = JSON | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-supplement-listing-compliance-checker.json`

**Score and gate status:** CLEAR 45/50 (C9·L9·E13·A9·R5) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed

**Token overhead:** JSON adds roughly +5-10% tokens versus an equivalent Markdown version, mainly from field quoting and the nested `examples`/`output_schema` structure.

**Summary:** The original one-line instruction gave no way to distinguish the three violation types, no matching logic, and no output contract, so I rebuilt it in TIDD-EC: explicit semantic-matching instructions, three named `dos` distinguishing unauthorised/disease/dosage violations, hard `donts` protecting compliant text and excluding efficacy judgments, your worked example plus two illustrative ones covering the other two rule types, and a concrete `output_schema` so the flagged-sentence, rule, and rewrite triad is always machine-parseable. Four assumptions were made to close open points per your instruction and are flagged above rather than asked about.