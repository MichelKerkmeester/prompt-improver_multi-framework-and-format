# Grading 4: SFW-019 to SFW-024 and PFW-019 to PFW-024

Graded against the playbook as it stood at run time, `scratchpad/graded-playbook/sk-prompt-improver/manual-testing-playbook`. Run folder `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh`. Scores are taken from the reported score line and gate status, as the scenarios' Evidence sections ask, and were not rescored.

```csv
id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note
SFW-019,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Fails only on tier because the header reads Complexity Low (4/10) against the High band of 7 to 8, with export, path-first reply, five labelled FRAME elements, VISUAL 53/60, facts, scope and invitation all holding."
PFW-019,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on commentary before the block, a Low (4/10) header outside the High tier and a dropped fact since Zeeland appears nowhere in the block, while the five FRAME labels, VISUAL 55/60, attestation, no-save and invitation hold."
SFW-020,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Fails on a Medium (5/10) header outside the Complex tier, Focus, Rendering and Atmosphere having no labels, and a sampler suggestion the user did not ask for."
PFW-020,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on commentary before the block, a Medium (5/10) header outside the Complex tier, three unlabelled FRAME elements and altered facts since Leiden is dropped and the children are moved onto a rooftop terrace."
SFW-021,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on a Medium (5/10) header outside the High tier and a dropped fact since the 8 second close-up loses her thumbs smoothing the rim."
PFW-021,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Fails only on tier because the header reads Medium (5/10) against the High band, with block-first delivery, six labelled MOTION elements, VISUAL ~64/70 passed, facts, scope and invitation holding."
SFW-022,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on a reply that opens with a YAML check sentence instead of the saved path, a Low (3/10) header outside the Complex tier, the chime moved from the end to 8 seconds and a constraints section adding a no on-screen text or logos rule."
PFW-022,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on a Low (4/10) header outside the Complex tier, four of six MOTION elements with no key, the chime moved from the end to the clock start and no voices narrowed to no spoken dialogue."
SFW-023,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on a reply that opens with a quality-check sentence instead of the saved path and on dropped facts since v0, the standing inspector and e-commerce are all missing from the file."
PFW-023,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on dropped facts since v0 is named in neither the header nor the body and the standing inspector is gone, while block order, High (7/10) tier, prose VIBE elements, EVOKE ~44/50, scope and invitation hold."
SFW-024,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Fails on a Medium (6/10) header outside the Complex tier and on altered facts since MagicPath is named nowhere in the file and the app becomes a Dutch e-bike insurance app."
PFW-024,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Fails only on tier because the header reads High (7/10) and the Complex tier needs 9 or 10 or a label above High, with every other item holding."
```

---

## Per-scenario grading

### SFW-019, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` shows `created: ["export/001 - enhanced-zeeland-gravel-hero-midjourney-prompt.md"]`, the sandbox `exports/export/` holds the file and it is byte-identical to the benchmark copy. The transcript's last tool call is the `Write`, and the reply's first line is ``Saved: `export/001 - enhanced-zeeland-gravel-hero-midjourney-prompt.md` ``
- Prompt not pasted: holds. The reply quotes only the parameter string `--ar 21:9 --style raw --s 250 --q 2 --v 6.1`, recorded as a fragment and not the prompt (judgment call)
- Header names FRAME inside the High tier: FAILS. Header reads `Mode: $image | Complexity: Low (4/10) | Framework: FRAME`. FRAME holds, mode label `$image`, but 4 sits below the 7 to 8 band
- FRAME elements labelled: holds. Bold labels `Focus`, `Rendering`, `Atmosphere`, `Modifiers`, `Exclusions`, plus a `Full Prompt (copy-paste ready)` line the scenario allows as the Midjourney payload
- VISUAL passes: holds. `VISUAL 53/60 | Gate: passed`, gate 48
- Facts: holds. Midjourney v6.1, Zeeland, gravel dyke path, golden hour, low angle toward camera, Oosterschelde behind, photorealistic catalogue look, warm light and long shadows, 21:9 with the left third empty for the headline, and the three exclusions as positive phrasing plus `--no` terms. The olive jersey sits only in the full prompt line, not in Focus, recorded. The homepage hero purpose survives as the "headline overlay" banner rule, read as kept (judgment call)
- Scope: holds. The 85mm lens and DSLR, and the watermark and signature exclusions, are read as defaults inside the Rendering and Exclusions elements that the user's "pick sensible parameters yourself" invites, not as a new output or section (judgment call)
- Share-back invitation: holds. "Try it in Midjourney and share the result"
- Advisory: the summary is one long sentence plus the invitation, recorded

### PFW-019, project, FAIL

- Deliverable Block before any commentary: FAILS. The reply opens with "Confirmed FRAME is the correct framework for `$image`. Proceeding to deliver" and a second paragraph, "Since no Canvas panel exists in this environment, the Deliverable Block is rendered as a single fenced block first". The scenario counts an environment note as commentary
- Header, prompt and attestation, no save claimed: holds. The fenced block carries the header and ends with `execution = did not occur | save = did not occur`. The chat gives an "Export-equivalent path" with a guessed `001`, not presented as saved
- Prompt not pasted again: holds
- Header names FRAME inside the High tier: FAILS. `Complexity: Low (4/10)`, mode label `$image`
- FRAME elements labelled: holds. `F`, `R`, `A`, `M`, `E` each with its element name, plus a paste-ready full prompt
- VISUAL passes: holds. `VISUAL 55/60`, "Gate passed"
- Facts: FAILS. Zeeland is absent from the whole block (grep count 0), so the location in "Zeeland gravel-cycling tours" is dropped. The exclusion "no other people" became a bare `people` in `--no text, logo, branding, watermark, signature, people, crowd, second rider, cars, road signage`, which also works against the one rider, recorded as a second alteration (judgment call)
- Scope: holds. 24mm at f/5.6, about 3000K, clouds and calm air, and the cars and road signage exclusions are read as defaults inside the elements (judgment call)
- Share-back invitation: holds. "Try this prompt in Midjourney v6.1 and share the result with me"

### SFW-020, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-night-of-science-poster-prompt.md`, the sandbox copy matches the benchmark file, the `Write` precedes the reply and the first line is ``Saved: `export/001 - enhanced-night-of-science-poster-prompt.md` ``
- Prompt not pasted: holds
- Header names FRAME inside the Complex tier: FAILS. `Mode: $image | Complexity: Medium (5/10) | Framework: FRAME`
- FRAME elements labelled: FAILS. The file has three labels, `Positive Prompt`, `Negative Prompt` and `Parameters`. Exclusions maps to the negative prompt and Modifiers to Parameters, but Focus, Rendering and Atmosphere are merged into the unlabelled positive prompt. The reply's "Perspectives: 5 (Focus, Rendering, Atmosphere, Modifiers, Exclusions)" does not make them visible in the file
- VISUAL passes: holds. `VISUAL 55/60 | Gate: passed`
- Facts: holds. Leiden city library, Night of Science, 2:3, flat 1960s screen print, the four HEX codes exact, the three layers in order, the empty top quarter with no lettering, grain and misregistration, children about 8 to 10 and non-photoreal, weights, separate negative prompt, CFG and steps. ComfyUI is not named, but SDXL is named and the negative prompt is split for its separate field, read as kept (judgment call). The positive prompt asks for Orion's stars "scattered across" the sky while the negative excludes "random scattered stars", recorded as an internal conflict
- Scope: FAILS. "Sampler suggestion: DPM++ 2M Karras or Euler a" is a settings field the user did not ask for, since the request names only CFG and steps, and the reply flags it as an assumption (judgment call, since a sampler could be read as a default)
- Share-back invitation: holds. "Share the generated result when you want refinement"

### PFW-020, project, FAIL

- Deliverable Block before any commentary: FAILS. The reply opens with a routing paragraph, "Mode/format resolved from routing: `$image` → Image Mode", and a no-Canvas note before the fence
- Header, prompt and attestation, no save claimed: holds. The attestation ends `execution = did not occur | save = did not occur`, the path is written `export/[###] - enhanced-night-of-science-poster.md` and nothing is claimed saved. The captured file carries `NNN` in its name, recorded
- Prompt not pasted again: holds
- Header names FRAME inside the Complex tier: FAILS. `Complexity: Medium (5/10)`, mode label `$image`
- FRAME elements labelled: FAILS. Only `Positive Prompt`, `Negative Prompt` and `Suggested Settings`, with `Foreground`, `Midground` and `Background` as inline layer labels. Focus, Rendering and Atmosphere have no labelled part
- VISUAL passes: holds. `VISUAL 55/60`, "Gate passed"
- Facts: FAILS. "the Leiden city library" became "a public library" (Leiden count 0), and the foreground children now stand "on a rooftop terrace at a (large brass telescope:1.2)", which relocates the first layer. ComfyUI is not named while SDXL is, read as kept
- Scope: holds. The 1024x1536 resolution is read as the pixel form of the requested 2:3 ratio, and the halftone pattern and "Masterpiece, best quality" as defaults inside the positive prompt (judgment call). The rooftop terrace is graded under facts
- Share-back invitation: holds. "Try this prompt in ComfyUI and share what you get"

### SFW-021, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-runway-potter-bowl-video-prompt.md`, the sandbox copy matches, the `Write` is the last tool call and the reply opens with the `Saved:` path
- Prompt not pasted: holds. The reply names the `"Dolly forward:"` prefix only
- Header names MOTION inside the High tier: FAILS. `Mode: $video | Complexity: Medium (5/10) | Framework: MOTION`
- MOTION elements labelled: holds. Bold `Movement`, `Origin`, `Temporal`, `Intention`, `Orchestration`, `Nuance`
- VISUAL passes: holds. `VISUAL 62/70 | Gate: passed`, gate 56, and the prompt carries camera and subject motion
- Facts: FAILS. The user's beat "a close-up of her thumbs smoothing the rim at 8 seconds" became "a tight close-up on her thumbs by second 8", so "smoothing the rim" is dropped (grep count 0). All other facts hold, including Runway Gen-4 image-to-video, the sunlit studio, 10 seconds at 9:16 for Reels, the rising bowl, the slip spiral, the dust in window light, waist height, the hold, warm light, shallow depth of field, the face out of frame and the soft clutter
- Scope: holds. No audio section and nothing unasked
- Share-back invitation: holds. "Try this prompt in Runway and share the result with me"

### PFW-021, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens directly with the ```` ```markdown ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the chat gives an "Export-equivalent path" with a guessed `001`, not presented as saved
- Prompt not pasted again: holds. The chat summary describes beats and does not repeat the prompt
- Header names MOTION inside the High tier: FAILS. `Complexity: Medium (5/10)`, mode label `$video`
- MOTION elements labelled: holds. `M`, `O`, `T`, `I`, `O`, `N` each with its element name under "MOTION Breakdown". The extra `Platform`, `Reference Image`, `Duration`, `Aspect Ratio` fields and the paste-ready prompt hold the user's own facts, recorded
- VISUAL passes: holds. "VISUAL ~64/70", "Gate passed". The score is approximate, read as a reported pass above 56 (judgment call)
- Facts: holds. "a close-up on her thumbs smoothing the rim at 8 seconds, then holds steady" is kept, along with every other beat
- Scope: holds. "intimate documentary style" is read as a style default. The Nuance line "No audio track (Runway Gen-4 has no native audio)" is a note that no audio is added, not an audio section (judgment call)
- Share-back invitation: holds. "Try this prompt in Runway Gen-4 and share the result with me!"
- Advisory: the summary runs two sentences, inside the band

### SFW-022, skill, FAIL

- Delivery, export saved before a path-first reply: FAILS on path-first. The `.yaml` export exists (`meta.json`, sandbox copy identical to the benchmark file, `Write` then a `Bash` syntax check before the reply), but the reply's first line is "YAML body parses cleanly, no tabs, valid syntax. VISUAL scoring self-check landed at 62/70", and the `**Saved:**` path comes on the third line
- Prompt not pasted: holds
- Header names MOTION inside the Complex tier: FAILS. `Mode: $video | Complexity: Low (3/10) | Framework: MOTION`, plain form, not a YAML comment
- MOTION elements labelled: holds. `movement`, `origin`, `temporal`, `intention`, `orchestration`, `nuance` sit as keys under one `motion` wrapper
- VISUAL passes: holds. `VISUAL 62/70 | Gate: passed`
- Payload parses: holds. Python `yaml.safe_load` on the lines below the header returns a mapping with top-level keys `platform` through `constraints`
- Facts: FAILS. "a distant chime at the end" became "one distant chime as the clock starts moving", and the 8 second beat reads "Distant chime marks the sweep", so the chime moves from the end of a 10 second shot to 8 seconds. No music and no voices survive as "No score, no dialogue" in the prompt and `dialogue or voices` in `audio.excluded`. The Kling camera wording used is "[move up]" and "crane up", recorded
- Scope: FAILS. The extra top-level `constraints` section adds "No on-screen text or logos" and "No negative or quality-keyword prompting", and `nuance.physics` adds "no slow motion or speed ramps", none of which the user asked for. Under the scenario's rule an extra top-level section passes only when it holds the user's own facts (judgment call on the physics line). The `audio` and `visual_style` sections hold user facts and pass as recorded extras
- Share-back invitation: holds. "Share the generated result when you want refinement"
- Recorded, not in the Pass/fail line: the three to seven percent token overhead is not reported

### PFW-022, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```yaml ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, path given as `export/[###] - enhanced-aalsmeer-flower-auction-opening-shot.yaml`. The captured file carries `NNN`, recorded
- Prompt not pasted again: holds
- Header names MOTION inside the Complex tier: FAILS. `Mode: $video $yaml | Complexity: Low (4/10) | Framework: MOTION`
- MOTION elements labelled: FAILS. Only `intention` and `camera.origin` carry element names. Movement is spread across `camera` and `subject`, Temporal across `duration`, `beat_4s` and `beat_8s`, and Orchestration and Nuance have no key of their own
- VISUAL passes: holds. `VISUAL 62/70`, "Gate passed (56+ threshold...)"
- Payload parses: holds. `yaml.safe_load` on the lines between the header and the `---` before the attestation returns a mapping
- Facts: FAILS. "a distant chime at the end" became "a single distant chime as the clock hand starts to move", and "no voices" became "no spoken dialogue", which narrows the exclusion (judgment call on the second). "about three metres" became "three metres", recorded as minor
- Scope: holds. `style: naturalistic documentary aesthetic` is flagged in the attestation as a default for the unstated style, and `mood` and "before trading begins" are read as defaults (judgment call)
- Share-back invitation: holds. "Try this prompt in Kling 2.6 and share the generated clip with me"
- Recorded: token overhead "+3-7%" is reported

### SFW-023, skill, FAIL

- Delivery, export saved before a path-first reply: FAILS on path-first. The export exists (`meta.json`, identical sandbox copy, `Write` before the final `Grep`), but the reply opens with "No quality-spam language, and the file exports as valid Markdown with the required single-line header." and the `**Saved:**` path is on line three. The transcript confirms that sentence opens the final assistant message after the last tool call
- Prompt not pasted: holds
- Header names VIBE inside the High tier: holds. `Mode: $vibe | Complexity: High (7/10) | Framework: VIBE`
- VIBE elements: holds as prose. Vision maps to "warm-neutral surfaces, generous breathing room, typography sized to be caught in a glance", Inspiration to "a well-lit instrument panel in a photo lab", Behavior to the grade-card and reject-capture paragraphs, Experience to "item 40 or item 300" and "Nothing here should feel gamified"
- EVOKE passes: holds. `EVOKE 44/50 (Standard, threshold 40+) | Gate: passed`, grounding pre-check reported passed
- Facts: FAILS. v0 is named in neither the header nor the body (grep for `v0` returns nothing in the file), which the scenario requires. "An inspector stands at a bench" lost "stands", and "fashion e-commerce warehouse" became "a fashion warehouse". shadcn/ui is kept with its library line
- Scope: holds. The avoid-list naming and the UX-floor paragraph are rule-mandated and recorded. The record waiting on scan, the between-item transition and "a paired scanner or keyboard" are read as defaults inside the Behavior and floor passages (judgment call)
- Share-back invitation: holds. "Share the result once you generate it in v0"
- Advisory: 350 words against the v0 range of 100 to 300, recorded

### PFW-023, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```markdown ```` fence, and the no-Canvas note follows the block
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the export-equivalent path uses a guessed `001` not presented as saved
- Prompt not pasted again: holds
- Header names VIBE inside the High tier: holds. `Mode: $vibe | Complexity: High (7/10) | Framework: VIBE`
- VIBE elements: holds as prose. Vision in "warm neutral surfaces, generous single-glance zones, and typography", Inspiration in "a boarding-gate scanner crossed with the tactile satisfaction of a photo booth's countdown", Behavior in the `Layout:` and reject-capture paragraphs, Experience in "trust builds tap after tap" and "steady and unhurried at item 300"
- EVOKE passes: holds. "EVOKE ~44/50", "Gate passed at 40+ threshold", approximate score read as a reported pass (judgment call)
- Facts: FAILS. v0 appears only in the attestation ("target platform read as v0.dev"), which is neither header nor body, so the scenario's "named in the header or the body" does not hold. The standing inspector is dropped ("a gloved inspector"). "300 items a shift" became "300 returned garments a shift", recorded as a minor narrowing (judgment call)
- Scope: holds. The avoid-list, "customized rather than left in their default state" and the UX-floor paragraph are rule-mandated and recorded. One colour family for A to C with a distinct reject zone is the named aesthetic choice, read as a default
- Share-back invitation: holds. "Try this prompt in v0 and share what it generates"
- Advisory: 377 words against the v0 range, recorded. The "Complexity note" offers a streamlined version "just ask", an offer after delivery and not a question instead of delivery

### SFW-024, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-ebike-theft-claim-magicpath-brief.md`, the sandbox copy matches, and the reply opens with the `Saved:` path
- Prompt not pasted: holds
- Header names VIBE-MP inside the Complex tier: FAILS. `Mode: $vibe | Complexity: Medium (6/10) | Framework: VIBE-MP`
- VIBE-MP elements and MagicPath calibration: holds as prose. Vision in the amber-on-asphalt palette and transit-board type, Inspiration in the station high-vis signage and the parcel or flight-status board, Behavior in the screen and back-arrow paragraphs, Experience in the opening paragraph. The avoid-list names Duolingo/Headspace and Stripe/Mercury. The single aesthetic risk, the safety-vest amber accent, is implied rather than named as the risk, read as mappable (judgment call)
- EVOKE passes: holds. "EVOKE (MagicPath) ≈ 45/50 | Gate: passed", gate 42, approximate score read as a reported pass (judgment call)
- Facts: FAILS. MagicPath appears nowhere in the file (grep count 0) and the scenario requires it in the header or body. "No component library, let MagicPath choose" became "No pre-built component library, let the composition stay native to this brief". "our e-bike insurance app" became "a Dutch e-bike insurance app", an unstated fact. The five screens, back links, signal-loss draft, Dutch and English and the tone are kept in meaning
- Scope: holds. The avoid-list and UX floor are rule-mandated. One-handed use, the station correction affordance and the named tracker milestones are read as defaults inside the requested screens (judgment call)
- Share-back invitation: holds. "Share your result for refinement once you generate the MagicPath output"
- Advisory: 448 words against the MagicPath range of 150 to 400, recorded. The reply's "It stays framework-free per your instruction" misstates the request, recorded

### PFW-024, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```markdown ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the export-equivalent path uses a guessed `001` not presented as saved
- Prompt not pasted again: holds
- Header names VIBE-MP inside the Complex tier: FAILS. `Complexity: High (7/10)`. The Complex tier needs the label `Complex`, 9 or 10, or a label above High
- VIBE-MP elements and MagicPath calibration: holds as prose. Vision in "graphite, slate, paper-white", Inspiration in "a well-run intake desk" and "a case file being assembled", Behavior in the back-link, draft and page-turn passages, Experience in the opening paragraph. The avoid-list and "As the one deliberate risk" are both named
- EVOKE passes: holds. "EVOKE-MP 46/50", "Gate passed at 42+/50 threshold"
- Facts: holds. MagicPath named ("let MagicPath choose its own materials"), all five screens in order, back links, signal-loss draft, steady and competent, Dutch and English, no component library. "generic fintech gradient" rendered as "the purple-to-blue gradient fintech-onboarding look" is read as the named default, not an alteration (judgment call)
- Scope: holds. The numbered progress rail is the rule-mandated single aesthetic risk, and "not as a bolted-on toggle" is flagged as an assumption about bilingual support, read as a default
- Share-back invitation: holds. "Try this in MagicPath and share what it generates"
- Advisory: 385 words, inside the MagicPath range

---

## Twin agreement

- SFW-019 and PFW-019: agree on FAIL. Both carry `Low (4/10)`. The Project twin also fails on commentary before the block and on dropping Zeeland, while the skill twin fails on tier alone
- SFW-020 and PFW-020: agree on FAIL. Both have `Medium (5/10)` and the same three unlabelled FRAME elements. The skill twin adds a sampler field, the Project twin opens with commentary and drops Leiden and adds a rooftop terrace
- SFW-021 and PFW-021: agree on FAIL. Both have `Medium (5/10)`. Only the skill twin drops "smoothing the rim", so the Project twin fails on tier alone
- SFW-022 and PFW-022: agree on FAIL. Both sit at Low (3 and 4 of 10) and both move the chime off the end. The skill twin labels all six MOTION keys but misses path-first and adds constraints, while the Project twin labels only two of six elements
- SFW-023 and PFW-023: agree on FAIL. Both reach High (7/10) with mappable prose and a passing EVOKE, and both lose v0 and the standing inspector. The skill twin also misses path-first and drops e-commerce
- SFW-024 and PFW-024: agree on FAIL. Both sit below the Complex tier (Medium 6 and High 7). The skill twin also drops MagicPath and adds "Dutch" to the app, while the Project twin fails on tier alone
