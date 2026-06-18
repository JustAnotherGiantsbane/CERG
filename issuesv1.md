# CERG Framework — Issues Analysis (v1)

*Generated from comprehensive review of the CERG corpus (131 documents, ~837K tokens). Focus: issues that materially improve adoption, operability, and long-term program health.*

---

## Legend

| Tag | Meaning |
|-----|---------|
| 🔴 **Critical** | Blocks adoption, creates silent failure modes, or produces shelfware if unaddressed |
| 🟠 **High** | Creates significant friction, operational ambiguity, or adoption risk |
| 🟡 **Medium** | Improves clarity, reduces maintenance burden, or closes a consistency gap |
| 🟢 **Low** | Polish, completeness, or future-proofing |
| 🏷️ **Area** | Adoption | Governance | Architecture | Evidence | Metrics | Tooling | Content | HR/Talent |

---

## 1. Adoption & On-Ramp Issues

### 1.1 🔴 Critical — Adoption: No "Bridge" Criteria from MVC to Full Adoption
**Location:** `IMP-001 §4–5`, `START-HERE.md`
**Problem:** The Minimum Viable CERG (8 artifacts) is well-defined. The 30/60/90-day rollout sequences adoption. But there are **no explicit exit criteria** for "MVC is running, now layer the rest." Teams will either stall at MVC forever or attempt big-bang adoption of remaining 20+ documents.
**Evidence:** IMP-001 §5.3 "By day 90 every pillar is producing work... That is a running program" — but no gate with measurable criteria.
**Fix:** Define **Gate 2 → Gate 3 transition criteria** in IMP-005 (Adoption Gates) with specific, measurable conditions (e.g., "3 consecutive monthly risk register reviews completed," "vulnerability SLA adherence >80% for 2 cycles," "first architecture review disposition issued"). Make Gate 3 the trigger for standard-layer adoption.

### 1.2 🔴 Critical — Adoption: VAR-001 Render Tool Not in Repository
**Location:** `VAR-001` (referenced in IMP-001 §7.1, IMP-003 §2), `IMP-001 §3.2`
**Problem:** IMP-001 §3.2 states: "Adaptation is mechanical, not creative... Use it. Do not hand-edit 28 documents." The render tool is **not present** in the repo. Adopters cannot mechanically adapt; they must hand-edit or build their own tooling.
**Evidence:** Search of `/tools/`, `/machine-readable/`, and root shows no render script. VAR-001 defines the token scheme but not the executor.
**Fix:** either (a) include the render tool in `/tools/` (Python/JS/Go), or (b) remove the "do not hand-edit" directive and provide a manual adaptation checklist with search/replace patterns. Option (a) strongly preferred — mechanical adaptation is a core CERG promise.

### 1.3 🟠 High — Adoption: Three-Person Model Is Theoretical
**Location:** `IMP-003 §4`, `OM-001 §6.2`
**Problem:** IMP-003 provides a 5-person and 15-person assignment map. The 3-person model says "consolidate further" but gives no concrete map. The 1-person model correctly says "don't adopt." Many real adopters will be 2–4 people.
**Fix:** Add a **concrete 3-person assignment map** to IMP-003 §4 with explicit role consolidations and compensating controls (e.g., "Person 1 = CISO + Governance Pillar Leader + Risk Register Owner; compensating: Executive Sponsor reviews all High/Critical acceptances").

### 1.4 🟠 High — Adoption: No "First Project" End-to-End Walkthrough
**Location:** `PRC-AR-001`, `FLOW-001 F-02`, `IMP-006`
**Problem:** Architecture review is the first real cross-pillar workflow a new adopter executes. The procedure (PRC-AR-001) and flow (F-02) are detailed, but there is **no worked example** showing a fictitious project moving from intake → disposition → handoff with all records populated.
**Fix:** Add a worked example appendix to PRC-AR-001 or FLOW-001 showing a sample "CloudApp Migration" project with filled intake form, architecture review record, threat model record, conformance scope statement, and production handoff summary.

### 1.5 🟡 Medium — Adoption: "Deferred = Accepted Risk" Not Enforced in Catalog
**Location:** `IMP-001 §7.4`, `CAT-001`
**Problem:** IMP-001 §7.2: "If you defer an applicable standard, record the decision and a target adoption date in the risk register." But CAT-001 catalog statuses (Approved/Planned/Deferred) don't require a risk register linkage field.
**Fix:** Add `risk_register_id` and `target_date` fields to CAT-001 entries for `Deferred` and `Planned` statuses. Validator (cerg-validate.py) should flag Deferred items without these fields.

---

## 2. Governance & Decision Rights Issues

### 2.1 🔴 Critical — Governance: "CISO Designee" Is an Undefined Escape Hatch
**Location:** `OM-001 §4.2`, `RMF-001 §9.7`, `POL-001 §7.1`
**Problem:** Multiple documents reference "CISO designee" as an approval authority (e.g., OM-001: "CISO designee for tactical risk decisions"). The designee is defined informally: "whichever named pillar leader the CISO has formally delegated to... recorded in writing and reviewed at least annually." **No canonical role, no delegation register, no validation.**
**Risk:** In a crisis or audit, "who was the designee?" has no authoritative answer. The designee may not know they are the designee.
**Fix:** Create a **Delegation Register** (lightweight: role, delegated authority, delegate name, start/end date, CISO signature) as a record type in FLOW-001. Reference it from RMF-001 §9.7 and OM-001 §4.2. Make delegation explicit, not implied.

### 2.2 🟠 High — Governance: Exception vs. Risk Acceptance Path Confusion Persists
**Location:** `RMF-001 §9.7a`, `PRC-RM-001`, `TMPL-RM-002`
**Problem:** RMF-001 §9.7a explicitly distinguishes "Policy Exception" (Governance-owned) from "Risk Acceptance" (Risk-owned + Business acceptance). But PRC-RM-001 and the Exception Request Form (TMPL-RM-002) **conflate them in a single workflow**. The form says "handles both types" but approval path divergence happens late.
**Risk:** Teams route risk acceptances through Governance exception workflow, bypassing Business Owner acceptance. Or Governance approves risk acceptances they shouldn't.
**Fix:** Split the template into **two distinct forms**: `Security_Exception_Request_Form` (Governance-only, stays in exception register) and `Risk_Acceptance_Request_Form` (requires Business Owner + per-RMF-001 authority). Update PRC-RM-001 to route explicitly.

### 2.3 🟠 High — Governance: No "Stop-the-Line" Escalation Mechanism for Cross-Pillar Disputes
**Location:** `OM-001 §4.3`, `FLOW-001 Principle 10`
**Problem:** OM-001 §4.3: "Disagreements that the pillars cannot resolve are escalated to the CISO... stop-the-line capability for any CERG team member who believes a decision is being made that materially violates policy or creates regulatory exposure." **No procedure, no form, no SLA, no protection for the escalator.**
**Fix:** Add a **Stop-the-Line Record** type to FLOW-001 with fields: trigger, pillar, decision challenged, policy/regulatory citation, CISO disposition, timestamp. Define 24-hour CISO response SLA. Protect escalator from retaliation (reference HR policy).

### 2.4 🟡 Medium — Governance: Risk Appetite Calibration Workbook Is a Placeholder
**Location:** `RMF-001 §9.8.1`
**Problem:** The workbook has fill-in-the-blank fields (`$_________`) but **no worked example, no calibration methodology, no guidance on how Finance/Board arrives at numbers.** "Calibrate them to your organization using the prompts below" is not actionable for a first-time adopter.
**Fix:** Add a **worked calibration example** for a mid-market utility ($1.2B revenue, NERC-CIP + SOX scope) showing inputs → calculations → calibrated bands. Include the math: ALE bands as % of revenue, single-risk ALE as function of insurance retention and downtime cost.

### 2.5 🟡 Medium — Governance: Cyber Oversight Group (COG) Membership Is Static
**Location:** `OM-001 §4.4`, `RMF-001 §8.2`
**Problem:** COG members are fixed titles (CIO, COO, GC, CFO, Enterprise Risk lead). In practice, **risk items cross business units unpredictably** — a cloud risk needs the Cloud Ops VP; an OT risk needs the VP of Generation. Fixed membership means the right decision-maker isn't always in the room.
**Fix:** Make COG membership **dynamic per agenda**: standing core + "Business Unit Risk Owner for systems on agenda" (already implied in OM-001 §4.4 but not explicit in cadence). Add to COG agenda template: "Attendees: core + [BU owners for items 2, 4, 5]."

---

## 3. Architecture & Structural Issues

### 3.1 🔴 Critical — Architecture: No Architecture Decision Records (ADRs) for Framework Choices
**Location:** Entire corpus
**Problem:** CERG makes significant architectural decisions (three pillars, overlay model, FAIR-aligned risk statements, NIST 800-53 as spine, inheritance evidence package, evidence tiers E1/E2/E3) but **captures none of the rationale, alternatives considered, or trade-offs**. Future maintainers cannot distinguish "this was deliberate" from "this was accidental."
**Fix:** Add an **ADR log** (lightweight: ADR-001 Three Pillars, ADR-002 NIST Spine, ADR-003 FAIR Risk Statements, ADR-004 Overlay Model, ADR-005 Evidence Tiers, ADR-006 Inheritance Package). Place in `/governance/adr/` or as a section in FRM-002. Each ADR: status, context, decision, consequences, date, author.

### 3.2 🟠 High — Architecture: RMF Phases Cut Across Pillars Creating Ownership Ambiguity
**Location:** `RMF-001 §2.1` (phase→pillar mapping)
**Problem:** RMF-001 Table §2.1 assigns primary ownership per phase: Categorize→Governance, Select→Governance, Implement→Engineering, Assess→Risk, Authorize→Governance, Monitor→Risk+Governance. But **Implement (Engineering) requires Governance standards; Assess (Risk) requires Engineering baselines; Monitor feeds back to Categorize.** The "supporting pillars" column is too thin to resolve daily friction.
**Fix:** For each phase, add a **RACI sub-matrix** showing *specific activities* (not just phase-level) with R/A/C/I per pillar. Example for "Implement": Baseline design→E(R), G(C); Control implementation→E(R), R(C), G(A for evidence); Handoff package→E(R), R(A), G(C).

### 3.3 🟠 High — Architecture: Crown Jewel Scenarios (CJ-001) Not Integrated with Threat Modeling (PRC-TM-001)
**Location:** `CJ-001 §3.3`, `PRC-TM-001`, `FLOW-001 F-02 §468`
**Problem:** CJ-001 defines "minimum control profile" for Tier 0/1 assets and "loss scenarios become threat-model design targets." But PRC-TM-001 has **no explicit step** to pull crown-jewel scenarios as threat model inputs. FLOW-001 F-02 mentions it as a mandatory rule but no procedural link.
**Fix:** In PRC-TM-001, add a step: "For assets on Crown Jewel Register (CJ-001), import associated loss scenarios as mandatory threat model scenarios. Model attack paths to each chain-breaking control." In CJ-001, add `threat_model_ref` field linking scenarios to TM records.

### 3.4 🟡 Medium — Architecture: Shared Responsibility Decision Table (CB-001 §7.1) Lacks "Provider Evidence Unavailable" Path
**Location:** `CB-001 §7.1`, `CB-001 §5` (Inheritance Evidence Package)
**Problem:** The decision table has a field "Residual Risk If Provider Evidence Is Unavailable" but **no procedural guidance** on what to do when provider attestation is missing, expired, or doesn't cover the customer's scope. Cloud/SaaS providers routinely have gaps.
**Fix:** Add a **Provider Evidence Gap Workflow** to CB-001: (1) Document gap in Shared Responsibility Decision Table, (2) Create compensating control or risk acceptance per RMF-001, (3) Set re-evaluation trigger (contract renewal, attestation expiry, scope change), (4) Escalate to CISO if gap affects Critical/High control.

### 3.5 🟡 Medium — Architecture: No Ephemeral/Dynamic Asset Handling in Asset Management
**Location:** `STD-AM-001` (referenced), `CB-001 CM-8`, `PRC-VM-001`
**Problem:** Asset inventory (Principle 1, CM-8, STD-AM-001) assumes persistent assets with owners. **Containers, serverless functions, CI/CD pipelines, ephemeral cloud resources** have no stable owner, short lifespans, and high churn. Current model: "asset class = Persistent/Dynamic/Ephemeral" (IMP-003 Asset Inventory schema) but no procedural handling for Dynamic/Ephemeral.
**Fix:** In STD-AM-001 or PRC-VM-001, add an **Ephemeral Asset Pattern**: tag-based inventory (not instance-based), pipeline-integrated baseline enforcement (policy-as-code), scan-on-deploy not scan-on-schedule, evidence via pipeline logs not manual collection.

---

## 4. Evidence & Control Effectiveness Issues

### 4.1 🔴 Critical — Evidence: Evidence Tier Definitions (AUD-001) Not Linked to Control Statuses (CB-001 §4)
**Location:** `AUD-001`, `CB-001 §4`, `CB-001 §9`
**Problem:** CB-001 §4 defines 6 control statuses (Implemented, Partially Implemented, Inherited, Planned, Risk Accepted, N/A). AUD-001 defines 3 evidence tiers (E1=self-attestation, E2=system-generated, E3=independent verification). **No mapping** between control status and required evidence tier. "Implemented" could mean E1 or E3 — auditor decides.
**Fix:** Add **Evidence Tier Requirement per Control Status** table to CB-001 §4 or AUD-001:
| Control Status | Minimum Evidence Tier |
|----------------|----------------------|
| Implemented    | E2 (E3 for Critical/High overlay controls) |
| Partially Implemented | E2 for implemented portion + POA&M (E1) |
| Inherited      | Provider E2/E3 + Customer E2 (per §5 package) |
| Planned        | E1 (design artifact) |
| Risk Accepted  | Risk acceptance record (E2) + compensating control evidence |
| Not Applicable | E1 (rationale document) |

### 4.2 🟠 High — Evidence: Control Effectiveness Framework (CEF-001) Exists but Not Integrated into Metrics
**Location:** `CEF-001`, `MTR-001`, `CB-001`
**Problem:** CEF-001 defines control effectiveness testing (design effectiveness, operating effectiveness, testing methods). MTR-001 metrics measure *posture* (vuln SLAs, risk scores, coverage) but **do not measure control effectiveness**. RM-007 "Scenario Defense Coverage" references CEF-001 but is the only metric that does.
**Fix:** Add **control effectiveness metrics** to MTR-001:
- CE-001: % of Implemented controls with current operating effectiveness test (CEF-001)
- CE-002: % of Critical/High overlay controls with E3 evidence
- CE-003: Control testing completion rate vs. annual plan
Link to CEF-001 testing cadence and CB-001 control status.

### 4.3 🟠 High — Evidence: Retrieval SLA (5 Business Days) Assumes Mature Tooling
**Location:** `CB-001 §9.2 Rule 3`, `AUD-001`
**Problem:** "Evidence shall be retrievable within five business days of an auditor request." For a team using spreadsheets and shared drives (IMP-003 §7–8), **5 days is unrealistic** for cross-pillar evidence (e.g., "show me all evidence for AC-6 across Engineering, Risk, and Governance").
**Fix:** Make retrieval SLA **tiered by adoption gate**:
- Gate 1 (Spine): 15 business days (manual collection acceptable)
- Gate 2 (Operating): 10 business days (structured evidence index)
- Gate 3 (Governed): 5 business days (tool-supported)
- Gate 4 (Adaptive): 2 business days (automated evidence pipeline)
Document in AUD-001 and IMP-005 Adoption Gates.

### 4.4 🟡 Medium — Evidence: "Partial = 0.5" Rule (MTR-001 §8.2) Not Enforced in Tooling
**Problem:** MTR-001 §8.2: "Partial = 0.5, not 1. Regulatory implementation percentages count Partially Implemented as half." This is a **scoring rule**, but no validator or calculator enforces it. CAT-001, CB-001, and regulatory packages all track status independently.
**Fix:** Add a **compliance scoring function** to `tools/cerg-validate.py` or a new `cerg-score.py` that reads CAT-001/CB-001/status and produces the weighted implementation percentage per framework. Make it the single source of truth for GV-001, GV-003, GV-005.

### 4.5 🟡 Medium — Evidence: Evidence Freshness Rules (CB-001 §9.2 Rule 1) Conflict with Annual Controls
**Problem:** CB-001 §9.2 Rule 1: "Evidence captured in the prior refresh cycle is current. Evidence older than two refresh cycles is stale." But some controls have **annual refresh** (e.g., CP-4 annual test, CM-7 quarterly). "Two refresh cycles" = 2 years for annual controls — too long for audit.
**Fix:** Change to: "Evidence older than **one refresh cycle plus 30 days** is stale." For annual controls: 13 months. For quarterly: 4 months. For continuous: 30 days. Align with retention requirements per framework.

---

## 5. Metrics & Reporting Issues

### 5.1 🟠 High — Metrics: Predictive Indicators (PL-001–PL-007) Lack Automated Data Sources
**Location:** `MTR-001 §3.7`
**Problem:** PL-001 (MTTE vs Patch Velocity), PL-002 (Attack Surface Change Rate), PL-005 (Control vs Threat Coverage) require **correlation across multiple systems** (CVE feeds, threat intel, asset inventory, ATT&CK mapping, detection rules). No single tool produces these; they require manual analysis.
**Risk:** Predictive metrics become "quarterly manual exercises" that stop when the analyst is busy.
**Fix:** For each PL metric, define a **minimum viable data pipeline**:
- PL-001: CISA KEV feed + vulnerability scanner API + patch management API → daily ratio
- PL-002: CMDB/asset API → monthly delta
- PL-005: ATT&CK mapping file (maintained by Detection Engineer) + detection rule registry → quarterly coverage %
Document in MTR-001 §4 Data Source Map with "MVP pipeline" column.

### 5.2 🟠 High — Metrics: Service Responsiveness Metrics (SR-001–SR-005) Have No Baseline for New Adopters
**Location:** `MTR-001 §3.9`, `SLC-001`
**Problem:** SR metrics measure CERG's own SLA adherence (architecture review turnaround, advisory response, intake disposition). SLC-001 defines commitment values but **new adopters have no baseline** — they will miss SLAs initially and show Red, creating false negative on program health.
**Fix:** Add **adoption-phase SLA targets** to SLC-001 and MTR-001:
| Phase | Architecture Review | Advisory Response | Intake Disposition |
|-------|---------------------|-------------------|-------------------|
| Gate 1 (0-90 days) | 15 business days | 10 business days | 15 business days |
| Gate 2 (90-180 days) | 10 business days | 5 business days | 10 business days |
| Gate 3+ (Mature) | Per SLC-001 | Per SLC-001 | Per SLC-001 |
Report SR metrics with phase context.

### 5.3 🟡 Medium — Metrics: Knowledge Management Metrics (KM-001–KM-003) Measure Activity, Not Resilience
**Location:** `MTR-001 §3.8`
**Problem:** KM-001 (procedure currency), KM-002 (role backup currency), KM-003 (cross-training hours) measure **process compliance**. They don't measure whether knowledge *actually transfers* — e.g., "can the backup Risk Register Owner run the monthly review without the primary?"
**Fix:** Add a **quarterly knowledge resilience test** (tabletop): "Primary X unavailable; Backup Y executes process Z. Result: Pass/Partial/Fail." Record as KM-004. Weight KM-004 higher than KM-003 in dashboard.

### 5.4 🟡 Medium — Metrics: Threshold Calibration (MTR-001 §10) Has No "Reset" Mechanism
**Location:** `MTR-001 §10.3 Rule 1`
**Problem:** "Tighten, do not loosen without cause." But **organizational contraction, budget cuts, or scope reduction** may legitimately require loosening. The rules don't address this.
**Fix:** Add a **Scope Change Trigger** to §10.2: "Significant scope reduction (asset count -20%, team -25%, regulatory scope removed) → review thresholds for loosening with CISO + Finance approval." Document in threshold change log.

---

## 6. Tooling & Automation Issues

### 6.1 🔴 Critical — Tooling: Validator (`cerg-validate.py`) Is Critical Infrastructure But Not Versioned/Documented as Such
**Location:** `tools/cerg-validate.py`, `AGENTS.md`
**Problem:** AGENTS.md: "This is the authoritative CI check — requires 0 errors." But the validator **has no version, no changelog, no test suite, no documentation of validation rules beyond the error classes listed**. It is a single point of failure for every commit.
**Fix:** Treat validator as a **first-class CERG component**:
- Add `tools/VALIDATOR.md` documenting every check, input, output, version
- Add unit tests for each error class (fixture markdown files)
- Version the validator (semantic) and pin version in CI config
- Add `--explain <error_code>` flag for human-readable remediation guidance

### 6.2 🟠 High — Tooling: No Policy-as-Code / Baseline-as-Code Examples
**Location:** `STD-CFG-001 (DISH)`, `PRC-AR-001`, `FLOW-001 F-01`
**Problem:** CERG advocates "policy-as-code," "admission control," "pipeline gates" (FRM-001 §3.2, OM-001 §3.1, FLOW-001 F-02 T3). But **no reference implementations** for OPA/Rego, Kyverno, GitHub Actions, GitLab CI, Terraform Sentinel, or cloud provider policy engines.
**Fix:** Create `/tools/policy-as-code/` with:
- DISH baseline as OPA policies (Linux, Windows, K8s)
- Architecture review gates as GitHub Actions workflow
- Change management admission control example
- CSPM/SSPM policy translation (AWS Security Hub, GCP SCC, Azure Defender)

### 6.3 🟠 High — Tooling: Machine-Readable Index Exists but No Query Layer
**Location:** `machine-readable/cerg-llm-index.json`, `machine-readable/METADATA.yaml`
**Problem:** The index is a **static JSON file** (~825K tokens). No CLI, no API, no query language. Adopters who want to "show me all Risk-owned procedures with OT scope" must write their own parser.
**Fix:** Add a lightweight **query CLI** (`tools/cerg-query.py`):
```bash
cerg-query --pillar risk --type procedure --scope ot
cerg-query --control AC-6 --evidence-tier E2
cerg-query --status Approved --owner "Governance Pillar Leader"
```
Output: JSON, CSV, or markdown table. Use the existing index as data source.

### 6.4 🟡 Medium — Tooling: No Drift Detection for Cross-Reference Integrity
**Location:** `tools/cerg-validate.py`, `AGENTS.md`
**Problem:** Validator checks "LINK_MISSING" (target file exists) but **not semantic drift**: a document references `CERG-GOV-RMF-001 §9.7` but that section was renumbered to §9.8. The link resolves but points to wrong content.
**Fix:** Add **anchor validation** to validator: extract all `#[section-anchor]` references, verify they exist in target file's current headings. Flag "anchor exists but heading text changed >50%" as warning.

### 6.5 🟡 Medium — Tooling: No Automated Catalog Status Sync
**Location:** `CAT-001`, `IMP-001 §7.4`
**Problem:** IMP-001 §7.4: "Every adoption decision updates your copy of CAT-001." But **CAT-001 is a markdown table** — manual updates drift. No tool to sync status from actual file metadata (frontmatter) to catalog.
**Fix:** Add `tools/cerg-catalog-sync.py`: read all markdown frontmatter → generate CAT-001 §5 catalog table → diff → update. Run in CI.

---

## 7. Content & Completeness Issues

### 7.1 🟠 High — Content: AI Security Standard (STD-AI-001) Exists But Integration Is Thin
**Location:** `STD-AI-001`, `IMP-005 §2.3` (regulatory overlay selector), `PRC-TPRM-001`
**Problem:** IMP-005 asks "Do you use AI tools, AI-enabled SaaS, or build AI features?" → add AI Security Standard. But **no integration** with: vendor risk (AI supply chain), threat modeling (AI-specific threats: prompt injection, model extraction, data poisoning), detection (AI-specific detection rules), evidence (model cards, training data provenance).
**Fix:** In STD-AI-001, add cross-references to PRC-TPRM-001 (vendor AI assessment), PRC-TM-001 (AI threat modeling), STD-LM-001 (AI detection rules), CB-001 (AI control overlays). Add an "AI Overlay" to CB-001 §8.

### 7.2 🟠 High — Content: Supply Chain Compromise Response (Beyond Vendor Assessment)
**Location:** `PRC-TPRM-001`, `PRC-IR-002`, `STD-SDL-001`, `SR-2/SR-3 in CB-001`
**Problem:** TPRM covers vendor *assessment*. But **SolarWinds-style supply chain compromise** (trusted vendor, compromised build pipeline) requires: SBOM analysis, build integrity verification, behavioral anomaly detection in vendor-delivered artifacts, coordinated response with vendor. Only SBOM checklist (TMPL-SBOM-001) exists.
**Fix:** Add a **Supply Chain Compromise Playbook** (new procedure or section in PRC-TPRM-001): trigger conditions, SBOM diff analysis, artifact verification, vendor communication template, containment steps, evidence preservation for legal/regulatory.

### 7.3 🟡 Medium — Content: Identity Threat Detection (UEBA) Mentioned But Procedurally Light
**Location:** `OM-001 §6.1` (Identity Risk Analyst), `STD-LM-001`, `MTR-001 PL-007`, `PRC-TI-001`
**Problem:** Identity Risk Analyst role exists. PL-007 tracks "Privileged Account Anomaly Rate." But **no procedure** for: UEBA rule tuning, identity threat triage, identity-based incident response, OAuth/token risk monitoring, service account anomaly detection.
**Fix:** Add an **Identity Threat Detection Procedure** (new or section in PRC-TI-001/PRC-AV-001): data sources (IdP, PAM, CloudTrail, SaaS logs), baseline establishment, alert thresholds, triage playbook, integration with IR (Lead Investigator role).

### 7.4 🟡 Medium — Content: No Explicit Incident Command System (ICS) Integration for OT Emergencies
**Location:** `OM-001 §3.4`, `PLN-IR-001`, `PLN-CIP-001`, `STD-OT-001`
**Problem:** OT environments have **safety-critical incidents** where cyber response must integrate with operational emergency response (ICS/Unified Command). CERG IR plan (owned by standing IR team) and NERC-CIP package don't address: cyber-physical incident command, safety precedence, operational authority vs. cyber authority, joint communication with reliability coordinator.
**Fix:** In PLN-CIP-001 or a new OT-IR annex, add: **Cyber-Physical Incident Command Protocol** — roles (Cyber IC, Operations IC, Unified Command), decision matrix (safety > reliability > security), communication templates (E-ISAC, RC, NERC), evidence preservation under operational urgency.

### 7.5 🟢 Low — Content: "Preliminary Defaults Requiring Organizational Calibration" Pattern Creates Adoption Friction
**Location:** `POL-001` (Impact bands), `RMF-001` (Appetite bands, Impact bands), `CB-001` (Inheritance examples), `MTR-001` (Metric thresholds)
**Problem:** The phrase "preliminary default requiring organizational calibration" appears **15+ times** across documents. Each is a decision point for adopters. No centralized "calibration checklist" exists.
**Fix:** Create a **Calibration Checklist** (appendix to IMP-001 or new document) consolidating every "preliminary default" with: parameter, default value, calibration inputs, calibration method, owning role, review cadence. One place to track all calibrations.

---

## 8. HR/Talent & Organizational Issues

### 8.1 🟠 High — HR: Cross-Pillar Rotation Model Described But Operational Detail Missing
**Location:** `OM-001 §6.5`, `OM-001 §10.4`, `MTR-001 KM-003`, `IMP-001 §10`
**Problem:** Rotation roles defined (Architecture Review Office Hours, IR support, Audit liaison). But **no rotation mechanics**: term length, handoff procedure, training prerequisite, workload balancing, performance evaluation during rotation, return-to-primary-role process.
**Fix:** Add a **Rotation Program Specification** to OM-001 or JA-001: term (6 months), prerequisites (shadow 2 cycles), handoff checklist (1 week overlap), evaluation (separate from primary role), capacity allocation (20% time).

### 8.2 🟡 Medium — HR: Succession Planning (SUCC-001) Is Standalone, Not Integrated into Operating Cadence
**Location:** `SUCC-001`, `OM-001 §7` (Cadence), `MTR-001 KM-002`
**Problem:** SUCC-001 exists as a separate document. OM-001 cadence has no "succession readiness review." KM-002 measures "role backup currency" but SUCC-001 outputs don't feed it.
**Fix:** Add **"Succession Readiness Review"** to OM-001 §7 Quarterly CISO Risk & Posture Review agenda. SUCC-001 outputs (readiness assessments, development plans) become inputs. Update KM-002 to source from SUCC-001.

### 8.3 🟡 Medium — HR: Competency Model (CMP-001) and Job Architecture (JA-001) Not Linked to Hiring/Promotion Workflows
**Location:** `CMP-001`, `JA-001`, `PERF-001`, `IMP-001 §10.4` (Interview Guide)
**Problem:** CMP-001 defines behavioral anchors per grade. JA-001 defines grades. PERF-001 defines evaluation. IMP-001 §10.4 has interview questions. But **no promotion workflow** linking: interview → hire at grade → quarterly check-in → annual eval → promotion packet → calibration → approval.
**Fix:** In PERF-001 or new document, define the **Promotion Workflow**: eligibility criteria, packet contents (evidence per CMP-001 anchor), panel composition (cross-pillar), calibration meeting, timeline, communication. Link to JA-001 grade definitions.

### 8.4 🟢 Low — HR: No "CERG Practitioner" Certification or Badging Path
**Location:** `IMP-001 §10.6`, `TRN-001`
**Problem:** TRN-001 exists (Training Development and Certification Framework). But **no external-facing certification** that signals "this person can operate in a CERG-structured team." Impacts hiring — candidates can't signal CERG fluency; orgs can't filter for it.
**Fix:** Define a **CERG Practitioner Badge** (three tiers: Associate, Professional, Expert) based on: CMP-001 competency demonstration, cross-pillar rotation completion, improvement register contribution, assessment pass. Host on CERG site or GitHub.

---

## 9. Regulatory & Compliance Issues

### 9.1 🟠 High — Regulatory: CIP-015 (INSM) Referenced But Not Operationalized
**Location:** `CB-001 §8` (BES Overlay), `PLN-CIP-001`, `STD-OT-001`
**Problem:** CB-001 BES Overlay: "CIP-015 INSM where applicable." CIP-015 (Internal Network Security Monitoring) is a **major new requirement** for Medium/High Impact BES Cyber Systems. No procedure, no evidence mapping, no metrics, no architecture guidance in CERG.
**Fix:** Add **INSM Implementation Annex** to PLN-CIP-001 or new PRC-INSM-001: network sensor placement (IT/OT boundaries, ESP/EAP), data collection requirements, alerting rules, evidence package, integration with exposure management (PRC-VM-001) and detection (STD-LM-001).

### 9.2 🟡 Medium — Regulatory: CMMC Level 2 / 800-171 Assessment Readiness — No "Mock Assessment" Procedure
**Location:** `PLN-CUI-001`, `PRC-AUD-001`, `MTR-001 GV-001/002`
**Problem:** PLN-CUI-001 covers SSP, POA&M, evidence. But **no procedure for internal mock assessment** (self-assessment against all 110 practices, simulated C3PAO interview, evidence package stress test). Organizations discover gaps at the real assessment.
**Fix:** Add **Mock Assessment Procedure** to PLN-CUI-001 or PRC-AUD-001: scope definition, assessor assignment (internal or partner), practice-by-practice evidence review, interview simulation, findings report, remediation timeline, re-test. Schedule: 6 months before target assessment date.

### 9.3 🟡 Medium — Regulatory: SOX ITGC Evidence Reuse for Hosted Financial Systems (SOC 1) Not Detailed
**Location:** `PLN-SOX-001`, `CB-001 §10.1` (SOX crosswalk), `CB-001 §7.1` (Inheritance)
**Problem:** CB-001 SOX crosswalk: "SOC 1 reuse for hosted financial systems." But **no procedure** for: SOC 1 report gap analysis, complementary user entity controls (CUECs) mapping, bridging SOC 1 control objectives to CERG controls, evidence collection from provider, auditor coordination.
**Fix:** Add **SOC 1 Reuse Procedure** to PLN-SOX-001: report acquisition, CUEC inventory, gap analysis vs. CB-001 controls, compensating controls for gaps, evidence package for external auditor, annual refresh cycle.

---

## 10. Structural Debt & Maintenance Issues

### 10.1 🟠 High — Maintenance: Cross-Reference Density Is High and Fragile
**Location:** Entire corpus
**Problem:** Documents heavily cross-reference (e.g., FRM-001 references OM-001, RMF-001, CB-001, POL-001, 15 standards, 12 procedures, 7 plans, 10 templates, 33 JDs). **Renumbering a section in one document breaks references in 10+ others.** Validator catches missing files but not stale section numbers.
**Fix:** (1) Add anchor validation to validator (see 6.4). (2) Adopt **stable section IDs** (e.g., `§risk-acceptance-authority` instead of `§9.7`) in addition to numbers. (3) Document cross-reference update procedure in STY-001.

### 10.2 🟡 Medium — Maintenance: Document Statuses Drift from Catalog
**Location:** `CAT-001`, individual file frontmatter
**Problem:** CAT-001 §5 is the authoritative catalog. But each document has its own frontmatter `Status` field. **No automated sync** — they drift. Validator checks `STATUS_MISMATCH` but only at CI time.
**Fix:** Make CAT-001 the **single source of truth** for status. Remove `Status` from individual frontmatter (or make it generated). Add `tools/cerg-catalog-sync.py` (see 6.5) that regenerates frontmatter Status from CAT-001 on commit.

### 10.3 🟡 Medium — Maintenance: Revision History Tables Are Manual and Inconsistent
**Location:** Every document §11/§12/Document Control
**Problem:** Each document maintains its own revision history table with varying columns (Version/Date/Author/Change vs Version/Date/Summary). **No standard format**, no automation, hard to query "what changed in v1.21 across all docs?"
**Fix:** Standardize revision history columns: `Version | Date | Author | Change Type (Major/Minor/Patch) | Summary | Linked Issue/PR`. Add `tools/cerg-changelog.py` to aggregate across corpus.

### 10.4 🟢 Low — Maintenance: No "Deprecation Policy" for Documents
**Location:** `CAT-001`, `IMP-005`
**Problem:** Documents can be `Retired` (CAT-001 status) but **no policy** for: when to retire, migration path for dependents, communication, evidence retention for retired controls, crosswalk updates.
**Fix:** Add a **Document Retirement Policy** to CAT-001 or STY-001: criteria (superseded, regulatory scope removed, framework retired), 90-day notice, migration guide for adopters, evidence retention per longest regulatory requirement, crosswalk freeze.

---

## Summary: Top 5 Issues to Address First

| Priority | Issue | Why First | Effort |
|----------|-------|-----------|--------|
| 1 | **VAR-001 Render Tool Missing** | Blocks mechanical adaptation promise; every adopter hits this Day 1 | Medium (tool dev) |
| 2 | **CISO Designee Undefined** | Creates accountability gap in risk acceptance; audit finding waiting to happen | Low (register + process) |
| 3 | **Evidence Tier ↔ Control Status Mapping Missing** | "Implemented" means nothing without evidence tier; auditor discretion creates inconsistency | Low (table + validator rule) |
| 4 | **MVC→Full Adoption Bridge Criteria Missing** | Teams stall at MVC or big-bang; no measurable Gate 2→3 transition | Low (criteria in IMP-005) |
| 5 | **Validator Not Versioned/Tested/Documented** | Single point of failure for all commits; changes risk breaking validation | Medium (tests + docs) |

---

## Next Steps

1. **Owner assignment**: Each issue needs a documented owner (pillar + role) and target date.
2. **Issue tracking**: Move selected issues to `IMPREG-001` (Program Improvement Register) with type, priority, owner, target.
3. **Batch by theme**: Tooling issues (6.1, 6.2, 6.3, 6.4, 6.5) can be a single "Tooling Hardening" epic. Governance issues (2.1, 2.2, 2.3, 2.4) a "Decision Rights Hardening" epic.
4. **Validation**: After fixes, run `cerg-validate.py` and `cerg-integrity-check.py` — zero errors required.

---

*End of issuesv1.md — generated from CERG corpus review (commit as of 2026-06-17). Issues are structural, not cosmetic; each blocks reliable operation at scale or creates silent failure modes.*
