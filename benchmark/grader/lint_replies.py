#!/usr/bin/env python3
"""Run the Deliverable Block linter over every reply a benchmark run captured.

`deliverable_lint.py` reads one file and prints one JSON object. Nothing before this
pointed it at a whole run, so this walks a run's `replies/` directory, lints each file
through the same `lint_reply()` the single-file tool calls, writes `deliverable-
lint.csv` beside it and returns an exit code that means something.

A linter that returns 0 whether a file is clean or carries a hard violation has
already been read as a pass once in this fleet, over a different system's linter. This
returns 0 only when every reply is clean, 1 when any reply carries a hard violation and
2 when there was nothing to read, so a caller that checks the code learns what the run
said rather than that the tool ran.

A dirty reply is a finding about the runtime that produced it, not about this
repository, so it belongs in a run record rather than in a source-tree gate. This
reports what a runtime wrote. It never edits a reply.

A single file is accepted too, with `--brief` printing one line rather than a table, so
a per-dispatch caller can report what it just captured without embedding a JSON reader
in shell, which is its own source of quoting defects a syntax check will not see.

Usage:
  lint_replies.py <run report dir or replies dir>
  lint_replies.py <file> --brief
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deliverable_lint import lint_reply  # noqa: E402  path set above

TEXT_SUFFIXES = {".txt", ".md"}


def replies_dir(target: Path) -> Path:
    """The directory holding reply files, given either it or the run root."""
    if (target / "replies").is_dir():
        return target / "replies"
    return target


def lint_file(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    violations, confidence = lint_reply(raw)
    hard = [v for v in violations if v["severity"] == "hard"]
    return {
        "file": path.name,
        "clean": not hard,
        "hard_violations": len(hard),
        "violations": ", ".join(f"{v['type']}x{v['count']}" for v in violations) or "none",
        "confidence": confidence,
    }


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: lint_replies.py <run report dir or replies dir>", file=sys.stderr)
        return 64
    brief = "--brief" in argv[1:]
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: lint_replies.py <run report dir or replies dir>", file=sys.stderr)
        return 64
    target = Path(args[0]).resolve()

    if target.is_file():
        row = lint_file(target)
        if brief:
            print("clean" if row["clean"] else f"DELIVERABLE {row['violations']}")
        else:
            print(f"  {row['file']}  {'clean' if row['clean'] else 'DIRTY'}  {row['violations']}")
        return 0 if row["clean"] else 1

    if not target.is_dir():
        print(f"{target} is not a directory, so no reply was read", file=sys.stderr)
        return 2
    directory = replies_dir(target)
    rows = [lint_file(p) for p in sorted(directory.iterdir())
            if p.is_file() and p.suffix in TEXT_SUFFIXES]
    if not rows:
        print(f"no reply files under {directory}, so nothing was linted", file=sys.stderr)
        return 2

    out = directory.parent / "deliverable-lint.csv"
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    width = max(len(r["file"]) for r in rows)
    for r in rows:
        print(f"  {r['file'].ljust(width)}  {'clean' if r['clean'] else 'DIRTY'}  {r['violations']}")
    dirty = [r for r in rows if not r["clean"]]
    print(f"  {len(rows) - len(dirty)} clean of {len(rows)}, written to {out.name}")
    if dirty:
        print(f"FAILED {len(dirty)} reply/replies carry a Deliverable Block hard violation")
        return 1
    print("PASSED every reply clean of Deliverable Block hard violations")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
