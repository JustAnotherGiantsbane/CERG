
# SURGE: Cyber Engineering, Risk & Governance

## SYSTEM SECURITY PLAN TEMPLATE
### System Boundary · Authorization Context · Control Implementation · Inheritance · Evidence Index

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-CUI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Parent Plan** | [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) - CUI / CMMC Operational Package |
| **Supporting Documents** | [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-TMPL-CUI-002`](CERG-TMPL-CUI-002_POAM_Template.md) |
| **Review Cycle** | Annual / On system boundary, CUI scope, or authorization change |
| **Frameworks** | NIST 800-171r3 · NIST 800-172 · CMMC L2 · NIST 800-53r5 |
| **Regulations** | Controlled Unclassified Information / CMMC contractual obligations |
| **Environments** | Systems that store, process, transmit, or protect CUI |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [SSP Cover Page](#3-ssp-cover-page)
4. [System Boundary](#4-system-boundary)
5. [System Environment](#5-system-environment)
6. [CUI Data Flow](#6-cui-data-flow)
7. [Roles and Responsibilities](#7-roles-and-responsibilities)
8. [Control Implementation Matrix](#8-control-implementation-matrix)
9. [Inherited Controls](#9-inherited-controls)
10. [External Providers and Interconnections](#10-external-providers-and-interconnections)
11. [Open Items and POA&M Linkage](#11-open-items-and-poam-linkage)
12. [Evidence Index](#12-evidence-index)
13. [Approval and Maintenance](#13-approval-and-maintenance)
14. [Document Control](#14-document-control)

---

## 1. Purpose and Use

This template creates a System Security Plan (SSP) for a system that stores, processes, transmits, or protects Controlled Unclassified Information (CUI). It is designed to be copied into a system-specific artifact and completed by the system owner, technical owners, and CMMC / Federal Compliance Manager.

The SSP explains the system boundary, CUI data flow, implemented security controls, inherited controls, external dependencies, open gaps, and evidence locations. It supports CMMC readiness, federal customer assurance, and internal authorization decisions.

> **An SSP Is a Control Story, Not a Form Dump**
>
> A useful SSP tells a reviewer what the system is, where CUI moves, which controls protect it, which controls are inherited, where the evidence lives, and what remains unfinished. If a control answer cannot be tied to evidence or a POA&M item, the SSP is not ready.

---

## 2. Template Instructions

1. Copy this template and rename the copy for the specific system.
2. Replace bracketed fields such as `[System Name]` with system-specific content.
3. Do not delete sections that are not applicable. Mark them `Not Applicable` and explain why.
4. Use asset IDs from `CERG-STD-AM-001` wherever possible.
5. Link all open control gaps to `CERG-TMPL-CUI-002` POA&M entries.
6. Link material residual risks to `CERG-PRC-RM-001` risk-register entries.
7. Store evidence in the evidence library governed by `CERG-PRC-AUD-001`.
8. Review the completed SSP annually and when the system boundary changes.

---

## 3. SSP Cover Page

| **Field** | **Value** |
|---|---|
| System Name | `[System Name]` |
| System Acronym | `[Acronym]` |
| System Owner | `[Executive Sponsor or Business Owner]` |
| Technical Owner | `[Engineering Pillar Leader or delegated technical owner]` |
| CUI Scope | `[In Scope / Out of Scope / Partial]` |
| Authorization Status | `[Draft / Under Review / Authorized / Not Authorized]` |
| Environment | `[Production / Non-production / Hybrid]` |
| Hosting Model | `[On-premises / Cloud / SaaS / Hybrid]` |
| Highest Data Classification | `[Public / Internal / Confidential / Restricted / CUI]` |
| External Providers | `[Provider names or None]` |
| SSP Version | `[Version]` |
| SSP Date | `[Date]` |

---

## 4. System Boundary

### 4.1 Boundary Narrative

Describe the system boundary in plain language.

`[Insert system boundary narrative. Include major components, users, locations, cloud accounts, network zones, and excluded components.]`

### 4.2 Boundary Components

| **Component / Asset ID** | **Type** | **Owner** | **Location** | **CUI Role** | **Notes** |
|---|---|---|---|---|---|
| `[Asset ID]` | `[Application / Server / Database / SaaS / Network / Endpoint]` | `[Owner]` | `[Location]` | `[Stores / Processes / Transmits / Protects]` | `[Notes]` |

### 4.3 Boundary Exclusions

| **Excluded Component** | **Reason Excluded** | **Evidence / Rationale** |
|---|---|---|
| `[Component]` | `[Reason]` | `[Evidence location]` |

---

## 5. System Environment

| **Area** | **Description** |
|---|---|
| Users | `[User populations and access paths]` |
| Administrators | `[Privileged user groups]` |
| Identity Provider | `[IdP, MFA, federation, PAM]` |
| Network Zones | `[Network segments and trust boundaries]` |
| Endpoints | `[Managed endpoints, VDI, mobile, BYOD constraints]` |
| Logging | `[Log sources and retention]` |
| Backup and Recovery | `[Backup tier, RTO, RPO, restore evidence]` |
| Encryption | `[Data-at-rest and data-in-transit controls]` |
| Exposure Management | `[Scanner, cadence, SLA]` |
| Configuration Baseline | `[Baseline source and exception handling]` |

---

## 6. CUI Data Flow

### 6.1 Data Categories

| **CUI Category** | **Source** | **Storage Location** | **Transmission Path** | **Recipient** | **Protection Notes** |
|---|---|---|---|---|---|
| `[Category]` | `[Source]` | `[System / database / repository]` | `[Path]` | `[Recipient]` | `[Controls]` |

### 6.2 Data Flow Narrative

`[Describe how CUI enters, moves through, exits, and is retained or deleted from the system.]`

### 6.3 Data Flow Diagram Reference

| **Diagram Name** | **Location** | **Last Updated** |
|---|---|---|
| `[Diagram]` | `[Repository / evidence location]` | `[Date]` |

---

## 7. Roles and Responsibilities

Use canonical CERG roles from `CERG-GOV-OM-001`.

| **Role** | **SSP Responsibility** | **Named Person / Team** |
|---|---|---|
| CMMC / Federal Compliance Manager | Owns SSP governance, review cycle, and CMMC mapping. | `[Name]` |
| Engineering Pillar Leader | Owns technical implementation accuracy. | `[Name]` |
| Governance Pillar Leader | Owns evidence and policy alignment. | `[Name]` |
| Risk Pillar Leader | Owns residual-risk linkage. | `[Name]` |
| Evidence Librarian | Maintains SSP evidence index. | `[Name]` |
| Risk Register Owner | Tracks risk and exception entries. | `[Name]` |

---

## 8. Control Implementation Matrix

Create one row per applicable requirement or control.

| **Control ID** | **Control Title** | **Status** | **Implementation Statement** | **Owner** | **Evidence** | **POA&M / Risk Link** |
|---|---|---|---|---|---|---|
| `[800-171 / CMMC / CERG ID]` | `[Title]` | `[Implemented / Partially Implemented / Planned / Inherited / Not Applicable]` | `[How the system satisfies the control]` | `[Canonical role]` | `[Evidence location]` | `[POA&M ID / Risk ID / None]` |

Implementation statements must be specific enough that an assessor can understand what exists without interviewing the whole team.

---

## 9. Inherited Controls

| **Inherited Control** | **Inherited From** | **Inheritance Condition** | **Evidence Owner** | **Evidence Location** |
|---|---|---|---|---|
| `[Control ID]` | `[Enterprise / Cloud Provider / SaaS / Shared Platform]` | `[Condition for inheritance]` | `[Owner]` | `[Location]` |

Inherited controls are valid only when the system still satisfies the conditions required to inherit them.

---

## 10. External Providers and Interconnections

| **Provider / Connection** | **Purpose** | **Data Shared** | **Security Requirements** | **Evidence** |
|---|---|---|---|---|
| `[Provider or connection]` | `[Purpose]` | `[Data]` | `[Requirements]` | `[Evidence]` |

Vendor and interconnection risks are linked to `CERG-PRC-TPRM-001` and `CERG-PRC-RM-001`.

---

## 11. Open Items and POA&M Linkage

| **POA&M ID** | **Related Control** | **Gap Summary** | **Owner** | **Target Date** | **Current Status** |
|---|---|---|---|---|---|
| `[POA&M ID]` | `[Control ID]` | `[Gap]` | `[Owner]` | `[Date]` | `[Status]` |

No known control gap may remain only in narrative text. Every gap must have a POA&M item, risk-register entry, or documented not-applicable rationale.

---

## 12. Evidence Index

| **Evidence ID** | **Evidence Name** | **Control(s)** | **Location** | **Owner** | **Refresh Cadence** |
|---|---|---|---|---|---|
| `[EV-001]` | `[Evidence name]` | `[Control IDs]` | `[Location]` | `[Owner]` | `[Cadence]` |

---

## 13. Approval and Maintenance

| **Approval Role** | **Approval Meaning** | **Name / Date** |
|---|---|---|
| CMMC / Federal Compliance Manager | SSP is complete enough for CMMC / CUI governance. | `[Name / Date]` |
| Engineering Pillar Leader | Technical statements are accurate. | `[Name / Date]` |
| Risk Pillar Leader | Open risks and POA&M items are correctly recorded. | `[Name / Date]` |
| Chief Information Security Officer (CISO) | Authorization or acceptance decision is recorded. | `[Name / Date]` |

---

## 14. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-CUI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Approved By** | CISO |
| **Parent Plan** | [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) - CUI / CMMC Operational Package |
| **Review Cycle** | Annual; and on system boundary, CUI scope, or authorization change |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-171r3; NIST 800-172; CMMC L2; NIST 800-53r5 |
| **Regulations** | Controlled Unclassified Information / CMMC contractual obligations |
| **Environments** | Systems that store, process, transmit, or protect CUI |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Governance | Initial release. Establishes a fill-in System Security Plan template for system boundary, CUI data flow, control implementation, inherited controls, external providers, POA&M linkage, evidence index, and approval workflow. |

### Review Triggers

- System boundary change
- CUI data-flow change
- Authorization or assessment event
- Material control implementation change
- POA&M or residual-risk change requiring SSP update
- Direction from the CISO
