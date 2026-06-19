# Task I02 Output: Prioritized Remediation Roadmap

## Purpose

This roadmap converts the A-H audit findings and I01 scorecard into an executable remediation sequence. It is a planning artifact only: no governed source files are rewritten here.

Execution principles:
- Fix authority contradictions before voice or examples.
- Prefer one-file edits where possible.
- Group cross-cutting changes only where editing one file without the others would create temporary contradiction.
- Validate after every source edit with `python3 tools/cerg-validate.py` and `python3 tools/cerg-integrity-check.py`.
- Regenerate machine-readable artifacts only where metadata, paths, inventory, classification, catalog, or machine-readable generation logic changes.

## Tier Summary

| Tier | Meaning | Count | Primary outcome |
|---|---:|---:|---|
| Tier 0 | Stop-the-line contradictions | 6 | Remove wrong authority, wrong role content, or materially conflicting execution rules. |
| Tier 1 | High-value conceptual clarifications | 10 | Make canonical sources, records, evidence, and routing unmistakable. |
| Tier 2 | Examples and reader-understanding improvements | 9 | Improve human comprehension without changing the model. |
| Tier 3 | Voice normalization | 6 | Apply CERG house voice after authority is stable. |
| Tier 4 | Polish | 7 | Safe, visible cleanup and low-risk formatting fixes. |

---

## Tier 0 — Stop-the-line contradictions

### T0-01 — Repair IR adjacent-function authority

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`; `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`; `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`; later `examples/day-in-the-life/README.md` Story 6 and `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md` if needed |
| Reason | OM and IR banners say standing IR team / Incident Commander owns incident response, notification-clock process, and exercises; IR bodies/footers assign some of that authority to CERG Governance/Risk. |
| Severity | Critical |
| Dependency | First source rewrite bundle. Edit in order: FLOW F-06 → PLN-IR → PRC-IR → Story 6/JD cleanup. |
| Estimated effort | Large, 3-5 file edits. |
| Owner/workstream | Adjacent Functions / IR boundary |
| Acceptance criteria | No source says or implies CERG owns incident command, incident declaration, regulatory notification-clock process, or IR exercise program. CERG Governance supports notification evidence/registers and cross-reference hygiene under Incident Commander/Legal direction. Metadata, document control, banners, roles, and flow language agree. |
| Machine-readable regen | No, unless metadata/status/owner fields change. If metadata owner/status changes, run `regenerate-machine-readable.py` and `regenerate-llm-index.py`. |

### T0-02 — Repair Detection Engineer and Vendor Risk Analyst JD body swap

| Field | Value |
|---|---|
| Files affected | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`; `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md` |
| Reason | Detection Engineer file contains Vendor Risk Analyst body content; Vendor Risk Analyst file contains Detection Engineer body content. |
| Severity | Critical |
| Dependency | Can proceed after T0-01 or in parallel on the same branch. Do not blindly rename files; preserve correct metadata/title and repair sections. |
| Estimated effort | Medium-large, 2 file edits plus careful validation. |
| Owner/workstream | Workforce / Role JDs |
| Acceptance criteria | Detection Engineer responsibilities, KSAs, success profile, and related docs are detection/ATT&CK/SIEM/coverage oriented. Vendor Risk Analyst content is TPRM/vendor tiering/evidence/SCCT oriented. No swapped role summaries remain. |
| Machine-readable regen | No if metadata/path/title unchanged. Consider `regenerate-llm-index.py` only if role summaries in the index must be refreshed. |

### T0-03 — Align risk acceptance and scoring authority

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`; `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`; `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`; `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`; later `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`, `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`, affected JDs and examples |
| Reason | RMF/PRC-RM duplicate scoring anchors differ; older templates and role text omit or weaken Business Owner acceptance. |
| Severity | Critical |
| Dependency | Establish RMF as canonical first; then PRC-RM; then templates; then role/example cleanup. |
| Estimated effort | Large, coordinated bundle. |
| Owner/workstream | Risk / Authority cleanup |
| Acceptance criteria | RMF remains canonical for scoring and acceptance. PRC-RM either points to RMF or exactly mirrors it with `RMF governs` note. Every residual-risk acceptance path requires Business Owner/Executive Sponsor consequence acceptance as appropriate. TMPL-RM-003 is retired or rewritten with Business Owner acceptance. |
| Machine-readable regen | No unless template/catalog status changes. If retiring or reclassifying TMPL-RM-003, update CAT-001 and run both regeneration scripts. |

### T0-04 — Repair FLOW F-04 closure and SLA conflict with PRC-VM

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`; check `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md` only for references |
| Reason | FLOW F-04 carries closure/SLA logic that duplicates or conflicts with PRC-VM's canonical exposure-state SLA model. |
| Severity | Critical/High |
| Dependency | After T0-03 if acceptance language is touched; otherwise can follow T0-01 FLOW edit. |
| Estimated effort | Medium, 1 primary file. |
| Owner/workstream | Flows / Exposure management |
| Acceptance criteria | FLOW F-04 describes trigger, handoff, records, evidence checkpoints, and closure shape. It points to PRC-VM §7.2 for canonical exposure clocks and does not publish a competing SLA table or closure rule. |
| Machine-readable regen | No. |

### T0-05 — Repair Story 8 Critical vendor exposure path

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/story-8-cerg-lite-maria.md` |
| Reason | Canonical CERG Lite story shows a Critical public-exploit vendor exposure handled like a routine exception, without explicit Business Owner/CISO/Executive Sponsor/PPR guardrails. |
| Severity | High/Critical because it teaches the wrong small-team pattern. |
| Dependency | After T0-03 acceptance authority is settled. Coordinate with Tier 2 small-team reader improvements. |
| Estimated effort | Medium, 1 file. |
| Owner/workstream | Examples / Small-team risk authority |
| Acceptance criteria | Either downgrade scenario to a non-PPR vendor gap suitable for time-bound exception, or keep Critical and show correct escalation, business acceptance, temporary controls, accelerated vendor/alternate-transfer decision, and no ordinary acceptance of PPR-tier exposure. |
| Machine-readable regen | No. |

### T0-06 — Fix machine-readable procedure pillar misclassification

| Field | Value |
|---|---|
| Files affected | `tools/regenerate-llm-index.py`; `machine-readable/cerg-llm-index.json` |
| Reason | LLM index classifies all procedures as `pillar: risk`, conflicting with source-document owners and operating accountability. |
| Severity | High for automation/LLM consumers. |
| Dependency | Can run after or in parallel with source authority cleanup. Best after T0-01/T0-03 if owner/status metadata changes. |
| Estimated effort | Medium, script + generated artifact. |
| Owner/workstream | Machine-readable / Authority cleanup |
| Acceptance criteria | Procedure pillar or new `primary_operating_pillar` reflects actual owner/accountability via metadata or explicit override table. Generated index no longer labels Engineering/Governance/External Interface procedures as Risk-only. |
| Machine-readable regen | Yes. Run `python3 tools/regenerate-llm-index.py`; run `regenerate-machine-readable.py` only if manifest metadata also changes. |

---

## Tier 1 — High-value conceptual clarifications

### T1-01 — Make CAT-002 the record-name authority and add alias discipline

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-CAT-002_Record_Catalog.md`; follow-on `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`; `governance/CERG-GOV-GEN-001_CERG_Glossary.md` |
| Reason | CAT-002, FLOW-001, GEN-001, examples, and templates use overlapping record definitions and local aliases. |
| Severity | High |
| Dependency | After T0-04 FLOW cleanup if touching same sections. |
| Estimated effort | Medium-large, start with CAT-002 only. |
| Owner/workstream | Records / Evidence |
| Acceptance criteria | CAT-002 states canonical record names, required fields, owner, trigger, and evidence value. It includes an alias column or alias guidance for common local names. FLOW and GEN defer to CAT-002 for record authority. |
| Machine-readable regen | No unless metadata/catalog entries change. |

### T1-02 — Convert FLOW-001 record definitions into flow-to-record crosswalk

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` |
| Reason | FLOW should show how work moves, not compete with CAT-002 as record catalog or with procedures as work instructions. |
| Severity | High |
| Dependency | After T1-01. |
| Estimated effort | Medium, 1 file. |
| Owner/workstream | Flows / Records |
| Acceptance criteria | FLOW primary-record sections use CAT-002 canonical names. Any local alias is visibly secondary. FLOW does not define record authority independently. |
| Machine-readable regen | No. |

### T1-03 — Update TRC-001 for access review and regulated architecture traces

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md` |
| Reason | Auditor path showed `PRC-AC-002` missing from AC-2/AC-6 trace and no curated composite trace for regulated architecture review. |
| Severity | High |
| Dependency | After T1-01 for record naming; can proceed before example rewrites. |
| Estimated effort | Medium, 1 file. |
| Owner/workstream | Traceability / Audit evidence |
| Acceptance criteria | AC-2/AC-6 rows cite `PRC-AC-002`. Add curated row/appendix for regulated architecture review showing composite controls, procedures, records, and evidence package. |
| Machine-readable regen | No. |

### T1-04 — Add privileged-access-review evidence checklist

| Field | Value |
|---|---|
| Files affected | `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`; possibly `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` |
| Reason | Evidence content exists but no single checklist tells producers what a privileged access review evidence package must include. |
| Severity | High |
| Dependency | After or alongside T1-03. |
| Estimated effort | Medium, 1-2 files. |
| Owner/workstream | Audit / Identity evidence |
| Acceptance criteria | Checklist includes population, scope, period, reviewer, reviewer authority, decisions, removals/modifications, exceptions, post-removal validation, timestamped exports, and evidence-library location. |
| Machine-readable regen | No. |

### T1-05 — Add OT/BES patch deferral route

| Field | Value |
|---|---|
| Files affected | `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`; `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md`; `governance/CERG-GOV-FRM-002_Framework_System_Map.md` |
| Reason | H02 found OT patch deferral content exists but requires inference; BES/non-BES and CIP deviation routing need a visible path. |
| Severity | High |
| Dependency | After T0-03 risk acceptance authority cleanup. |
| Estimated effort | Medium-large, 2-3 files. |
| Owner/workstream | OT / Exposure management |
| Acceptance criteria | PRC-VM has OT deferral decision table: non-BES OT, BES compliance unaffected, BES compliance impacted, emergency operational exception. FRM-002 has direct user-need row. CIP deviation path is surfaced. |
| Machine-readable regen | No. |

### T1-06 — Reconcile TMPL-AR-001 with PRC-AR-001 evidence package

| Field | Value |
|---|---|
| Files affected | `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`; `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` |
| Reason | H04 found standalone TMPL-AR-001 is much lighter than PRC-AR embedded Phase 1/2/4/5 artifacts. |
| Severity | High |
| Dependency | After T1-01 record naming. |
| Estimated effort | Medium, 1-2 files. |
| Owner/workstream | Architecture review / Evidence |
| Acceptance criteria | TMPL-AR-001 clearly says whether it is only front-door intake or the full evidence artifact. PRC-AR lists the complete closure package: intake, architecture decision, threat model, pre-production checklist, handoff package, risk acceptances, evidence links. |
| Machine-readable regen | No. |

### T1-07 — Refresh RAC-001 document/process RACI scope

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`; compare with `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` |
| Reason | RAC claims every CAT artifact should have RACI coverage, but newer artifacts appear missing; local RACI repetition creates drift. |
| Severity | High |
| Dependency | After T0-03 authority language. |
| Estimated effort | Large if fully refreshed; medium if scope rule is changed. |
| Owner/workstream | Governance / RACI maintenance |
| Acceptance criteria | RAC either covers current CAT-001 inventory or explicitly makes CAT-001 metadata authoritative for document ownership and limits RAC to process RACI. Local role sections defer to RAC. |
| Machine-readable regen | No unless catalog metadata changes. |

### T1-08 — Add Business Owner / System Sponsor reader path

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`; possibly `governance/CERG-GOV-FRM-002_Framework_System_Map.md` |
| Reason | H03 found business accountability is strong but non-security owners lack a dedicated front door. |
| Severity | High |
| Dependency | After T0-03. |
| Estimated effort | Small-medium, 1-2 files. |
| Owner/workstream | Reader paths / Business comprehension |
| Acceptance criteria | Path tells Business Owner what they decide, what Security decides, how to sponsor SaaS/project/vendor/risk decisions, and where risk acceptance/funding/evidence decisions appear. |
| Machine-readable regen | No. |

### T1-09 — Add business-facing decision boxes to high-use templates

| Field | Value |
|---|---|
| Files affected | `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`; `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`; `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`; `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md`; possible `templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md` |
| Reason | H03 found business users need explicit `approve/decline/no-action` consequences. |
| Severity | High |
| Dependency | After T0-03 and T1-06. |
| Estimated effort | Medium, multiple small template edits. |
| Owner/workstream | Templates / Business comprehension |
| Acceptance criteria | Each business-facing template includes: decision requested, if approve, if decline, if no action by date, Security role, Business Owner role, review/expiration. |
| Machine-readable regen | No. |

### T1-10 — Add control funding decision brief pattern

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`; `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`; optional new template if author approves later |
| Reason | H03 found funding decisions are surfaced in COG/MTR but not packaged as `fund/defer/accept/avoid`. |
| Severity | Medium/High |
| Dependency | After T0-03. May require author decision on whether to add a new template. |
| Estimated effort | Medium; large if new governed template is created. |
| Owner/workstream | Business decision support / Metrics |
| Acceptance criteria | A funding ask includes decision needed, affected process, options with cost/time/risk reduction, consequence of no decision, required approver, and review date. |
| Machine-readable regen | If new template is added, yes: update CAT-001, run both regeneration scripts. If only section text changes, no. |

---

## Tier 2 — Examples and reader-understanding improvements

### T2-01 — Repair Story 4 `Risk accepts` wording

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/README.md` Story 4 |
| Reason | Story says Risk accepts residual risk, conflicting with RMF/PRC-RM. |
| Severity | High |
| Dependency | After T0-03. |
| Estimated effort | Small, 1 local rewrite. |
| Owner/workstream | Examples / Risk authority |
| Acceptance criteria | Story says Risk documents/recommends/validates; Business Owner accepts consequence; Governance records. |
| Machine-readable regen | No. |

### T2-02 — Repair Story 6 IR handoff

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/README.md` Story 6 |
| Reason | Story blurs vendor incident triage and internal incident declaration authority. |
| Severity | High |
| Dependency | After T0-01. |
| Estimated effort | Medium, 1 story rewrite. |
| Owner/workstream | Examples / IR boundary |
| Acceptance criteria | Vendor Risk Analyst/Risk triages third-party exposure; Incident Commander/standing IR team declares or declines incident status; Governance supports regulatory mapping/evidence, not command. |
| Machine-readable regen | No. |

### T2-03 — Repair Story 10 new-CISO authority language

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/story-10-new-ciso-90-days.md` |
| Reason | H01 found Story 10 is a strong leadership story but teaches stale CISO-centered risk-acceptance language. |
| Severity | High |
| Dependency | After T0-03. |
| Estimated effort | Medium, 1 file. |
| Owner/workstream | Examples / CISO path |
| Acceptance criteria | Story distinguishes CISO cybersecurity approval/oversight from Business Owner/Executive Sponsor consequence acceptance. |
| Machine-readable regen | No. |

### T2-04 — Add evidence-request story or expand Story 3

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/README.md` Story 3 or new standalone example under `examples/day-in-the-life/` |
| Reason | H02/H04 found evidence paths are strong but need a worked example where evidence is rejected and repaired. |
| Severity | Medium |
| Dependency | After T1-04 and MTR audit metric cleanup if metric IDs are used. |
| Estimated effort | Medium if expanding Story 3; large if adding standalone file. |
| Owner/workstream | Examples / Evidence training |
| Acceptance criteria | Story shows audit intake, bad evidence rejection, producer correction, evidence library update, corrective action/improvement if systemic, and metric closure. |
| Machine-readable regen | If adding a new governed/example file tracked in catalog, update CAT-001 and run both scripts. If only editing README, no. |

### T2-05 — Add OT maintenance-window patch deferral story

| Field | Value |
|---|---|
| Files affected | New or existing `examples/day-in-the-life/` story |
| Reason | E02/H02 found OT deferral is judgment-heavy and lacks a canonical story. |
| Severity | Medium |
| Dependency | After T1-05. |
| Estimated effort | Large if new standalone story. |
| Owner/workstream | Examples / OT regulated operations |
| Acceptance criteria | Story shows OT operational priority, BES/non-BES decision, compensating controls, CIP deviation where needed, Business Owner/CISO authority, evidence, metrics, and review date. |
| Machine-readable regen | Yes if adding a new cataloged file; no if embedding in existing README without catalog change. |

### T2-06 — Add direct FRM-002 practitioner navigation rows

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-FRM-002_Framework_System_Map.md` |
| Reason | H02 found direct rows missing for exception/acceptance, access review evidence, third-party assessment, and OT patch deferral. |
| Severity | Medium/High |
| Dependency | After T1-03/T1-05 where paths are settled. |
| Estimated effort | Small, 1 file. |
| Owner/workstream | Navigation / Practitioner comprehension |
| Acceptance criteria | §5 includes direct rows with start document and follow-on template/procedure for each task. |
| Machine-readable regen | No. |

### T2-07 — Add first three CISO decisions callout

| Field | Value |
|---|---|
| Files affected | `START-HERE.md`; possibly `README.md` |
| Reason | H01 found first-hour path needs decision compression for CISO. |
| Severity | Medium |
| Dependency | After adoption scope wording T2-08 if same section. |
| Estimated effort | Small, 1 file. |
| Owner/workstream | Front-door / CISO comprehension |
| Acceptance criteria | Front door names first three decisions: readiness, adoption path/overlays, role/authority map for first 90 days. |
| Machine-readable regen | No. |

### T2-08 — Clarify MVC versus full operating spine

| Field | Value |
|---|---|
| Files affected | `START-HERE.md`; `governance/CERG-GOV-FRM-002_Framework_System_Map.md`; possibly `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md` |
| Reason | H01 found new CISO may confuse MVC minimum with full operating spine/adoption aids. |
| Severity | Medium |
| Dependency | None, but best after T2-07. |
| Estimated effort | Medium, 2-3 files. |
| Owner/workstream | Adoption / CISO comprehension |
| Acceptance criteria | MVC is described as the minimum governed operating spine; FRM/CAT/IMP reader aids are visible as adoption support, not optional confusion. |
| Machine-readable regen | No. |

### T2-09 — Add exact metric closure to stories

| Field | Value |
|---|---|
| Files affected | `examples/day-in-the-life/README.md`; `examples/day-in-the-life/story-8-cerg-lite-maria.md`; `examples/day-in-the-life/story-9-f-01-control-intent.md`; `examples/day-in-the-life/story-10-new-ciso-90-days.md` |
| Reason | E01 found stories often say metrics update generically rather than naming MTR IDs/source records. |
| Severity | Medium |
| Dependency | After MTR-001 cleanup in T1/T3 if metric IDs are added or repaired. |
| Estimated effort | Medium, several local edits. |
| Owner/workstream | Examples / Metrics traceability |
| Acceptance criteria | Each story's operational outputs include exact MTR metric IDs where they exist, or explicitly says metric is planned if not yet defined. |
| Machine-readable regen | No. |

---

## Tier 3 — Voice normalization

### T3-01 — Standardize document-control owner prose

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`; later broad standards/procedures/plans/templates/JDs |
| Reason | F03 found repeated `is responsible for` boilerplate weakens owner-centered voice. |
| Severity | Medium |
| Dependency | After authority cleanup so boilerplate does not preserve wrong owners. |
| Estimated effort | Medium to define pattern; large to apply corpus-wide. |
| Owner/workstream | Style / Document control |
| Acceptance criteria | STY-001 defines preferred document-control sentence patterns using `owns`, `runs`, `routes`, `approves`, `records`. Pilot applied to high-visibility documents first. |
| Machine-readable regen | No unless metadata fields change. |

### T3-02 — Replace vague applicability language in front-door adoption text

| Field | Value |
|---|---|
| Files affected | `START-HERE.md`; adoption docs using `where applicable` as scope logic |
| Reason | F03 found `where applicable` and `as needed` weaken adoption instructions when they decide scope. |
| Severity | Medium |
| Dependency | After T2-08. |
| Estimated effort | Small-medium. |
| Owner/workstream | Style / Adoption clarity |
| Acceptance criteria | Scope-dependent instructions name who decides applicability and where the decision is recorded. |
| Machine-readable regen | No. |

### T3-03 — Normalize `coordinate/support` verbs at decision points

| Field | Value |
|---|---|
| Files affected | High-use examples and procedures first: `examples/day-in-the-life/README.md`; `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`; `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` |
| Reason | F03 found `coordinates` can hide the actual record, handoff, or decision. |
| Severity | Medium |
| Dependency | After Tier 0 authority fixes. |
| Estimated effort | Medium. |
| Owner/workstream | Style / Operational voice |
| Acceptance criteria | At decision points, prose uses action verbs: routes, records, validates, approves, rejects, escalates, opens, closes, updates. `Coordinate` remains only for non-authority logistical collaboration. |
| Machine-readable regen | No. |

### T3-04 — Thin per-role JD dense/generated sections

| Field | Value |
|---|---|
| Files affected | Per-role JDs under `roles/jf-*/*.md`; start after T0-02 with affected role family |
| Reason | A02/F03/G01 found long bullets and dense competency/management sections reduce readability. |
| Severity | Medium |
| Dependency | After T0-02 and role authority cleanup. |
| Estimated effort | Large, batch pattern but one file per commit if source edits proceed. |
| Owner/workstream | Workforce / JD readability |
| Acceptance criteria | JD sections remain complete but scannable; long multi-clause bullets are split; generated content does not drown role-specific Monday-morning work. |
| Machine-readable regen | No unless role metadata/title/path changes. |

### T3-05 — Add workforce system map

| Field | Value |
|---|---|
| Files affected | `roles/CERG-GOV-JF-001_Job_Families_Overview.md` or a new workforce map section in existing workforce overview |
| Reason | G01 found workforce architecture is powerful but heavy; readers need to know which workforce artifact answers which question. |
| Severity | Medium |
| Dependency | After D01/JF-001 role list fix. |
| Estimated effort | Medium. |
| Owner/workstream | Workforce / Structural clarity |
| Acceptance criteria | A single section maps OM/RAC/JF/JA/CMP/PERF/TRN/SUCC/ONB/WFP/JDs to reader questions. |
| Machine-readable regen | No unless new file is added. If new governed file is added, update catalog and regenerate. |

### T3-06 — Add business/auditor plain-language glossary callouts

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-GEN-001_CERG_Glossary.md`; high-use templates; possibly `FRM-002` |
| Reason | H03 found terms like CUI, CIP, POA&M, CUEC, SCCT, APC, E2/E3 create friction for non-security readers. |
| Severity | Medium |
| Dependency | After record-name cleanup T1-01. |
| Estimated effort | Medium. |
| Owner/workstream | Voice / Business-reader comprehension |
| Acceptance criteria | First-use expansions or short glossary callouts exist in business-facing forms and paths; GEN remains the canonical glossary. |
| Machine-readable regen | No. |

---

## Tier 4 — Polish

### T4-01 — Fix SLC-001 malformed table rows

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` |
| Reason | G03 identified malformed leading `||` rows in a visible governance table. |
| Severity | Low |
| Dependency | None. |
| Estimated effort | Small, safe exact fix. |
| Owner/workstream | Polish |
| Acceptance criteria | Table renders correctly and validator passes. |
| Machine-readable regen | No. |

### T4-02 — Fix FRM-001 duplicate commas

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-FRM-001_CERG_Framework.md` |
| Reason | G03/H01 identified visible `NERC-CIP,,` and `800-171,,` in CISO-facing spine document. |
| Severity | Low |
| Dependency | None. |
| Estimated effort | Small, safe exact fix. |
| Owner/workstream | Polish |
| Acceptance criteria | Duplicate commas removed, no other text changed. |
| Machine-readable regen | No. |

### T4-03 — Fix glossary role-name typo

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-GEN-001_CERG_Glossary.md` |
| Reason | G03 identified `Policy and Standards Manager` should be `Policy & Standards Manager`. |
| Severity | Low |
| Dependency | After record/role terminology cleanup if nearby sections are edited. |
| Estimated effort | Small. |
| Owner/workstream | Polish / Terminology |
| Acceptance criteria | Canonical role name matches OM/RAC. |
| Machine-readable regen | No. |

### T4-04 — Fix PRC-IR Section 11 stale reference

| Field | Value |
|---|---|
| Files affected | `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` |
| Reason | G03 identified `Section 11` should be `Section 17`, conditional on no prior renumbering. |
| Severity | Low now; may be absorbed by T0-01/T0-03 IR rewrites. |
| Dependency | After T0-01 if PRC-IR is rewritten first. |
| Estimated effort | Small. |
| Owner/workstream | Polish / IR |
| Acceptance criteria | Cross-reference points to correct section after IR rewrite/renumbering. |
| Machine-readable regen | No. |

### T4-05 — Update START-HERE story count

| Field | Value |
|---|---|
| Files affected | `START-HERE.md` |
| Reason | E01/H01 found START-HERE says seven stories while examples catalog has ten. |
| Severity | Low/Medium because front-door visible. |
| Dependency | If story inventory changes in Tier 2, apply after example strategy decision; otherwise can fix immediately. |
| Estimated effort | Small. |
| Owner/workstream | Polish / Examples navigation |
| Acceptance criteria | START-HERE story count matches examples inventory. |
| Machine-readable regen | No. |

### T4-06 — Clean MTR-001 visible table/section defects

| Field | Value |
|---|---|
| Files affected | `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` |
| Reason | H01/G02 found CISO-facing defects: revision-history row inside metric table, empty Detection Metrics section, possible malformed data-source rows. |
| Severity | Medium despite polish tier because CISO-facing. |
| Dependency | Before using MTR externally; coordinate with any Tier 1 metric additions. |
| Estimated effort | Medium. |
| Owner/workstream | Metrics / Polish |
| Acceptance criteria | Metric dictionary tables contain only metric rows; Detection Metrics section has defined metrics or is explicitly planned; malformed rows fixed. |
| Machine-readable regen | No. |

### T4-07 — Remove stale `IMPREG-001 planned` wording in PRC-LL metadata

| Field | Value |
|---|---|
| Files affected | `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md` |
| Reason | H04 found PRC-LL metadata still labels IMPREG-001 as planned even though the document exists and is approved. |
| Severity | Low |
| Dependency | None. |
| Estimated effort | Small. |
| Owner/workstream | Polish / Improvement loop |
| Acceptance criteria | Supporting document reference no longer says planned; relationship to IMPREG-001 is current. |
| Machine-readable regen | No unless metadata table fields materially change in a way manifests track. |

---

## Recommended Execution Order

1. T0-01 IR authority cleanup.
2. T0-02 Detection/Vendor JD repair.
3. T0-03 RMF/PRC-RM/template authority cleanup.
4. T0-04 FLOW F-04 cleanup.
5. T1-01/T1-02 record-name authority and FLOW crosswalk.
6. T1-03/T1-04 auditor evidence trace improvements.
7. T1-05 OT/BES deferral route.
8. T0-05 Story 8 repair, then T2 example authority repairs.
9. T1-06/T1-09 template and business-reader improvements.
10. T1-07 RAC refresh and workforce map/readability tasks.
11. Tier 3 voice normalization.
12. Tier 4 polish, except visible safe fixes may be applied earlier if not overlapping active rewrites.

## Cross-Cutting Bundles

| Bundle | Includes | Why grouped |
|---|---|---|
| IR Boundary Bundle | T0-01, T2-02, T4-04 | Prevents incident ownership contradictions across flow, plan, playbook, and story. |
| Risk Authority Bundle | T0-03, T2-01, T2-03, T1-09 | Prevents business-risk acceptance drift across RMF, procedure, templates, and examples. |
| Workforce Repair Bundle | T0-02, T1-07, T3-04, T3-05 | Fixes incorrect role content before improving readability. |
| Record/Evidence Bundle | T1-01, T1-02, T1-03, T1-04 | Makes CAT/TRC/FLOW/AUD agree before examples/templates reference records. |
| Practitioner Navigation Bundle | T1-05, T2-06, T2-08 | Reduces time-to-understanding for weekly operational tasks. |
| CISO-Facing Polish Bundle | T4-02, T4-05, T4-06, T2-07 | Improves first-hour credibility. |

## I02 Acceptance Criteria Check

- Roadmap tiers included: yes, T0 through T4.
- Each remediation item has title, files, reason, severity, dependency, effort, owner/workstream, acceptance criteria, and machine-readable regeneration note: yes.
- Roadmap can be executed one file at a time where possible: yes; cross-cutting bundles state ordering.
- Cross-cutting changes explicitly grouped: yes.
- No vague `improve clarity` items without exact targets: yes.
