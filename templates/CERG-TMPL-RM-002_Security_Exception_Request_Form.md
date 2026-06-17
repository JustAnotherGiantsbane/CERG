
# SURGE: Cyber Engineering, Risk & Governance

## SECURITY EXCEPTION REQUEST FORM
### Control Exception · Waiver Request · Compensating Controls · Expiration · Approval

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Supporting Documents** | [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [`CERG-GOV-RAC-001`](../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| **Review Cycle** | Annual / On process or control change |
| **Frameworks** | NIST 800-30r1 · NIST 800-53r5 RA, CA, PM · ISO 31000 |
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

This form captures a temporary security exception or waiver request. It is used when a required control cannot be implemented as written, cannot be implemented by the due date, or must be bypassed temporarily for a justified business reason. The completed form feeds the risk register and cannot be used to create a permanent undocumented control gap.

> **Exceptions Expire**
>
> An exception is a temporary, visible, approved deviation. If it does not have an owner, compensating controls, an expiration date, and approval authority, it is not an exception. It is uncontrolled drift.

---

## 2. Template Instructions

1. Copy this template before use.
2. Replace every bracketed field with case-specific information.
3. Do not delete fields that appear not applicable. Mark them `Not Applicable` and explain why.
4. Use canonical CERG role names from `CERG-GOV-OM-001`.
5. Link risks, findings, exceptions, evidence, and approvals to the system of record.
6. Store the completed artifact in the evidence library governed by `CERG-PRC-AUD-001`.

---

## 3. Fill-In Template

### 3.1 Request Summary

| **Field** | **Value** |
|---|---|
| Exception ID | `[EX-YYYY-NNN]` |
| Request Date | `[Date]` |
| Requester | `[Name / Role]` |
| Affected System / Asset | `[Asset ID or system]` |
| Business Owner | `[Executive Sponsor or owner]` |
| Control / Requirement | `[Control ID and title]` |
| Exception Type | `[Temporary waiver / delayed implementation / compensating control / emergency exception]` |
| Requested Expiration Date | `[Date]` |
| Related Risk ID | `[Risk ID]` |

### 3.2 Exception Rationale

`[Explain why the control cannot be met as written and why the exception is needed now.]`

### 3.3 Risk and Impact

| **Area** | **Assessment** |
|---|---|
| Threat or weakness created | `[Description]` |
| Affected data or process | `[Scope]` |
| Regulatory scope | `[CUI / SOX / CIP / privacy / none]` |
| Inherent risk | `[Likelihood, impact, score]` |
| Residual risk with compensating controls | `[Likelihood, impact, score]` |
| Business consequence if denied | `[Consequence]` |

### 3.4 Compensating Controls

| **Control** | **Owner** | **Evidence** | **Monitoring Cadence** |
|---|---|---|---|
| `[Control]` | `[Owner]` | `[Evidence]` | `[Cadence]` |

### 3.5 Expiration and Exit Plan

| **Field** | **Value** |
|---|---|
| Expiration Date | `[Date]` |
| Remediation Plan | `[Plan]` |
| POA&M ID | `[POA&M ID if applicable]` |
| Renewal Allowed | `[Yes / No. If yes, state criteria.]` |
| Exit Evidence | `[Evidence needed to close]` |

---

## 4. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| Risk Register Owner | Confirms record completeness and register linkage. | `[Name / Date]` |
| Risk Pillar Leader | Approves Low or Medium exceptions where authorized. | `[Name / Date]` |
| Chief Information Security Officer (CISO) | Approves High or Critical exceptions and material regulated-scope deviations. | `[Name / Date]` |

Completed templates are reviewed at the cadence defined by their parent procedure or plan. Material changes require a new review.

---

## 5. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-RM-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Approved By** | CISO |
| **Parent Document** | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process |
| **Review Cycle** | Annual; and on process or control change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-30r1 · NIST 800-53r5 RA, CA, PM · ISO 31000 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope CERG environments where this template is used |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a standalone fill-in template for security exception request form. |

### Review Triggers

- Parent procedure or plan change
- Audit, assessment, or tabletop finding related to this template
- Role or approval model change
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Risk Register Templates and Reporting | [`CERG-TMPL-RM-001`](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Register and reporting schema |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Governing exception lifecycle |
