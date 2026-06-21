## RISK REGISTER AND EXCEPTION PROCESS — AnyTech Adaptation

### Identification · Treatment · Acceptance · Review

| | |
|---|---|
| **Document ID** | CERG-PRC-RM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Internal |
| **Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On significant change |
| **Frameworks** | NIST CSF 2.0 (GOVERN); NIST 800-53r5; NIST RMF |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Responsibilities](#2-roles-and-responsibilities)
3. [Risk Identification](#3-risk-identification)
4. [Risk Assessment and Scoring](#4-risk-assessment-and-scoring)
5. [Risk Treatment](#5-risk-treatment)
6. [The Risk Register](#6-the-risk-register)
7. [Exception Process](#7-exception-process)
8. [Approval Authority — AnyTech](#8-approval-authority--anytech)
9. [Review, Escalation, and Reporting](#9-review-escalation-and-reporting)
10. [Integration With Provider Risk Management](#10-integration-with-provider-risk-management)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

This procedure operationalizes Risk Management Framework Principle 6 of [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md). It defines how AnyTech identifies, documents, scores, treats, reviews, and reports cybersecurity risks, and how exceptions to established controls are requested, approved, tracked, and reviewed.

The risk register is the single, authoritative record of cybersecurity risk at AnyTech. The exception process is the single, authoritative record of intentional deviations from established controls.

### 1.1 Scope

This procedure applies to:
- All cybersecurity risks affecting AnyTech assets, data, or operations — regardless of whether the asset is managed by CERG directly or by a provider
- All deviations from controls established in [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) and its subordinate documents
- All risk-related decisions requiring documentation: acceptance, transfer, avoidance, and reduction
- All CERG team members, anyTech personnel, and providers operating within AnyTech scope

### 1.2 The Operating Premise

> **Undocumented Risk Is Accepted Risk Without an Owner**

Every organization has more risk than it has time to remediate. The question is not whether risk exists, it is whether the organization has a documented, owned, and reviewed posture toward each one. An undocumented risk that materializes into an incident leaves no audit trail.

At AnyTech, this is especially important because the team does not operate security controls directly. The risk register captures what is known, what is being treated, and what the IT Director has accepted.

---

## 2. Roles and Responsibilities

| Role | Risk Responsibility |
|------|-------------------|
| **IT Director** | Approves High and Critical risk acceptances. Calibrates risk appetite annually. Final escalation for unresolved risks. |
| **Risk Pillar Leader** | Owns the risk register. Leads risk scoring. Presents risks to IT Director. Manages exception process. |
| **Engineering Pillar Leader** | Identifies technical risks from MSP changes, architecture reviews, and vulnerability data. Confirms technical treatment feasibility. |
| **Governance Pillar Leader** | Ensures risk decisions are documented. Tracks exception expirations. Maintains evidence library for accepted risks. |
| **MSSP** | Provides threat intelligence for risk identification. Reports incidents that may indicate risk materialization. |
| **MSP** | Reports vulnerability findings, access control gaps, and configuration deviations that feed risk identification. |
| **AnyTech Personnel** | Report security concerns or observed risks to CERG via security@anytech.com. |

---

## 3. Risk Identification

Risks are identified from multiple sources at AnyTech:

### 3.1 Provider-Originated Risks

- **MSSP threat intel:** New threat actor TTPs, industry-specific campaigns, zero-day vulnerabilities affecting AnyTech stack
- **MSSP incident findings:** Post-incident analysis identifying root causes and systemic gaps
- **MSP vulnerability data:** Scanner findings that cannot be remediated within SLA
- **MSP change management:** Proposed changes that introduce new risk vectors
- **Provider audit reports:** SOC 2 findings, penetration test failures

### 3.2 CERG-Originated Risks

- Architecture reviews of new MSP services or SaaS onboarding
- Vendor risk assessments under [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md)
- Employee-reported concerns
- Lessons learned from near-misses
- Recurring SLA misses by any provider

### 3.3 External Sources

- CISA known exploited vulnerabilities (KEV) catalog
- Industry threat feeds relevant to AnyTech's sector
- Regulatory developments

---

## 4. Risk Assessment and Scoring

### 4.1 Scoring Model

AnyTech uses a 5×5 likelihood × impact matrix per [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md).

| Score | Band | Authority |
|-------|------|-----------|
| 20-25 | **Critical** | IT Director + board/CEO documentation |
| 12-16 | **High** | IT Director |
| 5-9 | **Medium** | Pillar Leader + IT Director notification |
| 1-4 | **Low** | Engineering or Risk Pillar Leader |

### 4.2 Inherent vs. Residual

Each risk is scored at inherent level (before treatment) and residual level (after treatment controls are applied). The residual score determines the acceptance authority required.

---

## 5. Risk Treatment

### 5.1 Treatment Strategies

| Strategy | Description | AnyTech Example |
|----------|-------------|----------------|
| **Avoid** | Eliminate the risk by removing the activity | Decommission a system no longer needed |
| **Mitigate** | Reduce likelihood or impact via controls | Ask MSP to implement additional compensating controls |
| **Transfer** | Shift risk to a third party via contract/SLA | MSSP contractual liability for incident response failures |
| **Accept** | Acknowledge and document residual risk | Documented acceptance by IT Director with recurring review date |

### 5.2 Provider-Assigned Treatment

AnyTech may assign treatment actions to providers via:
- Contract SLA obligations
- Provider improvement plans
- Quarterly priority actions from QBR

The Risk Pillar Leader tracks provider-assigned treatment just like internal treatment — with an owner and a due date.

---

## 6. The Risk Register

The risk register is AnyTech's single authoritative record. It is maintained by the Risk Pillar Leader.

### 6.1 Minimum Required Fields

| Field | Description |
|-------|-------------|
| Risk ID | RISK-YYYY-NNN |
| Risk Statement | Threat actor + action + asset + effect + impact |
| Source | MSSP / MSP / CERG / External |
| Inherent Score | Likelihood × Impact (1-5 each) |
| Inherent Severity | Critical / High / Medium / Low |
| Treatment Strategy | Avoid / Mitigate / Transfer / Accept |
| Treatment Actions | Specific actions with owner and due date |
| Treatment Owner | CERG role or provider name |
| Residual Score | Post-treatment likelihood × impact |
| Residual Severity | Critical / High / Medium / Low |
| Approval Authority | Risk Pillar Leader / IT Director / Board |
| Status | New / In Treatment / Accepted / Closed |
| Last Reviewed | Date of most recent review |
| Next Review | Date next review is due |

### 6.2 Register Format

The register is maintained as a spreadsheet or GRC platform until AnyTech outgrows the manual approach. See [TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting_AnyTech.md) for the standard template.

---

## 7. Exception Process

### 7.1 When an Exception Is Needed

An exception is required when:
- A control cannot be implemented within its required timeframe
- A provider cannot meet a contractual security requirement
- A compensating control deviates from the standard requirement

### 7.2 Exception Lifecycle

1. **Request:** Pillar Leader documents the exception using the exception template
2. **Review:** Risk Pillar Leader scores residual risk
3. **Approve:** Appropriate authority per §8 approves or rejects
4. **Track:** Exception is entered in the exception register
5. **Monitor:** Governance tracks expiration dates
6. **Renew or Close:** Before expiration, the exception is reviewed. Renew or close.

### 7.3 Exception Register Fields

| Field | Description |
|-------|-------------|
| Exception ID | EXC-YYYY-NNN |
| Control ID | From control being excepted |
| Requirement | What is not being met |
| Affected Assets | Systems or processes |
| Business Justification | Why exception is needed |
| Compensating Controls | What is in place instead |
| Residual Risk Score | Post-compensation |
| Approver | As per §8 |
| Approval Date | Date of approval |
| Expiration Date | Maximum 12 months |
| Status | Active / Expired / Closed |

---

## 8. Approval Authority — AnyTech

| Decision Type | Low | Medium | High | Critical |
|---------------|-----|--------|------|----------|
| Risk acceptance | Pillar Leader | Pillar Leader + notify IT Director | IT Director | IT Director + board/CEO |
| Exception approval | Pillar Leader | Pillar Leader + notify IT Director | IT Director | IT Director |
| Risk register entry | Pillar Leader | Pillar Leader | Pillar Leader | Pillar Leader |
| Treatment plan | Pillar Leader | Pillar Leader | Pillar Leader + IT Director | IT Director |

The IT Director is the ultimate risk acceptance authority. The IT Director may delegate Medium and Low authority to the pillar leaders. Critical risk acceptance must be documented with the board or CEO.

---

## 9. Review, Escalation, and Reporting

### 9.1 Monthly Risk Review

The Risk Pillar Leader presents to the IT Director:
- New risks identified this period
- Risk register status — open, in treatment, accepted, closed
- Exception expirations in the next 60 days
- Provider SLA misses with risk implications
- Top 5 risks by residual score

### 9.2 Escalation Path

If a risk reaches the following thresholds, the IT Director is notified immediately:
- Any Critical risk (score 20-25) identified
- Any actual or imminent SLA breach on a Tier 1 provider (MSSP or MSP)
- Any risk materializing into an active incident

### 9.3 Annual Risk Appetite Calibration

The IT Director reviews and recalibrates risk appetite annually. This drives adjustments to scoring thresholds and acceptance authorities.

---

## 10. Integration With Provider Risk Management

### 10.1 MSSP Risk Data

The MSSP provides a monthly risk summary including:
- New findings from monitoring
- Threat intelligence relevant to AnyTech
- Alert volume trends
- Incident summary if applicable

This data feeds directly into AnyTech's risk identification process.

### 10.2 MSP Risk Data

The MSP provides:
- Patch compliance report (monthly)
- Vulnerability scan summary (monthly)
- Access review completion status (quarterly)
- Change log summary (monthly)

### 10.3 Provider Risk Register Entries

Providers themselves may be entries in AnyTech's risk register. For example:
- RISK-2026-001: "Vendor concentration risk — single MSSP for all SOC/IR"
- RISK-2026-002: "MSP patch SLA compliance below 90% for critical systems"

---

## 11. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | Risk Pillar Leader | AnyTech adaptation. IT Director authority, provider-sourced risk identification, simplified scoring. |

### Review Triggers

- Provider change (new MSSP, new MSP)
- Material security incident
- Risk appetite recalibration
- Annual review cycle
- Direction from IT Director

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Cybersecurity Policy | [POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Risk Management Framework | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) | Risk scoring and acceptance model |
| Third-Party Risk Procedure | [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) | Provider risk inputs |
| Exposure Management Procedure | [PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure_AnyTech.md) | Vulnerability-to-risk linkage |
| Risk Register Templates | [TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting_AnyTech.md) | Register and exception templates |