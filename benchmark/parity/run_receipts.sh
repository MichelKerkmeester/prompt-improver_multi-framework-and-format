#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: RECEIPT CHECK RUNNER
# ───────────────────────────────────────────────────────────────
# This system's entry into the upload receipt check. A receipt is the only
# record that a live Project was updated, and it stops being trustworthy the
# moment the kernel or the knowledge directory moves, so this wrapper runs the
# shared checker with the receipt required and supplies the one per-system
# thing: the id.
#
# Exit Codes:
#   2 - the script directory could not be entered, so nothing ran
#   Any other status is the shared check's own, passed through by exec
set -uo pipefail
cd "$(dirname "$0")" || exit 2

exec python3 "../../../z — Claude Project Sync Loop/validate_parity.py" prompt-improver --receipts "$@"
