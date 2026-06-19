# Task H03 Output: Business owner path comprehension test

## Scope Reviewed
- Business-facing orientation and authority documents:
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` §9.6-§9.8
  - `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` §6-§8
  - `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`
- Procedures and templates reviewed from business-owner perspective:
  - `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
  - `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`
  - `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
  - `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
  - `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
  - `templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md`
  - `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
  - `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md`
- Relevant operational examples:
  - `examples/day-in-the-life/README.md` Stories 1, 2, 3, 5, and 6.

## Method
- Persona used: non-security Business Owner accountable for a system, vendor relationship, process, or budget decision.
- For each H03 scenario, I asked whether the Business Owner can tell:
  - what decision is being asked of them;
  - what risk they are accepting;
  - what evidence they must provide;
  - what happens if they do nothing;
  - who will escalate;
  - when the decision will be reviewed.
- I treated security jargon as a comprehension defect when the business reader has to know CERG internals before understanding the decision.

## Executive Summary

CERG is directionally strong for business accountability. It repeatedly teaches the right principle: Security assesses and recommends; the Business Owner owns the consequence. `RMF-001`, `PRC-RM-001`, `TMPL-RM-004`, `OM-001`, and the day-in-the-life stories all reinforce that business risk cannot be accepted by Security on behalf of the business.

The business-owner path is weaker than the security-practitioner path because business users do not have a dedicated front door. They encounter strong content only after opening procedure-heavy documents full of internal role names, control acronyms, and register terminology. The model is correct; the reader path is not yet optimized for a non-security decision-maker.

Highest-value fixes:

1. Add a `Business Owner / System Sponsor` reader path to `IMP-007` or `FRM-002`.
2. Add a plain-language decision box to each business-facing template: `You are being asked to decide...`, `If you approve...`, `If you decline...`, `If you do nothing...`.
3. Fix template/signature drift where templates omit Business Owner acceptance even when the procedure says the Business Owner owns residual risk.
4. Add a funding-decision artifact or section for control implementation asks; current COG/MTR language surfaces funding asks but does not package the business decision.
5. Reduce unexplained jargon in business-facing sections: `residual risk`, `compensating control`, `POA&M`, `CUEC`, `CUI`, `CIP`, `SOX`, `SLC`, `E2/E3`, `PPR`, `APC`, and `SCCT`.

## Scenario 1 — Accept residual risk for delayed remediation

### Likely path
- Trigger source: critical/high finding, vulnerability SLA miss, architecture go-live condition, or control exception.
- Relevant documents:
  - `PRC-RM-001` §7 Exception Process.
  - `RMF-001` §9.6-§9.7 Risk treatment and acceptance authority.
  - `TMPL-RM-004` Risk Acceptance Request Form.
  - `TMPL-RM-002` Security Exception Request Form when the trigger is a control/standard deviation.
  - Story 2 in `examples/day-in-the-life/README.md` for critical vulnerability and acceptance under SLA pressure.

### Business-owner comprehension test
| Question | Can the Business Owner tell? | Notes |
|---|---|---|
| What decision is being asked? | Mostly yes. | `TMPL-RM-004` is clear that the Business Owner accepts or declines residual risk. `PRC-RM-001` cleanly separates exception from risk acceptance. |
| What risk are they accepting? | Yes, if the form is completed well. | The form asks for risk statement, residual score, affected process, business consequence, controls, conditions, and expiration. |
| What evidence must they provide? | Partly. | They must provide business rationale, alternatives considered, and signature. Security/Risk provides scoring and controls. The template could say this division more plainly. |
| What happens if they do nothing? | Partly. | `PRC-RM-001` is clear for expired exceptions, but less direct for an unsigned acceptance request before SLA miss. The practical outcome is remediation must proceed, go-live may be blocked, SLA breach escalates, or finding remains open. |
| Who escalates? | Yes for process insiders; partly for business readers. | Risk Register Owner, Governance Pillar Leader, CISO, and Executive Sponsor appear in the process, but the business-facing escalation chain is not summarized. |
| When is the decision reviewed? | Yes. | `RMF-001` provides default durations by severity; `TMPL-RM-004` asks for expiration, review cadence, renewal criteria, and early-review triggers. |

### Jargon / internal assumptions
- `Residual risk score`, `inherent risk`, `compensating controls`, `risk appetite`, `authority table`, `PPR-tier`, and `POA&M` assume security/risk literacy.
- `RMF-001` §9.7a says the Exception Request Form handles both types, while newer procedure/template language separates `TMPL-RM-002` and `TMPL-RM-004`. That is confusing for a business reader and already appears in prior audit authority-drift findings.

### Recommendation
Add a plain-language decision panel to `TMPL-RM-004`:

> You are being asked to decide whether the business can tolerate this risk until the expiration date. If you accept, the finding remains visible and monitored; Security does not make it disappear. If you decline, the activity must be remediated, mitigated, delayed, transferred, or stopped. If you do not decide before the due date, the item escalates as an unresolved risk and may block go-live or create an SLA breach.

## Scenario 2 — Fund a control implementation

### Likely path
- Trigger source: risk treatment plan, metrics/KRI trend, COG agenda item, audit finding, vendor risk finding, or architecture review condition.
- Relevant documents:
  - `OM-001` §4.4 Cyber Oversight Group agenda and cross-functional treatment alignment.
  - `MTR-001` §6 CISO/COG brief template, especially `ASKS`.
  - `RMF-001` §9.6 treatment options and §12 cascading investment signals.
  - `PRC-RM-001` treatment plan and register fields.

### Business-owner comprehension test
| Question | Can the Business Owner tell? | Notes |
|---|---|---|
| What decision is being asked? | Partly. | COG/MTR language says funding, scope, or organizational moves may be required, but there is no standard business-facing funding ask packet. |
| What risk are they accepting if they do not fund? | Partly. | The risk register can show residual risk, but the funding decision is not packaged as `fund vs accept vs defer vs avoid`. |
| What evidence must they provide? | Weak. | CERG asks Security/Risk/Governance to bring risk evidence, but it does not clearly state what business information is needed: cost tolerance, outage constraints, budget owner, deadline, customer impact, or operational trade-off. |
| What happens if they do nothing? | Weak. | The risk remains open or worsens, but the business reader is not directly told whether this becomes acceptance, escalation, board reporting, go-live block, or operational risk. |
| Who escalates? | Mostly yes. | COG, CISO, Governance Pillar Leader, and Risk Register Owner are visible; however, the exact escalation path for unfunded treatment is not business-simple. |
| When is the decision reviewed? | Partly. | COG cadence is monthly; risk reviews and metrics cadence exist. But the funding ask itself lacks a review/expiry field. |

### Jargon / internal assumptions
- `KRI`, `OU Scorecard`, `residual-score weighted`, `risk appetite cascade`, and `improvement register` are useful internally but not sufficient for a business funding decision.
- CERG assumes the business reader can translate risk posture into budget choice. Many will need the choices stated explicitly.

### Recommendation
Create a small `Control Funding Decision Brief` pattern, either as a template or as a section in `PRC-RM-001` / `MTR-001`:

| Field | Business-facing meaning |
|---|---|
| Decision needed | Fund now / defer / accept residual risk / stop activity |
| Business process affected | What operation, customer, revenue, safety, or regulatory obligation is exposed |
| Treatment options | Good / better / best, with cost, time, and risk reduction |
| Consequence of no decision | What remains exposed and when escalation occurs |
| Required approver | Budget owner, Business Owner, CISO, Executive Sponsor, COG, Board if applicable |
| Review date | When the ask returns if unresolved |

## Scenario 3 — Sponsor a SaaS purchase

### Likely path
- Trigger source: business wants to buy/use a SaaS tool.
- Relevant documents:
  - `FRM-002` §5 `Review a new system or SaaS`.
  - `PRC-AR-001` Architecture Review and Project Intake Procedure.
  - `TMPL-AR-001` Architecture and Project Intake Form.
  - `PRC-TPRM-001` Third-Party and Supply Chain Risk Procedure.
  - Story 1 in `examples/day-in-the-life/README.md`.

### Business-owner comprehension test
| Question | Can the Business Owner tell? | Notes |
|---|---|---|
| What decision is being asked? | Yes. | Submit intake, sponsor the project, approve go-live for business scope, and accept residual risk where applicable. Story 1 is especially clear. |
| What risk are they accepting? | Mostly yes. | Vendor evidence gaps, logging gaps, access limitations, data classification, subprocessor/data residency, and go-live conditions are surfaced. |
| What evidence must they provide? | Mostly yes. | Intake asks for business process, data classification, vendor involvement, target go-live, owner, and technical owner. TPRM asks for vendor/service context. |
| What happens if they do nothing? | Partly. | The purchase/review may stall or remain unapproved, but the consequences of bypassing intake are not stated in business terms. |
| Who escalates? | Mostly yes. | Engineering and Governance route review; Vendor Risk Analyst handles TPRM; CISO appears for High/Critical acceptance. |
| When is the decision reviewed? | Yes for review clock; partly for residual conditions. | SLC and AR procedure provide timelines. Risk/exception review exists if conditions remain open. |

### Jargon / internal assumptions
- `CUI`, `BCSI`, `SOX`, `CIP`, `SSO`, `SCIM`, `SIEM`, `CUEC`, `FedRAMP equivalency`, and `subprocessor` may not be understood by a normal sponsor.
- `TMPL-AR-001` is usable but could include a non-security instruction line: `If you do not know, answer Unknown; do not guess.`

### Recommendation
Add a business-sponsor callout to `TMPL-AR-001` and/or `PRC-AR-001`:

> As Business Owner, your job is not to design the control. Your job is to name the business process, data, users, vendor, deadline, and consequence of delay; confirm whether the tool is worth the conditions placed on it; and accept only the residual business risk you actually own.

Also make Story 1 more visible from business-facing navigation; it is one of the strongest business-readable examples.

## Scenario 4 — Respond to an audit evidence gap

### Likely path
- Trigger source: auditor rejects evidence, evidence library lacks required artifact, or control test finds deficiency.
- Relevant documents:
  - `AUD-001` Evidence Quality Standard.
  - `PRC-AUD-001` Audit and Evidence Management Procedure.
  - `TMPL-AUD-001` Control Evidence and Test Worksheet.
  - Story 3 in `examples/day-in-the-life/README.md`.

### Business-owner comprehension test
| Question | Can the Business Owner tell? | Notes |
|---|---|---|
| What decision is being asked? | Partly. | The business owner may be asked to confirm facts, produce evidence, fund remediation, accept residual risk, or own corrective action. The procedure does not package those as business choices. |
| What risk are they accepting? | Partly. | If evidence cannot prove control operation, the business risk may be audit finding, control deficiency, regulatory exposure, or customer assurance issue. This is clear to Governance, not necessarily to the business owner. |
| What evidence must they provide? | Mostly yes if the control is known. | `AUD-001` clearly states who/when/what period/where/scope. `TMPL-AUD-001` asks for population, sample, evidence reviewed, exceptions, and owner. |
| What happens if they do nothing? | Partly. | Findings, POA&M, corrective actions, and escalation exist, but the business consequence of ignored evidence gaps is not explained plainly. |
| Who escalates? | Yes for internal readers. | Evidence Librarian opens corrective action; Governance Pillar Leader owns audit response; CMMC/Federal Compliance Manager or other compliance role escalates specific overlays; CISO reviews material findings. |
| When is the decision reviewed? | Mostly yes. | POA&M/monthly review and evidence metrics cadence are clear. Corrective action needs owner, due date, verification method, closure evidence. |

### Jargon / internal assumptions
- `E1/E2/E3`, `control operates`, `population`, `sample methodology`, `POA&M`, `C3PAO`, `SPRS`, and `evidence tier` are audit terms.
- The business owner may not understand the difference between `we did the work` and `we can prove the work for the requested period` unless the gap notice says so.

### Recommendation
Add an `Evidence Gap Notice` pattern for business/control owners:

| Plain-language field | Meaning |
|---|---|
| What the auditor/customer asked for | Exact request in non-security terms |
| What we have | Evidence currently available |
| Why it is not enough | Missing date, scope, population, reviewer, period, storage, independence, or closure proof |
| What you must do | Produce evidence, confirm facts, fund remediation, approve corrective action, or accept residual risk |
| If no action | Finding, POA&M, customer/auditor rejection, escalation, or risk acceptance required |
| Due date / escalation | When Governance escalates and to whom |

## Scenario 5 — Handle vendor risk finding

### Likely path
- Trigger source: vendor assessment finding, weak evidence, high-risk subprocessor, vendor breach, contract clause gap, or deteriorating monitoring signal.
- Relevant documents:
  - `PRC-TPRM-001` Third-Party and Supply Chain Risk Procedure.
  - `TMPL-TPRM-001` Vendor Security Questionnaire and Assessment Template.
  - `PRC-RM-001` for residual risk acceptance.
  - Story 6 in `examples/day-in-the-life/README.md` for third-party security incident notification.

### Business-owner comprehension test
| Question | Can the Business Owner tell? | Notes |
|---|---|---|
| What decision is being asked? | Mostly yes in procedure; weaker in template. | `PRC-TPRM-001` says Business / Asset Owners own vendor relationship and sign residual cyber risk. The template decision table lacks a Business Owner approval row. |
| What risk are they accepting? | Mostly yes. | Tiering, evidence-by-tier, control levels, MSP hard requirements, international access, breach/SCCT, and vendor refusal paths are clear. |
| What evidence must they provide? | Partly. | The vendor provides most evidence; business owner provides business criticality, service scope, relationship context, operational dependency, and whether to continue/suspend/terminate. This is not called out enough in the template. |
| What happens if they do nothing? | Partly. | Vendor may remain conditional/restricted/prohibited, risk acceptance may be required, or transition planning starts. The business consequence should be stated more directly. |
| Who escalates? | Yes. | Vendor Risk Analyst, Governance Pillar Leader, Engineering Pillar Leader, CISO, SCCT, Procurement, Legal, and Business Owner are named by scenario. |
| When is the decision reviewed? | Yes. | Reassessment cadence by tier, 90-day Amber review, SCCT closure, and vendor monitoring cadence are explicit. |

### Jargon / internal assumptions
- `CUEC`, `SCCT`, `APC`, `CIP-013`, `FedRAMP equivalency`, `CUI`, `BCSI`, `SBOM`, `VEX`, `SOC 2 carve-outs`, and `Inherited — Unverified` are high-density terms.
- The business owner needs a simple statement: `You own whether this vendor remains necessary despite these conditions; CERG owns the cyber assessment.`

### Recommendation
Update `TMPL-TPRM-001` Review and Approval to include the Business Owner when residual vendor risk exists:

- Business Owner: confirms business need, operational dependency, and accepts/rejects residual vendor risk.
- Vendor Risk Analyst: completes assessment and recommendation.
- Risk Pillar Leader / CISO: approve within authority.

Add a business-facing decision field: `Proceed / proceed with conditions / pause purchase / transition away / reject vendor`.

## Cross-Scenario Findings

| Finding | Severity | Type | Why it matters | Recommended action |
|---|---:|---|---|---|
| Business accountability principle is strong and repeated. | Strength | Model clarity | CERG correctly prevents Security from owning business consequences. | Preserve this language; use it as the basis for business-facing callouts. |
| No dedicated Business Owner reader path exists. | High | Navigation | Non-security owners must enter through security-practitioner documents. | Add a Business Owner / System Sponsor path in `IMP-007` or `FRM-002`. |
| Several forms lack a plain-language decision summary. | High | Reader comprehension | A business owner can sign the form without fully understanding the consequence. | Add `You are being asked to decide...` boxes to AR, RM, AUD, and TPRM templates. |
| Funding decisions are surfaced but not packaged. | High | Missing artifact / procedure content | Business owners need to decide fund/defer/accept/avoid, not just read risk metrics. | Add a `Control Funding Decision Brief` pattern. |
| TPRM template omits Business Owner approval despite procedure assigning business-side residual-risk ownership. | High | Traceability / role clarity | A vendor risk acceptance can appear CISO/Risk-owned in the form. | Add Business Owner signature/review row where residual risk exists. |
| `RMF-001` §9.7a has stale form-routing language compared with `PRC-RM-001` and `TMPL-RM-004`. | High | Consistency | Business readers may use the wrong form for risk acceptance. | Align with the separate `TMPL-RM-002` / `TMPL-RM-004` model. |
| `What happens if I do nothing?` is inconsistent. | Medium | Business-facing clarity | Silence can become accidental acceptance or unmanaged delay. | Add no-decision consequences to templates and escalation notices. |
| Examples are much easier for business readers than procedures. | Strength / opportunity | Example quality | Stories 1, 2, 3, and 6 translate CERG well. | Cross-link stories from business-facing rows and templates. |
| Acronym density is high in business-facing templates. | Medium | Jargon | CUI/SOX/CIP/POA&M/CUEC/SCCT/APC require translation. | Add glossary hover/table or parenthetical expansions on first use in forms. |

## Recommended Business-Owner Language Pattern

Use this pattern in business-facing forms, review packets, and escalation notices:

```text
You are being asked to decide: [fund / approve go-live / accept residual risk / proceed with vendor / provide evidence].

The business process affected is: [plain-language process].
The security concern is: [plain-language threat or control gap].
If you approve: [conditions, monitoring, expiration, review date].
If you decline: [remediation, delay, vendor rejection, alternate path].
If you do nothing by [date]: [escalation, SLA breach, finding, go-live block, vendor restriction, or COG/board visibility].
Security's role: assess, recommend, validate controls, and track evidence.
Your role: own the business consequence for the system, process, vendor, or budget you control.
```

## H03 Acceptance Criteria Check

- Tested whether CERG is understandable outside security: yes.
- Covered required scenarios: residual risk acceptance, control funding, SaaS sponsorship, audit evidence gap, vendor risk finding.
- Identified whether the business owner can tell decision/risk/evidence/no-action/escalation/review: yes, scenario tables included.
- Flagged jargon and internal assumptions: yes.
- Recommended specific language improvements for business-facing sections and templates: yes.
