## SYSTEM CONTROL PROFILE TEMPLATE
### Per-System Control Implementation · Evidence · Validation · Review State

---

| | |
|---|---|
| **Document ID** | CERG-TMPL-SCP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Document** | [CERG-GOV-CAT-002](../governance/CERG-GOV-CAT-002_Record_Catalog.md) - Record Catalog |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-GOV-TRC-001](../governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) · [CERG-GOV-AUD-001](../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| **Review Cycle** | Annual / On system classification, control baseline, or evidence model change |
| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 · ISO/IEC 27001 |
| **Regulations** | CMMC L2 · NERC-CIP · SOX ITGC · Cross-cutting |
| **Environments** | All systems or system classes requiring per-system control evidence |

---

## Table of Contents

1. [Purpose and Use](#1-purpose-and-use)
2. [Template Instructions](#2-template-instructions)
3. [YAML Structure](#3-yaml-structure)
4. [Fill-In Template](#4-fill-in-template)
5. [Review and Approval](#5-review-and-approval)
6. [Document Control](#6-document-control)

---

## 1. Purpose and Use

A System Control Profile (SCP) is a structured per-system or per-system-class record that connects the asset inventory, control baseline, implementation statement, evidence location, validation date, and next review date.

The SCP is not a new control framework and does not replace a regulated System Security Plan, POA&M, NERC-CIP evidence package, SOX test record, asset inventory, or risk register. It is the structured control-profile record that lets those artifacts agree with each other.

Use this template when an implementation needs to prove control state for a system, regulated boundary, crown-jewel service, OT asset class, CUI enclave, SOX-relevant application, or other system class where control implementation and evidence must be assessed at system level.

---

## 2. Template Instructions

1. Store SCP records as YAML using the schema at [`../machine-readable/schemas/system-control-profile.schema.json`](../machine-readable/schemas/system-control-profile.schema.json).
2. Use one SCP per system or per clearly bounded system class.
3. Use stable asset IDs from the authoritative asset inventory.
4. Use control IDs from [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md).
5. Link each control entry to evidence that is independently verifiable under [`CERG-GOV-AUD-001`](../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md).
6. Record `last_validated` and `next_review` for every control entry.
7. Link related risks, exceptions, POA&M items, and findings instead of embedding their full content.
8. Store the completed SCP in the evidence library and index it as a **System Control Profile Record** per [`CERG-GOV-CAT-002`](../governance/CERG-GOV-CAT-002_Record_Catalog.md).

---

## 3. YAML Structure

Minimum structure:

```yaml
system_id: "[stable asset or system identifier]"
name: "[system name]"
classification: "[Public / Internal / Confidential / Restricted / CUI / BES Cyber System / SOX-relevant / other]"
system_owner: "[Business Owner or System Owner role]"
technical_owner: "[Technical Owner role]"
environment: "[IT / Cloud / SaaS / OT / Hybrid]"
regulatory_scope:
  - "[CUI / BES / SOX / Privacy / None]"
profile_status: "[Draft / Approved / Superseded / Retired]"
last_profile_review: "[YYYY-MM-DD]"
next_profile_review: "[YYYY-MM-DD]"
controls_applied:
  - control: "[control ID]"
    implementation: "[how this system implements the control]"
    evidence: "[evidence link or evidence index ID]"
    evidence_type: "[export / report / ticket / configuration / attestation / test result / SCP-linked package]"
    last_validated: "[YYYY-MM-DD]"
    next_review: "[YYYY-MM-DD]"
    owner: "[control owner for this system]"
    status: "[Implemented / Partially Implemented / Planned / Inherited / Exception / Accepted Risk]"
    related_risks: []
    related_exceptions: []
```

---

## 4. Fill-In Template

A complete example is available at [`../examples/system-control-profile.example.yaml`](../examples/system-control-profile.example.yaml).

```yaml
system_id: HIST-47
name: Substation 47 Historian
classification: BES Cyber System
system_owner: Operations Technology Owner
technical_owner: OT Security Engineer
environment: OT
regulatory_scope:
  - BES
profile_status: Approved
last_profile_review: 2026-03-31
next_profile_review: 2026-06-30
controls_applied:
  - control: AC-2
    implementation: AD group S47-Operators controls operator access; quarterly access review performed by the System Owner.
    evidence: evidence://access-reviews/hist-47/quarterly_access_review_2026-03-31.pdf
    evidence_type: access_review_record
    last_validated: 2026-03-31
    next_review: 2026-06-30
    owner: Identity Engineer
    status: Implemented
    related_risks: []
    related_exceptions: []
  - control: CM-7
    implementation: DISH baseline v2.1 applied; local firewall allowlist restricts management services to the OT jump host.
    evidence: evidence://baselines/hist-47/cm7_baseline_comparison_2026-04-15.xlsx
    evidence_type: configuration_baseline_record
    last_validated: 2026-04-15
    next_review: 2026-07-15
    owner: OT Security Engineer
    status: Implemented
    related_risks: []
    related_exceptions: []
```

---

## 5. Review and Approval

| **Reviewer / Approver** | **Review Meaning** | **Name / Date** |
|---|---|---|
| System Owner / Business Owner | Confirms system scope, business ownership, and accepted residual conditions. | `[Name / Date]` |
| Technical Owner | Confirms implementation statements and evidence links are accurate. | `[Name / Date]` |
| Engineering Pillar Leader | Confirms control implementation and coverage profile. | `[Name / Date]` |
| Governance Pillar Leader | Confirms evidence quality, regulatory traceability, and retention route. | `[Name / Date]` |
| Risk Pillar Leader | Confirms linked risk, exception, or accepted-risk entries where residual exposure remains. | `[Name / Date]` |

Completed SCP records are reviewed at the cadence defined by their system classification, regulatory scope, and related control requirements. Material system change, control baseline change, ownership change, regulatory-scope change, or major evidence failure requires an SCP refresh.

---

## 6. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-SCP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-20 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | CISO |
| **Parent Document** | [CERG-GOV-CAT-002](../governance/CERG-GOV-CAT-002_Record_Catalog.md) - Record Catalog |
| **Review Cycle** | Annual; and on system classification, control baseline, or evidence model change |
| **Next Scheduled Review** | 2027-06-20 |
| **Frameworks** | NIST 800-53r5 · NIST 800-171r3 · NIST CSF 2.0 · ISO/IEC 27001 |
| **Regulations** | CMMC L2 · NERC-CIP · SOX ITGC · Cross-cutting |
| **Environments** | All systems or system classes requiring per-system control evidence |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-20 | Engineering Pillar Leader | Initial publication. Establishes the System Control Profile as a structured per-system control implementation, evidence, validation, and review record. |

### Review Triggers

- Control baseline or traceability matrix changes.
- Asset classification, ownership, boundary, or regulatory scope changes.
- Material system architecture or control implementation change.
- Evidence failure, audit finding, or regulator request requiring per-system control proof.
- Direction from the CISO.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Record Catalog | [CERG-GOV-CAT-002](../governance/CERG-GOV-CAT-002_Record_Catalog.md) | Defines System Control Profile Record as a canonical record type |
| Unified Control Baseline | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | Source for control identifiers and control state |
| Control-to-Procedure Traceability Matrix | [CERG-GOV-TRC-001](../governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) | Maps controls to procedures and expected evidence records |
| Evidence Quality Standard | [CERG-GOV-AUD-001](../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | Evidence quality rules for SCP-linked artifacts |
