# Task H04 Output: Auditor/evidence path comprehension test

## Scope Reviewed
- Trace spine and catalogs:
  - `governance/CERG-POL-001_Cybersecurity_Policy.md`
  - `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`
  - `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`
  - `governance/CERG-GOV-CAT-002_Record_Catalog.md`
  - `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
  - `templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md`
- Requirement-specific files:
  - `standards/CERG-STD-AC-001_Access_Management_Standard.md`
  - `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`
  - `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
  - `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
  - `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
  - `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
  - `standards/CERG-STD-CUI-001_CUI_Handling_Standard.md`
  - `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
  - `governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md`
  - `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md`

## Method
- Persona: external auditor, assessor, regulator, or internal audit partner.
- Controls traced:
  1. Privileged access review.
  2. Vulnerability remediation SLA.
  3. Architecture review for a regulated system, using CUI as the representative regulated overlay.
- For each trace, I followed:
  - policy statement;
  - control baseline;
  - standard requirement;
  - procedure step;
  - role accountable;
  - record created;
  - evidence quality rule;
  - metric/dashboard appearance;
  - improvement loop if failure occurs.
- I assessed whether the trace can be followed without tribal knowledge and recorded ambiguous evidence, missing ownership, or weak links.

## Executive Summary

CERG is auditable in structure. The policy-to-control-to-standard-to-procedure-to-record-to-evidence model exists and mostly works. `CB-001`, `TRC-001`, `CAT-002`, `AUD-001`, and `PRC-AUD-001` give an auditor a real path from requirement to proof instead of relying on undocumented control-owner explanations.

The strongest trace is vulnerability remediation SLA. It has a clear policy mandate, canonical controls (`RA-5`, `SI-2`), a detailed operating procedure, source metrics, exception/risk acceptance routing, and improvement-loop triggers.

The access-review trace is substantively strong, but ownership appears split across Engineering, Governance, Identity Engineer, and Evidence Librarian in ways an auditor may need explained. The architecture-review trace is operationally strong but less clean as a control trace because "architecture review for regulated system" is a workflow composed from several controls rather than a single named baseline control.

Top improvements for auditor comprehension:

1. Add `PRC-AC-002` explicitly to `TRC-001` rows for `AC-2`, `AC-6`, and access review evidence.
2. Add a one-page evidence map for privileged access review: population, period, reviewer, decisions, removals, exceptions, validation, storage.
3. Add a named control or trace row for `Pre-production / architecture review for regulated systems`, or a curated multi-control trace in `TRC-001`.
4. Reconcile `TMPL-AR-001` with the richer embedded templates in `PRC-AR-001`, or state which artifact is authoritative for audit evidence.
5. Clarify producer/owner roles in record/evidence chains: control owner, process owner, evidence producer, evidence librarian, and accountable approver.

## Trace 1 — Privileged Access Review

### Auditor question
Can the auditor prove that privileged access was reviewed on the required cadence, by an accountable reviewer, with findings removed or dispositioned, and with evidence retained?

### End-to-end trace
| Trace element | Artifact and finding |
|---|---|
| Policy statement | `POL-001` Principle 2 requires least privilege, documented lifecycle process, access reviews on subordinate-standard frequency, and heightened controls for privileged access. Principle 6 requires privileged/remote access logging and monitoring. |
| Control baseline | `CB-001` §6.1: `AC-2 Account Management` requires approved request, named owner, access level, current JML record, quarterly recert report. `AC-6 Least Privilege` requires users/admins/vendors only have needed access; privileged access time-bound/JIT and recorded. `AC-17` governs remote access. `IA-2` requires phishing-resistant MFA for privileged users. |
| Traceability matrix | `TRC-001` maps `AC-2` to `STD-AC-001`, audit testing through `PRC-AUD-001`, and evidence as JML log, quarterly recertification report, `TMPL-AUD-001`. `AC-6` maps to quarterly access review and exception workflow. |
| Standard requirement | `STD-AC-001` §9 requires access reviews by tier: privileged roles quarterly, Tier 1/SOX quarterly, Tier 2 semiannual, Tier 3 annual. It requires active attributable reviewer decisions and says rubber-stamp approvals are non-compliant. Findings such as terminated users, role mismatch, SoD violations, and dormant accounts must be remediated. |
| Procedure step | `PRC-AC-002` §5 gives operational cadence and workflow: campaign launched in IGA; reviewers see identity, entitlements, last-used dates, and role rationale; each entitlement is certified, modified, or removed; removals occur within 5 business days; audit log captured; exceptions flagged to Engineering/Identity. `PRC-AC-002` §6 adds PAM controls, dormant privileged account audit, session-recording sampling. |
| Role accountable | Substantive accountability is split: `STD-AC-001` says Governance owns access review/recertification program, Engineering operates identity platforms, Risk detects identity threats. `PRC-AC-002` owner is Identity Engineer. `PRC-AUD-001` makes Evidence Librarian responsible for evidence library and Governance responsible for audit response. |
| Record created | `CAT-002` §4.3 names `Access Review Record`, primary owner Identity Engineer / Governance, required for scheduled recertification or privileged access review, proving entitlement review and corrective actions. Also relevant: Evidence Index Entry, Finding Record if excessive access is material, Security Exception Record if access cannot be removed. |
| Evidence quality rule | `AUD-001` requires who produced evidence, when, system/control, period covered, and where stored. For E2, evidence must show complete scope or sample and population. For E3, method must be repeatable, independent where required, and show failure conditions. The bad-evidence examples explicitly reject `email saying done`, `policy text with no proof of operation`, and `sample with no population`. |
| Metric/dashboard | `MTR-001` §3.4: `ID-002 Access Recertification Currency`, `ID-003 Dormant Privileged Accounts`, `ID-001 Phishing-Resistant MFA Coverage (Privileged)`, `ID-004 Break-Glass Account Hygiene`; also `CE-001` and `CE-002` for control effectiveness/evidence quality. |
| Improvement loop | If review evidence fails or excessive access recurs, `PRC-AUD-001` §8 routes evidence deficiency to corrective action and repeated evidence misses to improvement. `PRC-LL-001` treats deficient audit/control ratings and repeated patterns as lessons. `IMPREG-001` tracks program-level changes to verified closure. |

### Evidence package an auditor should expect
- Access review campaign record or IGA audit log.
- System/application population: all privileged groups, admin roles, break-glass accounts, service/admin accounts as applicable.
- Review period and cadence evidence.
- Named reviewers and reviewer authority.
- Per-entitlement decisions: certify, modify, remove.
- Removal/modify tickets and post-removal validation export.
- Exceptions or risk acceptances for access retained outside policy.
- Evidence library path and submission package archive.
- Sampling method if not full-population review.

### Auditor comprehension result
Mostly pass. The auditor can trace from policy to evidence. The strongest material is in `STD-AC-001`, `PRC-AC-002`, `AUD-001`, and Story 3/5 examples. The chain is understandable if the auditor knows to open the access runbook after reading the standard.

### Gaps / ambiguities
| Gap | Severity | Why it matters | Recommendation |
|---|---:|---|---|
| `TRC-001` does not explicitly name `PRC-AC-002` for `AC-2` or `AC-6`. | High | The authoritative operating runbook is easy to miss in an auditor trace. | Update `TRC-001` AC rows to include `PRC-AC-002` as the access review/JML/PAM operating procedure. |
| Accountability varies by document: Engineering owner in `CB-001`, Governance owner in `STD-AC-001`, Identity Engineer/Governance in `CAT-002`. | Medium | The auditor may ask who owns control operation versus evidence versus audit response. | Add a short role split: Engineering operates IAM; Governance owns review program/evidence obligation; Identity Engineer produces exports; Evidence Librarian indexes evidence. |
| No single access-review evidence checklist exists in the procedure. | Medium | Evidence may be complete operationally but incomplete for audit. | Add checklist to `PRC-AC-002` or `PRC-AUD-001`: population, period, reviewer, decisions, removals, exceptions, validation, storage. |

## Trace 2 — Vulnerability Remediation SLA

### Auditor question
Can the auditor prove that a confirmed vulnerability/exposure was triaged, assigned an SLA, treated or accepted before SLA miss, independently verified, and reflected in metrics?

### End-to-end trace
| Trace element | Artifact and finding |
|---|---|
| Policy statement | `POL-001` Principle 5 requires continuous vulnerability visibility, severity/exploitability/asset-criticality assessment, tracking to remediation or documented risk acceptance within `PRC-VM-001` SLAs, OT-safe methods, and pre-production remediation or acceptance before go-live. |
| Control baseline | `CB-001` §6.6: `RA-5 Vulnerability Monitoring and Scanning` requires authenticated scanning or approved passive/alternative method with scan reports and SLA dashboard. `SI-2 Flaw Remediation` requires Critical/High findings remediated within SLA or approved exception/risk acceptance before SLA miss. `RA-3` requires risk assessment and treatment in the risk register. |
| Traceability matrix | `TRC-001` maps `RA-5` to `PRC-VM-001` with scan reports and SLA dashboard. `SI-2` maps to `PRC-VM-001` and `PRC-RM-001`, with SLA report, exception register, and POA&M as evidence. Gap signal: Critical/High finding past SLA without approved treatment. |
| Standard requirement | The operative requirement is primarily procedural rather than standard-based: `PRC-VM-001` is the canonical exposure procedure. Related standards include configuration baselines and environment overlays such as `STD-CUI-001` for CUI and `STD-OT-001` for OT/BES. |
| Procedure step | `PRC-VM-001`: collect observations; validate asset and condition; validate exposure path; classify; assign SLA from §7.2; select treatment; verify closure; route risk acceptance/exceptions through §11 and `PRC-RM-001`. SLA clock starts at classification, not raw scanner observation. |
| Role accountable | `PRC-VM-001` §3: Exposure Management Lead owns the procedure, triage, classification, tracking, posture, and SLAs. Engineering Pillar Leader implements treatments and compensating controls. System/Asset Owners approve maintenance windows and accept residual risk. CISO approves High/Critical acceptances under RMF authority. |
| Record created | `CAT-002` §4.2: Finding Record, Exposure Backlog Item, Risk Register Entry, Security Exception Record, Risk Acceptance Memo where applicable. Evidence Index Entry stores closure evidence. For CUI, POA&M Item may be required. |
| Evidence quality rule | `AUD-001` rejects tool exports with no scope definition. Acceptable vulnerability evidence needs scope, date, asset, scan configuration/exclusions, treatment evidence, verified closure method, and storage location. `PRC-VM-001` §9 requires independent verification: authenticated re-scan, configuration evidence, reachability test, or compensating-control validation. |
| Metric/dashboard | `MTR-001` §3.2: `EM-001` confirmed reachable critical exposure, `EM-002` observations awaiting triage, `EM-004` KEV with reachable path, `EM-007` SLA misses with compensating controls, `EM-008` SLA misses with no controls, `EM-009/010` timing metrics. `PH-001/002/003` cover patch hygiene separately. |
| Improvement loop | Repeated SLA misses, red metrics for two consecutive periods, control-test deficiencies, near-misses, or audit findings trigger `PRC-LL-001` lessons intake. Program changes are tracked in `IMPREG-001`, e.g., amend scan coverage, patch windows, asset inventory, or standards. |

### Evidence package an auditor should expect
- Observation source record: scanner, CSPM, SCA, OT passive monitor, vendor advisory, etc.
- Asset validation evidence: inventory record, owner, classification, environment, scope.
- Exposure-path assessment: reachability, exploitability, compensating controls, KEV/active exploitation status.
- Classification and SLA assignment record.
- Treatment decision: patch, configuration, block path, compensating control, redesign, exception, or acceptance.
- Change/remediation evidence with timestamp.
- Closure verification evidence: rescan, reachability test, configuration export, or compensating-control test.
- Exception/risk acceptance/POA&M where SLA cannot be met.
- Metrics extract showing SLA state and closure.

### Auditor comprehension result
Pass. This is the cleanest H04 trace. The control path is clear, the procedure is detailed, the evidence expectations are explicit, and the metrics are source-aligned.

### Gaps / ambiguities
| Gap | Severity | Why it matters | Recommendation |
|---|---:|---|---|
| The trace relies heavily on `PRC-VM-001`; there is no single domain standard called `Vulnerability Management Standard`. | Low | Not a defect if `PRC-VM-001` is intentionally authoritative, but auditors may expect a standard. | In `TRC-001` or `CB-001`, explicitly state that `PRC-VM-001` is the canonical operating requirement for RA-5/SI-2 SLA parameters. |
| Finding/exposure/observation vocabulary is strong in `PRC-VM-001` but can drift in flow and record documents. | Medium | Auditors need consistent status names to sample records. | Carry forward the existing record-name cleanup work from G02/G03: observation → finding/exposure → treatment → closure. |
| POA&M trigger is clear for CUI but less obvious in a generic vulnerability trace. | Low | Regulated auditors will ask when a finding becomes POA&M. | Add a small overlay note in `PRC-VM-001` evidence section: CUI SLA breach → POA&M; BES compliance impact → CIP deviation. |

## Trace 3 — Architecture Review for a Regulated System

### Auditor question
Can the auditor prove that a regulated system, represented here by a CUI system, received security review before go-live; that regulated-scope controls were identified; that unresolved risks were accepted or tracked; and that the handoff package contains evidence?

### End-to-end trace
| Trace element | Artifact and finding |
|---|---|
| Policy statement | Multiple `POL-001` principles apply: Principle 1 inventory and owner/regulatory designation; Principle 2 access; Principle 3 baseline hardening and exceptions; Principle 4 segmentation and sensitive-data protection; Principle 5 pre-production vulnerabilities remediated or accepted before go-live; Principle 7 controlled changes; Principle 8 third-party/supply-chain assessment. |
| Control baseline | No single baseline control is named `architecture review`. The workflow composes controls: `CM-8` inventory, `AC-3/AC-6/IA-2` identity, `CM-2/CM-6/CM-7` baseline/hardening, `CM-3` change control, `RA-3` risk assessment, `RA-5/SI-2` vulnerability/flaw remediation, `SI-4/AU-2` monitoring/logging, `SR-2/SR-3` vendor/supply chain. For CUI, overlay controls map through `TRC-001` §5. |
| Traceability matrix | `TRC-001` maps `AC-3` and `IA-3` to architecture review, `CM-3` to change control, `RA-3` to risk register, `RA-5/SI-2` to exposure management, and `SR-2` to TPRM. Overlay section maps CUI to `STD-CUI-001` and `PLN-CUI-001` with SSP, POA&M, CUI evidence package, SPRS/CMMC readiness records. |
| Standard requirement | `STD-CUI-001` requires CUI boundary definition, inventory, CUI data-flow map, periodic CUI risk assessment, monthly vulnerability scans, POA&M for gaps, CUI architecture diagram, baseline/change impact review, SSP/POA&M upkeep, and CUI incident/reporting obligations. Peer standards apply for access, IT/cloud/SaaS, logging, configuration, crypto, and resilience. |
| Procedure step | `PRC-AR-001`: mandatory review for CUI, BES/OT, SOX, Restricted-data SaaS, new cloud account, trust boundary, identity/federation/PAM topology, or new data/regulatory scope. Intake records CUI/BES/SOX scope. Engineering determines review path and overlay reviewers. Phase 2 architecture review and threat model align controls to `CB-001`. Phase 4 pre-production checklist verifies DISH, exposure posture, identity, logging, detection, crypto, resilience, vendor/TPRM, overlay artifacts, asset inventory, runbook, and change record. Phase 5 handoff package records control posture, evidence pointers, acceptances, owners, and sign-offs. |
| Role accountable | Business Owner submits intake, owns residual risk, and approves go-live for scope. Technical Lead supplies architecture artifacts. Pre-production Reviewer conducts Engineering review and maintains review record. Risk reviewer leads threat model. Governance Pillar Leader maps CUI/BES/SOX scope and triggers overlay reviewers. Engineering Pillar Leader validates controls and routes residual risk. CISO approves High/Critical risk acceptances. |
| Record created | `CAT-002` §4.3: Project Security Review Record, Threat Model Record, Asset Inventory Record, Asset Coverage Record, Configuration Baseline Record, Security Change Review Record. `CAT-002` §4.5 for CUI: System Security Plan and POA&M Item. Also Evidence Index Entry, Risk Register Entry, Security Exception Record, Risk Acceptance Memo, Vendor Risk Assessment Record as applicable. |
| Evidence quality rule | `AUD-001` requires evidence to identify producer, date, control/system, period, storage location, completeness, scope/population, repeatability, and failure conditions. For architecture review, evidence should be design + operation: intake, diagrams, threat model, control decisions, test outputs, handoff package, and post-go-live review evidence. |
| Metric/dashboard | `MTR-001`: `CM-002 Architecture Reviews Completed Pre-Production`, `SR-001 Architecture Review Turnaround`, `SR-003 Intake Disposition Time`, `SR-005 Time-to-Coverage`, `CE-001` control effectiveness test currency, `CE-002` Critical/High overlay controls with E3 evidence, `GV-001` CUI practices implemented, `GV-002` open POA&M items. |
| Improvement loop | `PRC-AR-001` appeal outcomes inform program improvement via `PRC-LL-001`. Phase 4/5 findings feed risk register and threat model. CUI deficiencies feed POA&M and can trigger `PRC-LL-001` lessons if control test deficient or systemic. `IMPREG-001` records standard, procedure, control, staffing, or metric improvements and verifies effectiveness. |

### Evidence package an auditor should expect
- Project intake with business owner, technical owner, target go-live, data classification, CUI/regulatory scope, vendors, and trust boundaries.
- Scope determination: mandatory/lightweight/out-of-scope, overlay reviewers required, threat model required, TPRM required, SLC tier.
- Required diagrams: context, data flow, identity, trust boundary, network where applicable, CUI boundary, backup/recovery for CUI/Tier 1.
- Architecture review checklist results and findings.
- Threat model with threats, existing controls, gaps, residual risks, owners, and due dates.
- CUI overlay evidence: boundary, inventory, data-flow map, SSP references, POA&M if gaps exist, FedRAMP equivalency where SaaS/cloud hosts CUI.
- Pre-production checklist evidence: DISH scan, exposure report, IdP/PAM export, SIEM source inventory, detection coverage, crypto configuration, backup config, TPRM evidence, asset inventory, runbook, change record.
- Production handoff package and go-live sign-offs.
- Risk acceptance packet if any findings ship open.
- Evidence library index entry and metric source records.

### Auditor comprehension result
Partial pass. The regulated architecture review procedure itself is strong and auditable. The trace is harder than the other two because it is inherently multi-control and multi-overlay. An auditor can follow it, but only if they understand that architecture review is a workflow composed from many controls, not a single `AR-*` control in the baseline.

### Gaps / ambiguities
| Gap | Severity | Why it matters | Recommendation |
|---|---:|---|---|
| No single `architecture review for regulated system` control or trace row exists. | High | Auditors may ask for the control and evidence directly; the answer requires assembling many controls. | Add a curated trace row or appendix in `TRC-001` for regulated architecture review, naming the composite controls and required evidence package. |
| `TMPL-AR-001` is much lighter than `PRC-AR-001` embedded Phase 1/2/4/5 templates. | Medium | An auditor may treat the standalone template as the complete intake/handoff artifact and miss richer required evidence. | Reconcile: either expand `TMPL-AR-001` or explicitly say it is the front-door intake only and `PRC-AR-001` handoff/threat model/pre-production templates are also required. |
| Metrics measure review completion and responsiveness more than evidence sufficiency. | Medium | `CM-002` can be green while the handoff package is weak. | Add or surface a quality metric: `% regulated ARs with complete handoff package and overlay evidence accepted`. |
| CUI overlay trace is good but jumps from standard to operational package/SSP/POA&M; first-time auditors may need a map. | Medium | CMMC/CUI assessors expect SSP/POA&M evidence quickly. | Add a regulated-architecture evidence checklist referencing SSP, POA&M, SPRS/CMMC readiness, CUI boundary, FedRAMP equivalency, and data-flow map. |

## Cross-Trace Findings

| Finding | Severity | Affected traces | Why it matters | Recommendation |
|---|---:|---|---|---|
| Evidence quality model is strong and reusable. | Strength | All | `AUD-001` gives auditors a clear way to reject weak evidence and accept strong evidence. | Preserve and cross-link more aggressively from procedures. |
| Record catalog is strong but not always surfaced in procedures. | Medium | All | `CAT-002` knows the record types, but procedure readers may not see the expected package up front. | Add `Records created` boxes to high-use procedures. |
| `TRC-001` is highly valuable but needs updates for newer operational procedures. | High | Access, architecture | Some traces rely on inference or omit runbooks/templates that now exist. | Update `TRC-001` as part of source rewrite phase. |
| Producer/owner/approver distinctions need an auditor-facing explanation. | Medium | Access, architecture | Control owner, process owner, evidence producer, evidence librarian, and approver can be different roles. | Add short role taxonomy to `PRC-AUD-001` or `CAT-002`. |
| Metrics exist for all three traces, but metric-to-record reproducibility should be explicit. | Medium | All | Auditors may ask how dashboard values are recalculated from source records. | Add metric source-record examples in `MTR-001` or procedure metric sections. |
| Improvement loop is strong in concept, but older references may say `IMPREG-001` is planned. | Low | All | `PRC-LL-001` metadata still labels `IMPREG-001` as planned even though it exists and is approved. | Clean up planned/status wording in `PRC-LL-001` during polish. |

## Auditor-Facing Evidence Chain Pattern

For each auditable control, CERG should make this chain easy to produce:

```text
Policy principle
  → CB-001 control ID and evidence expectation
  → TRC-001 trace row
  → governing standard requirement
  → operating procedure step
  → canonical role accountable
  → CAT-002 record type
  → AUD-001 evidence quality tier
  → MTR-001 metric and source record
  → PRC-LL-001 / IMPREG-001 improvement path if the control fails
```

The chain exists today for the tested controls, but it is clearest for vulnerability remediation and least obvious for composite workflows like regulated architecture review.

## H04 Acceptance Criteria Check

- Three full auditor traces included: yes.
- Traced policy statement: yes.
- Traced control baseline: yes.
- Traced standard requirement: yes.
- Traced procedure step: yes.
- Traced accountable role: yes.
- Traced record created: yes.
- Traced evidence quality rule: yes.
- Traced metric/dashboard appearance: yes.
- Traced improvement loop if failure occurs: yes.
- Identified evidence-chain weaknesses: yes.
