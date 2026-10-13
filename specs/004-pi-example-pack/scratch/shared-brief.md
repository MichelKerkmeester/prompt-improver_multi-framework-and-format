# Shared brief: Prompt Improver example pack

Every agent on this packet reads this file. It fixes the inputs of the eight new scenario pairs and the canonical wording of the rules the scenarios must state, so parallel writers produce the same text.

Paths are relative to `AI Systems/Prompt Improver/` unless they start with `specs/`.

## 1. House rules for every agent

- Never write an em dash or an en dash used as a dash. Use a comma, a colon, parentheses or a spaced hyphen. The repo gate enforces this.
- Touch only the files your own brief names. Never edit `SKILL.md`, `AGENTS.md`, anything under `sk-prompt-improver/references/` or `assets/`, or anything under `claude project/`.
- Never commit, stage, stash or reset. Another session holds uncommitted work in this tree.
- Read a file before you edit it. Cite a line number only after reading that line in the current file.

## 2. Canonical rule wordings

These rules are already in force: `d473b93` put the first three into `SKILL.md`, `AGENTS.md` and the kernel, and the root playbook states the fourth. Scenario files state them with this wording, adapted only for the runtime.

**Scope test.** A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect.

**Revision.** A revision the user asks for after a delivery is a new deliverable under the next number. Skill set: it saves as a new `export/[###]` file and never edits the delivered export in place. Project set: it renders a new Deliverable Block under the next export-equivalent name.

**Canvas stand-in (Project set only).** With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it.

**Summary band.** The two to three sentence summary is advisory under the root's Defect severity section. A summary outside the band is recorded and never decides a verdict.

**One consolidated question.** When essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message. Asking two things in that one message is correct. Splitting them across messages is the failure.

## 3. New scenario pairs

Each pair shares one exact Turn 1 prompt and one exact Turn 2 input, character for character across the skill and Project files. The skill file lives in `skill-<category>/`, the Project twin in `project-<category>/`. The Real user request is the same ask in natural words, without command tokens.

### STX-002 / PTX-002: `$deep` system prompt

- Category: text modes. Scorer: CLEAR. Format: Markdown.
- Turn 1: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`
- Turn 2: `Customers also write in Dutch. Keep the internal note in English, but quote the customer's key sentence in their own language.`

### STX-003 / PTX-003: `$short` quick enhancement

- Category: text modes. Scorer: CLEAR at Quick energy. Format: Markdown.
- Turn 1: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`
- Turn 2: `Mention that she joins us from Spotify.`

### STX-004 / PTX-004: `$refine` an existing prompt

- Category: text modes. Scorer: CLEAR. Format: Markdown.
- Turn 1: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`
- Turn 2: `Keep the call to action, but make it one short sentence.`

### STX-005 / PTX-005: `$raw` cleanup

- Category: text modes. Scorer: none, Raw mode skips DEPTH, questions and scoring. Format: Markdown.
- Turn 1: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`
- Turn 2: `Also ask it to end with the three products that sold worst.`

### SFM-002 / PFM-002: `$text $yaml` format lock

- Category: format modes. Scorer: CLEAR. Format: YAML.
- Turn 1: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`
- Turn 2: `Some invoices carry two VAT rates. Add a VAT breakdown with rate and amount per rate.`

### SFM-003 / PFM-003: `$improve $markdown` format lock

- Category: format modes. Scorer: CLEAR. Format: Markdown, locked by the long-form `$markdown` token.
- Turn 1: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`
- Turn 2: `Also have it flag any TODO comments left in the diff.`

### SCR-002 / PCR-002: `$video $yaml` motion prompt

- Category: creative modes. Scorer: VISUAL. Format: YAML.
- Turn 1: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`
- Turn 2: `Make it 6 seconds and end on a slow push-in instead of the orbit.`

### SCR-003 / PCR-003: `$vibe` UI concept

- Category: creative modes. Scorer: EVOKE. Format: Markdown.
- Turn 1: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`
- Turn 2: `She also wants to see yesterday's waste per shop.`
