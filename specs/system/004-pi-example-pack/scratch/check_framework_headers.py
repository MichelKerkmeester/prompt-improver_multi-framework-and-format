#!/usr/bin/env python3
"""Check each collected framework-coverage deliverable's header against its target.

Reads the brief for every SFW and PFW ID's framework and tier, finds that ID's
collected files in export/benchmark/skill/ and export/benchmark/claude project/,
and reads the single-line header (`Mode: ... | Complexity: ... | Framework: ...`,
or the same line behind a YAML `#`). A file passes when its framework matches the
target and its complexity sits inside the tier. A label is read as its tier name,
and a number as n/10 against the tier's range.

Usage: check_framework_headers.py <export/benchmark folder> [--ids ID,ID]
Exit codes:
  0  every checked ID has a file whose header matches
  1  at least one ID is missing a file or has no matching header
"""
import json
import os
import re
import sys

BRIEF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "framework-brief.json")
TIERS = {"Medium": (5, 6), "High": (7, 8), "Complex": (9, 10)}
LABELS = {"Medium": {"medium"}, "High": {"high"}, "Complex": {"complex", "very high", "high"}}
HEADER = re.compile(r"^\s*#?\s*\**Mode:?\**\s*(.+)$", re.I)


def norm(name):
    """Framework names compared without a qualifier in brackets, quotes, case,
    spaces or hyphens, so `RCAF (Layered)` reads as RCAF."""
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
    only = set()
    if "--ids" in argv:
        only = set(argv[argv.index("--ids") + 1].split(","))
    pairs = json.load(open(BRIEF, encoding="utf-8"))["pairs"]
    rows, misses = [], 0
    for p in pairs:
        for sid, folder in ((p["skill_id"], "skill"), (p["project_id"], "claude project")):
            if only and sid not in only:
                continue
            d = os.path.join(out, folder)
            files = sorted(f for f in os.listdir(d) if f.startswith(sid + " - ")) if os.path.isdir(d) else []
            best = None
            for f in files:
                h = header_fields(os.path.join(d, f)) or {}
                fw_ok = norm(h.get("framework")) == norm(p["framework"])
                cx_ok = tier_ok(h.get("complexity"), p["tier"])
                cand = (fw_ok and cx_ok, fw_ok, f, h.get("framework"), h.get("complexity"))
                if best is None or cand[:2] > best[:2]:
                    best = cand
            if best is None:
                rows.append((sid, p["framework"], p["tier"], "-", "-", "NO FILE"))
                misses += 1
                continue
            verdict = "PASS" if best[0] else ("TIER" if best[1] else "FRAMEWORK")
            misses += verdict != "PASS"
            rows.append((sid, p["framework"], p["tier"], best[3] or "-", best[4] or "-", verdict))
    for r in rows:
        print(" | ".join(r))
    print(f"{len(rows)} IDs checked, {len(rows) - misses} pass, {misses} miss")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
