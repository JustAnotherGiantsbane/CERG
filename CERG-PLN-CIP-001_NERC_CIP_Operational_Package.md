
# SURGE — Cyber Engineering, Risk & Governance

## NERC-CIP OPERATIONAL PACKAGE
### Evidence Library · OT VM · BES Access · Deviations · IT/OT Convergence · BES Categorization · ESP/EAP · CIP-013 · CIP-009 · CIP-015 (Forward-Looking)

---

| | |
|---|---|
| **Document ID** | CERG-PLN-CIP-001 |
| **Version** | 1.0 |
| **Status** | For Review |
| **Classification** | Internal — Confidential |
| **Owner** | Cyber Governance Manager (OT / NERC-CIP) |
| **Parent Standard** | CERG-STD-OT-001 — Grid Control Systems Security Standard |
| **Supporting Documents** | CERG-POL-001 · CERG-GOV-CB-001 · CERG-STD-AC-001 · CERG-STD-CFG-001 · CERG-STD-LM-001 · CERG-STD-RES-001 · CERG-STD-CR-001 · CERG-PRC-AR-001 · CERG-PRC-VM-001 · CERG-PRC-RM-001 · CERG-PRC-TPRM-001 · CERG-PRC-AV-001 · CERG-PLN-IR-001 |
| **Review Cycle** | Annual / Continuous tracking — evidence currency monthly |
| **Frameworks** | NIST 800-82r3 · IEC 62443-3-3 / 4-2 |
| **Regulations** | NERC-CIP v7 (CIP-002 through CIP-014) · CIP-015 (draft, forward-looking) · CIP-013-2 |
| **Environments** | BES Cyber Systems (Low / Medium / High Impact) + associated EACMS / PACS / PCAs |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Three-Lines-of-Defense Model](#2-three-lines-of-defense-model)
3. [CIP Version Strategy](#3-cip-version-strategy)
4. [BES Cyber System Categorization Procedure](#4-bes-cyber-system-categorization-procedure)
5. [ESP / EAP Topology Documentation](#5-esp--eap-topology-documentation)
6. [NERC-CIP Evidence Library Procedure (`CERG-GOV-CIP-001`)](#6-nerc-cip-evidence-library-procedure-cerg-gov-cip-001)
7. [OT Vulnerability Management Procedure (`CERG-PROC-VM-002`)](#7-ot-vulnerability-management-procedure-cerg-proc-vm-002)
8. [BES Cyber System Access Management Procedure (`CERG-PROC-AC-002-BES`)](#8-bes-cyber-system-access-management-procedure-cerg-proc-ac-002-bes)
9. [CIP Deviation and Mitigation Plan Template (`CERG-TMPL-CIP-001`)](#9-cip-deviation-and-mitigation-plan-template-cerg-tmpl-cip-001)
10. [IT/OT Convergence Security Architecture Guideline (`CERG-GL-OT-001`)](#10-itot-convergence-security-architecture-guideline-cerg-gl-ot-001)
11. [CIP-013 Supply Chain Risk Management Plan](#11-cip-013-supply-chain-risk-management-plan)
12. [CIP-009 Recovery Plan Package](#12-cip-009-recovery-plan-package)
13. [CIP-015 INSM — Forward-Looking Integration](#13-cip-015-insm--forward-looking-integration)
14. [Operating Cadence and Reporting](#14-operating-cadence-and-reporting)
15. [Regulatory and Framework Alignment Summary](#15-regulatory-and-framework-alignment-summary)
16. [Document Control](#16-document-control)

---

## 1. Purpose and Scope

The OT Standard names several subordinate artifacts and obliges CERG to maintain a full NERC-CIP evidence library separately. Until this package, those named subordinates did not exist. This package assembles them: an evidence library procedure, an OT VM procedure, a BES access management procedure, a CIP deviation template, an IT/OT convergence guideline, BES categorization and ESP/EAP topology procedures, the CIP-013 supply chain plan, the CIP-009 recovery plan package, and a forward-looking treatment of CIP-015 INSM.

It applies to every BES Cyber System (Low / Medium / High Impact) and the associated Electronic Access Control / Monitoring Systems (EACMS), Physical Access Control Systems (PACS), and Protected Cyber Assets (PCAs).

> **Operate the Compliance, Don't Just Document It**
>
> A binder of CIP requirements is not compliance. Compliance is the continuous evidence that the controls are operating — RTO measured, configurations baselined, access reviewed, deviations tracked, lessons learned actioned. This package is the operating manual for producing that evidence on a schedule the regulator can audit.

---

## 2. Three-Lines-of-Defense Model

CERG operates as the **second line of defense** for CIP controls.

| **Line** | **Role** | **Who** |
|---|---|---|
| **First** | Implementation of controls in the field. | OT Operators (substation engineering, control center operations, OT IT support). |
| **Second** | Review, track implementation, evidence, and deviation; coordinate with Operators on control design and remediation. | CERG (Governance — OT, Risk — OT, Engineering — OT). |
| **Third** | Dispassionate assurance independent of both. | Internal Audit and/or external firms. |

The model is intentionally explicit so audit trails are clean: Operators do; CERG reviews and tracks; Audit independently assures. CERG never grades its own homework on first-line activities, and Operators are not asked to be their own auditors.

---

## 3. CIP Version Strategy

CERG operates against the **latest approved** version of each CIP Standard, with a documented adoption window for newly approved versions and a draft-tracking posture for proposed standards. Specifically:

- Active version baseline reviewed at every CIP filing-effective-date change.
- Migration period for newly approved CIP versions tracked as risk register entries until cutover is complete.
- Draft / proposed standards (presently including CIP-015 INSM) tracked per Section 13.

---

## 4. BES Cyber System Categorization Procedure

CIP-002 requires identification and categorization of BES Cyber Systems. CERG categorizes following Attachment 1 criteria; the procedure:

1. **Inventory all BES Cyber Assets** in the enterprise inventory with required metadata (function, location, criticality input from Operations).
2. **Apply Attachment 1 criteria** (Section 1 — High Impact criteria; Section 2 — Medium Impact; everything else Low).
3. **Group BCAs into BES Cyber Systems** along functional / physical lines per operator input.
4. **Identify associated systems**: EACMS, PACS, PCAs, BCSI repositories.
5. **Document the rationale** for each categorization — the assessor will want to see it.
6. **Review annually** and on material grid configuration / asset changes.

The categorization is reflected in the asset inventory and drives every subsequent CIP obligation.

---

## 5. ESP / EAP Topology Documentation

CIP-005 requires Electronic Security Perimeters (ESPs) and Electronic Access Points (EAPs). CERG maintains:

- A network diagram set showing every Medium and High Impact ESP, the EAPs defining it, and the connections crossing each EAP.
- Per-EAP documentation: device, firmware version, rule set, last reviewed, owner, evidence of inbound/outbound deny-by-default, and authentication for interactive remote access.
- Per-ESP documentation: enclosed BCS, EACMS, PACS, PCAs; supported categorization (Medium/High); evidence of monitoring (CIP-007 R4, and forthcoming CIP-015 INSM).
- Annual review (or sooner on architecture change) with evidence routed into the library (Section 6).

---

## 6. NERC-CIP Evidence Library Procedure (`CERG-GOV-CIP-001`)

The Evidence Library is the single, authoritative repository of CIP compliance evidence — what the auditor opens first.

### 6.1 Library Structure

The library is organized by CIP Standard, then by Requirement, then by Sub-requirement. Each leaf has:

| **Field** | **Description** |
|---|---|
| Standard / Requirement / Sub-Req | E.g., CIP-007-6 R2.2 |
| Applicability | Low / Medium / High |
| Owner | CERG role + Operator role |
| Evidence Artifact(s) | Specific document / report / configuration / log |
| Evidence System of Record | Where the live artifact lives |
| Refresh Cadence | Monthly / Quarterly / Annual / 15-month / 36-month |
| Last Refresh | Date |
| Next Refresh | Date |
| Status | Current · Approaching Expiry · Expired |
| Deviation in Place? | Per Section 9 |
| Notes | — |

### 6.2 Evidence Discipline

- Every CIP Requirement applicable to in-scope assets has at least one Evidence Artifact named in the library.
- Evidence is gathered through normal operations (CERG-managed scans, configuration capture, access reviews) — not assembled at audit time.
- Refresh cadences are driven from this library to the operating cadence (Section 14).

### 6.3 Reused Evidence

CIP evidence reuses the broader CERG evidence catalog wherever possible (per `CERG-GOV-CB-001` Section 8). The library cites where it lives rather than duplicating the artifact.

---

## 7. OT Vulnerability Management Procedure (`CERG-PROC-VM-002`)

The enterprise vulnerability procedure (`CERG-PRC-VM-001`) governs IT scopes; this OT-specific procedure overlays it with OT-safe practices.

### 7.1 Identification

- **Passive scanning** is the default for live OT surfaces.
- **Authenticated checks** under engineering supervision in defined windows.
- **Vendor advisories** subscribed; advisories triaged against in-service firmware / software inventories.
- **NVD / CISA ICS Advisories** subscribed.
- Active scanning is permitted only under an approved scope and time window per `CERG-PRC-AV-001` Section 9.

### 7.2 Risk Assessment and Treatment

- Vulnerabilities mapped against CIP-007 R2 patch evaluation cycle (35 calendar days from release for Medium/High Impact to evaluate; per the standard's specifics).
- Treatment options: apply patch in next maintenance window · implement compensating control · accept via Risk Register and CIP deviation if a deviation is required (Section 9).

### 7.3 Patching

- Patch evaluation cadence per CIP-007 R2.
- Patch deployment per CIP-010 R1 — configuration changes require baseline update, security impact analysis, and authorization.
- Patch evidence retained in the Evidence Library per CIP-007 R2.4.

### 7.4 Documentation

- Per the procedure in `CERG-PRC-VM-001` Section 6 with OT-specific fields: applicability to BES, CIP-007 R2 timing, CIP-010 R1 change record.

---

## 8. BES Cyber System Access Management Procedure (`CERG-PROC-AC-002-BES`)

CIP-004 R4 / R5 obligations operationalized as an overlay on `CERG-PRC-AC-002`.

### 8.1 Authorization

- Access to BES Cyber Systems is authorized only after the individual has met CIP-004 personnel risk assessment requirements (background check, training).
- Authorization is documented with a named approver per role.
- Reviews per CIP-004 cadence (every 15 months, plus on role change).

### 8.2 Provisioning and Revocation

- Provisioning of unescorted physical access to ESPs and electronic access to BCS goes through PAM-mediated workflows where supported.
- Revocation within 24 hours of termination (CIP-004 R5.1) — CERG operates against 1 hour for involuntary terminations.
- BCSI access is governed under CIP-011 (information protection).

### 8.3 Vendor Remote Access

- Brokered through approved gateways with session recording.
- Authenticated per CIP-005 R2; monitored per CIP-005 R2.5 (interactive remote access via intermediate system).
- Vendor identities enrolled via `CERG-PRC-AC-002` Section 10 and `CERG-PRC-TPRM-001`.

---

## 9. CIP Deviation and Mitigation Plan Template (`CERG-TMPL-CIP-001`)

When a CIP requirement cannot be met as written (or cannot be met for a defined window), CERG documents a deviation and mitigation plan. This is in addition to the risk register entry in `CERG-PRC-RM-001`.

```
CIP DEVIATION AND MITIGATION PLAN — DEV-CIP-YYYY-NNNN

A. DEVIATION IDENTIFICATION
   Standard / Requirement   :  (e.g., CIP-007-6 R2.2)
   Applicability            :  Low / Medium / High
   Affected BCS / EACMS / PACS / PCAs
   Discovered By            :
   Discovery Date           :
   Description              :  Specific, requirement-citing language

B. CAUSE
   Why the requirement is not met as written

C. RISK
   Risk Register ID (per CERG-PRC-RM-001)
   Residual Risk Score
   Operator Sign-Off

D. MITIGATION
   Compensating control(s) — specific, in-place, named, evidenced
   Detection coverage uplift (if applicable)

E. PLAN TO ELIMINATE THE DEVIATION
   Steps                    :
   Owner                    :
   Target Closure           :

F. APPROVAL
   CERG Governance — OT     :
   CERG CISO                :
   Operations               :

G. RECORD
   Library Reference        :  (where deviation lives in Section 6 library)
   Self-Report Required?    :  Y/N
   Self-Report Submitted    :  Date if applicable
```

> **Deviations Get Self-Reported When Self-Reporting Is the Right Call**
>
> CERG works with Operations and Legal to determine when a deviation is a self-reportable noncompliance under the regional entity's self-reporting program. The deviation record above always exists; whether to self-report is a deliberate Legal / Compliance / CISO decision, not a default.

---

## 10. IT/OT Convergence Security Architecture Guideline (`CERG-GL-OT-001`)

The convergence guideline informs architecture decisions where IT systems touch OT systems. It is referenced by `CERG-PRC-AR-001` for any project crossing the IT/OT boundary.

### 10.1 Foundational Patterns

- **No flat IT/OT networks.** Convergence happens at named, documented EAPs.
- **One-way logging out of OT, brokered control into OT.** Data flows out of OT to SIEM are one-way; control / management flows into OT traverse identity, authorization, and recording controls.
- **Identity-first segmentation.** IT identity does not auto-translate to OT identity; OT identities are separate and governed by Section 8.
- **DMZ / industrial DMZ.** Where IT systems consume OT data, an industrial DMZ holds data brokers, historians, and integration services.
- **Engineering-tool isolation.** Engineering tools live on managed engineering workstations only; not on general-purpose corporate endpoints.

### 10.2 Pattern Reviews

The guideline catalogs approved IT/OT integration patterns:

- Historian-as-publisher (read-only, broker-mediated).
- Operator workstation reading OT data via DMZ.
- Vendor remote access via brokered jump.
- Cloud-hosted analytics consuming OT data via one-way export.
- IT identity using OT data in business analytics platforms.

Each pattern lists the controls, the diagrams required, and the architecture review depth.

### 10.3 Anti-Patterns

- Direct IT→OT VPN without brokering.
- OT-side credentials used by IT business processes.
- IT-side patching tools reaching into OT.
- Cloud agents installed directly on OT endpoints.
- File shares straddling IT and OT trust boundaries.

---

## 11. CIP-013 Supply Chain Risk Management Plan

Operationalized in coordination with `CERG-PRC-TPRM-001`. The CIP-013 Plan satisfies CIP-013-2 R1 and is reviewed annually (R3).

### 11.1 Scope

Vendor relationships involving Medium or High Impact BCS planning, design, installation, deployment, software/firmware/services, vendor remote access.

### 11.2 Components

| **R1 Risk Area** | **CERG Implementation** |
|---|---|
| Notification of vendor incidents | Contract clause + SCCT activation per `CERG-PRC-TPRM-001` Section 15 |
| Coordination of incident response | SCCT + `CERG-PLN-IR-001` interface |
| Notification of vendor personnel changes affecting access | Contract clause + CIP-004 access revocation per Section 8 |
| Disclosure of known vulnerabilities | Subscription to vendor advisories + Section 7 OT VM |
| Software / firmware integrity verification | `CERG-STD-OT-001` + `CERG-PRC-TPRM-001` Section 11 |
| Vendor remote access — coordination of session controls | Section 8 + `CERG-STD-AC-001` |

### 11.3 Evidence

CIP-013 evidence flows from this section into the Evidence Library (Section 6).

---

## 12. CIP-009 Recovery Plan Package

Operationalized in coordination with `CERG-STD-RES-001`. The CIP-009 obligations:

| **CIP-009 Requirement** | **CERG Implementation** |
|---|---|
| R1.1 Plan specifications | `CERG-STD-RES-001` Section 11 Recovery Plan template + Section 7 OT artifacts |
| R1.2 Roles and responsibilities | Documented per plan |
| R1.3 Process for backup management | `CERG-STD-RES-001` Section 4 |
| R1.4 Method for preserving recovery data | `CERG-STD-RES-001` Section 7.1 |
| R1.5 Operator-led recovery | Plan names operator with substation engineering authority |
| R2.1 Testing | `CERG-STD-RES-001` Section 5 — at least every 15 months |
| R2.2 Operational exercise | Every 36 months — full operational exercise |
| R3 Lessons learned and plan update within 90 days | `CERG-STD-RES-001` Section 5.2 step 8 |

---

## 13. CIP-015 INSM — Forward-Looking Integration

CIP-015 (Internal Network Security Monitoring) is in draft / approval at the time of V1 publication. CERG's posture:

- The detection foundation in `CERG-STD-LM-001` Sections 6.2 and 9 is designed to support CIP-015 obligations once finalized — passive OT monitoring with detection set anchored to ATT&CK for ICS.
- ESP/EAP topology documentation in Section 5 provides the basis for INSM scoping.
- Detection coverage metrics (DT-001 / DT-002) include OT sub-matrix; coverage on the BES INSM-relevant subset is tracked separately.
- When CIP-015 is approved, CERG executes an implementation plan within the standard's enforcement window: incrementally onboarding INSM coverage to High Impact ESPs first, then Medium Impact; updating the Evidence Library; updating the Convergence Guideline if architectures shift.

A risk register entry tracks the CIP-015 readiness gap until INSM coverage matches the final standard.

---

## 14. Operating Cadence and Reporting

| **Activity** | **Cadence** |
|---|---|
| Evidence library refresh sweep | Continuous; full review monthly |
| BES categorization review | Annual + on material change |
| ESP/EAP topology review | Annual + on architecture change |
| CIP-004 access reviews | Per CIP cadence (≤ 15 months); CERG operates quarterly |
| CIP-007 R2 patch evaluation | Per CIP cadence |
| CIP-009 recovery testing | Every 15 months minimum; full exercise every 36 months; CERG operates annually |
| CIP-010 baseline review | Per CIP cadence |
| CIP-013 plan review | Annual (R3) |
| Deviation register review | Monthly |
| Reg posture report | Quarterly per `CERG-GOV-MTR-001` |
| Internal CIP walkthrough | Quarterly (sampling) |
| Independent (third-line) review | Annual minimum |

---

## 15. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Package** |
|---|---|
| CIP-002 | Section 4 |
| CIP-003 | Cross-cutting (policy + program); Section 2 |
| CIP-004 | Section 8 |
| CIP-005 | Section 5 |
| CIP-006 | Interface to Facilities (out of CERG scope; coordinated) |
| CIP-007 | Sections 5–7, evidence library |
| CIP-008 | Interface to `CERG-PLN-IR-001` |
| CIP-009 | Section 12 + `CERG-STD-RES-001` |
| CIP-010 | Sections 5, 7 + `CERG-STD-CFG-001` |
| CIP-011 | Section 8 + `CERG-STD-CR-001` |
| CIP-013 | Section 11 + `CERG-PRC-TPRM-001` |
| CIP-014 | Interface to Facilities |
| CIP-015 (draft) | Section 13 + `CERG-STD-LM-001` |
| NIST 800-82r3 | Sections 7, 10 + `CERG-STD-OT-001` / `CERG-STD-CFG-001` |
| IEC 62443-3-3 / 4-2 | Sections 7, 10 |

---

## 16. Document Control

| | |
|---|---|
| **Document ID** | CERG-PLN-CIP-001 |
| **Version** | 1.0 |
| **Approved By** | Cyber Governance Manager (OT / NERC-CIP) · CISO endorsement |
| **Next Review** | Annual / on CIP version or filing change |
| **Change Log** | 1.0 — Initial publication. Evidence library, OT VM, BES access, deviation template, IT/OT convergence guideline, categorization, ESP/EAP, CIP-013, CIP-009, CIP-015 forward-looking. |

