## CERG SERVICE-LEVEL COMMITMENTS
### What the Business Can Expect Back From CERG · Reciprocal, Published, Measured

---

| | |
|---|---|
| **Document ID** | CERG-GOV-SLC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Chief Information Security Officer |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) · [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md) · [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) |
| **Review Cycle** | Annual / On engagement-model change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Service Commitment Catalog](#3-service-commitment-catalog)
   - 3.6 [What a missed commitment looks like in practice](#36-what-a-missed-commitment-looks-like-in-practice)
4. [Escalation Path for Missed Commitments](#4-escalation-path-for-missed-commitments)
5. [What This Is Not](#5-what-this-is-not)
6. [Metrics and Reporting](#6-metrics-and-reporting)
7. [Roles and Responsibilities](#7-roles-and-responsibilities)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG's operating premise is the yes-and default in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §2.2: the hard work is making "yes" safe, and guardrails should make the business move faster, not slower. The entire framework is built on engaging Engineering early, understanding exposure, and making the rules clear enough that work moves.

There is an asymmetry in how that premise is currently operationalized. Every service-level clock in the framework runs against the business: findings have remediation SLAs, exceptions have aging limits, patch currency is tracked. CERG's own responsiveness back to the business, how fast it answers an architecture review request, dispositions an intake, or responds to an advisory question, is measured only by an annual stakeholder perception survey ([`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md)). By the time that annual survey reports friction, the business has already built its workarounds. Shadow IT and shadow AI are what a slow security function produces.

This document corrects the asymmetry. It publishes CERG's reciprocal commitments: for every clock CERG runs against the business, CERG runs a clock against itself. It applies to every CERG engagement model in OM-001 §5 (Project, Continuous Service, Advisory, Program Oversight).

> **A Slow Yes Is a No**
>
> "Make yes safe" only enables the business if yes is also fast. A security function that takes three weeks to answer a question has, in practice, said no, because the business has already moved without it. Publishing a clock on ourselves is how we prove the yes-and philosophy is a commitment and not a slogan.

---

## 2. Principles

Five principles govern CERG's service commitments:

1. **Reciprocity.** For every service-level clock CERG runs against the business, CERG runs a clock against itself. Accountability is symmetric.
2. **Tiered.** Commitments scale by request criticality and project tier, not one-size-fits-all. A high-impact regulated project and a minor internal tool do not get the same clock.
3. **Published.** Commitments are visible to the business, not internal targets. The business is entitled to know what to expect and to escalate when it does not get it.
4. **Measured.** Every commitment maps to a metric in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) and is reported alongside, and with equal weight to, the discipline metrics that measure the business.
5. **Escalation, not silence.** A missed commitment triggers a defined escalation, never a silent delay. A request that will miss its commitment is surfaced before the clock expires, not after.

---

## 3. Service Commitment Catalog

The turnaround values below are **preliminary defaults requiring organizational calibration**, following the calibration pattern in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §12. They are starting points for a mid-size organization; each organization calibrates them to its own staffing and demand, and the CISO approves the calibrated set. Business days are used throughout.

### 3.1 Project Engagement (Engineering-Led, OM-001 §5.1)

| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |
|---|---|---|---|---|
| Architecture review intake acknowledgement | All projects | Acknowledge and assign a reviewer within 2 business days | Auto-notify Engineering Pillar Leader | SR-003 |
| Architecture review disposition | Tier 1 (high-impact / regulated / OT / AI) | Disposition within 10 business days of complete intake | Engineering Pillar Leader, then CISO | SR-001 |
| Architecture review disposition | Tier 2 (standard) | Disposition within 7 business days | Engineering Pillar Leader | SR-001 |
| Architecture review disposition | Tier 3 (minimal) | Disposition within 5 business days | Engineering Pillar Leader | SR-001 |

### 3.2 Continuous Service (Risk-Led, OM-001 §5.2)

| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |
|---|---|---|---|---|
| Bring a new asset under vulnerability / CSPM coverage | Post go-live | Coverage established within 5 business days of go-live notification | Risk Pillar Leader | SR-005 |

### 3.3 Advisory (Cross-Pillar, OM-001 §5.3)

| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |
|---|---|---|---|---|
| Advisory or office-hours question | All | Substantive written response within 3 business days | Owning Pillar Leader | SR-002 |
| New SaaS / cloud service review | Restricted-data placement | Decision within 10 business days | Governance + Engineering, then CISO | SR-003 |
| New SaaS / cloud service review | Non-Restricted | Decision within 5 business days | Owning Pillar Leader | SR-003 |

### 3.4 Program Oversight and Risk Decisions (Governance-Led, OM-001 §5.4)

| Request type | Tier / trigger | CERG commitment (preliminary default) | Escalation if missed | Metric |
|---|---|---|---|---|
| Exception / risk-acceptance request intake | All | Acknowledge and route to the correct approver within 3 business days | Risk Register Owner | SR-004 |

> **Intake clock, not decision clock.** The commitment in §3.4 is to acknowledge and route the request promptly. The decision authority and the substantive risk judgment remain with the approver named in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. SLC commitments govern CERG's responsiveness; they never compress or override a risk decision.

### 3.5 Adoption-Phase SLA Targets

The commitment values in §3.1–§3.4 are mature-program targets. New adopters progress through adoption gates; SR metrics use the phase-adjusted targets below until the program reaches Gate 3. Phase context is reported on the CISO Dashboard.

| Phase | Architecture Review (SR-001) | Advisory Response (SR-002) | Intake Disposition (SR-003) | Time-to-Coverage (SR-005) |
|-------|----------------------------|---------------------------|----------------------------|--------------------------|
| **Gate 1 (Spine, 0–90 days)** | 15 business days | 10 business days | 15 business days | 15 business days |
| **Gate 2 (Operating, 90–180 days)** | 10 business days | 5 business days | 10 business days | 10 business days |
| **Gate 3+ (Governed / Adaptive)** | Per §3.1 (10 / 7 / 5 business days by tier) | Per §3.3 (3 business days) | Per §3.1 / §3.3 | Per §3.2 (5 business days) |

> **Phase Advancement.** Advancement from one gate to the next is recorded in the adoption gates document ([`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md)) and communicated to the Cyber Oversight Group. SR metric reporting switches to the next phase target upon confirmation of gate transition.

### 3.6 What a missed commitment looks like in practice

The SLA commitments above are not abstractions. They show up in real meetings. The worked example below is a fictional but realistic Tuesday morning scenario at a growing SaaS company in the second quarter of CERG Standard adoption. It illustrates what the §4 escalation path actually produces.

A product team submits a T1 architecture review intake for a new customer-facing analytics feature on a Tuesday at 9 a.m. The intake is logged in the Project Intake Record, tiered T1 because the workload is internet-facing and handles customer data, and routed to Engineering. Per §3.5 Gate 2, the SR-001 commitment is a 10-business-day architecture review turnaround.

By day 6, Engineering has not started the review. The intake sits in the queue behind two higher-priority reviews. Nobody on Engineering has acknowledged the delay to the product team. By day 9, the product manager pings Engineering directly. Engineering says "we'll get to it." By day 11, the 10-business-day commitment has been missed. No notification was sent per §4 step 1.

Here is what the §4 escalation path produces:

1. **Day 11 (commitment missed, no notification sent).** The Engineering Pillar Leader is auto-notified by the SR-001 metric breach. The single miss is logged. The Engineering Pillar Leader contacts the product manager the same morning with a revised date (day 14) and a reason ("behind on two other T1s; yours is next"). The revised date goes into the intake record.

2. **Day 14 (revised date met).** The architecture review is delivered. The SR-001 metric records the miss: the commitment clock was 10 business days, the actual was 14. Quality was acceptable; the product team got a useful review.

3. **End of month (single miss).** The Engineering Pillar Leader reviews the SR-001 trend. One miss in the month is within noise. No further action. The miss is in the dashboard.

4. **Quarter review (pattern).** If the same pillar has three or more misses in a quarter, the pattern surfaces to the CISO and the Cyber Oversight Group per §4 step 3. The CISO opens a discussion: is the published value mis-calibrated to capacity, or is the pillar overcommitted? The answer drives a workforce-planning or scoping decision, not a "try harder" instruction.

5. **Annual (systemic).** If the same pillar has chronic misses across two quarters, the CISO records a Program Improvement Register entry per §4 step 4 with source "SLC systemic miss, pillar X, YYYY." The improvement is owned at the CISO level, not the pillar level, because chronic misses signal a capacity gap CERG must fix.

The same pattern applies to every commitment in §3. The numbers are smaller or larger, the pillar is different, but the chain is the same: miss, log, communicate, escalate by pattern, address systemically.

The point of publishing these commitments is not to create a metric treadmill. The point is to make CERG's responsiveness visible so that friction is caught early, not when the business has built workarounds. A single miss is acceptable. A pattern is a finding. Chronic is a program-level problem.

For a 90-day narrative that includes the first SR-001 miss in a real adoption arc, see [Story 10 (The new CISO's first 90 days)](../examples/day-in-the-life/story-10-new-ciso-90-days.md). For the worked example of how a business-side SLA breach is handled by Risk, see [Story 2 (Critical vulnerability)](../examples/day-in-the-life/README.md#story-2-critical-vulnerability).

---

## 4. Escalation Path for Missed Commitments

When CERG misses, or forecasts that it will miss, a published commitment:

1. **Before the clock expires:** the owning role notifies the requester that the commitment will be missed, with a revised date and reason. Silence is not permitted.
2. **On a miss:** the owning Pillar Leader is auto-notified. A single miss is logged.
3. **On repeated misses:** a pattern of misses in a service category surfaces to the CISO and to the Cyber Oversight Group, mirroring the escalation symmetry that applies to business-side SLA breaches.
4. **Systemic misses** are a CERG program finding and are recorded in the Program Improvement Register ([`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md)). A missed commitment is CERG's problem to fix, not the requester's problem to absorb. Chronic misses signal a capacity or process gap in CERG, addressed through workforce planning, not by quietly deprioritizing the business.

---

## 5. What This Is Not

- **Not a guarantee of "yes."** The commitment is to respond within the clock, not to approve. A fast, documented "no" with a path forward satisfies the commitment fully.
- **Not a bypass of rigor.** SLC commitments never justify a shallow architecture review or a rubber-stamp risk decision. Speed is measured alongside quality, and the anti-shallow-metrics guardrails in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §8 apply. A fast review that misses a material risk is a failure, not a success.
- **Not a substitute for prioritization.** When demand exceeds capacity, CERG triages by risk and business criticality and communicates the revised dates per Section 4. It does not silently let the lowest-priority requests rot.

---

## 6. Metrics and Reporting

Every commitment in Section 3 maps to a CERG Service Responsiveness metric (SR-001 through SR-005) defined in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md). These metrics are reported on the CISO dashboard with equal standing to the business-discipline metrics, and SR-004 (SLC Commitment Adherence) is reported to the Cyber Oversight Group and the board. The annual stakeholder perception survey ([`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md)) provides the qualitative companion to these continuous quantitative measures, so friction is caught monthly rather than once a year.

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **CISO** | Owns this document; approves the calibrated commitment values; owns board-level SLC adherence reporting. |
| **Engineering Pillar Leader** | Accountable for project-engagement and architecture-review commitments (§3.1) and their misses. |
| **Risk Pillar Leader** | Accountable for continuous-service coverage commitments (§3.2). |
| **Governance Pillar Leader** | Accountable for advisory and program-oversight commitments (§3.3, §3.4) and for SLC reporting. |
| **Risk Register Owner** | Accountable for exception / risk-acceptance intake routing (§3.4). |

---

## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-SLC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Approved By** | CISO |
| **Owner** | Chief Information Security Officer |
| **Next Review** | Annual / On engagement-model change |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.0 | 2026-06-12 | CISO | Initial publication. Establishes CERG's reciprocal, published, measured service-level commitments back to the business, with an escalation path for misses and a mapping to MTR-001 SR-series metrics. |

### Review Triggers

- Annual scheduled review.
- Change to any OM-001 §5 engagement model.
- Calibration of the preliminary default turnaround values.
- A pattern of missed commitments indicating the published values are mis-calibrated to capacity.

### Related Documents

- [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) - Operating Model (engagement models)
- [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) - Metrics and Reporting (SR-series metrics)
- [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) - Cross-Pillar Operational Flows (F-02 intake)
- [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - Architecture Review and Project Intake
- [`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md) - Stakeholder Perception Survey
- [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) - Program Improvement Register
