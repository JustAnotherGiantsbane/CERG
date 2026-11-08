## THIRD-PARTY AND SUPPLY CHAIN RISK PROCEDURE — AnyTech Adaptation
### Provider Oversight Model · Three-Tier Vendor System · MSSP/MSP-Specific Processes

---

| | |
|---|---|
| **Document ID** | CERG-PRC-TPRM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On new critical vendor onboarding |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech-managed environments, AnyTech SaaS footprint |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Interface to Procurement / MSP](#2-roles-and-interface-to-procurement--msp)
3. [Vendor Tiering](#3-vendor-tiering)
4. [Evidence by Tier](#4-evidence-by-tier)
5. [MSSP-Specific Oversight Process](#5-mssp-specific-oversight-process)
6. [MSP-Specific Oversight Process](#6-msp-specific-oversight-process)
7. [Contract Security Clause Library](#7-contract-security-clause-library)
8. [Shared Responsibility Matrix for MSSP and MSP](#8-shared-responsibility-matrix-for-mssp-and-msp)
9. [Continuous Monitoring and Re-Assessment](#9-continuous-monitoring-and-re-assessment)
10. [Approval Authority](#10-approval-authority)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

AnyTech operates a **cyber program office** model — an 8-person CERG team that oversees a federation of contracted security and IT providers. The three primary providers are an MSSP (SOC/IR), an MSP (IT operations), and a training vendor (awareness and phishing simulation). AnyTech has no in-house SOC, no dedicated IT operations team, and no internal security training function.

This procedure defines how CERG engages with the broader vendor management process, where CERG's cyber-specific work begins and ends, what evidence is collected at each vendor tier, and how the program maintains continuous oversight of provider security posture.

> **CERG Doesn't Own Vendor Management, It Owns the Cyber-Risk Slice**
>
> Procurement and the MSP own the vendor lifecycle — onboarding, contracts, master vendor records, and IT service provisioning. CERG accepts the business-determined vendor criticality as the starting point and applies a cyber-specific overlay: evidence requirements, SLA tracking, security clause enforcement, and risk acceptance for provider-related exposures. This boundary keeps an 8-person team focused on the security outcomes that matter.

### 1.1 Scope

This procedure applies to:

- **All third-party vendors and service providers** that access, process, or store AnyTech data or systems.
- **The three primary contracted providers** — MSSP (SOC/IR), MSP (IT operations), and training vendor (awareness/phishing) — with specific oversight processes defined for each.
- **AnyTech SaaS footprint** — all SaaS platforms used by AnyTech personnel, regardless of whether they are procured through formal vendor management.
- **Future vendors** — any new provider relationship initiated after this procedure's effective date.

### 1.2 Out of Scope

The following are outside this procedure's scope because they do not apply to AnyTech's operating context:

- **NERC-CIP CIP-013** — AnyTech is not a bulk electric system operator.
- **CMMC / DFARS / CUI** — AnyTech does not handle Controlled Unclassified Information or perform federal contract work requiring CMMC certification.
- **FedRAMP** — AnyTech is not a federal agency or federal contractor requiring FedRAMP-authorised services.
- **SOX ITGC** — AnyTech is not a publicly traded company subject to Sarbanes-Oxley.
- **SBOM and software supply chain** — AnyTech does not develop or deploy software products to customers; SBOM requirements are not applicable to AnyTech's provider oversight model.
- **International access controls** — AnyTech's data is not subject to export control or cross-border data flow restrictions at this time. International access by providers (e.g., MSSP's India office) is governed by contract data residency clauses and BCP coverage, not by a country-risk access framework.

### 1.3 Relationship to Other Documents

This procedure is the AnyTech-specific operationalisation of [CERG-PRC-TPRM-001](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) in the main CERG corpus. Where the main procedure addresses complex regulatory regimes (CIP-013, CMMC, FedRAMP, SBOM), this adaptation strips those out and instead provides the MSSP- and MSP-specific oversight processes that drive AnyTech's program.

This document is referenced by:
- [CERG-GOV-OM-001 (AnyTech Adaptation)](CERG-GOV-OM-001_Operating_Model_AnyTech.md) — defines the operating model, provider engagement patterns, and RACI matrices.
- [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) — Risk register and exception process; provider-related risks are intaken here.
- [CERG-PRC-AUD-001](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) — Evidence management procedure; provider evidence artifacts follow this process.
- [CERG-PRC-AR-001](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) — Architecture review; provider-proposed changes are evaluated per this procedure.

---

## 2. Roles and Interface to Procurement / MSP

### 2.1 Role Definitions

| **Function** | **Owns** | **CERG Interface** |
|---|---|---|
| **Procurement** | Vendor onboarding, contracts, master vendor record, license management | CERG reviews proposed contracts for security clauses; Governance Pillar Leader signs off on Tier 1 vendor security acceptance. |
| **MSP** | IT operations delivery, including vendor-relationship support where MSP administers SaaS platforms | CERG receives MSP vendor-performance data (e.g., patching status for SaaS-hosted infra); MSP notifies CERG before material changes to AnyTech's environment. |
| **IT Director** | Executive risk acceptance for cyber-related vendor decisions | Final sign-off on Tier 1 vendor acceptance, Tier 1 contract security scope changes, and risk acceptance for vendor-related exposures above Risk Pillar Leader authority. |
| **Engineering Pillar Leader** | Provider technical due diligence, architecture validation | Reviews provider-proposed changes with security impact; signs off on Tier 2/3 vendor acceptance; validates MSSP detection coverage and MSP patch compliance. |
| **Risk Pillar Leader** | Vendor risk assessment methodology, risk register entries from provider findings | Conducts periodic risk assessments per this procedure; inputs provider-related risk findings into the risk register. |
| **Governance Pillar Leader** | This procedure, evidence collection from providers, SLA tracking, QBRs, contract clause reviews, audit evidence | Leads quarterly provider business reviews; maintains evidence library; tracks SLA performance; coordinates with Procurement on contract security language. |
| **Evidence / SLA Manager** | Evidence collection, validation, and archiving; SLA metric tracking | Collects MSSP/MSP evidence on standing cadence; produces monthly SLA performance reports; supports QBR preparation. |

### 2.2 Vendor Onboarding Flow

1. **Procurement** initiates vendor engagement and provides the proposed vendor's scope, data classification, and access requirements to CERG.
2. **Governance Pillar Leader** evaluates the vendor against the tiering criteria in Section 3 and assigns a proposed tier.
3. **Engineering Pillar Leader** (for technical vendors) conducts a technical due diligence review — architecture, data flow, access model, encryption.
4. **Risk Pillar Leader** records the vendor in the risk register and inputs initial risk assessment findings.
5. **Governance Pillar Leader** applies the evidence requirements per Section 4, reviews proposed contract clauses against the library in Section 7, and prepares the acceptance package.
6. **Approval authority per Section 10** signs off.
7. **Governance Pillar Leader** records the vendor in the Approved Provider and SaaS Catalog (per the operating model) with status, tier, evidence links, and next review date.

---

## 3. Vendor Tiering

AnyTech uses a **3-tier vendor model** aligned to the cyber program office's scale. This is simpler than the enterprise 5-tier model because AnyTech's vendor portfolio is concentrated around a small number of critical providers.

| **Tier** | **Description** | **Examples** |
|---|---|---|
| **Tier 1 — Critical** | Failure or compromise has material business, operational, or reputational impact. Provider operates with elevated access to AnyTech systems or data. | MSSP (SOC/IR — privileged access to all monitored systems), MSP (IT operations — privileged access to infrastructure, endpoints, identity). |
| **Tier 2 — Important** | Failure or compromise materially disrupts operations or processes sensitive (but not critical) data. | Training vendor (access to employee directory, phishing simulation platform), major SaaS platforms (core productivity, HR, finance). |
| **Tier 3 — Standard** | Failure or compromise is operationally inconvenient but recoverable. Limited data access, no privileged system access. | Low-risk SaaS (marketing tools, project management one-off), one-off contractors with restricted system access, commodity services. |

### 3.1 Tiering Inputs

CERG accepts the **business criticality** from Procurement / the MSP as the starting point and applies a cyber-specific adjustment only when security concerns are material. Inputs considered:

- **Data classification** handled by the vendor (Public vs. Internal vs. Restricted).
- **System access level** (no access, user-level access, administrative/privileged access).
- **Blast radius** — how many systems or data stores are accessible if the vendor is compromised.
- **Operational dependency** — can AnyTech operate without this vendor for a day? A week? A month?
- **Regulatory scope** — currently none, but tracked if applicable in the future.

### 3.2 Tier Adjustment Factors

| **Cyber Concern** | **Adjustment** |
|---|---|
| Vendor has privileged (administrative) access to AnyTech systems | +1 tier (to T1 if not already) |
| Vendor processes or stores Restricted-classification data | +1 tier |
| Vendor has a material breach affecting its customers within the past 12 months | +1 tier with case-by-case review |
| Vendor is unable to produce required evidence for its proposed tier | Hold at lower tier until evidence is current |
| Vendor relationship includes a material sub-processor change | +1 tier if sub-processor is new or in a different jurisdiction |

Adjustments are documented in the vendor record. The business owner may challenge an adjustment through the exception process per [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) Section 8.

---

## 4. Evidence by Tier

Evidence requirements grow with tier. The table below names the cyber evidence required at minimum for each tier.

### 4.1 Evidence Table

| **Evidence** | **Tier 3 (Standard)** | **Tier 2 (Important)** | **Tier 1 (Critical)** |
|---|---|---|---|
| SOC 2 Type II report (or ISO 27001 certification), current | — | Required | Required |
| SOC 2 carve-outs and CUECs reviewed | — | — | Required |
| Penetration test summary (sanitized), within 12 months | — | Required | Required |
| Security questionnaire (SIG / CAIQ or CERG equivalent) | Optional | Required | Required |
| Sub-processor list | — | Required | Required |
| Right-to-audit clause in contract | — | Required | Required |
| Breach / incident notification commitment (timing, scope) | Required | Required | Required |
| Cyber liability insurance (industry-appropriate limits) | — | Required | Required |
| Business continuity / disaster recovery plan summary | — | — | Required |
| Data residency disclosure | — | Required | Required |
| Monthly SLA performance report | — | — | Required (MSSP/MSP) |
| Quarterly business review participation | — | — | Required |
| Self-attestation (CERG-provided form) | Required | — | — |

### 4.2 Evidence Currency

- **Tier 1** evidence is reviewed annually, no later than 30 days before attestation expiry.
- **Tier 2** evidence is reviewed annually.
- **Tier 3** evidence is reviewed on contract renewal or every 24 months, whichever is earlier.

Material vendor events (breach, ownership change, material service change, regulator action) trigger an out-of-cycle evidence review regardless of tier.

### 4.3 Evidence Quality

All evidence is assessed against [CERG-GOV-AUD-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md). The Evidence / SLA Manager validates that each artifact:
- Covers the correct scope (service, data, environment).
- Is current (within validity period).
- Is from a recognised assessor (for SOC 2/ISO 27001).
- Has no material exceptions that would reduce AnyTech's assurance.

Evidence that fails quality review is flagged to the Governance Pillar Leader, who escalates to the provider for remediation within 10 business days.

---

## 5. MSSP-Specific Oversight Process

The MSSP is AnyTech's most critical vendor. It provides 24×7 SOC monitoring, incident response, threat intelligence, and detection engineering. The oversight process below is specific to the MSSP relationship and operates in addition to the general evidence requirements in Section 4.

### 5.1 Monthly SLA Verification

The Evidence / SLA Manager verifies the following metrics monthly using MSSP-provided reports:

| **Metric** | **Target** | **Measurement Source** |
|---|---|---|
| Alert triage time — P1/P2 (critical/high severity) | ≤ 15 minutes | MSSP system logs |
| Alert triage time — P3/P4 (medium/low severity) | ≤ 60 minutes | MSSP system logs |
| Incident containment time — confirmed incidents | ≤ 2 hours from classification | MSSP incident timeline |
| SIEM uptime | ≥ 99.9% | MSSP platform status |
| Monthly report delivery | Within 5 business days of month end | Report receipt timestamp |
| Threat intelligence feed delivery | Daily, by 08:00 local | Feed receipt timestamp |

SLA miss consequences follow the escalation model in Section 10 of the [Operating Model (AnyTech Adaptation)](CERG-GOV-OM-001_Operating_Model_AnyTech.md) §10.2.

### 5.2 SIEM Health and Detection Coverage

The Engineering Pillar Leader reviews MSSP SIEM health metrics monthly:

- **Log source coverage** — percentage of configured log sources actively sending data.
- **Detection rule coverage** — mapping of AnyTech environment to MITRE ATT&CK; target ≥ 80% of applicable techniques covered.
- **Alert volume trends** — month-over-month comparison; investigation of significant changes.
- **False positive rate** — percentage of alerts closed as non-malicious; target ≤ 20%.

Detection gaps identified are documented as MSSP improvement actions and tracked through the quarterly business review.

### 5.3 Quarterly Joint Review

The Governance Pillar Leader chairs a quarterly review meeting with the MSSP service delivery manager. Participants include:

- Engineering Pillar Leader (technical validation)
- Risk Pillar Leader (exposure and threat landscape)
- Evidence / SLA Manager (SLA performance data)
- MSSP service delivery manager and technical lead(s)

**Agenda:**

1. **SLA performance** — metric-by-metric review for the quarter; miss patterns and corrective actions.
2. **Findings from MSSP monitoring** — significant alerts, incident trends, detection gaps identified.
3. **Threat landscape update** — MSSP presents relevant threat intelligence: campaigns, TTPs, CVEs affecting AnyTech's industry or technology stack.
4. **Detection coverage review** — Engineering-led review of detection rule performance and gaps.
5. **Improvement plan status** — open corrective actions from previous quarters.
6. **Forward look** — upcoming changes to MSSP service, technology roadmap, AnyTech environment changes.

The quarterly review produces a written summary with action items, owners, and target dates. Action items are tracked in the provider scorecard and reviewed at the next quarterly session.

### 5.4 Annual Review

Annually, in addition to the general Tier 1 evidence requirements:

1. **SOC 2 Type II review** — Governance reviewed against AnyTech's control baseline; carve-outs and user-control considerations (CUECs) reconciled.
2. **Tabletop exercise** — MSSP facilitates a scenario-based exercise involving CERG team members and invited business stakeholders. The exercise tests incident response coordination, communication paths, and decision-making under pressure.
3. **Contract compliance review** — Governance reviews MSSP contract compliance: data handling, sub-processor changes, insurance, notification obligations.
4. **Service scope validation** — Engineering confirms that the MSSP's service scope matches AnyTech's current environment (systems, log sources, detection requirements).

### 5.5 India Office Oversight

The MSSP operates a co-delivery model with a US office and an India office. The following additional requirements apply:

- **Data residency** — AnyTech data processed or accessible by the India office must be documented in a data-flow map. The contract must specify that AnyTech data does not leave approved processing regions without explicit consent.
- **BCP coverage** — The MSSP must demonstrate that the India office is covered under the MSSP's business continuity plan, with distinct RTO/RPO for services delivered from India. Annual BCP test results must include the India office scope.
- **Sub-processor disclosure** — Any sub-processors used by the India office (e.g., data center providers, connectivity providers) must be disclosed in the MSSP's sub-processor list.
- **Communication path** — The India office must have a documented escalation path to the AnyTech CERG team that bypasses overnight time-zone gaps. A primary and backup contact must be named.

---

## 6. MSP-Specific Oversight Process

The MSP is AnyTech's second most critical vendor. It manages IT operations: patching, identity and access management, endpoint management, asset inventory, and change management. The oversight process below is specific to the MSP relationship.

### 6.1 Patching SLA Tracking

The Engineering Pillar Leader reviews MSP patching performance against the following SLAs weekly:

| **Patch Severity** | **Deployment Target** | **Measurement** |
|---|---|---|
| Critical (CISA KEV, active exploitation) | ≤ 72 hours from vendor release | MSP patch log |
| High severity | ≤ 7 days from vendor release | MSP patch log |
| Standard severity | ≤ 30 days from vendor release | MSP patch log |
| Endpoint agent health (EDR, AV, MDM) | ≥ 98% active | MSP endpoint platform |

The Engineering Pillar leader reviews monthly patching summaries and flags any patterns of SLA misses to the Governance Pillar Leader for escalation.

### 6.2 Access Management Evidence Delivery

The MSP manages identity lifecycle (joiner/mover/leaver) and conducts access reviews. The Evidence / SLA Manager collects the following evidence on a standing cadence:

| **Evidence** | **Cadence** | **Content Requirements** |
|---|---|---|
| Joiner/Mover/Leaver processing report | Monthly | Count of requests, processing time (target ≤ 24 hours), exceptions |
| Access review completion evidence | Quarterly | Review scope, participants, completion date, findings and remediation |
| Privileged access group membership | Monthly | Members of admin/privileged groups; validation that no stale or unauthorised accounts exist |
| Service account inventory | Quarterly | List of all service accounts with owners, expiration, and last-use dates |
| MFA enrollment status | Monthly | Percentage of active users with MFA enrolled; target ≥ 99% |

Access review evidence that shows unresolved findings (e.g., stale accounts not removed, access not recertified) is flagged to the Governance Pillar Leader for escalation to the MSP service delivery manager.

### 6.3 Change Management — Security-Impact Review

The MSP is required to notify the **Engineering Pillar Leader** before implementing any material change with potential security impact. The following change types require advance notification and CERG review:

- Changes to firewall rules, network segmentation, or VPN configurations.
- Changes to identity provider configuration (SSO, MFA policies, federation).
- Changes to endpoint management policies (EDR, AV, MDM baselines).
- Changes to cloud infrastructure (IaaS/PaaS) affecting security groups, IAM roles, or encryption configuration.
- Changes to backup infrastructure or disaster recovery configuration.
- Deployment of new software or significant version upgrades to existing software.
- Changes to monitoring or logging configuration.

**Notification requirement:** Minimum 5 business days' advance notice for standard changes. Emergency changes (e.g., critical patch deployment) may proceed with notification within 24 hours after implementation.

The Engineering Pillar Leader reviews the change, assesses security impact, and either approves, conditionally approves, or rejects the change. Rejected changes are escalated to the IT Director.

### 6.4 Asset Inventory Accuracy

The MSP maintains the AnyTech asset inventory. The Evidence / SLA Manager reviews inventory accuracy monthly:

| **Metric** | **Target** | **Method** |
|---|---|---|
| Asset inventory completeness | ≥ 95% of expected assets | Compare inventory to authoritative sources (M365 admin center, EDR console, cloud provider inventory) |
| Asset classification completeness | ≥ 90% of assets classified | Assets tagged with owner, criticality, environment |
| Unmanaged device detection | 0 unmanaged devices with network access | Network access control / EDR visibility |

Inventory gaps above target thresholds are escalated to the Engineering Pillar Leader, who works with the MSP to remediate within 10 business days.

---

## 7. Contract Security Clause Library

CERG provides Procurement and Legal with a clause library for vendor contracts. Procurement owns negotiation; CERG provides the security requirements. Clauses below are minimums; alternative language with equivalent intent is acceptable.

| **Clause** | **Required For** | **Substantive Content** |
|---|---|---|
| **Incident notification** | All vendors with system or data access | Notification within 24 hours of confirmed incident affecting AnyTech data or services. Notification must include: incident description, data or systems affected, containment actions taken, and expected timeline for resolution. |
| **Right to audit** | Tier 1 and Tier 2 | Right to request evidence (SOC 2, ISO 27001, penetration test results) at any time with reasonable notice (10 business days). Right to conduct or commission an independent security assessment annually. |
| **Sub-processor notification** | All vendors processing AnyTech data | Vendor must maintain a current sub-processor list. Vendor must notify AnyTech at least 30 days before adding or changing a sub-processor. AnyTech reserves the right to object; if objection is not resolved, AnyTech may terminate without penalty. |
| **SLA commitments** | Tier 1 and Tier 2 | Defined service-level commitments for availability, response time, and incident handling. Service credits or contract remedies for SLA breaches. |
| **Termination for cause — security grounds** | All vendors | AnyTech may terminate the contract immediately if the vendor suffers a material security breach affecting AnyTech data or systems, fails to remediate a critical security finding within agreed timelines, or refuses to provide required evidence. |
| **Data handling and protection** | All vendors processing AnyTech data | Vendor shall process AnyTech data only for the purposes specified in the contract. Vendor shall implement appropriate technical and organisational measures to protect AnyTech data. Vendor shall return or destroy AnyTech data upon termination and provide certification. |
| **Data residency** | Tier 1 and Tier 2 | Vendor shall not store or process AnyTech data outside the approved regions without explicit written consent. Vendor shall disclose all locations where AnyTech data may be stored or processed. |
| **Insurance** | Tier 2+ | Vendor shall maintain cyber liability insurance with minimum coverage limits appropriate to the service scope. Vendor shall provide evidence of coverage on request and notify AnyTech of any material change in coverage. |
| **Background checks** | Tier 1 vendors (MSSP, MSP) | Vendor shall conduct background screening of all personnel with access to AnyTech systems or data. Vendor shall maintain named-individual access records. |
| **Cooperation** | All vendors with system or data access | Vendor shall cooperate fully in incident investigations, regulatory inquiries, and litigation related to AnyTech data or systems. Vendor shall preserve relevant evidence. |

---

## 8. Shared Responsibility Matrix for MSSP and MSP

The Shared Responsibility Matrix defines what AnyTech (CERG) owns versus what each provider owns for control areas. This is the single source of truth for cross-team conversations about "who handles X."

### 8.1 MSSP Shared Responsibility Matrix

| **Control Area** | **MSSP Owns** | **AnyTech (CERG / IT Director) Owns** |
|---|---|---|
| **SOC monitoring and alert triage** | 24×7 monitoring, alert classification, initial triage | Notification of environment changes; provision of asset criticality context |
| **Incident response** | Triage, containment, eradication, recovery support | Business-impact decisions, notification approval, risk acceptance |
| **Detection engineering** | SIEM rule creation, tuning, maintenance | Environment-specific detection requirements; validation of rule effectiveness |
| **Threat intelligence** | Feed production, delivery, relevance filtering | Consumption, actioning, escalation of relevant intel |
| **SIEM infrastructure** | Platform uptime, capacity, patching, backup | Log source configuration; data retention policy |
| **Log source integration** | Connector deployment, log parsing, health monitoring | Identification of log sources; access credentials for connectors |
| **Penetration testing** | Test execution, reporting, findings management | Scope definition; remediation acceptance |
| **Tabletop exercises** | Facilitation, scenario design | Participation, decision-making, improvement action tracking |
| **Monthly SLA reporting** | Report production | Report review, feedback, action tracking |

### 8.2 MSP Shared Responsibility Matrix

| **Control Area** | **MSP Owns** | **AnyTech (CERG / IT Director) Owns** |
|---|---|---|
| **Patch management** | Vulnerability assessment, patch deployment, compliance reporting | Patching policy, severity thresholds, exception approval |
| **Identity and access management** | Joiner/mover/leaver execution, access reviews, privileged access management | IAM policy, access approval authority, role definitions |
| **Endpoint management** | Configuration management, EDR/AV agent deployment and health, compliance scanning | Endpoint security baselines, policy exceptions |
| **Asset inventory** | Asset discovery, inventory maintenance, classification tagging | Asset classification schema, criticality designations |
| **Change management** | Change execution, documentation, notification | Security impact review, approval/rejection authority |
| **Network security** | Firewall management, network segmentation, VPN administration | Network security policy, segmentation requirements |
| **Backup and recovery** | Backup execution, restoration testing, BCP technical execution | RTO/RPO requirements, BCP planning, test scope |
| **Cloud infrastructure** | IaaS/PaaS configuration, security group management, cloud resource administration | Cloud security baseline, IAM role structure, encryption policy |
| **Monthly SLA reporting** | Report production | Report review, feedback, action tracking |

---

## 9. Continuous Monitoring and Re-Assessment

### 9.1 Provider SLA Performance Tracking

The Evidence / SLA Manager maintains a standing SLA tracker for all Tier 1 and Tier 2 providers. The tracker is updated monthly from provider reports and reviewed by the Governance Pillar Leader before the monthly CERG Risk and Posture Forum (CRPF).

The following metrics are tracked:

| **Metric** | **Source** | **Cadence** |
|---|---|---|
| % of SLAs met (by provider, by metric) | Provider monthly reports | Monthly |
| Open corrective action items | Provider scorecard | Quarterly |
| Evidence currency | Evidence library | Monthly |
| Incident response time (MSSP) | MSSP incident reports | Per incident |
| Patch compliance (MSP) | MSP patch reports | Weekly review, monthly report |

### 9.2 MSSP Threat Intelligence Consumption

The Risk Pillar Leader receives the MSSP's threat intelligence feed and assesses its relevance to AnyTech's environment weekly. Urgent intel (active threats targeting AnyTech's industry or technology stack) is escalated to the Engineering Pillar Leader and IT Director within 24 hours.

Threat intelligence is used to:
- Validate that MSSP detection rules cover emerging threats.
- Inform risk register entries about threat actor activity.
- Drive tabletop exercise scenarios.
- Provide context for the quarterly business review threat landscape update.

### 9.3 Annual Re-Assessment

Every vendor is re-assessed on the following cadence:

| **Tier** | **Re-Assessment Cadence** | **Trigger Events (override cadence)** |
|---|---|---|
| Tier 1 (Critical) | Annual | Vendor breach, material change in service, M&A activity, key person departure, regulatory action |
| Tier 2 (Important) | Annual | Vendor breach, material change in service |
| Tier 3 (Standard) | 24 months or contract renewal | Vendor breach affecting the service consumed |

The re-assessment consists of:
1. **Evidence review** — all required evidence per Section 4 is collected and reviewed for currency, scope, and quality.
2. **Risk assessment** — Risk Pillar Leader updates the vendor risk record in the risk register.
3. **Provider scorecard update** — Governance updates the provider scorecard with SLA performance, corrective action status, and any new findings.
4. **Recommendation** — the Governance Pillar Leader recommends retain / conditionally retain / initiate transition, approved per Section 10.

### 9.4 Escalation Paths for Deteriorating Vendor Posture

| **Condition** | **Escalation** | **Action** |
|---|---|---|
| SLA miss pattern (same metric missed 3+ times in 90 days) | Governance Pillar Leader → Provider SDM | Written notice; provider submits corrective action plan within 10 business days |
| Vendor breach with potential AnyTech impact | IT Director (via Governance Pillar Leader) | Immediate review; assess containment, exposure, and notification obligations |
| Critical finding open > 90 days without remediation plan | Governance Pillar Leader → Engineering Pillar Leader → IT Director | Escalate to provider executive; consider contract remedies |
| Vendor refuses to provide required evidence | Governance Pillar Leader → IT Director | Risk acceptance required; if unacceptable, initiate vendor transition planning |
| Vendor financial distress indicators | Governance Pillar Leader → IT Director | Develop contingency plan; identify alternative providers |

### 9.5 Vendor Offboarding

When a vendor relationship ends, the Governance Pillar Leader coordinates offboarding with Procurement and the MSP:

| **Step** | **Action** | **Owner** | **Timing** |
|---|---|---|---|
| 1 | Notify vendor; confirm effective date | Procurement | Immediately |
| 2 | Disable all vendor user accounts | MSP | Effective date or within 24 hours |
| 3 | Revoke vendor API keys, OAuth grants, service principals | MSP | Effective date |
| 4 | Rotate shared secrets vendor had access to | MSP | Within 5 business days |
| 5 | De-authorise SSO / federation | MSP | Effective date |
| 6 | Remove vendor from Approved Provider Catalog | Governance Pillar Leader | Within 5 business days |
| 7 | Confirm data retrieval or destruction per contract | Procurement + Governance | Per contract |
| 8 | Final risk register update | Risk Pillar Leader | Within 10 business days |

### 9.6 Approved Provider and SaaS Catalog

CERG maintains an **Approved Provider and SaaS Catalog** as the system-of-record for which third-party services may be used. The catalog is managed by the Governance Pillar Leader and contains:

| **Field** | **Definition** |
|---|---|
| Provider Name / Service | — |
| Vendor Tier | Per Section 3 |
| Approved Scopes | Public / Internal / Restricted |
| Data Residency Constraints | Approved regions |
| Last Evidence Review | Date and reviewer |
| Next Required Review | — |
| Outstanding Risks | Risk register IDs |
| Status | Approved · Approved-with-Conditions · Conditional Use Only · Sunset · Prohibited |

Procurement consults the catalog at intake. CERG updates it at each evidence cycle and after each material vendor event.

---

## 10. Approval Authority

Vendor acceptance decisions require documented approval at the following levels:

| **Decision** | **Tier** | **Authority** |
|---|---|---|
| Vendor acceptance — initial onboarding | Tier 1 (Critical) | **IT Director** |
| Vendor acceptance — initial onboarding | Tier 2 (Important) | **Engineering Pillar Leader** |
| Vendor acceptance — initial onboarding | Tier 3 (Standard) | **Engineering Pillar Leader** |
| Contract security scope change (material) | Tier 1 | **IT Director** |
| Contract security scope change (material) | Tier 2/3 | **Engineering Pillar Leader** |
| Risk acceptance — vendor-related residual risk: Critical or High | All tiers | **IT Director** |
| Risk acceptance — vendor-related residual risk: Medium or Low | All tiers | **Risk Pillar Leader** |
| Exception to evidence requirement | All tiers | **Governance Pillar Leader** |
| Vendor transition initiation (due to security posture) | Tier 1 | **IT Director** |
| Vendor transition initiation (due to security posture) | Tier 2/3 | **Engineering Pillar Leader** |

The IT Director is the final risk acceptance authority for all severities above Medium and may not delegate Tier 1 vendor acceptance decisions. The Engineering Pillar Leader may delegate Tier 2/3 acceptance to a Security Engineer in writing for a defined period.

---

## 11. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-TPRM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (AnyTech CERG) |
| **Approved By** | IT Director (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On new critical vendor onboarding |
| **Next Scheduled Review** | 2027-06-21 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-21 | Governance Pillar Leader (AnyTech CERG) | Initial AnyTech Adaptation. Stripped to 3-tier vendor model; removed SBOM, CIP-013, CMMC, FedRAMP, CUI, SCCT, SOX, and international access sections. Added MSSP-specific oversight process (§5) with monthly SLA verification, quarterly joint review, annual review, and India office oversight. Added MSP-specific oversight process (§6) with patching SLA tracking, access management evidence delivery, change management review, and asset inventory validation. Simplified evidence requirements (§4) and contract clause library (§7). Adapted approval authority (§10) for IT Director + Engineering Pillar Leader. |

### Review Triggers

This procedure shall be reviewed annually and upon any of the following:

- New critical (Tier 1) vendor onboarding.
- Material change to the MSSP, MSP, or training vendor relationship (scope change, contract renegotiation, provider change).
- Significant security incident involving any vendor that reveals gaps in this procedure.
- Addition of a regulatory regime to AnyTech scope.
- IT Director transition.
- Change in CERG team structure or size that affects TPRM capacity.
- Direction from AnyTech executive leadership.

The Governance Pillar Leader owns this document. Changes require IT Director approval.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Parent policy — foundational security principles |
| Operating Model (AnyTech Adaptation) | [CERG-GOV-OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Defines the provider engagement model, SLA framework, RACI patterns, and pillar structure |
| Risk Register and Exception Process | [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk register operation; vendor-related risks are intaken here |
| Architecture Review and Project Intake Procedure | [CERG-PRC-AR-001](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Pre-production engagement; adapted for provider-proposed changes |
| Audit and Evidence Management Procedure | [CERG-PRC-AUD-001](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence collection procedure; applies to provider evidence |
| Exposure Management Procedure | [CERG-PRC-VM-001](../../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Vulnerability management; data sourced from MSSP/MSP |
| Threat Intelligence Procedure | [CERG-PRC-TI-001](../../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Intel consumption process; feed sourced from MSSP |
| Document Catalog and Naming Convention | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Authoritative inventory of every CERG artifact |
| Unified Control Baseline | CERG-GOV-CB-001) | Control spine for mapping provider-delivered controls |

---

*End of Document — CERG-PRC-TPRM-001 (AnyTech Adaptation)*
