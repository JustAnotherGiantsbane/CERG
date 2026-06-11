# SURGE: Cyber Engineering, Risk & Governance

## CONTROL EFFECTIVENESS FRAMEWORK
### Effectiveness Measurement · Failure Analysis · Rationalization · Adaptive Maturity Integration

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CEF-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-GOV-TRC-001`](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) · [`CERG-PRC-LL-001`](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) · [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) |
| **Review Cycle** | Annual / On control baseline revision |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.IM, PROTECT all categories) · NIST 800-55 · ISO/IEC 27004 |
| **Regulations** | Cross-cutting : applies to all CERG-supported frameworks |
| **Environments** | All CERG-managed controls |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Why Implementation Is Not Effectiveness](#2-why-implementation-is-not-effectiveness)
3. [Effectiveness Measurement Model](#3-effectiveness-measurement-model)
4. [Control Family Effectiveness Metrics](#4-control-family-effectiveness-metrics)
5. [Control Failure Analysis](#5-control-failure-analysis)
6. [Control Rationalization](#6-control-rationalization)
7. [Integration with Maturity Assessment](#7-integration-with-maturity-assessment)
8. [Roles and Responsibilities](#8-roles-and-responsibilities)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

CERG's Unified Control Baseline (CB-001) tracks whether each control is Implemented, Partially Implemented, Inherited, Planned, Risk Accepted, or Not Applicable. That answers "is the control in place?" It does not answer "is the control working?"

A control can be Implemented, baseline deployed, evidence collected, and yet be ineffective: poorly configured, bypassed in practice, defending against a threat vector that no longer applies, or generating alerts that nobody investigates. An organization that can only report implementation status is operating at Repeatable maturity. An organization that measures and acts on control effectiveness is operating at Adaptive maturity.

This framework defines how CERG measures whether controls are working, analyzes why they fail, and rationalizes the control portfolio so that every control earns its place.

> **The Assessor Test**
>
> An assessor asks: "Your access recertification control is Implemented. What percentage of recertifications result in access reduction?" If the answer is "We do not track that," the control may be rubber-stamping : present but not effective. If the answer is "12% of recertifications result in reduction, and we investigate when that falls below 5%," the control is being measured, not just checked. The difference is the gap between Repeatable and Adaptive.

---

## 2. Why Implementation Is Not Effectiveness

### 2.1 Four Ways an Implemented Control Can Be Ineffective

| Failure Mode | Description | Example |
|---|---|---|
| **Design failure** | The control was designed for a threat that no longer applies, or was never correctly designed for the threat it was meant to address. | A WAF ruleset tuned for SQL injection in 2019 that does not cover the API-based attacks the organization now faces. |
| **Implementation failure** | The control is correctly designed but was incorrectly deployed, configured, or scoped. | MFA is required by policy but was not enforced on the VPN gateway because the integration was misconfigured. |
| **Operational failure** | The control is correctly designed and deployed but is not being operated : alerts are ignored, reviews are skipped, evidence is stale. | SIEM alerts fire for privileged account anomalies but the investigation queue has a 14-day backlog. |
| **Coverage failure** | The control works where it is deployed but does not cover assets or environments that need it. | Endpoint EDR covers workstations but not the jump hosts used to access OT environments. |

Each failure mode requires a different fix: redesign, re-implementation, operational discipline, or scope expansion. Knowing that a control is ineffective is not enough; the program must know why, so the fix addresses the root cause.

### 2.2 The Distinguishing Question

For each control, the program must answer two questions:

1. **Implementation:** Is the control in place? (CB-001 answers this)
2. **Effectiveness:** Is the control producing its intended risk reduction? (This framework answers this)

A control that cannot answer the second question is not yet at Adaptive maturity, regardless of its implementation status.

---

## 3. Effectiveness Measurement Model

### 3.1 Core Principle

Every control family must have at least one effectiveness metric that is distinct from its implementation metric. The implementation metric confirms presence; the effectiveness metric confirms performance.

### 3.2 Metric Design Rules

1. **Effectiveness metrics are outcome-oriented.** "Access reviews completed on time" is an implementation metric. "Percentage of access reviews that resulted in access reduction" is an effectiveness metric : it measures whether the review is detecting and correcting real access creep.
2. **Effectiveness metrics have thresholds.** A metric without a threshold is a measurement without a decision. Each effectiveness metric defines green, amber, and red bands.
3. **Effectiveness metrics are trended.** A single-point effectiveness reading is nearly useless. Direction and rate of change tell the story.
4. **Effectiveness metrics trigger action.** When an effectiveness metric goes red, it triggers a control failure analysis (Section 5) and potentially an improvement register entry (IMPREG-001).

> **The Signal-to-Noise Rule**
>
> An effectiveness metric that is always green is not measuring enough. An effectiveness metric that is always red is measuring too coarsely. The right metric produces a signal: it is green most of the time, amber when something needs attention, and red when the program must intervene. If the metric never moves, recalibrate the threshold.

---

## 4. Control Family Effectiveness Metrics

For each control family in the baseline (CB-001 Section 3), the table below defines the effectiveness metric and distinguishes it from the implementation metric already tracked.

### 4.1 Access Control (AC)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| JML log present; recertification report exists; access reviews completed on schedule | **AC-EFF-001: Access Recertification Reduction Rate.** Percentage of recertification cycles where at least one access entitlement was reduced or removed per system. | If every recertification cycle confirms existing access without reduction, the review is confirming the status quo, not detecting access creep. Target: >= 70% of recertification cycles produce at least one reduction. |
| Privileged account inventory maintained | **AC-EFF-002: Privileged Session Anomaly Investigation Rate.** Percentage of flagged privileged session anomalies that received investigation within SLA. | Alerts are implementation. Investigation is effectiveness. Target: >= 95% of flagged anomalies investigated within SLA. |

### 4.2 Configuration Management (CM)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| Baseline applied; drift rate reported | **CM-EFF-001: Mean Time to Remediate Drift.** Mean hours from drift detection to drift remediation, segmented by severity. | If drift is detected in 2 hours but remediated in 30 days, the baseline is present but not enforcing. Target: Critical drift remediated within 24 hours; High within 7 days. |
| Change control records exist | **CM-EFF-002: Unauthorized Change Rate.** Percentage of detected changes that lacked a corresponding approved change record. | Measures whether the change control process actually controls changes. Target: < 2% unauthorized. |

### 4.3 Audit and Accountability (AU)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| SIEM source inventory; coverage report | **AU-EFF-001: Alert Investigation Rate.** Percentage of high-severity alerts that received investigation within SLA. | If alerts fire but nobody looks, detection is present but not effective. Target: >= 95% of high-severity alerts investigated within SLA. |
| Log sources onboarded | **AU-EFF-002: Detection Gap Discovery Rate.** Number of incidents where a detection rule should have fired but did not, per quarter. | The best measure of log coverage is whether incidents are missed. Target: zero un-detected incidents per quarter; each one triggers a detection gap analysis. |

### 4.4 Risk Assessment (RA)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| Risk register exists; risks scored | **RA-EFF-001: Risk Treatment Effectiveness Rate.** Percentage of risks where the residual score decreased at the next review after treatment was applied. | If risks are documented and treated but residual scores never improve, the RMF is documenting, not managing. Target: >= 60% of treated risks show residual score decrease. |
| Exceptions tracked | **RA-EFF-002: Exception Renewal Rate.** Percentage of expiring exceptions that are renewed vs. closed (remediated or accepted). | If every exception is renewed indefinitely, the exception process is a rubber stamp. Target: < 30% renewal rate. |

### 4.5 Contingency Planning (CP)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| Backup report; restore test exists | **CP-EFF-001: Restore Test RTO Compliance Rate.** Percentage of restore tests that met the defined RTO. | If tests pass but take longer than RTO, the plan is present but not viable. Target: >= 90% of restore tests meet RTO. |
| DR plan documented | **CP-EFF-002: DR Plan Currency.** Percentage of DR plans updated within the review cycle (12 months). | An outdated DR plan is an untested assumption. Target: 100% current. |

### 4.6 Supply Chain Risk (SR, mapped to CERG TPRM domain)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| Vendor tiered; questionnaire on file | **SR-EFF-001: Vendor Event Blind-Spot Rate.** Percentage of Critical vendors where a reportable supply chain event occurred without CERG advance notice or within-SLA detection. | Measures whether vendor monitoring actually detects trouble before it impacts the organization. Target: 0%. |
| SCCT defined | **SR-EFF-002: SCCT Activation Time.** Mean hours from trigger event to SCCT activation for Tier 1 vendors. | A supply chain crisis management team that takes 72 hours to convene is a paperwork exercise. Target: <= 4 hours. |

### 4.7 Incident Response Interface (IR)

| Implementation Metric (exists) | Effectiveness Metric (new) | Rationale |
|---|---|---|
| IR plan exists; contact list current | **IR-EFF-001: IR Plan Exercise Coverage.** Percentage of IR plan scenarios exercised within 18 months. | An IR plan that has not been exercised is an untested document. Target: >= 80% of scenarios exercised within 18 months. |

### 4.8 System and Communications Protection (SC), System and Information Integrity (SI), Identification and Authentication (IA)

These families map to multiple CERG standards (IT-001, NET-001, LM-001, CR-001, AC-001). Effectiveness metrics for these families are defined in their governing standards and reported through the metrics dashboard (MTR-001). This framework requires that each family have at least one effectiveness metric; the specific metric is defined in the standard that governs the family.

### 4.9 Cross-Family Effectiveness Summary

| NIST Family | CERG Owner | Implementation Tracked In | Effectiveness Metric ID | Effectiveness Metric Name |
|---|---|---|---|---|
| AC | Engineering | CB-001 Section 6 | AC-EFF-001 | Access Recertification Reduction Rate |
| AC | Engineering | CB-001 Section 6 | AC-EFF-002 | Privileged Session Anomaly Investigation Rate |
| CM | Engineering | CB-001 Section 6 | CM-EFF-001 | Mean Time to Remediate Drift |
| CM | Engineering | CB-001 Section 6 | CM-EFF-002 | Unauthorized Change Rate |
| AU | Risk | CB-001 Section 6 | AU-EFF-001 | Alert Investigation Rate |
| AU | Risk | CB-001 Section 6 | AU-EFF-002 | Detection Gap Discovery Rate |
| RA | Governance | CB-001 Section 6 | RA-EFF-001 | Risk Treatment Effectiveness Rate |
| RA | Governance | CB-001 Section 6 | RA-EFF-002 | Exception Renewal Rate |
| CP | Engineering | CB-001 Section 6 | CP-EFF-001 | Restore Test RTO Compliance Rate |
| CP | Engineering | CB-001 Section 6 | CP-EFF-002 | DR Plan Currency |
| SR (TPRM) | Risk | CB-001 Section 6 | SR-EFF-001 | Vendor Event Blind-Spot Rate |
| SR (TPRM) | Risk | CB-001 Section 6 | SR-EFF-002 | SCCT Activation Time |
| IR | Risk (interface) | CB-001 Section 6 | IR-EFF-001 | IR Plan Exercise Coverage |

Effectiveness metrics for AT, MA, MP, PE, PL, PM, PS, SA, SC, and SI families follow the same pattern: implementation tracked in CB-001 Section 6; effectiveness metric defined in the governing standard or this framework, to be populated as those standards mature.

---

## 5. Control Failure Analysis

When a control that is marked Implemented in CB-001 fails to prevent or detect an incident, a Control Failure Analysis is required. The analysis determines whether the failure was in design, implementation, operation, or coverage : and therefore what kind of fix is needed.

### 5.1 Trigger Events

A Control Failure Analysis is triggered by:

- An incident that occurred despite a relevant control being marked Implemented
- An adversarial validation finding that demonstrates a control bypass (PRC-AV-001)
- An audit finding where the evidence shows the control was present but ineffective
- An effectiveness metric in red for two consecutive reporting periods

### 5.2 Analysis Structure

The accountable pillar leader conducts the analysis within 14 days of the trigger. The output is a structured analysis document containing:

1. **Which control failed?** Control ID from CB-001, implementation status, evidence on file.
2. **What was the failure mode?** Design / Implementation / Operational / Coverage (per Section 2.1).
3. **Why did it fail?** Root cause : not the symptom. "The WAF didn't block the attack" is the symptom. "The WAF ruleset was not updated to cover API-based attacks because there is no process for WAF rule lifecycle management" is the root cause.
4. **Was this a one-off or a systemic weakness?** Does the same root cause affect other controls? (Yes / Maybe / No, with rationale.)
5. **What is the corrective action?** If design failure: redesign the control. If implementation failure: fix the deployment. If operational failure: restore discipline, potentially with automation. If coverage failure: expand scope.
6. **What program change prevents recurrence?** Beyond fixing the immediate control, what standard, procedure, or tooling change prevents this class of failure from recurring elsewhere? This feeds into the improvement register (IMPREG-001).

### 5.3 Routing

| Failure Mode | Corrective Action Owner | Program Change Routes To |
|---|---|---|
| Design | Pillar owner of the control | IMPREG-001 (control redesign) |
| Implementation | Engineering Pillar Leader | Operational fix; if systemic, IMPREG-001 |
| Operational | Procedure owner | Operational discipline restoration; if systemic, IMPREG-001 |
| Coverage | Pillar owner of the control | IMPREG-001 (scope expansion) |

### 5.4 Analysis Registry

A Control Failure Analysis Registry is maintained by the Governance Pillar Leader. It tracks: control ID, incident or trigger reference, failure mode, root cause, corrective action, program change IMPREG ID, and verification status. The registry is reviewed at the quarterly Lessons Aggregation Review (PRC-LL-001 Section 5).

---

## 6. Control Rationalization

An Adaptive program does not only add controls. It removes controls that no longer reduce risk. Control bloat : the accumulation of controls added over years without corresponding retirement : creates compliance overhead without security benefit and dilutes attention from controls that matter.

### 6.1 Rationalization Cadence

Control rationalization occurs annually as part of the control baseline review (GOV-CAL-001). The Governance Pillar Leader, with input from pillar leaders, reviews the entire control baseline for rationalization candidates.

### 6.2 Rationalization Criteria

A control is a candidate for retirement if it meets any of these criteria:

- **No trigger in 24 months.** The control has not been triggered, tested, or relevant to any incident, audit finding, or adversarial validation in 24 months. A control that never fires is either not needed or not being tested.
- **Persistently low effectiveness.** The control's effectiveness metric has been red for 4+ consecutive quarters and attempts to improve effectiveness have failed. If the program cannot make the control work, the control may be the wrong design for the environment.
- **Replaced by a superior control.** A new control, tool, or architecture makes the old control redundant. Example: a network segmentation rule that enforced separation between two environments that are now air-gapped at the physical layer.
- **Threat vector no longer applicable.** The threat the control was designed to address no longer exists in the current threat landscape. Example: a control designed for a protocol the organization no longer uses.

### 6.3 Rationalization Process

1. **Candidate identification.** Governance Pillar Leader identifies candidates per the criteria above.
2. **Impact assessment.** For each candidate: what other controls, procedures, or evidence packages depend on it? What regulatory requirement does it satisfy?
3. **Pillar review.** Engineering and Risk pillar leaders confirm the candidate does not address a threat they are actively managing.
4. **CISO approval.** Control retirement requires CISO approval.
5. **Catalog amendment.** Retired controls are moved to Retired status in CB-001 and the catalog (CAT-001). The retirement rationale is documented.
6. **Improvement register entry.** Retirements are recorded in IMPREG-001 as program improvements (type: Retirement).

> **Retirement Is Not Abandonment**
>
> A retired control is not deleted. It is moved to Retired status, the retirement rationale is documented, and the entry is retained for audit purposes. An assessor who asks "Why did you remove control X?" gets a documented answer with the date, rationale, and approver. A program that never retires a control is a program that has never critically examined its own portfolio.

---

## 7. Integration with Maturity Assessment

The maturity self-assessment (MAT-001) currently scores domains based on evidence of process definition, execution, measurement, and review. This framework adds a control effectiveness dimension to the Adaptive tier.

### 7.1 MAT-001 Scoring Amendment

For a domain to score Adaptive (Tier 4) in MAT-001, the following additional criteria apply:

- At least one control in the domain has a defined effectiveness metric (from this framework)
- The effectiveness metric has been measured for at least two consecutive quarters
- At least one effectiveness-driven program change has been made (if warranted by the metric) and recorded in the improvement register (IMPREG-001)
- A Control Failure Analysis has been completed for any control in the domain that failed to prevent or detect an incident (if such an incident occurred)

### 7.2 Evidence Requirements

To substantiate an Adaptive score in a domain, the assessor should expect to see:

- Effectiveness metric trend data (at least two quarters)
- The improvement register entry resulting from an effectiveness metric signal
- The Control Failure Analysis for any control failure in the domain (if applicable)
- Verification evidence that the improvement had the intended effect

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Governance Pillar Leader** | Owns this framework. Maintains the Control Failure Analysis Registry. Conducts the annual control rationalization review. Updates effectiveness metrics in MTR-001. |
| **Engineering Pillar Leader** | Defines and reports effectiveness metrics for Engineering-owned control families (AC, CM, CP, IA, MA, SC, SI). Conducts Control Failure Analyses for Engineering-owned controls. Participates in rationalization review. |
| **Risk Pillar Leader** | Defines and reports effectiveness metrics for Risk-owned control families (AU, IR-interface, SR/TPRM). Conducts Control Failure Analyses for Risk-owned controls. Participates in rationalization review. |
| **CISO** | Approves control retirements. Reviews the annual rationalization report. |
| **Risk Register Owner** | Links control failure analyses to risk register entries when a control failure creates or changes a risk. |
| **Adversarial Testing Lead** | Reports control bypass findings from adversarial validation as Control Failure Analysis triggers. |
| **Policy & Standards Manager** | Executes catalog and CB-001 amendments for retired controls. Updates cross-references. |

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CEF-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-26 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | (pending) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On control baseline revision |
| **Next Scheduled Review** | 2027-05-26 |
| **Frameworks** | NIST CSF 2.0 (ID.IM, PROTECT all categories); NIST 800-55; ISO/IEC 27004 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed controls |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-26 | Cyber Governance | Initial draft. Established the Control Effectiveness Framework: effectiveness metrics per control family, control failure analysis procedure, control rationalization process, and integration with the maturity self-assessment. Addresses NIST CSF Adaptive gap: measuring whether controls are working, not just whether they are in place. |