# Task H02 Output: Practitioner path comprehension test

## Scope Reviewed
- Starting navigation file:
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md` §4-§5
- Workflow files followed from `FRM-002` user-need navigation:
  - `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
  - `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
  - `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
  - `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
  - `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
  - `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`
  - `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
  - `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
  - `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
  - `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md`
- Workflow files used only after a gap became visible:
  - `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`
  - `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md`
  - `plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md` references through OT/CIP routing
- Files intentionally not exhaustively reviewed:
  - Full standards corpus, full role corpus, full control baseline. H02 tests whether a practitioner can perform this week's task without reading the entire corpus.

## Method
- For each workflow, I started at `FRM-002` §5 Navigation by User Need.
- I followed only documents directly named by the relevant navigation row or by the first procedure reached.
- I recorded where a practitioner would lack:
  - a next step;
  - a primary owner;
  - a template or record;
  - a decision rule;
  - an example showing the work end to end.
- I classified each gap as navigation, procedure content, role clarity, or missing example.

## Executive Summary

A practitioner can execute most common work from `FRM-002` without reading the entire corpus, especially SaaS intake, vulnerability triage, TPRM, and risk exceptions. The strongest paths have three features: an obvious `FRM-002` entry row, a procedure with role/step tables, and a named template.

The weak paths are not caused by missing subject-matter content. They are caused by routing. Privileged access evidence and OT patch deferral both have good authoritative material, but the practitioner has to infer which operational document to open after starting from `FRM-002`. Risk exception routing is conceptually strong inside `PRC-RM-001`, but `FRM-002` lacks a direct user-need row for someone who simply needs to request an exception this week.

Top time-to-understanding improvements:

1. Add `FRM-002` §5 rows for `Request an exception or risk acceptance`, `Respond to an access review evidence request`, `Assess a third party or vendor`, and `Defer an OT patch or BES remediation`.
2. Add small "Use this form when..." callouts for `TMPL-RM-002` versus `TMPL-RM-004` in front-door navigation, not only inside `PRC-RM-001`.
3. Create or cross-link a privileged-access-review evidence mini-path: `AUD-001` / `PRC-AUD-001` → `PRC-AC-002` §5 → evidence worksheet → evidence library.
4. Add an OT patch deferral routing card: `PRC-VM-001` → `STD-OT-001` §4.2/§11 → `PRC-RM-001` §7.5 → CIP deviation path for BES.
5. Add one missing story or worked example for an evidence request that fails/returns for rework and one for OT maintenance-window patch deferral.

## Workflow 1 — Architecture Review for SaaS

### Starting point from `FRM-002`
- User need: `Review a new system or SaaS`.
- Start with: `PRC-AR-001`.
- Then use: `TMPL-AR-001`, `PRC-TPRM-001`.

### Practitioner path
1. Open `PRC-AR-001` to understand intake, routing, review steps, threat modeling triggers, findings, and go-live conditions.
2. Use `TMPL-AR-001` to collect the project summary, data scope, SaaS/vendor trigger, identity/logging/deployment details, and routing decisions.
3. If a vendor or subprocessors are involved, open `PRC-TPRM-001` for cyber vendor tiering, evidence-by-tier, SaaS catalog status, inherited controls, and contract/security clause handling.
4. Route findings to remediation, exception, or risk acceptance using the risk process when the SaaS cannot meet requirements.

### Can the practitioner proceed?
Yes. This is one of the clearest paths. `FRM-002` names the correct procedure and template, and the template asks enough early questions to avoid late security surprise.

### What is clear
- Next step: submit a project/security intake using `TMPL-AR-001`.
- Owners: business owner and technical owner provide facts; Engineering leads architecture review; Risk joins for threat/risk analysis; Governance confirms evidence and regulated scope.
- Template: `TMPL-AR-001` is obvious from `FRM-002`.
- Decision rules: SaaS, vendors, data classification, privileged access, APIs, cloud, AI, OT, and regulated scope all trigger routing.
- Records: project security review record, findings, exceptions/risk records where needed, vendor assessment evidence where a third party is involved.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| SaaS-specific procedure sequence is spread across `PRC-AR-001`, `TMPL-AR-001`, and `PRC-TPRM-001`. | Navigation | A practitioner can follow it, but may not know when to run TPRM in parallel versus after architecture review. | Add a short SaaS routing note in `FRM-002`: "For SaaS, run architecture review and TPRM in parallel after intake." |
| The end-to-end SaaS record package is implicit. | Procedure content | The practitioner can infer the records, but the expected package is not stated as a single checklist. | Add a `SaaS review closure package` checklist: intake, architecture decision, vendor tier/evidence, shared responsibility notes, go-live conditions, exceptions/accepted risks, evidence library link. |
| No promoted SaaS-specific worked example is named from this path. | Missing example | The procedure is executable but an example would reduce first-time hesitation. | Promote or add a short SaaS intake story showing Engineering/Risk/Governance handoff and TPRM parallelization. |

## Workflow 2 — Critical Vulnerability Triage

### Starting point from `FRM-002`
- User need: `Start exposure management`.
- Start with: `PRC-VM-001`.
- Then use: `RMF-001`, `CAT-002`.

### Practitioner path
1. Open `PRC-VM-001`.
2. Treat scanner output as observations, not automatically as risk.
3. Validate reachability, exploitability, asset criticality, KEV status, compensating controls, and crown-jewel or regulated scope.
4. Classify into the exposure state model and treatment path.
5. If remediation cannot meet SLA, route to `PRC-RM-001` for exception or risk acceptance.
6. Use `CAT-002` to identify the expected records and `MTR-001`/procedure metrics for backlog, SLA, and exposure posture reporting.

### Can the practitioner proceed?
Yes. `PRC-VM-001` is operationally strong and teaches the important rule: a critical CVSS finding is not automatically a critical exposure until context is validated.

### What is clear
- Next step: validate the observation before calling it an exposure.
- Owner: Risk / Exposure Management Lead owns triage and SLA clock; Engineering owns remediation; Governance owns evidence/metrics/escalation integrity.
- Decision rules: reachability, exploitability, KEV, critical asset scope, compensating controls, operational impact, and regulatory context.
- Exception route: `PRC-VM-001` §11 points to risk acceptance / exceptions when treatment cannot meet SLA.
- Metrics: exposure posture, triage backlog, SLA misses, KEV reachable path, and patch hygiene.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| `FRM-002` §5 points to `PRC-VM-001` but not to `FLOW-001` F-04, even though §4 has a critical vulnerability worked mini-example. | Navigation | A new practitioner may miss the cross-pillar closure model and focus only on VM mechanics. | Add `FLOW-001` F-04 as a secondary link in the exposure management row. |
| Record/template path for findings is less obvious than the technical triage path. | Navigation / procedure content | The practitioner understands what to decide but may not immediately know which record names and evidence artifacts prove closure. | Add a `records created` box near the start of `PRC-VM-001`: observation, finding/exposure record, remediation record, exception or risk acceptance, closure evidence. |
| SLA/closure language has known drift with `FLOW-001` F-04. | Procedure content | A practitioner may see different closure/exception language if they open flow and procedure side by side. | Resolve under the existing G02 `FLOW F-04 cleanup` task. |

## Workflow 3 — Risk Exception Request

### Starting point from `FRM-002`
- Closest user need: `Stand up risk management`.
- Start with: `RMF-001`.
- Then use: `PRC-RM-001`, `TMPL-RM-001`.
- Actual practitioner need: request an exception or risk acceptance this week.

### Practitioner path
1. `FRM-002` does not have a direct "request exception" row, so the practitioner must infer the risk-management path.
2. Open `PRC-RM-001`.
3. Use §7.1 to decide between:
   - Security Exception: control or standard cannot be met as written → `TMPL-RM-002`.
   - Risk Acceptance: residual business risk is being accepted after treatment decision → `TMPL-RM-004`.
4. If unsure, route as Security Exception for triage by the Risk Register Owner.
5. Engineering reviews compensating controls; Risk scores residual risk; Governance routes approval; Business / Asset Owner signs residual risk where applicable.

### Can the practitioner proceed?
Yes after opening `PRC-RM-001`, but the path from `FRM-002` is too indirect for a weekly task. The procedure itself is strong; front-door navigation is the weak point.

### What is clear
- Decision rule: exception is deviation from a requirement; risk acceptance is acceptance of residual business risk.
- Templates: `TMPL-RM-002` and `TMPL-RM-004` are explicitly named in `PRC-RM-001`.
- Owners: requester submits; Engineering reviews compensating controls; Risk scores; Governance routes; Business / Asset Owner owns business consequence; CISO/Executive Sponsor approve above thresholds.
- Escalation: expired exceptions auto-create findings and escalate through the warning chain.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| No direct `FRM-002` row for "Request an exception or risk acceptance." | Navigation | A practitioner with a concrete exception task may not think to start with "stand up risk management." | Add a user-need row: `Request an exception or accept residual risk` → `PRC-RM-001` §7 → `TMPL-RM-002` / `TMPL-RM-004`. |
| `TMPL-RM-001` appears in the `FRM-002` risk row, but the exception-specific forms are not visible until inside `PRC-RM-001`. | Navigation | The first visible template is the register template, not the request form the practitioner needs. | Add the two request forms in the `Then use` column. |
| Some adjacent documents still carry older CISO-centered acceptance language. | Procedure content / consistency | The practitioner could learn the correct rule in `PRC-RM-001` and then see stale language elsewhere. | Address under the existing RMF/PRC-RM alignment and Story 10 repair tasks. |

## Workflow 4 — Privileged Access Review Evidence Request

### Starting point from `FRM-002`
- Closest user need: `Prepare for audit`.
- Start with: `AUD-001`.
- Then use: `PRC-AUD-001`, regulator operational package.
- Actual practitioner need: produce evidence for a privileged access review request.

### Practitioner path
1. Open `AUD-001` to learn what evidence quality requires.
2. Open `PRC-AUD-001` for audit intake, response rules, evidence submission, findings, corrective actions, and roles.
3. From the audit request text, infer that the control operation lives in access management.
4. Locate `PRC-AC-002` §5 for access review/recertification and §6 for PAM.
5. Collect privileged access review output: population, reviewer, cadence, decisions, removals/modifications, completion date, remediation follow-up, and evidence storage link.
6. Package through Governance; preserve the exact submitted set.

### Can the practitioner proceed?
Partially. The evidence quality and audit response documents are excellent, but `FRM-002` does not route the practitioner from an evidence request to the control-specific procedure. A knowledgeable practitioner will find `PRC-AC-002`; a new practitioner may stop at generic evidence rules and still not know what exact access-review artifact to request.

### What is clear
- Evidence quality: `AUD-001` clearly rejects screenshots, emails saying "done," undefined samples, and policy text without proof of operation.
- Audit intake: `PRC-AUD-001` clearly requires Governance intake, scope, due date, requested evidence, owner, producing roles, submission status, and preserved submitted package.
- Access review operation: `PRC-AC-002` §5 clearly defines cadence, workflow, recertification decisions, removal SLA, audit logs, and anti-rubber-stamp controls.
- Owner split: Evidence Librarian operates evidence library and package; Identity Engineer / IAM produces access evidence; Governance submits; control/system owners correct deficiencies.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| `FRM-002` audit row does not point to the control procedure needed for common evidence requests. | Navigation | The practitioner learns what good evidence is, but not where privileged access review evidence comes from. | Add examples in the audit row: privileged access review → `PRC-AC-002` §5; vulnerability SLA → `PRC-VM-001`; architecture review → `PRC-AR-001`. |
| No visible privileged-access evidence mini-checklist. | Procedure content | A producer may submit incomplete evidence: no population, no period, no removals, no reviewer, no storage location. | Add a checklist in `PRC-AUD-001` or `PRC-AC-002`: population, scope, period, reviewers, decisions, exceptions, remediation, timestamps, evidence library path. |
| `TMPL-AUD-001` exists but is not surfaced in the `FRM-002` audit row. | Navigation | The practitioner may miss the worksheet that can structure the response. | Add `TMPL-AUD-001` to `FRM-002` `Prepare for audit` row. |
| No story shows an evidence request moving from audit intake to control owner to evidence package. | Missing example | The concept is clear, but the first-time practitioner lacks an operational story for handoffs and rejection/rework. | Add or promote an "access review evidence request" story, ideally with one bad-evidence rejection. |

## Workflow 5 — Third-Party Assessment

### Starting point from `FRM-002`
- Indirect user need: `Review a new system or SaaS` points to `PRC-TPRM-001` as the secondary procedure.
- There is no direct user-need row for `Assess a vendor / third party`.

### Practitioner path
1. Open `PRC-TPRM-001`.
2. Confirm CERG owns the cyber slice, not vendor management overall.
3. Accept business/vendor tier from Procurement/ERM as input.
4. Apply cyber-specific tier adjustments: privileged access, Restricted/CUI/BCSI data, OT/BES interaction, recent breach, inadequate evidence, SOX relevance, deployed software with elevated privileges, non-US access.
5. Collect evidence by tier using the evidence table.
6. For SaaS, update/consult Approved Provider and SaaS Catalog and shared-responsibility expectations.
7. Use `TMPL-TPRM-001` for questionnaire/assessment structure.
8. Route residual vendor cyber risk through `PRC-RM-001` if the business wants to proceed despite unresolved risk.

### Can the practitioner proceed?
Yes, if they know to open `PRC-TPRM-001`. The procedure is strong, practical, and clear about CERG's boundary with Procurement, ERM, BR, and Legal. The weak point is discoverability from `FRM-002` when the user need is a vendor assessment rather than a SaaS architecture review.

### What is clear
- Owner: Vendor Risk Analyst owns cyber assessment; Procurement owns vendor onboarding/contracts; ERM owns enterprise vendor tier; Business Owner owns vendor relationship and residual risk; Legal owns negotiation.
- Decision rules: tiering, cyber-specific adjustments, evidence-by-tier, vendor type differences, control-level honesty, MSP/MSSP hard requirements.
- Template: `TMPL-TPRM-001` exists and supports assessment.
- Records: vendor assessment, tier adjustment, approved provider/catalog entry, evidence package, residual risk record where needed.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| No direct `FRM-002` row for third-party assessment. | Navigation | A practitioner may find TPRM only if the third party is tied to SaaS intake. | Add user-need row: `Assess a vendor or supply-chain dependency` → `PRC-TPRM-001` → `TMPL-TPRM-001`, `PRC-RM-001`. |
| TPRM boundaries are clear in the procedure but not visible at the front door. | Navigation / role clarity | Practitioners may over-own Procurement, contract, or business continuity work until they read the procedure. | Add one-line boundary language in `FRM-002`: "CERG owns the cyber slice; Procurement/ERM/Legal own adjacent vendor lifecycle." |
| No single closure checklist for vendor assessment. | Procedure content | The practitioner may complete a questionnaire but miss catalog update, evidence storage, residual risk, or contract clause follow-up. | Add a `TPRM closure package` checklist near the start/end of `PRC-TPRM-001`. |

## Workflow 6 — OT Patch Deferral

### Starting point from `FRM-002`
- Closest user need: `Start exposure management` → `PRC-VM-001`, `RMF-001`, `CAT-002`.
- Regulated adoption path later points NERC-CIP / OT readers to OT and CIP package material, but the practitioner path for deferring an OT patch is not direct.

### Practitioner path
1. Open `PRC-VM-001` for exposure treatment, patch hygiene, exceptions, and risk acceptance.
2. Identify that this is OT, not ordinary IT patching; active scanning/remediation and patch windows may create operational risk.
3. Open `STD-OT-001` for OT-specific vulnerability identification, patch treatment, BES/non-BES distinction, and exception/escalation rules.
4. Determine whether the asset is BES or non-BES.
5. For non-BES OT: document operational reason, compensating controls, Engineering review, risk/exception request, review cycle.
6. For BES: initiate risk acceptance/exception plus CIP deviation and mitigation plan through Governance/NERC-CIP process; preserve evidence in the NERC-CIP evidence library.
7. Track in risk register and exposure metrics until patch, mitigation, or approved window closure.

### Can the practitioner proceed?
Partially. The content exists and is directionally sound, but the navigation requires inference. A practitioner can see from `PRC-VM-001` that OT is special and from `STD-OT-001` that BES deferral needs CIP deviation, but `FRM-002` does not provide a direct "OT patch deferral" path.

### What is clear
- Decision rule: OT patching must respect operational safety/availability; CVSS alone is insufficient.
- BES distinction: BES Cyber System gaps carry NERC-CIP deviation and mitigation obligations.
- Owners: Risk validates and tracks exposure; Engineering validates compensating controls and executes safe change; Governance owns CIP evidence/deviation process; CISO approval is required for OT exceptions in current OT standard language.
- Hard guardrail: PPR-tier exposures are generally not eligible for risk acceptance except OT operational-windowing scenarios where the CIP deviation process is the approved path.

### Friction points
| Gap | Type | Why it slows the practitioner | Suggested fix |
|---|---|---|---|
| No direct `FRM-002` row for OT patch deferral. | Navigation | A practitioner may treat this like ordinary exposure management and miss CIP deviation or OT safety constraints. | Add user-need row: `Defer an OT or BES patch` → `PRC-VM-001` §11, `STD-OT-001` §4.2/§11, `PRC-RM-001` §7.5, CIP operational package. |
| Non-BES versus BES path is clear in `STD-OT-001` but not summarized in `PRC-VM-001`. | Procedure content | The exposure procedure is the likely first document; it should warn immediately when OT/BES scope is present. | Add a short OT deferral decision table to `PRC-VM-001`: non-BES OT, BES compliance unaffected, BES compliance impacted, emergency operational exception. |
| Template path for CIP deviation is not visible from the first two documents. | Navigation | The practitioner knows a deviation is required but may not know which artifact to use. | Surface the CIP deviation template/path in `FRM-002` and `PRC-VM-001` OT references. |
| Approval language may conflict with the broader business-owner risk-acceptance model. | Procedure content / consistency | `STD-OT-001` says CISO approval for OT exceptions; `PRC-RM-001` says Business Owner owns consequence and CISO approves by severity. | Align as part of the existing RMF/PRC-RM/OT authority cleanup: Business Owner accepts business/operational risk; CISO/Governance approve policy/CIP exception authority. |
| No canonical story shows a safe OT maintenance-window deferral. | Missing example | The practitioner needs to see how CERG avoids false urgency without letting patch debt disappear. | Add the missing OT maintenance-window exception story identified in E02/E03. |

## Cross-Workflow Findings

| Finding | Severity | Affected workflows | Classification | Recommendation |
|---|---:|---|---|---|
| `FRM-002` user-need navigation is excellent for broad program tasks but misses several concrete weekly tasks. | High | Risk exception, privileged access evidence, TPRM, OT deferral | Navigation | Add direct user-need rows for these four practitioner jobs. |
| Evidence paths teach quality before source. | High | Privileged access review evidence | Navigation / procedure content | Add control-specific evidence examples and surface `TMPL-AUD-001`. |
| Exception versus risk acceptance is strong inside `PRC-RM-001` but not front-door visible. | Medium | Risk exception, vuln SLA miss, OT deferral, vendor residual risk | Navigation | Add `TMPL-RM-002` and `TMPL-RM-004` to `FRM-002` risk-related rows with one-line usage rule. |
| Closure packages are often implicit. | Medium | SaaS review, TPRM, evidence request, vulnerability triage | Procedure content | Add small `closure package` boxes to high-use procedures. |
| OT/BES routing requires too much inference. | High | OT patch deferral | Navigation / procedure content | Add explicit OT/BES deferral route in `FRM-002` and `PRC-VM-001`. |
| Missing stories are concentrated where operational judgment matters. | Medium | Evidence request, OT deferral, SaaS/TPRM parallel path | Missing example | Add or promote targeted examples; do not add broad generic stories. |
| Role clarity is generally good once inside procedures, but first contact often names domains rather than a primary actor. | Medium | Evidence request, SaaS, TPRM | Role clarity | Add first-action owner to front-door path rows where possible. |

## Time-to-Understanding Improvement Queue

| Priority | Change | Files | Expected effect |
|---:|---|---|---|
| 1 | Add direct practitioner user-need rows for exception/acceptance, access review evidence, third-party assessment, and OT patch deferral. | `governance/CERG-GOV-FRM-002_Framework_System_Map.md` | Reduces first-click uncertainty for four weekly tasks. |
| 2 | Add a privileged access review evidence mini-path and checklist. | `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`; `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md` | Prevents bad evidence packages and clarifies producer/submitter split. |
| 3 | Add OT deferral decision table. | `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`; `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md` | Makes BES/non-BES and CIP deviation routing unmistakable. |
| 4 | Add closure-package boxes to SaaS/architecture and TPRM procedures. | `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`; `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` | Helps practitioners know when the work is done and what evidence proves it. |
| 5 | Add two practitioner stories: access review evidence request and OT patch deferral. | `examples/day-in-the-life/` | Gives judgment-heavy workflows a training-quality narrative. |
| 6 | Align stale acceptance/approval wording across OT, VM, RMF, and examples. | Existing G02 authority-alignment bundle | Prevents practitioners from learning competing approval models. |

## H02 Acceptance Criteria Check

- Workflow comprehension notes included: yes, six workflows tested.
- Started from `FRM-002` navigation by user need: yes.
- Followed directed links first and recorded inference points: yes.
- Identified lack of next step, owner, template, or decision rule: yes, in each workflow table.
- Classified issues as navigation, procedure content, role clarity, or missing example: yes.
- Identified changes that reduce time-to-understanding: yes, prioritized queue included.
