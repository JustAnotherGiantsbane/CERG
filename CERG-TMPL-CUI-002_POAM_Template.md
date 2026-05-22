
# SURGE: Cyber Engineering, Risk & Governance

## PLAN OF ACTION AND MILESTONES TEMPLATE
### POA&M Register · Milestones · Ownership · Validation · Closure Evidence

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-CUI-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Parent Plan** | [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) - CUI / CMMC Operational Package |
| **Supporting Documents** | [`CERG-TMPL-CUI-001`](CERG-TMPL-CUI-001_System_Security_Plan_Template.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| **Review Cycle** | Monthly while open / Annual template review |
| **Frameworks** | NIST 800-171r3 · NIST 800-172 · CMMC L2 · NIST 800-53r5 CA |
| **Regulations** | Controlled Unclassified Information / CMMC contractual obligations |
| **Environments** | Systems and programs with open security gaps, assessment findings, or planned control implementations |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [POA&M Discipline](#2-poam-discipline)
3. [POA&M Register Template](#3-poam-register-template)
4. [Milestone Detail Template](#4-milestone-detail-template)
5. [Evidence and Validation](#5-evidence-and-validation)
6. [Closure Criteria](#6-closure-criteria)
7. [Review Cadence](#7-review-cadence)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Use

This template creates a Plan of Action and Milestones (POA&M) for security gaps, CMMC / CUI findings, assessment observations, audit findings, and planned control implementations. It is designed to be copied into a system-specific or program-specific POA&M register.

A POA&M item is not a wish list entry. It is a dated management commitment with an owner, milestones, evidence expectations, and closure validation.

> **No Owner, No Date, No POA&M**
>
> A row without an accountable owner and target date is not a plan. It is a note. The POA&M exists so leadership can see what remains open, who owns it, when it will be fixed, what risk exists while it remains open, and what evidence proves closure.

---

## 2. POA&M Discipline

Use this template when one of the following conditions exists:

- a control is partially implemented or planned;
- an SSP control statement identifies a gap;
- an audit or assessment produces a finding;
- a risk treatment plan requires implementation work;
- a vulnerability or configuration issue requires coordinated remediation;
- a vendor, system, or business owner commits to corrective action.

Each POA&M item must link to at least one source: control ID, risk ID, finding ID, assessment ID, vulnerability ID, or SSP section.

---

## 3. POA&M Register Template

| **Field** | **Required** | **Instructions** |
|---|---|---|
| POA&M ID | Yes | Use `POAM-YYYY-NNN`. |
| Source | Yes | SSP, audit, assessment, risk, vulnerability, incident, vendor, or self-identified. |
| Source ID | Yes | Finding ID, control ID, risk ID, CVE, ticket, or assessment reference. |
| Affected System / Asset | Yes | Asset ID or system name. |
| Control ID | Yes | NIST, CMMC, CERG, or framework control. |
| Gap Statement | Yes | Plain-language description of what is missing. |
| Risk Summary | Yes | Business and security consequence while open. |
| Owner | Yes | Canonical CERG role or named business owner. |
| Supporting Roles | No | Roles needed to complete the work. |
| Treatment Approach | Yes | Mitigate, transfer, avoid, accept, or document not applicable. |
| Milestones | Yes | Milestone IDs or summary. |
| Target Completion Date | Yes | Date. |
| Current Status | Yes | Not Started, In Progress, Blocked, Validation, Closed, Cancelled. |
| Residual Risk ID | Conditional | Required for High/Critical risk or missed target dates. |
| Exception ID | Conditional | Required when a control gap is accepted temporarily. |
| Closure Evidence | Yes at closure | Evidence location. |
| Closure Validator | Yes at closure | Role validating closure. |
| Closure Date | Yes at closure | Date closed. |

### 3.1 POA&M Register Rows

| **POA&M ID** | **Source** | **Source ID** | **System / Asset** | **Control ID** | **Gap Statement** | **Owner** | **Target Date** | **Status** | **Risk / Exception Link** |
|---|---|---|---|---|---|---|---|---|---|
| `[POAM-YYYY-NNN]` | `[Source]` | `[ID]` | `[System]` | `[Control]` | `[Gap]` | `[Owner]` | `[Date]` | `[Status]` | `[Risk ID / Exception ID / None]` |

---

## 4. Milestone Detail Template

Every POA&M item has at least one milestone. Complex items should use multiple milestones so progress can be verified before the final due date.

| **Milestone ID** | **POA&M ID** | **Description** | **Owner** | **Due Date** | **Status** | **Evidence Expected** |
|---|---|---|---|---|---|---|
| `[M-001]` | `[POAM-YYYY-NNN]` | `[Milestone]` | `[Owner]` | `[Date]` | `[Status]` | `[Evidence]` |

Milestones must describe completion outcomes, not activity. "Deploy MFA to admin group" is valid. "Work on MFA" is not.

---

## 5. Evidence and Validation

Closure evidence must prove the gap is fixed or the risk treatment is complete.

| **Evidence Type** | **Examples** |
|---|---|
| Configuration evidence | Screenshot, export, policy file, baseline record. |
| Control test evidence | Test worksheet, command output, sampled records. |
| Process evidence | Approved procedure, ticket history, review minutes. |
| Technical validation | Scan result, restore test, access review result, pipeline check. |
| Approval evidence | Risk acceptance, exception approval, CISO decision. |

Evidence is stored according to `CERG-PRC-AUD-001` and linked from the POA&M row.

---

## 6. Closure Criteria

A POA&M item can close only when all closure criteria are met:

1. required milestones are complete;
2. control implementation or risk treatment is validated;
3. evidence is stored and linked;
4. related SSP, risk register, or control documentation is updated;
5. closure validator signs off;
6. residual risk is accepted or below the treatment threshold.

If a due date is missed, the item is not silently re-dated. The owner records the reason, updates the target date, and determines whether the delay creates or changes residual risk.

---

## 7. Review Cadence

Open POA&M items are reviewed monthly. High or Critical items are reviewed at the cadence set by the CISO or Risk Pillar Leader. Closed items are sampled during audits and assessments to confirm closure evidence remains available.

POA&M review outputs:

- overdue item list;
- blocked item list;
- High/Critical residual-risk list;
- items requiring CISO escalation;
- items ready for validation;
- closed items with evidence exceptions.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-CUI-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Approved By** | CISO (pending) |
| **Parent Plan** | [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) - CUI / CMMC Operational Package |
| **Review Cycle** | Monthly while open; annual template review |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-171r3; NIST 800-172; CMMC L2; NIST 800-53r5 CA |
| **Regulations** | Controlled Unclassified Information / CMMC contractual obligations |
| **Environments** | Systems and programs with open security gaps, assessment findings, or planned control implementations |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a fill-in POA&M register, milestone detail template, evidence expectations, closure criteria, and review cadence. |

### Review Triggers

- CMMC or CUI assessment cycle
- Material POA&M process change
- Repeated missed target dates
- Audit finding related to remediation tracking
- Direction from the CISO
