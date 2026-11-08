## CERG Risk Management Framework — AnyTech Adaptation

> This framework defines how AnyTech identifies, scores, treats, and monitors cybersecurity risk. It
> does not assume enterprise-scale tooling or dedicated threat intelligence platforms — risk data
> comes primarily from provider inputs (MSSP, MSP) and CERG manual observations. The IT Director
> holds executive risk acceptance authority; there is no CISO.

| | |
|---|---|
| **Document ID** | CERG-GOV-RMF-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy |
| **Review Cycle** | Annual / On material change |
| **Frameworks** | NIST CSF 2.0; NIST SP 800-37 (RMF) |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Framework Architecture](#2-framework-architecture)
3. [Risk Sources](#3-risk-sources)
4. [Risk Scoring](#4-risk-scoring)
5. [Risk Treatment](#5-risk-treatment)
6. [Risk Acceptance Authority for AnyTech](#6-risk-acceptance-authority-for-anytech)
7. [Continuous Monitoring](#7-continuous-monitoring)
8. [Integration with Third-Party Risk](#8-integration-with-third-party-risk)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

### 1.1 Purpose

The CERG Risk Management Framework (CERG-RMF) defines how AnyTech's 8-person cyber program office identifies, scores, treats, and monitors cybersecurity risk. It is the operational backbone that gives every risk decision a shared vocabulary, a repeatable process, and a clear owner.

This framework is purpose-built for AnyTech's operating reality:

- **Provider-delivered security operations.** AnyTech does not operate its own SIEM, EDR, or threat intelligence platform. The MSSP delivers continuous monitoring, incident detection and response, and threat intelligence feeds. The MSP delivers IT operations, vulnerability scanning, access management, and change execution.
- **No CISO.** The IT Director serves as the executive risk acceptance authority. Risk decisions are documented and escalated to the board or CEO only at the Critical severity level.
- **No regulatory frameworks currently in scope.** This framework is designed to scale when regulations (e.g., CMMC, NIST 800-171, state privacy laws) are added — but today, it operates on voluntary best-practice risk management.
- **Small-team operation.** CERG's three pillars (Engineering, Risk, Governance) are staffed by 8 people. Processes are designed to be lightweight, manual where automation is absent, and dependent on provider data rather than internal tooling.

### 1.2 Scope

This framework applies to:

- All AnyTech-owned or managed information systems, data, and networks
- All provider-managed environments that process, store, or transmit AnyTech data
- All third-party services with access to AnyTech environments
- All personnel — AnyTech employees and provider staff operating within AnyTech scope

This framework does not prescribe technology-specific configurations, tool choices, or operational runbooks. Those are established in provider contracts, SLAs, and the AnyTech CERG Operating Model ([OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md)).

### 1.3 Design Intent

Risk management at AnyTech is not a quarterly checkbox exercise. It is a continuous, adaptive cycle that uses provider-sourced data to produce a risk posture the IT Director can defend to the CEO, the board, and — when they are added — regulators and auditors. Because AnyTech does not operate its own security tools, the quality of the risk program depends on the quality of provider data and the rigor of CERG's review process.

---

## 2. Framework Architecture

### 2.1 The CERG-RMF Cycle

The CERG Risk Management Framework follows the six-phase NIST RMF cycle (Categorize, Select, Implement, Assess, Authorize, Monitor). At AnyTech, the cycle is adapted to account for provider-delivered execution:

| Phase | NIST RMF Step | AnyTech Primary Owner | Supporting Role |
|---|---|---|---|
| 1. Categorize | Step 1 – Categorize | Governance | Risk, MSP (asset data) |
| 2. Select | Step 2 – Select | Governance | Engineering, Risk |
| 3. Implement | Step 3 – Implement | **Providers (MSP/MSSP)** | Engineering (validates) |
| 4. Assess | Step 4 – Assess | Risk | MSSP (scanning/pen testing), Governance |
| 5. Authorize | Step 5 – Authorize | Governance | IT Director (acceptance authority), Risk |
| 6. Monitor | Step 6 – Monitor | Risk + Governance | MSSP (SIEM/threat intel), MSP (vuln scans) |

**Key difference from a full CISO-led RMF:** At AnyTech, the "Implement" phase is largely provider-delivered. CERG selects controls and monitors compliance; providers execute. The "Assess" phase is a shared responsibility — the MSSP runs technical assessments; CERG Risk validates findings and interprets business impact.

### 2.2 NIST CSF 2.0 Function Mapping

| CSF Function | CERG-RMF Phase(s) | What AnyTech Does |
|---|---|---|
| **GOVERN** | Categorize, Authorize | Sets risk strategy and acceptance authority. IT Director owns risk posture; CERG operates the program. |
| **IDENTIFY** | Categorize, Assess | Maintains asset inventory and system categorization. Uses provider data for risk assessments. |
| **PROTECT** | Select, Implement | CERG selects controls from baselines; providers implement per contract and SLA. |
| **DETECT** | Monitor, Assess | MSSP operates SIEM and detection content. Risk reviews alerts and threat intel from MSSP feed. |
| **RESPOND** | Monitor (IR hand-off) | MSSP leads incident response per IR retainer. CERG coordinates internal notification and reporting. |
| **RECOVER** | Monitor (lessons learned) | CERG captures lessons learned from incidents and drives improvement with providers. |

### 2.3 AnyTech-Specific Adaptations

Because AnyTech relies on providers for execution, several standard RMF activities are adapted:

| Standard Activity | AnyTech Approach |
|---|---|
| System categorization | Governance leads with input from MSP (asset inventory). No FIPS 199 or NERC-CIP designations needed currently. Uses simple CIA ratings based on business impact. |
| Control implementation | Providers implement controls per contract scope. Engineering validates that implementation meets CERG-selected baseline. |
| Vulnerability scanning | MSP runs authenticated scans monthly; MSSP provides external attack-surface scanning. Risk reviews and validates findings. |
| Penetration testing | MSSP delivers annual external and internal penetration tests per contract. Risk reviews the report and tracks findings. |
| Threat intelligence | MSSP provides a curated threat intel feed (tactical and operational). CERG Risk reviews weekly for relevance to AnyTech. |
| Risk register | Maintained by Governance in a shared document (not a dedicated GRC tool). Provider-sourced findings are entered manually. |

---

## 3. Risk Sources

Risk at AnyTech comes from four primary sources. Each source produces specific data types that feed into the risk register.

### 3.1 MSSP (Managed Security Service Provider)

The MSSP is AnyTech's primary source of security telemetry. Data from the MSSP includes:

| Data Type | Description | Cadence | Used For |
|---|---|---|---|
| Threat intelligence feed | Curated IOCs, TTPs, and sector-specific threat actor intelligence | Continuous; weekly summary | Risk scoring, treatment urgency |
| Incident reports | Post-incident analysis for any confirmed security event | Per incident (SLA-bound) | Risk register entry, control gap analysis |
| SIEM findings | Alerts from SIEM correlation rules — tuned and triaged by MSSP before delivery | Continuous; daily digest | Risk identification, KRI tracking |
| Penetration test results | Annual external and internal penetration testing report | Annual + ad hoc | Risk scoring, control effectiveness assessment |
| Vulnerability scan exports | External attack-surface scan results | Weekly | Finding register, risk prioritization |

### 3.2 MSP (Managed Service Provider)

The MSP delivers IT operations and provides operational risk data:

| Data Type | Description | Cadence | Used For |
|---|---|---|---|
| Vulnerability scan exports | Authenticated internal vulnerability scans | Monthly | Finding register, risk scoring |
| Access review outputs | User access rights and privilege audits | Quarterly | Access risk identification, SOD analysis |
| Change logs | Record of changes to systems, applications, and configurations | Weekly | Configuration drift detection, risk identification |
| Patch compliance reports | Status of patch deployment against defined SLAs | Monthly | Risk scoring (unpatched systems) |
| Asset inventory updates | Additions, removals, and changes to the managed asset base | Weekly | Categorization updates, scope maintenance |

### 3.3 CERG (Internal)

CERG generates risk data through manual observation and analysis:

| Data Type | Description | Cadence | Used For |
|---|---|---|---|
| Manual observations | Risks identified during regular work (email reviews, architecture discussions, contract reviews) | As identified | Risk register entry |
| SaaS vendor assessments | Lightweight security assessments of SaaS tools used by AnyTech employees | Onboarding + annual | Vendor risk scoring |
| Employee reports | Security concerns reported by AnyTech staff via the reporting channel | As reported | Risk identification |
| Policy exception reviews | Security exceptions requested and tracked by Governance | As requested | Risk register entry (where residual risk exists) |
| Risk register reviews | Periodic validation that existing register entries are still accurate and current | Monthly | Risk re-scoring, treatment re-evaluation |

### 3.4 External Sources

| Data Type | Description | Cadence | Used For |
|---|---|---|---|
| CISA advisories | Known Exploited Vulnerabilities (KEV) catalog, emergency directives | As published | Risk re-scoring, treatment urgency |
| Industry threat intel | Sector-specific threat briefings, ISAC feeds, peer sharing groups | As available | Risk identification, threat community reference |
| Vendor security notices | Security advisories from AnyTech's technology vendors and providers | As received | Risk identification, treatment prioritization |

### 3.5 Data Quality and Limitations

AnyTech acknowledges that risk data quality depends on provider inputs. CERG takes the following approach to data quality:

| Limitation | Mitigation |
|---|---|
| MSSP SIEM tuning may miss AnyTech-specific scenarios | Quarterly provider performance reviews include a SIEM rule coverage check |
| MSP vulnerability scans may not cover all assets independently deployed by teams | CERG performs a quarterly asset inventory reconciliation |
| Penetration testing is annual — gaps can emerge mid-cycle | MSSP provides continuous external attack-surface scanning as a bridge |
| No internal GRC or risk management platform | Risk register is maintained in a shared document; manual processes are documented in [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) |

---

## 4. Risk Scoring

### 4.1 The 5×5 Matrix

AnyTech uses a standard 5×5 Likelihood × Impact matrix. Each risk is scored on two dimensions (1–5), and the product produces a composite severity score.

### 4.2 Likelihood Bands

| Score | Label | Description |
|---|---|---|
| 5 | Very High | Almost certain — occurs multiple times per year |
| 4 | High | Likely — occurs approximately once per year |
| 3 | Medium | Possible — could occur within 1–3 years |
| 2 | Low | Unlikely — could occur within 3–10 years |
| 1 | Very Low | Rare — less than once per 10 years |

**Guidance for providers.** Likelihood is assessed based on MSSP threat intelligence, observed industry trends, AnyTech's own incident history, and the presence or absence of compensating controls. When providers supply likelihood estimates, CERG Risk validates and may adjust based on AnyTech-specific context.

### 4.3 Impact Bands

| Score | Label | Description |
|---|---|---|
| 5 | Critical | >$500K financial impact; extended operational outage (>1 week); material reputation damage; legal or regulatory action |
| 4 | High | $100K–$500K financial impact; significant operational disruption (days); reportable to leadership |
| 3 | Medium | $10K–$100K financial impact; limited operational disruption (hours); contained reputation impact |
| 2 | Low | $1K–$10K financial impact; minor operational impact (minutes); minimal visibility |
| 1 | Negligible | <$1K financial impact; no operational impact; no external visibility |

> **Note on calibration.** The dollar bands above are preliminary defaults for AnyTech's current size and risk appetite. The Risk Pillar Leader refreshes them annually with the IT Director and Finance, using revenue, insurance retention, downtime cost, and contractual exposure as the basis.

### 4.4 Composite Severity

Likelihood score × Impact score = Severity score. The product maps to a severity band:

| Severity Score | Severity Band |
|---|---|
| 20–25 | **Critical** |
| 12–16 | **High** |
| 5–9 | **Medium** |
| 1–4 | **Low** |

> **Note on score gaps.** The gap between 9 and 12 (Medium → High) and between 16 and 20 (High → Critical) is intentional. These buffer zones ensure that a risk must clearly cross into the next severity band — borderline scores are resolved toward the lower band unless additional factors (active exploitation, regulatory exposure, safety impact) justify upward adjustment.

### 4.5 Severity Band Actions

| Band | Required Action |
|---|---|
| **Critical** | Immediate IT Director notification. Risk must be actively treated — acceptance is exceptional and requires board/CEO documentation. Weekly review until closed or accepted. |
| **High** | IT Director notification within 5 business days. Treatment plan required within 30 days. Monthly review until closed or accepted. |
| **Medium** | Risk register entry with treatment plan. Quarterly review. IT Director notified of any Medium risk that remains open past 180 days. |
| **Low** | Tracked in the risk register. Annual review or on any material change. No formal acceptance required beyond documentation. |

### 4.6 Scoring Examples

| Scenario | Likelihood | Impact | Score | Severity |
|---|---|---|---|---|
| Ransomware encrypts file server — no backups tested recently | 3 (Medium) | 4 (High) | 12 | High |
| Phishing campaign targets finance team — no MFA on email | 4 (High) | 3 (Medium) | 12 | High |
| Unpatched CVE in Internet-facing web app (per MSSP scan) | 4 (High) | 4 (High) | 16 | High |
| Vendor data breach via compromised credentials (per vendor notification) | 2 (Low) | 5 (Critical) | 10 | Medium |
| Employee laptop lost — disk encryption verified via MSP | 2 (Low) | 2 (Low) | 4 | Low |
| Firewall rule drift allows RDP from Internet (per MSP change log) | 4 (High) | 5 (Critical) | 20 | Critical |

### 4.7 Event-Driven Re-Scoring

A risk is automatically re-scored when any of the following occurs:

| Trigger Event | Action |
|---|---|
| CISA KEV addition affecting the risk's vulnerability | Immediately re-score as Critical |
| Active exploit observed in the wild (per MSSP threat intel or CIR) | Re-score within 5 business days |
| Affected asset changes business criticality | Re-score within 30 days |
| Related incident occurs | Immediate re-score as part of post-incident review |
| Provider contract or SLA change materially alters control effectiveness | Re-score within 30 days |

---

## 5. Risk Treatment

### 5.1 Treatment Strategies

AnyTech uses four standard risk treatment strategies. Every risk in the register must have a documented treatment decision.

| Treatment | Definition | When Appropriate at AnyTech |
|---|---|---|
| **Remediate** | Eliminate the risk by removing the vulnerability, threat source, or exposure. | When technically feasible within reasonable time and cost. MSP/MSSP executes; CERG verifies closure. |
| **Mitigate** | Reduce likelihood or impact through compensating controls. | When full remediation is not immediately feasible. Engineering specifies controls; providers implement. |
| **Transfer** | Shift financial or operational impact through insurance, contract provisions, or provider SLAs. | For risks where insurance coverage is available, or where a provider contract SLA assigns accountability. "Transfer" at AnyTech often means assigning risk responsibility to the MSSP or MSP via contractual SLA. |
| **Accept** | Formally acknowledge and document the risk without further treatment. | When residual risk falls within AnyTech's appetite. Requires documented approval at the authority level defined in [§6](#6-risk-acceptance-authority-for-anytech). The IT Director must sign off on any acceptance above Medium. |

> **Transfer through provider SLAs.** At AnyTech, "Transfer" often means the risk of a specific control failure is contractually assigned to a provider. For example, the MSSP's SOC is contractually responsible for detecting and alerting on specific threat types — that risk is "transferred" to the provider via SLA. CERG monitors SLA compliance as the primary control; if the provider fails to meet the SLA, the risk transfers back to AnyTech and must be re-evaluated.

### 5.2 Treatment Decision Workflow

```
Risk identified (from any source in §3)
    │
    ▼
Entered into risk register
    │
    ▼
Risk scored (5×5 matrix per §4)
    │
    ▼
Treatment decision documented
    │
    ├── Remediate → Provider assigned → CERG validates closure
    ├── Mitigate  → Compensating controls specified → Provider implements → CERG validates
    ├── Transfer  → Contract/SLA assigned → CERG monitors SLA compliance
    └── Accept    → Approval per §6 authority table → Registered with expiration date
```

### 5.3 Compensating Controls

When a risk is mitigated (not remediated), compensating controls must be:

1. **Documented** in the risk register entry with enough detail that an independent reviewer can understand how they reduce exposure
2. **Validated** by CERG Risk (for technical controls) or Governance (for administrative/procedural controls)
3. **Re-validated** at least annually, or on any material change to the compensating control's operating environment

### 5.4 Treatment Timelines

| Severity | Default Treatment Timeline | Notes |
|---|---|---|
| Critical | 30 days | Remediate or accept with board/CEO documentation. Weekly progress review. |
| High | 90 days | Treatment plan required within 30 days. Monthly progress review. |
| Medium | 180 days | Treatment plan required. Quarterly progress review. |
| Low | 365 days | Annual review minimum. |

> **Extension policy.** If a treatment cannot be completed within the default timeline, a documented extension request must be submitted to the approving authority (per §6) before the original expiration date. Extensions beyond 180 days for High severity or 90 days for Critical severity require IT Director approval regardless of the standard authority table.

---

## 6. Risk Acceptance Authority for AnyTech

### 6.1 Authority Table

This table is the single source of truth for who may accept residual risk at AnyTech. It replaces the CISO-and-business-owner model used in the full CERG framework; AnyTech's model uses the IT Director as the executive authority with provider contract escalation.

| Residual Risk | Risk Role | CERG Role | Business / Executive Role | Acceptance By | Documentation Required | Default Max Duration |
|---|---|---|---|---|---|---|
| **Critical** | Signs finding; validates compensating controls; provides written risk assessment | Governance structures acceptance package; ensures board/CEO documentation | **IT Director** accepts business consequence; **CEO / Board** documented at next governance cycle | **IT Director + Board/CEO documentation** | Risk assessment, compensating controls, business justification, target remediation date, board/CEO memo | 30 days; renewal requires material change in treatment plan |
| **High** | Signs finding; validates compensating controls; provides written risk assessment | Governance structures acceptance package; coordinates IT Director review | **IT Director** accepts business consequence | **IT Director** | Risk assessment, compensating controls, business justification, target remediation date | 90 days; renewal requires documented progress toward remediation |
| **Medium** | Performs risk assessment; confirms residual risk level | Documents acceptance in register; **notifies IT Director** | Pillar Leader accepts business consequence | **Pillar Leader + IT Director notification** | Risk assessment, compensating controls, target remediation date; notification email to IT Director | 180 days; renewal requires confirmation conditions have not worsened |
| **Low** | Confirms low residual risk (if needed) | Approves procedural exception; tracks in risk register | Engineering or Risk Pillar Leader accepts | **Engineering or Risk Pillar Leader** | Brief justification; tracked in risk register | 365 days; annual review at minimum |

> **Notification vs. approval.** "Notification" means the IT Director is informed of a risk acceptance decision but is not required to approve it. The Pillar Leader who made the decision retains accountability. The IT Director may overrule any acceptance at any severity level.

### 6.2 Role Definitions

| Role | Who Holds It at AnyTech | Authority |
|---|---|---|
| **IT Director** | IT Director (executive) | High and Critical acceptance authority; may overrule any acceptance; board/CEO escalation for Critical. |
| **Risk Pillar Leader** | CERG Risk lead | Low acceptance authority; Medium acceptance with IT Director notification. |
| **Engineering Pillar Leader** | CERG Engineering lead | Low acceptance authority. |
| **Governance Pillar Leader** | CERG Governance lead | Low acceptance authority; Medium acceptance with IT Director notification. |
| **Board / CEO** | CEO or Board of Directors | Documented for Critical acceptances. Not a standing approval body for routine risk acceptance. |

> **Determining Risk Pillar Leader vs. Engineering Pillar Leader for Low acceptance.** If the risk is primarily technical (vulnerability, configuration, architecture), the Engineering Pillar Leader accepts. If the risk is primarily procedural or vendor-related (policy gap, contract issue, process failure), the Risk Pillar Leader accepts. When in doubt, the Risk Pillar Leader accepts and coordinates with Engineering.

### 6.3 Duration and Renewal Rules

- **No acceptance renews automatically.** Every acceptance requires a fresh approval cycle at expiration.
- An acceptance renewed more than twice without treatment progress escalates one tier above the original approver.
- The default durations in §6.1 apply unless a provider contract, SLA, or specific risk condition requires a shorter duration. If more than one rule applies, the shortest duration wins.

### 6.4 What Risk Acceptance Is Not

> Risk acceptance does not make the risk disappear. It is a deliberate decision to tolerate a known risk under specific conditions for a defined period. It does not:
> - Make the finding disappear from the risk register
> - Reset the treatment SLA without documented approval
> - Transfer accountability from the business to the CERG team
> - Satisfy a provider contractual requirement by itself
> - Excuse AnyTech from monitoring the risk
>
> **Every acceptance must have:** a named approver, a documented rationale, compensating controls where applicable, an expiration date, and a review commitment.

---

## 7. Continuous Monitoring

### 7.1 Monitoring Cadences

AnyTech operates a simplified continuous monitoring program appropriate for a small, provider-dependent team:

| Activity | Frequency | Owner | Provider Input | Output |
|---|---|---|---|---|
| MSSP alert review and triage | Daily (business days) | Risk Pillar Leader | MSSP SIEM dashboard / daily digest | Alert disposition; escalation log |
| Provider performance check | Weekly | Risk Pillar Leader | MSSP + MSP SLA dashboards | SLA compliance summary; escalation items |
| Vulnerability finding review | Weekly (external) / Monthly (internal) | Risk Pillar Leader | MSSP external scan + MSP authenticated scan | Prioritized finding register |
| Threat intelligence review | Weekly | Risk Pillar Leader | MSSP-curated threat intel feed | Risk re-scoring triggers; threat brief |
| Risk register review | Monthly | Governance Pillar Leader | Risk provides updated scores | Updated risk register; IT Director briefing items |
| Provider risk posture review | Quarterly | Risk Pillar Leader | MSSP + MSP quarterly performance reports | Provider risk rating update; contract remediation items |
| Full risk appetite recalibration | Annual | Risk Pillar Leader + IT Director | Annual risk register summary, incident history, business changes | Updated risk appetite statement |
| Penetration test | Annual | Risk Pillar Leader | MSSP pen test report | Risk register updates; control gap analysis |
| Access review | Quarterly | Governance Pillar Leader | MSP access review output | Access risk entries in register |
| Incident post-mortem | Per incident (within 30 days) | Risk + Governance Pillar Leaders | MSSP incident report | Lessons learned; risk register updates; control improvements |

### 7.2 Weekly Monitoring Details

The weekly risk review is the core continuous monitoring cadence at AnyTech. It should take no more than 60 minutes and covers:

1. **New MSSP alerts** — review any security alerts from the past week that were not auto-closed by the MSSP. Determine if any represent a risk register entry.
2. **Threat intel update** — review the MSSP's weekly threat intelligence summary. Note any relevant CISA KEV additions, sector-specific threats, or TTP changes.
3. **Vulnerability findings** — review critical and high-severity vulnerabilities from MSSP external scanning. Validate that MSP internal scanning is on schedule.
4. **Provider SLA compliance** — spot-check MSSP and MSP SLA metrics. Flag any SLA breaches or near-breaches.
5. **Open risk register items** — review any open items approaching their treatment deadline.

### 7.3 Monthly Risk Register Review

The monthly risk register review is chaired by the Governance Pillar Leader with the Risk Pillar Leader and IT Director. It covers:

- Full register pass: every open risk is reviewed for status, treatment progress, and score validity
- New risks added since the last review
- Risks approaching their treatment deadline
- Risks that have exceeded their acceptance expiration
- Provider SLA breaches with risk implications
- IT Director direction on any pending acceptance decisions

### 7.4 Annual Risk Appetite Recalibration

Once per year, aligned with AnyTech's planning cycle, the Risk Pillar Leader prepares a risk appetite recalibration package for the IT Director. The package contains:

1. **Risk register summary** — total open risk by severity, concentration by provider, treatment effectiveness rate
2. **Incident summary** — trailing 12 months of security incidents (frequency, severity, root causes)
3. **Provider performance summary** — trailing 12 months of MSSP and MSP SLA compliance
4. **Business changes** — new products, markets, technology, or organizational changes affecting risk posture
5. **Threat landscape summary** — significant threat trends from the trailing 12 months
6. **Recommended appetite changes** — proposed adjustments to the impact bands, acceptance authority thresholds, or treatment timelines

The IT Director reviews the package, approves or adjusts the recommendations, and documents the outcome. A "no change" decision is a deliberate conclusion, not a default.

### 7.5 Key Risk Indicators (KRIs)

AnyTech tracks a small set of KRIs that are measurable using provider-sourced data:

| KRI | Target | Source | Escalation Trigger |
|---|---|---|---|
| Critical/High findings past SLA | 0 Critical; <3 High past SLA | MSSP + MSP scan reports | Any Critical past SLA; >3 High past SLA |
| Open risk register items past target date | 0 | Risk register | Any item >30 days past target date |
| Provider SLA compliance | ≥95% per provider | MSSP + MSP SLA dashboards | <90% for two consecutive months |
| MSSP alert time-to-triage | Within SLA (per contract) | MSSP SLA report | Any breach of contractual SLA |
| MSP patch compliance — Critical | 100% within 14 days | MSP patch report | Any Critical patch >14 days late without approved exception |
| Risk register review cadence | 100% of monthly reviews completed | Calendar / meeting records | Missed monthly review |


---

## 8. Integration with Third-Party Risk

### 8.1 Relationship to PRC-TPRM-001

The CERG Third-Party and Supply Chain Risk Procedure ([PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md)) is the operational companion to this framework. Together, they ensure that:

- Provider and vendor risks are identified through [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) assessment activities
- Those risks enter the risk register and are scored per this framework (§4)
- Treatment decisions follow this framework (§5)
- Acceptance follows this framework's authority table (§6)
- Monitoring cadences capture provider risk posture (§7)

### 8.2 Provider Risk Scoring

Provider risk scores are treated as inputs to the AnyTech risk register. When [PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) produces a provider risk rating (e.g., from a vendor security assessment), it is translated into risk register entries using this framework's scoring methodology.

| Provider Input | Feeds Into | Risk Register Impact |
|---|---|---|
| MSSP contract SLA breach | Risk register: MSSP SLA failure | Scored per likelihood/impact of missed detection or response |
| MSP access review gap | Risk register: access control risk | Scored per likelihood/impact of unauthorized access |
| SaaS vendor assessment finding | Risk register: vendor risk entry | Scored per likelihood/impact of vendor compromise |
| MSSP incident report finding | Risk register: incident root cause risk | Scored per likelihood of recurrence and potential impact |

### 8.3 Provider Risk in the Register

Every risk entry that originates from a provider source must include:

- **Provider attribution** — which provider (MSSP, MSP, SaaS vendor) supplied the data
- **Provider impact** — whether the risk is primarily AnyTech-owned or provider-owned (i.e., the provider is responsible for the control but AnyTech owns the consequence)
- **Contract reference** — relevant contract section or SLA that governs the provider's responsibility

### 8.4 Quarterly Provider Risk Posture Review

The quarterly provider risk posture review (per §7.1) examines:

- Aggregate provider-sourced risk in the register (volume, severity, trends)
- Provider SLA performance and its effect on risk posture
- Provider contract changes that affect risk allocation
- Any open acceptance decisions involving provider-delivered controls
- Recommendations for contract remediation, SLA adjustment, or provider change

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-RMF-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Effective Date** | 2026-06-21 |
| **Classification** | Public |
| **Document Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Approved By** | IT Director (AnyTech) |
| **Review Cycle** | Annual; triggered by significant provider change, material incident, or IT Director request |
| **Next Scheduled Review** | 2027-06-21 |
| **Parent Document** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy |

### 9.1 Revision History

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0 | 2026-06-21 | Risk Pillar Leader | Initial AnyTech adaptation. Replaced CISO authority with IT Director. Simplified risk scoring (removed FAIR depth). Added provider-specific risk sources (§3). Adapted framework architecture for provider-delivered implementation (§2). Added AnyTech-specific acceptance authority table (§6). Simplified continuous monitoring (§7). Added provider risk integration (§8). |

### 9.2 Review Triggers

This document shall be reviewed outside the standard annual cycle when any of the following occurs:

- A material change in AnyTech's provider relationships (new MSSP, MSP, or significant contract change)
- A security incident that results in material financial or operational impact
- AnyTech enters a regulatory framework (e.g., CMMC, state privacy law, industry regulation)
- A change in the IT Director role or executive risk acceptance structure
- AnyTech's headcount, revenue, or risk profile changes significantly
- Provider SLA performance falls below 90% for two consecutive quarters

### 9.3 Related Documents

| Document ID | Title | Relationship |
|---|---|---|
| [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Cybersecurity Policy | Parent policy; establishes the CERG program |
| [CERG-GOV-OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Operating Model | Defines pillar roles and provider interaction model |
| [CERG-GOV-FRM-001](CERG-GOV-FRM-001_CERG_Framework_AnyTech.md) | CERG Framework | Top-level framework reference |
| [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) | Risk Register and Exception Process | Operational procedure for risk register management |
| [CERG-TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting_AnyTech.md) | Risk Register Templates and Reporting | Templates for risk register entries and reporting |
| [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) | Third-Party and Supply Chain Risk Procedure | Provider and vendor risk assessment procedure |
| [CERG-PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure_AnyTech.md) | Exposure Management Procedure | Vulnerability and exposure management operations |
| [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Document Catalog | Document catalog and naming convention |

---

*End of Document*
