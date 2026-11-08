#!/usr/bin/env python3
"""Read-aloud voice check for CERG prose.

Scores the things a person hears when reading quietly: filler, nominalization,
passive constructions, and breaths that run long between punctuation. Tables,
code fences, headings, document IDs and link-dense list items are excluded, as
are sentences protected by tools/voice-exemptions.json.

The checker triages. It ranks documents for a human pass; it does not judge them.
An earlier version scored rhythm variability and ranked the repo's cleanest file
worst, which is how we learned not to automate taste.

Exemptions are data, not logic. Every exemption example is verified against the
corpus: if a protected sentence has disappeared, the run fails, because deleting
a protected sentence is a dropped rule rather than a cleanup.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import statistics
import sys

EXEMPTIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voice-exemptions.json")

FILLER = [
    "it is worth noting", "it should be noted", "in order to", "the fact that",
    "serves to", "as such", "thereby", "leverage", "utilize", "utilizing",
    "operationalize", "operationalizes", "operationalizing", "facilitate",
    "facilitates", "robust", "holistic", "seamless", "best-in-class",
    "moving forward", "at the end of the day", "in terms of", "with respect to",
    "ensures that", "provides the ability to", "in the event that",
    "for the purpose of", "a number of", "in light of", "subsequent to",
    "with regard to", "it is important to", "this ensures", "this allows",
    "this enables", "on an ongoing basis", "at this point in time",
    "due to the fact that", "is designed to", "is intended to",
    "can be used to", "has the ability to",
]
NOMINAL = re.compile(r"\b\w{4,}(tion|tions|ment|ments|ance|ances|ence|ences|ity|ities|ness)\b", re.I)
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ed|shown|made|given|taken|held|kept|seen|done|written|built|set)\b", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def load_exemptions(path: str) -> list[dict]:
    return json.load(open(path, encoding="utf-8"))["rules"]


def verify_exemptions(rules: list[dict], root: str) -> list[str]:
    """Every pinned sentence must still be in the corpus."""
    problems = []
    for rule in rules:
        for ex in rule.get("examples", []):
            f = os.path.join(root, ex["file"])
            if not os.path.exists(f):
                problems.append(f"{rule['id']}: file missing - {ex['file']}")
                continue
            if norm(ex["sentence"]) not in norm(open(f, encoding="utf-8", errors="ignore").read()):
                problems.append(f"{rule['id']}: PROTECTED SENTENCE GONE - {ex['file']}: {ex['sentence'][:70]}")
    return problems


def protects(rule: dict, sentence: str, path: str, prev: str | None, nxt: str | None) -> bool:
    m = rule["match"]
    t = m["type"]
    if t == "regex":
        return re.search(m["pattern"], sentence) is not None
    if t == "short-final":
        return len(sentence.split()) <= m["max_words"] and nxt is None
    if t == "term-list":
        return any(term.lower() in sentence.lower() for term in m["terms"])
    if t == "path-bullets":
        return path.replace(os.sep, "/").startswith(m["path_glob"].rstrip("/"))
    if t == "anaphora":
        if prev is None:
            return False
        a, b = sentence.split()[:2], prev.split()[:2]
        return a == b
    return False


def read_prose(path: str) -> list[str]:
    out, fence = [], False
    for line in open(path, encoding="utf-8", errors="ignore"):
        s = line.strip()
        if s.startswith("```"):
            fence = not fence
            continue
        if fence or not s or s.startswith(("|", "#", "---")):
            continue
        if len(re.findall(r"\]\(", s)) >= 2:
            continue
        out.append(s)
    return out


def analyse(path: str, root: str, rules: list[dict]) -> dict:
    rel = os.path.relpath(path, root)
    lines = read_prose(path)
    kept, exempted = [], 0
    for i, line in enumerate(lines):
        for s in re.split(r"(?<=[.!?])\s+", line):
            s = s.strip()
            if len(s.split()) < 3:
                continue
            prev = lines[i - 1].split(".")[-1].strip() if i else None
            nxt = lines[i + 1] if i + 1 < len(lines) else None
            if any(protects(r, s, rel, prev, nxt) for r in rules):
                exempted += 1
                continue
            kept.append(s)
    if len(kept) < 12:
        return {}
    body = " ".join(kept)
    words = re.findall(r"[A-Za-z']+", body)
    n = max(len(words), 1)
    low = body.lower()
    fill = sum(low.count(f) for f in FILLER)
    nom = len(NOMINAL.findall(body))
    pas = len(PASSIVE.findall(body))
    breaths = [len(c.split()) for s in kept for c in re.split(r"[,;:—–]", s) if c.split()]
    long_breath = sum(1 for b in breaths if b > 18) / max(len(breaths), 1)
    score = (fill / n * 10000 + nom / n * 60 + pas / n * 50 + long_breath * 70)
    lens = [len(s.split()) for s in kept]
    return {
        "path": rel, "words": len(words), "sentences": len(kept),
        "exempted": exempted, "mean": round(statistics.mean(lens), 1),
        "filler_per_1k": round(fill / n * 1000, 1),
        "nominal_pct": round(nom / n * 100, 1),
        "passive_per_1k": round(pas / n * 1000, 1),
        "long_breath_pct": round(long_breath * 100, 1),
        "score": round(score, 1),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--exemptions", default=EXEMPTIONS)
    args = ap.parse_args()

    rules = load_exemptions(args.exemptions)
    problems = verify_exemptions(rules, args.root)
    if problems:
        print("Exemption check FAILED:")
        for p in problems:
            print("  " + p)
        return 1

    files = [p for p in glob.glob(os.path.join(args.root, "**", "*.md"), recursive=True)
             if ".git" not in p and "node_modules" not in p]
    rows = [r for r in (analyse(p, args.root, rules) for p in files) if r]
    rows.sort(key=lambda r: -r["score"])
    if args.json:
        print(json.dumps({"rules": len(rules), "files": rows}, indent=1))
        return 0

    print(f"{len(rules)} exemption rules verified; {len(rows)} files scored, "
          f"{sum(r['words'] for r in rows)} prose words\n")
    print(f"{'score':>6} {'words':>6} {'mean':>5} {'fill':>5} {'nom%':>5} {'pas':>5} {'brth%':>6} {'exmpt':>5}  file")
    for r in rows[: args.limit]:
        print(f"{r['score']:6.1f} {r['words']:6d} {r['mean']:5.1f} {r['filler_per_1k']:5.1f} "
              f"{r['nominal_pct']:5.1f} {r['passive_per_1k']:5.1f} {r['long_breath_pct']:6.1f} "
              f"{r['exempted']:5d}  {r['path']}")
    q = statistics.quantiles([r["score"] for r in rows], n=4)
    print(f"\nquartiles: {q[0]:.1f} / {q[1]:.1f} / {q[2]:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
