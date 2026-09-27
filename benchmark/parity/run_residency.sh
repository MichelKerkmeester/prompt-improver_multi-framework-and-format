#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: RESIDENCY CHECK RUNNER
# ───────────────────────────────────────────────────────────────
# This system's entry into the shared residency check. The rows live in the
# parity declaration and the checker reuses the parity gate's readers, so this
# file supplies the only per-system thing: the id.
#
# Exit Codes:
#   2 - the script directory could not be entered, so nothing ran
#   Any other status is the shared check's own, passed through by exec
set -uo pipefail
cd "$(dirname "$0")" || exit 2

exec bash "../../../z — Claude Project Sync Loop/run_residency.sh" prompt-improver
