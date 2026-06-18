# Task A02 Output: Run mechanical validation and collect known structural issues

## Scope Reviewed
- Files read: `machine-readable/cerg-llm-index.json`, `governance/CERG-GOV-GEN-001_CERG_Glossary.md`, `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`, `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`, `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`, `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`, and scan outputs across `governance/`, `standards/`, `procedures/`, `plans/`, `templates/`, `roles/`, and `examples/`.
- Sections reviewed: mechanical validation output; integrity checker output; numbered headings; canonical role roster; candidate role synonyms; core glossary drift terms.
- Files intentionally not reviewed: non-Markdown files, rendered outputs, and machine-readable generated YAML/JSON other than the LLM index.

## Method
- Steps performed:
  1. Ran `python3 tools/cerg-validate.py`.
  2. Ran `python3 tools/cerg-integrity-check.py`.
  3. Ran `grep -RIn '^## [0-9]' governance standards procedures plans templates roles examples` and analyzed top-level/subsection numbering patterns.
  4. Extracted the 27 canonical roles from `GEN-001` §6 and compared scan hits for likely noncanonical role synonyms.
  5. Scanned glossary drift terms: `finding`, `vulnerability`, `risk`, `exception`, `risk acceptance`, `control gap`, `incident`, `evidence`, `record`, `owner`, `accountable`, `responsible`, plus common role-name variants.
- Search terms or scripts used: Python regex scans over Markdown files; targeted seed-observation searches for `NERC-CIP,,`, `800-171,,`, `||`, and long role-JD bullets over 350 characters.
- Assumptions avoided: scan hits were not treated as defects without context. This task records mechanical and human-review observations only.

## Validation Baseline

### Authoritative validator

Command:

```bash
python3 tools/cerg-validate.py
```

Result:

```text
CERG validation passed: links, catalog references, and file inventory are consistent.

Quality Checks: 0 issues — PASS
```

Exit status: `0`.

### Supplementary integrity checker

Command:

```bash
python3 tools/cerg-integrity-check.py
```

Result:

```text
CERG Integrity Check
============================================================
Files found: 146
Catalog entries: 131

RESULTS
============================================================

[P0] FAIL — 0 issue(s)

[P1] WARN — 0 issue(s)

[P2] INFO — 0 issue(s)

============================================================
Total issues: 0
P0 defects: 0 — PASS
```

Exit status: `0`.

## Mechanical Scan Summary

| Scan | Result | Notes |
|---|---:|---|
| Markdown heading scan | 1,377 numbered heading lines | Raw grep includes fenced examples in STY-001, so human review is required before treating anomalies as structural defects. |
| Canonical roles extracted from GEN-001 | 27 | Matches the expected CISO, pillar, engineering, risk, governance, and adjacent IR roles. |
| Role JD long bullet scan (`>350` chars) | 51 lines across 25 files | Confirms the seed observation is widespread, not isolated to one Cloud Security Engineer file. |
| FRM-001 duplicate punctuation scan | 2 hits | `NERC-CIP,,` and `800-171,,` verified in a spine document. |
| SLC-001 double-pipe table scan | 2 hits | Leading `||` verified in §3.4 table rows. |
| FLOW-001 heading/TOC scan | Multiple hits | TOC, top-level headings, and subsection numbers drift from each other. |

## Role and Vocabulary Scan Counts

These counts are baseline indicators for F02/D01 review. They are not findings by themselves.

| Term | Hits | Files | Initial classification |
|---|---:|---:|---|
| `security team` | 25 | 16 | Mixed: many benign narrative references; some useful as explicit negative examples. |
| `GRC` | 58 | 26 | Mixed: often tool/system shorthand; review for generic-GRC voice drift. |
| `compliance team` | 5 | 5 | Mixed: may be descriptive in workforce/JD contexts; review for role precision. |
| `risk owner` | 26 | 10 | Context-sensitive: may be enterprise-risk/business role, not always CERG role. |
| `system owner` | 24 | 11 | Context-sensitive: likely access/asset/business ownership term, but not in GEN-001 role roster. |
| `asset owner` | 33 | 21 | Canonical term in GEN-001, but not a canonical workforce role. |
| `technical owner` | 17 | 7 | Record field used in FLOW/templates/examples; not a canonical role. |
| `business owner` | 162 | 51 | Canonical term in GEN-001, heavy and likely correct. |
| `finding` | 1,066 | 111 | High-volume canonical term; C03/F02 must classify context. |
| `vulnerability` | 352 | 85 | High-volume canonical distinction; C03/F02 must classify context. |
| `risk` | 5,234 | 131 | Too broad for blind replacement; C03 must focus on conversion rules. |
| `exception` | 883 | 87 | High-volume canonical term; C03/F02 must classify context. |
| `waiver` | 7 | 4 | Mostly discouraged/negative examples; review all hits. |
| `deviation` | 122 | 27 | Often legitimate regulatory/NERC-CIP term; distinguish from generic waiver language. |
| `acceptance` | 442 | 79 | Review as part of risk acceptance terminology. |
| `artifact` | 427 | 85 | Generally accepted CERG term. |
| `evidence` | 2,251 | 114 | Core term; review quality/record closure context. |
| `record` | 1,127 | 90 | Core term; review source-of-truth consistency. |
| `ticket` | 90 | 42 | Context-sensitive: can be acceptable as implementation system but should not replace authoritative record names. |
| `control owner` | 21 | 12 | Context-sensitive; may blur owning pillar/control baseline ownership. |
| `process owner` | 6 | 6 | Context-sensitive; review where it substitutes for a canonical role. |
| `responsible` | 123 | 86 | Mostly RACI language; validate one-A/accountability rules where used. |
| `accountable` | 170 | 67 | Mostly RACI/accountability language; validate role clarity where used. |
| `Risk Manager` | 2 | 1 | Only appears in OM-001 as a do-not-use synonym for Risk Pillar Leader. |
| `AppSec owner` | 1 | 1 | Only appears in STY-001 as a negative example. |
| `Audit person` | 1 | 1 | Only appears in STY-001 as a negative example. |
| `Vendor owner` | 1 | 1 | Only appears in STY-001 as a negative example. |
| `Executive security lead` | 1 | 1 | Only appears in STY-001 as a negative example. |

## Findings

### A02-F01 Medium FLOW-001 table of contents and heading numbering drift
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: The Table of Contents and actual numbered sections do not match. The TOC starts with `1. Operating Principles` linked to `#2-operating-principles`, while the actual Section 1 is `Flow Structure Conventions` and Section 2 is `Operating Principles`. Later actual sections continue through `## 21. Document Control`, while the TOC ends at `18. Document Control`. Subsections under `## 8. Shared State Models` are numbered `### 7.1` through `### 7.5`, and minimum record templates under `## 19` are numbered `### 16.1` through `### 16.5`.

Why it matters: FLOW-001 is a spine document for handoffs. Numbering drift makes cross-references brittle and can cause readers to cite or implement the wrong flow section.

Evidence from corpus:
- Actual headings include `## 1. Flow Structure Conventions`, `## 2. Operating Principles`, `## 8. Shared State Models`, `### 7.1 Project Security Review State Model`, `## 19. Minimum Record Templates`, and `### 16.1 Finding Record`.
- TOC lists `1. Operating Principles`, `7. Shared State Models`, `16. Minimum Record Templates`, and `18. Document Control`.

Recommended action: Create a targeted FLOW-001 polish/edit task after conceptual flow review, or fix early if later C01 relies on stable section references. Renumber from highest to lowest, update TOC, and search/update cross-references.

Owner/workstream: Handoffs / Polish.

### A02-F02 Low SLC-001 malformed table pipes verified
Affected files:
- `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md`

Problem: Two rows in the Section 3.4 table begin with `||`, which creates malformed Markdown table syntax.

Why it matters: This is low conceptual risk but visible formatting debt in an Approved governance instrument.

Evidence from corpus:
- Line 91 begins `|| Request type | Tier / trigger | ...`.
- Line 93 begins `|| Exception / risk-acceptance request intake | ...`.

Recommended action: Safe mechanical polish: replace the leading `||` with `|` on those rows, then validate.

Owner/workstream: Polish.

### A02-F03 Low FRM-001 duplicate punctuation verified in spine text
Affected files:
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`

Problem: The framework document contains duplicate commas in framework/regulation references.

Why it matters: Low severity, but FRM-001 is a front-door spine document and visible punctuation defects reduce polish.

Evidence from corpus:
- Intro line contains `NERC-CIP,,`.
- Design principle line contains `800-171,,`.

Recommended action: Safe mechanical polish in FRM-001 after A/B baseline commits.

Owner/workstream: Polish.

### A02-F04 Medium Role JD readability issue is widespread
Affected files:
- 25 files under `roles/jf-*/*.md`, including `roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md`.

Problem: The long-bullet scan found 51 role-JD bullet lines over 350 characters. Many appear to contain several duties collapsed into a single bullet separated by hyphens.

Why it matters: The workforce architecture is intended to make role accountability human-readable. Collapsed bullets make per-role JDs harder to use for hiring, onboarding, and role-to-procedure fit testing.

Evidence from corpus:
- `roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md:49` length 965.
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md:49` length 1053.
- `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-001_NERC-CIP_Compliance_Manager.md:49` length 1074.

Recommended action: Carry into D01/D02/G03. Do not batch-reflow blindly; verify whether bullets were generated from structured source and whether section semantics should become sub-bullets.

Owner/workstream: Roles / Polish.

### A02-F05 High Two Risk Operations JD files appear role-content swapped
Affected files:
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md`

Problem: Mechanical long-bullet samples show the Detection Engineer JD containing vendor-tiering and third-party assessment duties, while the Vendor Risk Analyst JD contains detection-rule/SIEM/ATT&CK duties.

Why it matters: If confirmed by D01, this is a workforce accountability defect: readers would assign detection and vendor-risk responsibilities to the wrong role.

Evidence from corpus:
- `JD-RISKOPS-004_Detection_Engineer.md:49` begins with `Tier vendors by risk... Conduct vendor security assessments...`.
- `JD-RISKOPS-007_Vendor_Risk_Analyst.md:49` begins with `Author, test, and deploy detection rules across SIEM, EDR, NDR...`.

Recommended action: Verify in D01 against RAC-001 and role files, then swap or rewrite the affected JD responsibility/knowledge sections if confirmed.

Owner/workstream: Roles.

## Human-Review Observations

| Observation | Initial interpretation | Follow-up |
|---|---|---|
| `security team` appears 25 times | Many hits are benign narrative references or negative examples, not role drift. | F02 should classify only contexts where a canonical role is needed. |
| `technical owner`, `system owner`, `control owner`, and `process owner` appear as record fields or business/process terms | These may be valid operational ownership concepts even though they are not canonical CERG workforce roles. | D01/F02 should decide whether GEN-001 needs clearer distinction between role names and owner fields. |
| `waiver` appears only 7 times | Likely manageable; several hits are explicit warnings not to treat exception/risk acceptance as a waiver. | F02/C03 can review all hits manually. |
| Raw heading scan flags STY-001 | False positives likely come from fenced skeleton/examples and section `12.5`; do not treat as numbering failure without code-fence-aware parsing. | G03 polish only if a human reader sees drift outside examples. |
| FLOW-001 contains two `### Mandatory Rules` blocks in F-04 | Could be harmless duplication or conflicting closure rule language, because one says Risk must validate Critical/High while the later duplicate says Risk must validate every finding. | C03/C01 should resolve during finding-conversion review. |

## Positive Confirmations
- The CI validator is clean with 0 errors.
- The supplementary integrity checker is clean with 0 P0/P1/P2 issues.
- The index and filesystem counts already confirmed in A01 remain consistent.
- The canonical role roster can be extracted cleanly from GEN-001 and contains 27 roles.
- The most obvious prohibited role synonyms from STY-001 (`AppSec owner`, `Audit person`, `Vendor owner`, `Executive security lead`) appear only in the style guide as negative examples.

## Open Questions
- Should `Technical Owner`, `System Owner`, `Asset Owner`, `Control Owner`, and `Process Owner` be explicitly classified in GEN-001 as ownership fields/persona terms rather than canonical roles?
- Should FLOW-001 numbering be fixed before C01 flow tracing, or should C01 first confirm any conceptual changes that might require additional renumbering?
- Were the role JD sections generated from a source that caused the Detection Engineer and Vendor Risk Analyst content swap, and could the same generator have affected other JD fields?

## Proposed Next Tasks
- Commit A01 and A02 audit outputs separately.
- Fix safe low-severity polish only after the author confirms whether to keep going into edits now or continue audit findings first.
- Next conceptual task in recommended order: B01, with A02-F01/A02-F05 carried forward as known issues.
