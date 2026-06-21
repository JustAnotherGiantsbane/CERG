## EXPOSURE MANAGEMENT PROCEDURE — AnyTech Adaptation
### Provider Oversight Model · 6-Step Exposure Loop · Patch Hygiene Oversight

---

| | |
|---|---|
| **Document ID** | CERG-PRC-VM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Internal |
| **Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On major provider change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech in-scope environments |

---

## Table of Contents

1. [Purpose and Philosophy](#1-purpose-and-philosophy)
2. [The Exposure State Model](#2-the-exposure-state-model)
3. [Roles and Responsibilities — AnyTech Specific](#3-roles-and-responsibilities--anytech-specific)
4. [Step 1 — Collect Observations](#4-step-1--collect-observations)
5. [Step 2 — Validate Asset and Condition](#5-step-2--validate-asset-and-condition)
6. [Step 3 — Validate Exposure Path](#6-step-3--validate-exposure-path)
7. [Step 4 — Classify](#7-step-4--classify)
8. [Step 5 — Select Treatment](#8-step-5--select-treatment)
9. [Step 6 — Verify Closure](#9-step-6--verify-closure)
10. [Patch Hygiene (Oversight Model)](#10-patch-hygiene-oversight-model)
11. [Risk Acceptance and Exceptions](#11-risk-acceptance-and-exceptions)
12. [Reporting and Metrics for IT Director](#12-reporting-and-metrics-for-it-director)
13. [Procedure Control](#13-procedure-control)

---

## 1. Purpose and Philosophy

This procedure establishes AnyTech's exposure management program — adapted from the CERG 6-step exposure model for an organisation where the CERG team operates as a cyber program office that oversees contracted providers rather than running security tools directly.

### 1.1 The Operating Premise

> **A scanner report tells the MSP what to patch. The exposure program tells us whether the MSP is actually closing exposure paths.**
>
> AnyTech does not operate a vulnerability scanner, does not deploy patches, and does not run its own SOC. The CERG cyber team (8 people) manages a federation of providers: an MSP that handles IT operations including patching, endpoint management, and asset management, and an MSSP that handles SOC monitoring, detection, and response.
>
> The exposure management program therefore does not start with "deploy scanner, find vulnerabilities, assign SLA, patch." It starts with the question: *How do we maintain visibility into what is vulnerable when we do not run the tools?* The answer is an oversight architecture: CERG identifies and classifies exposures from provider-sourced data, tickets the MSP for remediation, and tasks the MSSP with confirming closure through monitoring telemetry.

The operating premise for AnyTech is that **visibility is the program.** If CERG cannot see what is vulnerable across MSP-managed assets, it cannot prioritise, cannot hold the MSP accountable, and cannot report posture to the IT Director.

### 1.2 What This Procedure Adapts

This document adapts [CERG-PRC-VM-001](../../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) for AnyTech's provider-federation model. The core 6-step exposure model (Collect → Validate Asset → Validate Path → Classify → Treat → Verify) is preserved. The following changes are structural:

| Original Assumption | AnyTech Adaptation |
|---------------------|--------------------|
| Security team runs vulnerability scanners | MSP runs scanners; CERG receives exports |
| Security team deploys patches | MSP deploys patches per their SLA |
| Security team verifies closure via re-scan | MSSP confirms closure via monitoring telemetry |
| CISO is acceptance authority | IT Director is acceptance authority |
| Adversarial validation by internal team | MSSP handles adversarial testing per contract |
| OT-specific regulatory overlays | Not applicable to AnyTech's current scope |
| CVSS-driven priority | Exposure path + asset criticality + KEV drive priority (same as original model) |

### 1.3 Scope

This procedure governs all in-scope AnyTech environments — enterprise IT, cloud, SaaS — where the MSP manages assets and the MSSP monitors for threats. AnyTech does not currently operate OT environments, handle CUI, or operate under regulatory regimes (NERC-CIP, CMMC, SOX, FedRAMP). If AnyTech's regulatory scope changes, this procedure shall be reviewed and adapted accordingly.

---

## 2. The Exposure State Model

Every observation moves through a defined state pipeline. The states are identical to the original CERG model; what changes is **who provides the evidence** for each transition.

### 2.1 State Definitions

| State | Definition | Evidence Source at AnyTech |
|-------|-----------|---------------------------|
| **Observed** | A tool-reported condition. No validation has occurred. | MSP vulnerability scanner export, MSSP threat intel feed, CERG manual finding, external advisory |
| **Validated** | The asset is confirmed real, in scope, and the affected software is present. | CERG Risk Analyst + MSP asset owner confirmation |
| **Reachability Assessed** | The exposure path has been evaluated. | CERG + MSSP monitoring data (is the service reachable? Is it being probed?) |
| **Exposure Confirmed** | A reachable, useful exploitation path exists. | CERG classification decision |
| **Treatment Selected** | A specific treatment has been chosen and assigned. | CERG tickets MSP for remediation; or CERG routes to exception/acceptance |
| **Closure Verified** | The treatment has been applied and independently verified. | MSP provides patching evidence; MSSP confirms via monitoring telemetry |

### 2.2 The Provider Loop

The exposure state model at AnyTech operates as a **closed-loop provider oversight system**:

```
MSP Scan Data ──→ CERG Identifies/Classifies ──→ CERG Tickets MSP
                                                       │
                                                       ▼
                                              MSP Remediation
                                                       │
                                                       ▼
                                        MSSP Monitoring Confirms Closure
                                                       │
                                                       ▼
                                              CERG Verifies & Closes
```

Each transition between states is gated by evidence from a **different provider** than the one performing the action:

| Transition | Action By | Evidence By |
|------------|-----------|-------------|
| Observed → Validated | CERG Risk Analyst | MSP asset owner confirms asset scope and existence |
| Validated → Reachability Assessed | CERG Risk Analyst | MSSP monitoring data on network reachability |
| Reachability Assessed → Exposure Confirmed | CERG Risk Analyst | CERG analysis (internal) |
| Exposure Confirmed → Treatment Selected | CERG Risk Analyst | CERG tickets MSP |
| Treatment Selected → Closure Verified | CERG Risk Analyst | MSP provides patch evidence; MSSP confirms closure via telemetry |

This **separation of duties** prevents the MSP from being the sole arbiter of whether a vulnerability has been resolved.

### 2.3 The Apache Example (AnyTech Context)

> An MSP scan report shows Apache CVE-2024-XXXX (CVSS 9.9) on host `web-07`. CERG cannot simply forward the scan report to the MSP and call it done. CERG must:
>
> 1. Confirm that `web-07` is still an active, in-scope asset (MSP asset owner confirms).
> 2. Determine whether Apache is actually running and reachable (MSSP monitoring data helps here).
> 3. If the path is real and reachable, classify the exposure and ticket the MSP for remediation.
> 4. After the MSP reports patching complete, ask the MSSP to confirm via monitoring telemetry that the service is no longer exploitable.
> 5. CERG verifies both sources of evidence and closes the finding.
>
> Without Steps 1 and 2, CERG would be forwarding raw scanner noise to the MSP. Without Step 4, CERG would rely on the MSP's self-attestation — which is the same entity that missed the vulnerability in the first place.

---

## 3. Roles and Responsibilities — AnyTech Specific

### 3.1 CERG Cyber Team (8-Person Program Office)

| Role | Exposure Management Responsibility |
|------|-----------------------------------|
| **Risk Pillar Leader** | Owns this procedure. Operates observation collection, triage, classification, and tracking. Reviews MSSP threat intel. Validates MSP remediation evidence. Escalates exposure findings to IT Director. Maintains the exposure backlog. |
| **Cyber Risk Analyst(s)** | Score exposures, manage the risk register link, track SLAs, validate asset and condition with MSP asset owners, ticket MSP for remediation. Daily triage of incoming observations. |
| **Engineering Pillar Leader** | Reviews MSP remediation evidence for technical completeness. Escalates recurring technical failures. Maintains asset inventory jointly with MSP. Provides technical input on compensating controls. |
| **Governance Pillar Leader** | Ensures evidence from providers is collected and retained. Manages the exception process. Tracks SLA compliance. Prepares monthly exposure summary for IT Director. Ensures provider contracts require the evidence this procedure depends on. |
| **Evidence / SLA Manager** | Collects MSP patch reports, MSSP closure confirmations, and exposure backlog data. Produces monthly SLA compliance dashboards. Supports quarterly provider business reviews. |

### 3.2 External Providers

| Provider | Role in Exposure Management |
|----------|----------------------------|
| **MSP** (IT Operations) | Patches systems per SLA. Manages endpoint security tools. Provides patching status reports and vulnerability scanner exports. Confirms asset inventory and scope. Executes remediation actions as ticketed by CERG. The MSP runs the vulnerability scanner; CERG receives the data. |
| **MSSP** (SOC / Detection & Response) | Monitors for exploitation attempts against AnyTech assets. Confirms exposure closure via monitoring telemetry. Provides threat intelligence feed. Conducts adversarial testing per contract scope. Reports active exploitation attempts that may indicate vulnerability discovery. |

### 3.3 Acceptance Authority

| Role | Authority |
|------|-----------|
| **IT Director** | Final acceptance authority for all exposure-related risk acceptances (any severity). Approves exceptions and accepts residual risk. Receives the monthly 1-page exposure summary. No CISO exists at AnyTech; the IT Director is the most senior cyber decision-maker. |

---

## 4. Step 1 — Collect Observations

Observations arrive from multiple sources. At AnyTech, the observation pipeline is populated **primarily from provider data** rather than from internally operated tools.

### 4.1 Observation Sources

| Source | Description | Delivered By |
|--------|-------------|--------------|
| MSP vulnerability scanner exports | Authenticated and unauthenticated scans of MSP-managed servers, endpoints, network devices, and cloud workloads | MSP (scheduled export, minimum weekly) |
| MSSP threat intelligence feed | CVEs, KEV matches, active exploitation signals, and emerging threats relevant to AnyTech's technology stack | MSSP (continuous feed, daily summary) |
| CERG manual findings | Observations from internal reviews, architecture assessments, project intake reviews, or incident post-mortems | CERG cyber team (as discovered) |
| External threat intel | Vendor advisories, CISA alerts, ISAC feeds, public disclosure notifications | CERG Risk Analyst (monitoring) |
| Provider incident reports | Vulnerabilities discovered during incident response or forensic investigation | MSSP (per incident) |
| End-of-support notifications | MSP identifies assets approaching or past vendor end-of-support | MSP (quarterly report) |

### 4.2 What CERG Does NOT Collect From

At AnyTech, CERG does not operate:
- An internal vulnerability scanner
- A container/image registry scanner
- A CSPM or SSPM console
- A SAST/DAST tool
- A bug bounty program

These capabilities are provided by the MSP (scanning, CSPM where contracted) or the MSSP (application testing where contracted), or are not applicable to AnyTech's current operating context (bug bounty, SCA).

### 4.3 Observation Intake

All observations enter the pipeline with:
- Source provider and contact
- Asset identifier (MSP asset tag)
- Raw severity/score as reported
- Timestamp of observation
- CERG tracking ID

No SLA clock starts at intake. The clock starts at classification (Step 4).

---

## 5. Step 2 — Validate Asset and Condition

Before asking "is this dangerous," ask "is this real?" At AnyTech, this step requires coordination with the MSP, who owns the asset inventory.

### 5.1 Validation Criteria

| Question | Owner | Action if No |
|----------|-------|-------------|
| Is the asset in the MSP's authoritative inventory? | CERG Risk Analyst + MSP asset owner | Escalate to MSP asset management team; hold observation until resolved |
| Is the asset in scope for AnyTech exposure management? | CERG Risk Analyst | Close as out-of-scope with rationale |
| Is the reported software/service/configuration present on the asset? | MSP asset owner (CERG asks, MSP confirms via remote access or tooling) | Close as scanner artifact; document rationale |
| Is the reported version accurate? (Check for backported fixes) | MSP engineering | Adjust version; re-evaluate |

### 5.2 MSP Asset Inventory Dependency

CERG cannot validate assets without a current, accurate asset inventory from the MSP. The MSP is contractually required to maintain and provide:

- A complete asset inventory (hardware, software, cloud resources) updated at least weekly
- Asset ownership attribution (who owns/operates each asset)
- Asset criticality classification (Crown Jewel, Critical, Standard, Test/Dev)
- Asset in-scope status (production vs. non-production, AnyTech-owned vs. contractor-provided)

CERG performs a **quarterly asset inventory validation** — picking a sample of 20 assets from the MSP inventory and independently verifying their existence, operating system, and installed software. Discrepancies are escalated to the Engineering Pillar Leader and the MSP account manager.

### 5.3 Validation Timing

| Observation Signal | Validation Required Within |
|--------------------|---------------------------|
| KEV-listed or actively exploited (reported by MSSP) | 4 hours |
| CVSS >= 9.0 or Critical MSSP alert | 24 hours |
| CVSS 7.0–8.9 | 3 business days |
| CVSS < 7.0 | 5 business days |

---

## 6. Step 3 — Validate Exposure Path

A validated condition is not automatically an exposure. This step asks: **can an attacker actually reach this?** At AnyTech, the MSSP's monitoring telemetry is a primary source of reachability evidence.

### 6.1 Exposure Path Assessment

| Question | Evidence Source at AnyTech |
|----------|---------------------------|
| Is the service running? | MSP confirms via endpoint management tooling |
| Is it reachable from the Internet? | MSSP external attack surface monitoring |
| Is it reachable from internal user populations? | MSSP network telemetry, firewall log review |
| Is authentication required? | MSP configuration evidence |
| Is the asset segmented? | MSP network diagram, firewall rule review |
| Is there a compensating control? | MSP endpoint protection status, MSSP detection rule coverage |
| Has active exploitation been observed? | MSSP SOC escalation |

### 6.2 KEV Acceleration

If the observation matches a CISA Known Exploited Vulnerabilities (KEV) entry **and** the MSSP has observed active scanning or exploitation attempts against AnyTech's environment, the exposure path assessment is accelerated to **4 hours** regardless of CVSS score.

### 6.3 The "Not Reachable" Decision

If CERG determines the exposure path is not reachable (service not running, blocked at firewall, compensated), the finding may be:

- **Closed** with documented rationale (not reachable, not exploitable)
- **Reclassified as Hygiene Debt** (weakness exists but no reachable path — track in patch hygiene)

Both decisions require CERG Risk Analyst sign-off and are documented in the exposure backlog.

---

## 7. Step 4 — Classify

After validation and reachability assessment, every observation is classified into exactly one category. Classification drives treatment priority and SLA. The classification taxonomy is identical to the original CERG model.

### 7.1 Classification Taxonomy

| Classification | Definition | Treatment Approach | SLA Driver |
|---------------|-----------|-------------------|------------|
| **Non-issue / Scanner Artifact** | The observation does not represent a real condition (backported fix, version-only match, scanner error) | Close with evidence | N/A |
| **Hygiene Debt** | A real weakness exists but no reachable exposure path has been confirmed | Track; address in patch cycle | Patch hygiene cadence |
| **Confirmed Flaw, Not Currently Exposed** | The flaw exists on a reachable asset but a compensating control blocks exploitation | Monitor control; plan remediation | Next maintenance window |
| **Confirmed Exposure** | A reachable, exploitable path exists | Treat per SLA | Severity-tiered SLA (see §7.2) |
| **Material Risk** | Confirmed exposure on a crown jewel or actively exploited | Emergency treatment | PPR tier |

### 7.2 Treatment SLAs

SLAs are measured from classification to verified closure. These apply to the **MSP remediation timeline** as tracked by CERG.

| Classification | Context | SLA |
|---------------|---------|-----|
| **Material Risk — PPR** | KEV-listed, active exploitation, or crown-jewel exposure | **48 hours** (Internet-facing) / **72 hours** (internal) |
| **Confirmed Exposure — Critical** | Internet-reachable, no compensating control | **14 days** |
| **Confirmed Exposure — High** | Internal reachable, or Internet-reachable with limited impact | **30 days** |
| **Confirmed Exposure — Medium** | Limited reachability or impact | **60 days** |
| **Confirmed Flaw, Not Exposed** | Compensated or segmented | **90 days** (align with maintenance) |
| **Hygiene Debt** | No confirmed exposure path | Per patch hygiene cadence (§10) |

> **Note on Critical SLA:** The original CERG model uses 3 days for Critical exposures. AnyTech uses 14 days to align with the MSP's standard patching SLA for critical-severity patches. If faster remediation is required (KEV, active exploitation, crown jewel), the finding is classified as Material Risk — PPR, not Critical.

### 7.3 Recurring Failures

If the same observation type (same CVE, same configuration issue, same asset class) appears more than twice in a rolling 90-day window, CERG escalates to the Engineering Pillar Leader for root-cause review. The goal is to identify whether the MSP has a systemic gap (e.g., a recurring missed patch, a configuration drift pattern) rather than a one-time miss.

---

## 8. Step 5 — Select Treatment

Treatment is chosen based on the most effective path to close confirmed exposure. At AnyTech, the **default treatment is CERG tickets the MSP for remediation**. Other options exist when patching is not feasible.

### 8.1 Treatment Options

| Treatment | When to Use | Who Executes | CERG Action |
|-----------|------------|--------------|-------------|
| **Ticket MSP for patching** | Default for any Confirmed Exposure where a vendor fix exists | MSP | Create ticket with finding details, asset, SLA deadline, and evidence of exposure |
| **Block path** | The exposure is reachable but the service must stay (firewall rule, ACL) | MSP (network team) | CERG validates block is in place via MSSP telemetry |
| **Change configuration** | A config change eliminates the exposure without a patch | MSP | CERG validates configuration change evidence |
| **Add compensating control** | Patching is not feasible (end-of-support, vendor delay) | MSP (with CERG technical input) | CERG validates compensating control is effective and documented |
| **Accept residual risk** | Treatment is infeasible or disproportionate | IT Director (approves) | CERG prepares risk acceptance package (§11) |
| **Remove service** | The vulnerable component is not needed | MSP (with business owner approval) | CERG verifies service is decommissioned |

### 8.2 How CERG Tickets the MSP

When CERG classifies an observation as Confirmed Exposure, the CERG Risk Analyst:

1. Creates a ticket in the shared CERG-MSP ticketing system with:
   - Observation ID, asset identifier, CVE/vulnerability reference
   - Classification and SLA deadline
   - Exposure path evidence (reachability assessment)
   - Required remediation action
2. Assigns the ticket to the MSP remediation queue
3. Sets the SLA timer

The MSP acknowledges the ticket within **4 business hours** for Material Risk / Critical exposures, or **1 business day** for all others.

### 8.3 When the MSP Cannot Remediate

If the MSP reports that remediation is not feasible within the SLA (e.g., vendor has not released a patch, asset is end-of-support, operational constraints), CERG has three options:

1. **Escalate to Engineering Pillar Leader** — may identify a compensating control or configuration change that closes the exposure without a patch.
2. **Route to exception process** (§11) — if no technical workaround exists and the exposure cannot be accepted, an exception is raised to the IT Director.
3. **Accept residual risk** — if the exposure is low-severity or compensated, the IT Director may accept the residual risk.

---

## 9. Step 6 — Verify Closure

A treatment is not complete until independently verified. At AnyTech, verification involves **two independent sources**: the MSP (who performed the remediation) and the MSSP (who confirms via monitoring telemetry).

### 9.1 Verification Flow

```
MSP reports remediation complete
        │
        ▼
CERG asks MSP for evidence of patching
        │
        ▼
MSP provides: patch confirmation, scan re-check, screenshot, or tool status
        │
        ▼
CERG asks MSSP to confirm via monitoring telemetry
        │
        ▼
MSSP confirms: service version changed, vulnerability no longer detectable, or exploitation path closed
        │
        ▼
CERG verifies both evidence sources and closes the finding
```

### 9.2 Verification Methods

| Method | When Required | Provider Responsible |
|--------|--------------|---------------------|
| MSP-provided patch confirmation | All Confirmed Exposures (Critical, High, Medium) | MSP |
| MSP re-scan screenshot or export | Material Risk — PPR and Critical exposures | MSP |
| MSSP monitoring telemetry confirmation | All Confirmed Exposures | MSSP |
| Configuration change evidence | Configuration changes, blocking rules | MSP |
| Reachability test | When treatment was "block path" | MSSP |
| Compensating control validation | When treatment involved compensating controls | CERG + MSP |

### 9.3 Verification Timing

- MSP must provide remediation evidence within **3 business days** of reporting completion.
- MSSP must provide telemetry confirmation within **2 business days** of CERG's request.
- CERG must close or escalate the finding within **5 business days** of receiving all evidence.
- Unverified treatments are treated as **open exposures** and count toward SLA breach metrics.

### 9.4 Reopening and Escalation

If the MSSP cannot confirm closure (e.g., the service still shows the vulnerable version, the exploitation path is still open), CERG:

1. **Reopens** the finding with a notation of the MSSP's finding
2. **Escalates** to the Engineering Pillar Leader and the MSP account manager
3. **Escalates the SLA breach** — the original SLA timer continues; the MSP is considered to have missed the deadline

---

## 10. Patch Hygiene (Oversight Model)

Patch hygiene at AnyTech is the **MSP's operational responsibility**. CERG does not patch systems. CERG exercises **oversight** — tracking whether the MSP is meeting its patching SLAs, identifying recurring failures, and conducting independent sample verification.

### 10.1 MSP Responsibility

The MSP is contractually obligated to maintain a patch management program that includes:

- Monthly Patch Tuesday deployment for Windows systems (within 14 days of release)
- Monthly Linux patching (within 30 days of release)
- Critical out-of-band patches deployed within 48 hours of vendor release
- Network device patching per vendor advisory (assessed quarterly)
- Endpoint protection signature updates (daily, automated)
- Cloud PaaS managed service currency (provider-managed; verified monthly)

The MSP maintains its own patching tooling (WSUS, SCCM, or equivalent). CERG does not have direct access to these tools — CERG receives **reports and exports** from the MSP.

### 10.2 CERG Oversight Responsibilities

CERG tracks the following from MSP-provided data:

| Metric | Definition | Source | Cadence |
|--------|-----------|--------|---------|
| Patching cadence compliance | % of assets patched within the platform-class window | MSP patch report | Monthly |
| SLA compliance by severity | % of exposure tickets closed within SLA | CERG exposure backlog | Monthly |
| Recurring failures | Assets or CVE patterns appearing more than twice in 90 days | CERG exposure backlog | Monthly |
| End-of-support count | Assets running software past vendor end-of-support | MSP quarterly report | Quarterly |

### 10.3 Monthly MSP Patch Report Review

Each month, the MSP delivers a patch compliance report to CERG covering:

- Percentage of assets patched within window, by platform class
- List of assets that missed the patching window and rationale
- Outstanding critical/security patches not yet deployed
- End-of-support items and remediation plan status

CERG reviews the report and **flags deviations**:

- Any platform class below **95% patch currency** triggers a review with the MSP account manager
- Any asset missing more than two consecutive patch cycles triggers a CERG escalation to the Engineering Pillar Leader
- Any exposure-critical patch not deployed within SLA triggers an escalation to the IT Director

### 10.4 Quarterly Sample-Based Patch Verification

Once per quarter, CERG conducts an **independent patch verification**:

1. CERG selects **10 critical systems** from the asset inventory (crown jewels, Internet-facing systems, systems with Restricted data).
2. CERG requests direct evidence from the MSP for each selected system — current patch level, installed software versions, and last patch date.
3. CERG cross-references this evidence against the MSP's patch compliance report.
4. If all 10 systems match the reported state, the quarter is considered verified.
5. If **any** system shows a discrepancy (unreported missing patch, incorrect version), CERG expands the sample to 20 systems. If discrepancies persist, CERG escalates to the IT Director and triggers a contractual review with the MSP.

### 10.5 Hygiene Debt Tracking

Observations classified as Hygiene Debt (§7.1) are tracked separately from Confirmed Exposures. They are reported to the MSP as a patching backlog item — not as an SLA-bound exposure. Hygiene Debt items are reviewed quarterly:

- If a Hygiene Debt item remains unresolved for more than **two quarter-ends**, CERG re-evaluates whether a compensating control or exception is required.
- If a Hygiene Debt item becomes reachable (network change, service enabled, control removed), it is automatically promoted to Confirmed Exposure and routed through the standard 6-step model.

---

## 11. Risk Acceptance and Exceptions

### 11.1 Policy Exception vs. Risk Acceptance

These are different paths at AnyTech, just as in the original CERG model.

| Scenario | Type | Path |
|----------|------|------|
| "This system cannot be patched because the vendor has not released a fix" | Risk | Risk acceptance via IT Director |
| "This system is intentionally running an older OS version due to application compatibility" | Policy exception | Governance-owned exception workflow |
| "We will isolate the system, monitor all sessions, and retire by Q4" | Treatment | MSP executes; CERG tracks |
| "The IT Director accepts the residual risk until the asset is decommissioned" | Business risk acceptance | IT Director approves |

### 11.2 Risk Acceptance Process

When a Confirmed Exposure cannot be remediated within the SLA, and no technical workaround (compensating control, configuration change, path block) exists, CERG prepares a risk acceptance package for the IT Director.

The package must include:

1. **Observation identifier**, asset, environment, and classification
2. **Reason** treatment is not feasible within SLA (vendor delay, end-of-support, operational constraint)
3. **Compensating controls** in place — even if partial, document what exists (e.g., network isolation, monitoring coverage, reduced user access)
4. **MSSP assessment** — is the MSSP able to detect exploitation of this vulnerability? What is the estimated detection time?
5. **Risk owner** — who in the business accepts accountability for the residual exposure
6. **Expiration date** — when the acceptance must be reviewed or a final remediation date
7. **Re-evaluation triggers** — what events would force re-evaluation (patch release, CVSS change, KEV listing, MSSP detects exploitation)

### 11.3 Approval Authority

| Severity | Approver |
|----------|----------|
| Material Risk — PPR | **IT Director** (mandatory; cannot be delegated) |
| Confirmed Exposure — Critical | **IT Director** |
| Confirmed Exposure — High | **Risk Pillar Leader** |
| Confirmed Exposure — Medium or Low | **Risk Pillar Leader** (documented in risk register) |

The IT Director is the final risk acceptance authority at AnyTech. There is no CISO role. The IT Director may not delegate PPR-tier acceptance decisions.

### 11.4 Exception Process

When a policy or control baseline deviation is required (not a risk acceptance, but an intentional deviation from a security standard), the Governance Pillar Leader manages the exception workflow per [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

### 11.5 Acceptance Register

All risk acceptances and exceptions are recorded in the risk register with:
- Unique ID, date, and expiration
- Asset and observation reference
- Compensating controls and validation evidence
- Approver and date of approval
- Review schedule and review outcomes

The Governance Pillar Leader maintains this register.

---

## 12. Reporting and Metrics for IT Director

CERG reports exposure posture to the IT Director monthly. The goal is **one page** that tells the IT Director what is exposed, whether the MSP is closing exposures on time, and whether the trend is improving or deteriorating.

### 12.1 Monthly 1-Page Exposure Summary

| Section | Content |
|---------|---------|
| **Total Open Exposures** | Count of findings in state "Exposure Confirmed" or "Material Risk" — broken out by severity (PPR, Critical, High, Medium) |
| **Critical Count** | Count of Critical + Material Risk exposures, with a clear "Red/Yellow/Green" indicator |
| **SLA Compliance %** | Percentage of exposure tickets this month closed within SLA, overall and by severity |
| **SLA Misses Detail** | List of exposures past SLA — asset, age, reason, escalation status |
| **Improvement / Decline Trend** | Month-over-month change in total open exposures and SLA compliance (arrows: ↑ improving, → stable, ↓ declining) |
| **KEV / Active Threat** | Any KEV-matched observations or MSSP-reported active exploitation attempts relevant to AnyTech's stack |
| **Patch Hygiene Overview** | MSP patch currency rate by platform class, flagged deviations, quarterly verification status |
| **Risk Acceptances** | Count of active risk acceptances, newly accepted, expired, or breached |

### 12.2 Exposure Management Metrics

| ID | Metric | Definition | G / A / R |
|----|--------|-----------|-----------|
| EM-001 | Confirmed Reachable Critical Exposure | Count of exposures in "Exposure Confirmed" state with Critical/PPR classification AND Internet-facing reachability | 0 / 1–2 / > 2 |
| EM-002 | Observations Not Yet Triaged | Count of observations in "Observed" state past validation SLA (≤5% / 6–15% / >15%) | ≤ 5% / 6–15% / > 15% |
| EM-003 | KEV with Reachable Path | Count of KEV-matched observations in "Exposure Confirmed" or "Material Risk" state | 0 / 1–2 / > 2 |
| EM-004 | Exposures on Crown Jewels | Count of confirmed exposures on crown-jewel-classified assets | 0 / 1 / > 1 |
| EM-005 | SLA Misses with No Controls | Exposures past SLA with no compensating control | 0 / 1 / > 1 |
| EM-006 | Median Time: Observation to Classification | Median days from observation intake to classification | ≤ 3d / 4–7d / > 7d |
| EM-007 | MSP Ticket Closure Rate | % of MSP remediation tickets closed within SLA this month | ≥ 95% / 85–94% / < 85% |
| EM-008 | Quarterly Verification Pass Rate | % of sampled systems passing independent patch verification | 100% / 90–99% / < 90% |

### 12.3 Patch Hygiene Metrics (Reported Separately)

| ID | Metric | Definition | G / A / R |
|----|--------|-----------|-----------|
| PH-001 | MSP Patch Currency Rate | % of MSP-managed assets within platform-class patch cadence window | ≥ 95% / 85–94% / < 85% |
| PH-002 | Hygiene Debt Count | Number of observations classified as Hygiene Debt | Trend; no control target |
| PH-003 | End-of-Support Count | Assets running software past vendor end-of-support | 0 / 1–5 / > 5 |

### 12.4 Escalation Triggers

Immediate escalation to IT Director:

- **Active exploitation observed** against an AnyTech in-scope asset (MSSP reports)
- **Any PPR-tier exposure** open beyond its SLA
- **A Critical exposure** open beyond SLA with no compensating control
- **Quarterly verification** finds >1 system with unreported patch status
- **MSP SLA compliance** drops below 85% for two consecutive months

### 12.5 Reporting Cadence

| Report | Audience | Cadence |
|--------|----------|---------|
| Exposure summary (1-page) | IT Director | Monthly |
| Observation triage backlog | Risk Pillar Leader | Weekly |
| MSP remediation ticket queue | CERG Risk Analyst + MSP | Weekly |
| Patch hygiene dashboard | Engineering Pillar Leader | Monthly |
| Provider SLA performance | Governance Pillar Leader | Monthly |
| Quarterly patch verification report | IT Director + MSP account manager | Quarterly |
| Annual exposure posture summary | IT Director | Annually |

---

## 13. Procedure Control

| | |
|---|---|
| **Document ID** | CERG-PRC-VM-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Internal |
| **Owner** | Risk Pillar Leader (AnyTech CERG) |
| **Approved By** | IT Director (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On major provider change |
| **Next Scheduled Review** | 2027-06-21 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-21 | Risk Pillar Leader (AnyTech CERG) | Initial AnyTech Adaptation. Adapted 6-step exposure model for provider-federation (MSP patches, MSSP confirms). Replaced internal scanning with provider-sourced observations. Added oversight-focused patch hygiene model with quarterly sample verification. Removed OT, CUI, adversarial validation sections. Adapted roles for 8-person program office. Established IT Director as acceptance authority. Created monthly 1-page reporting template. |

### Review Triggers

This procedure shall be reviewed annually and upon any of the following:

- Material change to the MSP or MSSP relationship (scope change, contract renegotiation, provider change).
- Addition of a regulatory regime to AnyTech scope (e.g., if AnyTech becomes subject to NERC-CIP, CMMC, SOX, or similar).
- Significant security incident involving unremediated exposure that reveals gaps in this procedure.
- IT Director transition.
- Change in CERG team structure or size that affects exposure management capacity.
- Direction from AnyTech IT Director or executive leadership.

The Risk Pillar Leader owns this document. Changes require IT Director approval.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Parent policy — defines the CERG operating model at the principle level |
| Operating Model (AnyTech Adaptation) | [CERG-GOV-OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Defines the provider engagement model, SLA framework, RACI patterns, and pillar structure |
| Risk Register and Exception Process | [CERG-PRC-RM-001](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk acceptance and exception workflow |
| Third-Party and Supply Chain Risk Procedure (AnyTech Adaptation) | [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) | Provider oversight, vendor tiering, MSSP/MSP-specific processes |
| Threat Intelligence Procedure | [CERG-PRC-TI-001](../../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Intel consumption process; feed sourced from MSSP |
| Audit and Evidence Management Procedure | [CERG-PRC-AUD-001](../../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Evidence collection procedure; applies to provider evidence |
| Metrics Dashboard and Reporting | [CERG-GOV-MTR-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | EM and PH metrics definitions |
| Document Catalog and Naming Convention | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Authoritative inventory of every CERG artifact |
| Unified Control Baseline | [CERG-GOV-CB-001](.. (deferred - see CAT-001)) | Control spine for mapping provider-delivered controls |

---

> _A scanner report tells the MSP what to patch. The exposure program tells us whether the MSP is actually closing exposure paths._

---

*End of Document — CERG-PRC-VM-001 (AnyTech Adaptation)*