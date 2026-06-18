#!/usr/bin/env python3
"""CERG Aggregated Changelog — aggregate revision history from all CERG docs.

Usage:
    python3 tools/cerg-changelog.py                          # All entries, markdown table
    python3 tools/cerg-changelog.py --since YYYY-MM-DD      # Filter by date
    python3 tools/cerg-changelog.py --doc PLN-CIP-001        # Filter by document ID
    python3 tools/cerg-changelog.py --json                   # JSON output
    python3 tools/cerg-changelog.py --since 2026-01-01 --doc CUI-001 --json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "machine-readable", "tools", "policy-as-code", "scripts", "assets"}


@dataclass
class ChangelogEntry:
    """A single revision history entry extracted from a CERG document."""

    doc_id: str
    doc_title: str
    version: str
    date: str
    author: str
    change_type: str | None
    summary: str
    linked_issue: str | None
    raw_line: str  # original table row for debugging


def find_documents(root: Path) -> list[Path]:
    """Find all CERG markdown documents that have revision history tables."""
    docs = []
    for filepath in root.rglob("*.md"):
        rel = filepath.relative_to(root)
        parts = rel.parts
        if any(part in EXCLUDE_DIRS for part in parts):
            continue
        if filepath.name in ("README.md", "CONTRIBUTING.md", "AGENTS.md", "CHANGELOG.md"):
            continue
        if not re.search(r"CERG-[A-Z]+-[A-Z]+-\d{3}", filepath.name):
            continue
        docs.append(filepath)
    return sorted(docs)


def extract_doc_id(filepath: Path) -> str:
    """Extract CERG document ID from filename."""
    m = re.search(r"(CERG-[A-Z]+-[A-Z]+-\d{3})", filepath.name)
    return m.group(1) if m else filepath.stem


def extract_title(text: str) -> str:
    """Extract document subtitle/title from metadata or headings."""
    # Try metadata: | **Document ID** | value |
    # Then look for ## heading after the title block
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("## ") and "Document" not in line and "SURGE" not in line:
            return line.strip().lstrip("#").strip()
    return ""


def parse_revision_history(text: str, filepath: Path) -> list[ChangelogEntry]:
    """Parse revision history table from document text.

    Supports multiple table formats:
    - Standard 6-column: Version | Date | Author | Change Type | Summary | Linked Issue/PR
    - Short 4-column:   Version | Date | Author | Change Summary
    - Legacy 3-column:  Version | Date | Change Summary
    """
    doc_id = extract_doc_id(filepath)
    doc_title = extract_title(text)
    entries: list[ChangelogEntry] = []

    # Find the revision history section
    revision_section = re.search(
        r"### Revision History\s*\n(.*?)(?=\n###|\n##|\Z)",
        text,
        re.DOTALL,
    )
    if not revision_section:
        # Try alternate heading
        revision_section = re.search(
            r"\|\|?\s*\n\|\|?\s*(?:Revision History|Change Log)\s*\n(.*?)(?=\n##|\Z)",
            text,
            re.DOTALL,
        )

    if not revision_section:
        return entries

    section_text = revision_section.group(1)

    # Find table rows — lines starting with |
    for line in section_text.split("\n"):
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue

        cells = [c.strip() for c in line.split("|")]
        # Remove empty leading/trailing cells
        cells = [c for c in cells if c]

        if len(cells) < 3:
            continue

        # Skip header rows
        first_cell = cells[0].lower()
        if first_cell in ("version", "**version**", "---", ""):
            continue

        # Extract version from first cell
        version = cells[0].strip("*").strip()

        # Determine column layout by looking at remaining cells
        if len(cells) >= 6 and "change type" in section_text.lower():
            # 6-column standard format
            date = cells[1].strip("*").strip()
            author = cells[2].strip("*").strip()
            change_type = cells[3].strip("*").strip()
            summary = cells[4].strip("*").strip()
            linked_issue = cells[5].strip("*").strip() if len(cells) > 5 else None
        elif len(cells) >= 4:
            # 4-column: Version | Date | Author | Summary
            date = cells[1].strip("*").strip()
            author = cells[2].strip("*").strip()
            change_type = None
            summary = cells[3].strip("*").strip()
            linked_issue = None
        elif len(cells) >= 3:
            # 3-column: Version | Date | Summary
            date = cells[1].strip("*").strip()
            author = ""
            change_type = None
            summary = cells[2].strip("*").strip()
            linked_issue = None
        else:
            continue

        # Skip rows that don't look like revision entries
        if not re.search(r"\d+\.\d+", version) and version.lower() not in ("draft",):
            continue

        entries.append(ChangelogEntry(
            doc_id=doc_id,
            doc_title=doc_title,
            version=version,
            date=date,
            author=author,
            change_type=change_type,
            summary=summary,
            linked_issue=linked_issue,
            raw_line=line,
        ))

    return entries


def parse_date(entry: ChangelogEntry) -> datetime | None:
    """Try to parse the date field into a datetime object."""
    date_str = entry.date.strip()
    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%d %B %Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def format_markdown(entries: list[ChangelogEntry]) -> str:
    """Format entries as a markdown table."""
    if not entries:
        return "_No revision history entries found._"

    lines = [
        "| **Date** | **Doc ID** | **Version** | **Author** | **Change Type** | **Summary** | **Linked Issue/PR** |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in entries:
        change_type = entry.change_type or "—"
        linked = entry.linked_issue or "—"
        summary = entry.summary.replace("\n", " ").replace("|", "/")
        author = entry.author or "—"
        lines.append(
            f"| {entry.date} | {entry.doc_id} | {entry.version} | {author} | {change_type} | {summary} | {linked} |"
        )
    return "\n".join(lines)


def format_json(entries: list[ChangelogEntry]) -> str:
    """Format entries as JSON."""
    data: list[dict[str, Any]] = []
    for entry in entries:
        data.append({
            "doc_id": entry.doc_id,
            "doc_title": entry.doc_title,
            "version": entry.version,
            "date": entry.date,
            "author": entry.author,
            "change_type": entry.change_type,
            "summary": entry.summary,
            "linked_issue": entry.linked_issue,
        })
    return json.dumps(data, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate revision history from CERG documents")
    parser.add_argument("--since", type=str, help="Filter entries after this date (YYYY-MM-DD)")
    parser.add_argument("--doc", type=str, help="Filter by document ID (e.g., PLN-CIP-001)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    docs = find_documents(REPO_ROOT)

    all_entries: list[ChangelogEntry] = []
    for doc_path in docs:
        try:
            text = doc_path.read_text(encoding="utf-8")
        except Exception:
            continue
        entries = parse_revision_history(text, doc_path)
        all_entries.extend(entries)

    # Apply filters
    if args.doc:
        # Allow short form (e.g., PLN-CIP-001) or full (CERG-PLN-CIP-001)
        filter_doc = args.doc.upper()
        if not filter_doc.startswith("CERG-"):
            filter_doc = f"CERG-{filter_doc}"
        all_entries = [e for e in all_entries if e.doc_id == filter_doc]

    if args.since:
        try:
            since_date = datetime.strptime(args.since, "%Y-%m-%d")
            all_entries = [
                e
                for e in all_entries
                if (parsed := parse_date(e)) is not None and parsed >= since_date
            ]
        except ValueError:
            print(f"⚠  Invalid --since date format. Use YYYY-MM-DD.", file=sys.stderr)
            return 1

    # Sort by date descending, then by doc ID
    def sort_key(entry: ChangelogEntry) -> str:
        dt = parse_date(entry)
        if dt:
            return f"{dt.strftime('%Y-%m-%d')}|{entry.doc_id}|{entry.version}"
        return f"0000-00-00|{entry.doc_id}|{entry.version}"

    all_entries.sort(key=sort_key, reverse=True)

    # Output
    if args.json:
        print(format_json(all_entries))
    else:
        print(f"# CERG Aggregated Changelog\n")
        print(f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_\n")
        if args.doc:
            print(f"_Filtered by document: {args.doc}_\n")
        if args.since:
            print(f"_Filtered since: {args.since}_\n")
        print(f"**{len(all_entries)} entries found**\n")
        print(format_markdown(all_entries))

    return 0


if __name__ == "__main__":
    sys.exit(main())
