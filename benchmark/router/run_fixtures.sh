#!/usr/bin/env bash
# Deterministic route-contract fixture runner.
# Exits 0 only when every fixture routes exactly as the manifest expects;
# any mismatch prints the diff and fails the gate. This is the regression
# oracle for the executable route contract: the same command must fail on a
# naive substring/keyword-first router (which would bind $short-but-deep-
# complex to DEEP, or match ask inside basket) and pass on the exact-token,
# word-boundary one.
set -uo pipefail
cd "$(dirname "$0")"
python3 route_contract.py fixtures.json
