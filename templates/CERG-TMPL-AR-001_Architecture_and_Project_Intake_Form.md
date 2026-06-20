## ARCHITECTURE AND PROJECT INTAKE FORM
### Project Intake · Data Scope · Threat Modeling Trigger · Review Routing

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AR-001 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Document** | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - Architecture Review and Project Intake Procedure |
| **Supporting Documents** | [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 SA, RA, AC, SC |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [Fill-In Template](#3-fill-in-template)
4. [Review and Approval](#4-review-and-approval)
5. [Document Control](#5-document-control)

---

## 1. Purpose and Use

This form is the front-door intake artifact for the architecture review procedure. It captures enough information to route a project to the correct CERG review path, trigger threat modeling when needed, and identify data, vendor, regulatory, and deployment scope early.

This template does **not** replace the full architecture review record, threat model, pre-production security review, production handoff package, or go-live risk acceptance packet defined in [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) §§6-9. A completed intake form opens and routes the engagement; later procedure records close it.

> **The Intake Form Is the Front Door**
>
> Projects should not discover security requirements at the end. Intake is where ownership, data, architecture, vendors, identity, logging, and deployment risk become visible early enough to matter. Approval of this intake confirms routing, not production readiness or risk acceptance.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed field with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md).
5. Use the completed form to record scope determination, review path, and required follow-on artifacts.
6. Do not use the completed form as evidence of architecture approval, pre-production readiness, go-live authorization, or risk acceptance.
7. Link later risks, findings, exceptions, evidence, and approvals to the system of record.
8. Store the completed artifact in the evidence library governed by [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md).

---

## 3. Fill-In Template

### 3.1 Project Summary

| **Field** | **Value** |
|---|---|
| Intake ID | `[AR-YYYY-NNN]` |
| Project Name | `[Name]` |
| Request Date | `[Date]` |
| Business Owner | `[Owner]` |
| Technical Owner | `[Owner]` |
| Target Go-Live | `[Date]` |
| Project Type | `[New system / major change / SaaS / cloud / integration / AI / OT / other]` |
| Environment | `[Production / non-production / hybrid]` |

### 3.2 Scope and Data

| **Question** | **Answer** |
|---|---|
| What business process does this support? | `[Answer]` |
| What data classifications are involved? | `[Public / Internal / Confidential / Restricted / CUI]` |
| Is personal data involved? | `[Yes / No / Unknown]` |
| Is CUI involved? | `[Yes / No / Unknown]` |
| Is SOX, NERC-CIP, or contractual scope involved? | `[Scope]` |
| Are vendors or subprocessors involved? | `[Yes / No / Unknown]` |

### 3.3 Architecture and Control Triggers

| **Trigger** | **Yes / No / Unknown** | **Notes** |
|---|---|---|
| New internet-facing service | `[ ]` | `[Notes]` |
| New privileged access path | `[ ]` | `[Notes]` |
| New API or integration | `[ ]` | `[Notes]` |
| New cloud account, subscription, or tenant | `[ ]` | `[Notes]` |
| AI or automated decisioning | `[ ]` | `[Notes]` |
| OT, ICS, or safety impact | `[ ]` | `[Notes]` |
| New third party | `[ ]` | `[Notes]` |
| Threat model required | `[ ]` | `[Reason]` |

### 3.4 Review Routing

| **Review Area** | **Owner** | **Required** | **Outcome** |
|---|---|---|---|
| Architecture review | Engineering Pillar Leader | `[Yes / No]` | `[Outcome]` |
| Threat modeling | Application Security Engineer | `[Yes / No]` | `[Outcome]` |
| Vendor review | Vendor Risk Analyst | `[Yes / No]` | `[Outcome]` |
| Data governance | Governance Pillar Leader | `[Yes / No]` | `[Outcome]` |
| Risk review | Risk Pillar Leader | `[Yes / No]` | `[Outcome]` |

### 3.5 Intake Disposition and Follow-On Records

| **Disposition Field** | **Value** |
|---|---|
| Review Path | `[Mandatory / Lightweight / Out of Scope]` |
| SLC Tier | `[Tier 1 / Tier 2 / Tier 3 / N/A]` |
| Phase 2 Architecture Review Record Required | `[Yes / No; link when created]` |
| Threat Model Required | `[Yes / No; link when created]` |
| Phase 4 Pre-Production Security Review Required | `[Yes / No; link when created]` |
| Production Handoff Package Required | `[Yes / No; link when created]` |
| Risk Acceptance Packet Required | `[Yes / No; link when created]` |
| Intake Decision Rationale | `[Brief rationale for review path and required follow-on records]` |

### 3.6 Business Decision Box

| **Decision Question** | **Business Owner / System Sponsor Response** |
|---|---|
| What business outcome justifies this project or change? | `[Outcome and priority]` |
| What decision is needed from CERG now? | `[Route only / architecture review / go-live support / risk acceptance / other]` |
| What date is the business asking CERG to support? | `[Target date and driver]` |
| What happens if CERG identifies blocking findings? | `[Delay / reduce scope / fund remediation / request risk acceptance]` |
| Who can approve scope, funding, schedule, or residual-risk decisions? | `[Named role(s)]` |
| What is the business consequence if the project does not proceed? | `[Consequence]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Engineering Pillar Leader | Confirms routing and architecture review decision. | `[Name / Date]` |
| Risk Pillar Leader | Confirms risk treatment path where needed. | `[Name / Date]` |
| Governance Pillar Leader | Confirms regulated-scope and evidence requirements. | `[Name / Date]` |

Reviewer signatures on this form confirm intake routing and required follow-on records only. Production readiness, go-live authorization, and risk acceptance are documented through the Phase 4 and Phase 5 records governed by [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md).

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AR-001 |
| **Version** | 1.2 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - Architecture Review and Project Intake Procedure |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 SA, RA, AC, SC |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.2 | 2026-06-18 | Engineering Pillar Leader | Added business-facing decision box for project outcome, requested CERG decision, blocking-finding options, and sponsor authority. |
| 1.1 | 2026-06-18 | Engineering Pillar Leader | Clarified that TMPL-AR-001 is the front-door intake artifact and added follow-on record routing fields. |
| 1.0 | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for architecture and project intake form. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Governing procedure |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Threat modeling trigger path |
| Audit and Evidence Management Procedure | [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence library storage and evidence request handling |
