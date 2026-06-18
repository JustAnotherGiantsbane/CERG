# Task B01 Output: Test whether three pillars still hold

## Scope Reviewed
- Files read:
  - `README.md`
  - `governance/CERG-GOV-FRM-001_CERG_Framework.md`
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
  - all files under `standards/`
  - all files under `procedures/`
  - all files under `examples/day-in-the-life/`
- Sections reviewed: pillar mission statements, operating mandates, canonical role roster, master RACI, seven canonical flows, standards headings and owner metadata, procedure headings and owner metadata, and all day-in-the-life story walkthroughs.
- Files intentionally not reviewed: workforce JDs beyond the A02 role-JD anomaly, risk-specific RMF details not needed for the three-pillar verdict, and adoption implementation guides except where stories cited them.

## Method
- Steps performed:
  1. Extracted pillar mission language from `README`, `FRM-001`, `FRM-002`, and `OM-001`.
  2. Compared the verbs and scope of each pillar statement.
  3. Built an activity inventory from standards, procedures, FLOW-001, RAC-001, and examples.
  4. Tested candidate fourth pillars: Incident Response, Security Awareness, Compliance, Detection, Architecture, Workforce, Privacy, Business Continuity, and Program Management.
  5. Checked the specific tests from the work plan: detection placement, threat intelligence routing, standards authorship versus approval, Governance implementation creep, Engineering post-production monitoring creep, and Risk business-acceptance creep.
- Search terms or scripts used: Python extraction of metadata owners and numbered headings from all standards/procedures; targeted scans for `Detection Engineer`, `Threat Intelligence`, `risk acceptance`, `Governance does not`, `standing IR team`, and pillar mission phrases.
- Assumptions avoided: did not assume a document's machine-readable `pillar` field was the activity owner; compared it to the document owner, headings, RAC-001 assignments, and narrative examples.

## Pillar Mission Comparison

| Source | Engineering | Risk | Governance | Assessment |
|---|---|---|---|---|
| `README.md` | Builds security in early. | Understands exposure and drives treatment. | Sets clear rules, records decisions, keeps evidence usable. | Strong, compressed front-door version. |
| `FRM-001` | Build securely. Deploy confidently. Consult continuously. | Know your exposure. Manage it deliberately. Never be surprised. | Set the rules. Track the work. Enable the business to move with confidence. | Strongest narrative version. Adds business-enablement voice. |
| `FRM-002` | How do we build and operate this securely? Architecture decisions, baselines, secure patterns, remediations. | What exposure remains and what treatment is required? Findings, risk records, vendor assessments, threat validation. | What rule, evidence, decision, or report governs this? Standards, evidence records, metrics, audit packages, improvement actions. | Strongest operational-question version. Best for handoffs. |
| `OM-001` | Build secure systems by design. Embed security into architecture, configuration, and operational baselines before production. | Maintain continuous visibility into organizational exposure. Drive the work that reduces it. Test that controls hold up under attack. | Own the policy library, compliance posture, risk register, and evidence library. Translate regulation into actionable expectations. | Most precise accountability version. |

Conclusion from mission comparison: the verbs are consistent enough to hold. The shortest front-door wording, the narrative spine, the operating question model, and the mandate model all point to the same decomposition: build, understand/treat exposure, and govern decisions/evidence.

## Pillar Activity Inventory

| Activity or artifact area | Primary pillar | Supporting pillar(s) | Evidence reviewed | Fit assessment |
|---|---|---|---|---|
| Access standard and identity requirements | Engineering | Governance, Risk | `STD-AC-001`, `PRC-AC-002`, RAC access process | Fits Engineering because identity controls are built and operated; Governance supplies evidence and access review conformance. |
| AI intake, acceptable use, and AI system controls | Engineering | Risk, Governance | `STD-AI-001`, FLOW F-02 AI routing, Story 7 | Fits Engineering for implementation and architecture, with Risk assessing model/vendor/data exposure and Governance setting use conditions. |
| Asset inventory and registration | Engineering | Risk, Governance | `STD-AM-001`, FLOW F-03 | Fits Engineering as asset records and ownership are created during build/handoff; Risk validates coverage, Governance maps obligations. |
| Secure configuration baselines | Engineering | Risk, Governance | `STD-CFG-001`, FLOW F-01/F-05 | Fits Engineering as hardening implementation; Risk validates drift/exposure; Governance controls baseline authority. |
| Cryptography, certificates, keys, secrets | Engineering | Governance, Risk | `STD-CR-001`, PRC-CHG, PRC-AC | Fits Engineering as platform/control implementation; Governance owns policy conformance for regulated overlays. |
| CUI handling | Governance | Engineering, Risk | `STD-CUI-001`, CUI plan references | Cross-pillar regulated package, but primarily Governance because boundary, SSP, POA&M, evidence, and CMMC posture dominate. Engineering/Risk activities are embedded. |
| Data classification and handling | Governance | Engineering, Risk | `STD-DG-001`, Story 1, Story 7 | Fits Governance as rule and classification authority; Engineering and Risk consume classification for design and assessment. |
| Endpoint and mobile controls | Engineering | Risk, Governance | `STD-EP-001` | Fits Engineering for endpoint baselines and EDR platform control; Detection handoff remains Risk/IR boundary. |
| Cloud, SaaS, hosted IT security | Engineering | Risk, Governance | `STD-IT-001`, Story 1, Story 4 | Fits Engineering for architecture and control implementation; Risk handles vendor/posture exposure; Governance confirms conformance. |
| Logging, monitoring, and detection standard | Risk | Engineering, Governance, IR adjacent | `STD-LM-001`, OM role roster, RAC detection process | Fits Risk because detection is treated as exposure visibility and validation, not incident command. Engineering supplies sources, Governance owns retention/evidence rules. |
| Email and messaging controls | Engineering | Risk, Governance, Awareness adjacent | `STD-MSG-001` | Fits Engineering for platform controls; Awareness may consume phishing themes but does not become a CERG pillar. |
| Network segmentation and boundary control | Engineering | Risk, Governance | `STD-NET-001`, OT standard | Fits Engineering as architecture and implementation; Risk validates exposure paths. |
| OT/grid control systems security | Governance for regulated posture; Engineering for technical controls | Risk, IR/OT Ops adjacent | `STD-OT-001`, OM adjacent-function boundary | Fits three pillars because OT is an environment overlay, not a pillar. OT operations remain adjacent. |
| Cyber resilience and backup | Engineering | Governance, BC adjacent, Risk | `STD-RES-001` | Fits Engineering for backup/recovery control implementation; BCP remains adjacent business function. |
| Secure software development | Engineering | Risk, Governance | `STD-SDL-001`, PRC-AR, PRC-TM | Strong Engineering fit, with Risk threat modeling/validation and Governance gate/evidence rules. |
| Architecture review and project intake | Engineering | Risk, Governance | `PRC-AR-001`, FLOW F-02, Stories 1/4/7 | Strong Engineering fit. Risk joins for threat model and elevated exposure; Governance confirms conformance/evidence. |
| Threat modeling | Risk in current procedure ownership | Engineering, Governance | `PRC-TM-001`, `PRC-AR-001`, `STD-SDL-001` | Acceptable split. Risk facilitates exposure/adversary thinking; Engineering owns design changes. Needs clear local wording where threat modeling appears in Engineering SDLC. |
| Exposure management | Risk | Engineering, Governance | `PRC-VM-001`, FLOW F-04, Stories 2/8 | Strong Risk fit. It converts observations into validated exposure and treatment. |
| Adversarial validation | Risk | Engineering, Governance, IR adjacent | `PRC-AV-001`, FLOW F-04/F-07 | Strong Risk fit. Findings feed Engineering remediation and Governance reporting. |
| Threat intelligence | Risk | Engineering, Governance, IR adjacent | `PRC-TI-001`, OM core activities | Strong Risk fit. It feeds design, detection, policy, and IR without owning IR operations. |
| Third-party and supply chain risk | Risk | Governance, Engineering, Procurement adjacent | `PRC-TPRM-001`, Story 1, Story 6 | Strong Risk fit for assessment and vendor exposure; Governance handles contracts/evidence; Procurement remains adjacent. |
| Risk register and exception process | Governance operational owner with Risk inputs | Risk, Business Owner, CISO | `PRC-RM-001`, GEN conversion rules, RAC | Fits Governance as register/exception workflow owner. Risk supplies analysis; business/CISO accept residual risk. |
| Audit and evidence management | Governance | Engineering, Risk, auditors adjacent | `PRC-AUD-001`, Story 3 | Strong Governance fit. Evidence is a program control, not implementation. |
| Security change management | Engineering | Risk, Governance | `PRC-CHG-001`, FLOW F-05 | Strong Engineering fit. Risk reviews risk-significant changes; Governance checks evidence/conformance. |
| Incident response playbooks | Adjacent IR team | CERG supports through all three pillars | `PRC-IR-002`, FLOW F-06, Story 6 | Not a fourth CERG pillar. It is explicitly external interface/adjacent, with CERG support roles. |
| Lessons learned and program improvement | Governance | Engineering, Risk, IR adjacent | `PRC-LL-001`, FLOW F-07, Story 10 | Strong Governance fit as improvement register and oversight mechanism; source events come from all pillars. |
| Metrics, oversight, and board reporting | Governance/CISO | Engineering, Risk | `FRM-002`, FLOW F-07, OM cadence, Story 10 | Strong Governance fit with CISO accountability. Not a separate program-management pillar. |
| Small-team role consolidation | Cross-pillar operating mode | All | Story 8 | Supports the model: heads collapse, questions do not. |

## Candidate Fourth Pillar Stress Test

| Candidate fourth pillar | Evidence tested | Verdict | Reason |
|---|---|---|---|
| Incident Response | OM §3.4, FLOW F-06, PRC-IR-002, Story 6 | Adjacent function, not a CERG pillar | IR has its own command authority, plan, notification clocks, and Incident Commander. CERG contributes context, evidence, remediation, and lessons learned. |
| Security Awareness | FRM-001, OM interfaces, access/AI/story references | Adjacent function, not a CERG pillar | Awareness consumes Governance policy and Risk intelligence, but program ownership is separate. |
| Compliance | FRM-001, OM Governance mandate, PRC-AUD, CUI/OT/SOX docs | Sub-discipline inside Governance | Compliance without evidence and policy authority is not separate from Governance in CERG. Treating it as a fourth pillar would recreate GRC silos. |
| Detection | OM role roster, RAC, STD-LM, PRC-TI, PRC-IR | Sub-discipline inside Risk with IR handoff | Detection creates exposure/coverage intelligence and hands declared incidents to IR. It does not own incident command. |
| Architecture | OM, PRC-AR, standards | Sub-discipline inside Engineering | Architecture is the primary Engineering expression. It is not broad enough to own risk treatment, evidence, or oversight. |
| Workforce | JF/JD ecosystem in index, OM role roster | Cross-cutting workforce view | Workforce content supports accountability and role scaling; it is not an operating pillar. |
| Program Management | OM cadence, COG, metrics, Story 10 | Governance/CISO mechanism | The cadence is how the model operates. It does not own work separate from the pillars. |
| Privacy | OM adjacent functions, CUI/data docs | Adjacent function with Governance interface | Privacy has Legal/Privacy leadership; CERG supplies data classification, evidence, and breach support. |
| Business Continuity | OM adjacent functions, RES standard | Adjacent function with Engineering/Governance interface | CERG owns cyber resilience controls; enterprise BCP owns business continuity. |

Verdict on fourth pillars: no candidate justifies a fourth CERG pillar. The awkward work is either an adjacent function, an environment/regulatory overlay, a cross-pillar flow, or a workforce/support view.

## Specific Test Results

| Test | Result | Notes |
|---|---|---|
| Detection Engineer in Risk Operations | Holds with one workforce caveat | OM/RAC/STD-LM treat detection as coverage, triage, tuning, and handoff to IR. A02 identified likely JD content swap that could undermine this in role files. |
| Threat Intelligence in Risk | Holds | PRC-TI feeds Engineering, Governance, and IR through products, action tracking, and reprioritization without becoming IR ownership. |
| Standards technically authored by Engineering but approved through Governance | Holds, but depends on RAC-001 note | RAC-001 explicitly separates content/upkeep from catalog approval authority. Some metadata owners vary by standard, which B03 should test as authority duplication. |
| Governance owns evidence/conformance but not implementation | Holds | FRM-002 Story 2 explicitly says Governance does not patch. FLOW F-01/F-05 place implementation with Engineering. |
| Engineering owns implementation and pre-production, not post-production risk monitoring | Holds | OM production handoff and FLOW F-03/F-04 move ongoing exposure to Risk and evidence/reporting to Governance. |
| Risk owns findings/exposure but not business risk acceptance | Holds in spine, one example needs repair | RAC/RMF/GEN keep business/CISO acceptance distinct. Story 4 contains one sentence that can be read as Risk accepting residual risk. |

## Verdict

**Three-pillar model holds with repairs.**

The core conceptual decomposition survives aggressive testing. Every major activity in the standards, procedures, flows, and examples fits naturally into one of three questions:

1. Engineering: how do we build, change, or operate this securely?
2. Risk: what exposure remains and what treatment is required?
3. Governance: what rule, record, evidence, decision, or report governs this?

The repairs are local and mostly reader-protection issues: one example sentence blurs Risk versus acceptance authority, the machine-readable index currently labels all procedures as `risk`, and the workforce JD anomaly from A02 could make Detection/Vendor Risk role logic look wrong even though the operating model is sound.

## Findings

### B01-F01 High Story 4 wording implies Risk can accept residual risk
Affected files:
- `examples/day-in-the-life/README.md`

Problem: In Story 4, the narrative says: `Risk accepts one low residual risk around delayed DDoS exercise completion with a 30-day due date.` That wording makes Risk appear to be the acceptance authority for residual risk.

Why it matters: CERG's distinction is that Risk analyzes exposure and recommends treatment, while a Business Owner, CISO, or delegated authority accepts residual risk per RMF/RAC rules. Blurring that line would cause a reader to route risk acceptance to the wrong accountable role.

Evidence from corpus:
- `FRM-002` says Risk asks, `What exposure remains and what treatment is required?`
- `RAC-001` states risk acceptance approval follows `RMF-001` §9.7 and does not override acceptance authority.
- `GEN-001` defines Risk Acceptance as a documented decision by a Business Owner with approver, rationale, and review date.
- Story 4 uses `Risk accepts` instead of `Risk records`, `Risk recommends`, or `Business Owner accepts`.

Recommended action: Rewrite the Story 4 sentence to preserve the role boundary. Example: `Risk records one low residual launch risk around delayed DDoS exercise completion and recommends a 30-day treatment deadline. The Business Owner accepts the residual risk per the RMF authority path, and Governance records the exception as time-bound and visible in reporting.`

Owner/workstream: Examples / Risk vocabulary.

### B01-F02 Medium Machine-readable index classifies all procedure documents as Risk pillar
Affected files:
- `machine-readable/cerg-llm-index.json`
- source or logic behind `tools/regenerate-llm-index.py`

Problem: The LLM index classifies all 12 procedure files with `pillar: risk`, even when the document owner and operating content are Engineering-led, Governance-led, or External Interface. Examples: `PRC-AR-001` and `PRC-CHG-001` are Engineering-led; `PRC-AUD-001` and `PRC-LL-001` are Governance-led; `PRC-IR-002` is owned by the Standing IR Team / Incident Commander.

Why it matters: Human readers using Markdown can recover the correct ownership, but LLM and automation workflows may select or summarize procedures by pillar. Labeling all procedures as Risk weakens the machine-readable expression of the three-pillar model.

Evidence from corpus:
- A01/A02 index counts show `procedure | risk` for all procedure documents.
- Procedure metadata owners include `Engineering Pillar Leader`, `Identity Engineer`, `Governance Pillar Leader`, `Risk Register Owner`, `Vendor Risk Analyst`, `Exposure Management Lead`, and `Standing IR Team / Incident Commander`.
- RAC-001 and FLOW-001 assign procedure execution across all three pillars.

Recommended action: Update the index generation logic to derive procedure pillar from document metadata, canonical owner, or a maintained override table. If `pillar` is intended as document-family grouping rather than operational ownership, add a separate field such as `primary_operating_pillar`.

Owner/workstream: Machine-readable / Pillar Logic.

### B01-F03 Medium Detection/Vendor role JD anomaly threatens a pillar stress test even though the model holds
Affected files:
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md`

Problem: A02 found the Detection Engineer JD sample duties appear vendor-risk oriented, while the Vendor Risk Analyst JD sample duties appear detection-oriented. B01 did not perform the full D01 workforce reconciliation, but this anomaly directly affects the required detection stress test.

Why it matters: The operating model and RACI correctly place Detection Engineer in Risk Operations as coverage and exposure intelligence, not IR ownership. If the role file is wrong, readers using workforce artifacts may think the model is inconsistent.

Evidence from corpus:
- OM-001 and RAC-001 define Detection Engineer as detection-rule authoring, ATT&CK coverage, tuning lifecycle, logging/monitoring coverage, and incident handoff.
- A02 scan found `JD-RISKOPS-004_Detection_Engineer.md` beginning with vendor tiering and vendor assessments, and `JD-RISKOPS-007_Vendor_Risk_Analyst.md` beginning with detection rules, SIEM, EDR, NDR, cloud detection platforms, and ATT&CK.

Recommended action: Confirm in D01. If confirmed, swap or rewrite the affected JD responsibility and knowledge sections before relying on workforce artifacts for training or adoption.

Owner/workstream: Roles.

## Positive Confirmations
- The three-pillar mission language is stable across README, FRM-001, FRM-002, and OM-001.
- The strongest operational phrasing is FRM-002's three-question model. It should remain central: build/operate securely, exposure/treatment, rule/evidence/decision/report.
- No tested activity requires a fourth pillar. Incident Response and Awareness are properly adjacent; Compliance is inside Governance; Detection and Threat Intelligence are inside Risk; Architecture is inside Engineering.
- Day-in-the-life examples generally strengthen the model by showing records, evidence, metrics, and improvement loops rather than abstract roles.
- Small-team consolidation in Story 8 reinforces the model rather than weakening it: one person may hold multiple roles, but the questions and records remain distinct.

## Open Questions
- Should the phrase `Risk accepts` be prohibited in examples and replaced with `Risk records`, `Risk recommends`, or `Risk validates` unless the Risk role is explicitly an approved RMF acceptance authority?
- Should the LLM index distinguish `document taxonomy pillar` from `operating accountability pillar` so standards/procedures can be grouped by library type without distorting ownership?
- Should `FRM-002` be treated as the canonical short explanation of the pillar questions, with other documents explicitly deferring to its wording to prevent mission-statement drift?

## Proposed Next Tasks
- B02: test adjacent-function boundaries, especially IR, Awareness, Privacy, BCP, Legal, ERM, IT, OT, and business ownership.
- B03: build the authority register and test duplicate authority locations, especially role roster, RACI, risk acceptance, record definitions, and evidence rules.
- D01: confirm and repair the Detection Engineer / Vendor Risk Analyst role-file anomaly.
