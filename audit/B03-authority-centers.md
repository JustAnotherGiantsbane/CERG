# Task B03 Output: Identify duplicated or competing authority centers

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
  - `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
  - `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
  - `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md` by reference from PRC-RM
  - `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`
  - `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
  - `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`
  - `governance/CERG-GOV-CAT-002_Record_Catalog.md`
  - `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
  - `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` by A01/B01 extraction
  - `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`
  - `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md`
  - `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
  - `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- Sections reviewed: authoritative-owner statements, authority tables, role roster statements, record definitions, risk acceptance and exception workflows, evidence quality statements, document approval/status rules, IR External Interface statements, and SLC commitment rules.
- Files intentionally not reviewed: all local RACI tables in every standard/procedure. Those require a later D/C pass against RAC-001 at row level.

## Method
- Steps performed:
  1. Identified the document that claims or should claim canonical authority for each tested concept.
  2. Identified other documents that repeat, summarize, or operationalize the same concept.
  3. Classified repetition as safe summary, risky duplicate, contradiction, obsolete residue, or helpful reader aid needing pointer.
  4. Recommended keep, replace with cross-reference, move authority, merge, retire, or rewrite.
- Search terms or scripts used: targeted reads and scans for `single source of truth`, `authoritative`, `governs`, `canonical`, `authority`, `approval`, `acceptance`, `exception`, `record type`, `evidence`, `Incident Commander`, `External Interface`, `RACI`, and `owner`.
- Assumptions avoided: did not treat repetition as inherently bad. Repetition is acceptable where it orients readers and explicitly defers to the canonical source.

## Authority Register

| Concept | Canonical authority | Other locations repeating concept | Classification | Recommended action |
|---|---|---|---|---|
| Canonical role roster | `OM-001` §6.1 | `GEN-001` §6, `RAC-001` §4, CAT workforce catalog, per-role JDs | Safe summary with drift risk | Keep OM authoritative. GEN and RAC should state they are reference copies. D01 should verify role-file set. |
| RACI assignments | `RAC-001` | OM sample RACI patterns, local roles tables in standards/procedures/plans, examples | Safe in RAC, risky in locals | Keep RAC authoritative. Replace or label local RACI tables as reader aids that defer to RAC. |
| Document catalog and lifecycle status | `CAT-001` | Metadata tables, Document Control sections, manifests/indexes, STY-001 lifecycle guidance | Safe if synchronized | Keep CAT authoritative. Validator already enforces status sync. |
| Document structure and style | `STY-001` | AGENTS.md, document skeletons, existing documents | Safe summary | Keep STY authoritative. AGENTS is agent guidance, not source of truth. |
| Control baseline authority | `CB-001` | CMX, standards, procedures, FLOW F-01, CAT-002 records | Safe if standards remain subordinate | Keep CB authoritative for control set and evidence names; standards own detailed technical requirements. |
| Standards/procedure approval authority | `CAT-001` §4 | RAC-001 document ownership RACI, document metadata owners, Document Control sections | Helpful reader aid with mild drift risk | Keep CAT authority. RAC note explaining authorship vs approval is valuable and should stay. |
| Risk scoring and severity bands | `RMF-001` | `PRC-RM-001`, templates, FLOW F-04, examples | Risky duplicate | Align PRC-RM scoring calibration to RMF or explicitly mark PRC-RM as operational summary. |
| Risk acceptance authority | `RMF-001` §9.7 | OM decision rights, RAC, PRC-RM §8, AUD-001, TMPL-RM-003, TMPL-RM-004, examples | Mostly safe, one contradiction | RMF remains canonical. Fix TMPL-RM-003 and Story 4 wording. |
| Exception workflow | `PRC-RM-001` §7 with RMF authority reference | FLOW F-04, GEN conversion rules, TMPL-RM-002, AUD freshness/exception rules | Safe summary with conversion drift risk | Keep PRC-RM authoritative. FLOW/GEN should summarize and point back. |
| Finding to risk conversion | `GEN-001` + FLOW F-04, operationalized by PRC-VM/PRC-RM | PRC-VM, PRC-AV, PRC-AUD, examples | Helpful duplication requiring C03 test | Decide in C03 whether GEN or FLOW owns conversion definitions. Prefer GEN for vocabulary and FLOW for process. |
| Record type definitions and catalog | `CAT-002` should be canonical | `GEN-001`, `FLOW-001`, templates, examples | Competing authority labels | Make CAT-002 the authoritative record catalog. GEN defines terms; FLOW uses records in flows. |
| Evidence quality requirements | `AUD-001` | PRC-AUD, CB-001 evidence mapping, CAT-002, FLOW evidence tiers, SLC references | Safe summary | Keep AUD authoritative for quality, freshness, sampling; PRC-AUD owns collection and audit response. |
| Service-level commitments | `SLC-001` | OM engagement model, FLOW SLAs, PRC-AR, PRC-VM, MTR SR metrics | Safe but needs table polish | Keep SLC authoritative for CERG-to-business responsiveness, not remediation SLAs or risk decision clocks. |
| Incident ownership | `OM-001` §3.4 and External Interface headers | PLN-IR, PRC-IR, RAC incident rows, FLOW F-06, examples | Contradiction | Preserve standing IR team authority. Rewrite IR body/footer ownership conflicts. |
| Adjacent function boundaries | `OM-001` §3.4/§8 | PLN-IR, PRC-IR, PLN-PRIV, PLN-BC, FRM-001, examples | Mixed | Privacy and BCP are good. IR and Awareness need repair/operationalization. |
| Glossary vocabulary | `GEN-001` | FLOW operating principles, RMF, PRC-RM, AUD, examples | Safe if GEN defers where it says it defers | Keep GEN as vocabulary authority. Remove duplicate definitions elsewhere where they drift. |
| Machine-readable classification | Source Markdown plus regeneration scripts | `cerg-llm-index.json`, manifests, document tiers | Drift risk | Machine-readable artifacts should express, not reinterpret, source authority. Fix procedure pillar classification from B01. |

## Findings

### B03-F01 Critical Incident ownership has competing authority centers
Affected files:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: OM-001 and IR metadata/banners establish the standing IR team and Incident Commander as authoritative for incident operations, IR plan ownership, notification clocks, and exercise management. IR plan body/footer language and PRC-IR footer/exercise language assign some of that authority to CERG Governance or Risk.

Why it matters: This creates competing authority for an active incident, the highest-stress operating condition in the model. A reader could choose the wrong source and assign notification-clock or exercise accountability to Governance when the intended authority is the standing IR team/Incident Commander.

Evidence from corpus:
- OM-001 §3.4 says CERG does not own IR operations, the IR plan, regulatory notification clocks, or exercise management.
- PLN-IR and PRC-IR metadata show `External Interface` and owner `Standing IR Team / Incident Commander`.
- PLN-IR §3.1 and §6 assign notification clock ownership to Governance/Governance Lead.
- PLN-IR §11 assigns exercises and retainer/contact tests to Governance/Risk.
- PRC-IR §2.2 assigns exercise design to Governance Pillar Leader and PRC-IR Document Control says Cyber Governance owns the playbook set.

Recommended action: Canonical authority should be: `Standing IR Team / Incident Commander owns incident command, IR plan, notification-clock process, and IR exercise program. CERG Governance supports notification register/evidence and cross-reference hygiene.` Rewrite contradictory IR sections accordingly.

Owner/workstream: Adjacent Functions / Authority cleanup.

### B03-F02 High Risk acceptance memo template conflicts with RMF authority model
Affected files:
- `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`
- `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: RMF-001 §9.7 is the canonical risk acceptance authority and requires business owner acceptance at every business-impact level. TMPL-RM-004 correctly implements that model. TMPL-RM-003, however, has an approval table with Risk Register Owner, Risk Pillar Leader, CISO, and Executive Sponsor, but no Business Owner row. It is still cataloged and related from TMPL-RM-004 as a lightweight memo for Low/Medium risks.

Why it matters: Low and Medium risk acceptance still requires business ownership of consequence. A template that omits Business Owner acceptance can cause security to accept business risk, which the RMF explicitly prohibits.

Evidence from corpus:
- RMF-001 §9.7: Business Owner or Executive Sponsor accepts business consequence; security assesses and recommends.
- AUD-001 §7: every risk acceptance must include Business Owner Name and acknowledgement.
- TMPL-RM-004 §4 includes Business Owner, CISO, and Executive Sponsor rows.
- TMPL-RM-003 §4 omits Business Owner.

Recommended action: Prefer one acceptance template if possible. Either retire TMPL-RM-003 in favor of TMPL-RM-004, or rewrite TMPL-RM-003 as a Low/Medium memo that still requires Business Owner acceptance and references RMF-001 §9.7 and AUD-001 §7.

Owner/workstream: Risk / Templates.

### B03-F03 High Risk scoring calibration is duplicated and materially different between RMF and PRC-RM
Affected files:
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

Problem: RMF-001 and PRC-RM-001 both define likelihood, impact, and severity calibration. The concepts are similar but the numeric anchors differ. RMF uses LEF bands such as `Very High >10 events/year`, `High 1-10 events/year`, and impact bands such as Minor `$10K-$100K`, Medium `$100K-$1M`. PRC-RM uses annual probability bands such as Unlikely `5-20%`, Possible `20-50%`, and impact bands such as Minor `$50K-$250K`, Moderate `$250K-$1M`.

Why it matters: Different scoring anchors can produce different severity bands for the same risk. Severity drives treatment expectations, risk acceptance authority, reporting, and escalation. This is not just style drift.

Evidence from corpus:
- RMF-001 §9.5 claims the bands are the canonical CERG model and every document that scores risk must produce the same severity rating.
- PRC-RM-001 §4.3 carries a different quantitative calibration table.
- PRC-RM revision history says scoring bands were aligned to RMF, but the text still differs.

Recommended action: Keep RMF-001 as canonical for scoring and acceptance authority. Replace PRC-RM quantitative bands with a short operational pointer to RMF, or copy the RMF table exactly with an explicit `summary copy of RMF-001; RMF governs` note.

Owner/workstream: Risk / Authority cleanup.

### B03-F04 Medium Record type authority is spread across CAT-002, GEN-001, and FLOW-001
Affected files:
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Problem: Three documents present record-type definitions with authoritative language. CAT-002 is titled and written as the authoritative record catalog. GEN-001 defines record types and conversion terms as canonical vocabulary. FLOW-001 has a section titled `Authoritative Record Types` and embeds record definitions in flow operating principles.

Why it matters: Record names and ownership drive the evidence loop. If record definitions or owners diverge, readers may not know which source to follow. This matters especially for `Threat Model Record`, `Asset Record`, `Finding Record`, `Exception Record`, `Incident Record`, and `Improvement Record` ownership.

Evidence from corpus:
- CAT-002 §4 lists record types, primary owners, creating sources, triggers, and evidence value.
- GEN-001 §4 lists record types, owning pillar, and source of truth.
- FLOW-001 §3 lists authoritative record types and §2 defines several terms.
- Some entries use slightly different ownership framing, for example Threat Model Record as Risk/Engineering jointly in CAT-002 versus Engineering/Risk nuance in GEN-001.

Recommended action: Make CAT-002 the canonical source for record type, owner, source of truth, and required trigger. Make GEN-001 the canonical source for vocabulary definitions and conversion terms. Make FLOW-001 reference CAT-002 for the record catalog and list only the records required by each flow.

Owner/workstream: Records / Evidence.

### B03-F05 Medium Local and generated classification can compete with source-document authority
Affected files:
- `machine-readable/cerg-llm-index.json`
- `tools/regenerate-llm-index.py`
- source Markdown documents under `procedures/`

Problem: The machine-readable index classifies all procedure files as `pillar: risk` even where source-document owner, RAC-001, and FLOW-001 assign the procedure to Engineering, Governance, or External Interface. This creates a machine-readable authority center that disagrees with the human source documents.

Why it matters: CERG explicitly supports LLM and automation use. A generated index that misstates operating pillar can cause an LLM to route work incorrectly, even if the Markdown source is correct.

Evidence from corpus:
- B01 documented the all-procedure `pillar: risk` pattern.
- CAT-001 §4 and §5, RAC-001, and procedure metadata identify varied procedure owners.

Recommended action: Add a `primary_operating_pillar` derivation or override table to the index generator. Preserve document type grouping separately from operating accountability.

Owner/workstream: Machine-readable / Authority cleanup.

## Positive Confirmations
- RAC-001 correctly states the division of labor: OM owns role names, RAC owns assignment of work, and local tables must conform.
- CAT-001 is strong as document catalog and lifecycle authority. The validator confirms status/catalog/link consistency.
- AUD-001 is clear as evidence quality authority and PRC-AUD is clear as collection/audit-response procedure. That authority split is healthy.
- SLC-001 correctly says service commitments do not compress or override risk decisions. That protects RMF authority.
- CB-001 is strong as control baseline authority. It distinguishes control ownership, evidence names, overlays, and inheritance requirements.
- PRC-RM-001 §7.1 and TMPL-RM-004 show a strong modern distinction between security exceptions and risk acceptance.

## Open Questions
- Should TMPL-RM-003 be retired now that TMPL-RM-004 exists, or retained as a shorter Low/Medium memo with mandatory Business Owner acceptance?
- Should record-type definitions be removed from FLOW-001 entirely, or retained as local summaries with CAT-002 as explicit authority?
- Should the RMF 5x5 scoring model use FAIR LEF/LM bands everywhere, or should PRC-RM retain the simpler annual-probability language but point to RMF for final severity?
- Should generated machine-readable artifacts be validated against owner-to-pillar expectations as part of CI?

## Proposed Next Tasks
- C01: trace FLOW-001 flows after noting that record authority should point to CAT-002.
- C03: perform detailed conversion-rule review for finding, risk, exception, acceptance, and control gap.
- D01: verify role roster and JD alignment, including the Detection/Vendor role anomaly.
- G02/G03: add rewrite queue entries for IR authority, TMPL-RM-003, PRC-RM scoring alignment, and record-definition authority cleanup.
