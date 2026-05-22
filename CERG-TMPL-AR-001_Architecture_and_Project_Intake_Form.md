
# SURGE: Cyber Engineering, Risk & Governance

## ARCHITECTURE AND PROJECT INTAKE FORM
### Project Intake · Data Scope · Threat Modeling Trigger · Review Routing

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-AR-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Document** | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - Architecture Review and Project Intake Procedure |
| **Supporting Documents** | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) |
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

This form promotes the reusable intake appendix from the architecture review procedure into a standalone template. It captures enough information to route a project to the correct CERG review path, trigger threat modeling when needed, identify data and regulatory scope, and document go-live conditions.

> **The Intake Form Is the Front Door**
>
> Projects should not discover security requirements at the end. Intake is where ownership, data, architecture, vendors, identity, logging, and deployment risk become visible early enough to matter.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed placeholder with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001`.
5. Link risks, findings, exceptions, evidence, and approvals to the system of record.
6. Store the completed artifact in the evidence library governed by `CERG-PRC-AUD-001`.

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

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Engineering Pillar Leader | Confirms routing and architecture review decision. | `[Name / Date]` |
| Risk Pillar Leader | Confirms risk treatment path where needed. | `[Name / Date]` |
| Governance Pillar Leader | Confirms regulated-scope and evidence requirements. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-AR-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | CISO (pending) |
| **Parent Document** | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - Architecture Review and Project Intake Procedure |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 SA, RA, AC, SC |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for architecture and project intake form. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Governing procedure |
| Threat Modeling Procedure | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Threat modeling trigger path |
