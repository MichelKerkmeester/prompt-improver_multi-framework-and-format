#!/usr/bin/env python3
"""Prove the collector's edit guard against a synthetic run, before trusting it.

No model is called and nothing leaves the machine. The test builds a small run
folder with one skill export and one Project reply in a temporary directory, then
runs collect_exports.py against it in a subprocess, the way an operator would.

An export in export/benchmark may be edited by hand after collection, and a later
collection must never undo that edit silently. So the test passes only when:

  fresh      a first collection writes both deliverables, and a second one with
             nothing edited writes them again without a warning
  kept       a skill export and a Project export edited by hand are kept, each
             with a warning line, and the collection still exits 0
  dry        a dry run over the edited files prints the same warnings and writes
             nothing
  force      --force restores the run's copy of both
  control    the collector as committed before the guard overwrites the same
             edited file, so this test would fail without the guard

The control runs only while git can show that earlier collector, and says so when
it cannot.

Usage: selftest.py [--keep]
  --keep  leave the temporary directory in place and print where it is

Exit codes:
  0  every check passed
  1  at least one check failed
"""
import os
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
COLLECTOR = os.path.join(HERE, "collect_exports.py")
# The commit whose collector had no edit guard, used as the negative control.
UNGUARDED_REV = "d473b93"

SKILL_NAME = "001 - enhanced-test-prompt.md"
SKILL_BODY = "Mode: $improve | Complexity: 2 | Framework: RCAF\n\n**Role:** Test prompt body.\n"
PROJECT_BLOCK = (
    "Mode: $improve | Complexity: 2 | Framework: RCAF\n\n"
    "**Role:** A copywriter for a test gym, writing the first onboarding email a new member "
    "receives after signing up, so the email must mention the free trial week and the class "
    "schedule and stay under 120 words.\n\n"
    "---\n"
    "Attestation: docs consulted = test | format = Markdown | execution = did not occur\n"
)
PROJECT_REPLY = PROJECT_BLOCK + "\nExport-equivalent path: `export/[NNN] - enhanced-test-email.md`\n"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def collect(collector, run, out, *flags):
    return subprocess.run([sys.executable, "-B", collector, run, out, *flags],
                          capture_output=True, text=True)


def make_run(root):
    run = os.path.join(root, "run")
    write(os.path.join(run, "skill", "STX-001 improve", "exports", SKILL_NAME), SKILL_BODY)
    write(os.path.join(run, "claude project", "PTX-001 improve", "turn-1.md"), PROJECT_REPLY)
    return run


class Checks:
    def __init__(self):
        self.failed = 0

    def check(self, ok, label):
        print(f"{'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            self.failed += 1


def main():
    keep = "--keep" in sys.argv[1:]
    root = tempfile.mkdtemp(prefix="pi-collector-selftest-")
    t = Checks()
    try:
        run = make_run(root)
        out = os.path.join(root, "benchmark")
        skill_target = os.path.join(out, "skill", f"STX-001 - {SKILL_NAME}")
        project_target = os.path.join(out, "claude project", "PTX-001 - NNN - enhanced-test-email.md")

        first = collect(COLLECTOR, run, out)
        again = collect(COLLECTOR, run, out)
        t.check(first.returncode == 0 and read(skill_target) == SKILL_BODY
                and read(project_target) == PROJECT_BLOCK,
                "fresh: a first collection writes the skill export and the Project block")
        t.check(again.returncode == 0 and "warning" not in again.stdout,
                "fresh: an unedited target is written again without a warning")

        write(skill_target, "edited skill export\n")
        write(project_target, "edited project export\n")
        dry = collect(COLLECTOR, run, out, "--dry-run")
        t.check(dry.returncode == 0 and dry.stdout.count("warning") == 2
                and read(skill_target) == "edited skill export\n"
                and read(project_target) == "edited project export\n",
                "dry: a dry run warns on both edited targets and writes nothing")

        kept = collect(COLLECTOR, run, out)
        t.check(kept.returncode == 0 and read(skill_target) == "edited skill export\n"
                and "warning skill STX-001" in kept.stdout,
                "kept: an edited skill export survives the collection with a warning")
        t.check(read(project_target) == "edited project export\n"
                and "warning project PTX-001" in kept.stdout,
                "kept: an edited Project export survives the collection with a warning")

        forced = collect(COLLECTOR, run, out, "--force")
        t.check(forced.returncode == 0 and read(skill_target) == SKILL_BODY
                and read(project_target) == PROJECT_BLOCK and "warning" not in forced.stdout,
                "force: --force restores the run's copy of both targets")

        rel = os.path.relpath(COLLECTOR, subprocess.run(
            ["git", "-C", HERE, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True).stdout.strip())
        old = subprocess.run(["git", "-C", HERE, "show", f"{UNGUARDED_REV}:{rel}"],
                             capture_output=True, text=True)
        if old.returncode != 0 or "def edited(" in old.stdout:
            print(f"SKIP  control: git cannot show the unguarded collector at {UNGUARDED_REV}")
        else:
            unguarded = os.path.join(root, "unguarded_collect_exports.py")
            write(unguarded, old.stdout)
            write(skill_target, "edited skill export\n")
            control = collect(unguarded, run, out)
            t.check(control.returncode == 0 and read(skill_target) == SKILL_BODY,
                    "control: the collector without the guard overwrites the edited export")
    finally:
        if keep:
            print(f"kept {root}")
        else:
            shutil.rmtree(root, ignore_errors=True)
    print(f"selftest: {'all checks passed' if not t.failed else f'{t.failed} check(s) failed'}")
    return 1 if t.failed else 0


if __name__ == "__main__":
    sys.exit(main())
