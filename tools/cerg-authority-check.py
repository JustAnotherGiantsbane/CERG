#!/usr/bin/env python3
"""Authority gate: refuse to merge prose edits to documents CERG does not own.

The voice pass checks content preservation, register, and protected sentences.
None of those ask whether CERG is allowed to rewrite a file at all. Two
documents in the tree belong to the Standing IR Team -- Status "External
Interface", Owner "Standing IR Team / Incident Commander" -- and their own
metadata says CERG reviews them for cross-reference accuracy only.

Run before merging a prose branch:

    python3 tools/cerg-authority-check.py --base main --head audit/batch-2

Exit 1 means the branch edits a document another team owns. The fix is not a
better sentence; it is to drop the commit and route the diff to the owner.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys

NOT_OURS_STATUS = ("external interface",)
NOT_OURS_OWNER = ("standing ir", "incident commander")


def run(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True).stdout


def changed_md(base: str, head: str) -> list[str]:
    out = run("git", "diff", "--name-only", f"{base}..{head}")
    return [f.strip() for f in out.splitlines() if f.strip().endswith(".md")]


def metadata(text: str) -> tuple[str, str]:
    status = re.search(r"\|\s*\*\*Status\*\*\s*\|\s*([^|]+)\|", text)
    owner = re.search(r"\|\s*\*\*Owner\*\*\s*\|\s*([^|]+)\|", text)
    return (
        status.group(1).strip() if status else "",
        owner.group(1).strip() if owner else "",
    )


def resolve(rev: str) -> bool:
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", rev],
                          capture_output=True).returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="main")
    ap.add_argument("--head", required=True)
    ap.add_argument("--rev", default=None, help="read metadata at this rev instead of working tree")
    args = ap.parse_args()

    # A gate that cannot resolve its inputs must not report a pass. Otherwise a
    # mistyped branch, a stale ref, or a CI job in the wrong directory produces
    # a green check about nothing.
    for label, rev in (("base", args.base), ("head", args.head)):
        if not resolve(rev):
            print(f"AUTHORITY GATE ERROR: cannot resolve {label} rev {rev!r} - nothing checked", file=sys.stderr)
            return 2

    paths = changed_md(args.base, args.head)
    if not paths:
        print(f"AUTHORITY GATE ERROR: {args.base}..{args.head} changes no Markdown files - "
              "nothing checked is not a pass", file=sys.stderr)
        return 2

    violations = []
    unreadable = []
    for path in paths:
        at_head = run("git", "show", f"{args.head}:{path}")
        at_base = run("git", "show", f"{args.base}:{path}")
        if not at_head and not at_base:
            # A blob that will not resolve at either end is a finding, not a skip.
            unreadable.append(path)
            continue
        # Ownership is read at both ends: a branch that edits a document and
        # rewrites its Owner row on the way through must still be caught by the
        # owner it had before it touched it.
        for label, text in (("head", at_head), ("base", at_base)):
            if not text:
                continue
            status, owner = metadata(text)
            if any(k in status.lower() for k in NOT_OURS_STATUS) or any(
                k in owner.lower() for k in NOT_OURS_OWNER
            ):
                violations.append((path, label, status, owner))
                break

    if unreadable:
        print(f"AUTHORITY GATE FAILED: {len(unreadable)} changed file(s) could not be read")
        for path in unreadable:
            print(f"  {path}  (no blob at base or head)")
        return 1

    if violations:
        print(f"AUTHORITY GATE FAILED: {len(violations)} changed file(s) belong to another team")
        for path, where, status, owner in violations:
            print(f"  {path}\n    Status: {status} | Owner: {owner}  (matched at {where})")
        print("\nDrop these commits from the merge set and route the diff to the owner.")
        return 1

    print(f"Authority gate passed: {len(paths)} changed Markdown file(s), all CERG-owned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
