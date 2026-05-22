#!/usr/bin/env python3
"""
cerg-render.py - CERG corpus render tool.

Reads cerg-org-profile.yml, substitutes {{TOKEN}} placeholders and known
hard-coded phrases across the CERG Markdown corpus, and writes an
organization-specific copy to an output directory. The source corpus is
never modified.

Token scheme, token catalog, and the phrase map are defined in
CERG-GOV-VAR-001 (Organization Adaptation Profile).

Standard library only. Runs anywhere Python 3.8+ runs.

Usage:
    python3 tools/cerg-render.py
    python3 tools/cerg-render.py --profile cerg-org-profile.yml --source . --out rendered
    python3 tools/cerg-render.py --check        # validate only, no output written
"""

import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Token catalog: maps catalog token name -> (yaml section, yaml key).
# Mirrors CERG-GOV-VAR-001 Section 4. New tokens require a catalog amendment
# in CERG-GOV-VAR-001 AND an entry here.
# ---------------------------------------------------------------------------
TOKEN_CATALOG = {
    "ORG_NAME":             ("organization", "org_name"),
    "ORG_LEGAL_NAME":       ("organization", "org_legal_name"),
    "ORG_SHORT_NAME":       ("organization", "org_short_name"),
    "ORG_SECTOR":           ("organization", "org_sector"),
    "ORG_CONTENT_REPO":     ("organization", "org_content_repo"),
    "PROGRAM_NAME":         ("program", "program_name"),
    "PROGRAM_ACRONYM":      ("program", "program_acronym"),
    "TOTAL_EMPLOYEES":      ("scale", "total_employees"),
    "PROTECTED_POPULATION": ("scale", "protected_population"),
    "CERG_TEAM_SIZE":       ("scale", "cerg_team_size"),
    "ENG_STAFF":            ("scale", "eng_staff"),
    "RISK_STAFF":           ("scale", "risk_staff"),
    "GOV_STAFF":            ("scale", "gov_staff"),
    "SCALE_TIER":           ("scale", "scale_tier"),
    "COG_NAME":             ("oversight", "cog_name"),
    "IR_TEAM_NAME":         ("oversight", "ir_team_name"),
    "EXEC_BODY_NAME":       ("oversight", "exec_body_name"),
    "REGULATORS":           ("regulatory", "regulators"),
    "PRIMARY_REGULATOR":    ("regulatory", "primary_regulator"),
    "SECURITY_CONTACT":     ("contact", "security_contact"),
    "DOC_CONTROL_CONTACT":  ("contact", "doc_control_contact"),
    "ADOPTION_DATE":        ("contact", "adoption_date"),
}

# ---------------------------------------------------------------------------
# Phrase map: exact hard-coded V1 phrases -> token-bearing replacement.
# Bridges the un-tokenized V1 corpus. Entries are retired as the corpus is
# tokenized in place. See CERG-GOV-VAR-001 Section 7.
# ---------------------------------------------------------------------------
PHRASE_MAP = {
    "14,000 employees, 60-person security team":
        "{{TOTAL_EMPLOYEES}} employees, {{CERG_TEAM_SIZE}}-person security team",
    "14,000 employees, an equal population of consultants and contractors, and a 60-person CERG team":
        "{{TOTAL_EMPLOYEES}} employees, an equal population of consultants and contractors, "
        "and a {{CERG_TEAM_SIZE}}-person {{PROGRAM_NAME}} team",
    "60-person CERG across approximately 14 Engineering staff, 15 Risk staff, and 13 Governance staff":
        "{{CERG_TEAM_SIZE}}-person {{PROGRAM_NAME}} across approximately {{ENG_STAFF}} Engineering "
        "staff, {{RISK_STAFF}} Risk staff, and {{GOV_STAFF}} Governance staff",
    "60-person team reporting to the CISO":
        "{{CERG_TEAM_SIZE}}-person team reporting to the CISO",
}

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

# Meta-placeholders: abstract syntax examples used in the prose of
# CERG-GOV-VAR-001 itself (e.g. "a token has the form {{TOKEN_NAME}}").
# They are documentation, not real tokens. Left verbatim, never reported.
RENDER_IGNORE = {"TOKEN", "TOKEN_NAME"}

# Files and directories the render tool never touches.
SKIP_DIRS = {".git", "rendered", "tools", "node_modules"}
SKIP_FILES = {"cerg-org-profile.yml"}

# Files copied to the output verbatim, with NO token substitution. These
# documents teach the token scheme and contain literal {{TOKEN}} examples
# in their prose; substituting them would corrupt the documentation.
NO_RENDER_FILES = {"CERG-GOV-VAR-001_Organization_Adaptation_Profile.md"}


def parse_profile(path):
    """Minimal YAML reader for the flat two-level cerg-org-profile.yml.

    Supports: top-level section keys, two-space-indented key: value pairs,
    optionally double-quoted values, and # comments (full-line and inline,
    including inline comments after a quoted value). No lists, no nesting
    beyond two levels - which is all the profile schema uses.
    """
    if not os.path.isfile(path):
        sys.exit("ERROR: profile not found: %s" % path)
    values = {}
    section = None
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            indent = len(line) - len(line.lstrip())
            if indent == 0:
                # section header: "name:"
                section = stripped.rstrip(":").strip()
                values.setdefault(section, {})
                continue
            if ":" not in stripped:
                continue
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith('"'):
                # quoted value: take text up to the closing quote;
                # anything after it (e.g. an inline # comment) is discarded
                end = val.find('"', 1)
                val = val[1:end] if end != -1 else val[1:]
            elif "#" in val:
                # unquoted value with an inline comment
                val = val.split("#", 1)[0].rstrip()
            values.setdefault(section or "", {})[key] = val
    return values


def build_token_values(profile):
    """Resolve catalog token names to their string values from the profile."""
    resolved = {}
    missing = []
    for token, (sec, key) in TOKEN_CATALOG.items():
        sec_map = profile.get(sec, {})
        if key in sec_map and sec_map[key] != "":
            resolved[token] = sec_map[key]
        else:
            missing.append(token)
    return resolved, missing


def collect_markdown(source):
    """Yield every .md file path under source, skipping SKIP_DIRS/SKIP_FILES."""
    for root, dirs, files in os.walk(source):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".md") and name not in SKIP_FILES:
                yield os.path.join(root, name)


def render_text(text, token_values):
    """Apply the phrase map, then substitute tokens. Return (text, unknown,
    unresolved) where unknown = tokens not in the catalog, unresolved =
    catalog tokens with no profile value."""
    for phrase, replacement in PHRASE_MAP.items():
        text = text.replace(phrase, replacement)

    unknown = set()
    unresolved = set()

    def repl(match):
        name = match.group(1)
        if name in RENDER_IGNORE:
            return match.group(0)
        if name not in TOKEN_CATALOG:
            unknown.add(name)
            return match.group(0)
        if name not in token_values:
            unresolved.add(name)
            return match.group(0)
        return token_values[name]

    return TOKEN_RE.sub(repl, text), unknown, unresolved


def main():
    ap = argparse.ArgumentParser(description="Render the CERG corpus for an organization.")
    ap.add_argument("--profile", default="cerg-org-profile.yml",
                    help="Path to the organization profile (default: cerg-org-profile.yml)")
    ap.add_argument("--source", default=".",
                    help="Corpus source directory (default: current directory)")
    ap.add_argument("--out", default="rendered",
                    help="Output directory for the rendered corpus (default: rendered)")
    ap.add_argument("--check", action="store_true",
                    help="Validate only: report token problems, write nothing, exit non-zero on error")
    args = ap.parse_args()

    profile = parse_profile(args.profile)
    token_values, missing_profile = build_token_values(profile)

    all_unknown = set()
    all_unresolved = set()
    files = list(collect_markdown(args.source))

    if not files:
        sys.exit("ERROR: no Markdown files found under %s" % args.source)

    rendered_files = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        if os.path.basename(path) in NO_RENDER_FILES:
            # Copy verbatim: this file teaches the token scheme and
            # contains literal {{TOKEN}} examples that must not change.
            out_text = text
        else:
            out_text, unknown, unresolved = render_text(text, token_values)
            all_unknown |= unknown
            all_unresolved |= unresolved

        if not args.check:
            rel = os.path.relpath(path, args.source)
            dest = os.path.join(args.out, rel)
            os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(out_text)
            rendered_files += 1

    # Report
    print("CERG render: %d Markdown file(s) processed." % len(files))
    if all_unknown:
        print("\nUNKNOWN TOKENS (not in the CERG-GOV-VAR-001 catalog):")
        for t in sorted(all_unknown):
            print("  {{%s}}" % t)
    if all_unresolved:
        print("\nUNRESOLVED TOKENS (catalog token with no value in the profile):")
        for t in sorted(all_unresolved):
            print("  {{%s}}" % t)

    error = bool(all_unknown or all_unresolved)

    if args.check:
        if error:
            print("\nCHECK FAILED. Resolve the tokens above.")
            sys.exit(1)
        print("\nCHECK PASSED. Every token resolves.")
        sys.exit(0)

    print("\nRendered %d file(s) into ./%s" % (rendered_files, args.out))
    if error:
        print("WARNING: rendered output contains unresolved or unknown tokens (left verbatim).")
        sys.exit(1)
    print("Done.")
    sys.exit(0)


if __name__ == "__main__":
    main()
