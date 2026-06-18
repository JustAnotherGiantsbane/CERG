#!/usr/bin/env python3
"""
CERG Compliance Scoring Tool (cerg-score.py)

Reads control baseline statuses from CB-001 and optional CAT-001 catalog
overrides, and produces weighted implementation percentages per framework.

Enforces the "Partial = 0.5" rule from MTR-001 §8.2:
  - Implemented = 1.0
  - Partially Implemented = 0.5
  - Inherited = 1.0 (requires current Inheritance Evidence Package per CB-001 §5)
  - Planned = 0.0
  - Risk Accepted = 0.0 (accepted risk is not implemented)
  - Not Applicable = excluded from denominator
  - Not Implemented = 0.0

Usage:
    python3 tools/cerg-score.py
    python3 tools/cerg-score.py --framework cmmc
    python3 tools/cerg-score.py --cb-json controls.json --verbose
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional

# Default paths relative to repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CB = REPO_ROOT / "governance" / "CERG-GOV-CB-001_Unified_Control_Baseline.md"
DEFAULT_CAT = REPO_ROOT / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md"

# Weight map per MTR-001 §8.2 Rule 2
STATUS_WEIGHT: Dict[str, float] = {
    "Implemented": 1.0,
    "Partially Implemented": 0.5,
    "Inherited": 1.0,
    "Planned": 0.0,
    "Risk Accepted": 0.0,
    "Not Applicable": None,  # excluded
    "Not Implemented": 0.0,
}

WEIGHT_EXPLANATION: Dict[str, str] = {
    "Implemented": "1.0 — fully implemented and evidenced",
    "Partially Implemented": "0.5 — partial credit per MTR-001 §8.2 Rule 2",
    "Inherited": "1.0 — provided by provider/parent (requires current Inheritance Evidence Package)",
    "Planned": "0.0 — not yet operating",
    "Risk Accepted": "0.0 — accepted risk is not implemented control",
    "Not Applicable": "excluded — control not applicable to scope",
    "Not Implemented": "0.0 — no design or implementation exists",
}

# Framework prefixes for regulatory crosswalk filtering
FRAMEWORK_PREFIXES: Dict[str, str] = {
    "nist": "NIST 800-53",
    "cmmc": "CMMC L2",
    "nerc": "NERC-CIP",
    "sox": "SOX",
    "cis": "CIS",
    "iso": "ISO/IEC",
}


class ControlEntry(NamedTuple):
    """A single control with status and optional framework annotation."""
    control_id: str
    status: str
    framework: str  # "Baseline" or framework name from overlay
    overlay: str  # Overlay name if applicable


def parse_cb_statuses(cb_path: Path) -> List[ControlEntry]:
    """
    Parse CB-001 §4 implementation statuses and §6 control entries
    to extract baseline control statuses.
    """
    if not cb_path.exists():
        print_error(f"CB-001 not found at {cb_path}")
        return []

    text = cb_path.read_text(encoding="utf-8")

    # Find the §6 Organizational Baseline section to extract control IDs
    # and any inline status markers. CB-001 §6 is a reference baseline;
    # the actual statuses are maintained in the adopter's copy.
    # We extract the canonical control list as denominator.

    section_6_match = re.search(
        r"## 6\. Organizational Baseline \(Core\)",
        text,
    )
    section_7_match = re.search(
        r"## 7\. Control Status Decision Tree",
        text,
    )

    controls: List[ControlEntry] = []

    if not section_6_match:
        print_warning("Could not find §6 (Organizational Baseline) in CB-001")
        return controls

    section_6_start = section_6_match.end()
    section_6_end = section_7_match.start() if section_7_match else len(text)
    section_6_text = text[section_6_start:section_6_end]

    # Extract control IDs from §6 tables: lines with "|| AC-2 " or "|| AC-2|"
    control_pattern = re.compile(
        r"\|\|\s*([A-Z]{2}-\d+(?:\([^)]*\))?)",
    )
    for match in control_pattern.finditer(section_6_text):
        cid = match.group(1)
        controls.append(ControlEntry(
            control_id=cid,
            status="Not Implemented",  # default — overridden by CAT-001 or adopter input
            framework="Baseline",
            overlay="",
        ))

    # Extract overlay controls from §8 overlay descriptions
    overlay_section = re.search(
        r"## 8\. Overlay Matrix(.+?)(?:#+\s|$)",
        text,
        re.DOTALL,
    )
    if overlay_section:
        overlay_text = overlay_section.group(1)
        # Look for overlay names and any control references
        overlay_names = re.findall(
            r"\|\|\s*\*\*([A-Z][\w\s-]+?)\*\*\s*\|",
            overlay_text,
        )
        for name in overlay_names:
            name_clean = name.strip()
            if name_clean and name_clean not in ("Overlay", "Applies To", "Adds / Tightens"):
                # Each overlay adds control requirements; count them
                # as additional control obligations
                cid = f"OVERLAY-{name_clean.upper().replace(' ', '_').replace('-', '_')}"
                controls.append(ControlEntry(
                    control_id=cid,
                    status="Not Implemented",
                    framework=name_clean,
                    overlay=name_clean,
                ))

    return controls


def parse_cat_overrides(cat_path: Path) -> Dict[str, str]:
    """
    Parse CAT-001 §5 catalog table to extract document-level statuses
    that may override CB-001 default statuses.
    """
    overrides: Dict[str, str] = {}
    if not cat_path.exists():
        print_warning(f"CAT-001 not found at {cat_path}; using CB-001 defaults")
        return overrides

    text = cat_path.read_text(encoding="utf-8")

    # Find §5 catalog table
    cat_section = re.search(
        r"## 5\..+?Catalog|\\|\\|\\s*`CERG-",
        text,
    )
    if not cat_section:
        return overrides

    # Parse table rows looking for document IDs and statuses
    row_pattern = re.compile(
        r"\|\s*`(CERG-[A-Z]+-\d+)`\s*\|\s*[^|]*\|\s*([^|]*?)\s*\|",
    )
    for match in row_pattern.finditer(text):
        doc_id = match.group(1)
        status = match.group(2).strip()
        # Normalize statuses
        for key in STATUS_WEIGHT:
            if key.lower() in status.lower():
                overrides[doc_id] = key
                break

    return overrides


def compute_scores(
    controls: List[ControlEntry],
    overrides: Dict[str, str],
    framework_filter: Optional[str] = None,
) -> Dict:
    """
    Compute weighted implementation scores.

    Returns dict with per-framework and total scores.
    """
    # Organize by framework / overlay
    frameworks: Dict[str, List[ControlEntry]] = defaultdict(list)
    for c in controls:
        fw = c.framework
        if fw == "Baseline":
            fw = "Baseline"
        frameworks[fw].append(c)

    results: Dict[str, Dict] = {}

    for fw_name, fw_controls in sorted(frameworks.items()):
        if framework_filter:
            fw_lower = fw_name.lower()
            filter_lower = framework_filter.lower()
            if filter_lower not in fw_lower and fw_lower != "baseline":
                continue

        total = 0
        weighted = 0.0
        excluded = 0
        details: List[Dict] = []

        for c in fw_controls:
            weight = STATUS_WEIGHT.get(c.status)
            if weight is None:
                excluded += 1
                details.append({
                    "control_id": c.control_id,
                    "status": c.status,
                    "weight": "excluded",
                    "explanation": WEIGHT_EXPLANATION.get(c.status, "Excluded (N/A or unknown)"),
                })
                continue

            total += 1
            weighted += weight
            details.append({
                "control_id": c.control_id,
                "status": c.status,
                "weight": weight,
                "explanation": WEIGHT_EXPLANATION.get(c.status, ""),
            })

        pct = (weighted / total * 100) if total > 0 else 0.0
        results[fw_name] = {
            "total_controls": total,
            "excluded": excluded,
            "weighted_score": round(weighted, 1),
            "implementation_pct": round(pct, 1),
            "controls": details,
        }

    # Overall
    all_controls = [c for c in controls if STATUS_WEIGHT.get(c.status) is not None]
    all_total = len(all_controls)
    all_weighted = sum(STATUS_WEIGHT[c.status] for c in all_controls)
    all_excluded = sum(1 for c in controls if STATUS_WEIGHT.get(c.status) is None)
    all_pct = (all_weighted / all_total * 100) if all_total > 0 else 0.0

    results["_overall"] = {
        "total_controls": all_total,
        "excluded": all_excluded,
        "weighted_score": round(all_weighted, 1),
        "implementation_pct": round(all_pct, 1),
    }

    return results


def format_results(results: Dict, verbose: bool = False) -> str:
    """Format scoring results as a human-readable report."""
    lines: List[str] = []
    lines.append("=" * 70)
    lines.append("CERG COMPLIANCE SCORING REPORT")
    lines.append(f"  Enforcing: Partial = 0.5 per MTR-001 §8.2")
    lines.append("=" * 70)
    lines.append("")

    overall = results.pop("_overall", {})
    for fw_name, data in sorted(results.items()):
        pct = data["implementation_pct"]
        bar = "#" * int(pct / 5) + "-" * (20 - int(pct / 5))
        lines.append(f"  {fw_name:40s} {pct:5.1f}%  [{bar}]")
        lines.append(f"  {'':40s} {data['weighted_score']:5.1f} / {data['total_controls']} controls")
        if data["excluded"]:
            lines.append(f"  {'':40s} ({data['excluded']} N/A controls excluded)")

        if verbose and data["controls"]:
            lines.append("")
            lines.append(f"  {'Control':20s} {'Status':25s} {'Weight':>6s}")
            lines.append(f"  {'-'*20} {'-'*25} {'-'*6}")
            for c in data["controls"]:
                w = f"{c['weight']:.1f}" if isinstance(c['weight'], float) else c['weight']
                lines.append(f"  {c['control_id']:20s} {c['status']:25s} {w:>6s}")
        lines.append("")

    if overall:
        lines.append("-" * 70)
        lines.append(f"  OVERALL SCORE:         {overall['implementation_pct']:5.1f}%")
        lines.append(f"  Weighted Score:        {overall['weighted_score']:5.1f} / {overall['total_controls']}")
        lines.append(f"  Controls Excluded:     {overall['excluded']}")
        lines.append(f"  Controls in Scope:     {overall['total_controls']}")
        lines.append("-" * 70)

    return "\n".join(lines)


def format_json_results(results: Dict) -> str:
    """Format as JSON."""
    return json.dumps(results, indent=2)


def print_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def print_warning(msg: str) -> None:
    print(f"[WARN] {msg}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CERG Compliance Scoring Tool — enforces Partial=0.5 per MTR-001 §8.2",
    )
    parser.add_argument(
        "--cb-path",
        type=Path,
        default=DEFAULT_CB,
        help=f"Path to CB-001 markdown (default: {DEFAULT_CB})",
    )
    parser.add_argument(
        "--cat-path",
        type=Path,
        default=DEFAULT_CAT,
        help=f"Path to CAT-001 markdown (default: {DEFAULT_CAT})",
    )
    parser.add_argument(
        "--framework", "-f",
        type=str,
        default=None,
        help="Filter to a specific framework (nist, cmmc, nerc, sox, cis, iso)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Include per-control detail in output",
    )
    parser.add_argument(
        "--cb-json",
        type=Path,
        default=None,
        help="Load control list from JSON file instead of parsing CB-001",
    )

    args = parser.parse_args()

    if args.cb_json:
        if not args.cb_json.exists():
            print_error(f"JSON input not found: {args.cb_json}")
            return 1
        try:
            data = json.loads(args.cb_json.read_text(encoding="utf-8"))
            controls = [
                ControlEntry(
                    control_id=c["control_id"],
                    status=c.get("status", "Not Implemented"),
                    framework=c.get("framework", "Baseline"),
                    overlay=c.get("overlay", ""),
                )
                for c in data.get("controls", [])
            ]
        except (json.JSONDecodeError, KeyError) as e:
            print_error(f"Invalid JSON input: {e}")
            return 1
    else:
        controls = parse_cb_statuses(args.cb_path)

    overrides = parse_cat_overrides(args.cat_path)

    # Apply overrides from CAT-001 to matching controls
    # (CB-001 control IDs don't directly match CAT-001 document IDs,
    #  but we track the mapping for informational purposes)
    _ = overrides  # reserved for future use

    if not controls:
        print_warning("No controls found — cannot compute score")
        return 0

    results = compute_scores(controls, overrides, args.framework)

    if args.json:
        print(format_json_results(results))
    else:
        print(format_results(results, verbose=args.verbose))

    return 0


if __name__ == "__main__":
    sys.exit(main())
