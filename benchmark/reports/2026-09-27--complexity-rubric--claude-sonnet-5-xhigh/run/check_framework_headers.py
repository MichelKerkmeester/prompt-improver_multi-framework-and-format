#!/usr/bin/env python3
"""Check each collected framework-coverage deliverable's header against its target.

Reads every SFW and PFW ID's framework, tier and format from framework-targets.json
next to this script, finds that ID's collected file in export/benchmark/skill/ or
export/benchmark/claude project/, and reads the single-line header
(`Mode: ... | Complexity: ... | Framework: ...`, or the same line behind a YAML `#`).

- Framework: the header names the target, compared without case, spaces, hyphens,
  quotes or a qualifier in brackets, so `RCAF (Layered)` reads as RCAF.
- Tier: a number is read as n/10 against the tier's range. A label is read as its
  tier name, and a Complex item also passes on a label above High such as
  `Very High`. A bare `High` names the High tier, so it fails a Complex item.
- Format: the file extension matches the target's format command.

Usage: check_framework_headers.py <export/benchmark folder> [--ids ID,ID]
Prints one line per ID: id | framework | tier | header framework | header
complexity | format | verdict, where the verdict is PASS, TIER, FRAMEWORK, FORMAT
or NO FILE.
Exit codes:
  0  every checked ID has a file whose header and format match
  1  at least one ID is missing a file or misses a check
"""
import json
import os
import re
import sys

TARGETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "framework-targets.json")
TIERS = {"Medium": (5, 6), "High": (7, 8), "Complex": (9, 10)}
LABELS = {"Medium": {"medium"}, "High": {"high"}, "Complex": {"complex", "very high"}}
EXTENSIONS = {"$markdown": {".md"}, "$json": {".json"}, "$yaml": {".yaml", ".yml"}}
HEADER = re.compile(r"^\s*#?\s*\**Mode:?\**\s*(.+)$", re.I)


def norm(name):
    name = re.sub(r"\(.*?\)", "", name or "")
    return re.sub(r"[\s\-_\"'`]", "", name).lower()


def header_fields(path):
    """The header's fields as a dict, read from the first lines of the file."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for _ in range(6):
            line = fh.readline()
            if not line:
                break
            m = HEADER.match(line.strip().strip("`"))
            if m and "|" in line:
                fields = {"mode": m.group(1).split("|")[0].strip()}
                for part in line.split("|")[1:]:
                    if ":" in part:
                        k, v = part.split(":", 1)
                        fields[k.strip().strip("*").lower()] = v.strip().strip("*` ")
                return fields
    return None


def tier_ok(value, tier):
    """True when a complexity label or number sits inside the tier."""
    if not value:
        return False
    num = re.search(r"(\d+)\s*/\s*10", value) or re.match(r"(\d+)\b", value)
    if num:
        lo, hi = TIERS[tier]
        return lo <= int(num.group(1)) <= hi
    return value.strip().lower() in LABELS[tier]


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    out = argv[1]
    only = set(argv[argv.index("--ids") + 1].split(",")) if "--ids" in argv else set()
    targets = json.load(open(TARGETS, encoding="utf-8"))["targets"]
    rows, misses = [], 0
    for t in targets:
        if only and t["id"] not in only:
            continue
        folder = os.path.join(out, t["side"])
        files = sorted(f for f in os.listdir(folder) if f.startswith(t["id"] + " - ")) if os.path.isdir(folder) else []
        best = None
        for f in files:
            h = header_fields(os.path.join(folder, f)) or {}
            fw_ok = norm(h.get("framework")) == norm(t["framework"])
            cx_ok = tier_ok(h.get("complexity"), t["tier"])
            ext_ok = os.path.splitext(f)[1].lower() in EXTENSIONS[t["format"]]
            cand = (fw_ok and cx_ok and ext_ok, fw_ok, ext_ok, h.get("framework"), h.get("complexity"),
                    os.path.splitext(f)[1])
            if best is None or cand[:3] > best[:3]:
                best = cand
        if best is None:
            rows.append((t["id"], t["framework"], t["tier"], "-", "-", "-", "NO FILE"))
            misses += 1
            continue
        verdict = "PASS" if best[0] else ("FRAMEWORK" if not best[1] else "FORMAT" if not best[2] else "TIER")
        misses += verdict != "PASS"
        rows.append((t["id"], t["framework"], t["tier"], best[3] or "-", best[4] or "-", best[5], verdict))
    for r in rows:
        print(" | ".join(r))
    print(f"{len(rows)} IDs checked, {len(rows) - misses} pass, {misses} miss")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
