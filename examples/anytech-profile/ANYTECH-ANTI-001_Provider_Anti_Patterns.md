## PROVIDER ANTI-PATTERNS — AnyTech Adaptation
### Vendor-Oversight Failure Modes · Observable Symptoms · Corrective Actions

---

| | |
|---|---|
| **Artifact ID** | ANYTECH-ANTI-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Classification** | Public |
| **Owner** | Risk Pillar Lead (AnyTech) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) — Cybersecurity Policy (AnyTech) |
| **Supporting Documents** | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) · [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) · [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) · [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) · [CERG Anti-Pattern Catalog](../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md) |
| **Review Cycle** | Quarterly / On material adoption feedback |
| **Frameworks** | NIST CSF 2.0 (GOVERN) |
| **Environments** | AnyTech vendor-oversight model |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How to Use This Catalog](#2-how-to-use-this-catalog)
3. [Anti-Pattern Index](#3-anti-pattern-index)
4. [Provider Oversight Anti-Patterns](#4-provider-oversight-anti-patterns)
5. [Provider RACI Anti-Patterns](#5-provider-raci-anti-patterns)
6. [Provider Relationship Anti-Patterns](#6-provider-relationship-anti-patterns)
7. [Provider Transition Anti-Patterns](#7-provider-transition-anti-patterns)
8. [Using These Anti-Patterns in Quarterly Review](#8-using-these-anti-patterns-in-quarterly-review)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

The upstream [CERG Anti-Pattern Catalog](../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md) covers 35 cross-domain failure modes. This catalog is a supplement specific to the vendor-oversight model. It focuses on patterns that emerge when a small security team relies on external providers for most operational capabilities.

These anti-patterns are not theoretical. They are the predictable failure modes of a program office model and will appear if not actively managed.

An anti-pattern is included when it meets three tests:

1. It is common enough that AnyTech is likely to encounter it.
2. It creates operational risk, governance confusion, or false confidence.
3. It has a practical correction available inside the AnyTech adaptation.

---

## 2. How to Use This Catalog

Use this catalog during quarterly provider reviews, transition planning, and lessons learned.

- **Engineering Lead** uses it to challenge MSSP performance reporting.
- **Risk Lead** uses it to identify provider-driven risk register entries.
- **Governance Lead** uses it to assess evidence quality.
- **IT Director** uses it to ask sharp questions during quarterly reviews.
- **All CERG** use it to detect drift before it becomes a material gap.

---

## 3. Anti-Pattern Index

| ID | Anti-Pattern | Domain | Observable Symptom | Corrective Anchor |
|---|---|---|---|---|
| ANPV-001 | MSSP as Black Box | Provider Oversight | Provider treated as sealed unit; no validation of triage or SLA compliance | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) |
| ANPV-002 | Questionnaire-as-Due-Diligence | Provider Oversight | 300-question assessment replaces understanding the provider's actual operating model | [TPRM Procedure](CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md) |
| ANPV-003 | Contract-as-Control | Provider Oversight | SLA language treated as proof of operating capability without measurement | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §5 |
| ANPV-004 | Validation by Assumption | Provider Oversight | CERG asserts oversight but has no evidence access or review cadence | [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) §5 |
| ANPV-005 | Sampling Drift | Provider Oversight | Same alerts, same engineers, same time of day sampled every week | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §10 |
| ANPV-006 | SLA Report Reliance | Provider Oversight | Provider self-reports SLA compliance without independent validation | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §6 |
| ANPV-007 | Provider RACI Drift | RACI | Provider scope changed but RACI was never updated | [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) §6 |
| ANPV-008 | Orphaned Ownership | RACI | Capability has a provider (D) but no CERG validator (V) | [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) §7 |
| ANPV-009 | Provider-to-Provider Gap | RACI | MSSP and MSP each think the other owns a shared capability | [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) §7 |
| ANPV-010 | Relationship Capture | Relationship | CERG engineer becomes friendly with provider analysts and stops challenging | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §10 |
| ANPV-011 | Review Theater | Relationship | Quarterly review is a slide show with no decisions, no score, no change | [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) |
| ANPV-012 | Past-Peak Dependency | Relationship | Provider's best people were on the account at contract signing; now second-string | [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) §3.2 |
| ANPV-013 | Transition Dread | Transition | Provider issues deliberately ignored because the thought of switching is overwhelming | [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) |
| ANPV-014 | Cutover Impatience | Transition | Provider transition is rushed; parallel run is shortened or skipped | [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) §3 |
| ANPV-015 | Coverage Atrophy | Transition | Asset inventory grows but provider coverage list does not | [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §3.1 |

---

## 4. Provider Oversight Anti-Patterns

### 4.1 ANPV-001 — MSSP as Black Box

(Extended from the upstream [ANTI-VEND-001](../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md))

AnyTech-specific variant: The 3-person Engineering team is too busy with other work to validate MSSP delivery. Alerts get reviewed only when there's a problem. The MSSP operates without meaningful oversight for weeks or months at a time.

**Corrective action:** The 4-hour-per-week allocation in the [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) is a minimum, not a target. If engineers are too busy for it, reduce other scope, not MSSP validation. Escalate capacity constraints to the IT Director.

### 4.2 ANPV-002 — Questionnaire-as-Due-Diligence

(Extended from the upstream [ANTI-VEND-002](../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md))

AnyTech-specific variant: Due diligence on a new MSSP or MSP consists of reviewing their SOC 2 Type II report and a completed questionnaire. No operational evidence is sampled. No exercise is conducted. The assumption is that a certified provider will perform.

**Corrective action:** Treat SOC 2 and questionnaires as prerequisites, not sufficient evidence. Require an operational assessment during the parallel run period before cutover. See [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) §3.

### 4.3 ANPV-003 — Contract-as-Control

(Extended from the upstream [ANTI-VEND-003](../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md))

AnyTech-specific variant: The MSSP contract says "15-minute response time for critical alerts," and that language is used as the answer when IT Director asks about detection capability. No one measures actual response times.

**Corrective action:** Every SLA term must have a corresponding measurement in the [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §5. The Quarterly Review must include actual vs. contractual SLA comparison.

### 4.4 ANPV-004 — Validation by Assumption

**What it looks like:** CERG's Provider RACI says "V" (validates) for a capability, but there is no defined validation method, evidence access, or review cadence. Everyone assumes validation is happening, but nothing is being checked.

**Why it fails:** A "V" in the RACI without a validation procedure is a governance illusion. The capability looks covered but is unsupervised. The provider knows they are not being validated, and quality drifts accordingly.

**Corrective action:** Every "V" in the Provider RACI must have a documented validation method, evidence source, and review cadence. Use the [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) as the template for validation procedure design. If a validation method cannot be defined, the capability cannot be scored as validated.

### 4.5 ANPV-005 — Sampling Drift

**What it looks like:** Every alert quality sample reviews the same shift (day shift, weekdays), the same engineer's alerts, or the same alert types. The sample becomes representative of the provider's best work, not their average work.

**Why it fails:** Sampling that does not rotate across shifts, teams, and alert types creates a blind spot. The overnight shift, weekend analysts, and new hires may produce lower-quality triage that is never measured.

**Corrective action:** Rotate sample selection across shifts, analysts, and alert types. Periodically sample alerts from nights, weekends, and holidays. The [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §3.2 provides the methodology.

### 4.6 ANPV-006 — SLA Report Reliance

**What it looks like:** CERG relies on the MSSP's self-reported SLA compliance report without independent validation. The report shows 98% compliance, but nobody has checked whether the timestamps in the report match actual notification receipts.

**Why it fails:** Self-reported SLA data is a metric designed to look good. It may use different measurement methodology than the contract defines, exclude certain alert types, or adjust timestamps.

**Corrective action:** Spot-check SLA compliance independently at least once per quarter. Compare the MSSP's reported timestamps against AnyTech's notification receipt timestamps for a sample of 10 alerts. Discrepancies of more than 5 minutes should be investigated.

---

## 5. Provider RACI Anti-Patterns

### 5.1 ANPV-007 — Provider RACI Drift

**What it looks like:** The RACI was correct when the contract was signed, but the provider's scope has expanded or contracted since then. New systems were added, alert categories changed, or the provider began offering a new service. The RACI was never updated.

**Why it fails:** An outdated RACI is worse than no RACI — it creates a false sense of clarity. When an incident hits, nobody can agree on who owns what.

**Corrective action:** Review the Provider RACI quarterly against the current contract. If the provider's scope has changed, update the RACI before the next review. Use the RACI change management process in [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md) §6.

### 5.2 ANPV-008 — Orphaned Ownership

**What it looks like:** A capability has a provider in the "D" (Delivers) role but no CERG role in the "V" (Validates) column. The capability is delivered but unvalidated.

**Why it fails:** Without validation, the team cannot distinguish between a capability that is operating and one that exists only on paper. The gap is invisible until an incident or audit.

**Corrective action:** Every "D" in the Provider RACI must have a corresponding "V." If the team lacks capacity to validate a capability, either reduce provider scope or escalate for additional capacity. Document the gap in the risk register.

### 5.3 ANPV-009 — Provider-to-Provider Gap

**What it looks like:** MSSP and MSP each assume the other owns endpoint detection coverage. The MSSP assumes the MSP manages endpoint agents; the MSP assumes the MSSP deploys its own agents. Neither is doing it.

**Why it fails:** In vendor-oversight models, providers do not naturally coordinate. Each performs their contracted scope and assumes the other handles the shared boundaries. The gaps are where incidents happen.

**Corrective action:** Map provider-to-provider handoffs explicitly in the [Provider RACI](ANYTECH-RACI-001_Provider_RACI_Extension.md). Test each handoff in a joint exercise annually. If the handoff involves a shared system or shared data, document which provider is responsible for which part.

---

## 6. Provider Relationship Anti-Patterns

### 6.1 ANPV-010 — Relationship Capture

**What it looks like:** The CERG Detection Engineer has worked with the same MSSP analysts for two years. They are on friendly terms. The engineer stops challenging alert quality scores because it feels personal. The scores drift upward.

**Why it fails:** Social relationships with provider staff are natural and valuable — they improve communication during incidents. But they also create unconscious bias in validation. The validator becomes reluctant to flag issues because it feels like criticizing a colleague.

**Corrective action:** Rotate the primary validator every 12 months. The second engineer should periodically shadow the sampling process and produce an independent score for comparison. If there is a consistent gap between the primary and shadow scores, investigate.

### 6.2 ANPV-011 — Review Theater

**What it looks like:** The quarterly provider review is a slide show. The provider presents metrics, CERG asks polite questions, and everyone leaves without decisions. No scorecard is produced. No action items are assigned. The review is treated as a relationship meeting rather than a governance meeting.

**Why it fails:** A review that does not produce decisions is not a review; it is a social visit. The provider interprets the lack of challenge as satisfaction. AnyTech misses the opportunity to correct drift early.

**Corrective action:** Follow the structured agenda in the [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) §4. Every review must produce a scorecard, at least one decision, and action items with owners and due dates. If a review produces none of these, the Governance Lead is responsible for escalating to the IT Director.

### 6.3 ANPV-012 — Past-Peak Dependency

**What it looks like:** The provider's best people were on the account at contract signing — the senior engineer, the experienced incident commander, the architect who designed the monitoring setup. Two years later, those people have been promoted, transferred, or left. The account is now staffed with junior analysts. The SLA reports still look good, but depth of experience is gone.

**Why it fails:** Provider staffing is not static, but contracts rarely require key-person retention beyond an initial period. The team loses institutional knowledge about AnyTech's environment. Response quality declines gradually, so it is hard to detect in any single review.

**Corrective action:** Request provider personnel changes as a standing agenda item in the [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) §3.2. Track cumulative experience on the account (total years of AnyTech-specific experience across the team). If cumulative experience drops below a threshold, discuss in the quarterly review and consider contractual key-person requirements in the next renewal.

---

## 7. Provider Transition Anti-Patterns

### 7.1 ANPV-013 — Transition Dread

**What it looks like:** Provider performance has been declining for two quarters. The scorecard is consistently yellow. Improvement plans are not working. But the thought of running a provider transition — the parallel run, the knowledge transfer, the risk — feels overwhelming. So the team stays with the underperforming provider.

**Why it fails:** Transition dread is an understandable human response, but it is a risk management failure. Every quarter the underperforming provider stays, the organization accumulates risk. By the time the team is forced to transition (e.g., provider acquisition, contract termination), the transition is more expensive and more rushed.

**Corrective action:** Use the transition decision thresholds in the [Quarterly Review Kit](ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md) §5. If the scorecard triggers "Orange" or "Red," the transition evaluation process starts automatically — it is not optional. The [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) makes the process predictable and reduces the fear of the unknown.

### 7.2 ANPV-014 — Cutover Impatience

**What it looks like:** The parallel run is going well. The new provider is performing. The team is eager to cut over and be done. The parallel run period is shortened from the planned 4 weeks to 2 weeks. The new provider becomes primary before critical fatigue has been tested — how does the SOC perform during a 3 AM incident on a Saturday?

**Why it fails:** A parallel run that looks good during business hours on weekdays may not reveal gaps in overnight coverage, weekend staffing, or sustained fatigue during a multi-day incident. Cutting the parallel run short is the most common cause of post-transition discovery of provider gaps.

**Corrective action:** The parallel run period has a minimum duration defined in the [Vendor Transition Playbook](ANYTECH-TRANS-001_Vendor_Transition_Playbook.md) §3. The IT Director must approve any reduction. Post-transition validation (§9) fills the remaining gaps, but the parallel run is the only time the two providers can be compared directly.

### 7.3 ANPV-015 — Coverage Atrophy

**What it looks like:** AnyTech's asset inventory grows over time — new systems, new cloud accounts, new environments. The provider's detection coverage map, last reviewed 18 months ago, covers only the original scope. New systems are not being monitored, and no one has noticed.

**Why it fails:** Coverage atrophy is a silent failure. The provider does not know about new systems unless told. The CERG team assumes new systems are covered because the provider has general monitoring. There is no monthly cross-reference between asset inventory and detection coverage.

**Corrective action:** The [MSSP Engagement Playbook](ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md) §3.1 requires a monthly detection coverage cross-reference. The Infrastructure Engineer maintains a current asset inventory and compares it against the MSSP's coverage map. Any gaps are added to the risk register.

---

## 8. Using These Anti-Patterns in Quarterly Review

During each quarterly review, the Risk Lead presents the anti-pattern assessment:

1. Which anti-patterns are currently present in AnyTech's operating model?
2. Which anti-patterns were present last quarter and are still present?
3. What corrective action was taken, and what is the status?

The same tracking table applies as in the upstream catalog:

| Field | Description |
|---|---|
| Anti-pattern ID | The catalog ID, e.g., ANPV-001 |
| Affected capability or workflow | The capability, procedure, or provider relationship where the pattern appears |
| Evidence observed | What shows the pattern is present |
| Risk created | The operational or governance risk the pattern creates |
| Corrective action | The specific change to procedure, RACI, contract, or cadence |
| Owner and due date | Named owner and target closure |
| Tracking record | Risk register entry or Program Improvement Register item |

---

## 9. Document Control

| Field | Value |
|---|---|
| **Artifact ID** | ANYTECH-ANTI-001 |
| **Version** | 1.0 |
| **Status** | Active |
| **Effective Date** | 2026-06-27 |
| **Classification** | Public |
| **Owner** | Risk Pillar Lead (AnyTech) |
| **Approved By** | Risk Pillar Lead |
| **Review Cycle** | Quarterly / On material adoption feedback |
| **Next Scheduled Review** | 2026-09-27 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-27 | Risk Pillar Lead | Initial release. Establishes 15 vendor-oversight-specific anti-patterns across provider oversight, RACI, relationship, and transition domains for the AnyTech adaptation. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| CERG Anti-Pattern Catalog | `../../governance/CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md` | Upstream cross-domain anti-pattern catalog |
| MSSP Engagement Playbook | `ANYTECH-MSSP-001_MSSP_Engagement_Playbook.md` | Validation methodology and sampling procedures |
| Provider RACI Extension | `ANYTECH-RACI-001_Provider_RACI_Extension.md` | RACI change management and ownership mapping |
| Quarterly Review Kit | `ANYTECH-REVIEW-001_Quarterly_Provider_Review_Kit.md` | Review scoring and anti-pattern assessment |
| Vendor Transition Playbook | `ANYTECH-TRANS-001_Vendor_Transition_Playbook.md` | Transition procedures and rollback criteria |
| TPRM Procedure (AnyTech) | `CERG-PRC-TPRM-001_Third_Party_Risk_Procedure_AnyTech.md` | Vendor tiering and assessment |

---
