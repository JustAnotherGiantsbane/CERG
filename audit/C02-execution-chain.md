# Task C02 Output: Test standards-to-procedures-to-records chains

## Scope Reviewed
- Files read:
  - All 15 standards under `standards/`
  - All 12 procedures under `procedures/` by direct read or targeted trace:
    - `CERG-PRC-AC-002`
    - `CERG-PRC-AR-001`
    - `CERG-PRC-AUD-001`
    - `CERG-PRC-AV-001`
    - `CERG-PRC-CHG-001`
    - `CERG-PRC-IR-002`
    - `CERG-PRC-LL-001`
    - `CERG-PRC-RM-001`
    - `CERG-PRC-TI-001`
    - `CERG-PRC-TM-001`
    - `CERG-PRC-TPRM-001`
    - `CERG-PRC-VM-001`
  - `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`
  - `governance/CERG-GOV-CAT-002_Record_Catalog.md`
  - `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`
  - `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
  - `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md`
  - Selected templates under `templates/`, especially AR, AUD, AI, CUI, RM, SaaS, SBOM, and TPRM templates.
- Sections reviewed:
  - Standard purpose, requirement/control tables, related documents, roles, evidence, and metrics references.
  - Procedure workflow, records/evidence, metrics, and template sections.
  - CAT-002 record catalog and TRC-001 traceability rules/matrix.
- Files intentionally not reviewed:
  - Full regulatory operational packages line-by line, except where standards explicitly routed to CUI, CIP, SOX, BCP, or Privacy packages.
  - Machine-readable schemas beyond noting SBOM registry references. C02 focused on human Markdown execution chains.

## Method
- Steps performed:
  1. Identified the major operational requirement families in each standard. Instead of reproducing every control row, grouped each standard's top requirements into executable requirement families.
  2. Mapped each requirement family to the procedure, plan, or template that tells a human how to execute it.
  3. Mapped each procedure path to its expected record, evidence, evidence quality rule, and metric or oversight use.
  4. Compared direct standard-to-procedure links with `GOV-TRC-001` and `CAT-002` to identify stale or missing routing.
  5. Flagged chains that stop at policy/standard language, procedures that run work without clearly invoking available templates, and metrics that are referenced but not defined.
- Search terms or scripts used:
  - `find standards procedures templates -maxdepth 1 -type f -name '*.md'`
  - Targeted scans for `Evidence`, `Record`, `Metric`, `Procedure`, `Template`, `PRC-`, `TMPL-`, `DT-`, `SBOM`, `SaaS`, and `classification`.
- Assumptions avoided:
  - Did not require every standard to have its own standalone procedure. A standard may execute through AR, CHG, VM, AUD, RM, TPRM, or a regulatory package if the record/evidence path is clear.
  - Did not treat a missing template reference as fatal if a procedure embeds an equivalent local template and says it is authoritative.

## Execution-Chain Matrix

| Standard | Top operational requirement families tested | Primary execution path | Record(s) / template(s) | Evidence quality / audit path | Metric / oversight use | Chain result |
|---|---|---|---|---|---|---|
| `STD-AC-001` Access Management | Identity source, SSO/MFA, privileged access, JML, access review, break-glass, session logging, remote access, service accounts, exceptions | `PRC-AC-002`, `PRC-AUD-001`, `PRC-RM-001`, AR/CHG for architecture changes | Access Review Record, JML log, PAM logs, exception register, evidence worksheet | AUD-001 E2/E3 rules; PRC-AUD control testing | MTR ID-001 through ID-004 | Strong; TRC-001 should be refreshed to name `PRC-AC-002` explicitly. |
| `STD-AI-001` Artificial Intelligence | sanctioned tools, AI intake, data restrictions, built/embedded AI review, model inventory, prompt/injection threats, vendor AI reassessment, shadow AI | `PRC-AR-001`, `PRC-TPRM-001`, `PRC-RM-001`, `STD-DG`, `STD-SDL`, `STD-LM` | `TMPL-AI-001`, `TMPL-AI-002`, `TMPL-AI-003`, Project Security Review, Vendor Risk Assessment, Risk Register Entry | AUD-001 evidence rules; CAT-002 record types | CM-002, SR-003, TP metrics; no dedicated AI metrics found | Good new chain; metrics are indirect and may be sufficient for now. |
| `STD-AM-001` Asset Management | asset classes, ephemeral assets, authoritative inventory, required attributes, ownership, classification, criticality, lifecycle, EOL, inventory metrics | FLOW F-03, `PRC-AR-001`, `PRC-VM-001`, `PRC-AUD-001` | Asset Inventory Record, Asset Coverage Record, CMDB/CSPM exports | AUD-001 evidence freshness for scans/inventory; PRC-AUD sampling | PH-003, PL-002, SR-005; FLOW F-03 asset coverage metrics | Mostly strong; inventory completeness metric mentioned in standard is not clearly defined in MTR. |
| `STD-CFG-001` DISH Configuration Baseline | DISH profile, tiers, baseline catalog, scanning, drift, exceptions, OT-safe assessment, pipeline/container/IaC checks | `PRC-CHG-001`, `PRC-VM-001`, `PRC-RM-001`, AR for new systems | Configuration Baseline Record, DISH scan, drift report, exception record | AUD-001 E2/E3; PRC-AUD testing; CB-001 evidence | CM-001 baseline drift; EM/PH metrics | Sound chain; detailed day-to-day DISH operating procedure is implicit rather than standalone. |
| `STD-CR-001` Cryptography and Key Management | approved/prohibited algorithms, TLS, certs, secrets, tokens, CMK/BYOK, FIPS, vendor inheritance, sunset tracking | AR/CHG for changes; TPRM for inherited/provider crypto; RM for exceptions; AUD for testing | Certificate/key inventory, secrets manager export, KMS inventory, inheritance evidence package, exception record | AUD-001 evidence rules; PRC-AUD control tests | ID/CM/TP metrics indirectly; no crypto-specific metric | Requirements are clear; execution path is distributed and would benefit from a crypto lifecycle record/runbook pointer. |
| `STD-CUI-001` CUI Handling | SSP, POA&M, flow-down, boundary, CUI asset inventory, access, crypto, logging, exposure, incident support, evidence | CUI operational package, `PRC-VM-001`, `PRC-RM-001`, `PRC-AUD-001`, TPRM | `TMPL-CUI-001` SSP, `TMPL-CUI-002` POA&M, CUI evidence package, risk/exception entries | AUD-001/PRC-AUD and CMMC package evidence | GV-001, GV-002, CUI posture | Strong regulated chain. |
| `STD-DG-001` Data Governance | classification scheme, classifying/labelling, handling table, lifecycle, retention, disposal, DLP | Other standards implement treatment; PRC-AUD retains evidence; no dedicated data classification/retention procedure | Classification evidence, disposal record, DLP event/finding, retention schedule | AUD-001/PRC-AUD for evidence; unclear operational workflow for classification decisions | No direct DG metrics; DLP/detection metrics intended but DT metrics missing | Conceptually strong but execution chain is weak for classification, retention, disposal, and DLP operations. |
| `STD-EP-001` Endpoint and Mobile | endpoint classes, endpoint protection, EDR, device posture, mobile/BYOD, patching, removable media, privileged endpoints | `PRC-VM-001`, `PRC-TPRM-001` for contractors, `PRC-AUD-001`; CHG for posture changes | MDM compliance report, EDR coverage, endpoint inventory, exception register | AUD-001/PRC-AUD evidence; scan/posture freshness | CM/PH/EM metrics indirectly; no endpoint-specific metric | Adequate through VM/AUD, but BYOD/device posture operating steps are not as explicit as access or TPRM. |
| `STD-IT-001` IT/Cloud/SaaS | approved services, data placement, tenancy/account governance, IAM, logging, baseline drift, exposure treatment, SaaS responsibility, isolation, resilience | `PRC-AR-001`, `PRC-TPRM-001`, `PRC-CHG-001`, `PRC-VM-001`, `PRC-AUD-001` | Project review, Vendor Risk Assessment, Approved Provider Catalog, Shared Responsibility Matrix, Change Record, Finding Record | AUD-001; provider inheritance evidence package | CM, EM, TP, SR metrics | Strong. SaaS evidence checklist template should be invoked from TPRM/IT path. |
| `STD-LM-001` Logging/Monitoring/Detection | mandatory sources, SIEM onboarding, day-one detections, detection coverage, triage/tuning, purple-team validation, OT/CUI logging overlays | `PRC-AV-001`, `PRC-VM-001`, `PRC-RM-001`, PRC-AUD; FLOW F-03/F-06/F-07 | SIEM Onboarding Record, Detection Coverage Record, validation records, finding/risk entries | AUD-001 E2/E3; adversarial validation evidence | References DT-001; MTR data map names DT-001-DT-003 | Chain breaks at metrics: MTR Detection Metrics section is empty while LM depends on DT metrics. |
| `STD-MSG-001` Email and Messaging | SPF/DKIM/DMARC, inbound protection, anti-phishing, outbound/DLP, mailbox security, collaboration tools, reporting | LM for detection, AC for mailbox/account security, DG for DLP, VM/RM for findings/exceptions | Email configuration exports, DLP events, detection rules, exception register | AUD-001/PRC-AUD | Detection, ID, and possibly DLP metrics; no message-specific metric | Requirements clear; execution chain distributed and not explicitly routed in the standard. |
| `STD-NET-001` Network Security | zero trust, segmentation, boundary control, IT/OT boundary, remote access, vendor access, wireless, cloud network controls | AR/CHG for network changes, TPRM for vendor access, RM for exceptions, AV for testing | Network diagrams, change records, gateway logs, exception records, segmentation validation | AUD-001/PRC-AUD; adversarial validation | CM/EM/DT metrics indirectly | Adequate but no explicit segmentation validation procedure/record beyond general AR/CHG/AV. |
| `STD-OT-001` Grid/Control Systems | BES/non-BES, asset categorization, risk acceptance, third-party/CIP-013, access, logging, patching, change windows, incident reporting, recovery | CIP package, VM, RM, AV, CHG, BC package, IR interface | CIP evidence package, CIP deviation, OT exposure record, change-window record, recovery evidence | Regulatory package evidence plus AUD-001 | GV-003, GV-004, EM/PH overlays | Strong regulated chain, with known IR boundary issues tracked in B02/B03/C01. |
| `STD-RES-001` Resilience/Backup | recovery tiers, backup protection, immutability, restoration testing, evidence, ransomware recovery, SOX evidence, BCP interface | BCP/DR plan, PRC-AUD, CHG for recovery-control changes, LL/IMPREG for exercise lessons | Backup and Recovery Test Record, restoration evidence, BCP exercise record, SOX evidence | AUD-001 evidence freshness; PRC-AUD testing | CM-004, CM-005; SOX/GV metrics | Strong chain; BCP boundary handled well. |
| `STD-SDL-001` Secure SDLC | SDLC phases, software risk tiers, gates, code review, SAST/DAST/SCA, secrets, SBOM, dependencies, pipeline security, gate bypass, pre/post-production findings | AR, TM, VM, RM, TPRM, CHG | Project review, Threat Model Record, Finding Record, SBOM, exception record, pipeline evidence | AUD-001; automated evidence standard; VM validation | CM-002, EM metrics, TP-004 SBOM | Strong, but SBOM evidence checklist template is not clearly invoked by SDL/TPRM. |

## Findings

### C02-F01 High Detection requirements point to metrics that are not defined
Affected files:
- `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`

Problem: The logging/monitoring/detection standard uses detection coverage as an operational requirement and references `DT-001` as the detection coverage metric. MTR-001 has a `Detection Metrics (Owner: Cyber Risk)` heading, and the MTR data-source map names `DT-001 – DT-003`, but the metrics dictionary contains no DT metric rows.

Why it matters: This breaks the standards → records → metric chain. Operators can onboard log sources and create detection coverage records, but the board/CISO metric closure is undefined. Detection coverage is also central to the Detection Engineer / Risk Operations role clarity already flagged in B01.

Evidence from corpus:
- STD-LM says detection coverage is measured as `DT-001` in MTR-001.
- MTR-001 §3.2b is empty.
- MTR-001 §4 data source map references `DT-001 – DT-003` as if they exist.
- CAT-002 lists `Detection Coverage Record`, but the metric names and formulas are missing.

Recommended action: Populate MTR-001 detection metrics before rewriting surrounding prose. Minimum set: detection coverage by required ATT&CK sub-matrix/source, required log-source onboarding completeness, and detection validation pass rate from purple-team/adversarial testing.

Owner/workstream: Metrics / Risk.

### C02-F02 High PRC-AR and TMPL-AR disagree about the authoritative intake template state
Affected files:
- `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`
- `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md`
- `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md`

Problem: PRC-AR §11 says the intake form, threat model, handoff package, and go-live acceptance templates embedded in the procedure are authoritative, and that promotion to standalone `CERG-TMPL-AR-*` artifacts is tracked as a planned V1.x item. But `CERG-TMPL-AR-001` already exists as an Approved standalone template. The standalone template also uses a narrower review/approval section and assigns threat-model review to Application Security Engineer, while PRC-AR assigns threat modeling leadership to Risk.

Why it matters: Project intake is the front door to CERG. If a project team uses the standalone template, while Engineering uses the embedded PRC-AR template, required fields, review routing, and role accountability may diverge.

Evidence from corpus:
- PRC-AR §11: embedded templates are authoritative; standalone promotion is planned.
- TMPL-AR-001: Approved standalone form with parent PRC-AR.
- TMPL-AR-001 §4 review routing differs from PRC-AR §2 and §6.2 role model.
- CAT-001 now catalogs TMPL-AR-001 as Approved, while its revision history says `1.0 Draft`.

Recommended action: Make the standalone TMPL-AR-001 the authoritative intake artifact or retire it. If retained, update PRC-AR §11 and align the template fields and review roles to PRC-AR, especially Risk ownership of threat modeling.

Owner/workstream: Engineering / Templates.

### C02-F03 High TRC-001 is useful but stale as the execution-chain source of truth
Affected files:
- `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md`
- `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
- `templates/` standalone templates

Problem: TRC-001 is designed to be the missing operating layer between CB-001 controls, standards, procedures, and evidence. The concept is exactly right, but the current matrix is stale against newer artifacts. Examples: access controls often route to `Access review and JML process under access standard` instead of the dedicated `PRC-AC-002` runbook; DT metrics are referenced elsewhere but not defined in MTR; standalone templates such as TMPL-AR-001, TMPL-SAAS-001, and TMPL-SBOM-001 are not reflected in procedure routing.

Why it matters: C02's purpose is exactly what TRC-001 claims to do. If TRC-001 is stale, future maintainers and LLM agents will use an outdated execution map and miss the newer operational artifacts.

Evidence from corpus:
- TRC-001 purpose says every control needs a runbook or reason.
- TRC-001 AC rows do not name PRC-AC-002 despite that runbook existing and being Approved.
- TRC-001 revision history says `1.0 Draft` while status is Approved.
- CAT-001 shows many templates added after the original TRC draft.

Recommended action: Treat TRC-001 as the canonical execution-chain matrix and refresh it after C02/C03 findings. Add a maintenance check to compare TRC rows to the catalog whenever new procedures/templates are approved.

Owner/workstream: Governance / Traceability.

### C02-F04 Medium Data Governance has strong requirements but weak procedural execution for classification, retention, disposal, and DLP
Affected files:
- `standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md`

Problem: STD-DG-001 clearly states how classification should work and how classification drives access, encryption, backup, logging, disposal, and DLP. But the execution chain relies on other standards and does not provide a clear procedure or record path for routine classification decisions, reclassification, retention schedule maintenance, disposal evidence, or DLP event handling.

Why it matters: Data classification is the input to many other controls. If classification is wrong or undocumented, access, encryption, logging, and retention controls inherit the wrong scope. A reader can understand the requirements, but may not know which record to update or which workflow to run.

Evidence from corpus:
- STD-DG §4 says data owner classifies and reclassification is a recorded decision.
- STD-DG §8 says disposal of Confidential/Restricted data produces a retained disposal record.
- STD-DG §9 says DLP events are detection signals and coverage gaps are accepted risk until closed.
- CAT-002 does not list a dedicated Data Classification Record, Retention Schedule Record, Disposal Record, or DLP Event Record.

Recommended action: Prefer a light-weight record mapping over a new large procedure. Add CAT-002 records or aliases for classification decision, retention schedule, disposal evidence, and DLP event/finding. Add a short execution-path section in STD-DG pointing to AC/CR/RES/LM/PRC-AUD/PRC-RM workflows.

Owner/workstream: Governance / Data.

### C02-F05 Medium TPRM-related standalone templates are not clearly invoked by the TPRM procedure
Affected files:
- `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`
- `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md`
- `templates/CERG-TMPL-SAAS-001_SaaS_Evidence_Collection_Checklist.md`
- `templates/CERG-TMPL-SBOM-001_SBOM_Evidence_Collection_Checklist.md`
- `standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`
- `standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md`

Problem: PRC-TPRM contains strong vendor tiering, evidence-by-tier, SaaS catalog, shared responsibility, and SBOM requirements. But the standalone TPRM, SaaS evidence, and SBOM checklist templates are not clearly invoked in the procedure. Some are visible mainly in CAT-001, examples, or the template files themselves.

Why it matters: Templates are supposed to make execution repeatable. If the procedure does not tell an operator when to use the template, teams may invent local questionnaires/checklists and lose consistency in vendor evidence and SBOM collection.

Evidence from corpus:
- PRC-TPRM §5 defines evidence by tier and §11 defines SBOM processing, but the procedure does not link TMPL-TPRM-001, TMPL-SAAS-001, or TMPL-SBOM-001 in metadata or related documents.
- CAT-001 catalogs these templates as Approved.
- Story 10 uses TMPL-TPRM-001, suggesting the intended path exists narratively but not in the governing procedure.

Recommended action: Update PRC-TPRM metadata and relevant sections to invoke the three templates: TMPL-TPRM-001 for assessments, TMPL-SAAS-001 for SaaS/customer-side evidence, and TMPL-SBOM-001 for SBOM collection/validation.

Owner/workstream: Risk / TPRM templates.

### C02-F06 Medium Several standards depend on distributed execution paths without a local chain summary
Affected files:
- `standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md`
- `standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md`
- `standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md`
- `standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md`
- `standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md`

Problem: These standards have clear requirements, but their execution paths are distributed across AR, CHG, VM, RM, AUD, LM, TPRM, and regulatory packages. A knowledgeable reader can infer the path; a new practitioner may not know which procedure to run for common work such as certificate rotation, segmentation validation, DLP tuning, BYOD exceptions, email authentication evidence, or DISH drift response.

Why it matters: CERG should let a capable reader answer `what do I do next?` without guessing. Distributed execution is acceptable, but each standard should include a small `Execution Path` table: requirement, procedure, record, evidence, metric.

Evidence from corpus:
- STD-CR has strong FIPS and CMK evidence tables, but no simple key/certificate lifecycle procedure pointer.
- STD-NET names remote access and segmentation requirements, but execution is implicit through AR/CHG/TPRM/AV.
- STD-MSG depends on AC/DG/LM but lacks an operational chain summary.
- STD-CFG's DISH operation is clear as a baseline, but scan scheduling, drift response, and exception handling are distributed.

Recommended action: Do not create five new procedures by default. Add a short execution-path table to each affected standard or maintain the mapping centrally in a refreshed TRC-001.

Owner/workstream: Standards / Traceability.

### C02-F07 Medium Some metric claims in standards do not map cleanly to MTR metric IDs
Affected files:
- `standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md`
- `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Problem: STD-AM says inventory completeness is a reported metric, and FLOW F-03 names asset coverage completeness, missing owner, missing scan, and missing logging metrics. MTR has related PH/PL/SR metrics but no obvious asset inventory completeness metric. STD-LM references DT metrics that are not defined.

Why it matters: Standards can require controls and procedures can execute them, but if metrics are missing or indirect, oversight cannot tell whether the execution chain is healthy.

Evidence from corpus:
- STD-AM §10.4 says inventory completeness is reported per MTR-001.
- FLOW F-03 lists asset coverage metrics.
- MTR includes PH-003 End-of-Support Count and PL-002 Attack Surface Change Rate, but no explicit asset inventory completeness metric.
- MTR Detection Metrics section is empty.

Recommended action: Add or cross-reference explicit asset inventory/coverage metrics in MTR, and populate DT metrics. If existing metrics are intended to cover the standard, update the standards to name the exact IDs.

Owner/workstream: Metrics / Engineering / Risk.

## Positive Confirmations
- The standard-to-procedure model is much stronger than a typical policy library. Most standards have real operational routes through AR, CHG, VM, RM, AUD, TPRM, LL, and regulated packages.
- The regulated chains are especially strong: CUI has SSP/POA&M and audit paths; OT has CIP package/deviation paths; SOX change and backup evidence paths are present.
- PRC-AUD and AUD-001 provide a robust universal evidence quality layer. Even where a standard lacks a local evidence section, audit testing can often provide the evidence mechanics.
- CAT-002 provides the right record-catalog concept. The remaining work is mostly alignment of names and missing record aliases, not inventing a new model.
- STD-AI has one of the clearest modern requirement-to-template chains through AI intake, sanctioned tools, and AI system/model register.
- PRC-VM's exposure-state model is strong and should remain the execution source for post-production exposure treatment.

## Open Questions
- Should TRC-001 become the single maintained execution-chain matrix for all standards, or should each standard include its own local execution-path table?
- Should Data Governance receive a lightweight procedure, or would CAT-002 record additions plus a STD-DG execution table be enough?
- Should metrics be expanded for every major standard, or only where a control family needs CISO/board visibility?
- Should standalone templates always be invoked from parent procedures, or is catalog registration plus template metadata sufficient? C02 recommends parent-procedure invocation for operational templates.

## Proposed Next Tasks
- C03: continue into exception/risk/finding conversion rules, using C01/C02 F-04 and PRC-VM findings as seed issues.
- G02: add rewrite entries for MTR detection metrics, PRC-AR/TMPL-AR alignment, TRC refresh, Data Governance execution mapping, TPRM template invocation, and standard execution-path tables.
- G03: carry `1.0 Draft` revision-history text in Approved documents to the polish queue where it appears in TRC-001 and TMPL-AR-001.
