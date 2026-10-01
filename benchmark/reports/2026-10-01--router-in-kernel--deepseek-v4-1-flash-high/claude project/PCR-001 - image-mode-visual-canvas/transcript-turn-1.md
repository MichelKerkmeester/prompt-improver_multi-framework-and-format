# PCR-001 turn 1 transcript

**User:** $image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.

**Tool call:** `ls` `{"path": ".", "limit": 100}`

**Tool call:** `ls` `{"path": "knowledge", "limit": 200}`

**Tool result:** `ls`

```text
Custom Instructions.md
knowledge/
```

**Tool result:** `ls`

```text
Prompt Improver - Assets - Framework Pattern Library - v0.100.md
Prompt Improver - Assets - Image Mode Library - v0.101.md
Prompt Improver - Assets - Video Mode Library - v0.101.md
Prompt Improver - Assets - Visual Mode Library - v0.110.md
Prompt Improver - DEPTH Thinking Framework - v0.200.md
Prompt Improver - Format Guide JSON - v0.142.md
Prompt Improver - Format Guide Markdown - v0.141.md
Prompt Improver - Format Guide YAML - v0.142.md
Prompt Improver - Image Mode - v0.123.md
Prompt Improver - Interactive Mode - v0.700.md
Prompt Improver - Patterns and Evaluation - v0.212.md
Prompt Improver - Video Mode - v0.123.md
Prompt Improver - Visual Mode - v0.301.md
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Image Mode - v0.123.md", "offset": 1, "limit": 400}`

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md", "offset": 1, "limit": 400}`

**Tool result:** `read`

```text
# Prompt Improver - Image Mode - v0.123

Specialized mode for optimizing prompts for AI image generators including Flux 2 Pro, Google Imagen 4 (Nano Banana Pro), Runway, Midjourney, DALL-E 3, Stable Diffusion, Seedream, Leonardo, and Ideogram.

---

## 1. OVERVIEW

### Purpose

Transform vague visual requests into structured, platform-optimized image prompts using the FRAME framework and VISUAL scoring system.

### When to Use

- Activated by `$image` / `$img` commands
- Image generation prompts and platform-specific optimization
- Composition vocabulary, style references, and anti-pattern detection

---

## 2. OBJECTIVE

Transform vague visual descriptions into detailed, evocative prompts optimized for AI image generators.

**Commands:** `$image`, `$img`
**DEPTH Rounds:** 5 (creative iteration)
**Framework:** FRAME
**Scoring:** VISUAL (60 points, 48+ threshold)

**Core Philosophy:**
> "Describe what you see, feel, and sense—not what you want the AI to figure out."

**Key Principles:**
1. **Subject first** - Lead with the main focus, add context after
2. **Specificity over abstraction** - "Golden retriever puppy" not "dog"
3. **No negative prompts on newer models** - Flux 2 Pro, Imagen 4 ignore them
4. **Natural language** - Modern models prefer conversational prompts
5. **Platform awareness** - Each generator has unique syntax and strengths
6. **Reference images** - Use when available for consistency (multi-reference supported)

The kernel points here for the negative-prompt
```

**Tool result:** `read`

```text
# Prompt Improver - Assets - Image Mode Library - v0.101

Reusable FRAME prompt banks, platform structures, examples, refinement templates and quick lookups for image generation prompts.

---

## 1. OVERVIEW

### Purpose

Provides copyable image-generation vocabulary, platform prompt structures, examples, refinement templates and quick lookup material separated from the Image Mode workflow.

### Usage

Use this with `Prompt Improver - Image Mode - v0.123` for `$image` or `$img` work. Copy, adapt or consult the relevant section after the reference workflow identifies the target platform and FRAME needs.

---

## 2. FRAME SUB-CATEGORY BANKS

### F - FOCUS (30%) - 6 Sub-Categories

The Focus component defines WHAT the viewer sees and HOW the scene is composed.

#### F1. Shot Types

- **Extreme Wide**
  - Frame Coverage: Full environment
  - Use Case: Establishing, epic landscapes
  - Example Prompt Fragment: "extreme wide shot of mountain range"
- **Wide Shot**
  - Frame Coverage: Full body + setting
  - Use Case: Context, action, architecture
  - Example Prompt Fragment: "wide shot showing full figure in forest"
- **Medium Wide**
  - Frame Coverage: Knees-up
  - Use Case: Fashion, full outfit display
  - Example Prompt Fragment: "medium wide capturing outfit and pose"
- **Medium Shot**
  - Frame Coverage: Waist-up
  - Use Case: Conversation, portraits
  - Example Prompt Fragment: "medium shot from the waist up"
- **Medium Close-Up**
  - Frame Coverage: Chest-up
  - Use Case: Em
```

**Tool call:** `read` `{"path": "knowledge/Prompt Improver - Image Mode - v0.123.md", "offset": 401, "limit": 120}`

**Tool call:** `grep` `{"pattern": "Midjourney", "path": "knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md", "context": 3, "limit": 80}`

**Tool result:** `read`

```text
- **Tag soup**
  - Problem: "trending on artstation, 8k"
  - Transform To: Remove entirely

### Platform-Specific Anti-Patterns

- **Flux 2 Pro**
  - Avoid: Weighted syntax, negatives
  - Use Instead: Natural sentences
- **Imagen 4**
  - Avoid: Complex negatives
  - Use Instead: Clear positive description
- **Midjourney**
  - Avoid: Overly long prompts
  - Use Instead: Concise, comma-separated
- **DALL-E 3**
  - Avoid: Keyword lists
  - Use Instead: Natural paragraphs
- **Stable Diffusion**
  - Avoid: Missing negatives
  - Use Instead: Always include negative prompt

### Vague-to-Specific Transformation

```yaml
vague_to_specific:
  "portrait" → "medium close-up portrait, soft natural lighting, shallow depth of field"
  "landscape" → "wide shot landscape at golden hour, dramatic clouds, leading lines"
  "product" → "product photography on white seamless, soft box lighting, sharp focus"
  "fantasy" → "epic fantasy illustration, dramatic lighting, detailed environment"
  "modern" → "contemporary minimalist aesthetic, clean lines, muted color palette"
  "vintage" → "1970s Kodachrome aesthetic, warm tones, subtle grain"
```

---

## 10. TRANSFORMATION EXAMPLES

Templates: see `Prompt Improver - Assets - Image Mode Library - v0.101`

---


## 11. ITERATIVE REFINEMENT FLOW

### Post-Delivery Question (MANDATORY)

Templates: see `Prompt Improver - Assets - Image Mode Library - v0.101`


### Iteration Best Practices

- **1st**
  - Focus: Composition validation
  - Typical Adjustments
```

**Tool result:** `grep`

```text
Prompt Improver - Assets - Image Mode Library - v0.101.md-653- - **Imagen 4**
Prompt Improver - Assets - Image Mode Library - v0.101.md-654-   - Quality Markers: Not needed (quality is automatic)
Prompt Improver - Assets - Image Mode Library - v0.101.md-655-   - Avoid: Quality keywords
Prompt Improver - Assets - Image Mode Library - v0.101.md:656: - **Midjourney**
Prompt Improver - Assets - Image Mode Library - v0.101.md-657-   - Quality Markers: `--q 2` for max, `--style raw` for realism
Prompt Improver - Assets - Image Mode Library - v0.101.md-658-   - Avoid: Excessive quality words
Prompt Improver - Assets - Image Mode Library - v0.101.md-659- - **DALL-E 3**
Prompt Improver - Assets - Image Mode Library - v0.101.md-671- 
Prompt Improver - Assets - Image Mode Library - v0.101.md-672- #### M3. Emphasis Syntax by Platform
Prompt Improver - Assets - Image Mode Library - v0.101.md-673- 
Prompt Improver - Assets - Image Mode Library - v0.101.md:674: - **Midjourney**
Prompt Improver - Assets - Image Mode Library - v0.101.md-675-   - Emphasis Method: `::2` weight, `--sref` style, `--cref` char
Prompt Improver - Assets - Image Mode Library - v0.101.md-676-   - Example: `dragon::2 castle::1`
Prompt Improver - Assets - Image Mode Library - v0.101.md-677- - **SD/SDXL**
Prompt Improver - Assets - Image Mode Library - v0.101.md-689- 
Prompt Improver - Assets - Image Mode Library - v0.101.md-690- #### M4. Library Parameters
Prompt Improver - Assets - Image Mode Library - v0.101.md-691- 

```

**Tool call:** `read` `{"limit": 300, "offset": 600, "path": "knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md"}`

**Tool call:** `read` `{"limit": 200, "offset": 1180, "path": "knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md"}`

**Tool result:** `read`

```text
  - Visual Effect: Everything sharp, starburst
  - Use Case: Architecture, landscapes
- **Tilt-Shift**
  - Aperture Equivalent: Variable selective
  - Visual Effect: Miniature/toy effect
  - Use Case: Cityscapes, creative

---

### M - MODIFIERS (15%) - 6 Sub-Categories

The Modifiers component defines TECHNICAL PARAMETERS and platform-specific controls.

#### M1. Aspect Ratio Presets

- **1:1**
  - Dimensions Example: 1024x1024
  - Platform/Use Case: Instagram, social media square
  - Best For: Profiles, product shots
- **4:5**
  - Dimensions Example: 1080x1350
  - Platform/Use Case: Instagram portrait, Pinterest
  - Best For: Portraits, fashion
- **3:2**
  - Dimensions Example: 1536x1024
  - Platform/Use Case: Standard photography (DSLR native)
  - Best For: Photography, prints
- **16:9**
  - Dimensions Example: 1920x1080
  - Platform/Use Case: Cinematic, video, widescreen
  - Best For: Film stills, banners
- **9:16**
  - Dimensions Example: 1080x1920
  - Platform/Use Case: Stories, Reels, TikTok, mobile
  - Best For: Vertical video, stories
- **2:3**
  - Dimensions Example: 1024x1536
  - Platform/Use Case: Portrait orientation, posters
  - Best For: Portraits, book covers
- **21:9**
  - Dimensions Example: 2560x1080
  - Platform/Use Case: Ultra-widescreen, cinematic
  - Best For: Epic landscapes, banners
- **4:3**
  - Dimensions Example: 1024x768
  - Platform/Use Case: Traditional screen ratio
  - Best For: Presentations, classic

#### M2. Platform-Specific Quality Markers
```

**Tool result:** `read`

```text

### Example 2: Product Shot (Imagen 4)

**Input:**
```
coffee mug photo
```

**Output:**
```
Professional product photograph of a handcrafted ceramic
coffee mug in matte sage green. The mug sits on a light
oak wooden table surface with visible grain texture.

Steam rises gently from fresh coffee inside. The mug features
subtle speckled glaze texture and an organic curved handle.
Text on the mug reads "MORNING RITUAL" in minimal sans-serif.

Soft window light from the right, creating gentle shadows.
Clean, minimalist composition with negative space on left.
Warm, inviting atmosphere. Shot at eye level with shallow
depth of field blurring the background slightly.
```

**VISUAL Score:** 54/60

---

### Example 3: Fantasy Art (Midjourney)

**Input:**
```
dragon
```

**Output:**
```
Ancient dragon perched atop a crumbling stone tower,
wings folded against storm clouds at twilight,
scales gleaming with deep emerald and gold iridescence,
piercing amber eyes surveying the misty valley below,
epic fantasy illustration, dramatic volumetric lighting,
rain falling through god rays, detailed environment
--ar 16:9 --s 500 --style raw
```

**VISUAL Score:** 50/60

---

### Example 4: Street Photography (Stable Diffusion)

**Input:**
```
city scene
```

**Output:**
```
Prompt:
masterpiece, best quality, street photography,
rainy Tokyo alley at night, neon signs reflecting
on wet pavement, lone figure with umbrella walking away,
steam rising from street vents, Blade Runner atmosphere,
shot o
```

**Tool call:** `read` `{"limit": 200, "offset": 1, "path": "knowledge/Prompt Improver - Interactive Mode - v0.700.md"}`

**Tool call:** `read` `{"limit": 250, "offset": 1, "path": "knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md"}`

**Tool result:** `read`

```text
# Prompt Improver - Interactive Mode - v0.700

Conversation flows, state management, and response patterns for interactive prompt enhancement with energy-level-driven DEPTH processing.

---

## 1. OVERVIEW

### Purpose

Defines the conversation architecture, state machine, question protocol, and response patterns that drive interactive prompt enhancement with energy-level-driven DEPTH processing.

### When to Use

- Commands ($raw, $short, $deep, $vibe, etc.) override the question flow
- Routing a request through the single-question flow when no command is supplied
- Managing conversation state, error recovery, and quality-controlled delivery

---

## 2. CONVERSATION ARCHITECTURE

### Primary Flow

```
Start --> Single Question (ALL info) --> Wait --> Process (DEPTH) --> Deliver --> Report
```

### Core Rules

1. **ONE comprehensive question:** Ask for ALL information at once
2. **WAIT for response:** Never proceed without user input (except $raw)
3. **Intent detection:** Commands + NLP. Canonical commands live in the Smart Routing section of the Project instructions.
4. **DEPTH processing:** Apply with two-layer transparency and energy-level scaling
5. **Prompt delivery:** All output properly formatted with transparency report

The kernel points here for the disambiguation rule:

4. **Disambiguate once when unsure.** A request with no command and no keyword hit, or one with conflicting mode commands, enters Interactive Mode: ask one comprehensive question covering the source
```

**Tool result:** `read`

```text
# Prompt Improver - DEPTH Thinking Framework - v0.200

The single thinking system for all prompt improvement work. Five phases, five energy levels, cognitive techniques applied when they add value.

---

## 1. OVERVIEW

### Purpose

Defines DEPTH (Discover, Engineer, Prototype, Test, Harmonize) as a 5-phase thinking system with energy-level scaling, cognitive rigor techniques, CLEAR quality scoring (40+/50), mode-specific scoring for Creative energy (EVOKE, VISUAL), and proof-through-output transparency.

### When to Use

- The one thinking system applied to every prompt improvement task
- Multi-perspective analysis (min 3, target 5) and the cognitive rigor toolkit
- CLEAR quality gates (40+/50) and energy-level-driven phase execution

---

## 2. FRAMEWORK OVERVIEW

### Core Definition

**DEPTH:** **D**iscover **E**ngineer **P**rototype **T**est **H**armonize. Five phases. One thinking system. No other thinking framework is referenced or needed.

### Energy Levels (Canonical Reference)

This table is the source of truth. Every other document in this Project reads its energy levels from here.

- **Raw**
  - Phases: None
  - Perspectives: 0
  - Cognitive Techniques: None
  - When: `$raw`: passthrough, no enhancement
- **Quick**
  - Phases: D → P → H
  - Perspectives: 1-2
  - Cognitive Techniques: Pick 1
  - When: `$short`/`$s`: concise enhancement, quick refinements
- **Standard**
  - Phases: D → E → P → T → H
  - Perspectives: 3 minimum (BLOCKING), target 5
  - Cognitive Techn
```

**Tool call:** `grep` `{"context": 6, "limit": 60, "path": "knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md", "pattern": "VISUAL"}`

**Tool call:** `grep` `{"context": 4, "limit": 40, "path": "knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md", "pattern": "FRAME|Image"}`

**Tool result:** `grep`

```text
Prompt Improver - Patterns and Evaluation - v0.212.md-5- ---
Prompt Improver - Patterns and Evaluation - v0.212.md-6- 
Prompt Improver - Patterns and Evaluation - v0.212.md-7- ## 1. OVERVIEW
Prompt Improver - Patterns and Evaluation - v0.212.md-8- 
Prompt Improver - Patterns and Evaluation - v0.212.md-9- ### Purpose
Prompt Improver - Patterns and Evaluation - v0.212.md-10- 
Prompt Improver - Patterns and Evaluation - v0.212.md:11: Provides the evaluation and enhancement reference set: systematic enhancement patterns and the CLEAR, EVOKE and VISUAL evaluation methodology.
Prompt Improver - Patterns and Evaluation - v0.212.md-12- 
Prompt Improver - Patterns and Evaluation - v0.212.md-13- ### When to Use
Prompt Improver - Patterns and Evaluation - v0.212.md-14- 
Prompt Improver - Patterns and Evaluation - v0.212.md-15- - Read when enhancement patterns or scoring methodology are needed
Prompt Improver - Patterns and Evaluation - v0.212.md-16- - Enhancement patterns, CLEAR/EVOKE/VISUAL scoring, recovery protocols, and mastery principles
Prompt Improver - Patterns and Evaluation - v0.212.md-17- - The framework library and selection algorithms live in `Prompt Improver - Assets - Framework Pattern Library - v0.100`
Prompt Improver - Patterns and Evaluation - v0.212.md-10- 
Prompt Improver - Patterns and Evaluation - v0.212.md-11- Provides the evaluation and enhancement reference set: systematic enhancement patterns and the CLEAR, EVOKE and VISUAL evaluation methodology.
Prompt Improv
```

**Tool result:** `grep`

```text
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-7- ## 1. OVERVIEW
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-8- 
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-9- ### Purpose
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-10- 
Prompt Improver - Assets - Framework Pattern Library - v0.100.md:11: Provide the complete framework lookup set (RCAF, COSTAR, RACE, CIDI, TIDD-EC, CRISPE, CRAFT, VIBE, VIBE-MP, FRAME, MOTION) with selection algorithms, deep dives, combination patterns and optimization strategies.
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-12- 
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-13- ### Usage
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-14- 
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-15- Use when choosing or switching frameworks, combining frameworks or optimizing an existing framework choice. Apply the matrix first, then the deep dive for the selected framework. The evaluation methodology that reads this library stays in `Prompt Improver - Patterns and Evaluation - v0.212`.
Prompt Improver - Assets - Framework Pattern Library - v0.100.md-15- Use when choosing or switching frameworks, combining frameworks or optimizing an existing framework choice. Apply the matrix first, then the deep dive for the selected framework. The evaluation methodology that reads this library stays in `Prompt Improver - Patterns 
```

**Tool call:** `read` `{"limit": 120, "offset": 1, "path": "knowledge/Prompt Improver - Format Guide Markdown - v0.141.md"}`

**Tool call:** `read` `{"limit": 60, "offset": 944, "path": "knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md"}`

**Tool result:** `read`

```text
# Prompt Improver - Format Guide Markdown - v0.141

Formatting guide for Markdown (Standard) output structure in prompt engineering with RCAF/CRAFT frameworks, file delivery standards, syntax validation, and format-specific best practices.

---

## 1. OVERVIEW

### Purpose

Reusable Markdown format rules for exported Prompt Improver deliverables. Defines Markdown syntax specifications, structure patterns, validation rules, and file delivery standards for natural language prompt output, covering RCAF/CRAFT frameworks in Markdown format, file delivery standards, syntax validation, format conversions, advanced patterns, and best practices.

### Usage

- Read for the routed `$markdown` command or when the final prompt must be valid Markdown

---

## 2. FORMAT RATIONALE

### Why Markdown (Standard) Format?

Markdown provides natural language prompt engineering with optimal human readability while maintaining clear structure through RCAF/CRAFT frameworks.

**Terminology:**
- **Framework** = Prompt organization method (RCAF vs CRAFT)
- **Format** = Data structure (Standard/Markdown vs JSON vs YAML)

**See Also:** YAML Format Guide, JSON Format Guide, Interactive Mode, DEPTH guide, Patterns guide

- **Readability**
  - Markdown: Natural language
  - JSON: Structured data
  - YAML: Human-friendly structure
- **Token Usage**
  - Markdown: Baseline (100%)
  - JSON: +5-10%
  - YAML: +3-7%
- **Best For**
  - Markdown: Human interaction
  - JSON: API integration
  - YAML: Configuration
- *
```

**Tool result:** `read`

```text
Pro Tips:
- Strong at text rendering - use for logos, signs, labels
- Leverage multi-reference for character consistency
- Specify aspect ratio explicitly when needed
- Avoid: negative prompts, complex multi-scene requests
```

---

**Midjourney v6.1:**
```
Key Parameters:
--ar [ratio]     : Aspect ratio (16:9, 3:2, 1:1, 9:16)
--s [0-1000]     : Stylization (0=accurate, 1000=artistic)
--c [0-100]      : Chaos/variety (higher=more variation)
--q [.25,1,2]    : Quality (affects generation time)
--style raw      : Less Midjourney aesthetic influence
--sref [url]     : Style reference image
--cref [url]     : Character reference image
--no [item]      : Partial negative support

Optimal Prompt Structure:
[Subject], [action/pose], [setting], [lighting],
[art style], [mood], [composition] --ar [ratio] --s [value]

Example:
Portrait of a cyberpunk hacker, neon-lit Tokyo alley,
rain-slicked streets reflecting holographic advertisements,
blade runner aesthetic, dramatic rim lighting,
cinematic composition --ar 16:9 --s 500 --style raw

Pro Tips:
- Use --style raw for photorealism
- --sref for consistent style across images
- --cref for character consistency
- Lower --s for accuracy, higher for artistic interpretation
```

---

**DALL-E 3:**
```
Key Characteristics:
- Excellent prompt following
- Good text rendering capability
- Natural language preferred
- No negative prompts
- Two sizes: 1024x1024, 1792x1024 (or 1024x1792)
- Two styles: "vivid" (dramatic) or "natural" (realistic)

Op
```

**Assistant:**

```
Mode: $image | Complexity: Low (2/10) | Framework: FRAME
```

```
Log cabin with glowing amber windows in a misty pine forest at dawn, low fog pooling between the trunks, volumetric god rays raking through the trees, weathered timber and stone chimney with thin smoke, wide establishing shot, layered foreground ferns, photorealistic cinema still, anamorphic 35mm, cool blue-grey palette with warm interior glow --ar 16:9 --s 350 --style raw --q 2 --no text, watermark
```

```
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Image Mode, Image Mode Library, Framework Pattern Library, Patterns and Evaluation, Format Guide Markdown | assumptions = 16:9 aspect ratio, --s 350 realism-leaning stylization, --style raw, photorealistic treatment over painterly, empty forest (no figures) | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-misty-forest-cabin-dawn-midjourney.md` (placeholder number — this Project has no filesystem write, so nothing was saved; the block above is the deliverable).

**Score and gate status:** VISUAL 56/60 | Gate passed (threshold 48/60) | Dimensions: Vivid 14/15, Intentional 9/10, Styled 9/10, Unambiguous 9/10, Atmospheric 10/10, Layered 5/5 | Format: Markdown (default, no format command detected) — no token overhead note needed.

**Summary:** Your one-line concept was rebuilt on FRAME: the cabin and its lit windows lead as subject, the rendering locks to a photorealistic cinema still shot on anamorphic 35mm, the atmosphere splits dawn's cool blue-grey mist against the warm amber interior glow, and the modifiers carry Midjourney's own parameter block. Kept to 51 descriptive words because Midjourney rewards concise comma-separated phrasing, and exclusions use `--no` since Midjourney supports only partial negatives.

**Assumptions to check:** I defaulted to 16:9 and a realism-leaning `--s 350` with `--style raw`, and read the scene as empty of people. Say the word and I'll shift to 21:9 for a wider cinematic crop, push `--s` up for a more painterly read, or add a figure on the porch.

---

**🖼️ Share Your Generated Image for Refinement**

Run this in Midjourney and share the result back — paste or upload the image and tell me what's off.

- **Refine the prompt** if the composition, framing or detail isn't right
- **Adjust atmosphere** if the lighting, mist density or colour temperature needs tuning
- **Dial in specifics** the model interpreted differently (cabin architecture, foliage, god-ray intensity)

Just share the output and what you'd like changed, and I'll run another pass.
