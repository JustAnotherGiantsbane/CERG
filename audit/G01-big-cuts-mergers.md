# Task G01 Output: Big cuts and mergers review

## Scope Reviewed
- Files read:
  - Task instructions in `/workspace/thebigone.md` for G01.
  - Prior audit outputs: `audit/B01-three-pillar-logic.md`, `audit/C01-flow-trace.md`, `audit/F03-house-voice-findings.md`.
  - Spine and navigation documents: `README.md`, `START-HERE.md`, `governance/CERG-GOV-FRM-001_CERG_Framework.md`, `governance/CERG-GOV-FRM-002_Framework_System_Map.md`, `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`, `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`, `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`, `governance/CERG-GOV-GEN-001_CERG_Glossary.md`, `governance/CERG-GOV-CAT-002_Record_Catalog.md`.
  - Adoption documents: `governance/CERG-GOV-IMP-001` through `CERG-GOV-IMP-007`.
  - Workforce architecture documents: `roles/CERG-GOV-JF-001_Job_Families_Overview.md`, `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`, `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md`, `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md`, `governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md`, `governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md`, `governance/CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md`, `governance/CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md`, `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md`, representative per-role JD and family index files.
  - Day-in-the-life example index and representative promoted-example candidates.
- Sections reviewed:
  - G01 candidate areas: repeated pillar descriptions, local RACI content, glossary/definition repetition, adoption guidance spread, workforce architecture overlap, examples that repeat procedures, and old consolidated JD content.
  - Headings and document purposes for adoption and workforce clusters.
  - Search results for role/RACI/definition headings across standards, procedures, plans, and examples.
- Files intentionally not reviewed:
  - Full line-by-line review of every standard/procedure role table. G01 evaluates structural simplification candidates; G02/G03 will queue file-level rewrites.
  - Full role JD bodies. D/F workstreams already captured the major JD risks and readability issues.

## Method
- Steps performed:
  1. Identified duplication clusters named by the G01 task.
  2. Tested whether each repetition helps a reader orient or creates drift risk.
  3. Checked prior findings to distinguish structural simplification from local rewrite needs.
  4. Produced a big-cut candidate table with recommendation, effort, risk, and conceptual benefit.
  5. Prioritized human reader protection over raw line-count reduction.
- Search terms or scripts used:
  - Heading inventory across IMP, workforce, standards, procedures, plans, and role docs.
  - Searches for `three pillars`, `Cyber Engineering`, `Cyber Risk`, `Cyber Governance`, `Build securely`, `RACI`, `Responsible`, `Accountable`, `Roles and Responsibilities`, `Glossary`, `Definitions`, `Record Types`, and `Definition`.
- Assumptions avoided:
  - Did not assume repeated explanation is bad. CERG needs controlled repetition in front-door and workflow documents.
  - Did not recommend merging documents merely because they share a theme. Separate artifacts may support different reader moments.
  - Did not treat `retire` as safe unless catalog, links, and adoption paths could survive it.

## Big-Cut Candidate Table

| ID | Candidate duplication or structure | Affected files | Does it help the reader? | Drift risk | Recommendation | Effort | Risk | Conceptual benefit |
|---|---|---|---|---|---|---|---|---|
| G01-C01 | Repeated three-pillar descriptions across front-door and spine docs | `README.md`, `START-HERE.md`, `FRM-001`, `FRM-002`, `OM-001`, `FLOW-001`, examples | Yes, if each document uses a different reader lens | Medium | **Keep, but canonize the short wording and shorten secondary restatements** | Medium | Low | High |
| G01-C02 | Local RACI/roles sections in standards, procedures, and plans after RAC-001 became authoritative | Many standards/procedures/plans; `RAC-001` | Helps local execution, but full RACI tables can drift | High | **Shorten and point to RAC-001; keep only procedure-specific execution roles** | High | Medium | High |
| G01-C03 | Glossary and conversion definitions repeated in FLOW-001, GEN-001, CAT-002, RMF, PRC-RM | `GEN-001`, `FLOW-001`, `CAT-002`, `RMF-001`, `PRC-RM-001` | Helps where definitions are used immediately | High for record names and risk terms | **Split authority: GEN owns vocabulary; CAT-002 owns record names; FLOW uses compact operational crosswalk** | Medium | Medium | High |
| G01-C04 | Adoption guidance spread across seven IMP documents | `IMP-001` through `IMP-007`, `START-HERE.md` | Yes for different user moments, but entry path is crowded | Medium | **Keep set, but create a stronger adoption hub and merge/retire only after H01/H02 tests** | Medium | Low | Medium |
| G01-C05 | `IMP-001` rollout guidance overlaps with `IMP-005` decision tree and `IMP-006` role checklists | `IMP-001`, `IMP-005`, `IMP-006`, `START-HERE.md` | Partly; rollout, dependency, and checklist moments differ | Medium | **Shorten IMP-001 into a narrative overview; make IMP-005 the adoption-scope authority and IMP-006 the action authority** | Medium | Low | High |
| G01-C06 | `IMP-003` small-team role consolidation overlaps with RAC-001 scaling map and Story 8 | `IMP-003`, `RAC-001`, `FRM-002`, Story 8 | Yes; small teams need repetition | High because maps disagree per D03 | **Do not merge; synchronize and designate one canonical map** | Medium | Medium | High |
| G01-C07 | Workforce architecture split across JF, JA, CMP, PERF, TRN, SUCC, ONB, WFP, per-role JDs | Workforce docs and roles tree | Yes for HR lifecycle, but reader can get lost | Medium | **Keep separate lifecycle artifacts; add one workforce system map and remove duplicated competency payload from per-role JDs where possible** | High | Medium | High |
| G01-C08 | Per-role JDs duplicate CMP-001 behavioral anchors and JA-001 management-track guidance | All per-role JDs; `CMP-001`, `JA-001` | Some local context helps; full duplicated rows hurt readability | High | **Shorten per-role JD competency sections; point to CMP/JA as authority** | High | Medium | High |
| G01-C09 | `CERG-GOV-JD-001` old monolithic JD document now acts as index | `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md`, roles tree | Yes as compatibility/index | Low if clearly marked | **Keep as index/redirect for one major version; do not restore monolithic content** | Low | Low | Medium |
| G01-C10 | Family index docs (`*-000`) and JF-001 both explain families | `roles/*/*-000_*.md`, `JF-001` | Yes; family docs are local indexes | Low | **Keep; ensure family docs are thin indexes, not second family authorities** | Low | Low | Low |
| G01-C11 | Examples sometimes repeat procedure steps rather than demonstrate model behavior | `examples/day-in-the-life/README.md`, individual stories, related procedures | Yes for teaching, but too much procedure copy ages badly | Medium | **Shorten procedural duplication; promote stories that show decisions, records, evidence, and metrics** | Medium | Low | High |
| G01-C12 | FLOW-001 duplicates procedure-level SLA/closure rules | `FLOW-001`, `PRC-VM`, `PRC-CHG`, `PRC-AR`, `SLC-001` | Helps at flow level, but competing tables break execution | High | **Shorten FLOW to flow logic and defer detailed clocks/closure to procedures/SLC** | Medium | Medium | High |
| G01-C13 | Record definitions split across CAT-002 and FLOW-001 | `CAT-002`, `FLOW-001`, examples, templates | Yes only if FLOW uses aliases carefully | High | **Make CAT-002 canonical; FLOW holds record crosswalk and examples use CAT-002 names** | Medium | Medium | High |
| G01-C14 | Compliance/regulatory package guidance appears in START-HERE, IMP-005, plans, standards, and examples | `START-HERE.md`, `IMP-005`, plans, standards, examples | Yes at different depths | Medium | **Keep layered guidance; use IMP-005 as scope/dependency authority** | Low | Low | Medium |
| G01-C15 | OM-001 role roster overlaps with RAC-001 role descriptions and per-role JDs | `OM-001`, `RAC-001`, `JD-*` | Yes if each has different depth | High where role authority changes | **Keep three-tier model: OM roster, RAC authority, JD human role detail; remove authority detail from local copies** | Medium | Medium | High |

## Findings

### G01-F01 High RACI and role-accountability repetition should be shortened, not deleted
Affected files:
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- Standards under `standards/`
- Procedures under `procedures/`
- Plans under `plans/`
- `governance/CERG-POL-001_Cybersecurity_Policy.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`

Problem: Many artifacts contain local `Roles and Responsibilities` sections. They are useful at the point of work, but they can become alternate RACI authorities. Prior findings already show authority drift in IR ownership, risk acceptance, PRC-AR extension authority, and stale RAC document ownership rows.

Why it matters: CERG's operating promise is that a reader can identify who owns work. If every procedure carries a full local authority table, readers may get different answers depending on which document they opened.

Evidence from corpus:
- `RAC-001` explicitly says it is the single authoritative RACI and subordinate documents should be corrected if they disagree.
- Most procedures and many standards include local role sections.
- B/C/D findings show role/authority drift is one of the main remaining framework-quality issues.

Recommended action: Keep short local role sections, but constrain their purpose:
1. First sentence: `RAC-001 is authoritative for RACI; this section names procedure-specific execution duties.`
2. Local rows should name only actions needed to run the document.
3. Approval authority, risk acceptance authority, and canonical role descriptions should point to RAC/RMF/OM rather than be restated.
4. G02 should queue high-risk files first: IR, RM/VM, AR, TPRM, and policy role table.

Owner/workstream: G02 structural rewrite queue / role authority cleanup.

### G01-F02 High FLOW-001 should stop carrying competing procedure-level clocks and closure rules
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md`
- `procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md`

Problem: FLOW-001 is supposed to show how work moves across pillars. Some flows also carry detailed SLA and closure rules that duplicate or conflict with procedures. C01 found F-04's closure rules and SLA model conflict with PRC-VM.

Why it matters: A flow is a map; a procedure is the work instruction. When the map contains a different clock than the procedure, operators cannot know which governs.

Evidence from corpus:
- C01-F02: contradictory F-04 closure rules.
- C01-F03: F-04 severity SLA model conflicts with PRC-VM's canonical exposure-state SLA model.
- C01-F06: F-05 omits metrics that PRC-CHG defines, proving FLOW cannot reliably own every execution detail.

Recommended action: Make FLOW-001 own triggers, handoffs, required records, evidence checkpoints, and closure shape. Procedures/SLC own detailed clocks, treatment tables, and validation mechanics. FLOW may summarize with `see PRC-VM §7.2 for canonical exposure clocks` but should not publish a competing table.

Owner/workstream: G02 FLOW rewrite.

### G01-F03 High Record definitions need a single authority plus an alias strategy
Affected files:
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- Examples and templates using local record names.

Problem: CAT-002 claims to define canonical record types, while FLOW-001 and examples use flow-local names such as `Control Change Record`, `Project Intake Record`, `Risk Record`, and `Exception Record`. F02/C01 found record-name drift.

Why it matters: Records are the traceability spine. Duplicate labels for the same record make evidence, metrics, templates, and automation harder to align.

Evidence from corpus:
- CAT-002 contains authoritative record types and required fields.
- FLOW-001 says every material workflow resolves to one primary system-of-record object but often uses aliases.
- F02-F06 and C01-F04 both flag record-name drift.

Recommended action: Do not merge GEN, CAT, and FLOW. Instead, split authority explicitly:
- GEN-001: term definitions.
- CAT-002: canonical record names, required fields, and evidence value.
- FLOW-001: flow-to-record crosswalk using CAT-002 names, with one alias column if useful.
- Examples/templates: canonical name first, local tool/ticket alias second.

Owner/workstream: G02 record vocabulary cleanup.

### G01-F04 Medium Adoption documents should become a clearer suite, not a single merged mega-guide
Affected files:
- `START-HERE.md`
- `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-IMP-004_Implementation_Cards.md`
- `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`

Problem: The adoption library is large and overlaps: IMP-001 has rollout and scaling; IMP-003 covers small teams; IMP-005 covers path/dependencies; IMP-006 gives checklists; IMP-007 gives reading paths; START-HERE gives another path. This can feel like too many front doors.

Why it matters: Adoption guidance is where human comprehension matters most. Merging everything would create a worse mega-guide, but leaving the suite without a clear hub can overwhelm a new CISO or small-team lead.

Evidence from corpus:
- Heading inventory shows seven IMP documents with distinct but adjacent purposes.
- F03-F02 found START-HERE uses `where applicable` where a scope decision should be recorded.
- D03 found small-team consolidation maps disagree across OM/RAC/IMP-003/Story 8.

Recommended action: Keep the suite for now, but clarify document roles:
- START-HERE: front-door path selection, very short.
- IMP-005: canonical adoption scope/dependency authority.
- IMP-001: narrative adoption overview and rollout story; remove duplicated decision-tree detail.
- IMP-002: safety rails and anti-patterns.
- IMP-003: CERG Lite operations, but synchronize its map with RAC.
- IMP-006: action checklists only.
- IMP-007: reader paths only.

Owner/workstream: H01/H02 comprehension tests, then G02 adoption rewrite.

### G01-F05 High Workforce architecture needs a system map and thinner per-role JDs, not fewer authoritative documents
Affected files:
- `roles/CERG-GOV-JF-001_Job_Families_Overview.md`
- `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md`
- `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md`
- `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md`
- `governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md`
- `governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md`
- `governance/CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md`
- `governance/CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md`
- `governance/CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md`
- Per-role JD files under `roles/jf-*`.

Problem: The workforce subsystem is comprehensive but cognitively heavy. It covers families, grade architecture, competencies, performance, training, succession, onboarding, workforce planning, NICE mappings, and per-role JDs. The issue is not that these should merge; each serves a real HR lifecycle function. The issue is that per-role JDs duplicate long competency and management-track content, and readers lack a simple map of which workforce artifact answers which question.

Why it matters: Workforce architecture is a major CERG differentiator. It should feel navigable, not like a second corpus.

Evidence from corpus:
- F03-F05: JD competency rows are too dense for human scanning.
- A02: long-bullet readability issue affects 25 role files.
- D01: JF-001 omits five canonical roles from its main family table.
- D01: Detection Engineer and Vendor Risk Analyst JD bodies appear swapped.

Recommended action: Keep the workforce documents separate, but add a concise `Workforce System Map` section or document that says:
- OM/RAC: what roles own work.
- JF/JF-002: how roles group and map to NICE.
- JA: grade/level architecture.
- CMP: behavioral anchors.
- PERF: review/promotion process.
- TRN: development/certifications.
- SUCC: continuity/succession.
- ONB: first 90 days.
- WFP: staffing/capacity.
- Per-role JDs: role-specific summary, responsibilities, KPIs, and links.
Then shorten per-role JD copied competency material once the role-swap issue is fixed.

Owner/workstream: Workforce architecture cleanup.

### G01-F06 Medium `CERG-GOV-JD-001` should remain an index/redirect, not be retired immediately
Affected files:
- `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md`
- Per-role JD files under `roles/jf-*`.

Problem: JD-001 used to be monolithic but is now an index pointing to per-role documents. It is no longer the duplicate content problem the G01 prompt warned about, but it remains a cataloged artifact that could confuse readers if they expect full job descriptions inside it.

Why it matters: Retiring it immediately could break links and reader habits. Keeping it as a clear redirect protects continuity while the per-role JD tree stabilizes.

Evidence from corpus:
- JD-001 v2.0 explicitly states it is now a family-level index.
- It contains per-role document links and no full monolithic job descriptions.
- Role files now carry the substantive JD content.

Recommended action: Keep JD-001 as an index/redirect through the next major release. Add stronger wording later if needed: `Do not use this document as the role authority; use the linked per-role JD and RAC-001.` Consider moving equivalent index function into `roles/README.md` in a future major version, but do not make that cut before catalog/link impact review.

Owner/workstream: Workforce / catalog maintenance.

### G01-F07 Medium Examples should be pruned for demonstration value, not merged into procedures
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-*.md`
- Related procedures and flows.

Problem: Some examples repeat procedure content or present flow tables close to operational instructions. The best examples, however, are essential because they show the model under pressure: named owner, record, evidence, decision, metric, and improvement.

Why it matters: Procedures tell the reader what to do; examples teach why the handoffs matter. If examples become procedure copies, they age badly and create drift. If they are removed, CERG loses its most human teaching layer.

Evidence from corpus:
- E01 found Stories 2, 9, and 10 are strongest promotion targets.
- E02 proposed minimal new stories, not a large example expansion.
- F03-F04 found example tables sometimes use vague `coordinates` language.

Recommended action: Keep examples as a separate teaching layer. Cut procedural detail that belongs in PRC/FLOW docs. Promote stories that show decision/evidence closure. Label each story by the flow(s) it demonstrates and link back to authoritative procedures rather than restating their rules.

Owner/workstream: Examples rewrite plan / G02.

### G01-F08 Low Repeated three-pillar descriptions should be harmonized, not removed
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `examples/day-in-the-life/README.md`

Problem: The three-pillar description appears repeatedly. That repetition is intentional, but each file should not invent a new conceptual model.

Why it matters: The three-pillar model is CERG's core claim. Readers need to encounter it more than once, but the wording should reinforce, not fragment, the model.

Evidence from corpus:
- B01 found the pillar model holds across README, FRM-001, FRM-002, and OM-001.
- FRM-002's three-question model is the strongest operational shorthand.
- F03 found slogans are acceptable when paired with operational consequences.

Recommended action: Use FRM-002's three-question wording as the canonical short form:
- Engineering: `How do we build and operate this securely?`
- Risk: `What exposure remains and what treatment is required?`
- Governance: `What rule, evidence, decision, or report governs this?`
Keep narrative flavor in FRM-001 and brief mission language in README/START-HERE, but point back to FRM-002 for navigation.

Owner/workstream: G02/G03 front-door harmonization.

## Positive Confirmations

- No major file should be retired immediately except possibly future relocation of index behavior after link/corpus impact review.
- CERG's controlled repetition is usually reader-protective: README/START-HERE orient; FRM-001 explains; FRM-002 navigates; OM/RAC assign; FLOW executes.
- The biggest simplification opportunities are not file deletions. They are authority consolidation: RACI in RAC, records in CAT-002, vocabulary in GEN, clocks in procedures/SLC, and examples as demonstrations.
- JD-001 has already been converted from monolithic content to index form, which resolves the largest obvious G01 retirement candidate.
- The adoption and workforce clusters are large because CERG is a full operating model, not because they are redundant checklists.

## Open Questions

- Should a new `Workforce System Map` be added, or should the map live in existing `JF-001` or `roles/README.md`?
- Should `START-HERE.md` become the only public adoption hub, with IMP-001 reduced to governed implementation detail?
- Should FLOW-001 include an explicit `Authoritative detailed procedure` field for each flow to prevent future clock/closure drift?
- Should CAT-002 include an alias column for local/common record labels, or should aliases live only in FLOW/examples?

## Proposed Next Tasks

- G02 should convert these structural recommendations into file/section rewrite tasks.
- H01/H02 should test whether the adoption-document suite confuses first-hour readers before any merge/retire action.
- Workforce cleanup should wait until D01 role-swap and JF-001 omission findings are addressed.
- Record-name cleanup should be synchronized across CAT-002, FLOW-001, FRM-002, templates, and examples rather than handled piecemeal.
