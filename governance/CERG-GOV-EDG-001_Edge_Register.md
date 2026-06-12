# SURGE: Cyber Engineering, Risk & Governance

## EDGE REGISTER
### The Organizational Edge Is No Longer Only IP Space · Six Edge Types · Defend What's Actually Reachable

---

| | |
|---|---|
| **Document ID** | CERG-GOV-EDG-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst / Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-NET-001](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) · [CERG-STD-SDL-001](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) |
| **Review Cycle** | Annual / On material change to vendor population, SaaS portfolio, or network architecture |
| **Frameworks** | NIST CSF 2.0 (IDENTIFY, GOVERN) · NIST 800-53r5 (CA, SA, SR) · NIST 800-161r1 |
| **Regulations** | NERC-CIP CIP-013 · CMMC L2 · SOX ITGC |
| **Environments** | All organizational edges — network, identity, SaaS, vendor, software supply, data |

---

## Table of Contents

1. [The Edge — What Changed](#1-the-edge--what-changed)
2. [The Six Edge Types](#2-the-six-edge-types)
3. [Edge Management Model](#3-edge-management-model)
4. [Low-Control / High-Dependency Operating Model](#4-low-control--high-dependency-operating-model)
5. [Edge Register Operations](#5-edge-register-operations)
6. [Document Control](#6-document-control)

---

## 1. The Edge — What Changed

For twenty years, "the organizational edge" meant the firewall. You knew what was inside and what was outside, and security's job was to harden the perimeter.

That edge no longer exists in any useful form. Organizations operate across SaaS tenants, identity providers, vendor admin paths, MSP tooling, CI/CD dependencies, managed detection providers, cloud control planes, APIs, domains, certificates, subprocessors, and data egress paths. Each of these is a boundary across which trust, data, privilege, or control flows. Each of these is an edge.

> **The organizational edge is not a network diagram. It is the set of boundaries across which the organization's security posture can be changed by someone outside the organization.**

CERG maintains this Edge Register as the authoritative inventory of organizational edges. It is not a replacement for the TPRM procedure — it is the conceptual model that elevates third-party and supply-chain risk from "a procedure" to a first-class architectural concern. The TPRM procedure ([CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)) is the operational document that implements this model.

A program that truly knows its edge is less impressed by AI-powered attack branding. The edge doesn't care whether the attacker used AI. It cares whether the path existed.

---

## 2. The Six Edge Types

### 2.1 Network Edge

The traditional perimeter — and still relevant. What is Internet-reachable? What VPNs, APIs, and remote-access paths exist?

| Attribute | Description |
|-----------|-------------|
| **Examples** | Internet-facing hosts, VPN concentrators, public APIs, cloud load balancers, exposed management interfaces |
| **Primary owner** | Network Engineering / Cloud Engineering |
| **CERG role** | Risk validates external attack surface continuously; Engineering reviews architecture for new Internet-facing services |
| **Evidence** | EASM export, DNS/cloud reconciliation, firewall rule review |
| **Key question** | "If we didn't know this was here, could an attacker find it?" |

### 2.2 Identity Edge

The most consequential edge in modern environments. Who can authenticate? What can they reach after authentication? What federated trust relationships exist?

| Attribute | Description |
|-----------|-------------|
| **Examples** | IdP (Entra ID, Okta), federation trusts, OAuth applications, privileged groups, service principals, API keys |
| **Primary owner** | Identity Engineering |
| **CERG role** | Risk monitors privileged access; Governance tracks recertification; Engineering reviews federation and OAuth grants |
| **Evidence** | IdP logs, privileged group membership diff, OAuth application inventory, service principal audit |
| **Key question** | "If an attacker has a valid credential, what can they reach before we detect them?" |

### 2.3 SaaS Edge

Every SaaS tenant is an organizational edge. The organization's data, identities, and configurations live inside a provider's infrastructure.

| Attribute | Description |
|-----------|-------------|
| **Examples** | M365 tenant, Salesforce org, Workday instance, ServiceNow, GitHub org, Slack workspace |
| **Primary owner** | Business application owners + IT |
| **CERG role** | Governance maintains Approved Provider Catalog; Risk runs SSPM; Engineering reviews tenant configurations |
| **Evidence** | SSPM report, admin setting export, OAuth grant review, shared responsibility matrix per provider |
| **Key question** | "What data lives in this tenant, who can access it, and what happens if the provider is compromised?" |

### 2.4 Vendor Edge

Vendors and service providers with privileged access, remote connectivity, or administrative paths into organizational systems.

| Attribute | Description |
|-----------|-------------|
| **Examples** | MSP tooling, remote support accounts, OT vendor maintenance access, managed detection providers, contractor admin paths |
| **Primary owner** | Vendor Risk Analyst |
| **CERG role** | Risk assesses and tiers vendors; Governance tracks contract clauses and evidence; Engineering validates access controls |
| **Evidence** | PAM session logs, vendor access review, contract clause register, kill-switch test records |
| **Key question** | "If this vendor is compromised, what can the attacker reach, and how fast can we cut them off?" |

### 2.5 Software Supply Edge

Every dependency — open-source library, commercial SDK, CI/CD pipeline, build system — is a path through which malicious code can enter the organization.

| Attribute | Description |
|-----------|-------------|
| **Examples** | npm/PyPI/Maven packages, Docker base images, CI/CD pipeline integrations, build system access, signed releases |
| **Primary owner** | Engineering / Application Security |
| **CERG role** | Risk runs SCA; Engineering maintains SBOM; Governance tracks integrity requirements |
| **Evidence** | SBOM (NTIA minimum elements), CVE advisory subscription, signed release verification, pipeline access review |
| **Key question** | "If a popular open-source package we depend on is compromised tonight, do we know within hours?" |

### 2.6 Data Edge

Every path through which organizational data leaves the organization's control — subprocessors, external data shares, outbound integrations, backup targets.

| Attribute | Description |
|-----------|-------------|
| **Examples** | External data shares (SharePoint, Box), subprocessor data flows, outbound API integrations, backup replication targets, analytics pipelines |
| **Primary owner** | Data Governance / Business application owners |
| **CERG role** | Governance tracks subprocessor inventory; Risk assesses data egress paths; Engineering reviews integration architecture |
| **Evidence** | Subprocessor register, data flow diagrams, DLP policy coverage, external share audit |
| **Key question** | "Where does our data live outside our control, and who can see it?" |

---

## 3. Edge Management Model

Every edge is managed through a common lifecycle:

| Phase | Activity | Owner |
|-------|----------|-------|
| **Discover** | Identify and inventory the edge. What exists? | Risk / Engineering |
| **Assess** | Evaluate the risk. What's the blast radius if compromised? | Risk |
| **Control** | Implement controls. What reduces the exposure to acceptable levels? | Engineering |
| **Monitor** | Continuously validate. Has anything changed? | Risk |
| **Respond** | React to compromise. How fast can we cut access? | Engineering / Risk / SCCT |

Each edge type has its own discovery cadence, assessment criteria, control catalog, and monitoring signals. The table below summarizes the primary tooling and evidence for each type:

| Edge Type | Discovery | Assessment | Control | Monitoring |
|-----------|-----------|------------|---------|------------|
| Network | EASM, external scan, cloud inventory | CVSS + exposure + asset criticality | Firewall, WAF, ACL, segmentation | Continuous external scan, drift detection |
| Identity | IdP export, privileged group review | Access review, privilege analysis | PAM, JIT, phishing-resistant MFA | IdP logs, anomalous access detection |
| SaaS | SSPM, tenant inventory, OAuth review | Configuration assessment, data classification | Tenant configuration baseline, OAuth app approval | SSPM continuous monitoring, drift alerting |
| Vendor | Vendor register, contract review | Tier-based assessment, evidence collection | PAM, session recording, kill-switch | Access review, SOC 2 / attestation monitoring |
| Software supply | SBOM, pipeline inventory, dependency scan | CVE matching, exploitability analysis | Signed releases, pipeline access control, dependency pinning | SCA continuous monitoring, advisory feeds |
| Data | DLP discovery, share audit, integration map | Data classification, egress path analysis | DLP policies, encryption, access controls | DLP alerts, external share review, subprocessor change alerts |

---

## 4. Low-Control / High-Dependency Operating Model

Not all edges can be controlled. Some can only be influenced, contracted, or monitored. CERG recognizes four control levels:

| Control Level | What the Org Can Do | Examples |
|---------------|---------------------|----------|
| **Direct Control** | Configure, monitor, patch, test | Owned servers, self-managed cloud workloads, on-premise network |
| **Shared Control** | Configure tenant, require evidence, validate logs | SaaS tenants (M365, Salesforce), IaaS/PaaS (AWS, Azure) |
| **Contractual Control** | Negotiate clauses, notification, audit rights | MSPs, managed security providers, subprocessors |
| **Opaque Dependency** | Track residual risk, exit plan, kill switch, compensating monitoring | SaaS vendor's underlying infrastructure, open-source library maintainers, upstream cloud provider outages |

**Operating at each level:**

- **Direct and Shared control** environments follow standard CERG controls — baselines, scanning, change management, evidence collection.
- **Contractual control** environments require: security clauses in contracts, annual evidence collection (SOC 2, ISO 27001, or equivalent), incident notification commitments, and a tested kill-switch procedure.
- **Opaque dependency** environments require: documented residual risk acceptance, an exit/migration plan, compensating monitoring (e.g., CSPM/SSPM for what IS visible), and a documented assumption of what the dependency provides. CERG does not pretend to control what it cannot control.

---

## 5. Edge Register Operations

### 5.1 Register Maintenance

The Edge Register is maintained as a living document. The Vendor Risk Analyst (or delegate) reviews each edge type quarterly:

- New edges added within 30 days of discovery
- Edges retired when the relationship, service, or path no longer exists
- Control level re-assessed annually

### 5.2 Integration with CERG Procedures

| Procedure | Edge Type | Integration |
|-----------|-----------|-------------|
| [TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor, SaaS, Software supply | Primary operational procedure for third-party edges |
| [VM-001](../procedures/CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | Network, Software supply | Exposure management feeds edge assessment |
| [AC-002](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) | Identity, Vendor | Access reviews and privileged access management |
| [AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | All | New services trigger edge registration during architecture review |
| [IR Plan](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | All | SCCT activation when a vendor edge is compromised |

### 5.3 The Principle

> **A program that knows its edge is less impressed by attack branding.**
>
> AI-powered attacks, supply-chain campaigns, and nation-state actors all exploit the same thing: an edge the organization didn't know it had, or didn't manage. The edge doesn't care about the attacker's tooling. It cares whether the path existed.

---

## 6. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 | 2026-06 | CERG Governance | Initial release. Six edge types, edge management model, low-control operating model. |

### Review Triggers

Annual review or upon: material change to vendor population, SaaS portfolio, network architecture, or regulatory scope.

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| TPRM Procedure | CERG-PRC-TPRM-001 | Operational implementation of vendor, SaaS, and software supply edges |
| Access Management Standard | CERG-STD-AC-001 | Identity edge controls |
| IT/Cloud/SaaS Security Standard | CERG-STD-IT-001 | SaaS and cloud edge controls |
| Network Security Standard | CERG-STD-NET-001 | Network edge controls |
| Secure Development Standard | CERG-STD-SDL-001 | Software supply edge controls |
| Cross-Pillar Operational Flows | CERG-GOV-FLOW-001 | SCCT activation and edge compromise response |
| Exposure Management Procedure | CERG-PRC-VM-001 | Exposure discovery feeds network and software supply edge assessment |

---

> **SURGE, Cyber Engineering, Risk & Governance**
>
> _Know your edge. Manage it deliberately. Never be surprised._

---

_CERG-GOV-EDG-001 · Version 1.0 · PUBLIC_
