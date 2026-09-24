#!/usr/bin/env bash
# Run every after-the-fact check a finished Prompt Improver benchmark report supports.
#
# Nothing before this file looked at a run as a whole. `lint_replies.py` and
# `twin_divergence.py` both take a report directory, but a check that depends on
# someone remembering to run it by hand after every playbook pass is the same as no
# check, and this system had zero of either kind before this phase. One command
# removes the remembering.
#
# Every check still runs after an earlier one reports findings, because stopping at
# the first hides the rest. The exit code is the count of checks that reported
# findings, not the count that failed to run or the first finding's own code, so a
# caller cannot misread one dirty check as the only problem.
#
# What the exit code means: how many checks reported findings, not how many failed to
# run. A dirty reply or a diverging twin is a finding about the runtime that produced
# the report, not a defect in this repository, so a caller reading a non-zero code
# should read the indented output rather than look for something to revert here.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
# Not ${1:?...}, which exits 1, and 1 already means one check reported findings here.
# A caller reading only the code could not tell a usage error from a real finding.
if [ $# -lt 1 ]; then
  echo "usage: check_report.sh <run report dir>" >&2
  exit 64
fi
REPORT="$1"
if [ ! -d "$REPORT" ]; then
  echo "no report directory at $REPORT, so nothing was checked" >&2
  exit 66
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

found=0
total=0
for check in lint_replies twin_divergence; do
  total=$((total + 1))
  printf '  %-16s ' "$check"
  if python3 "$HERE/$check.py" "$REPORT" > "$WORKDIR/$check.out" 2>&1; then
    echo "clean"
  else
    rc=$?
    if [ "$rc" = 2 ] || [ "$rc" = 64 ]; then
      echo "could not run, its own output follows"
      sed 's/^/      /' "$WORKDIR/$check.out"
      found=$((found + 1))
      continue
    fi
    echo "findings, its own output follows"
    sed 's/^/      /' "$WORKDIR/$check.out"
    found=$((found + 1))
  fi
done

echo
if [ "$found" = 0 ]; then
  echo "all $total report checks clean"
  exit 0
fi
echo "$found of $total report checks reported findings"
exit "$found"
