## INCIDENT BUSINESS OWNERSHIP PROCEDURE — AnyTech Adaptation
### CERG / MSSP Boundary · Business Impact · Notification · Remediation Tracking

---

| | |
|---|---|
| **Artifact ID** | ANYTECH-IR-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Public |
| **Owner** | Engineering Pillar Lead (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy (AnyTech) |
| **Supporting Documents** | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) · [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) · [Risk Management Framework](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) · [Incident Response Plan](../../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) · [Incident Response Playbook Set](../../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) |
| **Review Cycle** | Quarterly / On MSSP transition |
| **Frameworks** | NIST CSF 2.0 (RESPOND, RECOVER) |
| **Environments** | All AnyTech environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Boundary Model: MSSP IR Operations vs. CERG Business Ownership](#2-boundary-model-mssp-ir-operations-vs-cerg-business-ownership)
3. [Incident Declaration and Notification](#3-incident-declaration-and-notification)
4. [Business Impact Assessment](#4-business-impact-assessment)
5. [Regulatory and Legal Notification](#5-regulatory-and-legal-notification)
6. [Root Cause and Remediation Tracking](#6-root-cause-and-remediation-tracking)
7. [Lessons Learned Procedure](#7-lessons-learned-procedure)
8. [Communication Templates](#8-communication-templates)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

AnyTech's MSSP owns IR operations: detection, triage, containment, eradication, and technical recovery. AnyTech's 8-person CERG team owns **incident business ownership**: business impact assessment, regulatory and legal notification, root cause tracking, remediation verification, and lessons learned.

This document defines the boundary between those two domains and provides the procedures CERG follows when an incident is declared. It does not replace the MSSP's IR playbooks — it defines the CERG side of the handoff.

### 1.1 When This Procedure Activates

This procedure activates when the MSSP declares an incident (not an alert — an incident). An incident is declared when:

1. Confirmed unauthorized access to a system or data
2. Confirmed malware execution on a production system
3. Confirmed denial of service affecting production services
4. Confirmed data exfiltration or unauthorized disclosure
5. Confirmed privilege escalation or account compromise of a privileged user
6. Any event the MSSP Incident Commander determines meets incident criteria

When the MSSP declares an incident, the MSSP IC follows their IR playbook for the technical response. The Engineering Pillar Lead simultaneously activates this procedure for the business ownership response.

---

## 2. Boundary Model: MSSP IR Operations vs. CERG Business Ownership

| Activity | MSSP IR Team | CERG Engineering Lead |
|---|---|---|
| Detection and triage | **Owns** — determines if event is an incident | Informed of declaration |
| Containment | **Owns** — executes containment actions | Informed of containment decisions |
| Eradication | **Owns** — removes threat from environment | Informed of eradication actions |
| Technical recovery | **Owns** — restores systems from backup | Coordinates with MSP for IT recovery |
| Forensic analysis | **Owns** — collects and analyzes evidence | Receives forensic report |
| **Business impact assessment** | **Inputs** — technical scope, affected systems, data types | **Owns** — business impact, financial impact, operational impact |
| **Regulatory notification** | **Inputs** — technical details, timeline | **Owns** — notification decisions, timing, content |
| **Legal notification** | **Inputs** — technical evidence | **Owns** — legal counsel notification, insurance notification |
| **Customer notification** | **Inputs** — technical scope of data exposure | **Owns** — notification decisions and content |
| **Root cause analysis** | **Drafts** — technical RCA | **Validates and owns** — accepts/rejects RCA, tracks remediation |
| **Remediation tracking** | **Inputs** — technical remediation steps | **Owns** — tracks closure, verifies remediation |
| **Lessons learned** | **Participates** — technical findings | **Owns** — facilitates session, tracks improvement items |
| **Post-incident reporting** | **Drafts** — technical incident report | **Owns** — final report for IT Director |

---

## 3. Incident Declaration and Notification

### 3.1 MSSP → CERG Notification

When the MSSP declares an incident, they notify the Engineering Pillar Lead within:

| Severity | Notification SLA | Channel |
|---|---|---|
| P1 (Critical) | 15 minutes | Phone call + ticket |
| P2 (High) | 30 minutes | Phone call + ticket |
| P3 (Medium) | 2 hours | Ticket + email |

### 3.2 CERG Internal Notification

Upon receiving incident notification, the Engineering Lead:

1. **Acknowledges** the notification to the MSSP IC
2. **Notifies** the IT Director within 30 minutes (P1) or 1 hour (P2)
3. **Assembles** the incident response cell:
   - Engineering Lead (incident business owner)
   - Infrastructure Engineer (remediation verification)
   - Risk Lead (risk register impact)
   - IT Director (notification decisions, escalation)
4. **Opens** an incident tracking record in the risk register
5. **Initiates** the Business Impact Assessment (§4)

### 3.3 Status Updates During Incident

| Interval | Update Content | From | To |
|---|---|---|---|
| Every 2 hours (P1) | Technical status, containment progress, ETA | MSSP IC | Engineering Lead |
| Every 4 hours (P2) | Technical status, containment progress, ETA | MSSP IC | Engineering Lead |
| Daily (P3) | Investigation status | MSSP IC | Engineering Lead |
| On change | Escalation, scope change, or new evidence | MSSP IC | Engineering Lead |

Engineering Lead provides consolidated status to IT Director on the same cadence.

---

## 4. Business Impact Assessment

The Business Impact Assessment (BIA) runs in parallel with the MSSP's technical response. It answers questions the MSSP cannot answer: what does this incident mean for the business?

### 4.1 BIA Template

| Field | Description | Source |
|---|---|---|
| **Incident ID** | CERG tracking ID | Engineering Lead |
| **MSSP Incident ID** | MSSP's reference | MSSP |
| **Systems affected** | Which systems are involved | MSSP IC |
| **Data types involved** | PII, PHI, financial, IP, operational | MSSP IC + CERG system owner |
| **User impact** | Which users are affected, how | CERG business contact |
| **Operational impact** | Is any business process disrupted | CERG business contact |
| **Financial impact estimate** | Direct costs, recovery costs, potential liability | Engineering Lead + IT Director |
| **Regulatory exposure** | Which regulations may be triggered | Risk Lead |
| **Customer notification required** | Yes/No — based on data type and legal obligation | IT Director + Legal |
| **Insurance notification required** | Yes/No | IT Director |
| **PR/communication need** | Internal or external communication needed | IT Director |

### 4.2 BIA Completion SLA

| Severity | BIA Due |
|---|---|
| P1 | Within 4 hours of incident declaration |
| P2 | Within 24 hours |
| P3 | Within 5 business days |

---

## 5. Regulatory and Legal Notification

### 5.1 Notification Decision Tree

```
Does this incident involve PII, PHI, or regulated data?
  → No → Document decision, no regulatory notification
  → Yes → Can we confirm data was accessed or exfiltrated?
    → No → Monitor, document assumptions, re-evaluate if evidence emerges
    → Yes → Which regulations apply?
      → GDPR → Notify DPA within 72 hours of confirmation
      → CMMC → Notify PO within 30 days (if applicable)
      → SOX → Notify audit committee per breach policy
      → State breach notification → Notify per state timelines (typically 30-60 days)
```

### 5.2 Notification Content

Every notification (regulatory, legal, customer, insurance) must include:

1. Date and time of incident discovery
2. Date and time of confirmation
3. Type of data involved
4. Number of affected individuals (if applicable)
5. Containment actions taken
6. Remediation status
7. Contact information for follow-up

Engineering Lead drafts notification content. IT Director approves. Legal counsel reviews before external sending.

---

## 6. Root Cause and Remediation Tracking

### 6.1 RCA Review Process

1. MSSP delivers technical RCA within the SLA (5 business days for P1, 10 for P2, 15 for P3)
2. Engineering Lead reviews the RCA for completeness and accuracy
3. Infrastructure Engineer validates technical findings against any independent evidence
4. Engineering Lead accepts, rejects, or requests supplements to the RCA
5. Accepted RCA is recorded in the risk register as supporting evidence
6. Open remediation items are tracked in the remediation register

### 6.2 Remediation Register

| Incident ID | Finding | Remediation Action | Owner | Due Date | Verified | Status |
|---|---|---|---|---|---|---|
| INC-2026-001 | | | | | | |

Each remediation item must be verified by the CERG team (not self-reported by the provider) before closure. Verification methods:

| Finding Type | Verification Method |
|---|---|
| Configuration change | CERG reviews configuration evidence or screenshots |
| Process change | CERG observes the new process in operation |
| Tool addition | CERG confirms coverage in next detection coverage map |
| Training/awareness | CERG samples post-training competency |
| Policy change | CERG reviews the updated policy language |

---

## 7. Lessons Learned Procedure

### 7.1 Timing

| Severity | Lessons Learned Session | Report Due |
|---|---|---|
| P1 | Within 10 business days of incident closure | Within 15 business days |
| P2 | Within 15 business days | Within 20 business days |
| P3 | Combined with next quarterly review | Within 5 business days of session |

### 7.2 Session Format

Participants: Engineering Lead (facilitator), Infrastructure Engineer (technical reviewer), Risk Lead (process reviewer), MSSP IC (technical input), MSP rep (if IT systems involved).

Agenda:

1. **What happened** — timeline review (5 min)
2. **What went well** — what worked as expected (10 min)
3. **What went wrong** — gaps in detection, response, communication, process (20 min)
4. **Root cause** — confirm or challenge the technical RCA (10 min)
5. **Improvement items** — for each gap, assign an owner and due date (15 min)
6. **Evidence quality** — did the evidence from this incident meet the Evidence Quality Standard? (5 min)

### 7.3 Output

- Improvement items added to the Program Improvement Register
- Procedure updates (if needed) submitted within 10 business days
- Lessons learned summary distributed to the IT Director
- If the same gap appears in two consecutive incidents, it becomes a program improvement item

---

## 8. Communication Templates

### 8.1 Internal Incident Notification (to IT Director)

```
Subject: [SEVERITY] Incident Declaration — [BRIEF DESCRIPTION]

Incident ID: CERG-INC-[YYYY]-[NNN]
Declared by: [MSSP Name]
Alert Type: [Alert type or vector]
Status: Active / Contained / Eradicated

Current Assessment:
- Systems affected: [list]
- Data types involved: [list]
- Business impact: [summary]
- Regulatory exposure: [yes/no, which]

Actions Taken:
- [Action 1]
- [Action 2]

Next Steps:
- [Step 1]
- [Step 2]

Expected Resolution: [ETA or TBD]
BIA Due: [Date/Time]
Next Update: [Date/Time]
```

### 8.2 Incident Closure Report (to IT Director)

```
Subject: Incident Closure Report — CERG-INC-[YYYY]-[NNN]

Summary:
- Incident: [Description]
- Duration: [Start] to [End]
- Severity: [P1/P2/P3]
- Root cause: [1-2 sentence summary]

Outcome:
- Containment: [When, How]
- Eradication: [When, How]
- Recovery: [When, Verified]

Business Impact:
- Operational: [Summary]
- Financial: [Estimate]
- Regulatory: [Notifications made or rationale for none]

Remediation Items:
- [Open items with owners and due dates]

Lessons Learned:
- [Key findings]

Attachments:
- MSSP incident report
- BIA
- RCA (if complete)
```

---

## 9. Document Control

| Field | Value |
|---|---|
| **Artifact ID** | ANYTECH-IR-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Lead (AnyTech) |
| **Approved By** | Engineering Pillar Lead |
| **Review Cycle** | Quarterly / On MSSP transition |
| **Next Scheduled Review** | 2026-09-27 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Engineering Pillar Lead | Initial release. Establishes the CERG/MSSP incident boundary model, business impact assessment procedure, regulatory notification decision tree, and lessons learned framework for AnyTech's vendor-oversight model. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy (AnyTech) | `CERG-POL-001_Cybersecurity_Policy_AnyTech.md` | Parent policy |
| MSSP Engagement Playbook | `ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md` | Evidence sampling and SLA methodology |
| Provider RACI Extension | `ANYTECH-RACI-001_Provider_RACI_Extension.md` | Incident response role mapping |
| Risk Management Framework (AnyTech) | `CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md` | Risk register and acceptance |
| Incident Response Plan | `../../plans/CERG-PLN-IR-001_Incident_Response_Plan.md` | Upstream IR governance |
| Incident Response Playbook Set | `../../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` | Upstream IR procedures |

---
