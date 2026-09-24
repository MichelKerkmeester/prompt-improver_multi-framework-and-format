# Route Contract (executable)

Deterministic characterization of how Prompt Improver routes a request to an
intent, locks the output format and decides whether to ask one comprehensive
question, so routing behavior is testable without invoking a model. The
skill and project kernels are written against this contract; claude.ai still
interprets prose stochastically, so live adherence testing remains
mandatory.

## Files

- `route_contract.py` — the deterministic router (exact tokens, word-boundary
  keywords, one primary intent, independent format lock, disambiguation,
  resources, schema).
- `fixtures.json` — the expected route objects (test oracle).
- `run_fixtures.sh` — gate runner; exits 0 only when all fixtures pass.

## Run

```bash
bash run_fixtures.sh
# or directly:
python3 route_contract.py fixtures.json
# or inspect a single request:
python3 route_contract.py "$short but this needs a deep and complex multi-step strategic rewrite"
```

## Route object

Every request resolves to one stable object:

```json
{
  "intent": "SHORT",
  "energy": "quick",
  "scorer": "CLEAR",
  "format": "markdown",
  "source": "command",
  "needs_disambiguation": false,
  "resources": [
    "references/depth-framework.md",
    "references/interactive-mode.md",
    "references/patterns-evaluation.md",
    "assets/framework-pattern-library.md",
    "assets/format-guide-markdown.md"
  ]
}
```

The schema rejects unknown or duplicate fields, so the manifest cannot
drift silently from the contract.

## Decision rules (durable rationale)

- **Exact tokens**: only a complete `$token` selects a mode command. `$raw`,
  `$text`/`$t`, `$improve`/`$i`, `$refine`/`$r`, `$short`/`$s`, `$deep`/`$d`,
  `$vibe`/`$v`, `$image`/`$img` and `$video`/`$vid` are matched as whole
  tokens, never as substrings, so a longer word can never carry a bare alias
  into an intent.
- **One primary intent, command wins**: a single explicit mode command beats
  every natural-language signal, so `$short but this needs a deep and
  complex multi-step strategic rewrite` binds SHORT, not DEEP, even though
  DEEP's keywords score far higher. Without a command, the highest
  word-boundary keyword score wins and no second intent loads a second
  resource lane.
- **Command conflict asks, it does not guess**: two distinct mode commands
  in the same request (`$short $deep pick one energy level for me`) are not
  silently resolved to either one; they route to INTERACTIVE so the user
  names the one they meant.
- **Word-boundary keywords**: `\bask\b` matches "ask a question" but never
  "basket"; `\bprompt\b` matches "write me a prompt" but never "promptly".
  A substring hit inside a longer word never selects an intent.
- **Format is an independent axis**: `$json`, `$yaml` and `$markdown`
  (`$j`, `$y`, `$md`, `$m`) lock the output format on their own axis and
  never compete with the mode intent for the primary route. A bare `$json`
  with no mode signal still falls back to INTERACTIVE for the intent while
  `format` stays `"json"` and the JSON guide still loads.
- **Disambiguation gate**: a request with no command and no keyword hit, or
  one with conflicting mode commands, routes to INTERACTIVE with
  `needs_disambiguation=true`, so the router asks one comprehensive question
  instead of inventing the mode.
- **Energy and scorer are derived, not detected**: each intent carries one
  fixed DEPTH energy level and one fixed scorer (`CLEAR` for the text
  family, `EVOKE` for Visual/MagicPath, `VISUAL` for Image/Video, `None`
  for Raw and the meta/topic intents Framework, Scoring, Interactive and
  Thinking, which are informational routes, not a gated deliverable).
- **Runtime discovery + guarded loading**: every routing call resolves
  resource names against the live `references/*.md` and `assets/*.md`
  inventory (discover, existence-check, dedupe). A renamed or deleted
  reference degrades to a smaller resource set instead of a dead path or
  crash. Missing bases contribute nothing without failing.
