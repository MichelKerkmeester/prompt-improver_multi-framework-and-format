#!/usr/bin/env python3
"""Extract python fences from a SKILL.md and run them against fixture requests.

Usage: extract_and_run.py <skill_md_path> <skill_root_for_execution> <fixtures.json> <output.json>
"""
import json
import re
import sys
from pathlib import Path

def extract_python_fences(skill_md_text: str) -> str:
    fences = re.findall(r"```python\n(.*?)```", skill_md_text, flags=re.DOTALL)
    if not fences:
        raise SystemExit("No python fences found in SKILL.md")
    return "\n\n".join(fences)

def build_namespace(fake_skill_md_path: Path):
    loaded_calls = []
    shown_messages = []

    def load(relative_path):
        loaded_calls.append(relative_path)

    def show_user(message):
        shown_messages.append(message)

    namespace = {
        "__name__": "prompt_improver_router_harness",
        "__file__": str(fake_skill_md_path),
        "load": load,
        "show_user": show_user,
    }
    return namespace, loaded_calls, shown_messages

def main():
    skill_md_path = Path(sys.argv[1]).resolve()
    skill_root_for_execution = Path(sys.argv[2]).resolve()
    fixtures_path = Path(sys.argv[3]).resolve()
    output_path = Path(sys.argv[4]).resolve()

    skill_md_text = skill_md_path.read_text()
    code = extract_python_fences(skill_md_text)

    # Fake __file__ so SKILL_ROOT = Path(__file__).resolve().parent resolves
    # to the real skill folder (with real references/ and assets/), regardless
    # of where the actual SKILL.md text was read from.
    fake_skill_md_path = skill_root_for_execution / "SKILL.md"

    namespace, loaded_calls, shown_messages = build_namespace(fake_skill_md_path)
    exec(compile(code, str(skill_md_path), "exec"), namespace)

    route_fn_name = "route_prompt_improver_resources"
    if route_fn_name not in namespace:
        raise SystemExit(f"Router entry point {route_fn_name} not found in extracted code")
    route_fn = namespace[route_fn_name]

    fixtures = json.loads(fixtures_path.read_text())
    results = []
    for fixture in fixtures:
        loaded_calls.clear()
        shown_messages.clear()
        request_text = fixture["request"]
        try:
            outcome = route_fn(request_text)
        except Exception as exc:  # noqa: BLE001
            outcome = {"error": f"{type(exc).__name__}: {exc}"}
        results.append({
            "id": fixture["id"],
            "request": request_text,
            "outcome": outcome,
            "show_user_calls": list(shown_messages),
        })

    output_path.write_text(json.dumps(results, indent=2, default=str))
    print(f"Ran {len(results)} fixtures -> {output_path}")

if __name__ == "__main__":
    main()
