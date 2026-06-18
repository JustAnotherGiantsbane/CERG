# Story 10: The new CISO's first 90 days

This story is for the CISO, the incoming security leader, or the executive sponsor trying to understand what good adoption looks like at the program level. It is a narrative arc, not a single event. It walks day 1 through day 90 of a new CISO inheriting a fragmented program and bringing it onto CERG Standard.

For the underlying checklists that anchor this arc, see [CERG-GOV-IMP-006 §3](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md#3-ciso-or-security-lead-checklist). For the consolidation and pacing logic, see [CERG-GOV-IMP-005](../../governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md).

## Setting

Meridian Analytics is a 180-person B2B SaaS company selling a customer data platform to mid-market and enterprise customers. The platform processes customer behavioral data, integrates with major CRMs and marketing tools, and runs as a multi-tenant cloud service. Meridian holds a SOC 2 Type II report that is up for renewal in six months. Three enterprise customers have audits queued in the next 90 days.

The previous CISO left two months ago. Since then, the CEO Jordan has been "covering it" with help from an outside vCISO who works four hours a week. There is a folder of policy documents from 2022 that have not been updated. There is a spreadsheet called "security risks" with 14 rows, none of which have owners. There is a vulnerability scanner running weekly against the production cloud tenant, but findings go into an email thread that no one closes. There is no risk register. There is no evidence library. There is no decision log. There is no documented owner for anything.

Priya Anand starts on a Monday. She has held CISO roles at two smaller SaaS companies and has been a deputy CISO at a larger one. She has read CERG before, ran a CERG Lite adoption at her last company, and has chosen Meridian specifically because the board has committed to a real program.

This is the story of her first 90 days.

## Day 1-7: Arrival and the first 48 hours

Priya arrives at 9 a.m. on Monday. Her first meeting is with Jordan at 9:30. By 10 a.m. she has:

- Confirmed Jordan will be the Executive Sponsor (per IMP-006 §3.1, first row).
- Asked for the names of the Engineering, Risk, and Governance interim owners. Jordan names Tomás (Engineering Manager, has been running the production cloud), Sara (Director of Trust, has been running SOC 2 and customer audits), and himself as Governance until Priya hires.
- Asked for the vCISO's notes. There are none worth keeping.
- Scheduled a Tuesday afternoon meeting with Tomás, Sara, and the Head of Sales (because the enterprise audits will land first).

By Tuesday at 5 p.m., Priya has filled in [CERG-GOV-VAR-001](../../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) with Meridian's profile: 180 people, B2B SaaS, SOC 2 + customer-driven regulatory scope, cloud-only, no OT, no CUI. She has picked CERG Standard as the adoption path (IMP-005 §3) because Meridian has an existing engineering team and existing customer audits. She has created the [Role Assignment Map](../../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) per IMP-003 §5 Record 2. She has approved a shared Google Drive as the temporary evidence store (per IMP-006 §3.1, last row) because Meridian does not yet have a GRC platform.

By Friday she has the first 10 records seeded (per IMP-003 §5). The most important is Record 4: the initial top 10 risks. She writes those herself over Wednesday and Thursday. The list looks like this:

| # | Risk | Owner | Treatment |
|---|------|-------|-----------|
| 1 | SOC 2 Type II renewal in 6 months with no evidence library | Sara | Build evidence library by month 2 |
| 2 | Three enterprise customer audits queued with no response template | Sara | Build audit response template by month 1 |
| 3 | Vulnerability scanner findings not being closed | Tomás | Triage this week, fix process within 30 days |
| 4 | No documented access review cadence | Tomás | Implement quarterly cadence by month 2 |
| 5 | Vendor risk assessments not performed on three critical SaaS dependencies | Sara | Complete assessments by month 3 |
| 6 | No incident response plan or IR owner | Priya | Name IR owner, adopt IR Plan by month 1 |
| 7 | Board has not received a security update in 4 months | Priya | First board update at next board meeting |
| 8 | No documented data classification | Sara | Adopt DG standard by month 2 |
| 9 | Engineering security reviews happening informally | Tomás | Adopt Architecture Review procedure by month 2 |
| 10 | No metrics dashboard | Priya | First metrics report by month 2 |

This list becomes Priya's first 90 days. It is the risk register's seed content.

## Day 8-30: First monthly review

By the second Monday, the rhythm starts. The team adopts the IMP-003 weekly 1-hour cadence for a Standard team of Meridian's size (4 people: Priya, Tomás, Sara, plus an Engineering security engineer Devin who joins in week 2).

Week 2: Priya runs the first weekly meeting. Tomás walks the vulnerability scanner backlog. There are 23 findings, 2 Critical, 5 High. The Criticals are both on the production API tier. Tomás opens Change Records for both and schedules maintenance windows. By Friday both are remediated. The weekly cadence absorbed a Critical without a single ad hoc meeting.

Week 3: Sara delivers the audit response template. The template maps a customer audit request to the relevant CERG artifact, identifies the evidence owner, and sets a 10-business-day response clock. This becomes the basis for the three queued audits.

Week 4: Priya signs the [Cybersecurity Policy](../../governance/CERG-POL-001_Cybersecurity_Policy.md). It is the first authoritative artifact Meridian has had in two years. The board ratifies it at the next board meeting (which happens to be in week 4).

End of month 1 deliverables:

- Approved Cybersecurity Policy
- First 10 risks in the register with owners
- Risk appetite defaults approved (Priya proposed, board ratified)
- Cyber Oversight Group formed (Priya chairs, Tomás and Sara attend, vCISO joins as observer)
- First exposure backlog reviewed (the 23 scanner findings are now 6 open, all triaged)
- Exception and risk acceptance authority mapped (Priya for High and Critical, Sara for Medium with Priya notification)
- 30-day improvement backlog seeded

Priya logs every decision in the Decision Log per IMP-002 §4. The log is a simple spreadsheet. It has 11 entries at the end of month 1.

## Day 31-60: First quarterly review prep and first audit

Week 5 starts with the first exposure cycle closing out. The 6 open findings from month 1 are down to 2, both Medium, both with planned remediation windows. The scanner schedule moves from weekly to biweekly because the backlog is now stable.

Week 6: Priya runs the first formal audit response. An enterprise customer sends a 47-question security questionnaire with a 10-business-day clock. Sara uses the audit response template. The questionnaire maps to 12 CERG artifacts (Policy, Operating Model, RMF, Access Standard, Logging Standard, TPRM Procedure, and others). Sara pulls each from the evidence library, attaches the relevant evidence, and routes the response through Priya for sign-off. The response goes out on day 8 with 2 questions marked "evidence pending - response by day 12." The customer accepts the response without follow-up.

Week 7-8: Sara runs the first three vendor risk assessments on critical SaaS dependencies. The vendor assessments use [CERG-PRC-TPRM-001](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) and [CERG-TMPL-TPRM-001](../../templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md). Two vendors pass on first assessment. One vendor returns incomplete answers and is given a 30-day remediation window with an Exception Record.

End of month 2 deliverables:

- First metrics dashboard. Three metrics: open Critical/High findings, exceptions expiring in 30 days, vendor assessments current. All three are green.
- First board update. Priya presents the metrics dashboard, the top 10 risks, and the SOC 2 readiness status to the board. The board approves the next quarter's hiring plan: one additional Engineering security engineer and one Risk analyst.
- First risk acceptance memo. Tomás and Sara identify one Medium-risk decision (deferring a configuration baseline update until next quarter) and route it through Priya for acceptance. The memo has a named owner, an expiration date, and a remediation plan.

## Day 61-90: First audit lands, first exception, first quarterly review

Week 9: A SOC 2 readiness assessment (pre-audit gap analysis by an external firm) lands. The firm identifies 12 gaps across 8 control families. Each gap becomes a Finding Record. Each Finding Record has an owner (Sara or Tomás), a remediation deadline, and an evidence plan. None of the 12 gaps are Critical SLA. All are Medium or Low with 90-day windows. The quarterly SOC 2 audit is in 5 months; this is the work that closes the gaps.

Week 10: An enterprise customer's auditor requests live evidence of a quarterly access review for a Meridian system. Meridian has not been running quarterly access reviews (Risk #4 from day 7). Tomás runs an out-of-cycle review to satisfy the auditor. The review identifies 4 stale privileged accounts and 1 contractor account whose engagement ended 6 weeks ago. Engineering removes all 5. Priya opens an Exception Record with a 60-day expiration noting that the next scheduled quarterly review will happen on time. The auditor accepts the response.

Week 11-12: Priya runs the first quarterly review per IMP-003's quarterly half-day cadence. The review covers:

- Control evidence refresh (3 control families: Access, Logging, Asset Management)
- Lessons learned from the SOC 2 readiness findings and the customer audit
- Open high risks review
- Expired exceptions review
- Improvement backlog review

The quarterly review produces 5 new entries in the Program Improvement Register. None of them are "patch faster." They are systemic improvements: implement automated access review tooling, integrate vulnerability scanner with ticketing, define the Security Reviewer role in the Architecture Review procedure, add board pack insert for quarterly metrics, formalize the vCISO engagement scope.

End of month 3 deliverables (matches IMP-006 §3.3):

- First metrics dashboard reviewed by the CISO and approved for ongoing use.
- Control implementation snapshot reviewed. Of the 22 CERG control intents in [CB-001](../../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md), Meridian now has authoritative evidence for 14 and is working evidence plans for the remaining 8.
- Adoption expansion decision. The board approves expanding to CERG Regulated overlay for [CERG-PLN-SOX-001](../../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) readiness, even though Meridian is not yet SOX-relevant, because the next enterprise customer audit will require it.
- Open high risks reviewed. 2 of the original 10 are closed. 8 remain, all with owners and dates.
- Expired exceptions reviewed. The one exception from week 10 has a renewal decision: extend 60 days because the automated access review tool will not be live for another 60 days.
- Resourcing decisions approved. One Engineering security engineer and one Risk analyst hired, starting in month 4.

## What this story shows

The first 90 days of a CERG Standard adoption do not look like a "project." They look like a rhythm:

- Weekly 1-hour cadence absorbing Criticals without ad hoc meetings
- Monthly 2-hour cadence absorbing regulatory and audit work
- Quarterly half-day cadence producing systemic improvement

The CISO does not deliver the program. The CISO convenes it. The CISO's job in the first 90 days is to:

1. Get the Executive Sponsor named and the Role Assignment Map populated (week 1).
2. Seed the first 10 records so the program has something to operate on (week 2-3).
3. Sign the Cybersecurity Policy (week 4).
4. Run the weekly cadence every week without fail (weeks 2-12).
5. Run the first monthly review (week 4).
6. Run the first quarterly review (week 12).
7. Surface one Decision Log entry per material decision.
8. Produce one metrics dashboard for the board before the board asks.

By day 90, Meridian has 5 authoritative CERG artifacts (Policy, RMF, Operating Model, Risk Register, Document Catalog), 3 standards adopted (Access, Logging, Asset Management), 4 procedures in operation (Risk Register, TPRM, Architecture Review, Access Management Runbook), 12 records in the evidence library, 23 Decision Log entries, and one quarterly metrics report. The team has remediated 21 findings, opened 1 exception, filed 1 risk acceptance memo, and passed one customer audit without follow-up.

The SOC 2 Type II renewal in month 7 is now a finishing exercise, not a panic.

## What this story does not cover

- **A real incident.** The first 90 days did not include a declared incident. If one had, it would have triggered F-06 and the standing IR team. See Story 6 for the third-party incident pattern and the IR handoff.
- **A major regulator-driven control change.** The first 90 days did not include an external regulatory obligation. When the SOC 2 framework updated or a new customer required NIS2 alignment, Story 9's F-01 pattern would apply.
- **CERG Lite.** Meridian is a Standard team. See Story 8 for the small-team pattern.

For the CISO checklist that anchors this arc, see [CERG-GOV-IMP-006 §3](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md#3-ciso-or-security-lead-checklist). For the First 90-Day Completion Criteria, see [CERG-GOV-IMP-006 §8](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md#8-first-90-day-completion-criteria). For the role assignment map pattern, see [CERG-GOV-IMP-003 §4](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#4-role-consolidation-map). For the Decision Log requirement, see [CERG-GOV-IMP-002 §4](../../governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md#4-the-decision-log).
