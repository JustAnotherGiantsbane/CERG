
# SURGE — Cyber Engineering, Risk & Governance

## CERG OPERATING MODEL
### Pillar Structure · Engagement Models · Staffing · Interaction Patterns

---

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.0 DRAFT |
| **Status** | For Review |
| **Classification** | Internal — Confidential |
| **Owner** | Chief Information Security Officer |
| **Parent Policy** | CERG-POL-001 — Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Organizational Change |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 · NIST RMF · ISO 27001 |
| **Audience** | All CERG personnel; business sponsors; IT and OT leadership; executive leadership |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Premise](#2-operating-premise)
3. [The Three Pillars](#3-the-three-pillars)
4. [Authority, Reporting, and Decision Rights](#4-authority-reporting-and-decision-rights)
5. [Engagement Models](#5-engagement-models)
6. [Staffing and Roles](#6-staffing-and-roles)
7. [Coordination Cadence](#7-coordination-cadence)
8. [Interfaces With Other Functions](#8-interfaces-with-other-functions)
9. [RACI Patterns](#9-raci-patterns)
10. [Maturity, Metrics, and the Adaptive Target](#10-maturity-metrics-and-the-adaptive-target)
11. [Operating Model Control](#11-operating-model-control)

---

## 1. Purpose and Scope

This document describes the operating model for the Cyber Engineering, Risk, and Governance (CERG) function. It defines the three pillars, the authority and reporting structure, the engagement models through which CERG delivers value to the business, the staffing patterns that support those engagements, and the cadence by which CERG operates as one team rather than three silos.

This is not a policy. CERG-POL-001 is the policy. This document is the operating description that every CERG team member, business sponsor, and adjacent function partner can use to understand how the function works and how to engage it.

### 1.1 Scope

This document applies to:

- The CERG function itself — Engineering, Risk, and Governance pillars under CISO authority
- The interfaces between CERG and adjacent security functions (Awareness, Incident Response), IT and OT delivery teams, business owners, and executive leadership
- The engagement models by which CERG is consumed: project delivery, continuous service, advisory, and program oversight
- The staffing roles within each pillar and the rules of engagement among them

### 1.2 Relationship to Other Documents

This document is referenced by every CERG standard, procedure, and plan. Where another document assigns work to "Engineering," "Risk," or "Governance," this document defines what those terms operationally mean.

---

## 2. Operating Premise

### 2.1 Why CERG Exists

The traditional separation of cybersecurity into siloed functions — operational security here, GRC over there, engineering security as a third team — produces a predictable failure pattern. Engineering is asked to deliver, then security reviews it after the fact and asks for changes that are now expensive. Risk identifies findings that have no clear path back into engineering planning. Governance writes policy that operators interpret variously, or not at all. Audits and incidents reveal the seams.

CERG consolidates the three core security activities — building secure systems, managing exposure, and governing the program — into one function with one authority. The pillars are distinct in skill set and discipline, but they operate as one team with one CISO and one set of priorities.

### 2.2 The Yes-And Default

> **Governance Does Not Exist to Block the Business**
>
> CERG's default orientation is to enable the business with guardrails, not to close doors. When a risk cannot be eliminated, it is documented, owned, treated, and monitored — not refused on principle. Reflexive denial is not a risk management strategy. The hard work is making "yes" safe; "no" is the easy answer, and the wrong one.

### 2.3 Three Pillars, One Team

CERG operates as one team. The pillars provide structure for skill development, work intake, and accountability — not boundaries to hide behind. Cross-pillar collaboration is the norm. Every Engineering review involves Risk perspective. Every Risk finding has a Governance disposition. Every Governance policy is validated for operational practicability by Engineering and Risk before publication.

---

## 3. The Three Pillars

### 3.1 Cyber Engineering

**Mandate.** Build secure systems by design. Embed security into architecture, configuration, and operational baselines before production. Be the technical security partner to project delivery.

**Core activities.**

- Pre-production security architecture review for all in-scope projects
- Reference architectures, landing zones, and configuration baselines per platform class
- Security infrastructure-as-code, policy-as-code, and admission control
- IT/OT convergence advisory and Electronic Security Perimeter design
- Identity platform engineering (IdP, MFA, SSO, PAM, secrets management)
- Cryptography and key management platform engineering
- Endpoint, server, container, and cloud security tooling engineering
- Operational handoff documentation that supports Governance compliance evidence

**Engagement default.** Project-aligned engagement. Engineering is engaged early in project planning and follows the work through go-live.

### 3.2 Cyber Risk

**Mandate.** Maintain continuous visibility into organizational exposure. Drive the work that reduces it. Test that controls hold up under attack.

**Core activities.**

- Vulnerability management (scanning, prioritization, remediation tracking) per **CERG-PRC-VM-001**
- Adversarial validation: penetration testing, red-team operations, purple-team detection validation
- Threat intelligence consumption and translation into detection and posture controls
- Vendor and third-party security risk assessment
- Cloud security posture management (CSPM) and SaaS security posture management (SSPM)
- Identity-threat detection and continuous identity-risk monitoring
- Risk-register intake from technical sources

**Engagement default.** Continuous service. Risk is always on; engagement is by exposure type, not by ticket.

### 3.3 Cyber Governance

**Mandate.** Own the policy library, the compliance posture, the risk register, and the evidence library. Translate regulation into actionable expectations. Coordinate regulator and auditor engagements.

**Core activities.**

- Policy, standards, and procedures library — including CERG-POL-001 and all subordinate documents
- Compliance program management: NERC-CIP, CMMC, SOX ITGC, and customer-contractual frameworks
- Risk register operation per **CERG-PRC-RM-001**
- Evidence library curation; production of audit and assessment evidence
- Regulator and assessor liaison
- Awareness program coordination (program ownership rests with a separate Awareness function; Governance coordinates content alignment)
- Incident response plan stewardship per **CERG-PLN-IR-001** (the IR capability itself is operated jointly with Risk; the plan and the regulatory clocks are Governance-owned)

**Engagement default.** Program oversight and advisory. Governance is engaged when policy interpretation, exception decisions, or regulatory implications enter the conversation.

### 3.4 What CERG Is Not Responsible For

The following functions are intentionally outside CERG and operate under separate charters:

- **Security Awareness program ownership.** A distinct function under CISO oversight, coordinated with Governance.
- **Incident Response operations.** The IR capability operates as a joint Risk + Governance + Engineering effort under CISO direction during active incidents; the standing function may be organizationally separate.
- **Physical Security (non-cyber).** Owned by Facilities; CERG coordinates for assets within CIP-006 / PE-family scope.
- **Privacy program.** A distinct function under Legal / Privacy leadership; coordinates with Governance for breach notification and Restricted-data handling.
- **Business Continuity (non-cyber).** Owned by Enterprise Risk / Operations; CERG coordinates for cyber-driven business continuity activations.

---

## 4. Authority, Reporting, and Decision Rights

### 4.1 Reporting Line

CERG reports to the CISO. The CISO reports per the organizational structure (typically to the CIO or directly to the CEO depending on org design) and has a defined reporting line to the board (Audit Committee, Risk Committee, or a dedicated Cyber/Technology Committee, per board protocol).

The three pillars report to the CISO through pillar leaders (Manager / Director / VP titles vary by organizational scale).

### 4.2 Decision Rights

| **Decision** | **Authority** |
|---|---|
| Policy approval (CERG-POL-001 and subordinate standards) | CISO |
| Standards / procedure approval | Pillar leader; CISO for material changes |
| Risk acceptance — Low / Medium | Per CERG-PRC-RM-001 §8 |
| Risk acceptance — High / Critical / Severe | CISO; Executive Sponsor / Board awareness for Critical+ |
| Exception approval | Per CERG-PRC-RM-001 §8 |
| Incident classification & containment | Incident Commander (CISO or designee) |
| External notification (regulator, public) | IC + CISO + Legal |
| Pre-production go/no-go for in-scope projects | Engineering pillar leader with Risk input; escalation to CISO if business and CERG disagree |
| Vendor onboarding approval (Tier 1) | Risk pillar leader; CISO for material risk exceptions |
| New SaaS / cloud service approval | Governance + Engineering; CISO for Restricted-data placements |
| Budget allocation across pillars | CISO |

### 4.3 Escalation Path

Disagreements that the pillars cannot resolve are escalated to the CISO. The CISO maintains a published escalation path that includes a stop-the-line capability for any CERG team member who believes a decision is being made that materially violates policy or creates regulatory exposure.

---

## 5. Engagement Models

CERG is consumed by the rest of the organization through four engagement models. Most major initiatives use more than one.

### 5.1 Project Engagement (Engineering-Led)

Used for new systems, major changes, and significant integrations.

| **Phase** | **CERG Activity** | **Lead Pillar** |
|---|---|---|
| Concept | Lightweight architectural consult; data classification and environment-tier discussion. | Engineering |
| Design | Formal security architecture review; reference-architecture / landing-zone selection; threat-model session for novel components. | Engineering (+ Risk for threat modeling) |
| Build | Engineering partner embedded with the project team; pipeline gates configured; identity / cryptography / monitoring requirements implemented. | Engineering |
| Pre-production | Pre-production security review; vulnerability assessment; pen-test where warranted; risk-register entries for any acceptance sought. | Engineering + Risk |
| Production | Handoff to operations; baselines committed; ongoing CSPM / SSPM coverage; vulnerability management onboarding. | Engineering → Risk |
| Continuous | Continuous monitoring; periodic re-review; governance evidence integration. | Risk + Governance |

### 5.2 Continuous Service (Risk-Led)

Used for ongoing exposure management across the entire estate.

- Vulnerability management operates as a standing service per CERG-PRC-VM-001.
- CSPM / SSPM operates continuously across approved cloud and SaaS.
- Threat intelligence consumption produces standing detection and posture work.
- Identity-threat detection operates continuously.

Continuous services do not require project tickets. Business teams are partners in remediation rather than initiators of the work.

### 5.3 Advisory (Cross-Pillar)

Used when a business unit, IT team, or OT team has a question, decision, or exploration that does not yet require a project.

- Architecture review office hours
- Cloud / SaaS service evaluation advisory
- M&A / divestiture cyber due diligence support
- Vendor selection advisory
- Policy interpretation advisory

Advisory engagements are intentionally low-friction. They are tracked at the activity level but not treated as a queued service.

### 5.4 Program Oversight (Governance-Led)

Used for regulatory programs, audits, exam cycles, and board reporting.

- NERC-CIP self-certification cycle and CIP-014 / CIP-013 program management
- CMMC pre-assessment and assessment management
- SOX ITGC evidence cycle (quarterly)
- Internal audit coordination
- Customer / partner assessment response

Program oversight engagements are time-bounded with defined entry, milestone, and exit criteria. They are led by Governance with Engineering and Risk supplying evidence and SMEs.

---

## 6. Staffing and Roles

CERG staffing is intentionally consistent across the pillars: a pillar leader, senior practitioners with platform / domain ownership, individual contributors who execute the standing work, and rotations or shared roles where the pillars converge.

The structure below is a pattern, not a fixed org chart. Smaller organizations consolidate roles; larger organizations expand them.

### 6.1 Cyber Engineering — Typical Roles

| **Role** | **Focus** |
|---|---|
| Engineering Pillar Leader | Pillar accountability; project intake; reference-architecture authority. |
| Cloud Security Engineer | Cloud platforms, landing zones, IaC, CSPM gating. |
| Identity Engineer | IdP, MFA, SSO, PAM, secrets management, federation. |
| OT Security Engineer | IT/OT convergence, ESP/EAP design, BES Cyber System baselines (see CERG-STD-OT-001). |
| Application / Product Security Engineer | SAST/DAST integration, SDLC controls, threat modeling. |
| Endpoint / Workplace Engineer | Endpoint controls, EDR engineering, OS baselines. |
| Cryptography Engineer | Key management, CA, TLS posture, FIPS compliance. |
| Pre-production Reviewer (often a rotated function) | Owns the pre-production checklist; signs off on go-live readiness. |

### 6.2 Cyber Risk — Typical Roles

| **Role** | **Focus** |
|---|---|
| Risk Pillar Leader | Pillar accountability; exposure posture reporting. |
| Vulnerability Management Lead | Operates CERG-PRC-VM-001; owns the SLAs and posture metrics. |
| Cloud Posture / Detection Engineer | CSPM / SSPM operations and detection rules. |
| Threat Intelligence Analyst | Source curation, internal advisories, detection translation. |
| Adversarial Testing Lead (Red Team) | Internal or partner-managed offensive validation. |
| Vendor / Third-Party Risk Analyst | Vendor assessment and continuous monitoring. |
| OT Risk Analyst | OT-safe vulnerability assessment; ICS threat intelligence. |
| Identity Risk Analyst | UEBA, identity-threat detection, OAuth / token risk. |

### 6.3 Cyber Governance — Typical Roles

| **Role** | **Focus** |
|---|---|
| Governance Pillar Leader | Pillar accountability; regulator and auditor liaison; CISO reporting. |
| NERC-CIP Compliance Manager | OT/BES compliance posture (see CERG-STD-OT-001). |
| CMMC / Federal Compliance Manager | CUI posture (see CERG-STD-CUI-001). |
| SOX ITGC Lead | ITGC control evidence and audit coordination. |
| Policy & Standards Manager | Document library curation; review cycles. |
| Risk Register Manager | Operates CERG-PRC-RM-001; curates the register. |
| Evidence Librarian | Maintains the cross-framework evidence library. |
| IR Plan Steward | Maintains CERG-PLN-IR-001; coordinates exercises and notification clocks. |

### 6.4 Shared and Rotational Roles

Several roles intentionally sit between pillars and rotate:

- **Architecture Review Office Hours.** Engineering + Risk on rotation.
- **Incident Response on-call.** Risk-led with Engineering and Governance rotational coverage.
- **Audit liaison.** Governance-led with Engineering and Risk SMEs.

---

## 7. Coordination Cadence

CERG operates as one team because it talks like one team. The standing cadence below is the minimum; teams add working sessions as needed.

| **Forum** | **Cadence** | **Participants** | **Purpose** |
|---|---|---|---|
| CERG Leadership Sync | Weekly | CISO + pillar leaders | Cross-pillar priorities, blockers, escalations. |
| Risk Posture Review | Weekly | Risk + Engineering + Governance | Top-of-list risks, treatment progress, SLA breaches. |
| Pre-production Review Board | Twice weekly | Engineering + Risk + Governance | Pre-production go/no-go for in-scope projects. |
| Vulnerability Triage | Daily / standing | Risk team + Engineering rep | KEV / Critical / Internet-exposed findings. |
| Incident Response on-call rotation | 24/7 | Per IR plan | Active and standing incident readiness. |
| Threat Intelligence Brief | Weekly | Risk + Engineering + Governance | Relevant intel, posture implications. |
| Compliance Pulse | Bi-weekly | Governance + Engineering + Risk | Open compliance items, evidence gaps, regulator calendar. |
| CERG All-Hands | Monthly | All CERG | Program updates, recognition, knowledge sharing. |
| CISO Risk & Posture Review | Quarterly | CISO + leadership | Material risks, posture trends, regulatory cycle, budget. |
| Board Cyber Brief | Quarterly (per board protocol) | CISO → Audit / Risk / Tech Committee | Posture, material incidents, top risks, program initiatives. |

---

## 8. Interfaces With Other Functions

CERG operates inside a broader organizational ecosystem. The following interfaces are explicit.

| **Function** | **Interface** |
|---|---|
| **Incident Response (operational capability)** | Activated under the IC per CERG-PLN-IR-001; CERG provides Lead Investigator, Engineering Lead, and Governance Lead roles. |
| **Security Awareness** | Coordinated with Governance for content alignment; CERG provides phishing simulation operations through Risk. |
| **Internal Audit** | Receives evidence from Governance; engages SMEs from Engineering and Risk; findings tracked in the risk register. |
| **Legal / Privacy** | Engaged at activation for Sev 1/2 incidents; engaged for regulatory interpretation, breach notification, customer contractual obligations, and privilege judgments. |
| **Privacy / DPO** | Coordinates with Governance on Restricted-data handling and breach notification under GDPR / HIPAA / state laws. |
| **Enterprise Risk Management** | Receives quarterly cyber risk feed; interface ensures cyber risks are visible in enterprise risk reporting. |
| **Internal Communications / PR** | Engaged for material incident communications and major program announcements. |
| **Procurement / Vendor Management** | Coordinates third-party assessments and DFARS / CMMC flow-down; Governance is the security signatory. |
| **Human Resources** | Coordinates joiner / mover / leaver, personnel risk assessments (NERC-CIP CIP-004), and disciplinary referrals for willful non-compliance. |
| **IT Operations** | Executes Engineering-designed controls; jointly owns endpoint, server, network, and SaaS administration. |
| **OT Operations** | Co-owns CIP-008 incident response, CIP-007 patching cycles, and ESP/EAP architecture. CERG defers to operations on grid-impact judgments. |
| **Business Unit Owners** | Sponsor systems, approve treatments, own residual risk for systems in scope. |
| **Executive Leadership and the Board** | Receive standing CISO reporting; engaged on Sev 1 incidents and material risk decisions. |

---

## 9. RACI Patterns

The following patterns illustrate how the pillars typically distribute work. Specific RACI matrices are maintained per process. This is a sample — each standard and procedure cited in CERG-POL-001 §10 has its own.

### 9.1 New Cloud Workload Goes Live

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Approve architecture and landing-zone selection | **R / A** | C | C | C | I |
| Implement IAM, network, monitoring controls | **R** | C | I | C | I |
| Pre-production vulnerability assessment | C | **R / A** | I | C | I |
| Approve go-live | C | C | C | **A** | I |
| Onboard to CSPM and vulnerability management | C | **R / A** | I | I | I |
| Add to compliance evidence library | C | I | **R / A** | I | I |

### 9.2 Open High Vulnerability Past SLA

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Identify SLA breach and escalate | I | **R / A** | I | I | I |
| Recommend compensating controls | **R / A** | C | C | C | I |
| Decide treatment (remediate / mitigate / accept) | C | C | C | **A** | I (review for High+) |
| Approve risk acceptance (if High) | I | C | C | C | **A** |
| Record in risk register | I | C | **R / A** | I | I |

### 9.3 CMMC Pre-Assessment Cycle

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Maintain SSP and POA&M | C | C | **R / A** | I | I |
| Conduct self-assessment | C | **R** | **A** | C | I |
| Submit SPRS score | I | C | **R / A** | I | I |
| C3PAO engagement | I | C | **R / A** | I | **C** |
| Remediate POA&M items | **R** | C | A | **C** | I |

---

## 10. Maturity, Metrics, and the Adaptive Target

### 10.1 The Adaptive Target

CERG targets NIST Cybersecurity Framework **Tier 4 — Adaptive** posture for the organization. Adaptive does not mean "constantly changing." It means the organization understands its risk environment, continuously adjusts its program based on what it learns, integrates cybersecurity into enterprise risk and business decisions, and treats lessons learned as a first-class input to the program.

### 10.2 Maturity Indicators

The following indicators are tracked by Governance and reported to the CISO and board. They are leading indicators of program maturity, not lagging measures of incident counts.

| **Indicator** | **What It Measures** |
|---|---|
| % of in-scope assets in real-time inventory | Visibility |
| % of new projects passing pre-production review on first attempt | Engineering quality and "shift left" effectiveness |
| Median time-to-remediate by severity | Risk responsiveness |
| % of findings within SLA | Risk discipline |
| Open exception count and median age | Governance discipline |
| % of risks reviewed within scheduled review date | Risk register health |
| % of identified high risks with active treatment plans | Treatment discipline |
| Time from incident detection to containment (Sev 1/2) | Response capability |
| % of IRT roles backstopped (no single point of failure) | Continuity |
| Audit / assessor findings (count and severity) per cycle | External validation |
| Phishing simulation susceptibility trend | Workforce posture |
| % of vendor reassessments current | Third-party risk discipline |

### 10.3 Continuous Improvement

Every CERG activity produces feedback into the program backlog:

- Post-incident lessons → Engineering, Risk, Governance backlog items
- Audit findings → POA&M / risk register entries with treatment plans
- Exercise results → Plan and playbook updates
- Adversarial validation findings → Detection rules, posture controls, architectural changes
- Threat intelligence → Standing detection and control updates

The backlog is reviewed monthly. Items that age beyond planned dates without justification are flagged to the CISO.

---

## 11. Operating Model Control

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 DRAFT | 2026 | CISO + Cyber Governance | Initial release |

### Review Triggers

This operating model shall be reviewed annually and upon any of the following:

- Material organizational change affecting CERG structure or reporting
- Material change to scope (e.g., new regulated environment, major M&A)
- A Sev 1 incident or significant audit finding that reveals a structural gap
- CISO transition
- Direction from executive leadership or the board

The CISO owns this document. Cyber Governance maintains it on behalf of the CISO. Changes require CISO approval and broad CERG acknowledgment.

### Related Documents

The authoritative inventory is `CERG-GOV-CAT-001`. The references below are the V1 library at a glance, grouped by role within the operating model.

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | CERG-POL-001 | Parent policy — defines the CERG operating model at the principle level |
| Document Catalog and Naming Convention | CERG-GOV-CAT-001 | Authoritative inventory of every CERG artifact |
| Unified Control Baseline | CERG-GOV-CB-001 | Control spine, overlays, evidence mapping |
| Metrics, Dashboard, and CISO/Board Reporting | CERG-GOV-MTR-001 | KRIs, KPIs, CISO dashboard |
| Risk Management Framework | CERG_RMF_v1.0 | Lifecycle and KRI definitions |
| Compliance Matrix | CERG Compliance Matrix | Cross-regulator control intent alignment |
| Risk Taxonomy | CERG Risk Taxonomy | Risk language and categorization |
| Grid Control Systems Security Standard | CERG-STD-OT-001 | OT pillar adaptations |
| IT (Hosted/Cl