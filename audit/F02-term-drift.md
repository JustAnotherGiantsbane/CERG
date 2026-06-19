# Task F02 Output: Detect inconsistent terms, role names, and record names

## Scope Reviewed
- Files read:
  - `audit/F01-voice-vocab-inventory.md`
  - `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - Search results across `README.md`, `START-HERE.md`, `governance/`, `standards/`, `procedures/`, `plans/`, `templates/`, `roles/`, and `examples/`.
- Sections reviewed:
  - F01 preferred/discouraged terms, role names, record names, and exact-definition terms.
  - GEN-001 §3-6 canonical terms, record types, conversion rules, and role names.
  - FLOW-001 §1-7 operating principles, record definitions, canonical roles, and decision classes.
  - Targeted source lines where searched terms appeared in ambiguous or high-risk contexts.
- Files intentionally not reviewed:
  - Every occurrence of high-volume words such as `risk`, `finding`, `evidence`, and `record` line by line. These terms have hundreds or thousands of legitimate hits. F02 classified meaningful drift patterns rather than enumerating every occurrence.
  - Generated machine-readable artifacts. This task focuses on human Markdown language.

## Method
- Steps performed:
  1. Searched the exact terms required by the F02 task across governed Markdown and examples.
  2. Counted hits by file to identify high-use and high-risk terms.
  3. Reviewed representative contexts for ambiguous terms and likely drift.
  4. Classified each term category as correct canonical use, acceptable generic use, synonym to replace, ambiguous, or wrong.
  5. Produced a replacement table with context-specific guidance and noted where global replacement is unsafe.
- Search terms or scripts used:
  - `security team`, `GRC`, `compliance team`, `risk owner`, `system owner`, `asset owner`, `technical owner`, `business owner`, `finding`, `vulnerability`, `risk`, `exception`, `waiver`, `deviation`, `acceptance`, `artifact`, `evidence`, `record`, `ticket`, `control owner`, `process owner`, `responsible`, `accountable`.
  - Case-insensitive `rg` scans and a Python count script across Markdown files.
- Assumptions avoided:
  - Did not assume every generic word is wrong. `security team` is acceptable when describing team size; it is weak when assigning work.
  - Did not recommend blind global replacements. Most changes need local context.
  - Did not treat regulatory `deviation` as the same as CERG `Security Exception Record`; both can be valid but must be distinguished.

## Term Drift Table

| Term / pattern | Classification | Observed use | Recommended treatment | Safe global replacement? |
|---|---|---|---|---|
| `security team` | Acceptable generic in staffing/adoption; wrong as activity owner | Used in README/START-HERE, adoption guides, FRM, RMF, AUD. Often means headcount or business-side separation; sometimes could hide ownership. | Keep when discussing team size or security function generally. Replace when assigning work with CISO, Engineering Pillar, Risk Pillar, Governance Pillar, or canonical role. | No |
| `GRC` | Acceptable for tools/certifications; wrong as team/owner shorthand | Mostly appears as `GRC platform`, `GRC tool`, certification track, or traditional GRC contrast. | Keep for tool category or professional domain. Do not use as owner. Use Governance Pillar Leader, Evidence Librarian, Compliance Manager, or Risk Register Owner. | No |
| `compliance team` | Mostly acceptable generic/organizational scale; weak as owner | Appears in FRM and workforce docs for larger org structures. | Keep only when describing a generic org unit. For CERG work, use Governance Pillar, NERC-CIP Compliance Manager, CMMC / Federal Compliance Manager, or SOX ITGC Lead. | No |
| `risk owner` | Ambiguous | Used in POL/RMF/PRC-RM/IMP/VM/templates to mean business or asset accountable party; can be confused with Risk Register Owner or Risk pillar. | Prefer `Business Owner` for business consequence, `Asset Owner` for asset treatment accountability, `Risk Register Owner` for register curation. If `Risk Owner` remains, define it locally as Business/Asset Owner, not Risk pillar. | No |
| `system owner` | Ambiguous / synonym to replace | Appears in IMP-002, AC, TM, CUI/SOX plans/templates, Story 1. Meaning varies between business owner, asset owner, technical owner, and system security plan role. | Replace in CERG-owned operational text with Business Owner, Asset Owner, or Technical Owner. Keep only where a regulatory template requires `system owner`, and add mapping note. | No |
| `asset owner` | Correct canonical use | Common and generally aligned. | Keep. Where paired as `Business / Asset Owners`, split if decisions differ. | No |
| `technical owner` | Correct canonical/local project role | Mostly in FLOW, templates, and examples. | Keep for the person/team implementing or operating technical changes. Do not use for business risk acceptance. | No |
| `business owner` | Correct and important | Strong usage across RMF/PRC-RM/templates; some lowercase inconsistency. | Keep. Prefer capitalized `Business Owner` when used as the role. | Mechanical capitalization may be safe only after review. |
| `finding` | Mostly correct canonical use | High volume. Generally aligns to observed condition requiring disposition. | Keep. F02 concern is not raw usage but ensuring vulnerabilities do not skip triage into risks. | No |
| `vulnerability` | Mostly correct | High volume in exposure contexts. | Keep for technical weakness/raw input. Use Finding Record once triaged. | No |
| `risk` | High-volume exact-definition term | Mostly correct but broad. Drift appears in risk acceptance and `risk owner` contexts. | Keep only with clear distinction from finding/exception/acceptance. Use Risk Register Entry/Risk Record for durable object. | No |
| `exception` | Correct, but sometimes needs `Security Exception Record` | Core term used widely. Some places use `exception` as casual action (`close or exception top remediation items`). | Use `Security Exception Record` when referring to the durable record; `exception workflow` for process; avoid `exception` as a verb. | No |
| `waiver` | Synonym to replace except where explaining synonym | Appears in STY avoid-list, IMP warning, OM ask, and TMPL-RM-002 title/body. | Replace operational uses with `Security Exception` or `Security Exception Record`. Keep only in explanatory text like `not a regulatory waiver` or if explicitly saying adopters may call it waiver locally. | No |
| `deviation` | Mixed: correct regulatory term; ambiguous as generic exception | Correct for NERC-CIP/CIP deviation process and baseline deviation. RMF uses `Exception / Deviation` together. | Keep `deviation` for regulatory or baseline deviation contexts. Use `Security Exception Record` for CERG exception workflow. Clarify when both are required. | No |
| `acceptance` / `accepted risk` | Mostly correct, with known high-risk stale role wording | Strong in RMF/PRC-RM/templates; stale in RAC/roles/examples where security roles appear to hold risk-acceptance authority. | Use `Risk Acceptance Request`, `Risk Acceptance Memo`, or `Business Owner acceptance`. Avoid casual `accepted risk` without owner, approver, expiration/review date. | No |
| `artifact` | Generally acceptable for documents/templates | Used by CAT/STY and adoption docs. | Keep for governed document/template object. Use `record` for operational system-of-record object; use `evidence` for proof. | No |
| `evidence` | Correct and strong | High-volume, generally central to CERG voice. | Keep. Ensure evidence is linked to record/source/period/owner. | No |
| `record` | Correct, but record names drift | High-volume. Strong canonical concept, but labels vary. | Keep. Align specific record names to CAT-002/FLOW-001. | No |
| `ticket` | Acceptable tool object; weak as authoritative record | Used in examples, CB, CMP, WFP, adoption docs. | Keep only as implementation/tool artifact. Pair with authoritative record: `audit intake log`, `Finding Record`, `Change Record`, `Evidence Index Entry`. | No |
| `control owner` | Ambiguous but sometimes necessary | Used in TRC, CB, AUD, templates. Can be meaningful for control testing but is not in core OM role list. | Define locally as the role accountable for operating/evidencing a specific control. Where possible map to canonical role or Business/Asset Owner. | No |
| `process owner` | Acceptable generic field, ambiguous as role | Low volume. Appears in FRM-002 authority table, CB, PRC-AUD, templates. | Keep as metadata only if process ownership is defined; otherwise use canonical role. | No |
| `responsible` | Acceptable in prose; weaker than RACI if assigning accountability | High volume but mostly normal English. | Use R/A tables or `owns/accountable` for decision authority. Use `responsible` for descriptive support duties only. | No |
| `accountable` | Correct CERG/RACI term | Generally used well. | Keep. Ensure exactly one accountable role where a RACI row is used. | No |

## Replacement Table

| Current wording | Replace with | Rationale |
|---|---|---|
| `the security team reviews / approves / owns` | Named canonical role or pillar | Avoids hiding ownership. |
| `GRC owns` | Governance Pillar Leader, Evidence Librarian, Risk Register Owner, or Compliance Manager | GRC is a discipline/tool category, not a CERG role. |
| `compliance team owns` | Applicable Compliance Manager or Governance Pillar Leader | Names the accountable role. |
| `system owner` | Business Owner, Asset Owner, or Technical Owner | These are distinct accountabilities in CERG. |
| `risk owner` | Business Owner or Asset Owner; Risk Register Owner for register operations | Prevents confusion between business accountability and Risk pillar operations. |
| `waiver` | Security Exception Record | CERG's controlled term is exception, except when discussing external/regulatory waiver language. |
| `baseline deviation` | Security Exception Record for CERG deviation; CIP deviation/mitigation plan for NERC-CIP | Separates internal control exception from regulatory process. |
| `accepted risk` | Risk Acceptance Memo / Risk Acceptance Request with Business Owner acceptance | Forces owner, rationale, authority, and review date. |
| `risk accepted by security` | Business Owner accepts residual risk; security assesses/recommends/approves per authority | Preserves RMF authority model. |
| `ticket` as proof of work | Authoritative record name plus ticket link | Ticketing can host a record; it is not automatically the record. |
| `Control implementation record` where F-01 is meant | Control Change Record, or define separate Control Implementation Record | Aligns FLOW/GEN/F01 vocabulary. |
| `Vendor assessment file` | Vendor Risk Assessment Record | Aligns CAT-002 and PRC-TPRM vocabulary. |
| `Audit request ticket` | Audit intake log / Audit Request Record, plus ticket ID if used | Makes the request auditable outside a ticketing tool. |
| `Reporting Metric Record` without metric ID | Named metric ID/value/source record | Makes metric closure reproducible. |
| `responsible control owner` | Named Control Owner mapped to canonical role | Avoids generic accountability in control testing. |

## No-Blind-Replacement List

The following terms require context review and should not be globally replaced:

- `security team`: often valid for headcount or separation from business owner.
- `GRC`: valid for tool/platform/certification references.
- `deviation`: valid for NERC-CIP and regulatory deviation processes.
- `ticket`: valid as a source system or work-tracking object.
- `risk owner`: may be valid in RMF tables, but should be clarified rather than blindly replaced.
- `system owner`: may be required by CUI/SSP/SOX templates, but should be mapped.
- `responsible`: common English and role descriptions; only problematic when it hides accountability.

## Findings

### F02-F01 High `Risk Owner` is ambiguous enough to blur business accountability and risk-register operations
Affected files:
- `governance/CERG-POL-001_Cybersecurity_Policy.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md`

Problem: `Risk Owner` appears as a business/asset accountability label, while `Risk Register Owner` is a Governance role and `Risk Pillar` performs assessment. In PRC-RM this is partly clarified as `Business / Asset Owners (Risk Owners)`, but elsewhere the term can be read as Risk pillar ownership or security ownership.

Why it matters: Risk acceptance is one of the most sensitive authority centers in CERG. Any ambiguity around risk owner can lead a reader to think security owns the business consequence or the Risk Register Owner accepts risk.

Evidence from corpus:
- PRC-RM role table uses `Business / Asset Owners (Risk Owners)`.
- RMF defines Risk Owner as accountable business unit or IT/OT operations leader responsible for treatment decision.
- IMP-003 spreadsheet schema has both `Business Owner` and `Risk Owner (Security)`, which can teach the wrong split.
- PRC-VM says `System / Asset Owners` accept residual risk, while RMF/PRC-RM center Business Owner acceptance.

Recommended action: Use `Business Owner` for business consequence and acceptance; use `Asset Owner` for asset treatment accountability; use `Risk Register Owner` for register curation. If `Risk Owner` remains in RMF/PRC-RM, define it locally every time as `Business Owner or Asset Owner, not the Risk pillar and not the Risk Register Owner`.

Owner/workstream: Vocabulary / Risk authority cleanup.

### F02-F02 High `System Owner` remains an ambiguous synonym for three different CERG roles
Affected files:
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`
- `procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md`
- `plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md`
- `plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md`
- `templates/CERG-TMPL-CUI-001_System_Security_Plan_Template.md`
- `examples/day-in-the-life/README.md`

Problem: `System Owner` appears in access approval, threat modeling, CUI/SSP, SOX, adoption, and examples. Depending on context it may mean Business Owner, Asset Owner, Technical Owner, application owner, or a regulatory SSP role.

Why it matters: A CERG reader must know who can make business-risk decisions, who implements technical treatment, and who owns asset posture. `System Owner` collapses those distinctions.

Evidence from corpus:
- IMP-002 minimum separation table uses `System Owner` as access approver and exception-conflict role.
- CUI/SSP templates use system-owner language because that is common in federal SSP context.
- Story 1 says the business sponsor identifies the `system owner`, then later relies on Business Owner decisions.

Recommended action: Replace `System Owner` in CERG-owned prose with Business Owner, Asset Owner, or Technical Owner. In regulatory templates where `System Owner` is expected terminology, add a mapping note: `System Owner maps to Business Owner / Asset Owner / Technical Owner depending on local SSP responsibility`.

Owner/workstream: Vocabulary / Role clarity.

### F02-F03 Medium Generic team labels are acceptable for staffing but weak for ownership
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md`
- `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`

Problem: `security team`, `compliance team`, and `GRC` are used in multiple ways. Many uses are valid, such as team size, organizational context, GRC platform, or certification track. They become weak when they assign work or accountability.

Why it matters: CERG's house voice depends on named owners. Generic team labels are a common path back to pre-CERG operating ambiguity.

Evidence from corpus:
- STY-001 explicitly says avoid `Security team` where a canonical role exists.
- AUD-001 says `The security team` is insufficient as evidence producer.
- FRM-001 says CERG can beat traditional GRC, which is a valid contrast.
- IMP-003 uses `security team` to describe headcount, which is acceptable.

Recommended action: Leave generic team labels in descriptive/team-size contexts. Replace them in owner/action contexts with canonical roles. F03 should flag paragraphs where generic labels hide ownership.

Owner/workstream: Vocabulary / House voice.

### F02-F04 Medium `waiver`, `deviation`, and `exception` need stricter boundaries
Affected files:
- `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`
- `governance/CERG-POL-001_Cybersecurity_Policy.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`

Problem: `Exception` is CERG's canonical term for temporary control deviations. `Deviation` is also valid in regulated contexts, especially NERC-CIP. `Waiver` appears in the Security Exception template title/body and OM example language. Without clearer boundaries, readers may treat an internal exception, a regulatory deviation, and a waiver as interchangeable.

Why it matters: Regulatory deviations can carry obligations beyond CERG exception tracking. Conversely, calling an exception a waiver can imply permanence or external approval that does not exist.

Evidence from corpus:
- STY-001 says use `exception`, avoid `waiver` unless parent process uses it.
- TMPL-RM-002 subtitle includes `Waiver Request`, and body says temporary security exception or waiver request.
- IMP-002 correctly warns risk acceptance is not a regulatory waiver.
- POL/RMF/PRC-RM correctly distinguish NERC-CIP deviation processes in many places.

Recommended action: Make `Security Exception Record` the default internal term. Reserve `deviation` for regulatory or baseline-deviation contexts and explicitly state when a CIP deviation/mitigation plan is required in addition to the Security Exception Record. Remove or qualify `waiver` in TMPL-RM-002 unless the author intentionally supports local waiver terminology.

Owner/workstream: Vocabulary / Exception discipline.

### F02-F05 Medium `ticket` is useful as a tool object but should not replace authoritative records
Affected files:
- `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `examples/day-in-the-life/README.md`
- `governance/CERG-GOV-IMP-004_Implementation_Cards.md`
- `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md`

Problem: `Ticket` appears as a work-tracking object, evidence source, and sometimes as the record itself. CAT-002 allows ticketing systems to host findings, vulnerabilities, exceptions, changes, and improvements if required fields are preserved. But examples and control evidence tables sometimes say `audit request ticket`, `reconciliation tickets`, or `remediation tickets` where the authoritative CERG record should be named.

Why it matters: A ticket may hold the record, but a ticket ID alone does not guarantee required fields, evidence links, owner, decision, closure rationale, or metric source.

Evidence from corpus:
- CAT-002: ticketing system is acceptable only if required fields are preserved and reports exportable.
- Story 3 uses `Audit request ticket` as the record/evidence.
- CB-001 lists several evidence sources as tickets.
- FRM-001 Definition of Done says a ticket moving columns is not completion.

Recommended action: Use authoritative record names first, then ticket ID/tool as hosting detail. Example: `Audit Request Record in the audit intake log, hosted in ServiceNow ticket AUD-2026-001`.

Owner/workstream: Vocabulary / Record discipline.

### F02-F06 Medium Canonical record names drift between FLOW-001, CAT-002, FRM-002, and examples
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-9-f-01-control-intent.md`

Problem: CERG's record-centered language is strong, but specific record names vary. Examples include `Control Implementation Record`, `Control Change Record`, `Vendor assessment file`, `Audit request ticket`, and metric records without matching metric IDs.

Why it matters: Records are the traceability spine. If the same object has multiple names, operators cannot tell whether they are maintaining one durable record, a work ticket, a template, or an evidence attachment.

Evidence from corpus:
- F01 identified record labels as a remaining drift class.
- CAT-002 defines authoritative records such as Risk Register Entry and Security Exception Record.
- FLOW-001 uses flow-local records that do not always map cleanly to CAT-002 names.
- Story 9 is a strong control-intent example but should preserve a single F-01 record name consistently.

Recommended action: During G02/G03, create a record-name alignment pass. Choose canonical names in CAT-002, then update FLOW-001, FRM-002, and examples to use those names with aliases only where helpful.

Owner/workstream: Record vocabulary cleanup.

### F02-F07 Medium `control owner` and `process owner` need local definitions when used
Affected files:
- `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`
- `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`
- `templates/CERG-TMPL-AUD-002_Evidence_Request_Tracker.md`

Problem: `Control Owner` and `Process Owner` are useful operational labels, but they are not core CERG role-family names. If used without mapping, they can become shadow roles beside the canonical workforce model.

Why it matters: Control evidence, testing, and remediation require a clear accountable owner. A generic control owner can be valid, but only if the document maps that owner to an actual role or business function.

Evidence from corpus:
- TRC-001 uses `Control Owner` in missing-evidence and remediation contexts.
- CB-001 and AUD procedures use control/process owner language for test and evidence ownership.
- Templates include `Control Owner` fields.

Recommended action: Keep these terms where they are metadata fields. Add a short definition where used heavily: `Control Owner means the person or role accountable for operating and evidencing a specific control, mapped locally to a CERG role, Business Owner, Asset Owner, or process owner.`

Owner/workstream: Role vocabulary cleanup.

## Positive Findings

- CERG already has a strong exact-term backbone in GEN-001, FLOW-001, CAT-002, RMF-001, and PRC-RM.
- `Business Owner accepts residual risk; security does not accept business risk` is now a strong repeated phrase in RMF/PRC-RM/templates.
- `Evidence` and `record` are generally used as first-class operational concepts rather than after-the-fact audit attachments.
- `GRC` is usually used appropriately for tool/platform/domain context rather than as the primary operating model.
- `Exception` is already the dominant term; `waiver` is limited and repairable.

## Candidate Cleanup Queue

### Priority 1: Authority-sensitive vocabulary
1. Clarify or replace `Risk Owner` across RMF, PRC-RM, VM, IMP-003, and templates.
2. Replace or map `System Owner` where it means Business Owner, Asset Owner, or Technical Owner.
3. Fix known `Risk accepts` or security-role acceptance language in examples and role/RACI artifacts.

### Priority 2: Record-name alignment
1. Align CAT-002, FLOW-001, and FRM-002 record names.
2. Update day-in-the-life examples so tickets point to named CERG records.
3. Add alias notes only where useful for adopter tooling.

### Priority 3: Weak generic-owner cleanup
1. Review paragraphs using `security team`, `compliance team`, or `GRC` as sentence subject.
2. Replace only when the term performs an ownership/action role.
3. Preserve descriptive team-size and tool-context usage.

## Global Replacement Guidance

Do not run global replacements for this workstream. The only safe mechanical pattern after manual review is capitalization normalization for exact role names, for example changing `business owner` to `Business Owner` when the phrase is clearly the CERG role. Even that should be reviewed because some sentences use the phrase generically.

Recommended rewrite discipline:
1. Identify the sentence's operational object: finding, vulnerability, risk, exception, evidence, record, ticket, or metric.
2. Identify the decision authority: Business Owner, Asset Owner, Technical Owner, CISO, pillar leader, Risk Register Owner, Evidence Librarian, or compliance manager.
3. Identify the durable record: Risk Register Entry, Security Exception Record, Finding Record, Change Record, Evidence Index Entry, Vendor Risk Assessment Record, or other CAT-002 record.
4. Rewrite the sentence so the owner, decision, record, and evidence are explicit.

## Suggested Rewrite Examples

| Before | After |
|---|---|
| The security team accepts the residual risk. | The Business Owner accepts the residual risk under RMF-001 §9.7; Risk documents the assessment and Governance records the acceptance in the risk register. |
| The GRC team tracks exceptions. | The Risk Register Owner maintains the Security Exception Record and reports expired exceptions to the Governance Pillar Leader. |
| The system owner approves the exception. | The Business Owner approves the residual-risk decision; the Asset Owner approves the treatment plan for the affected asset. |
| Open a waiver ticket. | Create a Security Exception Record and link the implementation ticket that tracks compensating-control work. |
| Close the remediation ticket when done. | Close the Finding Record only after remediation evidence is linked, the owner validates the control state, and the source ticket is updated. |
| Upload evidence to the audit request ticket. | Create an Evidence Index Entry with source, period, owner, and reviewer; link the audit intake ticket as the workflow container. |

## Handoff Notes for G02/G03

- F02 should feed the governed-document rewrite queue, especially RMF/PRC-RM/VM/IMP-003, FLOW/CAT-002/FRM-002, and the day-in-the-life examples.
- Do not treat this as a style-only issue. The highest-risk drift affects decision authority and record traceability.
- Coordinate this cleanup with D01/D02 findings on stale risk-acceptance authority and the Detection Engineer/Vendor Risk Analyst role swap.
- If CAT-002 is updated, regenerate machine-readable artifacts after governed source edits.
