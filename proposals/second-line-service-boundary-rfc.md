# RFC: Clarifying CERG's Second-Line Boundary and First-Line Security-Service Interface

## Status

**Discussion draft — not an approved CERG artifact.** This RFC is deliberately outside the controlled document catalog so reviewers can challenge the proposed operating model before authoritative documents are changed.

## Decision Requested

Adopt a consistent boundary between CERG's second-line role and security operations performed by internal teams or a managed security service provider (MSSP); select one of the operating-model options in [Section 3](#3-operating-model-options); and approve the proposed direction, scope, and transition approach before updating controlled documents.

## 1. Problem

`CERG-GOV-OM-001` §2.4 correctly states that first-line system, service, business, IT, and OT owners operate controls while CERG is an integrated second-line cybersecurity function. Several downstream descriptions assign CERG operational ownership of the same controls. Examples include scanner operation, CSPM/SSPM administration, identity-threat monitoring, enterprise vulnerability-scan operations, SIEM alert triage, and production detection deployment.

This makes it unclear who:

- operates a production security service;
- owns the service outcome when work is outsourced;
- independently assesses whether the service is working; and
- commands an incident when an alert becomes material.

A title, reporting line, or employment relationship does not determine the line of defense. The activity does. An MSSP operating a SOC or a scanner is performing delegated first-line work. The organization still needs an internal first-line owner accountable for that service and a second-line function capable of challenging it.

## 2. Design Principles

1. **First-line accountability cannot be outsourced.** A named internal service or asset owner remains accountable when an MSSP performs work.
2. **CERG must not self-assure a standing service it operates.** The assurance function must be organizationally and evidentially separable from production operation.
3. **The boundary must be workable for small teams.** Role consolidation is allowed, but the resulting conflict must be explicit, time-bounded, and subject to an independent review route for consequential decisions.
4. **Existing authority is reused.** `OM-001` owns operating boundaries, `RAC-001` owns RACI, `PRC-VM-001` owns exposure workflow and clocks, `STD-LM-001` owns logging and detection requirements, and `PRC-TPRM-001` owns provider controls. This RFC does not propose a new permanent role, record type, or control catalog.
5. **CERG remains technically credible.** Second-line assurance includes technical validation, adversarial testing, requirement-setting, evidence review, and challenge. It is not administrative observation from a distance.
6. **Incident command remains with the standing IR team.** An alert queue may route an event to IR; it does not give CERG incident-command authority.

## 3. Operating-Model Options

### Option A — Strict Second Line

CERG sets requirements and independently assesses operation. It neither administers production security platforms nor authors/deploys production detection content.

| Benefits | Costs / risks |
|---|---|
| Strongest independence; simple audit narrative | Requires a mature first-line security-operations capability; may be impractical for small organizations; separates detection expertise from production implementation |

This option is most appropriate where a separate SOC, infrastructure security team, or MSSP already has substantial operational capability.

### Option B — Assurance-Led Second Line (recommended)

CERG may develop reference designs, requirements, candidate detection content, test cases, and acceptance criteria. A first-line team or MSSP operates production platforms, deploys approved content under its change process, staffs queues, and runs response handoffs. CERG independently validates coverage, control effectiveness, and selected outcomes.

| Benefits | Costs / safeguards |
|---|---|
| Preserves CERG technical depth while keeping standing production operation first-line; works with internal teams or MSSPs | Requires clear handoffs, a production acceptance/change process, and a rule that the content author does not approve their own effectiveness claim |

This is the proposed default. It treats detection engineering as assurance-oriented security engineering rather than as SOC operations.

### Option C — Hybrid Security Operations Inside CERG

CERG continues to operate scanners, SIEM/CSPM/SSPM, and alert triage while also setting requirements and assuring effectiveness.

| Benefits | Costs / risks |
|---|---|
| Lowest transition cost; may fit a very small organization temporarily | Does not meet the intended true-second-line model without a separately resourced independent assessor; makes assurance claims vulnerable to self-review |

If retained, this must be described honestly as a hybrid first-/second-line function, not as a wholly second-line CERG model. It is not recommended as the target state.

## 4. Proposed Boundary

The following language is proposed for incorporation into `CERG-GOV-OM-001` after review:

> CERG is a second-line cybersecurity function. It defines security outcomes and evidence criteria; evaluates exposure; performs independent validation and adversarial testing; challenges control performance; and escalates material deficiencies. CERG does not own the standing production operation of scanners, SIEM, EDR, CSPM, SSPM, identity-monitoring, or alert queues.
>
> First-line internal teams or contracted providers operate those services. The organization assigns an internal first-line service owner who remains accountable for scope, service performance, remediation execution, and operational records. A provider may be Responsible for contracted activities but does not assume the organization’s accountability.
>
> Under the assurance-led model, CERG may supply reference designs, requirements, candidate detection content, and test cases. First line accepts and deploys production content through its change process. CERG independently validates coverage and effectiveness and must not approve its own production operation.

### 4.1 Work Allocation

| Activity | First-line service owner | First-line operator / MSSP | CERG Engineering | CERG Risk | CERG Governance | Standing IR team |
|---|---|---|---|---|---|---|
| Security-service scope, funding, and performance | A | R/C | C | C | I | I |
| Scanner, SIEM, EDR, CSPM, SSPM, and connector operation | A | R | C | C | I | I |
| Operational source health and failed-connector restoration | A | R | C | I | I | I |
| Initial alert acknowledgement and triage | A | R | I | I | I | C for escalation interface |
| Incident declaration, command, containment, and recovery | I | R/C as contracted | C | C | C | A |
| Exposure classification and exposure-path assessment | C | C | C | R/A | I | I |
| Treatment decision and timely remediation | A | R | C | C / challenge | C for exception routing | C when incident-driven |
| Production detection deployment and tuning | A | R | C | C | I | I |
| Detection requirements, test cases, coverage measurement, and independent validation | C | C | C | R/A | C | C |
| Control-evidence criteria, conformance assurance, and reporting | C | R for operational evidence | C | C | R/A | C |

**RACI interpretation:** the internal service owner may also be the operator in a fully internal model, in which case it is R/A. If an MSSP operates the service, the internal owner remains A and the MSSP is R. The table separates service operation from risk classification deliberately: Risk can be accountable for an independent exposure decision without becoming accountable for running the scanner that produced the observation.

### 4.2 Detection Engineering Versus SOC Operations

The current term *Detection Engineer* spans two distinct activities. The intended boundary is:

- **CERG Detection Engineer:** defines detection requirements, maps priority attack paths, produces candidate logic and test cases, measures coverage, reviews tuning evidence, and independently validates detections through purple-team or equivalent testing.
- **First-line SOC / MSSP:** operates SIEM/EDR platforms and integrations, deploys approved production content, monitors source health, acknowledges and triages alerts, maintains cases, escalates qualifying events, and supports IR.
- **Standing IR team:** decides whether an event is an incident and owns incident command, containment, eradication, recovery, and the operational incident record.

A CERG practitioner may participate in a production change as a subject-matter contributor. The first-line owner approves and deploys it. A different qualified person or function validates effectiveness where the author’s work is being assessed.

## 5. Required First-Line Service Interface

No new permanent CERG record is proposed. For each operated security service, capture the following in the existing System Control Profile and, where a provider is involved, the TPRM shared-responsibility matrix/contract package:

| Required field | Purpose |
|---|---|
| Internal first-line service owner | Preserves organizational accountability |
| Operating party and service model | Identifies internal, MSSP, or hybrid delivery |
| In-scope assets, environments, and exclusions | Makes coverage claims testable |
| Operational activities and boundaries | Separates platform operation, triage, treatment, and assurance |
| Service targets and escalation path | Makes acknowledgement, triage, remediation, and outage performance observable |
| Required operational records and evidence location | Ensures CERG can assure actual operation |
| Production-change and acceptance authority | Prevents ambiguous deployment authority |
| CERG assurance cadence, method, and sampling population | Makes oversight repeatable rather than ad hoc |
| Provider access, data ownership, exit, and kill-switch provisions | Preserves the existing TPRM control model |

For an MSSP, the assurance plan should at least include monthly service reporting, quarterly samples of closed alerts and exposure dispositions, independent escalation-SLA checks, source-health/coverage review, annual joint exercise, and tracked corrective actions for provider failures.

## 6. Proposed Controlled-Document Changes

### Phase 1 — Boundary Authorities

| Artifact | Proposed change |
|---|---|
| `governance/CERG-GOV-OM-001_CERG_Operating_Model.md` | Add the boundary in Section 2; recast Engineering as design/guardrail/handoff support; recast Risk as exposure governance and independent validation; move SOC, tool operations, and alert triage explicitly to first line; update its sample RACIs. |
| `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` | Add First-Line Service Owner and First-Line Operator/MSSP interface columns for operational processes. Replace the current Risk R/A assignments for exposure scanning and alert handoff with split rows that distinguish operation, classification, treatment performance, and independent verification. |
| `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md` | Make observation-source operation first-line; retain Risk ownership of independent validation, classification, SLA measurement, challenge, and exposure reporting. Require source provenance/coverage status and distinguish provider treatment evidence from independent closure verification. |
| `governance/CERG-GOV-FRM-001_CERG_Framework.md` | Revise the lifecycle narrative, capability ownership, Risk core functions, illustrative staffing model, and regulatory descriptions to avoid stating that Risk performs continuous scans or owns standing monitoring. |

### Phase 2 — Direct Operational Consumers

| Artifact | Proposed change |
|---|---|
| `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md` | Name the SOC/MSSP as the triage operator and first-line owner as accountable; distinguish detection requirements/validation from production deployment and queue operation. |
| `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | Replace the statement that Risk conducts post-production monitoring with an assurance/independent-validation statement; add operational-service handoffs to F-03/F-04/F-06 as needed. |
| `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` | Add MSSP operating-performance assurance to the existing access, log ownership, and kill-switch requirements. |
| `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md` and `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md` | Replace production-tool operation, scanner schedules, alert triage, and rule deployment as CERG responsibilities with requirements, validation, challenge, and assurance responsibilities. |

### Phase 3 — Consistency Sweep

Reconcile workforce planning, implementation cards/checklists, compliance matrix examples, metrics, role competency language, and machine-readable outputs. This phase is necessary because those documents presently model scanner and detection operations as Risk work.

## 7. Transition Approach

1. **Inventory services before rewriting accountability.** Identify the actual operator and internal accountable owner for vulnerability management, SOC/SIEM, EDR, CSPM/SSPM, identity monitoring, and OT monitoring.
2. **Create or refresh the service interface.** Complete the existing provider/shared-responsibility and control-profile fields in Section 5 for each service.
3. **Test operational handoffs.** Sample alert-to-IR and observation-to-treatment handoffs before making assurance claims. Resolve missing records, unclear escalations, and inaccessible provider evidence.
4. **Update Phase 1 controlled documents.** Make the authority/RACI/procedure changes together so the corpus has one coherent answer.
5. **Update direct consumers and role descriptions.** Do not leave an operational standard or job description contradicting the boundary.
6. **Regenerate and validate.** Regenerate derived machine-readable artifacts; run corpus validation and integrity checks; obtain broad review before any merge to `main`.

## 8. Review Questions

1. Is Option B sufficiently independent to describe CERG as a true second-line model, or should the framework choose Option A for stricter separation?
2. Should CERG Detection Engineering retain candidate-rule authoring, or should it only specify requirements and validate first-line-produced content?
3. Which duties must remain inside first-line operations even in small organizations, and what compensating independent review is realistic where roles are consolidated?
4. Is the proposed distinction between exposure classification (CERG Risk) and scanner operation (first line) clear and usable?
5. Are the proposed MSSP assurance activities proportionate and implementable for smaller adopters?
6. Are there regulatory or sector interpretations that require a different allocation for NERC-CIP, CMMC, SOX, or another overlay?

## 9. Out of Scope

This RFC does not change risk-acceptance authority, control requirements, exposure SLAs, incident-response command, the canonical record catalog, or the NIST/NICE role mappings. It also does not prescribe a particular SOC, scanner, SIEM, GRC platform, or provider model.
