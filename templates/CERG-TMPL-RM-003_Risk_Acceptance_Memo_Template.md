
# SURGE: Cyber Engineering, Risk & Governance

## RISK ACCEPTANCE MEMO TEMPLATE
### Decision Record · Residual Risk · Business Rationale · Conditions · Expiration

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-003 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Supporting Documents** | [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [`CERG-TMPL-RM-002`](CERG-TMPL-RM-002_Security_Exception_Request_Form.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST 800-30r1 · NIST 800-39 · ISO 31000 |
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

This memo records an explicit risk acceptance decision. It is used when leadership chooses to accept residual risk rather than mitigate, transfer, or avoid it immediately. The completed memo must link to the risk register and must not replace the register entry.

> **Acceptance Is a Decision, Not an Absence of Action**
>
> Risk is not accepted because nobody fixed it. Risk is accepted only when the right authority understands the scenario, impact, residual exposure, conditions, expiration, and alternatives, then records the decision.

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

### 3.1 Decision Summary

| **Field** | **Value** |
|---|---|
| Memo ID | `[RA-YYYY-NNN]` |
| Risk ID | `[Risk ID]` |
| Risk Statement | `[Because of..., affecting..., there is a possibility that..., resulting in...]` |
| Requesting Owner | `[Owner]` |
| Affected Assets / Processes | `[Scope]` |
| Regulatory Scope | `[CUI / SOX / CIP / privacy / none]` |
| Residual Risk Rating | `[Low / Medium / High / Critical]` |
| Acceptance Period | `[Start date to expiration date]` |

### 3.2 Business Rationale

`[Explain why acceptance is appropriate compared with mitigation, transfer, or avoidance.]`

### 3.3 Conditions of Acceptance

| **Condition** | **Owner** | **Evidence / Monitoring** |
|---|---|---|
| `[Condition]` | `[Owner]` | `[Evidence]` |

### 3.4 Alternatives Considered

| **Alternative** | **Reason Not Selected** |
|---|---|
| `[Alternative]` | `[Reason]` |

### 3.5 Expiration and Review

| **Field** | **Value** |
|---|---|
| Expiration Date | `[Date]` |
| Review Cadence | `[Cadence]` |
| Renewal Criteria | `[Criteria]` |
| Trigger for Early Review | `[Trigger]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Risk Register Owner | Confirms register entry, scoring, and linkage. | `[Name / Date]` |
| Risk Pillar Leader | Approves within delegated authority. | `[Name / Date]` |
| Chief Information Security Officer (CISO) | Approves High or Critical acceptance where required. | `[Name / Date]` |
| Executive Sponsor | Provides business concurrence for Critical risk where required. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-RM-003 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-30r1 · NIST 800-39 · ISO 31000 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for risk acceptance memo template. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Governing risk acceptance lifecycle |
