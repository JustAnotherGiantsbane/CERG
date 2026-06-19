# Task D03 Output: Test small-team role consolidation for human clarity

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
  - `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
  - `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
  - `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - `examples/day-in-the-life/story-8-cerg-lite-maria.md`
  - Supporting workflow files: `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`, `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`, `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`, `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`, `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`, `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`, and `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`.
- Sections reviewed:
  - IMP-003 §2-8: CERG Lite package, operating rhythm, role consolidation map, first records, success criteria, fallback schemas, and evidence library.
  - IMP-006 §2-8: role checklists and small-team consolidated checklist.
  - IMP-007 §3-5: CISO, Risk Lead, and Engineering Lead reader paths.
  - FRM-002 §4.1-4.2: pillar interaction and collapse rule.
  - IMP-002 §4, §5, §7, §8: decision log, risk acceptance guardrails, role safety, and dangerous changes.
  - OM-001 capability map and §6.1 canonical roster.
  - RAC-001 §6-8: standing process RACI, role descriptions, and scaling map.
  - Story 8 full walkthrough.
- Files intentionally not reviewed:
  - Full workforce planning and succession documents. D03 tests small-team reader clarity, not long-term capacity modeling.
  - Every day-in-the-life story. Story 8 is the canonical CERG Lite story named by FRM-002 §4.2.
  - All per-role JDs. D01/D02 already tested role/JD fit; D03 tests consolidated hats and workflows.

## Method
- Steps performed:
  1. Extracted every major statement that says roles, pillars, or capabilities collapse onto fewer people.
  2. Compared the small-team maps in OM-001, RAC-001, IMP-003, IMP-006, FRM-002, and Story 8.
  3. Tested the required 2-person, 5-person, and 8-person scenarios against five workflows: critical vulnerability, SaaS intake, audit evidence request, expired exception, and incident handoff.
  4. For each workflow, checked whether a reader can identify which hat is acting: Engineering, Risk, Governance, CISO, Business Owner, or standing IR team.
  5. Applied IMP-002 role-safety rules to each scenario.
- Search terms or scripts used:
  - `rg -n "2-person|two-person|2 people|3 people|5-person|8 people|role consolidation|heads|collapse|collaps" governance examples/day-in-the-life roles`
  - Targeted reads of role consolidation maps and role safety sections.
  - Manual workflow tracing through FLOW-001, PRC-VM, PRC-RM, PRC-AR, PRC-TPRM, PRC-AUD, PRC-IR, and PLN-IR.
- Assumptions avoided:
  - Did not treat a person holding several hats as a defect by itself. That is the intended CERG Lite design.
  - Did not require small teams to use all full-corpus documents. D03 tests whether the core questions survive, not whether every mature artifact is adopted on day one.
  - Did not assume the security team can accept business risk. IMP-002, RMF-001, and PRC-RM keep business acceptance separate.

## Consolidation Principle Test

The principle is strong and memorable:

> Heads collapse; questions do not.

FRM-002 §4.2 says the three pillars collapse onto fewer heads in CERG Lite, but the questions remain distinct: Risk still triages, Engineering still builds, Governance still routes. GEN-001 reinforces that canonical role names collapse onto fewer heads while the questions do not collapse. RAC-001 §8 says a consolidated role is still an owned role. Story 8 shows the principle in motion.

The weakness is not the principle. The weakness is map consistency and edge-case guidance. A reader can understand the idea quickly, but may not know which source map to apply when they have 2, 3, 5, or 8 people.

## Small-Team Workflow Maps

### 2-person workflow map — inferred, not explicitly supplied by the corpus

The corpus says CERG Lite covers 2-8 people, but it does not provide a 2-person map. The map below is the safest inferred version from IMP-002 role-safety rules.

| Workflow | Person A: Security Lead / CISO / Governance / Risk hats | Person B: Engineering Lead / implementation hats | External required role | Can a reader tell which hat is acting? |
|---|---|---|---|---|
| Critical vulnerability | Risk hat validates exposure, classifies, starts SLA; Governance hat records evidence and escalation; CISO hat reviews High/Critical status. | Engineering hat patches, blocks path, changes config, or supplies compensating control evidence. | Business Owner / Executive Sponsor accepts residual business risk if SLA cannot be met. | Partially. Workflow can be inferred, but the 2-person split and independent acceptance rule are not written as a worked map. |
| SaaS intake | Governance hat checks regulatory scope and evidence; Risk/Vendor hat assesses vendor and residual third-party risk. | Engineering hat reviews SSO, logging, tenant configuration, data flow, and integration pattern. | Business Owner sponsors SaaS and owns residual business risk. Procurement/Legal own vendor contract. | Partially. PRC-AR/TPRM are clear, but the 2-person hat sequence is not made explicit. |
| Audit evidence request | Governance/Evidence hat receives request, indexes evidence, preserves submitted package. | Engineering hat produces technical/configuration/source evidence. | Auditor/assessor external; CISO for material findings. | Mostly. Separation works if Person A is not also the evidence producer for the tested control. IMP-002 requires independent sampling where self-review appears. |
| Expired exception | Governance/Risk Register hat sends warning chain, auto-creates Finding Record after expiration, escalates to CISO. | Engineering hat remediates or submits renewal/closure evidence. | Business Owner signs any residual risk above Low; CISO/Executive Sponsor for High/Critical path. | Mostly, but only if the reader remembers IMP-002. PRC-RM gives the workflow; 2-person role collision guidance is not embedded in the example. |
| Incident handoff | Governance/Risk hat supplies scope, data classification, risk history, evidence index; CISO receives material briefings. | Engineering hat supplies asset context and executes IC-directed technical support. | Standing IR team / Incident Commander commands the incident. | Yes for command boundary, because IR documents have strong adjacent-function banners. Less clear for small-team on-call assignment. |

### 5-person workflow map — clear in concept, inconsistent by source map

The safest 5-person operational map is RAC-001 §8: CISO; Governance bundle; Risk bundle; Engineering lead/cloud/identity/pre-production; and application/endpoint/crypto/OT engineering. IMP-003 uses a different 5-person distribution. The workflow below uses the RAC-style split because it preserves pillar boundaries most clearly.

| Workflow | CISO | Governance person | Risk person | Engineering person(s) | Business / Adjacent role | Can a reader tell which hat is acting? |
|---|---|---|---|---|---|---|
| Critical vulnerability | Reviews High/Critical escalation; approves High/Critical program acceptance where applicable. | Confirms evidence quality, exception/risk route, dashboard and escalation. | Exposure Management Lead validates, classifies, owns SLA tracking and posture metrics. | Engineering remediates, changes config, patches, validates implementation evidence. | Business Owner accepts residual business risk; Executive Sponsor for Critical. | Yes if RAC-001 map is used. Story 8 muddies authority for Critical vendor exposure. |
| SaaS intake | Receives material escalation. | Confirms regulatory scope and evidence obligations. | Vendor Risk Analyst tiers vendor and collects evidence; Risk participates if risk concentration threshold triggers. | Engineering runs PRC-AR intake, architecture review, SSO/logging/configuration review. | Business Owner sponsors SaaS and owns risk; Procurement/Legal own contract. | Mostly. PRC-AR/TPRM are clear, but IMP-003 map puts compliance/IR liaison in a separate fifth role while RAC puts governance in person 2. |
| Audit evidence request | Receives material audit findings and escalations. | Evidence Librarian/Governance owns intake, evidence library, submitted package, corrective action tracking. | Supplies exposure/risk/vendor evidence. | Supplies technical control evidence. | Auditor/assessor/customer external. | Yes. This is one of the best small-team fits if Governance is not also the evidence producer for the sampled control. |
| Expired exception | Receives Day 5 escalation or High/Critical acceptance route. | Risk Register Owner warning chain, auto-Finding, approval routing. | Reassesses likelihood/impact and treatment. | Provides remediation or compensating-control evidence. | Business Owner signs residual risk above Low. | Yes in PRC-RM; small-team role collision still needs explicit local decision-log entry. |
| Incident handoff | Receives material briefings; executive escalation. | Supplies regulatory/evidence/reporting support. | Supplies exposure, detection, vendor, and risk context. | Supplies asset/recovery/containment support as directed. | Incident Commander / standing IR team owns command. | Yes for command boundary. Some IR body text still blurs Governance ownership from B02/D02. |

### 8-person workflow map — plausible, but not defined

IMP-003 says it is for teams of 8 or fewer, but it provides a 5-person map and a 3-person fallback, not an 8-person map. Story 8 says Northwind may grow to 8 people, but the described deconsolidation appears to list only seven named security people. The map below is therefore inferred.

| Workflow | Likely 8-person split | Workflow clarity |
|---|---|---|
| Critical vulnerability | CISO; Governance/Risk Register/Evidence; Risk Lead/Exposure; Engineering Lead; platform/application engineer; Business Owner outside security. | Clear if roles follow RAC. An explicit 8-person map would remove guesswork. |
| SaaS intake | Engineering Lead opens intake; platform/cloud/identity engineer reviews technical controls; Vendor Risk Analyst or Risk Lead assesses vendor; Governance checks regulatory scope; Business Owner sponsors. | Mostly clear from PRC-AR/TPRM, but the 8-person role map is not shown. |
| Audit evidence request | Governance/Evidence owner intakes request; Compliance role handles framework overlay; Engineering and Risk produce evidence; CISO reviews material findings. | Clear if the 8-person team splits Governance from Compliance/Evidence; not specified. |
| Expired exception | Risk Register Owner runs warning chain; Risk reassesses; Engineering remediates; Governance routes approval; CISO/Executive Sponsor where required. | Clear in PRC-RM, but no 8-person assignment table shows who holds Risk Register Owner vs Governance Pillar Leader. |
| Incident handoff | CERG on-call activates Engineering, Risk, Governance support; IC commands; CISO receives briefings. | Clear at boundary level; staffing of CERG on-call for an 8-person team is not shown. |

## Findings

### D03-F01 High Small-team consolidation maps disagree across OM, RAC, IMP-003, and Story 8
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`

Problem: The corpus has several small-team maps, but they do not assign work the same way. OM-001's ≤5 capability map puts Exposure Management under the Security Engineer and Risk Register under the CISO/Security Lead. RAC-001's five-person map puts Risk roles, including Exposure Management Lead and Detection Engineer, on person 3 and Governance roles on person 2. IMP-003's five-person map puts CISO, Governance Pillar Leader, Policy & Standards Manager, Risk Register Owner, and Evidence Librarian all on person 1; Risk roles on person 2; Engineering roles across persons 3 and 4; and compliance/IR liaison on person 5. Story 8's three-person example says Maria is CISO + Governance + Risk Register, Priya is Risk + Exposure Management + Vendor Risk, and Devin is Engineering, but later says Priya owns the risk register.

Why it matters: The principle is clear, but a small-team adopter needs a single source of truth for assigning hats. If the maps disagree, the reader may assign exposure management, risk register curation, evidence, or compliance to different people depending on which file they opened first.

Evidence from corpus:
- OM-001 capability map: `Security Engineer` holds Security Architecture + Identity/Platform Engineering + Exposure Management.
- RAC-001 §8.2: person 3 holds Risk Pillar Leader, Exposure Management Lead, Adversarial Testing Lead, Threat Intelligence Analyst, Vendor Risk Analyst, and Detection Engineer.
- IMP-003 §4: person 1 combines CISO, Governance Pillar Leader, Policy & Standards Manager, Risk Register Owner, and Evidence Librarian; person 2 combines Risk Pillar Leader, Exposure Management Lead, Threat Intelligence Analyst, Detection Engineer, and Vendor Risk Analyst.
- Story 8: Maria is CISO + Governance + Risk Register; Priya is Risk + Exposure Management + Vendor Risk; later narrative says Priya owns the scanner schedule and the risk register.

Recommended action: Declare one authoritative small-team consolidation map, preferably in RAC-001 or OM-001, and make IMP-003, FRM-002, IMP-006, IMP-007, and Story 8 point to it. If multiple maps are intentionally examples, label them as examples and state which map governs conflict resolution. Fix Story 8's risk-register owner sentence.

Owner/workstream: Workforce / Small-team adoption.

### D03-F02 High CERG Lite says 2-8 people, but the two-person case is not operationally mapped
Affected files:
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`

Problem: FRM-002 and Story 8 frame CERG Lite as 2-8 people. IMP-003 says the guide is for teams of 8 or fewer, gives a five-person map, gives a three-person fallback, and says one person is not ready to adopt CERG as an operating model. It does not give a two-person map. IMP-006 §7 then says one person may act as Security Lead, Governance Lead, Risk Lead, and Engineering Lead in CERG Lite, which sounds like a one-person operating model unless read very generously.

Why it matters: The two-person case is the hardest case for separation of duties. A two-person security team can run the MVC spine only if it knows which decisions must leave the two-person team: business risk acceptance, independent evidence testing, exception approval where the requester is also the approver, and IR command. Without a worked two-person map, the reader has to infer the highest-risk rules from IMP-002.

Evidence from corpus:
- FRM-002 §4.2: small teams are `CERG Lite, 2-8 people`.
- IMP-003 §4: gives 5-person and 3-person guidance, and says one person is not ready.
- IMP-006 §7: `For CERG Lite, one person may act as Security Lead, Governance Lead, Risk Lead, and Engineering Lead`.
- IMP-002 §7: risk assessor and sole risk acceptor, evidence producer and tester, exception requester and approver, and Incident Commander and corrective-action validator must not collapse without independent review.

Recommended action: Add an explicit two-person map and a one-person boundary note. Suggested rule: two-person CERG Lite requires Security/Governance/Risk hats on one person, Engineering/implementation hats on the other, plus named Executive Sponsor/Business Owner outside the security team for acceptance and exception independence. One-person security may use CERG as a planning reference, but not claim CERG operating-model adoption unless an external reviewer or managed provider supplies the missing independent functions.

Owner/workstream: Small-team adoption / Role safety.

### D03-F03 High Story 8's Critical vendor exposure path weakens small-team risk and exception guardrails
Affected files:
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`

Problem: Story 8 is the canonical worked example for small-team collapse, but its SFTP Critical vendor scenario risks teaching the wrong exception behavior. The story says both Critical findings have public exploit code. The vendor-owned SFTP endpoint is handled by opening a Third-Party Finding and an Exception Record with compensating monitoring and a vendor patch date, and Maria approves it in the weekly meeting. The story does not explicitly show Business Owner approval for residual risk above Low, does not distinguish security exception from business risk acceptance in the narrative, and lets a Critical/public-exploit vendor exposure sit on a 30-day vendor patch timeline.

Why it matters: Examples teach the operating model more powerfully than tables. A small-team reader may copy this pattern and believe that the consolidated CISO/Governance person can approve a Critical exposure exception with monitoring and a vendor promise, without explicit business acceptance or heightened escalation.

Evidence from corpus:
- Story 8: two Critical CVEs have public exploits; one is on a vendor-owned legacy SFTP endpoint.
- Story 8: Priya creates an Exception Record; Maria approves the SFTP exception with monitoring and a vendor patch date.
- PRC-RM §7.3: Business owner approval is required for any exception carrying residual risk above Low.
- IMP-002 §5: the business owner must sign acceptance; security cannot accept risk on behalf of the business.
- PRC-VM §11: risk acceptance for missed treatment routes through PRC-RM, and PPR-tier exposures are not eligible for ordinary acceptance except OT/CIP deviation scenarios.

Recommended action: Rewrite the Story 8 SFTP branch to show the decision path explicitly. At minimum: classify whether it is a Security Exception or Risk Acceptance; name the Business Owner; show CISO/Executive Sponsor escalation if Critical residual risk remains; explain why PPR does or does not apply; and make compensating monitoring a temporary control, not a quiet 30-day acceptance of a public-exploit Critical exposure.

Owner/workstream: Examples / Small-team risk authority.

### D03-F04 Medium The eight-person deconsolidation path is implied but not mapped
Affected files:
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`

Problem: IMP-003 is explicitly for teams of 8 or fewer, but gives a five-person map and a three-person fallback. Story 8 says Northwind may grow to 8 people and will deconsolidate, but the described additions appear to produce seven people, not eight: Maria, Priya, Devin, dedicated Identity Engineer, dedicated Compliance person, and two more Engineering roles.

Why it matters: Eight people is the upper edge of CERG Lite. It is the point where an adopter should begin separating risky combinations. Without an 8-person map, the reader may not know what to peel off first: Evidence Librarian, Risk Register Owner, Vendor Risk, Identity, Compliance, or Pre-production Reviewer.

Evidence from corpus:
- IMP-003 metadata says small-team adopters are ≤8 people.
- IMP-003 §4 gives 5-person and 3-person examples only.
- Story 8 says growth to 8 people adds a dedicated Identity Engineer, dedicated Compliance person, and two more Engineering roles while Maria keeps CISO/Governance and Priya keeps Risk/Exposure Management.

Recommended action: Add a short 8-person deconsolidation table. Recommended split: CISO; Governance/Risk Register/Evidence; Compliance Manager; Risk/Exposure Lead; Vendor/Threat/Detection role; Engineering Lead/Cloud; Identity/Endpoint; Application/Pre-production/Crypto/OT. Then state the priority order for peeling roles off as headcount grows.

Owner/workstream: Small-team adoption / Workforce planning interface.

### D03-F05 Medium Role-safety guardrails are strong but too detached from the small-team maps
Affected files:
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`

Problem: IMP-002 has excellent role-collision guidance: risky consolidations, never-combine rules, and minimum separation of duties. But IMP-003's role map and IMP-006's consolidated checklist do not embed those rules at the points where the reader is assigning people. Story 8 mentions the Decision Log, but does not walk through the compensating-control decision for each risky consolidation.

Why it matters: Small teams do not fail because they reject separation of duties in theory. They fail because, under pressure, one person wearing four hats forgets which decisions need a second set of eyes. The safety rules need to be present beside the map and in the example, not only in a separate adoption-safety document.

Evidence from corpus:
- IMP-002 §7 lists risky consolidations and never-combine pairs.
- IMP-003 §4 tells the reader to document consolidations and points to IMP-002, but does not annotate the map with collision warnings.
- IMP-006 §7 gives a consolidated checklist but does not flag which tasks require independent review or external business approval.
- Story 8 shows a consolidated team in action but only lightly shows the compensating-control logic.

Recommended action: Add a `Collision checks` column to IMP-003 §4 and a short `When you are wearing both hats` warning box to IMP-006 §7. In Story 8, add one sentence each time Maria/Priya/Devin switch hats for a decision that requires independent review.

Owner/workstream: Small-team adoption / Human clarity.

### D03-F06 Low Incident handoff support has a local section-reference error
Affected files:
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`

Problem: PRC-IR §18.1 stand-down says CERG begins post-incident actions per Section 11, but post-incident CERG actions are in Section 17.

Why it matters: Low severity. The adjacent-function boundary is understandable, but a small-team reader trying to find post-incident CERG actions may jump to the wrong section.

Evidence from corpus:
- PRC-IR §17 is `Post-Incident CERG Actions`.
- PRC-IR §18.1 step 5 says CERG begins post-incident actions per Section 11.

Recommended action: Change `Section 11` to `Section 17` in PRC-IR §18.1.

Owner/workstream: G03 polish / Incident handoff clarity.

## Positive Confirmations
- The core phrase is excellent: the questions do not collapse, only the heads. FRM-002 §4.2 says this clearly enough for a new reader to retain.
- IMP-002 §7 is one of the strongest small-team safety sections in the corpus. It names risky consolidations, never-combine combinations, and minimum separation of duties in practical terms.
- IMP-003's first 10 records are exactly what a small team needs: profile, role assignment map, asset extract, top risks, exposure backlog, exception register, evidence index, control snapshot, regulatory applicability decision, and improvement backlog.
- IMP-006 is useful because it turns adoption into action by role and time horizon. The `Completion means artifact, record, decision, or evidence link` line is especially strong.
- Story 8 is operationally valuable. It shows a real Tuesday, real people, real records, and a bounded workload. With risk-authority cleanup, it can remain the canonical CERG Lite story.
- Incident handoff is mostly clear for small teams: the standing IR team commands; CERG supplies context, owners, evidence, and post-incident improvement work.

## Open Questions
- Which small-team map is authoritative: OM capability map, RAC scaling map, IMP-003 role map, or Story 8's example?
- Should CERG Lite explicitly support two-person operating-model adoption, or should two-person teams be treated as `planning / partial adoption` until an external reviewer or managed service fills separation-of-duty gaps?
- In an 8-person Lite team, which roles should deconsolidate first: Evidence Librarian, Risk Register Owner, Vendor Risk Analyst, Identity Engineer, or Pre-production Reviewer?
- Should Story 8 use a less dangerous second Critical scenario, or keep the vendor-owned Critical exposure and show the full business acceptance/escalation path?
- Should role collision warnings live only in IMP-002, or be repeated in every small-team checklist and example where the collision appears?

## Proposed Next Tasks
- E01: when evaluating examples, revisit Story 8 first because it is the canonical small-team narrative and now has D03 risk-authority findings.
- G02: add rewrite queue items for unified small-team map, two-person map, eight-person deconsolidation map, Story 8 SFTP exception path, and embedded role-collision warnings.
- G03: add polish queue item for PRC-IR §18.1 Section 11 → Section 17 reference.
- Later source remediation: align OM/RAC/IMP-003/Story 8 so there is one authoritative consolidation model and examples become illustrations rather than competing maps.
