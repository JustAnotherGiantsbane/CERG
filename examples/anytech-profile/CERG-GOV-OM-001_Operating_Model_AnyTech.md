## CERG OPERATING MODEL — AnyTech Adaptation
### Cyber Program-Office Model · Provider Federation · Pillar Structure

---

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On provider change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Premise — The Cyber Program Office](#2-operating-premise--the-cyber-program-office)
3. [The Three Pillars (Provider Oversight Reframed)](#3-the-three-pillars-provider-oversight-reframed)
4. [Authority, Reporting, and Decision Rights](#4-authority-reporting-and-decision-rights)
5. [Provider Engagement Model](#5-provider-engagement-model)
6. [Staffing and Roles](#6-staffing-and-roles)
7. [Coordination Cadence](#7-coordination-cadence)
8. [Interfaces With Providers and Functions](#8-interfaces-with-providers-and-functions)
9. [RACI Patterns](#9-raci-patterns)
10. [Provider SLA Framework](#10-provider-sla-framework)
11. [Maturity, Metrics, and Program Improvement](#11-maturity-metrics-and-program-improvement)
12. [Operating Model Control](#12-operating-model-control)

---

## 1. Purpose and Scope

This document describes the operating model for AnyTech's Cyber Engineering, Risk, and Governance (CERG) function. AnyTech does not operate a traditional in-house security operations team. The 8-person CERG team operates as a **cyber program office** that manages a federation of security service providers: an MSSP (SOC/IR), an MSP (IT operations), and a training vendor (awareness and phishing simulation).

This operating model defines the three pillars as they apply to AnyTech — not as hands-on delivery functions, but as oversight, validation, and governance bodies that ensure contracted providers meet their commitments. It defines the authority and reporting structure, the provider engagement models, the staffing patterns, and the coordination cadence that keeps an 8-person team in control of a broader security ecosystem.

This is not a policy. [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) is the policy. This document is the operating description that every CERG team member, IT Director, and contracted provider can use to understand how AnyTech's cyber function works and how to engage it.

### 1.1 Scope

This document applies to:

- The CERG function itself — Engineering, Risk, and Governance pillars under the IT Director's authority
- The interfaces between CERG and contracted providers (MSSP, MSP, training vendor)
- The interfaces between CERG and AnyTech business stakeholders, IT Director, and external auditors
- The provider oversight, validation, and governance models by which CERG ensures security outcomes without operating security tools directly
- The 8-person staffing model and the rules of engagement within and across the pillars

### 1.2 Relationship to Other Documents

This document is referenced by every CERG standard, procedure, and plan that applies to AnyTech. Where another document assigns work to "Engineering," "Risk," or "Governance," this document defines what those terms operationally mean — which at AnyTech is primarily about setting requirements for, validating the work of, and governing the performance of contracted providers.

---

## 2. Operating Premise — The Cyber Program Office

### 2.1 Why AnyTech Uses a Program-Office Model

AnyTech is not big enough to run a 24×7 SOC, a dedicated IT operations team, or an internal security awareness program. The 8-person cyber team cannot — and should not — attempt to replicate what a specialised provider can deliver at scale. Instead, AnyTech invests its 8 headcount in the **higher-value work of oversight, validation, and governance**.

This is the logical choice for an organisation of AnyTech's size. The risk is not that providers will be incompetent — it is that **providers will drift** from baseline, miss SLAs, miss context about AnyTech's environment, or work in isolation without coordinated threat intelligence and risk prioritisation. The CERG team exists to prevent that drift.

The CERG team does:

- **Set security requirements** — what providers must deliver, how they must operate, what evidence they must produce
- **Validate provider output** — is the MSSP tuning correctly? Is the MSP patching on schedule? Is the training vendor actually reducing susceptibility?
- **Govern provider performance** — SLA tracking, contract compliance, quarterly business reviews, escalation management
- **Manage risk** — aggregate provider-reported data into a single risk register, score and prioritise exposures, manage exceptions
- **Own policy and compliance** — write and maintain AnyTech policy, collect evidence from providers, manage audit engagements

The CERG team does **not**:

- Operate SIEM/SOAR consoles
- Run vulnerability scanners
- Execute patch deployment
- Manage endpoint administration
- Deliver end-user security training
- Run phishing campaigns
- Staff an incident response hotline

Those functions are contracted. The CERG team ensures they happen correctly.

### 2.2 The Yes-And Default

> **Governance Does Not Exist to Block the Business**
>
> CERG's default orientation is to enable the business with guardrails, not to close doors. When a risk cannot be eliminated, it is documented, owned, treated, and monitored, not refused on principle. Reflexive denial is not a risk management strategy. The hard work is making "yes" safe; "no" is the easy answer, and the wrong one.

### 2.3 Three Pillars, One Team, One Program Office

CERG operates as one team. The pillars provide structure for skill development, work intake, and accountability. At AnyTech, the pillars share an additional purpose: they are the lenses through which CERG evaluates provider performance. An MSSP report may contain a technical finding (Engineering lens), an exposure-scoring decision (Risk lens), and a contractual SLA implication (Governance lens). The pillars collaborate on every provider-facing decision.

---

## 3. The Three Pillars (Provider Oversight Reframed)

### 3.1 Cyber Engineering

**Mandate.** Set security requirements for contracted providers. Validate that provider-delivered architecture, configurations, and changes meet AnyTech standards. Be the technical authority for provider technical due diligence.

At AnyTech, Engineering does not build or operate infrastructure. It ensures that the providers who do build and operate infrastructure do so correctly.

**Core activities.**

- **Provider security requirements.** Define the technical security requirements in MSSP and MSP contracts. Maintain a requirements baseline that maps to AnyTech's control baseline.
- **Architecture validation.** Review provider-proposed architecture changes before implementation. Assess whether new controls, tool changes, or environment changes meet AnyTech requirements.
- **MSP change review.** Review MSP-proposed changes to infrastructure, endpoints, identity platforms, and cloud environments for security impact before approval. Track changes through to implementation validation.
- **Provider technical due diligence.** Evaluate new or replacement providers on technical capability. Conduct technical assessments during procurement and on periodic intervals for critical providers.
- **Incident response technical support.** During active incidents managed by the MSSP, provide AnyTech-specific technical context (environment knowledge, asset criticality, business impact). Not hands-on-keyboard — context and decisions.
- **Policy-as-code oversight.** Where AnyTech uses policy-as-code or automated enforcement mechanisms (e.g., cloud guardrails), Engineering defines the rules and validates provider-implemented changes.

**Engagement default.** Provider-aligned oversight. Engineering is engaged when a provider proposes a change, when a new provider is evaluated, or when provider technical output requires validation.

### 3.2 Cyber Risk

**Mandate.** Maintain continuous visibility into AnyTech's organisational exposure — using data provided by the MSSP and MSP. Own the risk register. Score and prioritise risks. Manage the exception and risk acceptance process.

At AnyTech, Risk does not run scanners, operate threat intel platforms, or conduct penetration tests. Risk receives and action data from the providers who do.

**Core activities.**

- **Risk register operation.** Own the single AnyTech risk register per [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). Intake risk data from MSSP (incident findings, threat intel, detection gaps) and MSP (patching gaps, access review findings, asset inventory gaps).
- **Exposure tracking.** Receive vulnerability data from MSSP's managed scanning and MSP's patching status. Score, prioritise, track remediation through provider SLAs. Report posture to IT Director.
- **MSSP intel consumption.** Consume threat intelligence feed from MSSP. Assess relevance to AnyTech environment. Escalate urgent intel to Engineering and IT Director. Track intel-to-detection coverage.
- **Vendor risk assessment.** Conduct periodic risk assessments of MSSP, MSP, and training vendor per [CERG-PRC-TPRM-001](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). Maintain provider risk tiers.
- **Exception management.** Own the exception process per [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §8. Route risk acceptance requests to the IT Director per the authority table in §4.2.
- **Provider-reported data quality.** Validate that risk-related data from providers is complete, timely, and accurate. Flag data gaps to Governance for SLA escalation.

**Engagement default.** Continuous service. Risk is always on; engagement is by exposure type and provider data cycle, not by ticket.

### 3.3 Cyber Governance

**Mandate.** Own the policy library, compliance posture, evidence collection from providers, SLA tracking, and provider performance management. Maintain the document control and evidence library. Coordinate audit and regulatory engagements.

At AnyTech, Governance does not deliver training, conduct audits of employees, or operate compliance scanning tools. It ensures that the providers and the CERG team collectively meet AnyTech's policy and compliance obligations.

**Core activities.**

- **Policy library.** Own [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) and all subordinate documents. Maintain AnyTech-specific adaptations. Write policy language that contractually binds providers.
- **Evidence collection.** Define the evidence requirements that each provider must produce. Collect, validate, and archive evidence on a standing cadence. Produce evidence packages for audits and assessments.
- **SLA tracking.** Track provider SLAs defined in contracts and the Provider SLA Framework (§10). Flag misses. Report SLA performance to IT Director monthly.
- **Provider performance management.** Lead quarterly provider business reviews. Maintain provider scorecards. Escalate chronic underperformance per contract terms.
- **Compliance oversight.** Map provider-delivered controls to the AnyTech control baseline. Identify coverage gaps. Manage corrective action plans.
- **Document control.** Maintain version control, review cycles, metadata consistency per CERG-GOV-STY-001. Own the Document Catalog.
- **Audit and assessor liaison.** Serve as primary point of contact for external auditors and assessors. Coordinate evidence production across CERG pillars and providers.

**Engagement default.** Program oversight and advisory. Governance is engaged when SLA performance, evidence production, compliance posture, or provider contract terms are in play.

### 3.4 What CERG Is Not Responsible For

The following functions are delivered by contracted providers and overseen by CERG:

- **Security Operations (SOC).** Delivered by MSSP. CERG receives alerts, reports, and metrics.
- **Incident Response.** Delivered by MSSP under retainer. CERG provides context and business-impact guidance during active incidents.
- **IT Operations (patching, IAM, endpoint management, asset management).** Delivered by MSP. CERG validates activity and results.
- **Security Awareness Training and Phishing Simulation.** Delivered by training vendor. CERG reviews completion metrics and susceptibility trends.
- **Physical Security.** Owned by Facilities / Business Operations.
- **Privacy Program.** Owned by Legal / Privacy lead.
- **Business Continuity (non-cyber).** Owned by Enterprise Risk / Operations.

---

## 4. Authority, Reporting, and Decision Rights

### 4.1 Reporting Line

AnyTech does not have a CISO or CSO. The CERG function reports through pillar leaders to the **IT Director**, who carries executive risk acceptance authority for cyber matters.

The three pillars report to the IT Director through pillar leaders. Pillar leaders have operational authority within their domains and escalate to the IT Director for decisions that exceed their authority or carry material organisational risk.

```
IT Director
│
├── Engineering Pillar Leader (Engineering Team — 3 people)
├── Risk Pillar Leader (Risk Team — 3 people)
└── Governance Pillar Leader (Governance Team — 2 people)
```

The IT Director reports to the AnyTech executive leadership (CEO / COO) and provides cyber posture updates in the regular executive reporting cadence.

### 4.2 Decision Rights

| **Decision** | **Authority** |
|---|---|
| Policy approval (CERG-POL-001 and subordinate documents) | IT Director (on recommendation from Governance Pillar Leader) |
| Standards / procedure approval | Pillar leader; IT Director for material changes |
| Risk acceptance — all severities | Per Risk Acceptance Authority table below |
| Exception approval | Per [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §8 |
| MSSP / MSP contract changes (security scope) | Governance Pillar Leader with Engineering/Risk input; IT Director for material scope changes |
| Provider onboarding / offboarding | Governance Pillar Leader with joint pillar review; IT Director approval |
| New SaaS / cloud service approval | Engineering + Risk evaluation; IT Director for Restricted-data placements |
| Incident classification during active event | MSSP Incident Commander, with AnyTech IT Director for business-impact decisions |
| External notification (regulator, public) | IT Director + Legal |
| Budget allocation across providers | IT Director |

**Risk Acceptance Authority Table:**

| **Residual Risk Severity** | **Authority** |
|---|---|
| Critical | IT Director |
| High | IT Director |
| Medium | Risk Pillar Leader |
| Low / Informational | Governance Pillar Leader |

The IT Director is the final risk acceptance authority for all severities above Medium. The IT Director may delegate acceptance for specific risk classes in writing, but retains accountability.

### 4.3 Escalation Path

**Internal escalation (within CERG):**

Disagreements that the pillars cannot resolve are escalated to the IT Director. Any CERG team member may raise a concern directly to a pillar leader or the IT Director if they believe a decision materially violates policy or creates unacceptable regulatory exposure.

**Provider escalation:**

- **For IR matters** — CERG Engineering or Risk Lead escalates to MSSP service delivery manager. If unresolved, to MSSP account director. If still unresolved, CERG Governance Lead activates contract escalation clauses.
- **For IT operations matters** — CERG Engineering Lead escalates to MSP service delivery manager. If unresolved, to MSP account director. If still unresolved, CERG Governance Lead activates contract escalation clauses.
- **For training/awareness matters** — CERG Governance Lead escalates to training vendor account manager.

Providers do not report to the IT Director. They are contracted service providers. Escalation follows contractual paths, not management reporting lines.

### 4.4 CERG Risk and Posture Forum (CRPF)

The **CERG Risk and Posture Forum (CRPF)** is the standing internal forum that reviews cyber risk posture at AnyTech between executive reporting cycles. It is chaired by the IT Director.

**Standing core members (every meeting):**
- IT Director — Chair
- Engineering Pillar Leader
- Risk Pillar Leader
- Governance Pillar Leader
- Business Operations representative (alternating, per agenda)

**Invited (per agenda):**
- MSSP service delivery manager — for incident trends, threat landscape items
- MSP service delivery manager — for patching/infrastructure posture items
- Any business owner whose systems appear on the risk agenda

The CRPF meets **monthly** and serves three purposes:

1. **Posture review.** Risk Pillar Leader presents the risk register summary, top KRIs, and any High or Critical risk acceptance decisions since last meeting.
2. **Provider alignment.** Review provider SLA performance, open escalations, and upcoming provider engagements.
3. **Pre-executive briefing.** Prepare the cyber posture update for anytech executive leadership.

The CRPF is not a risk acceptance authority. Acceptance authority lives in §4.2.

---

## 5. Provider Engagement Model

### 5.1 MSSP Engagement (SOC / IR / Threat Intel)

**Scope of provider responsibility:**
- 24×7 SOC monitoring and alert triage
- Detection engineering and SIEM management
- Incident response (triage, containment, eradication, recovery support)
- Threat intelligence feed production and delivery
- Monthly reporting (alerts, incidents, detection coverage metrics)
- Quarterly readiness report and tabletop exercise facilitation

**CERG engagement:**
- Receive and review daily/weekly alert summaries (Engineering + Risk)
- Participate in monthly SLA review meeting (all pillars)
- Review quarterly IR readiness report (Risk + Engineering)
- Participate in quarterly tabletop exercise (all pillars)
- Consume threat intelligence feed and assess relevance (Risk)
- Report MSSP performance into the monthly CRPF (Governance)

**Key interfaces:**
- Engineering: reviews detection rule changes, validates SIEM architecture changes
- Risk: consumes intel feed, reviews incident reports, tracks exposure data
- Governance: tracks SLA performance, manages contract compliance, leads QBRs

### 5.2 MSP Engagement (IT Operations / IAM / Patching / Endpoints)

**Scope of provider responsibility:**
- IT service desk and end-user support
- Identity and access management (joiner/mover/leaver, access reviews)
- Patch management (OS, third-party applications)
- Endpoint management (configuration, EDR agent health, compliance)
- Asset inventory maintenance
- Change management execution
- Monthly reporting (patching status, access review evidence, asset changes)

**CERG engagement:**
- Review and approve MSP-proposed changes with security impact (Engineering)
- Validate patching completion and SLA adherence (Engineering + Risk)
- Review access review evidence (Governance)
- Conduct periodic spot-checks of asset inventory completeness (Risk)
- Report MSP performance into the monthly CRPF (Governance)

**Key interfaces:**
- Engineering: validates MSP changes, reviews endpoint baselines, approves IAM configuration changes
- Risk: receives patching data, tracks exposure closure
- Governance: tracks SLA performance, collects evidence, leads QBRs

### 5.3 Training Vendor Engagement (Awareness)

**Scope of provider responsibility:**
- Mandatory annual security awareness training content and delivery
- Phishing simulation campaigns (monthly or quarterly as determined)
- Completion tracking and reporting
- Susceptibility trend analysis

**CERG engagement:**
- Review training content for alignment with policy (Governance)
- Review phishing simulation results (Governance + Risk)
- Determine campaign cadence and target groups (Governance)
- Escalate trends above threshold to IT Director (Governance)

**Key interfaces:**
- Governance: leads vendor management, reviews content, tracks completion
- Risk: reviews phishing susceptibility data for risk register implications

### 5.4 Provider RACI Summary

| **Activity** | **CERG** | **MSSP** | **MSP** | **Training Vendor** | **IT Director** |
|---|---|---|---|---|---|
| SOC monitoring and alert triage | I | **R/A** | — | — | I |
| Incident response execution | C | **R/A** | C | — | I |
| Detection engineering | C | **R/A** | — | — | I |
| Threat intelligence production | C | **R/A** | — | — | I |
| Vulnerability scanning | I | **R** | C | — | I |
| Patch deployment | I | — | **R/A** | — | I |
| Access management (identity lifecycle) | C | — | **R/A** | — | I |
| Endpoint management | I | C | **R/A** | — | I |
| Asset inventory maintenance | C | — | **R/A** | — | I |
| Security awareness training delivery | I | — | — | **R/A** | I |
| Phishing simulation execution | I | — | — | **R/A** | I |
| Risk register operation | **A** | C | C | — | I |
| Policy authorship and maintenance | **R/A** | I | I | — | C |
| SLA tracking and performance management | **A** | R | R | R | I |
| Provider contract management | **A** | C | C | C | C |
| Risk acceptance authority | C | — | — | — | **A** |

**Key:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 6. Staffing and Roles

### 6.0 Core Capabilities

Before defining roles, CERG defines capabilities — the durable work that must get done regardless of headcount. Capabilities survive reorgs. Roles are implementation detail.

At AnyTech, the 11 core CERG capabilities are delivered by 8 people:

| **Capability** | **Description** | **Primary Pillar** |
|---|---|---|
| **Security Requirements and Architecture Validation** | Define provider requirements, validate provider-proposed architecture and changes | Engineering |
| **Identity and Platform Security Oversight** | Set IAM requirements, validate MSP IAM operations, review cloud security posture | Engineering |
| **Change Security Review** | Review MSP-proposed changes for security impact before implementation | Engineering |
| **Exposure Management** | Receive and action vulnerability data from providers; track remediation through SLAs | Risk |
| **Threat Intelligence Consumption** | Consume MSSP intel feed; assess relevance; escalate urgent items | Risk |
| **Vendor Risk Management** | Assess providers, manage provider risk tiers, conduct due diligence | Risk |
| **Risk Register and Analysis** | Risk identification, scoring, treatment recommendation, exception management | Risk |
| **Policy and Standards** | Policy authorship, standard maintenance, regulatory citation mapping | Governance |
| **Compliance and Evidence Management** | Evidence collection from providers, audit coordination, control mapping | Governance |
| **SLA and Provider Performance** | SLA tracking, provider scorecards, quarterly business reviews | Governance |
| **Executive Risk Decision Support** | CRPF preparation, risk acceptance documentation, IT Director reporting | Governance (with all pillars) |

At 8 people, every person holds multiple capabilities. The capabilities remain the same as a 60-person team — the difference is breadth per person.

### 6.1 AnyTech Role Roster

| **Role** | **Pillar** | **Headcount** | **Primary Capabilities** |
|---|---|---|---|
| Engineering Pillar Leader | Engineering | 1 | Security requirements, architecture validation, change review, provider tech due diligence |
| Security Engineer (Cloud + AppSec) | Engineering | 1 | Cloud security oversight, application security validation, SaaS governance |
| Security Engineer (Identity + Platform) | Engineering | 1 | IAM requirements, endpoint baseline validation, platform security, change review support |
| Risk Pillar Leader | Risk | 1 | Risk register, exposure management, vendor risk, escalation management, CRPF preparation |
| Risk Analyst (Exposure + Intel) | Risk | 1 | Vulnerability data processing, threat intel consumption, KRI reporting |
| Risk Analyst (Vendor + Assessment) | Risk | 1 | Provider risk assessments, due diligence, exception process, risk register inputs |
| Governance Pillar Leader | Governance | 1 | Policy library, compliance oversight, provider QBRs, audit liaison, document control |
| Evidence / SLA Manager | Governance | 1 | Evidence collection from providers, SLA tracking, scorecards, reporting |

**Total: 8 people** (Engineering 3, Risk 3, Governance 2)

### 6.2 Role Descriptions

#### Engineering Pillar Leader

Owns the Engineering pillar. Sets provider technical requirements. Approves or rejects MSP/MSSP-proposed changes with security impact. Leads provider technical due diligence. Reports to IT Director. Acts as the technical authority for provider validation.

#### Security Engineer (Cloud + AppSec)

Owns cloud security posture validation. Reviews MSP cloud configuration changes. Validates MSSP detection coverage for cloud workloads. Conducts application security reviews. Supports SaaS governance evaluations.

#### Security Engineer (Identity + Platform)

Owns identity security requirements. Validates MSP IAM operations (joiner/mover/leaver, access reviews, MFA configuration). Reviews endpoint management baselines. Supports platform security validation and change review.

#### Risk Pillar Leader

Owns the risk register. Receives and actions risk data from MSSP (incidents, vulnerabilities, intel) and MSP (patching gaps, access issues). Leads exposure tracking and prioritisation. Manages vendor risk program. Reports to IT Director. Presents at CRPF.

#### Risk Analyst (Exposure + Intel)

Manages vulnerability data pipeline from providers. Scores and prioritises findings. Tracks remediation through provider SLAs. Consumes MSSP threat intelligence feed. Maintains KRI dashboard.

#### Risk Analyst (Vendor + Assessment)

Conducts provider risk assessments per [CERG-PRC-TPRM-001](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). Manages the exception process. Supports risk register entries from assessment findings. Tracks provider risk tier changes.

#### Governance Pillar Leader

Owns the policy library, compliance program, and provider performance management. Leads quarterly provider business reviews. Serves as audit liaison. Manages the document catalog. Reports to IT Director. Prepares CRPF materials.

#### Evidence / SLA Manager

Collects, validates, and archives provider evidence. Tracks SLA performance across all providers. Maintains provider scorecards. Produces monthly SLA reports. Supports audit evidence production. Backs up Governance Pillar Leader.

### 6.3 Role Consolidation Principles

At 8 people, depth is traded for breadth. Key principles:

- **Every pillar lead also does individual contributor work.** The Engineering Pillar Leader reviews MSP changes directly. The Risk Pillar Leader scores risks. The Governance Pillar Leader writes policy.
- **Cross-training is essential.** Every team member should be able to cover at least one capability outside their primary pillar for short periods.
- **The Evidence/SLA Manager role is the most back-office role** — it was intentionally created to keep the Governance Pillar Leader available for strategic work (QBRs, audit, policy).
- **No single-person points of failure.** For each critical capability, at least two people are trained. The risk register is the most critical — at least three people (Risk Pillar Leader + both Risk Analysts) can operate it.

---

## 7. Coordination Cadence

An 8-person team cannot afford meetings that duplicate provider calls or create overhead without output. Every standing meeting serves a specific purpose.

### 7.1 Standing Cadence

| **Forum** | **Cadence** | **Participants** | **Purpose** |
|---|---|---|---|
| CERG Team Standup | Weekly (30 min) | All 8 CERG members | Cross-pillar priorities, blockers, provider issues. Standing agenda: (1) provider status, (2) escalations, (3) this week's priorities. |
| Provider SLA Check-In (MSSP week) | Fortnightly (30 min) | Engineering + Risk + MSSP SDM | MSSP SLA review: alert volume, detection coverage, intel highlights, open incidents. Alternates with MSP week. |
| Provider SLA Check-In (MSP week) | Fortnightly (30 min) | Engineering + Governance + MSP SDM | MSP SLA review: patching status, access review progress, change log, asset inventory updates. Alternates with MSSP week. |
| Risk Posture Review | Weekly (30 min) | Risk + Engineering + Governance | Top risks, treatment progress, SLA breaches, provider data quality issues. |
| CRPF (CERG Risk and Posture Forum) | Monthly (45 min) | IT Director + all pillar leaders + invited providers | Risk register summary, top KRIs, provider performance, risk acceptance decisions, pre-executive briefing. |
| Provider Performance Review | Monthly (30 min) | Governance + relevant provider SDM | Detailed SLA scorecard review, evidence gaps, corrective action status. Alternates between providers on a 3-week cycle. |
| Provider Quarterly Business Review | Quarterly (90 min) | IT Director + all pillar leaders + provider account team | Strategic review: overall performance, improvement plan, contract changes, roadmap alignment |
| Tabletop Exercise | Quarterly (90 min) | CERG team + MSSP + invited business stakeholders | Scenario-based exercise. MSSP facilitates; CERG participates in decision-making. |
| CERG Team Improvement Session | Quarterly (60 min) | All 8 CERG members | Lessons learned, process improvements, cross-training review, backlog refinement. |
| Policy Review Cycle | Annual (as scheduled) | Governance Lead + all pillars | Full policy library review, gap analysis, update cycle. |
| Risk Appetite Recalibration | Annual | IT Director + all pillar leaders | Review and recalibrate risk appetite thresholds for the coming year. |

### 7.2 Meeting Discipline

- **Standups are strictly 30 minutes.** No extensions. Use async updates (Slack/Teams) for non-blocking information.
- **SLA check-ins alternate** to avoid consuming pillar leads with back-to-back provider calls. The off-week provider provides a written status update that Governance reviews asynchronously.
- **QBRs are the escalation point**, not the first conversation about a problem. Issues should be surfaced during SLA check-ins or monthly reviews.
- **No meeting without an agenda** prepared at least 24 hours in advance. Governance Pillar Leader enforces this.

---

## 8. Interfaces With Providers and Functions

### 8.1 Provider Interfaces

| **Provider** | **Interface Type** | **CERG Lead** | **Output Cadence** |
|---|---|---|---|
| MSSP | SOC alert summary | Risk (daily review) | Daily / Weekly |
| MSSP | Incident report | Risk + Engineering | Per incident + Monthly summary |
| MSSP | Threat intelligence feed | Risk | Continuous + Weekly briefing |
| MSSP | SIEM health / detection coverage | Engineering | Monthly |
| MSSP | IR readiness report | Risk + Engineering | Quarterly |
| MSSP | Tabletop exercise facilitation | All pillars | Quarterly |
| MSP | Patching status report | Engineering | Weekly / Monthly |
| MSP | Access review evidence | Governance | Monthly |
| MSP | Asset inventory | Governance | Monthly |
| MSP | Change log (security-impacting) | Engineering | Per change + Monthly summary |
| MSP | Endpoint compliance report | Engineering | Monthly |
| Training vendor | Training completion report | Governance | Monthly |
| Training vendor | Phishing campaign results | Governance + Risk | Per campaign |

### 8.2 Internal Function Interfaces

| **Function** | **Interface** | **CERG Lead** |
|---|---|---|
| IT Director | Executive risk acceptance, posture reporting, budget, escalation | All pillar leaders |
| Business Operations | Business impact context for risk decisions, system ownership | Risk + IT Director |
| Legal / Privacy | Breach notification, privacy obligations, contract language | Governance |
| Procurement | Provider contract terms, vendor onboarding, license management | Governance |
| Finance | Budget, provider invoice validation against SLA performance | Governance |
| Internal Audit | Evidence production, audit coordination, findings management | Governance |
| Enterprise Risk (non-cyber) | Cross-risk coordination, business continuity planning | Risk |

---

## 9. RACI Patterns

The following patterns illustrate how CERG distributes work with providers. Specific RACI matrices are maintained per procedure. Role names follow the roster in §6.1.

### 9.1 Provider-Proposed Infrastructure Change

| **Activity** | **CERG Engineering** | **CERG Risk** | **CERG Governance** | **MSP** | **IT Director** |
|---|---|---|---|---|---|
| Propose change with security impact | I | I | I | **R** | I |
| Assess security impact | **R / A** | C | I | C | I |
| Approve / reject change | **A** | C | I | R | I (material changes only) |
| Implement change | I | I | I | **R** | I |
| Validate implementation | **R / A** | I | I | C | I |
| Update asset inventory | C | I | C | **R / A** | I |
| Close change record | I | I | **A** | R | I |

### 9.2 MSSP-Detected Security Incident

| **Activity** | **CERG Engineering** | **CERG Risk** | **CERG Governance** | **MSSP** | **IT Director** |
|---|---|---|---|---|---|
| Detect and triage | I | I | I | **R / A** | I |
| Classify severity | C | C | I | **R** | **A** (business impact) |
| Contain threat | C | I | I | **R / A** | I |
| Investigate root cause | C | **R** | I | **R** | I |
| Document incident | I | I | **A** | R | I |
| Update risk register | I | **R / A** | C | C | I |
| Determine notification requirements | I | C | **A** | C | **A** |
| Conduct post-incident review | C | **R** | **A** | R | I |

### 9.3 Vulnerability Finding Past SLA

| **Activity** | **CERG Engineering** | **CERG Risk** | **CERG Governance** | **MSP** | **IT Director** |
|---|---|---|---|---|---|
| Identify SLA breach | I | **R / A** | I | C | I |
| Recommend compensating controls | **R / A** | C | I | C | I |
| Decide treatment (remediate / mitigate / accept) | C | **R** | C | R | **A** (High+) |
| Approve risk acceptance (if High+) | I | C | I | I | **A** |
| Record in risk register | I | **R / A** | C | I | I |
| Escalate to provider contract level | I | C | **R / A** | I | C |

### 9.4 Annual Policy Review Cycle

| **Activity** | **CERG Engineering** | **CERG Risk** | **CERG Governance** | **Providers** | **IT Director** |
|---|---|---|---|---|---|
| Review policy library for currency | C | C | **R / A** | I | I |
| Identify gaps (regulatory, operational, provider contract) | C | C | **R / A** | C | I |
| Draft policy updates | I | I | **R / A** | I | I |
| Operational practicability review (with providers) | **R** | C | C | C | I |
| Approve policy updates | I | I | **R** | I | **A** |
| Communicate changes to providers | I | I | **R / A** | C | I |
| Update provider contract requirements | I | C | **R / A** | C | C |

### 9.5 Quarterly Provider Business Review

| **Activity** | **CERG Engineering** | **CERG Risk** | **CERG Governance** | **Provider** | **IT Director** |
|---|---|---|---|---|---|
| Prepare performance scorecard | C | C | **R / A** | C | I |
| Present SLA performance | I | I | **R** | **A** | I |
| Review improvement plan | C | C | **R** | **A** | **A** |
| Discuss contract / scope changes | C | C | **R** | **A** | **A** |
| Document QBR outcomes | I | I | **R / A** | C | I |
| Escalate unresolved issues | I | I | **R** | C | **A** |

---

## 10. Provider SLA Framework

### 10.1 SLA Categories and Metrics

Provider SLAs are grouped into four categories. Each metric has a defined measurement method, reporting cadence, and consequence tier for misses.

#### MSSP SLAs

| **Metric** | **Target** | **Measurement** | **Reporting** |
|---|---|---|---|
| Alert triage time (P1/P2) | ≤ 15 minutes | MSSP system logs | Monthly |
| Alert triage time (P3/P4) | ≤ 60 minutes | MSSP system logs | Monthly |
| Incident containment time (P1) | ≤ 2 hours | MSSP incident timeline | Per incident + Monthly |
| SIEM uptime | ≥ 99.9% | MSSP platform status | Monthly |
| Detection coverage (ATT&CK mapped) | ≥ 85% of applicable techniques | MSSP coverage report | Quarterly |
| Threat intelligence feed delivery | Daily, by 08:00 local | Feed receipt timestamp | Monthly |
| Monthly report delivery | Within 5 business days of month end | Report receipt date | Monthly |
| Quarterly IR readiness report | Within 10 business days of quarter end | Report receipt date | Quarterly |

#### MSP SLAs

| **Metric** | **Target** | **Measurement** | **Reporting** |
|---|---|---|---|
| Critical patch deployment | ≤ 72 hours from vendor release | MSP patch log | Weekly |
| High severity patch deployment | ≤ 7 days from vendor release | MSP patch log | Weekly |
| Standard patch deployment | ≤ 30 days from vendor release | MSP patch log | Monthly |
| Endpoint agent health (EDR, AV, MDM) | ≥ 98% active | MSP endpoint platform | Monthly |
| Access review completion | Quarterly, within 5 business days of review start | Evidence delivery | Quarterly |
| Joiner/Mover/Leaver processing (access changes) | ≤ 24 hours from request | MSP ticket system | Monthly |
| Asset inventory completeness | ≥ 95% of known assets | Inventory vs. expected count | Monthly |
| Incident response to MSP-handled tickets (P1) | ≤ 30 minutes | MSP ticket system | Monthly |

#### Training Vendor SLAs

| **Metric** | **Target** | **Measurement** | **Reporting** |
|---|---|---|---|
| Annual training completion rate | ≥ 95% within 45 days of launch | Vendor platform | Monthly during campaign |
| Phishing simulation campaign delivery | Monthly on agreed schedule | Campaign trigger timestamp | Per campaign |
| Susceptibility rate | ≤ 10% first click, trending down | Vendor platform | Per campaign + Quarterly |
| Report delivery | Within 5 business days of campaign end | Report receipt date | Per campaign |

### 10.2 SLA Miss Consequences

| **Tier** | **Miss Duration** | **AnyTech Response** |
|---|---|---|
| **Observation** | First miss within 90-day window | Documented in provider scorecard. No formal action. Addressed in next SLA check-in. |
| **Warning** | Second miss (same metric) or any P1 SLA miss | Written notice to provider SDM. Provider must provide root cause and corrective action plan within 5 business days. |
| **Escalation** | Third miss (same metric) or P1 SLA miss unresolved > 24 hours | Escalate to provider account director. IT Director informed. Corrective action plan must include timeline. Possible service credit invocation per contract. |
| **Breach** | Fourth miss (same metric) or failure to execute corrective action plan | Formal contract breach notice. Governance escalates to IT Director and Legal. Service credits invoked. Contract termination evaluation begins. |

**Formula:** Each metric is tracked separately. The miss count resets after 90 consecutive calendar days without a miss on that metric.

### 10.3 Evidence and Reporting Requirements

Each provider must deliver the following evidence on a standing cadence. Governance maintains the evidence library.

**MSSP provides:**
- Monthly SLA report with metric-by-metric performance
- Incident reports within 48 hours of containment
- Weekly threat intelligence summary
- Quarterly IR readiness assessment
- SIEM health and detection coverage metrics (monthly)
- Alert volume and classification trends (monthly)

**MSP provides:**
- Monthly patching status report (by severity, by system class)
- Access review completion evidence (quarterly)
- Asset inventory (monthly, vs. previous month for delta tracking)
- Change log extract for security-impacting changes (monthly)
- Endpoint compliance report (monthly)
- Ticket metrics for security-related requests (monthly)

**Training vendor provides:**
- Training completion report (monthly during campaign window)
- Phishing campaign results (per campaign: sent, clicked, reported, compliance rate)
- Quarterly trend analysis

---

## 11. Maturity, Metrics, and Program Improvement

### 11.1 The Adaptive Target

AnyTech targets NIST Cybersecurity Framework **Tier 3, Repeatable** posture as the practical target for an 8-person program-office model. Tier 4 (Adaptive) is aspirational and pursued as the team matures, but Tier 3 is the realistic operating level where:

- Provider performance is consistently measured and governed
- Risk decisions are documented and repeatable
- Policy is current and enforced through provider contracts
- Lessons learned from incidents and exercises are systematically captured and actioned

### 11.2 Key Metrics

The following metrics are tracked by Governance and reported to the IT Director and the CRPF.

| **Metric** | **What It Measures** | **Source** |
|---|---|---|
| % of provider SLAs met (by provider, by metric) | Provider performance | Governance SLA tracker |
| Provider corrective action plan completion rate | Provider responsiveness | Governance |
| Open risk register entries by severity | Risk posture | Risk register |
| Median time-to-remediate by severity (tracked through provider SLAs) | Exposure responsiveness | Risk (from provider data) |
| % of risks within scheduled review date | Risk register health | Risk |
| Open exception count and median age | Governance discipline | Governance |
| Asset inventory completeness | Visibility | Governance (from MSP data) |
| Endpoint agent health (EDR, AV, MDM) | Control coverage | Engineering (from MSP data) |
| Phishing susceptibility trend | Workforce posture | Governance (from training vendor) |
| Annual training completion | Policy compliance | Governance (from training vendor) |
| Detection coverage (ATT&CK mapped) | Detection capability | Engineering (from MSSP data) |

### 11.3 Continuous Improvement

Every CERG activity produces feedback into the program improvement register:

- **Post-incident lessons** → Risk register entries, provider requirement updates
- **SLA miss patterns** → Provider corrective actions, contract renegotiation items
- **Tabletop exercise results** → Policy updates, procedure updates, provider scope changes
- **Vendor risk assessment findings** → Provider improvement plans, risk register entries
- **Policy review gaps** → Policy updates, new provider requirements
- **Team improvement sessions** → Process changes, tooling improvements, cross-training needs

The improvement register is reviewed quarterly. Items that age beyond planned dates without justification are flagged to the IT Director.

---

## 12. Operating Model Control

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (AnyTech CERG) |
| **Approved By** | IT Director (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On provider change |
| **Next Scheduled Review** | 2027-06-21 |
| **Frameworks** | NIST CSF 2.0 |
| **Environments** | AnyTech in-scope environments |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-21 | Engineering Pillar Leader (AnyTech CERG) | Initial AnyTech Adaptation. Complete rewrite of OM-001 for the 8-person program-office model. Introduced provider federation structure (MSSP, MSP, training vendor), provider SLA framework, program-office RACI patterns, and role consolidation for 8-person team. Removed CISO references; established IT Director as executive risk acceptance authority. |

### Review Triggers

This operating model shall be reviewed annually and upon any of the following:

- Change in AnyTech provider structure (new provider, provider change, significant contract change)
- Change in CERG team size or structure (growth or reduction beyond 8 ± 2)
- Significant incident that reveals a structural gap in the provider oversight model
- IT Director transition
- Addition of a regulatory regime to AnyTech scope
- Direction from AnyTech executive leadership

The Engineering Pillar Leader owns this document. Governance maintains it on behalf of the team. Changes require IT Director approval and acknowledgment by all pillar leaders.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Parent policy — defines the CERG operating model at the principle level |
| Risk Register and Exception Process | [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk register operating procedure; applies to AnyTech with provider-sourced data |
| Third-Party and Supply Chain Risk Procedure | [CERG-PRC-TPRM-001](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Provider risk assessment methodology; directly applied to MSSP, MSP, training vendor |
| Architecture Review and Project Intake Procedure | [CERG-PRC-AR-001](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Pre-production engagement; adapted for provider-proposed changes |
| Document Authoring and Style Guide | CERG-GOV-STY-001 | Document formatting and metadata conventions |
| Document Catalog and Naming Convention | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Authoritative inventory of every CERG artifact |
| Metrics, Dashboard, and CISO/Board Reporting | CERG-GOV-MTR-001 | KRIs, KPIs, CISO dashboard; adapted for IT Director reporting |
| Risk Management Framework | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework_AnyTech.md) | Risk lifecycle, scoring methodology |
| Unified Control Baseline | CERG-GOV-CB-001) | Control spine for mapping provider-delivered controls |
| Adversarial Validation Procedure | [CERG-PRC-AV-001](../../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Penetration testing; delivered by MSSP under CERG oversight |
| Security Change Management Procedure | [CERG-PRC-CHG-001](../../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Change review procedure for provider-proposed changes |
| Audit and Evidence Management Procedure | [CERG-PRC-AUD-001](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence collection procedure; applies to provider evidence |
| Lessons Learned and Program Improvement Procedure | [CERG-PRC-LL-001](../../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) | Post-incident and program improvement process |
| Exposure Management Procedure | [CERG-PRC-VM-001](../../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Vulnerability management; data sourced from MSSP/MSP |
| Threat Intelligence Procedure | [CERG-PRC-TI-001](../../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Intel consumption process; feed sourced from MSSP |

---

*End of Document — CERG-GOV-OM-001 (AnyTech Adaptation)*
