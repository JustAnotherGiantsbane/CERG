#!/usr/bin/env python3
"""Attach measured scores to audit records, with the revs they were read from.

Every number in a merge report has to name its base. A child's "23.0 -> 23.0"
is true against one branch tip and false against main, and neither reading is
wrong; the tree should make the correction automatic instead of earned.

This reads a batch's JSONL records and, for every rewritten file, computes
score_before at --base and score_after at --head using the same analyser as
cerg-voice-check.py, then writes score_before, score_after, score_base_rev and
score_head_rev back into the record.

    python3 tools/cerg-score-records.py results/batch-1.jsonl --base main --head audit/batch-1
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE / "cerg-voice-check.py"
EXEMPTIONS = HERE / "voice-exemptions.json"


def load_checker():
    spec = importlib.util.spec_from_file_location("cerg_voice_check", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def blob(root: str, rev: str, path: str) -> str:
    return subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                          capture_output=True, text=True).stdout


def score(vc, rules, text: str, name: str) -> float | None:
    d = tempfile.mkdtemp()
    p = os.path.join(d, os.path.basename(name) or "doc.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)
    r = vc.analyse(p, d, rules)
    return r["score"] if r else None


def rev_sha(root: str, rev: str) -> str:
    return subprocess.run(["git", "-C", root, "rev-parse", rev],
                          capture_output=True, text=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records", help="path to batch-N.jsonl")
    ap.add_argument("--root", default=".")
    ap.add_argument("--base", default="main")
    ap.add_argument("--head", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    vc = load_checker()
    rules = vc.load_exemptions(str(EXEMPTIONS))
    base_sha, head_sha = rev_sha(args.root, args.base), rev_sha(args.root, args.head)
    if not base_sha or not head_sha:
        print("cannot resolve --base or --head", file=sys.stderr)
        return 2

    out, changed = [], 0
    for line in open(args.records, encoding="utf-8"):
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("status") == "rewritten":
            before = blob(args.root, args.base, rec["file"])
            after = blob(args.root, args.head, rec["file"])
            sb, sa = score(vc, rules, before, rec["file"]), score(vc, rules, after, rec["file"])
            if sb is not None and sa is not None:
                rec["score_before"], rec["score_after"] = sb, sa
                rec["score_base_rev"] = base_sha[:8]
                rec["score_head_rev"] = head_sha[:8]
                changed += 1
        out.append(json.dumps(rec, ensure_ascii=False))

    if not args.dry_run:
        with open(args.records, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")
    print(f"{changed} records scored at {base_sha[:8]}..{head_sha[:8]}"
          f"{' (dry run)' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
