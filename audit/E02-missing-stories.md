# Task E02 Output: Identify missing operational stories

## Scope Reviewed
- Files read:
  - `audit/E01-example-quality.md`
  - `examples/day-in-the-life/README.md`
  - `examples/day-in-the-life/story-8-cerg-lite-maria.md`
  - `examples/day-in-the-life/story-9-f-01-control-intent.md`
  - `examples/day-in-the-life/story-10-new-ciso-90-days.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - Supporting documents previously read in E01/D03 for story-gap context: `PRC-AR`, `PRC-VM`, `PRC-RM`, `PRC-AUD`, `PRC-IR`, `PLN-IR`, `PRC-TPRM`, `FRM-002`, and `IMP-007`.
- Sections reviewed:
  - E01 scorecard, keep/rewrite recommendations, and story-quality findings.
  - Day-in-the-life story index and Stories 1-10.
  - FLOW-001 flow definitions F-01 through F-07, record definitions, operating principles, and state models.
- Files intentionally not reviewed:
  - Every source procedure in full. E02 is a narrative coverage audit, not a second execution-chain audit.
  - Full source rewrite plans. E03 will convert underperforming-story findings into edit instructions.

## Method
- Steps performed:
  1. Mapped each existing story to primary and secondary flows F-01 through F-07.
  2. Mapped each story to the dominant pillar, supporting pillars, and major role families.
  3. Compared coverage to the candidate missing-story list in `/workspace/thebigone.md`.
  4. Rejected candidate stories where an existing story can be expanded or repaired instead of adding a new narrative.
  5. Proposed only the smallest set of new examples needed to clarify gaps that are not currently taught well.
- Search terms or scripts used:
  - Reused E01 search inventory for story references.
  - Manual mapping from story flow declarations and walkthrough tables.
- Assumptions avoided:
  - Did not recommend a new story just because a topic is important. If an existing story can carry the teaching point with a small rewrite, E02 marks it as expansion rather than new-story need.
  - Did not treat every flow as requiring exactly one standalone story. Some stories legitimately cover multiple flows.
  - Did not treat examples as source-of-authority documents; stories teach source rules but do not create them.

## Existing Story-to-Flow Coverage Map

| Flow | Current coverage | Existing stories | Coverage assessment |
|---|---|---|---|
| F-01 Control Intent to Implementation | Strong | Story 9 | Excellent standalone coverage. No new F-01 story needed. |
| F-02 Project Intake, Architecture Review, and Threat Modeling | Strong for intake/design; weak for pre-production/handoff | Stories 1, 4, 7 | Intake, SaaS, cloud, and AI are covered. Phase 4/5 pre-production, handoff, and go-live evidence closure are not taught well. |
| F-03 Asset Registration and Coverage Validation | Moderate | Story 4, Story 10 | Story 4 includes asset registration, but coverage validation is secondary. Adequate for now; no standalone F-03 story needed unless future reader testing fails. |
| F-04 Finding to Remediation, Exception, or Residual Risk | Strong for vulnerability/access; weak for formal business acceptance and OT windowing | Stories 2, 5, 8, 6 | Critical vulnerability and access review are strong. Story 8 needs correction. OT maintenance-window and explicit business-risk acceptance remain weak. |
| F-05 Change and Release Security Routing | Moderate | Story 4, Story 2 | Emergency and launch-related change are present, but normal go-live security routing is not deeply shown. Can be covered by a pre-production/handoff story. |
| F-06 Incident to Recovery to Standards Feedback | Weak | Story 6 | Third-party incident notification exists but blurs IR boundary and does not strongly show detection/standards feedback. Needs either major rewrite or new focused story. |
| F-07 Metrics, Oversight, and Improvement Routing | Strong for adoption and audit; moderate for metrics specificity | Stories 3, 5, 10, 9 | Improvement and oversight are visible. Metric IDs need expansion from E01, but no new F-07-only story is needed. |

## Existing Story-to-Pillar and Role-Family Map

| Story | Primary pillar / perspective | Supporting pillars | Major role families shown | Notes |
|---|---|---|---|---|
| 1. New SaaS application | Engineering / Risk shared | Governance | Engineering, Vendor Risk, Governance, Evidence | Good SaaS intake and TPRM bridge; could add contract/evidence detail. |
| 2. Critical vulnerability | Risk | Engineering, Governance, Business Owner/CISO | Exposure Management, Engineering, Governance | Best compact cross-pillar operations story. |
| 3. Audit request | Governance | Engineering, Risk | Evidence Librarian, Engineering, Risk Register/Exception | Strong evidence-quality story; metric family missing in MTR-001. |
| 4. Major cloud workload launch | Engineering | Risk, Governance, Business Owner | Architecture/Cloud Engineering, Risk, Governance | Good multi-flow story but needs business-owner risk wording fix. |
| 5. Privileged access review | Governance / Engineering | Risk | Identity Engineering, Evidence, Risk | Strong access review story; can be expanded for toxic combinations if desired. |
| 6. Third-party security incident notification | Risk / Vendor Risk | Engineering, Governance, IR adjacent | Vendor Risk, Engineering, Governance, Incident Commander not explicit | Needs IR-boundary rewrite or focused new F-06 story. |
| 7. Enterprise AI assistant rollout | Engineering/Governance | Risk, Business Owner | Architecture, Governance, Vendor Risk, Data Governance | Good AI controlled-pilot pattern. |
| 8. CERG Lite scanner report | Risk in small team | Engineering, Governance/CISO | Consolidated Risk/Engineering/Governance | Excellent small-team feel; risk-authority path needs correction. |
| 9. F-01 regulator change | Governance | Engineering, Risk, CISO/Board | Governance, Engineering Pillar Leader, Risk Pillar Leader, CISO | Strongest control-change narrative. |
| 10. New CISO first 90 days | CISO / Program leadership | All pillars | CISO, Engineering Lead, Trust/Governance, Risk | Strong adoption arc; not a single operational flow. |

## Candidate Story Decision Table

| Candidate from task brief | Decision | Reason |
|---|---|---|
| Engineering-led pre-production review with Risk scan and Governance evidence closure | Add new story | F-02/F-05 coverage is strong at intake/design but weak at Phase 4/5 go-live readiness, handoff package, and evidence closure. |
| Governance-led policy/control change flowing into Engineering implementation | Reject as new; already covered | Story 9 covers this extremely well through F-01. Promote Story 9 instead of adding another. |
| Risk-led vendor assessment that becomes a contract clause and later evidence | Expand existing Story 1 or Story 6, not new | Story 1 already has SaaS intake + vendor assessment; Story 6 has vendor incident. Add contract-clause and annual evidence details there if needed. |
| OT maintenance-window exception that avoids false urgency but preserves accountability | Add new story | No current story teaches OT operational windowing, CIP deviation interface, and risk accountability without panic. This is a distinct CERG concept. |
| Detection coverage gap discovered post-incident and converted into a standards update | Add new story | Story 6 is the only F-06 story and is not strong enough. This topic teaches adjacent IR boundary plus F-06→F-01/F-07 feedback. |
| Business owner rejects remediation cost and accepts residual risk with CISO oversight | Add new story or dedicated major expansion | Existing stories mention risk acceptance but include bad wording or do not teach the authority model. Given repeated B/C/D/E findings, this deserves a focused teaching example. |
| Audit evidence fails quality review and becomes a program improvement item | Reject as new; expand Story 3 | Story 3 already includes evidence quality issue and improvement item. Add clearer failed-evidence decision and metric closure there rather than new story. |
| Identity access review finds toxic combination risk and drives both remediation and metric update | Reject as new; expand Story 5 | Story 5 already covers privileged access review, stale contractor access, finding, remediation, and improvement. Add toxic-combination variant as a paragraph or sidebar. |

## Proposed Minimal New Story Set

### Proposed Story A — Pre-production review catches a release gap before go-live

- **Title:** `Story 11: Pre-production review turns a risky launch into a clean handoff`
- **Trigger:** A customer-facing service is two days from go-live. Phase 4 pre-production review finds that vulnerability scan evidence is clean, but logging validation and backup restoration evidence are missing.
- **Primary flow:** F-02 Project Intake, Architecture Review, and Threat Modeling.
- **Supporting flows:** F-05 Change and Release Security Routing; F-03 Asset Registration and Coverage Validation; F-07 Metrics/Oversight if SLA is missed.
- **Supporting docs:** `PRC-AR-001`, `PRC-VM-001`, `STD-LM-001`, `STD-RES-001`, `CAT-002`, `AUD-001`, `MTR-001`, `RAC-001`.
- **Core teaching point:** Engineering owns pre-production/go-live readiness; Risk validates exposure and scan state; Governance verifies evidence quality and regulatory overlay. A release can be delayed, approved with explicit post-go-live risk, or handed off cleanly, but it cannot proceed on verbal assurance.
- **Records produced:** Project Security Review Record, Pre-Production Checklist, Production Handoff Package, Asset Coverage Record, Finding Record if evidence/control gap exists, Go-Live Risk Acceptance Packet only if residual risk is accepted.
- **Evidence produced:** Final scan output, logging/SIEM source verification, backup/restore test evidence, handoff sign-offs, evidence index entries, change/CAB reference.
- **Reason it is needed:** Current F-02 stories focus on intake/design. D02 found Pre-production Reviewer scope ambiguity, and C02 found AR template drift. This story would teach Phase 4/5 and role boundaries directly.

### Proposed Story B — OT maintenance window handles a Critical exposure without false urgency

- **Title:** `Story 12: OT patch deferred to the maintenance window without losing accountability`
- **Trigger:** A Critical vulnerability is confirmed on an OT asset where immediate patching could disrupt operations. The next approved maintenance window is 45 days away.
- **Primary flow:** F-04 Finding to Remediation, Exception, or Residual Risk.
- **Supporting flows:** F-05 Change and Release Security Routing; F-07 oversight if the window exceeds acceptable thresholds.
- **Supporting docs:** `PRC-VM-001`, `PRC-RM-001`, `STD-OT-001`, `PLN-CIP-001` where applicable, `RMF-001`, `CAT-002`, `AUD-001`.
- **Core teaching point:** OT risk discipline is not panic patching. Risk validates exposure; Engineering/OT operations define safe treatment; Governance routes CIP deviation or exception evidence; Business/Operations owns operational consequence; CISO sees material deferral. The maintenance window is a control, not an excuse.
- **Records produced:** Finding Record, Exposure Backlog Item, OT maintenance/change record, Security Exception Record or CIP deviation record where applicable, Risk Register Entry if window or residual risk threshold requires it.
- **Evidence produced:** OT-safe exposure validation, operational impact assessment, compensating controls, monitoring evidence, approved maintenance window, post-window verification scan/test.
- **Reason it is needed:** No current story covers OT-specific timing. This is a high-value distinction because CERG repeatedly warns that OT scanning/patching cannot be treated like IT, while still preserving accountability.

### Proposed Story C — Post-incident detection gap becomes a standards update

- **Title:** `Story 13: The incident ends, but the detection gap becomes program work`
- **Trigger:** The standing IR team closes a Sev 2 incident. The post-incident review finds the attacker used a cloud API pattern that was logged but not detected.
- **Primary flow:** F-06 Incident to Recovery to Standards Feedback.
- **Supporting flows:** F-01 Control Intent to Implementation; F-07 Metrics, Oversight, and Improvement Routing; F-04 if residual exposure remains.
- **Supporting docs:** `PLN-IR-001`, `PRC-IR-002`, `PRC-LL-001`, `STD-LM-001`, `MTR-001`, `IMPREG-001`, `CAT-002`, `AUD-001`.
- **Core teaching point:** The Incident Commander commands the incident; CERG supports and then owns post-incident program changes. A detection gap becomes a Detection Coverage Record, Program Improvement Record, control/standard update, metric change, and validation plan.
- **Records produced:** Incident Record and Incident Action Log from IR; Lessons Learned Record; Program Improvement Record; Detection Coverage Record; Control Change Record if standard/control changes; Risk Record if residual exposure remains.
- **Evidence produced:** Incident timeline excerpt, SIEM query evidence, detection rule test output, updated logging requirement, purple-team validation result, dashboard metric update.
- **Reason it is needed:** Story 6 currently blurs IR boundary and does not strongly teach F-06. This story would make the adjacent-function model concrete and show how incidents improve standards without CERG owning active response.

### Proposed Story D — Business owner accepts residual risk after rejecting remediation cost

- **Title:** `Story 14: Security recommends treatment; the business accepts the consequence`
- **Trigger:** A remediation plan for a Medium/High application risk requires a costly redesign. The Business Owner rejects immediate remediation and requests residual risk acceptance while funding is planned for next quarter.
- **Primary flow:** F-04 Finding to Remediation, Exception, or Residual Risk.
- **Supporting flows:** F-07 Metrics/Oversight; F-01 if repeated acceptance drives a control change.
- **Supporting docs:** `RMF-001`, `PRC-RM-001`, `TMPL-RM-004`, `CAT-002`, `MTR-001`, `IMP-002`.
- **Core teaching point:** Security assesses and recommends; Governance routes and records; CISO approves the cybersecurity-program side where required; the Business Owner accepts the business consequence. Risk acceptance does not erase the finding, reset accountability, or become permanent.
- **Records produced:** Finding Record, Risk Register Entry, Risk Acceptance Request Form, treatment plan, Oversight Decision Record if High/Critical or resource decision is needed.
- **Evidence produced:** Risk assessment rationale, options analysis, Business Owner signature, CISO approval where required, expiration/review date, compensating control evidence, dashboard entry.
- **Reason it is needed:** Risk-acceptance authority drift appears repeatedly across B03, C03, D01, D03, and E01. Existing stories mention acceptance but do not teach the full authority model cleanly.

## Rejected New-Story Ideas and How to Cover Them Instead

| Rejected story idea | Cover through |
|---|---|
| Another generic SaaS intake story | Story 1 already teaches SaaS intake; expand it with contract clause and evidence renewal details if needed. |
| Another audit response story | Story 3 already teaches audit intake/evidence quality; expand it with AE metric closure after MTR-001 is updated. |
| Dedicated toxic-combination identity story | Story 5 can absorb this as a variant: privileged access review finds toxic role combination, Engineering remediates, Governance records evidence, Risk evaluates exposure. |
| Another control-change story | Story 9 is already the canonical F-01 story. Promote it and link it from FLOW-001. |
| Standalone AI agent story | Story 7 covers AI assistant rollout well enough for current corpus. E02 does not recommend adding AI complexity until the existing AI story is fully metric-linked. |
| Pure metrics dashboard story | Story 10 already shows board/dashboard rhythm; F07 coverage is adequate. Improve metric IDs in existing stories instead. |
| Separate vendor contract-clause story | Expand Story 1 or Story 6; do not add unless TPRM reader testing later shows persistent confusion. |

## Findings

### E02-F01 High Phase 4/5 pre-production review and production handoff lacks a strong example
Affected files:
- `examples/day-in-the-life/README.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`

Problem: Existing F-02 stories show intake, architecture review, SaaS onboarding, cloud launch, and AI pilot setup. They do not show the pre-production checklist, go-live readiness decision, production handoff package, and evidence closure in a focused way.

Why it matters: Pre-production review is where Engineering's advisory model becomes an operational gate. D02 found role-scope ambiguity around Pre-production Reviewer; a story can clarify Monday-morning work better than another abstract role paragraph.

Evidence from corpus:
- PRC-AR §8-9 define Phase 4 Pre-Production Security Review and Phase 5 Production Handoff and Go-Live.
- CAT-002 names Project Security Review Record as a key engineering record.
- Existing Stories 1, 4, and 7 stop mostly at architecture review/pilot/go-live conditions rather than handoff package mechanics.

Recommended action: Add Proposed Story A or expand Story 4 substantially. Prefer new Story A because it isolates Phase 4/5 without overloading the cloud launch story.

Owner/workstream: Examples / Engineering handoff.

### E02-F02 High F-06 incident-to-improvement coverage is weak and should not be left to Story 6 as written
Affected files:
- `examples/day-in-the-life/README.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: Story 6 is the only direct F-06 story. It covers a third-party incident notification but does not strongly show Incident Commander authority, CERG's support-only role during active response, or the post-incident conversion into detection/control/standard updates.

Why it matters: IR adjacency is one of the corpus's highest-risk boundaries. A story that clearly shows `IR commands; CERG supports; CERG improves the program after stand-down` would repair a reader-comprehension gap that has appeared in B02, C01, D02, and E01.

Evidence from corpus:
- E01-F03 found Story 6 blurs the IR adjacent-function boundary.
- PRC-IR §17 lists post-incident CERG actions but Story 6 does not foreground that handoff.
- FLOW-001 F-06 exists to turn incident/recovery outcomes into standards feedback.

Recommended action: Add Proposed Story C, or rewrite Story 6 so completely that it becomes this story. If Story 6 remains vendor-incident focused, Proposed Story C should still be added because it teaches detection/standard feedback directly.

Owner/workstream: Examples / Adjacent IR boundary.

### E02-F03 Medium OT maintenance-window decisioning lacks any narrative example
Affected files:
- `examples/day-in-the-life/README.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md`
- `plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md`

Problem: The current stories are cloud, SaaS, access, vulnerability, vendor, AI, small-team, regulatory-change, and CISO-adoption oriented. None shows OT maintenance-window handling, even though OT exceptions and CIP deviations are one of CERG's most important examples of risk-based operation without reckless urgency.

Why it matters: CERG distinguishes exposure reduction from blind patching. OT is the clearest place to teach that distinction: do not endanger operations to satisfy an IT-style SLA, but do not let maintenance-window language become unmanaged risk.

Evidence from corpus:
- PRC-VM contains OT environment overlays and PPR-tier acceptance restrictions.
- IMP-002 warns OT scanning can disrupt operations and CIP deviations require formal handling.
- No existing story has OT as its primary scenario.

Recommended action: Add Proposed Story B.

Owner/workstream: Examples / OT and exposure management.

### E02-F04 Medium Business-owner residual-risk acceptance is too important to remain only as a correction inside other stories
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: Existing stories mention exception and risk acceptance, but the two most relevant places are flawed: Story 4 says Risk accepts low residual risk, and Story 8 shows a Critical vendor exception path without enough business-owner/CISO escalation detail. Story 2 includes acceptance as a branch, not as the main teaching point.

Why it matters: The business-owner acceptance model is central to CERG. Because source documents have drifted on this issue, a clean narrative example would help readers internalize the difference between risk assessment, security approval/concurrence, and business acceptance.

Evidence from corpus:
- E01-F01 and E01-F02 flagged story-level risk-authority issues.
- D01-F02 found OM/RAC/JD risk-acceptance language conflicts.
- C03 found stale risk acceptance references and PPR precedence ambiguity.

Recommended action: Add Proposed Story D unless the author prefers to make Story 4 or Story 8 the canonical risk-acceptance story through major rewrite. If not adding Story D, E03 must make the rewrite instructions for Story 4/8 very explicit.

Owner/workstream: Examples / Risk acceptance authority.

### E02-F05 Medium TPRM contract/evidence lifecycle is underrepresented but can be handled by expanding existing stories
Affected files:
- `examples/day-in-the-life/README.md`
- `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
- `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md`
- `templates/CERG-TMPL-SBOM-001_SBOM_Request_and_Attestation_Template.md`

Problem: Existing vendor coverage appears in Story 1 and Story 6, but neither strongly shows the full TPRM lifecycle from assessment to contract clause to evidence renewal. C02 also found TPRM/SaaS/SBOM templates exist but are not clearly invoked by PRC-TPRM.

Why it matters: This is a real narrative gap, but adding a full new vendor story may be unnecessary if Story 1 can carry the concept through a few additional paragraphs and operational outputs.

Evidence from corpus:
- Story 1 includes vendor questionnaire, contract clauses, subprocessors, and a missing vendor feature, but contract/evidence lifecycle is not the main teaching point.
- Story 6 is about third-party incident notification, not ordinary TPRM lifecycle.
- C02 found TPRM templates need clearer invocation.

Recommended action: Do not add a new story yet. Expand Story 1 in E03: add one vendor contract-clause decision, one evidence renewal date, and a template reference for vendor/security/SBOM evidence.

Owner/workstream: Examples / TPRM expansion.

## Positive Confirmations
- The current story set already covers most of CERG's operating model: control change, intake, findings, audit, access review, vendor incident, AI, small-team operation, and CISO adoption.
- The strongest examples should be promoted rather than duplicated. Story 9 should become the canonical F-01 example; Story 2 should become the canonical F-04 vulnerability example; Story 10 should become the canonical new-CISO/adoption arc.
- F-07 is better covered than it first appears. Stories 3, 5, 9, and 10 all show improvement, metrics, oversight, or board cadence. The issue is metric specificity, not absence of narrative coverage.
- Story 5 can absorb identity toxic-combination teaching without needing a separate example.
- Story 3 can absorb audit evidence failure teaching without needing a separate example.

## Open Questions
- Should the example set remain compact at 10 stories plus targeted expansions, or grow to 14 with the four proposed additions?
- Should Proposed Story C replace Story 6, or should Story 6 remain third-party focused while Story C becomes the canonical incident-to-standards-feedback example?
- Should Proposed Story D be a standalone business-risk example, or should Story 4/8 be rewritten so one of them becomes the canonical business-owner acceptance story?
- Should Proposed Story B use a NERC-CIP BES Cyber System scenario or a non-BES OT scenario to avoid overloading the first OT example with regulatory detail?
- Should the pre-production story use a SaaS, cloud workload, or internal application scenario? A neutral internal application may best avoid duplicating Stories 1/4/7.

## Proposed Next Tasks
- E03: write rewrite/expansion plans for existing Stories 1, 3, 4, 5, 6, 7, and 8, and include exact insertion points for the rejected-as-new candidate ideas.
- G02: add source rewrite queue entries for Proposed Stories A-D if the author approves adding new stories.
- G03: add navigation polish for story count and story-file layout from E01.
- H01/H02/H03/H04: reader tests should validate whether the proposed story set is too large or whether the four additions materially improve comprehension.
