# Prompt Improver - Claude Project Packaging

Hand-maintained local package for the Prompt Improver claude.ai Project. The kernel and every knowledge file are written by hand from the authoritative skill sources; `Custom Instructions.md` remains hand-synthesized. The live claude.ai Project is a separate manual upload because the claude.ai UI has no repository lock.

## Structure

```text
claude project/
|-- Custom Instructions.md        <- full synthesized Project kernel v1.4.7, Skill v1.3.0 aligned; the routing authority for this Project (SKILL.md is not loaded here)
|-- README.md                     <- this manifest and sync contract
`-- knowledge/                    <- upload every file below as Project Knowledge
    |-- Prompt Improver - DEPTH Thinking Framework - v0.200.md
    |-- Prompt Improver - Interactive Mode - v0.700.md
    |-- Prompt Improver - Patterns and Evaluation - v0.212.md
    |-- Prompt Improver - Assets - Framework Pattern Library - v0.100.md
    |-- Prompt Improver - Format Guide Markdown - v0.141.md
    |-- Prompt Improver - Format Guide JSON - v0.142.md
    |-- Prompt Improver - Format Guide YAML - v0.142.md
    |-- Prompt Improver - Visual Mode - v0.301.md
    |-- Prompt Improver - Assets - Visual Mode Library - v0.110.md
    |-- Prompt Improver - Image Mode - v0.123.md
    |-- Prompt Improver - Assets - Image Mode Library - v0.101.md
    |-- Prompt Improver - Video Mode - v0.123.md
    `-- Prompt Improver - Assets - Video Mode Library - v0.101.md
```

## Custom Instructions = Skill Kernel, Project-Adapted

`Custom Instructions.md` is the synthesized claude.ai Project kernel, v1.4.7, aligned to **Prompt Improver Skill v1.3.0**. It is the routing authority for this Project, because `SKILL.md` is not loaded here and no longer ships as a Project Knowledge mirror. It preserves prompt-only scope, DEPTH energy, smart routing (exact-token commands, command-wins, word-boundary keyword scoring, independent format lock), framework selection, CLEAR/EVOKE/VISUAL scoring, format locks and delivery rules.

CLI-only mechanics are removed or adapted: filesystem export becomes the **Deliverable Block**, direct file loading becomes Project Knowledge consultation and `export/[###] - enhanced-[description].[md|json|yaml]` is reported as an export-equivalent path.

## Paired-Version + Checksum Table

Knowledge files are hand-authored for Project retrieval, so the checksum table the retired AI System Sync Compiler generated here is gone and no hash ledger is kept. Drift is watched by the read-only commit-timestamp comparison of the manual parity method instead.


## Set Up The Live Project

1. Create or open the claude.ai Project named **Prompt Improver**.
2. Paste `Custom Instructions.md` into the Project custom instructions field.
3. Upload every file in `knowledge/` as Project Knowledge.
4. Keep filenames unchanged so the kernel can reference the documents clearly.
5. Run a smoke prompt for all ten routed intents (Raw, Text, Improve, Refine, Short, Deep, Visual, MagicPath, Image, Video) plus Interactive fallback, a false-command case, MagicPath-over-Visual precedence and format-lock independence from mode.
6. Confirm the Deliverable Block, attestation footer and export-equivalent path appear, and the routed score appears for every mode except Raw, which carries no score.

## Change Checklist

- Update the skill sources first, then hand-write the matching changes into `claude project/Custom Instructions.md` and the affected `claude project/knowledge/` files per the manual parity method, or record that no Project-facing change is needed and why
- If identity, routing, scoring, format handling or delivery behavior changes, re-derive `Custom Instructions.md` from the Skill kernel.
- On a version bump, rename the mirror to the new version suffix and remove the superseded versioned mirror. Never retain old and new filenames together.
- After a kernel change, record the review as a dated sentence in the system SYNC.md review notes: who reviewed, what changed, what was decided
- Before live upload, run this system's own checks from its root. The sync compiler was
  retired and `check --system` no longer exists, so nothing is verified by invoking it:
  - `bash benchmark/router/run_fixtures.sh`
  - `bash benchmark/parity/run_parity.sh`
- Re-upload changed files to the live Project and confirm the upload took.

## Known Notes

- Project Knowledge may be retrieved as chunks rather than full files, so the Project kernel repeats the core gates and routing contract.
- `SKILL.md` is no longer mirrored into `knowledge/`; `Custom Instructions.md` is the sole routing authority for this Project, since a Project cannot load `sk-prompt-improver/SKILL.md` directly.
- Largest mirrors by byte count: Image Mode Library 48614 bytes, Visual Mode 40363 bytes, Video Mode Library 35063 bytes. Advisory only. Review chunking behavior if any mirror grows meaningfully past this range.
- No compact fallback instructions file exists yet. Add one only if paste-testing shows the full kernel does not fit.
