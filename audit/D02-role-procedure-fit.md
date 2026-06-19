# Task D02 Output: Test role descriptions against real procedures

## Scope Reviewed
- Files read:
  - `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
  - `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md`
  - `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md`
  - `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
  - `governance/CERG-GOV-CAT-002_Record_Catalog.md`
  - `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
  - `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
  - `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
  - `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
  - `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- Sections reviewed:
  - Selected JD §1 role summaries, §4 responsibilities, §8 KPIs, §10 success profiles, and document-control notes.
  - RAC-001 §6 process RACI, §7 role descriptions, and §8 scaling map.
  - CAT-002 §4 record catalog entries for project review, exposure, evidence, and incident records.
  - PRC-AR §2-9, §12, and §14 role/review/handoff/metrics sections.
  - PRC-VM §4-13 observation through metrics workflow.
  - PRC-AUD §3-10 evidence library, cadence, testing, audit intake, corrective action, metrics, and roles.
  - PLN-IR §2-11 authority, roles, lifecycle, notification, evidence, and exercises.
  - PRC-IR §1-3, §17-18, and sampled scenario structure.
- Files intentionally not reviewed:
  - Every standard that feeds the selected roles. D02 tested whether role descriptions connect to procedure work, not full standards coverage.
  - Per-role JDs outside the four selected test roles, except where D01 findings remain relevant.
  - HR/performance governance files referenced by JD KPI sections; D02 used operational procedures and MTR-001 as the source of work evidence.

## Method
- Steps performed:
  1. Selected one role from each pillar plus one adjacent role: Pre-production Reviewer, Exposure Management Lead, Evidence Librarian, and Incident Commander.
  2. Compared each role's JD summary and responsibilities to RAC-001 role/process assignments.
  3. Searched governance, procedures, plans, standards, and templates for exact role-name references.
  4. Traced each role into the procedures where it performs work.
  5. For each role, answered the D02 operational questions: Monday-morning work, records, decisions, non-decisions, evidence, handoffs, and SLA-miss consequence.
  6. Compared role-specific records to CAT-002 and role-specific metrics to MTR-001 / procedure metrics sections.
- Search terms or scripts used:
  - Exact role-name scan for `Pre-production Reviewer`, `Exposure Management Lead`, `Evidence Librarian`, and `Incident Commander` across `governance/`, `procedures/`, `plans/`, `standards/`, and `templates/`.
  - Targeted reads of PRC-AR, PRC-VM, PRC-AUD, PRC-IR, PLN-IR, CAT-002, MTR-001, and RAC-001.
  - `rg` scan for PRC-AUD metric names in MTR-001.
- Assumptions avoided:
  - Did not treat low mention count as failure by itself. A specialized role may be operationally clear with few references if the procedure path is strong.
  - Did not assume the role name must appear in every step. Procedure ownership can be clear through the document owner, RACI row, or named record owner.
  - Did not rewrite adjacent Incident Response ownership. D02 records where the role boundary is understandable or blurred.

## Role Day-in-the-Life Summaries

| Role | Monday-morning work | Records created or updated | Decisions it can make | Decisions it cannot make | Evidence produced | Handoffs | If SLA or due date is missed |
|---|---|---|---|---|---|---|---|
| Pre-production Reviewer | Review project intake/review queue, run architecture or pre-production checks, verify findings closed or accepted, assemble readiness/handoff package, recommend Ready / Ready-with-Acceptance / Not Ready. | Project Security Review Record; Architecture Review record; Pre-production checklist evidence; Production Handoff Package; Go-Live Risk Acceptance Packet where needed; finding dispositions. | Determines Engineering findings; recommends handoff disposition; signs go-live readiness from the Engineering review perspective. | Cannot accept residual business risk; cannot approve High/Critical acceptance; cannot substitute for CAB/change approval; cannot ignore regulatory overlays. | Completed checklist, finding closure evidence, scan/test evidence pointers, handoff sign-offs, accepted-risk references. | Project/Technical Lead for remediation; Risk reviewer for threat-model findings and scans; Governance overlay reviewers for CUI/BES/SOX; Engineering Pillar Leader and Business Owner for go-live; CAB for change conversation. | PRC-AR defines phase SLAs and MTR-001 defines AR/SR metrics, but local missed-SLA escalation is mostly implicit through metrics and pillar leadership. Phase 4 extensions are assigned to Risk Pillar Leader, which is a role-boundary anomaly. |
| Exposure Management Lead | Check exposure pipeline, triage observations past validation SLA, validate asset/condition/exposure path, classify exposures, drive treatment selection, report EM metrics. | Finding Record; Exposure Backlog Item; exposure pipeline state; validation evidence; SLA status; treatment/closure evidence; risk-acceptance request when SLA cannot be met. | Classifies observations into exposure states; starts SLA clock at classification; prioritizes treatment queue; escalates PPR and material exposures; reports posture. | Cannot patch or change systems without Engineering/asset owner action; cannot accept residual business risk; cannot waive PPR-tier exposure rules except where the OT/CIP path applies. | Scanner outputs with context, reachability evidence, classification rationale, verification evidence, EM-001 through EM-010 metrics. | Engineering/IT/OT teams for remediation; Business/Asset Owner for treatment accountability; Risk Register Owner for acceptance/exception tracking; CISO for immediate escalation triggers; IR team for incident-driven exposure context. | Strongest of the four tested roles. PRC-VM ties missed treatment SLA to PRC-RM risk acceptance and makes PPR-tier exposures ineligible for ordinary acceptance. MTR-001 reports SLA misses with/without controls. |
| Evidence Librarian | Check evidence calendar, collect/refetch scheduled evidence, ingest evidence with quality metadata, validate freshness and source, respond to audit evidence requests, chase producing owners. | Evidence Index Entry; evidence library entries; audit intake log updates; submitted-package archive; control test evidence; evidence deficiency/corrective-action records. | Accepts or rejects evidence against AUD-001 quality bar; organizes evidence by control/framework/request; identifies evidence gaps; preserves exact submitted set. | Cannot manufacture or alter evidence to satisfy an auditor; cannot decide technical remediation; cannot accept residual risk; cannot make regulatory/legal notification decisions. | Source exports, approved artifacts, review records, test results, hashes/chain-of-custody fields, submitted audit packages, evidence rejection rationale. | Engineering/Risk/Governance process owners for source evidence; compliance managers for framework-specific packages; Governance Pillar Leader for audit response; Risk Register Owner/control owners for findings and corrective actions. | PRC-AUD records due date/priority and evidence deficiencies, but the evidence/audit metric set is not actually defined in MTR-001 with IDs and data sources. Missed evidence work is conceptually tracked, but operational reporting is weaker than the JD implies. |
| Incident Commander | On activation, confirm incident, assign incident ID/severity, establish channel and timeline, convene IRT, direct containment/recovery decisions, coordinate executive/legal/communications decisions. | Incident Record; Incident Action Log; timeline; severity decisions; notification decision rationale; post-incident report/action items. | Single-decision authority during active response; sets/updates severity; approves containment, eradication, recovery sequencing; coordinates notification decisions with Legal/Governance/executives. | Not a CERG role; cannot be overruled by CERG workflows during active incident; does not own CERG post-incident risk register curation; should not be described as CERG's internal liaison. | Timeline, action log, decision rationale, communications facts, forensic/evidence preservation direction, post-incident review outputs. | SOC/Lead Investigator for triage; Engineering/Risk/Governance support roles; Legal/Communications/Executive Sponsor; Evidence Librarian/Risk Register Owner after incident for evidence and risk/control updates. | IR Plan defines response cadence by severity and exercise/plan cadences. PRC-IR maps P1-P4 to Sev 1-4. However, adjacent-role and CERG-support language is still blurred in the JD and IR body text. |

## Findings

### D02-F01 High Pre-production Reviewer scope is broader than its name and JD summary suggest
Affected files:
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Problem: The JD frames the Pre-production Reviewer primarily as the rotated role that owns the pre-production checklist and go-live readiness. PRC-AR §2 assigns `CERG - Pre-production Reviewer` broader work: conducting Engineering review, maintaining the review record, determining Engineering findings, and recommending handoff disposition. That reads like the main security architecture reviewer across the five-phase AR procedure, not only the Phase 4 reviewer.

Why it matters: A reader trying to staff the architecture review workflow may not know whether this role owns only Phase 4, all Engineering review records, or the entire Engineering side of architecture review. The procedure still functions, but the role title, JD, and procedure assignment force the reader to infer the boundary.

Evidence from corpus:
- JD-SECENG-008 §1: `owns the pre-production checklist and sign off on go-live readiness`.
- RAC-001 §6.1: Pre-production review and go-live readiness is R/A for `Pre-production Reviewer`.
- PRC-AR §2: `CERG - Pre-production Reviewer` conducts Engineering review, maintains the review record, determines Engineering findings, and recommends handoff disposition.
- PRC-AR phases include intake, architecture review, threat model, build-time engagement, pre-production, and production handoff.

Recommended action: Clarify either the role or the procedure. Option A: expand the JD summary to say that when assigned, the Pre-production Reviewer operates the Engineering review record from intake through go-live, with Phase 4 as the formal readiness gate. Option B: split PRC-AR local terminology into `Security Architecture Reviewer` for Phases 1-3 and `Pre-production Reviewer` for Phase 4-5, with the same person allowed to hold both roles in small teams.

Owner/workstream: Workforce / Architecture Review procedure.

### D02-F02 Medium Phase 4 extension authority points to Risk instead of the Engineering review owner
Affected files:
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`

Problem: PRC-AR §8.2 says Phase 4 Pre-Production Security Review extensions may be granted by the Risk Pillar Leader where evidence review requires additional subject matter expertise. The Phase 4 owner is otherwise an Engineering role, and RAC-001 assigns pre-production review/go-live readiness to Engineering / Pre-production Reviewer.

Why it matters: This is not a catastrophic authority conflict, but it is a role-fit surprise. If Engineering owns the review and readiness gate, a reader expects Engineering Pillar Leader or the assigned reviewer to own schedule exceptions, with Risk consulted for evidence or threat context. Assigning extension authority to Risk makes Risk appear to control an Engineering service-level commitment.

Evidence from corpus:
- RAC-001 §6.1: `Pre-production review and go-live readiness` is Engineering R/A, named to Pre-production Reviewer.
- PRC-AR §8.2: extensions may be granted by the Risk Pillar Leader.
- PRC-AR §2: Engineering Pillar Leader approves Engineering disposition and validates compensating controls.

Recommended action: Change extension authority to `Engineering Pillar Leader, after consultation with Risk where evidence review requires additional subject matter expertise`, or explain why Risk owns this specific extension decision.

Owner/workstream: Architecture Review / Role boundary cleanup.

### D02-F03 High Adjacent Incident Commander role is mostly clear, but the JD and IR documents still blur CERG liaison and ownership language
Affected files:
- `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Problem: The Incident Commander JD starts with a strong adjacent-role banner and correctly says the IC has single-decision authority during active incidents. But its core responsibilities include `Serve as the primary CERG liaison during incidents requiring cross-pillar coordination`, which reverses the model: CERG provides a liaison to the IR team; the IC is not CERG's liaison. IR plan/playbook body text also still assigns Governance ownership of notification clocks, exercises, and plan maintenance in places despite the adjacent-function banner.

Why it matters: This is the role-description version of the B02/C01 incident boundary issue. During an active incident, a reader must know instantly that the IC commands and CERG supports. Any wording that makes the IC sound like a CERG role, or makes Governance sound accountable for IR clocks/exercises, weakens that boundary.

Evidence from corpus:
- JD-ADJUNCT-001 §1: adjacent-role banner says IC belongs to standing IR team, not CERG.
- JD-ADJUNCT-001 §4.1: `Serve as the primary CERG liaison during incidents requiring cross-pillar coordination`.
- RAC-001 §6.4: incident response operations have CERG roles as Consulted, with no CERG Accountable role.
- PLN-IR-001 banner says CERG is not responsible for IR operations, notification clocks, or exercise management.
- PLN-IR-001 body assigns Governance ownership of notification clock tracking and several exercise/roster/retainer activities.

Recommended action: Replace the JD responsibility with `Receive CERG liaison support and direct CERG Engineering, Risk, and Governance support inputs during active incidents`. Then align PLN-IR/PRC-IR body text so Governance `supports regulatory mapping, evidence preservation, and liaison with Legal` while the standing IR team/IC owns notification-clock operations and exercises unless the IR team explicitly delegates a support task.

Owner/workstream: Adjacent function boundary / Incident Response role cleanup.

### D02-F04 High Audit and evidence metrics are named in PRC-AUD but not defined in MTR-001
Affected files:
- `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Problem: The Evidence Librarian role is procedurally strong, but its measurable operating loop is incomplete. PRC-AUD §9 says audit and evidence metrics are reported through MTR-001 and lists metric concepts such as evidence completeness, overdue evidence, audit requests open by due date, rejected evidence, control tests completed, deficient controls, corrective actions, and repeat findings. MTR-001 does not define those audit/evidence metrics with IDs, formulas, owners, data sources, refresh rates, or RAG thresholds.

Why it matters: The JD says the Evidence Librarian keeps evidence current, retrievable, and audit-ready. PRC-AUD says missed or weak evidence becomes a corrective action. Without MTR-001 metric definitions, a reader can understand the work but cannot see how the Evidence Librarian's queue, overdue items, rework, or audit response load become dashboard-visible operating facts.

Evidence from corpus:
- JD-GOVCOMP-006 §1: evidence exists, is current, and is retrievable.
- PRC-AUD §9 lists audit/evidence metrics and says they are reported through MTR-001.
- Exact scan found those PRC-AUD metric names in PRC-AUD only, not in MTR-001.
- MTR-001 has GV/CE metrics, but no audit/evidence metric family equivalent to EM, RM, TP, CM, or SR.

Recommended action: Add an `Audit and Evidence Metrics` family to MTR-001, likely AE-001 through AE-008, mirroring PRC-AUD §9: evidence completeness, overdue evidence, audit requests open by due date, rejected/reworked evidence, control tests on schedule, deficient controls by age, corrective actions closed on time, and repeat findings. Name Evidence Librarian or Governance Pillar Leader as owner as appropriate, and map each metric to its source record.

Owner/workstream: Governance metrics / Evidence operations.

### D02-F05 Medium Selected JDs still make Monday-morning work harder to read than the procedures do
Affected files:
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md`
- `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md`
- `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`
- Potentially all per-role JD files with the same generated format

Problem: The selected JDs contain useful role content, but §4.1 and §5.1 often compress multiple responsibilities into one long markdown list item separated by hyphens. The procedures are usually clearer than the JDs because procedures name steps, records, decisions, and owners. A reader can answer `what does this role do on Monday morning?`, but often only after leaving the JD and tracing into procedures.

Why it matters: D02 tests human role understanding. A JD should be the fast path to role comprehension. Long compound bullets make operational duties look like an abstract competency list rather than a set of repeatable jobs.

Evidence from corpus:
- JD-SECENG-008 §4.1 is a single bullet containing checklist maintenance, reviews, signoff, escalation, handoff, Risk coordination, and Governance coordination.
- JD-RISKOPS-001 §4.1 is a single bullet containing source operation, triage criteria, SLAs, metrics, remediation coordination, scanner tuning, OT-safe scanning, tooling, and IR support.
- JD-GOVCOMP-006 §4.1 is a single bullet containing evidence ownership, collection, curation, retention, audit support, calendar management, gap closure, procedure contribution, and compliance-manager partnership.
- A02 already identified this as a broader long-bullet readability issue across many JDs.

Recommended action: In the later JD rewrite pass, split each role's §4.1 into short duty bullets grouped under `Operate`, `Decide`, `Record`, `Report`, and `Hand off`. Add a short `Monday morning` sentence to the four exemplar roles first, then apply the pattern across all JDs if it works.

Owner/workstream: Workforce JD readability / G03 polish queue, with G02 section-level rewrite for affected exemplar roles.

## Positive Confirmations
- Exposure Management Lead is one of the strongest role-to-procedure fits in the corpus. PRC-VM gives a clear state model, records, SLA start point, treatment path, closure verification, metrics, and risk-acceptance boundary.
- Evidence Librarian is conceptually strong. PRC-AUD makes evidence a managed operating asset, defines evidence library structure, quality bar, retention, chain of custody, audit intake, and corrective action flow.
- Incident Commander has a strong top-level adjacent-role banner in the JD, PLN-IR, and PRC-IR. The high-level model is correct: IR commands; CERG supports.
- CAT-002 is valuable for D02 reader comprehension. It turns role work into named record types and evidence value, especially Project Security Review Record, Finding Record, Exposure Backlog Item, Evidence Index Entry, Incident Record, and Incident Action Log.
- RAC-001 §8 scaling guidance reinforces that role consolidation does not delete accountability, which helps small-team readers understand how these four roles can be held by fewer people without changing decision boundaries.

## Open Questions
- Should the Pre-production Reviewer be renamed or split from a broader `Security Architecture Reviewer` role, or is the intended model that the same rotated reviewer owns the full Engineering review record?
- Should Phase 4 review extensions be an Engineering decision with Risk consultation, or is there an intentional reason Risk Pillar Leader grants them?
- For adjacent incident roles, should CERG-hosted JDs describe the full IR job or only the CERG-facing interface to the IR job?
- Should audit/evidence metrics be a standalone MTR-001 metric family, or should they be folded under GV/CE metrics with explicit Evidence Librarian ownership?
- Should every JD get a short `Monday morning` operational summary, or should that live only in role reader paths/adoption guidance?

## Proposed Next Tasks
- D03: test whether the role boundaries above remain clear when a small team consolidates multiple hats into two, five, or eight people.
- G02: add rewrite queue entries for Pre-production Reviewer scope clarification, IR adjacent-role wording, PRC-AUD/MTR audit metrics, and JD operational-summary structure.
- G03: add polish queue entries for long compound JD bullets and local PRC-AR role label cleanup.
- Later source remediation: update MTR-001 with audit/evidence metrics before treating Evidence Librarian performance reporting as complete.
