## CERG CYBERSECURITY POLICY — AnyTech Adaptation

### 6 Foundational Principles for a Vendor-Managed Security Program

> This policy defines the cybersecurity guardrails for AnyTech. It does not prescribe
> operations — those are delivered by providers under CERG oversight. This policy
> establishes what is always true, regardless of which provider handles execution.

| | |
|---|---|
| **Document ID** | CERG-POL-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Internal |
| **Owner** | Governance Pillar Leader (AnyTech CERG) |
| **Parent Policy** | Not applicable; this is the parent policy |
| **Review Cycle** | Annual / On significant provider change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The AnyTech CERG Operating Model](#2-the-anytech-cerg-operating-model)
3. [Foundational Security Principles](#3-foundational-security-principles)
4. [Roles and Responsibilities](#4-roles-and-responsibilities)
5. [Provider Management](#5-provider-management)
6. [Exceptions and Risk Acceptance](#6-exceptions-and-risk-acceptance)
7. [Compliance and Enforcement](#7-compliance-and-enforcement)
8. [Policy Review and Maintenance](#8-policy-review-and-maintenance)
9. [Related Documents](#9-related-documents)
10. [Document Control](#10-document-control)

---

## 1. Purpose and Scope

This policy establishes the foundational cybersecurity principles for AnyTech. It governs all information and technology assets, environments, and data within the AnyTech operating scope, regardless of whether those assets are managed internally by the CERG team or by contracted providers (MSSP, MSP, training vendors, SaaS providers).

The CERG team does not operate security tools or execute security operations directly. This policy sets the standards to which providers must operate on AnyTech's behalf.

### 1.1 Scope

This policy applies to:

- All AnyTech-owned or managed systems, data, and networks
- All provider-managed environments that process, store, or transmit AnyTech data
- All personnel — AnyTech employees and provider staff operating within AnyTech scope
- All third-party services with access to AnyTech environments

### 1.2 What This Policy Does Not Cover

This policy does not prescribe technology-specific configurations, tool choices, or operational runbooks. Those are established in provider contracts, SLAs, and the AnyTech CERG operating model ([OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md)).

---

## 2. The AnyTech CERG Operating Model

AnyTech operates a **cyber program office** model. The 8-person CERG team (Engineering, Risk, and Governance pillars) does not execute security operations. It oversees the providers who do.

- **MSSP** delivers SOC monitoring, detection engineering, incident response, and threat intelligence
- **MSP** delivers IT operations including patching, identity management, endpoint management, and asset management
- **Training vendor** delivers phishing simulations and mandatory employee security training
- **CERG team** owns policy, risk decisions, vendor oversight, exposure visibility, and architecture direction

The CERG pillar leaders report to the **IT Director**, who serves as the executive risk acceptance authority.

See [OM-001 Operating Model](CERG-GOV-OM-001_Operating_Model_AnyTech.md) for the full operating description.

---

## 3. Foundational Security Principles

### Principle 1 — Risk Ownership Cannot Be Delegated

AnyTech's CERG team owns all cybersecurity risk decisions. Providers may execute risk treatments, but the decision to accept, transfer, mitigate, or avoid a risk is made by the CERG team with IT Director concurrence for High and Critical risks.

### Principle 2 — Provider Security Is AnyTech Security

Every provider with access to AnyTech environments or data shall meet the security requirements defined in this policy and the Third-Party Risk Procedure [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md). A provider's security failure is AnyTech's security failure.

### Principle 3 — Evidence Is Required, Trust Is Not Sufficient

Providers must demonstrate compliance with security requirements through documented evidence. SLAs, SOC 2 reports, vulnerability scan exports, and access review outputs are evidence. Verbal assurance is not.

### Principle 4 — Secure by Default

All systems, applications, and services used by AnyTech shall be configured for the most secure operational state that the business function can tolerate. Secure defaults are established in provider contracts and validated during quarterly reviews.

### Principle 5 — Least Privilege and Need-to-Know

Access to AnyTech systems and data shall be granted on a least-privilege basis. Provider staff shall have access only to the systems and data required to perform their contracted scope. Access is reviewed quarterly.

### Principle 6 — Continuous Visibility

AnyTech shall maintain continuous visibility into its security posture through provider-provided data. The CERG team shall have access to MSSP monitoring dashboards, MSP patch compliance reports, and incident telemetry. AnyTech does not operate in a blind trust model.

### Principle 7 — Incidents Are Owned, Not Transferred

When an incident occurs, the MSSP leads technical response. However, the CERG **Risk Pillar Leader** owns the incident from a business perspective: communication, regulatory notification (if required), root cause analysis, and remediation tracking. Incident ownership is shared, not abandoned to the provider.

### Principle 8 — Continuous Improvement

Every incident, near-miss, provider SLA miss, and control gap is input into the improvement process. Lessons learned drive changes to contracts, procedures, and technical configurations.

---

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **IT Director** | Executive risk acceptance authority; approves policy; final escalation for provider performance issues |
| **Engineering Pillar Leader** | Sets security requirements for providers; validates architecture; reviews MSP-proposed changes |
| **Risk Pillar Leader** | Manages risk register; leads incident ownership from business side; tracks exposure; manages exceptions |
| **Governance Pillar Leader** | Manages policy lifecycle; collects provider evidence; tracks SLA compliance; drives document control |
| **MSSP** | Delivers SOC monitoring, detection engineering, IR, threat intelligence per SLA |
| **MSP** | Delivers IT operations, patching, IAM, endpoint management per SLA |
| **Training Vendor** | Delivers phishing simulations and mandatory employee training per contract |
| **All personnel** | Report security incidents to CERG; complete mandatory training; follow security policies |

---

## 5. Provider Management

All providers operating within AnyTech scope shall:

1. Maintain a current SOC 2 Type II report (Tier 1 providers) or equivalent certification
2. Provide monthly SLA performance reporting to CERG Governance
3. Notify CERG within 24 hours of any security incident affecting AnyTech
4. Participate in quarterly provider business reviews
5. Maintain documented incident response and business continuity plans
6. Allow CERG right-to-audit upon 30 days notice
7. Flow down AnyTech security requirements to their sub-processors

See [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) for the complete provider management procedure.

---

## 6. Exceptions and Risk Acceptance

Any deviation from this policy or its subordinate procedures requires a documented exception or risk acceptance.

- **Low/Medium risk:** Approved by Engineering or Risk Pillar Leader
- **High risk:** Approved by IT Director
- **Critical risk:** Approved by IT Director with documentation to board/CEO

All exceptions are tracked in the risk register and reviewed at least monthly. See [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) and [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) for the complete framework.

---

## 7. Compliance and Enforcement

- CERG Governance Pillar Leader monitors compliance with this policy
- Providers found non-compliant are subject to the SLA framework in [OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) §10
- AnyTech personnel found knowingly violating this policy are subject to escalation to the IT Director
- Persistent non-compliance by any provider triggers contract renegotiation or termination

---

## 8. Policy Review and Maintenance

This policy is reviewed annually by the CERG Governance Pillar Leader and approved by the IT Director. Unscheduled review is triggered by:

- A material change in AnyTech's provider landscape
- A significant security incident
- A change in regulatory obligations
- Direction from the IT Director

---

## 9. Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Operating Model | [OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Defines the program-office model this policy governs |
| Risk Management Framework | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) | Risk scoring and acceptance framework |
| Risk Register and Exception Process | [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) | Operational risk workflow |
| Third-Party Risk Procedure | [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) | Provider oversight procedure |
| Exposure Management Procedure | [PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure_AnyTech.md) | Vulnerability and exposure tracking |
| Framework | [FRM-001](CERG-GOV-FRM-001_CERG_Framework_AnyTech.md) | Three-pillar model explanation |
| Document Catalog | [CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Full document inventory and status |

---

## 10. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | CERG Governance | Initial AnyTech adaptation. 8 principles for vendor-managed security program. IT Director as approval authority. |

### Review Triggers

- Annual review cycle
- Change in AnyTech's provider landscape (new MSSP, MSP change, etc.)
- Significant security incident
- Change in regulatory obligations
- Direction from IT Director

### Related Documents

See §9 above.