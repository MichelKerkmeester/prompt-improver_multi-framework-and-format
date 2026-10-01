#!/usr/bin/env bash
# ───────────────────────────────────────────────────────────────
# COMPONENT: ROUTE FIXTURE RUNNER
# ───────────────────────────────────────────────────────────────
# Deterministic route-contract fixture runner plus the kernel parity gate.
# Exits 0 only when every fixture routes exactly as the manifest expects and
# the kernel's Router Code still equals the skill's router minus comments.
# Any mismatch prints the diff and fails the gate. This is the regression
# oracle for the executable route contract: the same command must fail on a
# naive substring/keyword-first router (which would bind $short-but-deep-
# complex to DEEP, or match ask inside basket) and pass on the exact-token,
# word-boundary one.
#
# The parity gate runs second because it oracles a different copy: fixtures
# prove the contract still routes, and kernel_parity.py proves the kernel's
# one python fence is the skill's Smart Router Pseudocode with its comments
# removed, so a hand edit to either copy fails the run.
#
# Exit Codes:
#   0 - Every fixture routed as the manifest expects and kernel parity held
#   1 - At least one fixture mismatched or the parity gate failed
#   2 - The run was refused before any fixture was checked
set -uo pipefail
cd "$(dirname "$0")" || exit 2

python3 route_contract.py fixtures.json
fixtures=$?
python3 kernel_parity.py
parity=$?

if [ "$fixtures" -eq 2 ]; then
    exit 2
fi
if [ "$fixtures" -ne 0 ] || [ "$parity" -ne 0 ]; then
    exit 1
fi
exit 0
