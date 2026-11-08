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
import os
import re
import subprocess
import sys

NOT_OURS_STATUS = ("external interface",)
NOT_OURS_OWNER = ("standing ir", "incident commander")

# Repo furniture: nothing it contains can change custody, so a missing nameplate
# is silence rather than a finding. Keep this list short and named - a permanent
# "cannot verify" note on twenty-four files is how a gate's honest hedge becomes
# wallpaper, and a tolerance that outlives its cause is how an alarm dies.
FURNITURE = re.compile(
    r"^(README[^/]*\.md|START-HERE\.md|SECURITY\.md|CONTRIBUTING\.md|"
    r"CODE_OF_CONDUCT\.md|AGENTS\.md|ADOPT-WITH-AGENT\.md|BEGINNER-GUIDE\.md|"
    r"CHANGELOG\.md|LICENSE[^/]*)$|^(examples|tools|\.github)/",
)

# Directories where a document can change hands. A changed file here with no
# Status/Owner row is the undeclared-external-document scenario: nothing matches
# because nothing declares, and a checker must not let that pass.
STRICT_DIRS = ("governance", "standards", "procedures", "plans", "templates", "practice-assets")


def run(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True).stdout


def changed_md(base: str, head: str) -> list[tuple[str, str]]:
    """(source_path, destination_path) for every changed Markdown file.

    Renames are reported with -M so the source path survives. Keying ownership
    on the destination alone lets a branch move a document and rewrite its
    nameplate in the same commit: the base lookup of the new path resolves to
    nothing, and the old, owned path is never consulted.
    """
    out = run("git", "diff", "--name-status", "-M", f"{base}..{head}")
    pairs: list[tuple[str, str]] = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 2 or not parts[0]:
            continue
        status = parts[0][0]
        if status in ("R", "C") and len(parts) >= 3:
            src, dst = parts[1], parts[2]
        else:
            src = dst = parts[1]
        if dst.endswith(".md") or src.endswith(".md"):
            pairs.append((src, dst))
    return pairs


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
    undeclared = 0
    for src, dst in paths:
        # Read every alias of the file: its path now, its path before, and the
        # two crossed combinations, so a rename cannot hide the old nameplate.
        candidates = [("head", dst), ("base", src), ("base", dst), ("head", src)]
        seen: set[tuple[str, str]] = set()
        resolved_once = False
        declared = False
        hit = False
        for where, path in candidates:
            rev = args.head if where == "head" else args.base
            key = (rev, path)
            if key in seen:
                continue
            seen.add(key)
            text = run("git", "show", f"{rev}:{path}")
            if not text:
                continue
            resolved_once = True
            status, owner = metadata(text)
            if status or owner:
                declared = True
            if any(k in status.lower() for k in NOT_OURS_STATUS) or any(
                k in owner.lower() for k in NOT_OURS_OWNER
            ):
                violations.append((f"{src} -> {dst}" if src != dst else dst, f"{where}:{path}", status, owner))
                hit = True
                break
        if not resolved_once:
            unreadable.append(f"{src} -> {dst}")
        elif not declared and not hit:
            p = dst.replace(os.sep, "/")
            top = p.split("/")[0] if "/" in p else ""
            base = p.rsplit("/", 1)[-1]
            is_furniture = bool(FURNITURE.match(base)) or p.startswith(("examples/", "tools/", ".github/"))
            if is_furniture:
                pass  # silence is correct: nothing here can change custody
            elif top in STRICT_DIRS:
                violations.append((f"{src} -> {dst}" if src != dst else dst,
                                   "UNDECLARED", "(no Status/Owner row)", "(document directory)"))
            else:
                undeclared += 1

    if unreadable:
        print(f"AUTHORITY GATE FAILED: {len(unreadable)} changed file(s) could not be read")
        for path in unreadable:
            print(f"  {path}  (no blob at base or head)")
        return 1

    if violations:
        print(f"AUTHORITY GATE FAILED: {len(violations)} changed file(s) cannot be cleared")
        for path, where, status, owner in violations:
            if where == "UNDECLARED":
                print(f"  {path}\n    no Status/Owner row: an undeclared document in "
                      "a directory where custody can change")
            else:
                print(f"  {path}\n    Status: {status} | Owner: {owner}  (matched at {where})")
        print("\nDrop these commits from the merge set and route the diff to the owner, "
              "or declare the document's Status and Owner rows.")
        return 1

    print(f"Authority gate passed: {len(paths)} changed Markdown file(s), all CERG-owned.")
    if undeclared:
        # A file with no nameplate cannot be checked for ownership. Say so,
        # rather than letting silence read as clearance.
        print(f"  note: {undeclared} changed file(s) carry no Status/Owner row; "
              "authority cannot be verified for them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
