#!/usr/bin/env python3
"""Regenerate core CERG machine-readable manifests from local Markdown source.

Outputs:
  - machine-readable/cerg-manifest.yaml
  - machine-readable/cerg-publication-manifest.yaml

The Markdown corpus is authoritative. This script intentionally derives paths,
versions, statuses, classifications, owners, hashes, and publication flags from
repo-local files so agents do not consume stale directoryless paths.
"""

from __future__ import annotations

import hashlib
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MR = ROOT / "machine-readable"
GITHUB_BASE = "https://github.com/m0dernz/CERG/blob/main"

INCLUDE_DIRS = {"governance", "standards", "procedures", "plans", "templates", "roles"}
DOC_ID_RE = re.compile(r"CERG-(?:POL-\d{3}|(?:STD|PRC|PLN|GL|TMPL|GOV)-[A-Z]{2,8}(?:-[A-Z]{2,8})?-\d{3})")
META_ROW_RE = re.compile(r"^\|\s*\*\*(?P<key>[^*]+)\*\*\s*\|\s*(?P<value>.*?)\s*\|\s*$")
HEADING_RE = re.compile(r"^#{1,3}\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)|`([^`]+)`|<[^>]+>")

TYPE_LABELS = {
    "POL": "policy",
    "GOV": "governance_instrument",
    "STD": "standard",
    "PRC": "procedure",
    "PLN": "plan",
    "TMPL": "template",
}


def clean_value(value: str) -> str:
    value = value.strip()
    value = LINK_RE.sub(lambda m: m.group(1) or m.group(2) or "", value)
    value = value.replace("`", "")
    value = value.replace(" - ", " — ")
    return " ".join(value.split())


def yaml_scalar(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    value = str(value)
    if value == "":
        return "''"
    if re.fullmatch(r"[A-Za-z0-9_./:@+\- ]+", value) and not value.startswith(("-", "?", "@")):
        return value
    return "'" + value.replace("'", "''") + "'"


def parse_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    lines = text[:6000].splitlines()
    for idx, line in enumerate(lines):
        if line.strip() != "| | |":
            continue
        for row in lines[idx + 1 :]:
            if not row.startswith("|"):
                if metadata:
                    return metadata
                continue
            if row.strip() == "|---|---|":
                continue
            m = META_ROW_RE.match(row)
            if m:
                key = m.group("key").strip()
                value = clean_value(m.group("value"))
                metadata[key] = value
            elif metadata:
                return metadata
        break
    return metadata


def title_from_path(path: Path, doc_id: str) -> str:
    stem = path.stem
    if stem.startswith(doc_id + "_"):
        stem = stem[len(doc_id) + 1 :]
    return stem.replace("_", " ").strip() or doc_id


def title_from_text(text: str, fallback: str) -> str:
    for m in HEADING_RE.finditer(text[:3000]):
        title = m.group(1).strip()
        if title and not title.startswith("SURGE:"):
            return title
    return fallback


def domain_from_id(doc_id: str) -> str:
    parts = doc_id.split("-")
    if parts[1] == "POL":
        return "POL"
    if len(parts) >= 5 and parts[2] == "JD":
        return f"{parts[2]}-{parts[3]}"
    return parts[2]


def type_from_id(doc_id: str) -> str:
    typ = doc_id.split("-")[1]
    if doc_id.startswith("CERG-GOV-JF-"):
        return "job_family"
    if doc_id.startswith("CERG-GOV-JD-"):
        return "job_description"
    return TYPE_LABELS.get(typ, typ.lower())


def pillar_from_path(path: Path, doc_id: str) -> str:
    p = path.as_posix()
    if "/jf-seceng/" in p or doc_id.startswith("CERG-STD-"):
        return "engineering"
    if "/jf-riskops/" in p or doc_id.startswith("CERG-PRC-"):
        return "risk"
    if "/jf-adjunct/" in p:
        return "adjacent"
    if "/jf-exec/" in p:
        return "executive"
    if doc_id.startswith("CERG-GOV-RMF") or doc_id.startswith("CERG-GOV-TAX"):
        return "risk"
    if doc_id.startswith("CERG-GOV-CB") or doc_id.startswith("CERG-GOV-TRC") or doc_id.startswith("CERG-GOV-CEF"):
        return "engineering"
    return "governance"


def priority(doc_id: str, path: Path) -> str:
    spine = {
        "CERG-POL-001", "CERG-GOV-FRM-001", "CERG-GOV-OM-001", "CERG-GOV-CAT-001",
        "CERG-GOV-RMF-001", "CERG-PRC-RM-001", "CERG-TMPL-RM-001", "CERG-PRC-VM-001",
    }
    if doc_id in spine:
        return "high"
    if path.parts[0] == "roles":
        return "low"
    return "medium"


def publication_profile(status: str, classification: str) -> str:
    if status == "External Interface":
        return "external_interface"
    if classification.lower() == "public":
        return "public"
    return "restricted"


def discover_docs():
    docs = []
    seen = set()
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if not rel.parts or rel.parts[0] not in INCLUDE_DIRS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        metadata = parse_metadata(text)
        doc_id = metadata.get("Document ID")
        if not doc_id:
            m = DOC_ID_RE.search(path.name)
            doc_id = m.group(0) if m else None
        if not doc_id or doc_id in seen:
            continue
        seen.add(doc_id)
        file_bytes = path.read_bytes()
        classification = metadata.get("Classification", "Public")
        status = metadata.get("Status", "Approved")
        owner = metadata.get("Owner") or metadata.get("Document Owner") or "Governance Pillar Leader"
        approved_by = metadata.get("Approved By") or metadata.get("Approval Authority") or owner
        rel_posix = rel.as_posix()
        docs.append({
            "document_id": doc_id,
            "title": title_from_path(path, doc_id),
            "document_type": type_from_id(doc_id),
            "domain": domain_from_id(doc_id),
            "version": metadata.get("Version", ""),
            "status": status,
            "classification": classification,
            "publication_profile": publication_profile(status, classification),
            "owner_role": owner,
            "approval_authority": approved_by,
            "parent_artifact": metadata.get("Parent Policy") or metadata.get("Parent Document") or metadata.get("Parent Plan") or "",
            "source_path": rel_posix,
            "source_file": path.name,
            "source_hash": hashlib.sha256(file_bytes).hexdigest(),
            "canonical_url": f"{GITHUB_BASE}/{rel_posix}",
            "llm_include": classification.lower() == "public" and status in {"Approved", "External Interface"},
            "llm_priority": priority(doc_id, rel),
            "normative_weight": "primary" if doc_id == "CERG-POL-001" else "supporting",
            "pillar": pillar_from_path(rel, doc_id),
            "summary": title_from_path(path, doc_id),
        })
    return docs


def write_manifest(docs):
    lines = [
        "# cerg-manifest.yaml",
        "# DERIVED ARTIFACT — authoritative source is the CERG markdown corpus",
        f"# Generated: {date.today().isoformat()} | Owner: Governance Pillar Leader (Document Control)",
        "# Regenerate on any change to source documents",
        "# See METADATA.yaml for full governance information",
        "",
    ]
    fields = [
        "document_id", "title", "document_type", "domain", "version", "status", "classification",
        "publication_profile", "owner_role", "approval_authority", "parent_artifact", "source_path",
        "source_file", "source_hash", "canonical_url", "llm_include", "llm_priority", "normative_weight",
        "pillar", "summary",
    ]
    for doc in docs:
        lines.append(f"- document_id: {yaml_scalar(doc['document_id'])}")
        for field in fields[1:]:
            lines.append(f"  {field}: {yaml_scalar(doc[field])}")
    (MR / "cerg-manifest.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_publication_manifest(docs):
    lines = [
        "# CERG Publication Eligibility Manifest",
        f"# Generated from document metadata | {len(docs)} artifacts",
        "# Separates lifecycle approval from public-release eligibility",
        "",
    ]
    for doc in docs:
        public = doc["classification"].lower() == "public"
        status_ok = doc["status"] in {"Approved", "External Interface"}
        full_allowed = public and status_ok
        summary_allowed = public and status_ok
        lines.extend([
            f"- document_id: {yaml_scalar(doc['document_id'])}",
            f"  source_path: {yaml_scalar(doc['source_path'])}",
            f"  status: {yaml_scalar(doc['status'])}",
            f"  classification: {yaml_scalar(doc['classification'])}",
            f"  publication_profile: {yaml_scalar(doc['publication_profile'])}",
            f"  public_summary_allowed: {yaml_scalar(summary_allowed)}",
            f"  full_text_public_allowed: {yaml_scalar(full_allowed)}",
            f"  redaction_required: {yaml_scalar(not full_allowed)}",
            f"  approved_public_release_by: {yaml_scalar(doc['approval_authority'])}",
            f"  release_date: {yaml_scalar(date.today().isoformat())}",
            "",
        ])
    (MR / "cerg-publication-manifest.yaml").write_text("\n".join(lines), encoding="utf-8")


def main():
    docs = discover_docs()
    write_manifest(docs)
    write_publication_manifest(docs)
    print(f"Regenerated manifest and publication manifest for {len(docs)} artifacts")


if __name__ == "__main__":
    main()
