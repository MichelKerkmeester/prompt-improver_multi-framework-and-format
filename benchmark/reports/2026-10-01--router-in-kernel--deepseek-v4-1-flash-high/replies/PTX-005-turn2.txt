```markdown
Mode: $raw | Complexity: Low (2/10) | Framework: none (raw passthrough)

---

Summarise the attached quarterly sales report for the exec team.

- Use bullet points.
- Highlight the regions that missed target.
- Do not make up numbers — use only figures stated in the report.
- Maximum 1 page.
- Finish with the three products that sold worst.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode | assumptions = the report is attached in the same conversation; "regions" means the report's own regional breakdown; "the three products that sold worst" comes from the report's product-level figures; "1 page" means one page of plain text | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/005 - enhanced-quarterly-sales-summary-for-exec.md` (same deliverable, updated — replaces the earlier version)

**Score and gate status:** no scorer applied — Raw mode (`$raw`) is passthrough cleanup, so perspectives = 0 and the CLEAR/EVOKE/VISUAL gates are not run.

**Token overhead:** none — Markdown deliverable.

**Summary:** Added your new ask as a fifth bullet, placed last to match the "end with" placement you wanted, and left the rest of the prompt untouched. The one thing worth flagging is that this line only works if the report itself breaks sales down by product — if it doesn't, ChatGPT will either skip the instruction or reach for numbers that aren't there, which is the exact failure your "do not make up numbers" line is guarding against.