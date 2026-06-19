# Author Decision Memo

## Decision 1: IR artifact ownership model

Question: Should CERG keep the IR Plan and IR Playbook Set as full External Interface artifacts in this repository, or reduce them to interface stubs that point to a standing IR team's separate authoritative plan?

Why it matters: The audit found the largest authority contradiction in the IR boundary. OM-001 and IR banners say the standing IR team / Incident Commander owns incident response, notification clocks, and exercises, while IR body sections assign some ownership to CERG Governance/Risk. The author must decide whether CERG is carrying the full external IR artifacts or only the CERG-facing interface.

Options:
1. Keep full External Interface artifacts in-repo, owned by Standing IR Team / Incident Commander, with CERG support language only.
2. Convert IR artifacts to CERG-facing interface stubs and require adopters to maintain their IR plan elsewhere.
3. Bring IR fully inside CERG ownership.

Recommended option: Option 1. Keep the artifacts in-repo because they help adopters, but make Standing IR Team / Incident Commander the clear owner. CERG Governance may maintain repository links, evidence cross-references, and CERG support outputs only.

Tradeoffs:
- Option 1 preserves practical adopter value but requires careful boundary language.
- Option 2 is cleaner conceptually but less useful for adopters without an IR plan.
- Option 3 contradicts the established adjacent-function model and should be rejected unless the operating model is intentionally expanded.

Files affected if approved:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md`
- `examples/day-in-the-life/README.md` Story 6

Files affected if rejected:
- If Option 2: IR plan/playbook catalog entries, links, examples, FLOW F-06, and machine-readable manifests may need larger restructuring.
- If Option 3: OM-001, RAC-001, IR JDs, adjacent-function model, and IR metadata would need conceptual rewrite.

## Decision 2: Notification-clock authority phrasing

Question: Who owns regulatory notification clocks during incidents: Incident Commander / standing IR team, Legal, CERG Governance, or a shared model?

Why it matters: Notification clocks are high-consequence. Ambiguous ownership can cause missed regulatory deadlines or unauthorized notification decisions.

Options:
1. Incident Commander / standing IR team owns the clock process; Legal owns legal notification advice/privilege; CERG Governance tracks notification evidence and affected security records under direction.
2. CERG Governance owns the notification clock because it owns governance and evidence.
3. Legal owns the clock entirely.

Recommended option: Option 1.

Tradeoffs:
- Option 1 best preserves command authority and evidence discipline.
- Option 2 is tempting because Governance knows regulators/evidence, but it contradicts the adjacent-function model.
- Option 3 may be accurate in some organizations but under-specifies operational incident timing.

Files affected if approved:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`

Files affected if rejected:
- OM-001 and IR banners must be rewritten to reflect the chosen owner.

## Decision 3: Risk acceptance memo strategy

Question: Should `TMPL-RM-003` be retired now that `TMPL-RM-004` exists, or retained as a lightweight Low/Medium memo?

Why it matters: `TMPL-RM-003` omits Business Owner acceptance while RMF-001 and `TMPL-RM-004` require business consequence acceptance. Keeping two acceptance templates creates authority drift unless the shorter one is repaired.

Options:
1. Retire `TMPL-RM-003` and use `TMPL-RM-004` for all formal risk acceptances.
2. Retain `TMPL-RM-003` as a Low/Medium lightweight memo, but add Business Owner acceptance and explicit RMF-001 §9.7 linkage.
3. Keep both unchanged.

Recommended option: Option 1 if simplicity is the priority; Option 2 if adopters need a shorter Low/Medium artifact. Reject Option 3.

Tradeoffs:
- Retiring reduces drift and tool confusion.
- Retaining a lightweight memo reduces friction for low-risk decisions but requires discipline to prevent bypass.
- Any retirement affects catalog and related-document references.

Files affected if approved:
- If Option 1: `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`, `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`, `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`, `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`, generated manifests/indexes.
- If Option 2: `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md`, `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md`, `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`.

Files affected if rejected:
- The roadmap must still carry an unresolved authority-risk item; examples and procedure text must warn readers not to use TMPL-RM-003 for business-risk acceptance.

## Decision 4: Canonical risk scoring model

Question: Should RMF-001's FAIR-aligned LEF/LM calibration be the only scoring model, or should PRC-RM keep a simpler annual-probability/impact calibration for operators?

Why it matters: RMF and PRC-RM currently contain materially different quantitative anchors. Severity drives approval, escalation, reporting, and acceptance duration.

Options:
1. RMF-001 is the only canonical scoring model; PRC-RM points to it and gives operational instructions only.
2. PRC-RM keeps a simplified copy, but values must exactly match RMF and state `RMF governs`.
3. Maintain two different calibrations for different audiences.

Recommended option: Option 1.

Tradeoffs:
- Option 1 minimizes drift but requires readers to open RMF for scoring tables.
- Option 2 improves convenience but keeps duplication risk.
- Option 3 undermines severity consistency and should be rejected.

Files affected if approved:
- `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md`
- `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`
- `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md`
- Examples that mention scores/acceptance thresholds.

Files affected if rejected:
- All documents using risk score bands need a rule for which table governs when RMF and PRC-RM disagree.

## Decision 5: Record authority and alias policy

Question: Should record definitions live only in CAT-002, or should FLOW-001 and GEN-001 continue to carry local authoritative record definitions?

Why it matters: Records are the evidence spine. Multiple authoritative record definitions make metrics, audit evidence, templates, and automation harder to align.

Options:
1. CAT-002 is canonical for record names, owners, triggers, required fields, and evidence value; GEN defines terms; FLOW maps flows to CAT records and may include aliases.
2. Keep CAT-002, GEN-001, and FLOW-001 as co-authoritative record sources.
3. Move all record definitions into FLOW-001.

Recommended option: Option 1.

Tradeoffs:
- Option 1 protects traceability and still lets examples use local aliases.
- Option 2 preserves current duplication but allows drift.
- Option 3 overloads FLOW with catalog authority.

Files affected if approved:
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- Examples and templates using record aliases.

Files affected if rejected:
- Rewrite queue must preserve multiple record authorities and add explicit conflict-resolution language elsewhere.

## Decision 6: Machine-readable `pillar` semantics

Question: In machine-readable indexes, should `pillar` mean document-family grouping, operating accountability, or both as separate fields?

Why it matters: The LLM index currently labels all procedures as Risk, even where source documents are Engineering-led, Governance-led, or External Interface. Automation and LLM consumers may route work incorrectly.

Options:
1. Keep `pillar` as operating accountability and fix values.
2. Keep `pillar` as document taxonomy/family grouping and add `primary_operating_pillar`.
3. Leave current behavior unchanged.

Recommended option: Option 2 if backward compatibility matters; Option 1 if no consumers depend on current semantics. Reject Option 3.

Tradeoffs:
- Option 2 is safest for machine consumers but adds schema complexity.
- Option 1 is simpler but may break consumers expecting current `pillar` grouping.

Files affected if approved:
- `tools/regenerate-llm-index.py`
- `machine-readable/cerg-llm-index.json`
- Possibly `machine-readable/cerg-manifest.yaml` if schema changes extend beyond LLM index.

Files affected if rejected:
- B01/B03 issue remains; documentation should warn that `pillar` is not operating ownership.

## Decision 7: Security Awareness boundary depth

Question: Is an OM-001 interface table enough for Security Awareness, or should CERG create an External Interface package similar to IR/Privacy/BCP?

Why it matters: Awareness is named as adjacent, but its boundary is less operationalized than IR, Privacy, and BCP. Phishing simulation and training evidence can easily drift into Risk/Governance ownership.

Options:
1. Add a concise Awareness interface table to OM-001.
2. Create a standalone External Interface awareness package.
3. Bring Awareness into CERG as a governed domain.

Recommended option: Option 1 for now.

Tradeoffs:
- Option 1 is low overhead and likely sufficient.
- Option 2 is more complete but adds another artifact.
- Option 3 changes CERG scope and should be a major model decision.

Files affected if approved:
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- Possibly `governance/CERG-GOV-FRM-001_CERG_Framework.md` and `governance/CERG-GOV-FRM-002_Framework_System_Map.md` if navigation should expose the interface.

Files affected if rejected:
- If Option 2: CAT-001, new package/template, machine-readable artifacts.
- If Option 3: FRM/OM/RAC/JF/JDs and awareness-related metrics.

## Decision 8: Identity Risk Analyst role strategy

Question: Should Identity Risk Analyst become an explicitly routed operating role, or be treated as an optional specialization under Detection Engineer / Risk Pillar Leader?

Why it matters: The role exists in architecture and has a JD, but operating procedures rarely reference it. A role without procedure touchpoints is hard to staff, evaluate, or consolidate.

Options:
1. Integrate Identity Risk Analyst into STD-AC, PRC-AC, STD-LM, MTR identity/detection metrics, and relevant RACI rows.
2. Mark Identity Risk Analyst as optional specialization for mature programs; Detection Engineer/Risk Pillar Leader covers the work in smaller programs.
3. Remove the role from canonical architecture.

Recommended option: Option 2 for simplicity unless the author wants identity risk as a first-class mature-program role; then Option 1.

Tradeoffs:
- Option 1 strengthens identity risk but adds role complexity.
- Option 2 preserves the role without forcing every adopter to staff it.
- Option 3 reduces complexity but may lose a useful modern identity-risk specialization.

Files affected if approved:
- Option 2: `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`, `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`, `roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md`, small-team adoption docs.
- Option 1 additionally: `standards/CERG-STD-AC-001_Access_Management_Standard.md`, `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`, `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`, `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`.

Files affected if rejected:
- Role remains present but disconnected; future role-procedure fit issues persist.

## Decision 9: Workforce architecture simplification approach

Question: Should the workforce subsystem be simplified by merging documents, adding a system map, or thinning per-role JDs?

Why it matters: Workforce architecture is a CERG differentiator but cognitively heavy. The audit found the issue is navigation and per-role density, not that the subsystem lacks purpose.

Options:
1. Keep workforce documents separate; add a Workforce System Map and thin repeated JD sections.
2. Merge workforce documents into a smaller set.
3. Leave structure unchanged and repair only defects.

Recommended option: Option 1.

Tradeoffs:
- Option 1 preserves HR lifecycle depth while improving reader comprehension.
- Option 2 may reduce file count but risks creating a mega-document.
- Option 3 leaves a known adoption friction point.

Files affected if approved:
- `roles/CERG-GOV-JF-001_Job_Families_Overview.md`
- Possibly `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md`
- Per-role JDs under `roles/jf-*/*.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`

Files affected if rejected:
- Only critical JD/content defects are repaired; workforce comprehension remains a future issue.

## Decision 10: Example inventory strategy

Question: Should Stories 1-7 remain embedded in `examples/day-in-the-life/README.md`, or should each story become a standalone file like Stories 8-10?

Why it matters: Examples are first-class teaching tools. Mixed storage makes inventory, linking, and promotion harder, but splitting files increases catalog and maintenance work.

Options:
1. Keep Stories 1-7 embedded and label README as containing Stories 1-7; keep 8-10 standalone.
2. Split Stories 1-7 into standalone files and make README an index only.
3. Collapse 8-10 back into README.

Recommended option: Option 2 if examples are intended as public training assets; Option 1 if minimizing file churn is more important during source cleanup.

Tradeoffs:
- Option 2 improves linking, reader navigation, and future story ownership but requires catalog/index updates.
- Option 1 is lower effort but preserves asymmetry.
- Option 3 would make README too large and reduce direct linking.

Files affected if approved:
- `examples/day-in-the-life/README.md`
- New story files for Stories 1-7 if Option 2
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` if catalog tracks individual examples
- `START-HERE.md`, `FRM-002`, `IMP-007`, and machine-readable artifacts if paths change.

Files affected if rejected:
- Keep README inventory explicit and update stale story counts only.

## Decision 11: New example story strategy

Question: Which missing stories should be added versus absorbed into existing stories?

Why it matters: E02 recommended a minimal high-value story set. Adding too many stories can dilute the examples; adding too few leaves judgment-heavy workflows under-taught.

Options:
1. Add two new stories: audit evidence failure/rework and OT maintenance-window patch deferral.
2. Add three stories: those two plus business owner rejects remediation cost / accepts residual risk.
3. Add no new stories; expand existing Story 3, Story 8, and Story 10.

Recommended option: Option 2 if examples are a primary training channel; Option 1 if keeping the set lean is more important.

Tradeoffs:
- Option 2 covers evidence, OT, and business-consequence decisions clearly.
- Option 1 leaves business-owner funding/acceptance mostly in templates/procedures.
- Option 3 avoids file growth but may overload existing stories.

Files affected if approved:
- `examples/day-in-the-life/README.md`
- Possible new `examples/day-in-the-life/story-*.md` files
- `START-HERE.md`, `FRM-002`, `IMP-007` cross-links
- CAT-001 and machine-readable artifacts if new cataloged examples are added.

Files affected if rejected:
- Existing stories must absorb the teaching points; H02/H03 gaps remain partially addressed by procedures/templates only.

## Decision 12: Small-team authority guardrail

Question: In CERG Lite, may one person hold security roles and business-risk acceptance authority, or must Business Owner/Executive Sponsor acceptance remain separate even when heads collapse?

Why it matters: The core small-team principle is `heads collapse, questions do not`. Story 8 and consolidation maps can accidentally imply authority collapses too.

Options:
1. Business consequence acceptance must remain separate from the security assessor role whenever possible; if impossible, require explicit executive acknowledgement and compensating review.
2. In CERG Lite, a CISO/security lead may accept all residual risk due to staffing constraints.
3. Allow local tailoring without a hard rule.

Recommended option: Option 1.

Tradeoffs:
- Option 1 preserves the operating model but requires very small teams to find an executive/business counterpart.
- Option 2 is easier for tiny teams but undermines business accountability.
- Option 3 invites silent authority collapse.

Files affected if approved:
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `START-HERE.md`

Files affected if rejected:
- RMF-001, PRC-RM, and small-team docs must be rewritten to explicitly allow consolidated risk acceptance.

## Decision 13: Regulated architecture review trace strategy

Question: Should `architecture review for regulated system` become a named control/record path, or remain a composite workflow documented in TRC-001?

Why it matters: H04 found the regulated architecture review path is operationally strong but harder for auditors because it spans many controls and overlays rather than one named baseline control.

Options:
1. Add a curated composite trace in TRC-001 without creating a new control.
2. Add a new named baseline control for pre-production/architecture review of regulated systems.
3. Leave the trace implicit across existing controls.

Recommended option: Option 1.

Tradeoffs:
- Option 1 improves auditor usability without changing the control baseline.
- Option 2 may be cleaner for auditors but expands CB-001 and downstream mappings.
- Option 3 keeps the model pure but leaves a known comprehension gap.

Files affected if approved:
- `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- Possibly `governance/CERG-GOV-FRM-002_Framework_System_Map.md`

Files affected if rejected:
- Auditors must be guided through separate controls manually or via examples only.

## Decision 14: Control funding decision artifact

Question: Should CERG create a standalone Control Funding Decision Brief template, or add funding-decision fields inside existing risk/metrics documents?

Why it matters: H03 found business owners can see risks and metrics but do not get a clear `fund / defer / accept / avoid` decision package.

Options:
1. Add a standalone template for control funding decisions.
2. Add a funding-decision section to MTR-001 and PRC-RM without a new template.
3. Leave funding decisions to local governance forums.

Recommended option: Option 2 initially; revisit Option 1 if adopters need a repeatable artifact.

Tradeoffs:
- Option 2 avoids new-document overhead and fits COG/MTR processes.
- Option 1 gives stronger repeatability but expands the template catalog.
- Option 3 leaves a business-owner comprehension gap.

Files affected if approved:
- Option 2: `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`, `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`.
- Option 1 additionally: new template file, `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`, machine-readable manifests/indexes.

Files affected if rejected:
- H03 funding-decision gap remains; business decision support must be handled in examples or local adoption guidance.

## Decision 15: Incident severity notation

Question: Should incident-facing documents standardize on `P1-P4`, `Sev 1-Sev 4`, or paired notation?

Why it matters: IR plan uses Sev labels, FLOW uses P labels, and PRC-IR maps them. The mapping avoids contradiction but adds incident-time cognitive load.

Options:
1. Use paired notation everywhere: `P1 / Sev 1 - Critical`.
2. Standardize on `Sev` for IR-owned artifacts and `P` for CERG support flows.
3. Standardize on one notation everywhere.

Recommended option: Option 1.

Tradeoffs:
- Option 1 is least ambiguous and easiest during transition.
- Option 2 preserves local language but requires readers to remember mapping.
- Option 3 is cleanest but may conflict with adopter conventions.

Files affected if approved:
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- Any examples using incident severity labels.

Files affected if rejected:
- Keep mapping table prominent in PRC-IR and add cross-reference from FLOW/IR plan.

## Decision 16: Adoption suite simplification

Question: Should the IMP adoption documents be merged, retained as a suite with clearer roles, or reduced by retiring some documents?

Why it matters: Adoption guidance is useful but has many front doors. Merging everything may create a mega-guide; leaving roles unclear creates reader fatigue.

Options:
1. Retain the suite and clarify each document's job: START-HERE front door, IMP-005 scope/dependency authority, IMP-001 narrative rollout, IMP-002 safety rails, IMP-003 CERG Lite, IMP-006 checklists, IMP-007 reader paths.
2. Merge the IMP suite into fewer documents.
3. Leave structure unchanged.

Recommended option: Option 1.

Tradeoffs:
- Option 1 reduces confusion without losing targeted documents.
- Option 2 reduces file count but risks making adoption harder to scan.
- Option 3 leaves known H01/H02 friction.

Files affected if approved:
- `START-HERE.md`
- `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md`
- `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md`
- `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md`
- `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`

Files affected if rejected:
- If merging/retiring: CAT-001, links across README/START-HERE/FRM-002, and machine-readable manifests/indexes.

## Decision 17: Public promotion readiness of examples

Question: Should the strongest examples be promoted/cross-linked now, or only after authority repairs?

Why it matters: Stories are high-impact teaching artifacts. Promoting them before fixing authority language may spread stale risk/IR/small-team patterns.

Options:
1. Delay promotion until Story 4, Story 6, Story 8, and Story 10 are repaired.
2. Promote Story 2 and Story 9 now; hold the rest.
3. Promote all top examples now with known issues.

Recommended option: Option 2 for controlled progress; Option 1 if public release is near.

Tradeoffs:
- Option 2 uses the strongest clean examples while avoiding known defects.
- Option 1 is safest but delays value.
- Option 3 risks teaching wrong authority.

Files affected if approved:
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md`
- `examples/day-in-the-life/README.md`

Files affected if rejected:
- Keep current links minimal until all example rewrites are complete.

## I03 Acceptance Criteria Check

- Memo contains only decisions requiring human judgment: yes.
- Mechanical fixes and obvious corrections are excluded: yes.
- Decision types covered: conceptual model, naming, authority-location, retirement, example strategy, tone/voice, and scope boundary decisions.
- Required format used for each decision: yes.
