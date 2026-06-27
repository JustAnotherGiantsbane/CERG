## THE CERG FRAMEWORK — AnyTech Adaptation

### Cyber Engineering, Risk, and Governance as a Vendor-Oversight Model

| | |
|---|---|
| **Document ID** | CERG-GOV-FRM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to the framework |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Three Pillars](#2-the-three-pillars)
3. [Cyber Engineering — Provider Oversight](#3-cyber-engineering--provider-oversight)
4. [Cyber Risk — Provider-Augmented Risk Management](#4-cyber-risk--provider-augmented-risk-management)
5. [Cyber Governance — Provider Compliance and Policy](#5-cyber-governance--provider-compliance-and-policy)
6. [How the Pillars Work Together](#6-how-the-pillars-work-together)
7. [Targeting NIST CSF Adaptive Maturity](#7-targeting-nist-csf-20-adaptive-maturity)
8. [Getting Started — The Path to Operating](#8-getting-started--the-path-to-operating)
9. [Document Control](#9-document-control)

---

## 1. Executive Summary

AnyTech operates a **cyber program office** — an 8-person cybersecurity team that does not run security tools or execute security operations directly. The team's job is to ensure that contracted providers (MSSP, MSP, training vendor) deliver effective security on AnyTech's behalf.

The CERG framework — Cyber Engineering, Risk, and Governance — structures this work into three tightly coupled pillars. Each pillar has a distinct role in provider oversight:

- **Engineering** sets security requirements and validates provider delivery
- **Risk** owns risk decisions informed by provider data
- **Governance** sets policy, collects evidence, and enforces accountability

This framework is a direct adaptation of the standard CERG model for organizations where security operations are delivered by external providers rather than an internal team.

---

## 2. The Three Pillars

The CERG model divides cybersecurity work into three activities:

| Pillar | Mandate | AnyTech Focus |
|--------|---------|--------------|
| **Engineering** | Build and deploy secure technology alongside the business | Set security requirements for MSP; validate provider architecture; review new services and changes |
| **Risk** | Assess exposure and manage risk continuously | Score and treat risks based on MSSP/MSP data; manage exception process; track exposure |
| **Governance** | Set standards, ensure compliance, and track conformance | Write policy; collect provider evidence; monitor SLAs; maintain the document library |

The three pillars operate as a loop, not a hierarchy. Engineering findings feed Risk scoring. Risk decisions drive Governance oversight. Governance requirements inform Engineering direction.

---

## 3. Cyber Engineering — Provider Oversight

### 3.1 What Engineering Does at AnyTech

In a standard CERG deployment, Engineering builds and deploys security technology. At AnyTech, Engineering **sets the requirements** that the MSP and other providers must meet, and **validates** that provider-delivered solutions meet those requirements.

### 3.2 Core Activities

- **Security requirements management:** Define security baselines for AnyTech environments. These become contractual obligations for providers.
- **Architecture review:** Review material changes proposed by MSP or new SaaS provider onboarding. Confirm changes do not introduce unacceptable risk.
- **Provider technical validation:** Annually confirm that MSSP and MSP technical controls meet contractual requirements. Review SOC 2 technical controls sections.
- **Crown jewel identification:** Maintain the asset register and classify systems by criticality. This feeds Risk scoring and MSP prioritization.
- **Incident technical support:** If the MSSP requests engineering context during an incident, Engineering provides it. Engineering does not lead IR — the MSSP does.

### 3.3 What Engineering Does NOT Do

- Run vulnerability scanners (MSP does)
- Operate endpoint protection platforms (MSP does)
- Configure firewalls or network equipment (MSP does)
- Build or maintain security tools

---

## 4. Cyber Risk — Provider-Augmented Risk Management

### 4.1 What Risk Does at AnyTech

In a standard CERG deployment, Risk runs scans, tests, and analyzes data. At AnyTech, Risk **receives risk-relevant data from providers** and makes risk decisions based on it.

### 4.2 Core Activities

- **Risk register management:** Own the single authoritative record of cybersecurity risk. Seed from known concerns, MSSP threat intel, and MSP vulnerability data.
- **Risk scoring:** Apply the CERG Risk Management Framework ([RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md)). Scores are based on provider-provided data, not internal tooling.
- **Exception management:** Process, document, and track exceptions. Escalate to IT Director for High/Critical risks.
- **Exposure management:** Track vulnerability findings from MSP scanner exports. Prioritize by criticality. Ticket MSP for remediation. Verify closure via MSSP monitoring.
- **Vendor risk assessments:** Assess providers under [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md). Quarterly review of Tier 1 providers (MSSP, MSP).
- **Incident business ownership:** When the MSSP responds to an incident, the Risk Pillar Leader owns the business-side response: communication, regulatory notification, root cause, remediation tracking.

### 4.3 What Risk Does NOT Do

- Run penetration tests (MSSP does via contracted pentesting)
- Operate SIEM (MSSP does)
- Write detection rules (MSSP does)
- Run adversary simulation (contracted separately if needed)

---

## 5. Cyber Governance — Provider Compliance and Policy

### 5.1 What Governance Does at AnyTech

Governance ensures that the program operates within its defined rules and that providers are meeting their commitments.

### 5.2 Core Activities

- **Policy lifecycle:** Maintain and review CERG policies. Ensure providers acknowledge and demonstrate compliance.
- **Evidence collection:** Collect SLA reports, SOC 2 reports, patch compliance data, and access review evidence from providers. Maintain the evidence library.
- **SLA tracking:** Monitor provider contractual obligations. Flag SLA misses. Escalate persistent underperformance.
- **Document control:** Maintain the document catalog ([CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md)). Track adoption status and review cycles.
- **Provider performance reviews:** Organize quarterly business reviews with MSSP, MSP, and training vendor. Document findings and action items.
- **Regulatory monitoring:** Track emerging regulatory obligations that may apply to AnyTech. When one triggers, lead the adoption of the applicable package.

### 5.3 What Governance Does NOT Do

- Deliver training (training vendor does)
- Manage provider contracts (legal/procurement does; Governance advises)
- Operate a GRC platform (may be introduced later)

---

## 6. How the Pillars Work Together

### 6.1 A Week in the Life of AnyTech CERG

| Day | Activity | Pillars Involved |
|-----|----------|-----------------|
| Monday | Weekly standup: review open exposures, active risks, provider SLA status | All three |
| Tuesday | MSP patch report review — Engineering validates, Risk scores overdue items | Engineering + Risk |
| Wednesday | Risk register update — new risk from MSSP threat intel feed | Risk |
| Thursday | Provider evidence collection — Governance pulls monthly SLA data from MSSP | Governance |
| Friday | Exception review — any expiring exceptions flagged for IT Director approval | All three |

### 6.2 Key Cross-Pillar Flows

| Trigger | Engineering | Risk | Governance |
|---------|-------------|------|------------|
| New SaaS purchase | Reviews security posture | Scores vendor risk | Collects contract evidence |
| Critical vulnerability found | Confirms with MSP asset owner | Scores exposure | Patches exception if needed |
| MSSP reports incident | Provides technical context | Owns business-side response | Documents lessons learned |
| Policy review due | Provides technical input | Provides risk data | Leads review and approval |
| Provider SLA missed | Assesses operational impact | Escalates in risk register | Triggers contract remedy |

---

## 7. Targeting NIST CSF 2.0 Adaptive Maturity

The NIST CSF 2.0 tier model applies equally to AnyTech, but the path is different. A provider-oversight organization achieves Adaptive maturity when:

- **Govern:** Provider contracts include security requirements. CERG oversight is independent of provider operations. Risk appetite is documented and reviewed.
- **Identify:** Asset inventory is current (MSP-owned). Risk register is active. Crown jewels are identified.
- **Protect:** Safeguards are provider-delivered but validated by Engineering. Access controls, data protection, and configuration baselines are in provider SLAs.
- **Detect:** MSSP monitors continuously. CERG reviews detection coverage quarterly. Alert quality is measured.
- **Respond:** MSSP has a tested IR plan. CERG has a tested escalation and communication plan. Joint tabletops occur annually.
- **Recover:** MSP owns backup/restore. CERG validates quarterly. BCP/DR plans are exercised annually.

AnyTech's target is **Tier 3 (Repeatable) in the first two quarters, Tier 4 (Adaptive) by the end of year one.**

---

## 8. Getting Started — The Path to Operating

### First 30 Days

| Week | Outcome |
|------|---------|
| 1 | Confirm IT Director as authority. Map MSSP + MSP scope boundaries. Fill organization profile. |
| 2 | Seed risk register with top 10 risks. MSSP delivers first SIER health report. MSP delivers first patch report. |
| 3 | First exception or risk acceptance documented. Evidence library structure created. |
| 4 | First monthly risk review with IT Director. First provider SLA check. |

### Key Artifacts to Create

1. Risk register (first 10 entries)
2. Exposure backlog (triage MSP scanner output)
3. Evidence index (start with MSSP monthly report)
4. Provider SLA scorecard template
5. Incident escalation contact sheet

---

## 9. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | CERG Engineering | AnyTech adaptation. Three pillars reframed for vendor-oversight model. |

### Review Triggers

- Annual review cycle
- Change in AnyTech provider landscape
- Material change to the CERG framework approach
- Direction from IT Director

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Cybersecurity Policy | [POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Parent policy |
| Operating Model | [OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Operating description |
| Risk Management Framework | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) | Risk scoring and acceptance |
| Document Catalog | [CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Full document inventory |
