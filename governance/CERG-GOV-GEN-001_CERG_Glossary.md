## CERG GLOSSARY
### Canonical Terms, Record Types, and Conversion Rules

---

| | |
|---|---|
| **Document ID** | CERG-GOV-GEN-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On any new record type or major terminology change |
| **Frameworks** | NIST CSF 2.0 (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How to Use This Glossary](#2-how-to-use-this-glossary)
3. [Canonical Terms](#3-canonical-terms)
4. [Record Types and Their Terms](#4-record-types-and-their-terms)
5. [Conversion Rules](#5-conversion-rules)
6. [Role Names](#6-role-names)
7. [Document Control](#7-document-control)

---

## 1. Purpose and Scope

CERG uses specific terms with specific meanings. "Finding" is not a vulnerability. "Risk" is not a finding. "Exception" is not an exception to risk acceptance. Confusing these terms produces records that do not match what auditors and adopters expect.

This document is the canonical glossary for CERG. It collects the terms that appear across the corpus and gives each one a definition, an authoritative record type, and a statement of what it converts to. Where the same word appears with different meanings in different documents (for example, "control" in POL-001 vs CB-001), this document disambiguates.

The glossary is the first place to look when a term is ambiguous. The Flow F-04 walkthrough (in [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md)) and the day-in-the-life stories use the terms defined here.

The glossary does not redefine terms that already have a published definition in another CERG artifact. Where a term's authoritative definition lives elsewhere (for example, "Risk Appetite" lives in [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md)), this document points to that source rather than restating the definition.

## 2. How to Use This Glossary

- **A leader adopting CERG for the first time** should read §3 and §4 once before reading any other CERG document. The 30 minutes invested pays back across every subsequent read.
- **A contributor** writing a new CERG artifact should check this glossary before coining a new term. If a term does not appear here and is not defined in the parent artifact, add it to §3 of this glossary before using it elsewhere.
- **An auditor or assessor** reviewing CERG adoption can use this glossary as the authoritative vocabulary against which to test that records, evidence, and reports use the same term consistently.

## 3. Canonical Terms

These terms appear throughout the CERG corpus with specific meanings.

| Term | Definition | Source |
|---|---|---|
| **Adoption path** | One of three preset operating modes (CERG Lite, CERG Standard, CERG Regulated) selected by an adopter based on team size and regulatory scope. Determines which artifacts are adopted first and which are deferred. | [CERG-GOV-IMP-005](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| **Adopter** | An organization that has decided to operate its cybersecurity program using CERG, regardless of adoption path or scope. | This document |
| **Asset** | A system, service, application, dataset, or other component that is in scope for the security program and is inventoried in the asset register. | [CERG-STD-AM-001](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) |
| **Asset Owner** | The named individual accountable for an asset's risk posture, classification, and adherence to applicable controls. | [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| **Audit** | A formal review of program adherence against an external standard (NERC-CIP, CMMC, SOX, ISO 27001) or internal control baseline. Distinct from a Finding. | [CERG-PRC-AUD-001](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| **Business Owner** | The named individual accountable for a business process that depends on one or more assets. Signs risk acceptance memos and exception requests on the business side. | [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) |
| **CERG** | The cybersecurity operating model defined in this repository. Pronounced "surge." The name "CERG" is the program name; the pronunciation appears only in the README. | [README.md](../README.md) |
| **Control** | A requirement that, when implemented, reduces a specific risk. In CERG, controls live in [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) (Unified Control Baseline) and are implemented via Standards and Procedures. | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) |
| **Control Change Record** | The authoritative record of work to convert a governance-originated control intent into implemented technical change. | [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-01 |
| **Evidence** | A timestamped, attributable artifact that demonstrates a control was operating as required. Quality tiers defined in [CERG-GOV-AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md). | [CERG-GOV-AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| **Exception** | An approved deviation from a control or requirement, with compensating controls, expiration, and named approver. Distinct from a Risk Acceptance. | [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **MVC (Minimum Viable CERG)** | The eight-document spine required for any CERG adoption: Policy, Framework, Operating Model, Document Catalog, Risk Management Framework, Risk Register Process, Risk Register Templates, Exposure Management Procedure. | [CERG-GOV-IMP-001](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §4 |
| **Pillar** | One of three accountability lines in CERG: Cyber Engineering (builds securely), Cyber Risk (knows exposure), Cyber Governance (makes rules clear). | [CERG-GOV-FRM-002](CERG-GOV-FRM-002_Framework_System_Map.md) §3.3 |
| **Risk** | A loss-event scenario with a named owner, treatment strategy, and acceptance decision. Distinct from a Finding (which is an observed condition) and from Vulnerability (which is a technical weakness). | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| **Risk Acceptance** | A documented decision by a Business Owner to operate with a known residual risk, with named approver, rationale, and review date. Distinct from an Exception (which is a deviation from a control). | [CERG-TMPL-RM-003](../templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) |
| **SLA** | Service-Level Agreement. In CERG, used in two directions: business-side SLAs (remediation clocks) and CERG-side SLAs (the commitments in [CERG-GOV-SLC-001](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md)). | [CERG-GOV-SLC-001](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |

## 4. Record Types and Their Terms

Every material workflow in CERG resolves to one of the following primary record types. Each record type is owned by one source-of-truth system. Where multiple systems hold similar data, the source-of-truth wins.

| Record Type | Definition | Owning Pillar | Source of Truth |
|---|---|---|---|
| **Project Intake Record** | The initial record of a project, application, or major change entering the security review pipeline. The first artifact in F-02. | Engineering | Project intake system (e.g., Jira, ServiceNow, spreadsheet) |
| **Architecture Review Record** | The record produced by an architecture review: scope, design decisions, conditions, disposition. | Engineering | GRC system or document management |
| **Threat Model Record** | The record of a threat modeling exercise: assets, threats, mitigations, residual risk. | Engineering (in flow) / Risk (when promoted) | GRC system |
| **Asset Record** | The authoritative inventory record for a system, service, application, or dataset. Includes owner, classification, criticality, coverage status. | Engineering | CMDB or asset management system |
| **Finding Record** | An observed condition requiring disposition. Discovered through scanning, testing, audit, or review. Distinct from a Vulnerability (raw input) or a Risk (loss scenario). | Risk | GRC system or exposure backlog |
| **Risk Record** | A loss-event scenario with a named owner, treatment strategy, and acceptance decision. May be promoted from a Finding or created directly. | Risk | GRC system or risk register |
| **Exception Record** | An approved deviation from a control or requirement, with compensating controls, expiration, and named approver. | Governance | GRC system or exception register |
| **Change Record** | The authoritative record of a security-relevant change: implementation window, SIA, rollback plan, control continuity result. | Engineering | Change management system |
| **Incident Record** | A declared security event requiring active response. Owned by the standing IR team; CERG is adjacent, not authoritative. | Adjunct (IR team) | IR incident tracking system |
| **Evidence Record** | A timestamped, attributable artifact demonstrating control operation. Indexed in the evidence library. | Governance | Evidence repository |
| **Improvement Record** | A program-level improvement item tracked in the Program Improvement Register with source attribution. | Governance | Program Improvement Register |
| **Control Change Record** | The record of converting a governance-originated control intent into implemented technical change and validated outcome. | Governance | GRC system |
| **Reporting Metric Record** | A single metric value for a defined period, with source, threshold, and action assignment. | Governance | BI dashboard or reporting tool |

### Conversion Rules

These are the rules that govern when one record type becomes another. They appear in [CERG-GOV-FLOW-001 §2](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#2-operating-principles) and are repeated here for discoverability.

- A **Vulnerability** becomes a **Finding** when triaged. It may be directly remediated without becoming a Risk.
- A **Finding** promotes to a **Risk Record** when: the SLA is exceeded, the affected asset is Tier 0 or Tier 1, exploitation is active, remediation requires a business decision, or compensating controls are needed.
- A **Risk** that involves a control deviation creates an **Exception Record**.
- An **Exception** that expires without renewal auto-creates a **Finding** (severity: High).
- A recurring **Finding** in the same control family triggers a **Control Change Record** (F-01).
- A **Control Gap** (a missing or ineffective control, a systemic condition) is usually recorded as a **Risk** because of its systemic impact.
- An **Incident** declaration does not replace a Finding. Lessons learned from an Incident may create Findings, Risks, or Control Change Records, but the Incident Record itself is the authoritative artifact for the event.

## 5. Conversion Rules (extended)

These extended rules cover record-to-record transitions that appear less frequently but still matter.

- A **Risk Acceptance** that expires without renewal auto-creates a **Finding** (severity: High). The original acceptance approver is notified.
- An **Exception** that is renewed without a change in scope does not create a new Finding; the existing Exception Record is updated with a new expiration date.
- A **Finding** that is closed as a False Positive does not create a Risk or an Exception. The determination method and evidence are recorded in the Finding Record's closure rationale.
- A **Risk** that is closed by treatment does not automatically close the underlying Finding. Each is closed independently based on its own closure criteria.
- A **Control Change Record** that is closed does not close related Findings. The Findings close when their remediation evidence is validated.

## 6. Role Names

These are the canonical role names used across CERG artifacts. Roles collapse onto fewer heads in CERG Lite per [CERG-GOV-IMP-003 §4](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#4-role-consolidation-map). The questions the role owns do not collapse.

### Executive and Pillar Leadership

- **CISO (Chief Information Security Officer)** - accountable for the security program overall
- **Executive Sponsor** - accountable executive outside the security team
- **Engineering Pillar Leader** - accountable for the Engineering pillar
- **Risk Pillar Leader** - accountable for the Risk pillar
- **Governance Pillar Leader** - accountable for the Governance pillar

### Engineering Pillar Roles

- **Cloud Security Engineer**
- **Identity Engineer**
- **OT Security Engineer**
- **Application Security Engineer**
- **Endpoint Engineer**
- **Cryptography Engineer**
- **Pre-production Reviewer**

### Risk Operations Pillar Roles

- **Exposure Management Lead**
- **Adversarial Testing Lead**
- **Threat Intelligence Analyst**
- **Detection Engineer**
- **OT Risk Analyst**
- **Identity Risk Analyst**
- **Vendor Risk Analyst**

### Governance and Compliance Pillar Roles

- **NERC-CIP Compliance Manager**
- **CMMC / Federal Compliance Manager**
- **SOX ITGC Lead**
- **Policy and Standards Manager**
- **Risk Register Owner**
- **Evidence Librarian**

### Adjunct Function Roles (Incident Response)

- **Incident Commander** - accountable during a declared incident
- **Lead Investigator** - accountable for incident investigation

## 7. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-GEN-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-18 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On any new record type or major terminology change |
| **Next Scheduled Review** | 2027-06-18 |
| **Frameworks** | NIST CSF 2.0 (GOVERN: Organizational Context) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.0 | 2026-06-18 | Governance Pillar Leader (Document Control) | Initial publication. Extracted canonical terms from FLOW-001 §2 (Operating Principles, Record Type Definitions) and CB-001 / RMF-001 / OM-001 cross-references. Added extended conversion rules and canonical role names per roles/ directory. |

### Review Triggers

- A new record type is added to [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) §4.
- A new term is introduced in any CERG artifact that does not appear in this glossary.
- A canonical role is added to or removed from the roles directory.
- A new pillar or sub-pillar is added to [CERG-GOV-FRM-001](CERG-GOV-FRM-001_CERG_Framework.md).
- A maintainer review identifies a term whose meaning has drifted from the original definition.

### Related Documents

- [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) - Source of the record type definitions and conversion rules in §4 and §5.
- [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) - Authoritative source for "Risk Appetite" and risk treatment vocabulary.
- [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) - Authoritative source for control vocabulary.
- [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) - Authoritative source for role definitions and pillar descriptions.
- [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) - Three-pillar model and CERG philosophy.
- [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) - Style conventions for CERG documents.
- [`roles/CERG-GOV-JF-001_Job_Families_Overview.md`](../roles/CERG-GOV-JF-001_Job_Families_Overview.md) - Job family structure and per-role descriptions.
