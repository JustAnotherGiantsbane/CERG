#!/usr/bin/env python3
"""CERG Catalog Sync Tool — sync file frontmatter Status to CAT-001 §5.

Usage:
    python3 tools/cerg-catalog-sync.py --dry-run    # Show diff without writing (default)
    python3 tools/cerg-catalog-sync.py --write       # Update CAT-001 in-place
    python3 tools/cerg-catalog-sync.py --ci          # Exit 1 if drift detected
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


# ── configuration ───────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"
EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "machine-readable", "tools", "policy-as-code", "scripts", "assets"}

# Valid CERG statuses (per STY-001 §X conventions)
VALID_STATUSES = {"Approved", "Draft", "For Review", "Retired", "Planned", "External Interface"}

# Prefix → type mapping (same as FRM-002 appendix / CAT-001 §5)
PREFIX_TYPE_MAP = {
    "POL": "Policy",
    "STD": "Standard",
    "PRC": "Procedure",
    "PLN": "Plan",
    "TMPL": "Template",
    "JF": "Job Family",
    "JD": "Job Description",
    "GOV": "Framework Instrument",
    "GL": "Guideline",
}

# ── data model ──────────────────────────────────────────────────────────────

@dataclass
class FileStatus:
    doc_id: str
    status: str
    file_path: str
    metadata_status: str | None = None


# ── file scanning ───────────────────────────────────────────────────────────

def find_documents(root: Path) -> list[Path]:
    """Find all CERG markdown documents that should be in the catalog."""
    docs = []
    for filepath in root.rglob("*.md"):
        rel = filepath.relative_to(root)
        parts = rel.parts
        # Skip excluded dirs
        if any(part in EXCLUDE_DIRS for part in parts):
            continue
        # Skip non-CERG files (README, CONTRIBUTING, AGENTS, CHANGELOG, etc.)
        if filepath.name in ("README.md", "CONTRIBUTING.md", "AGENTS.md", "CHANGELOG.md"):
            continue
        # Must have a CERG document ID in the filename (CERG-XXX-XXX-NNN)
        if not re.search(r"CERG-[A-Z]+-[A-Z]+-\d{3}", filepath.name):
            continue
        docs.append(filepath)
    return sorted(docs)


def extract_metadata_status(filepath: Path) -> str | None:
    """Extract Status from metadata table at the top of a CERG doc.

    The metadata table uses the 11-field format from STY-001 §4:
    | **Status** | Approved |
    """
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    # Look for | **Status** | VALUE |
    m = re.search(r"\|\s*\*\*Status\*\*\s*\|\s*(\S[^|]*?)\s*\|", text)
    if m:
        return m.group(1).strip()
    return None


def extract_doc_id(filepath: Path) -> str | None:
    """Extract CERG document identifier from filename (e.g., CERG-POL-001)."""
    m = re.search(r"(CERG-[A-Z]+-[A-Z]+-\d{3})", filepath.name)
    return m.group(1) if m else None


def detect_prefix(doc_id: str) -> str:
    """Extract the prefix from a CERG document ID."""
    m = re.match(r"CERG-([A-Z]+)-", doc_id)
    return m.group(1) if m else ""


def get_doc_type(doc_id: str) -> str:
    """Map a document ID to its catalog type heading."""
    prefix = detect_prefix(doc_id)
    return PREFIX_TYPE_MAP.get(prefix, "Other")


def compute_link(root: Path, doc_path: Path) -> str:
    """Compute relative link from catalog directory to the document."""
    try:
        return os.path.relpath(doc_path, CATALOG_PATH.parent).replace("\\", "/")
    except ValueError:
        return doc_path.name


# ── catalog parsing ─────────────────────────────────────────────────────────

def find_catalog_table(text: str) -> tuple[str, int, int]:
    """Find the §5 catalog table boundaries and the section header.

    Returns (section_text, start_pos, end_pos) or raises ValueError.
    """
    section_start = re.search(r"^## 5\. ", text, flags=re.MULTILINE)
    if not section_start:
        raise ValueError("Cannot find §5 catalog section header in CAT-001")

    remaining = text[section_start.end():]
    next_section = re.search(r"\n## \d+\. ", remaining, flags=re.MULTILINE)
    if not next_section:
        raise ValueError("Cannot find end boundary of §5 catalog section")

    section_end = section_start.end() + next_section.start()
    section_text = text[section_start.start():section_end]
    return section_text, section_start.start(), section_end


def parse_catalog_rows(text: str) -> dict[str, tuple[str, str, str, str]]:
    """Parse the catalog §5 table rows into a dict of doc_id → (link, owner, status, raw_line).

    Returns dict keyed by doc_id.
    """
    entries: dict[str, tuple[str, str, str, str]] = {}

    # Find all table rows (| ... | ... | ... | ... | ... |)
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # Filter out separator rows and header rows
        cells = [c for c in cells if c and c not in ("", "---")]
        # Table should have at least 5 content cells (id, doc name, type, owner, status)
        if len(cells) < 5:
            continue

        doc_id_col = cells[0]
        link_col = cells[1] if len(cells) > 1 else ""
        type_col = cells[2] if len(cells) > 2 else ""
        owner_col = cells[3] if len(cells) > 3 else ""
        status_col = cells[4] if len(cells) > 4 else ""

        # Extract doc_id from the link column or the first cell
        doc_id = extract_doc_id(doc_id_col) or extract_doc_id(link_col) or doc_id_col.strip()

        # Skip rows that don't look like CERG document entries
        if not doc_id.startswith("CERG-"):
            continue

        entries[doc_id] = (link_col, type_col, owner_col, status_col)

    return entries


# ── catalog update ──────────────────────────────────────────────────────────

def build_updated_catalog(text: str, file_statuses: dict[str, FileStatus]) -> str:
    """Rebuild the §5 section of CAT-001 from file statuses.

    Preserves everything outside §5, the section header, and the intra-section
    prose. Only the actual table rows are regenerated.
    """
    try:
        section_text, section_start, section_end = find_catalog_table(text)
    except ValueError as e:
        print(f"⚠  {e}", file=sys.stderr)
        return text

    # Parse current catalog entries for owner info we want to preserve
    catalog_entries = parse_catalog_rows(section_text)

    # Build output: everything before §5 + updated §5 + everything after §5
    prefix = text[:section_start]
    suffix = text[section_end:]

    # Split section into header/intro/body
    header_end = section_text.find("\n")
    header_line = section_text[:header_end].strip() if header_end > 0 else section_text.strip()

    # Find where type headers start (### 5.x)
    body_start_m = re.search(r"\n### 5\.\d", section_text)
    if body_start_m:
        intro_text = section_text[header_end:body_start_m.start()]
    else:
        intro_text = section_text[header_end:]

    # Group files by type
    type_groups: dict[str, list[tuple[str, str, str, str]]] = {}
    # type → order (preserve type heading order from original)
    type_order: list[str] = []

    # First, determine type order from existing catalog
    for _, link_col, type_col, _ in catalog_entries.values():
        if type_col and type_col not in type_order:
            type_order.append(type_col)

    # Collect files from actual docs
    for doc_id, fs in sorted(file_statuses.items()):
        doc_type = get_doc_type(doc_id)
        link = compute_link(REPO_ROOT, Path(REPO_ROOT / fs.file_path))
        owner = ""
        if doc_id in catalog_entries:
            owner = catalog_entries[doc_id][2]  # preserve owner from catalog
        status = fs.metadata_status or fs.status

        if doc_type not in type_groups:
            type_groups[doc_type] = []
        type_groups[doc_type].append((doc_id, link, owner, status))

    # Add any catalog-only types (present in catalog but no files found)
    for doc_id, (link_col, type_col, owner_col, status_col) in catalog_entries.items():
        if doc_id not in file_statuses and type_col:
            if type_col not in type_groups:
                type_groups[type_col] = []
                if type_col not in type_order:
                    type_order.append(type_col)
            # Check if already added
            existing_ids = [e[0] for e in type_groups[type_col]]
            if doc_id not in existing_ids:
                type_groups[type_col].append((doc_id, link_col, owner_col, status_col))

    # Build table body
    new_body_lines = []
    for type_name in type_order:
        if type_name not in type_groups:
            continue
        entries = sorted(type_groups[type_name], key=lambda x: x[0])

        # Build type header
        type_num = type_order.index(type_name) + 1
        new_body_lines.append(f"### 5.{type_num} {type_name}")
        new_body_lines.append("")
        new_body_lines.append("| Document ID | Document | Type | Owner | Status |")
        new_body_lines.append("|---|---|---|---|---|")
        for doc_id, link, owner, status in entries:
            # Create markdown link if we have a path
            if link and link != doc_id:
                link_text = doc_id
            else:
                link_text = doc_id
            new_body_lines.append(f"| {link_text} | {doc_id} | {type_name} | {owner} | {status} |")
        new_body_lines.append("")

    new_body = "\n".join(new_body_lines)

    # Rebuild section
    new_section = f"{header_line}\n{intro_text}\n{new_body}"

    return prefix + new_section + suffix


# ── main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sync file frontmatter Status to CAT-001 §5")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Show diff without writing (default)")
    parser.add_argument("--write", action="store_true",
                        help="Update CAT-001 in-place")
    parser.add_argument("--ci", action="store_true",
                        help="Exit 1 if drift detected")
    args = parser.parse_args()

    if args.write:
        args.dry_run = False

    # Scan all documents
    docs = find_documents(REPO_ROOT)
    print(f"Found {len(docs)} CERG documents", file=sys.stderr)

    # Collect statuses
    file_statuses: dict[str, FileStatus] = {}
    for doc_path in docs:
        doc_id = extract_doc_id(doc_path)
        if not doc_id:
            continue
        rel_path = str(doc_path.relative_to(REPO_ROOT))
        meta_status = extract_metadata_status(doc_path)
        fs = FileStatus(
            doc_id=doc_id,
            status=meta_status or "Unknown",
            file_path=rel_path,
            metadata_status=meta_status,
        )
        file_statuses[doc_id] = fs

    # Read current CAT-001
    catalog_text = CATALOG_PATH.read_text(encoding="utf-8")

    # Build updated catalog
    new_text = build_updated_catalog(catalog_text, file_statuses)

    if new_text == catalog_text:
        print("✅ Catalog is up to date — no changes needed.")
        return 0

    # Show diff
    import difflib
    diff = list(difflib.unified_diff(
        catalog_text.splitlines(keepends=True),
        new_text.splitlines(keepends=True),
        fromfile=str(CATALOG_PATH),
        tofile=str(CATALOG_PATH) + " (updated)",
    ))
    print("".join(diff[-200:]))  # Show last 200 lines of diff

    if args.dry_run:
        print(f"\n⚠  Catalog drift detected — {len(diff)} lines changed. Run with --write to update.")
        if args.ci:
            return 1
        return 0

    # Write
    CATALOG_PATH.write_text(new_text, encoding="utf-8")
    print(f"✅ Updated {CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
