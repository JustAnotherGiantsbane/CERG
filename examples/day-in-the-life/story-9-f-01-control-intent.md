# Story 9: F-01 Control Intent - when the regulator changes the rule

This story is for any team that needs to convert an external regulatory change into operating CERG work. None of the other stories in this directory show [Flow F-01](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-01--control-intent-to-implementation) (Control Intent to Implementation) in motion. F-01 is the flow that turns governance-originated change into implementable technical work and risk-validated outcomes.

## Situation

Halberd Mutual is a 220-person European insurance carrier. Halberd adopted CERG Standard in 2024. The CERG Operating Model is in place, the MVC spine is running, all core standards are adopted, and Halberd holds ISO 27001:2013 certification with a planned transition to ISO 27001:2022 already in flight.

On a Tuesday morning in late October, the CISO Lena opens an email from the General Counsel. The firm's home country has transposed the EU NIS2 Directive into national law. The transposition text names Halberd as an "important entity" in the financial services sector. Compliance deadlines start in 90 days for board-level accountability, 180 days for the operational measures, and 365 days for full evidence readiness.

NIS2 obligations cut across Halberd's existing CERG work: incident reporting timelines (24-hour early warning, 72-hour notification, 30-day final report), supply-chain security controls, encryption and cryptography requirements, business continuity and crisis management, vulnerability handling, and board-level cybersecurity accountability. None of these are new categories for CERG. What is new is the binding legal clock and the named executive accountability.

The work has to move fast. The CISO's question is: how does CERG absorb a regulatory change without breaking the program?

## CERG flow pattern

Primary flow: [F-01 Control Intent to Implementation](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-01--control-intent-to-implementation)

Supporting procedures and standards:

- [Risk Management Framework](../../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) - for the gap analysis that justifies the F-01 record.
- [Unified Control Baseline](../../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) - to map NIS2 obligations onto existing CB controls.
- [Compliance Matrix](../../governance/CERG-GOV-CMX-001_Compliance_Matrix.md) - to verify alignment with ISO 27001:2022, NIST CSF 2.0, and DORA simultaneously.
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - for obligations Halberd cannot meet by the deadline.
- [Cybersecurity Policy](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - the parent policy that may need a clarifying paragraph for board accountability.
- [Architecture Review and Project Intake Procedure](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) - for any technical changes that result.
- [Evidence Quality Standard](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md) - for the audit package that goes to the regulator.
- [Program Improvement Register](../../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) - for tracking and reporting the rollout.

### Why F-01, not F-02 or F-04

The temptation is to treat NIS2 as a project (F-02) or a finding (F-04). Neither fits. F-02 is for new systems or services entering production. F-04 is for specific vulnerabilities or audit findings. NIS2 is a control intent change at the program level: new rules that affect existing controls across many systems, with an external authority and a clock.

F-01 is the right flow when the trigger is:

- Policy changed (here: the regulator added requirements)
- Standard changed (consequence)
- Control baseline changed (consequence)
- Regulatory requirement added (direct trigger)

This story walks through the first two triggers.

## Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | The CISO convenes a one-hour "regulatory change" session with the General Counsel, the Risk Pillar Leader (Marco), the Governance Pillar Leader (Yusra), and the Engineering Pillar Leader (Aisha). They map NIS2 obligations onto CERG artifacts. | CISO | Decision Log entry; gap analysis spreadsheet |
| 2 | Yusra opens one Control Change Record per NIS2 obligation cluster (incident reporting, supply-chain, cryptography, continuity, vulnerability handling, board accountability). Six Control Change Records in total. | Governance Pillar Leader | 6 Control Change Records (CCR-NIS2-001 through CCR-NIS2-006) |
| 3 | For each Control Change Record, Yusra defines the conformance scope: which environments, which asset classes, which existing controls apply, which are missing. | Governance Pillar Leader | Conformance Scope Statement per CCR |
| 4 | Aisha produces the implementation design: which existing CERG standards need a new clause, which procedures need a step, which templates need new fields. | Engineering Pillar Leader | Implementation design package per CCR |
| 5 | Marco defines validation criteria before rollout: how Risk will test that the new obligation is met. For incident reporting, the validation is a tabletop that walks the 24-hour / 72-hour / 30-day clocks end to end. | Risk Pillar Leader | Validation plan per CCR |
| 6 | Yusra approves the evidence plan and assigns implementation deadlines. The 90-day obligation lands on CCR-NIS2-006 (board accountability). The 180-day obligations land on CCRs 001-004. The 365-day obligations land on the evidence-readiness track. | Governance Pillar Leader | Approved evidence plan per CCR |
| 7 | Aisha and the Engineering pillar execute rollout per CCR. Each implementation produces evidence: updated standards, updated procedures, new templates, training records, board materials. | Engineering Pillar Leader | Implementation evidence per CCR |
| 8 | Marco validates effectiveness per CCR. For each closure, Marco produces a Control Test Worksheet using [CERG-TMPL-AUD-001](../../templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md). | Risk Pillar Leader | Control Test Worksheets |
| 9 | For obligations Halberd cannot meet by the deadline, the Business Owner (CEO, in this case, because the obligation is board-level) signs a Risk Acceptance Memo with a documented remediation plan and a named review date. | CEO + CISO | Risk Acceptance Memo per missed obligation |
| 10 | Yusra updates the metrics dashboard with NIS2 implementation status and links the audit package. The dashboard now has a regulator-facing overlay that the board reads monthly. | Governance Pillar Leader | Updated Reporting Metric Record |

### Narrative

Lena opens the General Counsel's email at 9:14 a.m. By 9:30 a.m. she has scheduled a one-hour session for 11:00 a.m. with Marco, Yusra, and Aisha. She also loops in the CEO's chief of staff so the board-level accountability conversation has executive context.

At 11:00 a.m. the four sit down with the transposition text, a printout of the existing [Unified Control Baseline](../../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md), and the [Compliance Matrix](../../governance/CERG-GOV-CMX-001_Compliance_Matrix.md) cross-reference page. They walk each NIS2 article and find:

- Incident reporting timelines → CB-001 §6 already has the concept; specific 24/72/30 clocks are new.
- Supply-chain security → CB-001 §9 covers TPRM; NIS2 adds explicit subcontractor flow-down requirements that the existing CERG-PRC-TPRM-001 does not enforce.
- Cryptography → existing CERG-STD-CR-001 covers algorithm and key management; NIS2 adds explicit requirements for state-of-the-art cryptography that need a clarifying sentence.
- Business continuity → existing CERG-PLN-BC-001 covers DR; NIS2 adds explicit crisis-management obligations that link crisis to incident declaration.
- Vulnerability handling → existing CERG-PRC-VM-001 covers exposure management; NIS2 adds explicit coordination requirements with the regulator.
- Board accountability → existing CERG-POL-001 names the CISO; NIS2 requires named board-level sign-off and documented cybersecurity training for board members.

By noon the gap analysis is complete. Marco logs a Decision Log entry per IMP-002 §4: "NIS2 identified as in-scope. Six Control Change Records opened. Existing CERG work absorbs 80 percent of obligations. Three obligations need new clauses in existing standards. One obligation needs a board training program."

Yusra opens six Control Change Records before end of day. Each has the source reason, affected environments, affected asset classes, implementation deadline (mapped to the regulatory clock), required evidence, and reporting metric target. CCR-NIS2-006 (board accountability) gets the 90-day deadline. CCR-NIS2-001 through 004 (operational measures) get the 180-day deadline. CCR-NIS2-005 (full evidence readiness) gets the 365-day deadline.

Over the next two weeks, Aisha drafts implementation designs. The supply-chain gap requires a new clause in CERG-PRC-TPRM-001 requiring explicit flow-down language in vendor contracts. The cryptography gap requires a one-paragraph addendum to CERG-STD-CR-001 §3 defining "state-of-the-art" with reference to NIST and BSI guidance. The board accountability gap requires a board cybersecurity training program documented in CERG-GOV-TRN-001 and a board-pack insert prepared by Yusra.

Marco's validation plan for the incident reporting CCR is the most elaborate. He schedules a tabletop at day 100 that walks a real incident scenario through the 24-hour early warning, 72-hour notification, and 30-day final report. The tabletop is run by the standing IR team (Halberd has an internal IR function, not an external one) with CISO and General Counsel observing. The tabletop produces a control test result and a list of process gaps that go into the Program Improvement Register.

By day 175, CCR-NIS2-001 through 004 are validated and closed. The board accountability CCR closes on day 88, three days before the deadline. The full evidence-readiness CCR closes on day 340 with the audit package ready for regulator review.

For two obligations Halberd cannot fully meet by the deadline, the CEO signs a Risk Acceptance Memo with a remediation plan and a 90-day review date. The memos are time-bound, named-owned, and visible in reporting. They are not "exceptions hidden in email." They are exceptions with ownership and clocks.

### The key idea

F-01 exists so that when an external authority changes the rules, the program has one flow to absorb the change without scattering the work across ad hoc projects. The flow produces:

- One Control Change Record per obligation cluster (not one per control, not one per system).
- One Conformance Scope Statement per CCR (what is in scope, what is out).
- One Implementation Design per CCR (what changes in which standards, procedures, templates).
- One Validation Plan per CCR (how Risk will test).
- One Evidence Plan per CCR (what proves the obligation is met).
- One Closure per CCR or one Risk Acceptance Memo if the obligation cannot be met by the deadline.

The board never sees a "NIS2 project." The board sees the monthly regulatory-overlay line on the metrics dashboard. The dashboard is fed by the six CCRs. The CCRs are fed by the gap analysis. The gap analysis is fed by the regulatory text. The chain is traceable end to end in the evidence library.

## Operational outputs

- 6 Control Change Records opened with conformance scope, implementation deadline, evidence plan, and reporting metric target.
- 6 Implementation Design packages (updates to existing standards, procedures, and templates).
- 6 Validation Plans and 6 Control Test Worksheets.
- 1 tabletop exercise for the incident reporting CCR with named gaps fed to the Improvement Register.
- 2 Risk Acceptance Memos for obligations that miss the regulatory deadline, with remediation plans and 90-day review dates.
- 1 audit package with regulator-facing evidence indexed per NIS2 article.
- 1 monthly regulatory-overlay line on the board metrics dashboard, traceable end to end to the source obligations.

## What this story does not cover

- **Internal IR declaration.** The tabletop here is for validation, not for a real incident. See Story 6 for that.
- **Audit response.** This story assumes a forward-looking regulatory obligation, not an auditor's request. See Story 3 for that.
- **CERG Lite.** Halberd is a Standard team. See Story 8 for the small-team pattern.

For the F-01 SLAs and decision logic, see [CERG-GOV-FLOW-001 §9](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#9-flow-f-01--control-intent-to-implementation). For the gap-analysis pattern that justifies opening a CCR, see [CERG-GOV-RMF-001](../../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md). For the audit-ready evidence model, see [CERG-GOV-AUD-001](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md).
