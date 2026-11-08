#!/usr/bin/env python3
"""Run the test suite with or without pytest.

`pytest tests/` is the authority CI runs, but pytest is not installed in every
profile that holds this repo, and `unittest discover` collects nothing because
the tests are plain pytest-style functions. A suite that only one machine can
run makes "tests pass" a property of whoever typed last.

This shim imports each tests/test_*.py module and calls every zero-argument
`test_*` function, so the same command works anywhere with a stdlib Python:

    python3 tools/run-tests.py

It prints, for every failure, the test module, the function name and the
assertion message, and exits non-zero if anything fails. Report the runner in
any pass claim: "10 passed under tools/run-tests.py" is reproducible, "tests
pass" is an anecdote.
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    if not TESTS.is_dir():
        print(f"no tests directory at {TESTS}", file=sys.stderr)
        return 2

    passed, failed, needs_pytest = 0, [], []
    for path in sorted(TESTS.glob("test_*.py")):
        try:
            mod = load(path)
        except Exception:
            failed.append((path.name, "<import>", traceback.format_exc(limit=2)))
            continue
        for name in sorted(dir(mod)):
            if not name.startswith("test_"):
                continue
            fn = getattr(mod, name)
            if not callable(fn) or getattr(fn, "__code__", None) is None:
                continue
            if fn.__code__.co_argcount:
                needs_pytest.append(f"{path.name}::{name}")
                continue  # fixtures are pytest's business; CI runs pytest
            try:
                fn()
                passed += 1
            except Exception as exc:
                failed.append((path.name, name, f"{type(exc).__name__}: {exc}"))

    for mod_name, fn_name, msg in failed:
        print(f"FAIL {mod_name}::{fn_name}\n     {msg}")
    for fq in needs_pytest:
        print(f"SKIP {fq} (requires pytest fixtures)")
    total = passed + len(failed) + len(needs_pytest)
    print(f"\n{passed} passed, {len(failed)} failed, {len(needs_pytest)} need pytest, "
          f"{total} collected under tools/run-tests.py")
    if needs_pytest:
        print("Partial run: those tests are verified only under `pytest tests/`. "
              "State which runner a pass claim came from.")
    return 0 if failed else 1


if __name__ == "__main__":
    sys.exit(main())
