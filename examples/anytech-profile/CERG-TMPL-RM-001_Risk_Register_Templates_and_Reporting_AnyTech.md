## RISK REGISTER TEMPLATES AND REPORTING — AnyTech Adaptation

| | |
|---|---|
| **Document ID** | CERG-TMPL-RM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Internal |
| **Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On risk register format change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## 1. Purpose and Scope

This document provides the standard templates and schemas for AnyTech's risk register, exception register, and risk reporting. These templates operationalize [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md). They are designed for spreadsheet or simple database use — no GRC platform required.

### 1.1 When to Use These Templates

- Creating a new risk register entry
- Requesting a control exception
- Producing the monthly risk report for the IT Director
- Tracking provider-assigned risk treatment

---

## 2. Risk Register Template

### 2.1 Columns

| Column | Example | Notes |
|--------|---------|-------|
| Risk ID | RISK-2026-001 | Format: RISK-YYYY-NNN |
| Risk Statement | Single MSSP SOC/IR creates vendor concentration risk — MSSP outage or contract dispute could leave AnyTech without detection and response capability | Threat actor, action, asset, effect, impact |
| Source | MSSP / MSP / CERG / External / Provider Assessment | Where the risk was identified |
| Inherent Likelihood | 4 | 1-5 scale per RMF-001 |
| Inherent Impact | 4 | 1-5 scale per RMF-001 |
| Inherent Score | 16 | Likelihood × Impact |
| Inherent Severity | High | Per RMF-001 severity bands |
| Treatment Strategy | Mitigate / Transfer / Accept / Avoid | |
| Treatment Actions | [Specific, actionable steps with owners] | Include provider-assigned actions |
| Treatment Owner | Risk Pillar Leader / MSSP / MSP | |
| Treatment Due | 2026-09-30 | |
| Residual Likelihood | 2 | Post-treatment |
| Residual Impact | 3 | Post-treatment |
| Residual Score | 6 | |
| Residual Severity | Medium | |
| Approval Authority | IT Director | Per PRC-RM-001 §8 |
| Business Owner | [Name of business stakeholder] | Must be outside CERG |
| Risk Owner (CERG) | Risk Pillar Leader | CERG point of contact |
| Date Identified | 2026-06-21 | |
| Status | New / In Treatment / Accepted / Closed | |
| Last Reviewed | 2026-07-01 | |
| Next Review | 2026-08-01 | |

### 2.2 Risk Statement Format

Risk statements should follow a consistent format:

**[Threat actor] could [action] against [asset] resulting in [effect] leading to [impact].**

Example:
*"A sophisticated external threat actor could exploit an unpatched internet-facing system managed by MSP, resulting in data exfiltration and reputational damage."*

### 2.3 Scoring Reference

| Likelihood | Description |
|------------|-------------|
| 1 — Rare | Less than once per 5 years |
| 2 — Unlikely | Once per 2-5 years |
| 3 — Possible | Once per 1-2 years |
| 4 — Likely | Once per 6-12 months |
| 5 — Almost Certain | Monthly or more |

| Impact | Description |
|--------|-------------|
| 1 — Negligible | No measurable effect |
| 2 — Minor | Minor operational disruption |
| 3 — Moderate | Significant but contained disruption |
| 4 — Major | Serious business impact |
| 5 — Catastrophic | Business survival threatened |

---

## 3. Exception Register Template

### 3.1 Columns

| Column | Example | Notes |
|--------|---------|-------|
| Exception ID | EXC-2026-001 | Format: EXC-YYYY-NNN |
| Control ID | AC-2 | Policy or control reference |
| Requirement | Quarterly access review for all privileged accounts | What is not being met |
| Affected Assets | AnyTech cloud environment (MSP-managed) | |
| Business Justification | Access review tooling integration with MSP not yet deployed | Why exception is needed |
| Compensating Controls | Monthly manual review of top 10 privileged accounts | What replaces the standard control |
| Compensating Control Owner | Engineering Pillar Leader | Who maintains the compensating control |
| Residual Risk Score | 6 | |
| Residual Severity | Medium | |
| Business Owner | [Name] | Must be outside CERG |
| Approver | IT Director / Pillar Leader | Per PRC-RM-001 §8 |
| Approval Date | 2026-06-21 | |
| Expiration Date | 2027-03-21 | Maximum 12 months |
| Next Review | 2026-09-21 | Default mid-point review |
| Status | Active / Expired / Closed | |

### 3.2 Exception Duration Rules

- Maximum exception duration: 12 months
- Exceptions requiring IT Director approval: maximum 6 months, then require full re-review
- Exceptions to a provider SLA: duration must match the provider contract cycle
- No automatic renewal. Every exception must be explicitly reviewed and re-approved.

---

## 4. Monthly Risk Report Template (for IT Director)

### 4.1 Report Format

The Risk Pillar Leader produces a 1-page monthly risk report for the IT Director.

```
ANYTECH CERG — MONTHLY RISK REPORT
Month: [Month Year]
Prepared by: [Risk Pillar Leader]

SUMMARY
- Total open risks: N
- New this month: N
- Accepted/closed this month: N
- High/Critical open: N

TOP 5 RISKS (by residual score)
1. RISK-2026-NNN — [Risk statement] — Score N — [Status]
2. RISK-2026-NNN — [Risk statement] — Score N — [Status]
...

EXCEPTION WATCH
- Expiring this month: N
- Expiring next month: N
- Past due: N

PROVIDER RISK HIGHLIGHTS
- MSSP: [notable findings from monthly report]
- MSP: [patching compliance %, notable events]
- Other: [SaaS vendor assessments, etc.]

ESCALATIONS / DECISIONS NEEDED
- [Item needing IT Director decision]
- [Item needing IT Director notification]

NEXT REVIEW: [Date]
```

---

## 5. Provider-Assigned Treatment Tracker

The Risk Pillar Leader maintains a separate sheet tracking treatment actions assigned to providers.

| Action ID | Source Risk | Provider | Action | SLA/Target Date | Status | Last Verified |
|-----------|-------------|----------|--------|-----------------|--------|--------------|
| TRT-2026-001 | RISK-2026-005 | MSP | Implement quarterly privileged access review | 2026-09-30 | In Progress | 2026-07-01 |

---

## 6. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | Risk Pillar Leader | AnyTech adaptation. Simplified templates, provider treatment tracker, IT Director reporting format. |

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Risk Register and Exception Process | [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) | Operating procedure |
| Risk Management Framework | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) | Scoring and acceptance model |