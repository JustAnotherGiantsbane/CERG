## PROVIDER RACI EXTENSION — AnyTech Adaptation
### Who Delivers · Who Validates · Who Decides · Provider Accountability Mapping

---

| | |
|---|---|
| **Artifact ID** | ANYTECH-RACI-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Public |
| **Owner** | Risk Pillar Lead (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy (AnyTech) |
| **Supporting Documents** | [Operating Model](CERG-GOV-OM-001_Operating_Model_AnyTech.md) · [TPRM Procedure](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) · [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) · [Consolidated Roles and RACI](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| **Review Cycle** | Quarterly / On provider change |
| **Frameworks** | NIST CSF 2.0 (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) |
| **Environments** | All AnyTech environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [RACI Key](#2-raci-key)
3. [Provider-Specific RACI Dimensions](#3-provider-specific-raci-dimensions)
4. [Capability-to-Provider RACI Matrix](#4-capability-to-provider-raci-matrix)
5. [Validation Rights](#5-validation-rights)
6. [RACI Change Management](#6-raci-change-management)
7. [Common RACI Failures in the Vendor-Oversight Model](#7-common-raci-failures-in-the-vendor-oversight-model)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

The upstream CERG RACI instrument (`CERG-GOV-RAC-001`) defines accountability within a single organization. For AnyTech, many accountabilities are split across the internal team and external providers. This document extends the RACI to map **every material security capability** to:

- **Who delivers** the capability (performs the work)
- **Who validates** the capability (confirms it is operating)
- **Who decides** when the capability changes (approves scope, budget, exceptions)
- **Who is notified** of status, breaches, or gaps

This is essential because the default failure mode in a vendor-oversight model is **provider RACI drift** — the contract says the provider owns something, but nobody from AnyTech validates it, and the provider deprioritizes it. This document makes the validation obligation explicit.

### 1.1 The Three Provider Types

| Provider | Role | Scope |
|---|---|---|
| **MSSP** | SOC / IR operations | Detection, triage, incident response, threat intelligence |
| **MSP** | IT operations | Patching, access management, system administration, user support |
| **Training Vendor** | Security awareness | Training content, phishing simulations, competency assessment |

---

## 2. RACI Key

| Code | Meaning | Description |
|---|---|---|
| **R** | Responsible | Performs the work / delivers the capability |
| **A** | Accountable | Answers for the outcome. Only ONE per capability. |
| **C** | Consulted | Provides input before decisions |
| **I** | Informed | Receives status after action or decision |
| **D** | Delivers (provider) | Provider performs the operational work under CERG oversight |
| **V** | Validates (CERG) | CERG team confirms the provider's delivery meets standards |
| **O** | Oversees (CERG) | CERG team monitors provider delivery; does not perform it |

For clarity: **R/A/C/I** are standard RACI. **D/V/O** are AnyTech-specific extensions for the provider dimension. A provider can be **D** (delivers) while CERG is **V** (validates) and also **A** (accountable — CERG always retains accountability).

---

## 3. Provider-Specific RACI Dimensions

Each capability in the matrix below is assessed across two rows:

1. **CERG Internal** — who within the 8-person AnyTech team owns, validates, oversees
2. **Provider External** — which provider delivers, and what AnyTech's validation posture is

### Accountability Rule

**Accountability (A) ALWAYS stays with CERG.** Providers can be Responsible (R) or Deliver (D), but they are never Accountable. If a provider fails to deliver, CERG is accountable for detecting the failure and taking corrective action. This is the fundamental rule of vendor-oversight RACI.

---

## 4. Capability-to-Provider RACI Matrix

### 4.1 Detection and Monitoring

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Alert monitoring** (24/7) | V — Detection Engineer | D | — | — |
| **Threat intelligence** | O — Detection Engineer | D | — | — |
| **Detection engineering** (rule tuning) | V — Detection Engineer | D | — | — |
| **Log management** | O — Infrastructure Engineer | D (SIEM) | D (log sources) | — |
| **False positive management** | V — Detection Engineer | D | C | — |
| **Detection coverage mapping** | A — Infrastructure Engineer | D (report) | C (assets) | — |

### 4.2 Incident Response

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Incident command** | I — Engineering Lead | D (MSSP IC) | I | — |
| **Triage and containment** | I — Engineering Lead | D | C (if IT systems) | — |
| **Forensics and evidence** | I — Engineering Lead | D | — | — |
| **Business impact assessment** | A — Engineering Lead | C | C | — |
| **Regulatory notification** | A — Engineering Lead | C | — | — |
| **Root cause analysis** | V — Engineering Lead | D (report) | C | — |
| **Lessons learned** | A — Engineering Lead | C | C | — |
| **Remediation tracking** | A — Infrastructure Engineer | C (findings) | D (patches) | — |

### 4.3 Exposure and Vulnerability Management

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Vulnerability scanning** | V — Infrastructure Engineer | D (external scan) | D (internal scan) | — |
| **Patch management** | O — Infrastructure Engineer | — | D | — |
| **Vulnerability prioritization** | A — Infrastructure Engineer | C | C | — |
| **Remediation tracking** | A — Infrastructure Engineer | C | D (apply) | — |
| **Penetration testing** | V — Engineering Lead | D (annual) | C | — |
| **Exposure reporting** | A — Infrastructure Engineer | C (data) | C (data) | — |

### 4.4 Access and Identity Management

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **User access management** | V — Governance Analyst | — | D | — |
| **Privileged access management** | V — Infrastructure Engineer | — | D | — |
| **Access reviews** | A — Governance Analyst | C | D (report) | — |
| **Identity federation** | A — Infrastructure Engineer | — | D | — |
| **SSO and MFA administration** | V — Infrastructure Engineer | — | D | — |

### 4.5 Security Awareness and Training

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Training content** | V — Governance Analyst | — | — | D |
| **Phishing simulations** | V — Governance Analyst | — | — | D |
| **Competency assessment** | A — Governance Analyst | — | — | C |
| **Incident reporting culture** | A — All CERG | C | C | C |

### 4.6 Governance and Risk

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Policy management** | A — Governance Pillar Lead | I | I | I |
| **Risk register management** | A — Risk Pillar Lead | C (threat intel) | C (vuln data) | C |
| **Risk acceptance** | A — IT Director | C | C | — |
| **Evidence management** | A — Governance Analyst | C (reports) | C (reports) | C (reports) |
| **Compliance mapping** | A — Governance Pillar Lead | C | C | — |
| **Program improvement** | A — All Pillar Leads | C (findings) | C (findings) | C (findings) |

### 4.7 Business Continuity and Disaster Recovery

| Capability | CERG (Internal) | MSSP | MSP | Training Vendor |
|---|---|---|---|---|
| **Backup operations** | V — Infrastructure Engineer | — | D | — |
| **Restore testing** | A — Infrastructure Engineer | C (security) | D (perform) | — |
| **Business continuity planning** | A — IT Director | C | C | — |
| **Disaster recovery exercises** | V — All CERG | C | D | — |

---

## 5. Validation Rights

For every capability where CERG has a **V (Validate)** or **O (Oversee)** role, the CERG team must have:

| Right | Description |
|---|---|
| **Evidence access** | The provider must produce evidence of delivery on request, within agreed SLAs |
| **Observation access** | CERG may observe provider operations (e.g., shadow a triage shift) at least annually |
| **Sample review** | CERG may request random samples of provider output for quality review |
| **Findings challenge** | CERG may challenge provider findings and request re-evaluation |
| **Escalation access** | CERG has direct access to the provider's quality management team, not just the account manager |

If any of these rights are restricted by the current contract, document the restriction in the risk register and escalate to the IT Director.

---

## 6. RACI Change Management

The RACI matrix above is a baseline. It changes when:

1. **Provider scope changes** — MSSP takes on or drops a capability
2. **New provider onboarded** — e.g., adding a second MSSP, changing MSPs
3. **Internal team changes** — rebalancing roles across the 8-person team
4. **Capability maturity shifts** — a capability moves from provider-delivered to CERG-operated (or vice versa)

### Change Process

1. Engineering Lead proposes the RACI change
2. Risk Pillar Lead assesses impact on risk register entries
3. Governance Pillar Lead updates the RACI matrix
4. IT Director approves the change
5. The [Quarterly Provider Review](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) validates the updated RACI is being followed
6. Updated matrix is published within 10 business days

---

## 7. Common RACI Failures in the Vendor-Oversight Model

| Failure | What It Looks Like | Preventive Action |
|---|---|---|
| **RACI-at-signing** | RACI was correct when the contract was signed but has drifted as provider scope changed | Review RACI quarterly against the current contract |
| **Orphaned ownership** | A capability has a provider (D) but no CERG validator (V) | Every D must have a corresponding V |
| **Validation by assumption** | CERG asserts V but has no evidence access or review cadence | Define evidence access in the contract; maintain a sampling calendar |
| **Shadow RACI** | A provider does something CERG doesn't know about (or vice versa) | Annual RACI reconciliation with provider operations teams |
| **Provider-to-provider gaps** | MSSP and MSP each think the other owns a capability (e.g., endpoint detection coverage) | Map provider-to-provider handoffs explicitly; test in joint exercises |

---

## 8. Document Control

| Field | Value |
|---|---|
| **Artifact ID** | ANYTECH-RACI-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Risk Pillar Lead (AnyTech) |
| **Approved By** | Risk Pillar Lead |
| **Review Cycle** | Quarterly / On provider change |
| **Next Scheduled Review** | 2026-09-27 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Risk Pillar Lead | Initial release. Establishes the provider-specific RACI extension for AnyTech's vendor-oversight model, covering 7 capability domains across MSSP, MSP, and training vendor. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy (AnyTech) | `CERG-POL-001_Cybersecurity_Policy_AnyTech.md` | Parent policy |
| Operating Model (AnyTech) | `CERG-GOV-OM-001_Operating_Model_AnyTech.md` | Provider relationship framework |
| TPRM Procedure (AnyTech) | `CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md` | Vendor tiering and assessment |
| MSSP Engagement Playbook | `ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md` | Validation procedures |
| Quarterly Provider Review Kit | `ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md` | RACI review inputs |
| Consolidated Roles and RACI | `../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` | Upstream RACI methodology |

---
