# Task F03 Output: Identify prose that violates house voice

## Scope Reviewed
- Files read:
  - `audit/F01-voice-vocab-inventory.md`
  - `audit/F02-term-drift.md`
  - Spine documents: `README.md`, `START-HERE.md`, `governance/CERG-GOV-FRM-001_CERG_Framework.md`, `governance/CERG-GOV-FRM-002_Framework_System_Map.md`, `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`, `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`, `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`, `governance/CERG-GOV-GEN-001_CERG_Glossary.md`, `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`, `examples/day-in-the-life/README.md`.
  - Artifact samples:
    - Policy: `governance/CERG-POL-001_Cybersecurity_Policy.md`
    - Standard: `standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md`, `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md`
    - Procedure: `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`, `procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md`, `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
    - Plan: `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`, `plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md`
    - Template: `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
    - Role JD: `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`, `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md`
    - Examples: `examples/day-in-the-life/README.md`, `examples/day-in-the-life/story-8-cerg-lite-maria.md`, `examples/day-in-the-life/story-10-new-ciso-90-days.md`
- Sections reviewed:
  - F01 house voice rules, discouraged verbs, preferred role names, and sentence patterns.
  - Spine document introductions, pillar descriptions, flows, record/role passages, and example instructions.
  - Representative document-control sections and role JD competency/management sections.
  - Search-result contexts where terms such as `ensure`, `responsible for`, `coordinate`, `supports`, `stakeholders`, `where applicable`, `as needed`, `industry standard`, and `security team` appeared.
- Files intentionally not reviewed:
  - Every line in all 162 Markdown files. F03 is a house-voice scan, not a full copyedit.
  - Generated machine-readable files.
  - Full per-role JD corpus. A02/D01/D02 already identified broad JD readability and role-content issues; F03 sampled representative JD prose.

## Method
- Steps performed:
  1. Used F01 as the target voice model: operational, owner-centered, evidence-centered, active, and readable by small teams.
  2. Reviewed spine documents first for tone-setting passages.
  3. Reviewed at least one sample from each artifact type.
  4. Ran broad scans for weak-pattern words and phrases.
  5. Manually classified representative passages into F03 categories.
  6. Drafted CERG-voice rewrites for each weak passage.
- Search terms or scripts used:
  - `ensure`, `ensures`, `responsible for`, `as appropriate`, `where applicable`, `may be`, `should be`, `should ensure`, `stakeholders`, `coordinate`, `supports`, `supporting`, `collaborate`, `robust`, `best practice`, `industry standard`, `comprehensive`, `alignment`, `leverage`, `utilize`, `security team`.
  - `rg -n -C 2` for representative contexts.
  - Python count script across `README.md`, `START-HERE.md`, `governance/`, `standards/`, `procedures/`, `plans/`, `templates/`, `roles/`, and `examples/day-in-the-life/`.
- Assumptions avoided:
  - Did not treat every weak-pattern word as a defect. `where applicable` is often appropriate in regulatory metadata. `stakeholders` is often legitimate in management/competency documents. `supporting documents` is metadata, not weak voice.
  - Did not score legalistic `shall` language as automatically bad in policies and standards.
  - Did not recommend removing slogan lines where the following text operationalizes them.

## Findings

### F03-F01 Medium Document-control boilerplate weakens the owner-centered voice across many documents
Affected files:
- `standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md`
- `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md`
- `standards/CERG-STD-AC-001_Access_Management_Standard.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
- `procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
- Many other governed Markdown files using the same pattern.

Classification: passive voice hiding accountability / overlong boilerplate.

Quoted weak passages:
> `Cyber Engineering owns this document. The Engineering Pillar Leader (Platforms) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.`

> `Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.`

Problem: The first sentence is strong; the second falls back to `is responsible for` and compresses review, maintenance, approval routing, and endorsement into a long clause. The pattern is repeated so often that it becomes a house-voice tax.

Why it matters: Document-control sections teach how CERG governs itself. If they use weaker role/action language than the body, the framework ends each artifact in a less operational voice.

Evidence from corpus:
- F01 discourages `responsible for` when it can be replaced with `owns`, `operates`, `routes`, or `approves`.
- The repeated boilerplate appears in standards, procedures, governance instruments, plans, and JDs.
- The problem is style-first, not operationally severe; ownership is usually still identifiable.

Recommended action: Create a standard document-control sentence pattern and update mechanically with review. Example rewrite:

> `Cyber Engineering owns this standard. The Engineering Pillar Leader (Platforms) runs the annual review, records revision decisions, routes changes to the Governance Pillar Leader for approval, and obtains CISO endorsement before publication.`

Owner/workstream: G03 voice normalization / STY-001 document-control pattern.

### F03-F02 Medium `where applicable` and `as needed` are harmless in metadata but weaken adoption instructions when they decide scope
Affected files:
- `START-HERE.md`
- `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`

Classification: vague ownership / compliance boilerplate when used as scope logic.

Quoted weak passages:
> `Layer core standards next: Access Management, Asset Management, Configuration Baseline (DISH), IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup.`

> `MVC (all 8) + Access, Asset, Config Baseline, IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup standards + Architecture Review Procedure, TPRM Procedure.`

> `The CISO maintains the following pre-arranged external retainers, activated by the IC as needed:`

Problem: `Where applicable` and `as needed` are reasonable in regulatory applicability tables, but adoption and operational instructions should tell the reader who decides applicability and what record captures it.

Why it matters: CERG should help small teams avoid guessing. When scope turns on `where applicable`, a new adopter may skip a standard without creating a scope decision, risk register entry, or adoption backlog item.

Evidence from corpus:
- F01 requires paragraphs to answer who owns work, what must happen, and what record proves it happened.
- START-HERE is a high-traffic entry point for adopters.
- IMP-001/IMP-002 already have stronger adoption-decision language; START-HERE can point readers there.

Recommended action: Keep `where applicable` in metadata and standard rows when it describes regulatory/environmental conditions. Rewrite adoption instructions to name a decision and record. Example rewrite:

> `The CISO or Governance Pillar Leader records whether IT/Cloud/SaaS applies in the adoption backlog. If the organization uses cloud services, SaaS, or managed platforms, add STD-IT-001 before expanding beyond the MVC.`

For retainer activation:

> `The Incident Commander activates the retainer when the Incident Action Log shows a capability gap, surge-capacity need, or independent-investigation requirement.`

Owner/workstream: G03 entry-point rewrite / adoption clarity.

### F03-F03 High IR plan body still uses ownership prose that conflicts with the adjacent-function boundary
Affected files:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`

Classification: operational ambiguity, not just style.

Quoted weak passage:
> `Governance Pillar Leader | Owns the regulatory notification clock; maintains the SSP / POA&M impact tracking; coordinates with Legal on privilege; supports evidence preservation; assembles the post-incident report.`

Problem: The IR plan has a strong adjacent-function banner saying the standing IR team owns incident response, regulatory notification clocks, and exercise management. The body then says the Governance Pillar Leader owns the regulatory notification clock. This is not merely an active/passive voice problem; the sentence changes authority.

Why it matters: During an incident, ownership wording can change behavior. CERG should not appear to command incident notification decisions when the IR plan says the standing IR team and Incident Commander own active incident operations.

Evidence from corpus:
- B02 already identified the IR boundary contradiction.
- OM-001 says CERG coordinates/supports but does not own IR operations or notification clocks.
- The banner in PLN-IR-001 and PRC-IR-002 is clearer than this body row.

Recommended action: Rewrite the row to preserve CERG support while naming the Incident Commander/standing IR team as owner. Example rewrite:

> `Governance Pillar Leader | Tracks regulatory-notification evidence, SSP/POA&M impacts, and reporting artifacts under Incident Commander direction; coordinates with Legal on privilege-sensitive evidence handling; prepares the post-incident evidence package for lessons learned and audit use.`

Owner/workstream: G02/G03 IR boundary cleanup.

### F03-F04 Medium Example tables sometimes use `coordinates` where CERG should name the exact handoff or record update
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `examples/day-in-the-life/story-6-supplier-incident.md` if retained in the example set.

Classification: vague ownership / generic security advice.

Quoted weak passages:
> `Engineering owns remediation planning and coordinates patching, configuration change, WAF rule, or service isolation.`

> `Risk coordinates vendor questions, exposure analysis, and whether the event becomes an internal incident.`

> `He coordinates a same-day maintenance window with the Operations Director.`

Problem: `Coordinates` can be useful in narrative, but in flow tables it hides the actual CERG action: route, request, approve, update, validate, escalate, or record.

Why it matters: Examples are teaching artifacts. If examples use coordinator language at decision points, readers may copy the vagueness into procedures.

Evidence from corpus:
- F01 discourages `coordinates` when it hides ownership.
- E01/E03 identified the best examples as those that show records and decisions explicitly.
- Story 8 also has known Critical vendor exception issues; vague coordination makes that harder to see.

Recommended action: In example flow tables, replace `coordinates` with the concrete action. Example rewrites:

> `Engineering opens the Change Record, selects the treatment path, requests the approved maintenance window, and records the implemented patch, WAF rule, configuration change, or isolation step.`

> `Risk sends the vendor questionnaire, records the vendor response deadline in the Vendor Risk Assessment Record, and opens an Incident Commander consultation if internal incident criteria may be met.`

> `Devin requests same-day approval from the Operations Director and records the maintenance window in the Change Record.`

Owner/workstream: G03 example rewrite / day-in-the-life voice cleanup.

### F03-F05 Medium Role JD competency rows are operationally rich but too dense for human scanning
Affected files:
- `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md`
- `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md`
- Likely all per-role JD files populated from common competency and management-track sections.

Classification: overlong explanation.

Quoted weak passages:
> `At L3+ (SME track), a Management track option may be available per [CERG-GOV-JA-001] §8.1 (SME to Management Transition). Readiness indicators include: consistently sought out for guidance by junior team members, leading cross-functional initiatives without formal authority, and communicating clearly with non-technical stakeholders. The transition is a track change, not a grade promotion — an S3 Advisor moving to M1 Manager carries their technical credibility into the management role. Management competencies are defined in [CERG-GOV-CMP-001] §7. See [CERG-GOV-JA-001] §5 for Management grade definitions (M1-M4) and §9 (Span of Control and Team Design) for when to create a management role.`

> `Writes clear ticket updates and status reports. Explains a technical finding to their immediate team without ambiguity. | Writes architecture review findings that a project manager or business owner can understand and act on. Presents technical topics to their pillar. Authors clear, usable procedures. Communicates technical trade-offs to non-engineering audiences. | Represents Engineering in cross-functional forums with credibility...`

Problem: These sections are technically valuable, but the row/paragraph density makes them hard to use as job descriptions. The content reads like generated competency payload rather than CERG's crisp operational voice.

Why it matters: JDs are reader-path artifacts for hiring, onboarding, and role clarity. Dense rows can bury the behaviors that distinguish roles and seniority levels.

Evidence from corpus:
- A02 already found long-bullet readability issues affecting 25 files.
- D01/D02 identified role-content issues that require careful JD review.
- F01 says prose should be practical and readable by a small team.

Recommended action: Do not rewrite every JD manually until the role-swap issue is fixed. After that, normalize JD sections with a more scannable pattern: short bullet lists per level, one behavior per bullet, and cross-reference to CMP-001 for full detail. Example rewrite for the management-track paragraph:

> `At L3+ on the SME track, this role may move to Management under JA-001 §8.1. The move is a track change, not an automatic promotion. Readiness evidence includes: recurring guidance to junior staff, successful cross-functional leadership without formal authority, and clear communication with non-technical leaders. Use CMP-001 §7 for management competencies and JA-001 §5/§9 for grade and team-design rules.`

Owner/workstream: Workforce readability cleanup after D01 role-content repair.

### F03-F06 Low Some slogan and marketing-adjacent lines are acceptable but should be paired with operational consequences
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`
- `examples/day-in-the-life/README.md`

Classification: adoption marketing / slogan without operational consequence when isolated.

Quoted passages:
> `A spine, not shelfware.`

> `Compliance alignment is a byproduct of operating well.`

> `Set the rules. Track the work. Enable the business to move with confidence.`

> `Add Architecture Review and TPRM procedures. These are the two procedures that prevent the most future pain.`

Problem: These lines are memorable and generally fit CERG's public voice. The weakness appears only when the surrounding paragraph does not immediately translate the phrase into role, record, evidence, or next step.

Why it matters: CERG should sound confident but not vendor-like. A strong line earns its place when it teaches a concrete operating behavior.

Evidence from corpus:
- FRM-001 usually operationalizes mission slogans in the following sections.
- START-HERE's `future pain` line is human and useful, but it could be stronger if it named the pain: late findings, vendor surprises, and production exceptions.
- F01 says signature phrases should be used sparingly and only when surrounding text operationalizes them.

Recommended action: Keep the best slogans; sharpen nearby prose. Example rewrite:

> `Add Architecture Review and TPRM next. Architecture Review catches design risk before go-live; TPRM catches vendor risk before contract signature. Both create records that prevent late exceptions and emergency remediation.`

Owner/workstream: G03 entry-point polish.

### F03-F07 Medium `The security team` remains acceptable in audience descriptions but weak in evidence and procedure prose
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`

Classification: vague ownership.

Quoted weak passage:
> `The security team` is insufficient as evidence producer.

Problem: This exact line in AUD-001 is good because it gives a negative example. The broader pattern remains that `security team` appears in audience/team-size language and can leak into owner language. F02 covered term drift; F03 adds the voice point: it turns active CERG prose back into generic security prose.

Why it matters: The phrase is harmless when describing the intended audience, but weak when it is the grammatical subject of operational work.

Evidence from corpus:
- Search found 31 hits for `security team`.
- README and START-HERE use it mostly as audience/team-size language.
- STY-001 explicitly says to replace it with a pillar leader or canonical role where assigning work.

Recommended action: Preserve audience uses such as `small security team` and `established security team`. In procedures, evidence standards, examples, and flow tables, replace subject uses with the role that acts. Example rewrite:

> `The Evidence Librarian records the evidence producer by named role, system, and extraction date. A generic label such as security team is not sufficient.`

Owner/workstream: G03 house-voice cleanup; coordinate with F02 term cleanup.

### F03-F08 Low Standards are mostly declarative, but long compound requirements can bury evidence expectations
Affected files:
- `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md`
- `standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`
- `standards/CERG-STD-CUI-001_CUI_Handling_Standard.md`

Classification: overlong explanation / legalistic standard wording.

Quoted weak passage:
> `The model is an inventoried component. A model, whether trained in-house or a third-party model the application depends on, is a component recorded in the asset inventory per CERG-STD-AM-001, the AI system and model register using CERG-TMPL-AI-003 or an equivalent local record, and, where applicable, in the software bill of materials per CERG-STD-SDL-001 §8.`

Problem: The requirement is correct and important, but a single sentence contains three records, applicability logic, and cross-document references. A reader could miss the evidence expectation.

Why it matters: Standards are most useful when implementers can turn each requirement into a record/evidence check without parsing a long sentence.

Evidence from corpus:
- CERG standards generally perform well: they are more declarative than advisory.
- The weak passages are local density issues, not conceptual failure.

Recommended action: Split compound standards into direct bullets or a mini-table. Example rewrite:

> `Every AI model is an inventoried component. The Asset Owner records it in the asset inventory. The AI owner records model purpose, source, version, and data scope in the AI System and Model Register. If the AI application ships software or third-party components, Engineering also records the model dependency in the SBOM.`

Owner/workstream: G03 standard readability pass.

## Positive Confirmations

- The spine documents mostly already use CERG's strongest voice: named pillars, explicit handoffs, records, clocks, and decisions.
- STY-001 contains the right house-voice rules. The issue is uneven enforcement, not lack of guidance.
- FLOW-001 has the strongest repeatable prose pattern: trigger, owner, record, handoff, closure.
- Examples 2, 9, and 10 remain strong teaching examples because they show owner/action/record/decision chains.
- Policies and standards generally use declarative requirements; they need targeted readability cleanup, not a full voice rewrite.
- Marketing-adjacent lines in README/FRM are mostly acceptable because CERG balances them with operational content.

## Open Questions

- Should STY-001 define an approved Document Control owner sentence for all artifact types?
- Should START-HERE include a short `scope-decision record` step whenever it says `where applicable`?
- Should per-role JD competency rows remain fully expanded in each JD, or should they shorten locally and point to CMP-001 as the authoritative competency source?
- Should examples use only CAT-002 record names, or may they include friendly aliases with the canonical name in parentheses?

## Proposed Next Tasks

- Feed F03 findings into G03 as the voice-normalization backlog.
- Pair F03-F03 with B02 IR boundary cleanup; this is operational ambiguity, not mere style.
- Pair F03-F05 with D01 role-content repair before changing JD prose at scale.
- Use F03-F02 and F03-F06 when rewriting START-HERE and README in the refinement phase.
- Create a small style lint list for future author review: `responsible for`, `coordinates`, `ensure`, `where applicable`, `as needed`, and `security team` when used as an operational subject.
