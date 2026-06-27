## QUARTERLY PROVIDER REVIEW KIT — AnyTech Adaptation
### Structured Agenda · Evidence Sampling · SLA Review · Decision Templates

---

| | |
|---|---|
| **Artifact ID** | ANYTECH-REVIEW-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Public |
| **Owner** | Governance Pillar Lead (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy (AnyTech) |
| **Supporting Documents** | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) · [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) · [Risk Management Framework](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) · [Operating Model](CERG-GOV-OM-001_Operating_Model_AnyTech.md) |
| **Review Cycle** | Quarterly |
| **Frameworks** | NIST CSF 2.0 (GOVERN) |
| **Environments** | All AnyTech environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Quarterly Review Cycle](#2-quarterly-review-cycle)
3. [Pre-Review Preparation Checklist](#3-pre-review-preparation-checklist)
4. [Standard Meeting Agenda](#4-standard-meeting-agenda-90-minutes)
5. [Provider Scorecard Template](#5-provider-scorecard-template)
6. [Decision Templates](#6-decision-templates)
7. [Annual Deep-Dive Rotations](#7-annual-deep-dive-rotations)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

The Quarterly Provider Review is AnyTech's primary mechanism for structured oversight of its three providers (MSSP, MSP, training vendor). It is not a status update meeting. It is a **decision meeting** where each provider's performance is scored, risks are surfaced, and corrective actions are assigned.

This kit provides:
- A standard agenda that produces decisions, not discussion
- Scorecard templates calibrated for vendor-oversight (not internal operations)
- Decision templates for common review outcomes
- Annual deep-dive rotation to prevent the review from becoming routine

### 1.1 Participants

| Role | Required | Notes |
|---|---|---|
| IT Director | Yes | Risk acceptance authority. Makes retention/remediation/termination decisions. |
| Engineering Pillar Lead | Yes | Presents MSSP scorecard |
| Risk Pillar Lead | Yes | Presents risk register changes and provider RACI status |
| Governance Pillar Lead | Yes | Presents evidence quality and compliance status. Facilitates the meeting. |
| MSSP Account Manager | Yes | Presents MSSP-side metrics. Attends for MSSP-specific segment. |
| MSP Account Manager | Required for 2 reviews/year | Attends for MSP-specific segment |
| Training Vendor Rep | Required for 1 review/year | Attends for training-specific segment |

---

## 2. Quarterly Review Cycle

```
Week 1-2:     Data collection
                → Each pillar lead gathers provider evidence for their domain
                → Detection Engineer compiles alert quality scores
                → Risk Lead updates risk register with provider-driven changes
                → Governance Lead compiles evidence calendar compliance

Week 3:       Pre-brief (30 min, CERG internal)
                → Pillar leads align on scores and recommendations
                → Surface disagreements before the provider attends
                → Identify the 2-3 most important decisions for this quarter

Week 4 (Q1-3): Quarterly Review (90 min, with providers)
                → Structured agenda (see §4)
                → Scorecards presented and discussed
                → Decisions recorded

Week 4 (Q4):   Annual Deep-Dive (half-day, with providers)
                → All of the above + annual rotation topic (§7)
                → Next-year priorities and scope changes
```

---

## 3. Pre-Review Preparation Checklist

### 3.1 Governance Lead (2 weeks before)

- [ ] Confirm meeting date with IT Director and all provider account managers
- [ ] Distribute evidence request to each provider (see §3.2)
- [ ] Confirm which providers will attend in person vs. video
- [ ] Review open improvement items from the previous review

### 3.2 Evidence Requests to Providers

**To MSSP (due 10 business days before review):**

- [ ] SLA compliance report — by tier, for the past 90 days
- [ ] Alert volume and closure summary — total alerts by severity, mean time to triage, mean time to resolve
- [ ] Incident summary — incidents declared, classification, current status, post-incident report status
- [ ] Detection coverage map — systems monitored, changes since last quarter
- [ ] Rule/detection change log — new rules, modified rules, retired rules
- [ ] Exercise participation log — exercises conducted, participation rates, findings
- [ ] Personnel changes — new analysts, departing analysts, certifications
- [ ] Open improvement items — status updates on items from prior reviews

**To MSP (due 10 business days before, Q2 and Q4 reviews):**

- [ ] Patch compliance report — systems patched within SLA, overdue patches, critical patch mean time to apply
- [ ] Access review summary — user access changes, privilege changes, terminations processed
- [ ] Open tickets related to security — security-relevant tickets and their status
- [ ] System changes affecting security — new systems, decommissioned systems, configuration changes

**To Training Vendor (due 10 business days before, Q4 review):**

- [ ] Training completion rates — by role, by module
- [ ] Phishing simulation results — click rates, reporting rates, trend vs. prior year
- [ ] Content updates — new modules, updated content, regulatory alignment

### 3.3 Engineering Lead Preparation

- [ ] Compile alert quality scores from weekly samples (§3 of [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md))
- [ ] Calculate SLA compliance by tier
- [ ] Prepare detection coverage comparison (MSSP coverage vs. asset inventory)
- [ ] Review open improvement items for status
- [ ] Draft scorecard for MSSP (§4)

### 3.4 Risk Lead Preparation

- [ ] Identify any risk register entries triggered by provider performance
- [ ] Review the Provider RACI for drift since last quarter
- [ ] Prepare risk acceptance requests for IT Director decision

### 3.5 Governance Lead Preparation

- [ ] Compile evidence quality scores (based on provider-submitted evidence timeliness and completeness)
- [ ] Review policy exception requests
- [ ] Prepare the consolidated decision tracker from the previous review

---

## 4. Standard Meeting Agenda (90 minutes)

### 4.1 Opening (5 min)

- Review meeting purpose: decisions, not updates
- Confirm decisions needed from this session (3-5 max)
- Review previous review action item status

### 4.2 MSSP Scorecard Presentation (25 min)

Engineering Lead presents:

1. **Alert quality score** — aggregate of weekly sampling scores, trend vs. prior quarter
2. **SLA compliance** — breaches by tier, response vs. resolution, trend
3. **Incident summary** — incidents this quarter, quality of post-incident reports
4. **Detection coverage** — coverage ratio, changes, gaps identified
5. **Open improvement items** — status, overdue items flagged

**Decision point:** Retain, Remediate, or Retest?

### 4.3 Risk and RACI Review (15 min)

Risk Lead presents:

1. **Risk register changes** — new or modified risks from provider performance
2. **RACI drift assessment** — any capabilities where provider scope changed without RACI update
3. **Risk acceptance requests** — items requiring IT Director sign-off

**Decision point:** Approve risk acceptance requests. Escalate unresolved RACI drift.

### 4.4 Evidence Quality and Compliance (10 min)

Governance Lead presents:

1. **Evidence submission compliance** — did providers submit on time and complete?
2. **Evidence quality score** — is the evidence usable for audit?
3. **Policy exception status** — any open exceptions, renewal decisions

**Decision point:** Renew or close policy exceptions.

### 4.5 Provider Response (15 min)

Provider account manager presents:

1. Response to AnyTech's scorecard
2. Provider's own improvement initiatives
3. Upcoming changes affecting AnyTech (personnel, tooling, scope)
4. Requests or escalations from provider to AnyTech

### 4.6 Decisions and Action Items (15 min)

1. Record decisions from each segment
2. Assign action items with owners and due dates
3. Confirm next review date and evidence requirements
4. Document in the decision tracker

### 4.7 Closed Session — CERG Only (5 min)

- Pillar leads + IT Director discuss any sensitive items not raised with providers present

---

## 5. Provider Scorecard Template

### MSSP Scorecard

| Category | Weight | Score (1-5) | Trend | Notes |
|---|---|---|---|---|
| Alert triage quality | 25% | | ↗ → ↘ | Based on weekly sampling scores |
| SLA compliance | 25% | | ↗ → ↘ | Breaches by tier |
| Incident response quality | 20% | | ↗ → ↘ | Post-incident report quality, timeliness |
| Detection coverage | 15% | | ↗ → ↘ | Coverage ratio, gap closure rate |
| Evidence quality | 10% | | ↗ → ↘ | Submission timeliness, completeness |
| Collaboration | 5% | | ↗ → ↘ | Communication quality, improvement receptiveness |
| **Weighted total** | **100%** | | | |

**Scale:** 5 = Exceeds expectations, 4 = Meets expectations, 3 = Needs minor improvement, 2 = Needs significant improvement, 1 = At risk

### MSP Scorecard

| Category | Weight | Score (1-5) | Trend | Notes |
|---|---|---|---|---|
| Patch compliance | 30% | | ↗ → ↘ | Systems patched within SLA |
| Access management | 25% | | ↗ → ↘ | Timeliness of access changes, terminations |
| Security ticket resolution | 20% | | ↗ → ↘ | Mean time to resolve security-relevant tickets |
| System hygiene | 15% | | ↗ → ↘ | Configuration compliance, decommissioning |
| Collaboration | 10% | | ↗ → ↘ | Communication, security awareness |
| **Weighted total** | **100%** | | | |

### Overall Thresholds

| Score | Rating | Action |
|---|---|---|
| 4.0-5.0 | Green | Retain. Continue oversight at current cadence. |
| 3.0-3.9 | Yellow | Remediate. Increase monitoring cadence. Remediation plan due in 30 days. |
| 2.0-2.9 | Orange | Escalate. IT Director review. Compensating controls. 90-day improvement plan. |
| Below 2.0 | Red | Terminate. Begin transition to alternative provider. Legal notified. |

---

## 6. Decision Templates

### Retain Decision

```
Provider: [Name]
Decision: Retain
Period: Q[X] [Year] — Q[X] [Year]
Rationale: Score ≥ 4.0, no material concerns
Conditions: Continue standard oversight cadence
Signed: [IT Director]
Date: [Date]
```

### Remediate Decision

```
Provider: [Name]
Decision: Remediate
Issue: [Describe the specific performance gap]
Root Cause: [Provider's stated root cause]
Remediation Plan:
  1. [Action]
  2. [Action]
  3. [Action]
Owner: [Provider-side owner] | Validator: [CERG owner]
Due Date: [Date]
Interim Compensating Controls: [What CERG does in the meantime]
Escalation Trigger: [Condition that promotes to terminate discussion]
Signed: [IT Director]
Date: [Date]
```

### RACI Change Decision

```
Capability: [Name]
Previous RACI: [Provider: D, CERG: —]
New RACI: [Provider: D, CERG: V]
Rationale: [Why the change is needed]
Validation Method: [How CERG will validate going forward]
Effective Date: [Date]
Signed: [IT Director]
Date: [Date]
```

---

## 7. Annual Deep-Dive Rotations

Each Q4 review includes one deep-dive topic beyond the standard agenda. Rotate annually:

| Year | Deep-Dive Topic | Lead | Output |
|---|---|---|---|
| Year 1 | **Provider RACI reconciliation** — full walk-through of every capability with all three providers present. Validate every D/V/O mapping against current contracts and operations. | Risk Lead | Updated RACI matrix. RACI drift inventory. |
| Year 2 | **Joint tabletop exercise** — 2-hour scenario during the review (not separate from it). Observe how providers coordinate during an incident. | Engineering Lead | Exercise findings register. Handoff gap analysis. |
| Year 3 | **Evidence quality audit** — deep sample of provider evidence across all categories. Audit evidence against the CERG Evidence Quality Standard. | Governance Lead | Evidence quality report. Evidence calendar update. |
| Year 4 | **Contract and scope alignment** — review all three provider contracts against current operations. Any scope drift not reflected in contracts? Any SLAs that no longer fit? | IT Director | Contract amendment recommendations. Scope alignment report. |

---

## 8. Document Control

| Field | Value |
|---|---|
| **Artifact ID** | ANYTECH-REVIEW-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Governance Pillar Lead (AnyTech) |
| **Approved By** | Governance Pillar Lead |
| **Review Cycle** | Quarterly |
| **Next Scheduled Review** | 2026-09-27 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Governance Pillar Lead | Initial release. Establishes the quarterly provider review framework, scorecard templates, decision templates, and annual deep-dive rotation for AnyTech's vendor-oversight model. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy (AnyTech) | `CERG-POL-001_Cybersecurity_Policy_AnyTech.md` | Parent policy |
| MSSP Engagement Playbook | `ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md` | Evidence sampling and SLA review methodology |
| Provider RACI Extension | `ANYTECH-RACI-001_Provider_RACI_Extension.md` | RACI baseline reviewed each quarter |
| Risk Management Framework (AnyTech) | `CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md` | Risk register and acceptance |
| Operating Model (AnyTech) | `CERG-GOV-OM-001_Operating_Model_AnyTech.md` | Provider relationship framework |
| CERG Service Level Commitments | `../../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` | SLA design methodology |

---
