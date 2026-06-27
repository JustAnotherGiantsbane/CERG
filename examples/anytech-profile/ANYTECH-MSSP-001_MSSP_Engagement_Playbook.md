## MSSP ENGAGEMENT PLAYBOOK — AnyTech Adaptation
### Validation Framework · Evidence Sampling · Joint Exercises · SLA Oversight

---

| | |
|---|---|
| **Artifact ID** | ANYTECH-MSSP-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Public |
| **Owner** | Engineering Pillar Lead (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy (AnyTech) |
| **Supporting Documents** | [Operating Model](CERG-GOV-OM-001_Operating_Model_AnyTech.md) · [TPRM Procedure](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) · [Exposure Management](CERG-PRC-VM-001_Exposure_Management_Procedure_AnyTech.md) · [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) · [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) · [CERG Service Level Commitments](../../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |
| **Review Cycle** | Quarterly / On provider transition |
| **Frameworks** | NIST CSF 2.0 (GOVERN, DETECT, RESPOND, RECOVER) |
| **Environments** | AnyTech production environment — MSSP-scoped systems |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Who Does What: The 3-Person Engineering Team](#2-who-does-what-the-3-person-engineering-team)
3. [Evidence Sampling Framework](#3-evidence-sampling-framework)
4. [Joint Exercise Calendar](#4-joint-exercise-calendar)
5. [SLA Breach Escalation Workflow](#5-sla-breach-escalation-workflow)
6. [Alert Quality Review Procedure](#6-alert-quality-review-procedure)
7. [Communication and Escalation Paths](#7-communication-and-escalation-paths)
8. [Quarterly Business Review Inputs](#8-quarterly-business-review-inputs)
9. [New MSSP Transition Checklist](#9-new-mssp-transition-checklist)
10. [Common Anti-Patterns](#10-common-anti-patterns)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

AnyTech's Engineering team is 3 people. They do not operate a SOC, manage detection infrastructure, or tune SIEM rules. The MSSP does all of that. The Engineering team's job is to **validate that the MSSP is actually doing it**.

This playbook is the operational manual for that validation. It answers questions like:

- How do we know the MSSP is triaging alerts properly?
- How do we know SLAs are being met when we don't have direct access to their ticketing system?
- How do we exercise incident response without running our own IR?
- What happens when the MSSP misses an alert?
- How do we switch MSSPs without losing detection coverage?

This playbook assumes a single MSSP covers SOC and IR for AnyTech's production environment. If the MSSP structure changes — multiple MSSPs, co-managed SOC, internal SOC transition — update this playbook before those changes take effect.

### 1.1 What This Playbook Does Not Cover

- IT operations oversight (MSP) — see the [TPRM Procedure](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md)
- Incident business ownership (communication, regulatory notification) — see [Incident Business Ownership Procedure](ANYTECH-IR-001_Incident_Business_Ownership_Procedure.md)
- Risk scoring and acceptance — see [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md)

---

## 2. Who Does What: The 3-Person Engineering Team

| Role | MSSP Oversight Responsibility |
|---|---|
| Engineering Pillar Lead | Owns the MSSP relationship. Conducts quarterly business reviews. Approves SLA changes. Escalates unresolved breaches. |
| Security Engineer (Detection) | Samples alert quality weekly. Reviews closed alerts for triage accuracy. Tracks SLA compliance. Maintains the evidence sampling calendar. |
| Security Engineer (Infrastructure) | Verifies exposure coverage (systems the MSSP monitors match AnyTech's live asset inventory). Reviews MSSP onboarding of new systems. Coordinates with MSP on asset visibility. |

### 2.1 Time Allocation

Each engineer allocates approximately **4 hours per week** to MSSP validation activities:

| Activity | Frequency | Engineer | Hours |
|---|---|---|---|
| Alert quality sample review | Weekly (30 min) | Detection Engineer | 2 |
| SLA compliance check | Weekly (15 min) | Detection Engineer | 1 |
| Exposure coverage verification | Biweekly (45 min) | Infrastructure Engineer | 1.5 |
| Evidence sampling | Monthly (2 hrs) | Detection Engineer | 2 |
| Joint exercise participation | Quarterly (4 hrs) | All 3 Engineers | 4 per quarter |
| Quarterly business review prep | Quarterly (2 hrs) | Engineering Lead | 8 per quarter |

---

## 3. Evidence Sampling Framework

The Engineering team cannot inspect MSSP systems directly. Validation is performed through **evidence the MSSP provides on a defined cadence**.

### 3.1 Evidence Categories

| Category | What It Proves | Sampling Cadence |
|---|---|---|
| Closed alert samples | Triage accuracy, classification quality, escalation appropriateness | Weekly (5 random closed alerts per severity tier) |
| SLA compliance report | Response and resolution times met per contract terms | Monthly (aggregate report from MSSP) |
| Detection coverage map | All scoped systems have active monitoring coverage | Monthly (cross-reference MSSP coverage list against asset inventory) |
| Incident report quality | Post-incident reports meet documentation standards | Per incident (review within 5 business days of closure) |
| Rule/detection change log | MSSP detection tuning is appropriate and documented | Monthly |
| Access review log | MSSP personnel access to AnyTech environment is current and appropriate | Quarterly |

### 3.2 Weekly Alert Quality Sample

The Detection Engineer selects **5 closed alerts per severity tier** (Critical, High, Medium) each week — 15 total. For each alert, evaluate:

| Criteria | Pass | Fail |
|---|---|---|
| Classification matches the event | Alert category is correct | Misclassified |
| Triage notes are complete | Analyst documented their reasoning | Notes are absent or boilerplate |
| Escalation was appropriate | True positives escalated; false positives documented | Missed escalation or unnecessary escalation |
| Containment or referral happened | Action was taken or a ticket was created | No action, no referral |
| Alert-to-incident linkage (if applicable) | Alert is linked to an incident case | No linkage for a true positive |

### 3.3 Monthly Evidence Sampling

Once per month, conduct a deeper validation:

1. Request 20 random closed alerts from the previous month (stratified by severity)
2. Request 3 full incident reports from the previous quarter (if available)
3. Request the MSSP's detection coverage map and cross-reference against AnyTech's current asset inventory
4. Request the MSSP's rule change log for the past 30 days
5. Score each category on a 3-point scale: **Compliant**, **Needs Improvement**, **At Risk**

Any category scoring **At Risk** triggers a review within 5 business days. Two consecutive **Needs Improvement** scores in the same category also trigger a review.

---

## 4. Joint Exercise Calendar

Since AnyTech does not run its own IR operations, exercises must be joint with the MSSP.

| Frequency | Exercise Type | Participants | Objectives |
|---|---|---|---|
| Quarterly | Tabletop (MSSP-led) | MSSP IR team + AnyTech Engineering | Test communication paths, decision escalation, notification timelines. MSSP presents inject; AnyTech practices business-owner decisions. |
| Semi-annual | Full simulation (joint) | MSSP IR team + AnyTech Engineering + IT Director | End-to-end scenario: detection, containment, eradication, business notification, recovery, lessons learned. |
| Annual | Adversarial simulation | MSSP red team or 3rd party | Test detection coverage, analyst response quality, escalation paths, and recovery procedures without advance notice. |
| Annual | Ransomware recovery drill | MSSP IR + MSP + AnyTech Engineering | Test backup restoration, communication during extended outage, and business continuity coordination. |

### 4.1 Exercise Output Requirements

Every exercise must produce:

- **Exercise plan** (scenario, injects, participants, timeline) — distributed 2 weeks before
- **Findings register** — what went well, what went wrong, improvement items with owners
- **Updated procedures** — changes to playbooks, contact lists, or escalation paths within 10 business days
- **SLA validation data** — response and resolution times measured during the exercise, compared against contractual SLAs

---

## 5. SLA Breach Escalation Workflow

### 5.1 SLA Tiers (Example — Calibrate to Your Contract)

| Tier | Alert Type | Response SLA | Resolution SLA |
|---|---|---|---|
| P1 | Critical — active compromise, data loss, service outage | 15 min | 4 hours |
| P2 | High — confirmed vulnerability, privilege escalation, malware | 30 min | 8 business hours |
| P3 | Medium — suspicious activity, policy violation, scanning | 2 hours | 24 business hours |
| P4 | Low — informational, false positive confirmed | 4 hours | 5 business days |

### 5.2 Breach Tiers

| Breach | Definition | Action |
|---|---|---|
| Minor | Single missed SLA within a 30-day window | Document in quarterly review tracker. No escalation. |
| Repeat | Same SLA tier missed twice in 30 days | Meeting request to MSSP account manager. Written remediation plan due in 10 business days. |
| Significant | Any P1 SLA breach, or 3+ breaches across tiers in 30 days | Engineering Lead escalates to IT Director. Formal breach notice under contract. Compensating controls review. |
| Critical | P1 breach with material impact, or pattern of 5+ breaches in 90 days | Executive escalation. Contract remedy evaluation. Parallel MSSP evaluation initiated. |

### 5.3 Escalation Chain

```
Alert → MSSP acknowledges (per SLA)
  → AnyTech Detection Engineer notified
    → SLA missed? → Document breach tier
      → Minor? → Log and track
      → Repeat/Significant? → Engineering Lead calls MSSP account manager
        → Not resolved in 10 days? → IT Director escalates
          → Critical pattern? → Legal + procurement notified
```

---

## 6. Alert Quality Review Procedure

### 6.1 Weekly Review Cadence

The Detection Engineer conducts a 30-minute weekly review:

1. Pull the MSSP's alert summary for the past 7 days
2. Select 5 closed alerts per severity tier (Critical, High, Medium)
3. Evaluate each against the criteria in §3.2
4. Document scores in the quality tracker
5. If 3 or more alerts fail in a single week, schedule a review call with the MSSP SOC lead

### 6.2 Monthly Scoring

At month end, aggregate the weekly scores:

| Score | Definition |
|---|---|
| 90-100% | Compliant — alert triage quality meets expectations |
| 75-89% | Needs Improvement — discuss trends in monthly call |
| Below 75% | At Risk — formal review required, remediation plan due |

### 6.3 Quarterly Trend Report

Each quarter, the Detection Engineer compiles:

- Alert quality trend (weekly scores over the quarter)
- SLA compliance by tier
- Common misclassification patterns
- Rule change frequency and quality
- Open improvement items from prior quarters

This report feeds into the [Quarterly Provider Review](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md).

---

## 7. Communication and Escalation Paths

### 7.1 Routine Communication

| Frequency | Channel | Participants | Purpose |
|---|---|---|---|
| Weekly | Email / shared tracker | Detection Engineer ↔ MSSP SOC lead | Alert quality scores, open items |
| Monthly | Video call | Engineering Lead + Detection Engineer ↔ MSSP account manager | SLA compliance, trends, upcoming changes |
| Quarterly | Video call (structured) | All 3 AnyTech engineers ↔ MSSP team | Business review — see [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) |

### 7.2 Incident Communication

| Event | Channel | Participants | SLA |
|---|---|---|---|
| Critical alert (P1) | Phone call + ticket | MSSP IC → AnyTech Engineering Lead | Within 15 min |
| Incident declaration | Phone call + ticket | MSSP IC → AnyTech Engineering Lead | Within 30 min of declaration |
| Status updates | Every 2 hours during active incident | MSSP IC → AnyTech Engineering Lead | Per incident severity |
| Post-incident report | Written report | MSSP → AnyTech Engineering Lead | Within 5 business days of closure |
| Lessons learned | Video call | MSSP IR team + AnyTech Engineering + IT Director | Within 10 business days of closure |

### 7.3 Escalation After Hours

| Tier | AnyTech Contact | Backup Contact |
|---|---|---|
| P1 / Incident declaration | Engineering Lead (on-call rotation) | IT Director |
| P2 | Detection Engineer (on-call) | Engineering Lead |
| P3 | Next business day | — |

---

## 8. Quarterly Business Review Inputs

The Engineering Lead prepares these inputs for each [Quarterly Provider Review](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md):

1. **Alert quality scorecard** — weekly and monthly scores, trend vs. prior quarter
2. **SLA compliance report** — breaches by tier, response vs. resolution, trend
3. **Incident summary** — incidents declared, response quality, post-incident report timeliness
4. **Detection coverage report** — systems monitored, changes to coverage, gaps identified
5. **Exercise summary** — exercises conducted, findings, improvement item status
6. **Open improvement items** — items from prior reviews and their status
7. **Risk register impact** — any new or changed risks driven by MSSP performance
8. **Recommendation** — retain, remediate, or retest?

---

## 9. New MSSP Transition Checklist

When onboarding a new MSSP (or renegotiating with the current one), complete each item before the transition date:

- [ ] Define monitoring scope — systems, environments, alert categories, severity tiers
- [ ] Establish SLAs for each tier (response, resolution, notification)
- [ ] Define evidence sampling expectations and cadence
- [ ] Agree on joint exercise schedule for the first 12 months
- [ ] Establish communication channels and escalation paths
- [ ] Set up alert quality scoring criteria (§3.2)
- [ ] Configure automated notification for P1/P2 alerts
- [ ] Share contact lists and on-call rotations
- [ ] Conduct parallel-run period (minimum 2 weeks, both MSSPs active)
- [ ] Perform baseline evidence sample (first 2 weeks of alerts reviewed in depth)
- [ ] Update the Provider RACI (see [Provider RACI Extension](ANYTECH-RACI-001_Provider_RACI_Extension.md))
- [ ] Update this playbook if the engagement model differs from the standard
- [ ] Inform the MSP of the MSSP change and confirm handoff paths
- [ ] Schedule the first quarterly review on day 60 of the new engagement

---

## 10. Common Anti-Patterns

These are failure modes specific to a small Engineering team validating an MSSP. See the full catalog at [Provider Anti-Patterns](ANYTECH-ANTI-001_Provider_Anti_Patterns.md) for deeper analysis.

| Pattern | What It Looks Like | How to Avoid |
|---|---|---|
| Sampling drift | Same 5 engineers' alerts are reviewed every week | Rotate sample selection across shifts and teams |
| SLA report reliance | MSSP self-reports SLA compliance without independent validation | Spot-check a sample of timestamps against independent notifications |
| Exercise capture | MSSP always chooses the exercise scenario | AnyTech proposes the scenario in alternating quarters |
| Relationship capture | Engineer becomes friendly with MSSP analysts and stops challenging results | Rotate the lead validator every 12 months |
| Coverage atrophy | Asset inventory grows but the MSSP coverage list does not | Mandate monthly cross-reference between asset inventory and coverage map |

---

## 11. Document Control

| Field | Value |
|---|---|
| **Artifact ID** | ANYTECH-MSSP-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Lead (AnyTech) |
| **Approved By** | Engineering Pillar Lead |
| **Review Cycle** | Quarterly / On provider transition |
| **Next Scheduled Review** | 2026-09-27 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Engineering Pillar Lead | Initial release. Establishes the MSSP validation framework, evidence sampling schedule, SLA escalation workflow, and joint exercise calendar. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy (AnyTech) | `CERG-POL-001_Cybersecurity_Policy_AnyTech.md` | Parent policy |
| Operating Model (AnyTech) | `CERG-GOV-OM-001_Operating_Model_AnyTech.md` | Provider relationship framework |
| TPRM Procedure (AnyTech) | `CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md` | Vendor tiering and assessment |
| Exposure Management (AnyTech) | `CERG-PRC-VM-001_Exposure_Management_Procedure_AnyTech.md` | Detection coverage alignment |
| Provider RACI Extension | `ANYTECH-RACI-001_Provider_RACI_Extension.md` | Role accountability mapping |
| Quarterly Provider Review Kit | `ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md` | Review input/output structure |
| Incident Business Ownership | `ANYTECH-IR-001_Incident_Business_Ownership_Procedure.md` | CERG-side incident management |
| Service Level Commitments | `../../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` | SLA design methodology |

---
