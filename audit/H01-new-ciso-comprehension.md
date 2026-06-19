# Task H01 Output: New CISO path comprehension test

## Scope Reviewed
- Files read for first-pass CISO path:
  - `README.md`
  - `START-HERE.md`
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
  - `governance/CERG-GOV-FRM-001_CERG_Framework.md`
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`
  - `examples/day-in-the-life/story-10-new-ciso-90-days.md`
- Authoritative files read for correction/comparison:
  - `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`
  - `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
  - `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` §9.6-§9.7a
  - `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` §1-§5
- Sections reviewed:
  - First-hour CISO orientation, adoption paths, MVC, operating model, COG/CISO decision rights, metrics dashboard, and new-CISO example.
  - Authoritative adoption gate, dependency, checklist, RACI, and risk-acceptance authority sections.
- Files intentionally not reviewed:
  - Full corpus. H01 tests whether a new CISO can understand the model quickly from likely first-read documents.
  - All examples. Story 10 was selected because it is the obvious new-CISO path example.
  - Full RMF/PRC-RM/RAC line-by-line. Only authority-correction sections were needed for this comprehension test.

## Method
- Steps performed:
  1. Read only the likely first-hour CISO documents.
  2. Answered the six H01 questions as if I had no deeper corpus knowledge.
  3. Read authoritative adoption, checklist, RACI, and risk-acceptance files.
  4. Compared first-pass answers against authoritative answers.
  5. Identified first-hour reader friction and recommended front-door changes.
- Search terms or scripts used:
  - Targeted reads of H01-required documents.
  - Prior audit memory used only after first-pass answers were formed, to check whether observed friction had already been captured.
- Assumptions avoided:
  - Did not assume the CISO would read every linked document.
  - Did not treat known back-office accuracy as sufficient if the front-door path could still teach a stale idea.
  - Did not require a new CISO to understand implementation details beyond first decisions, ownership, operating spine, metrics, and adoption risks.

## First-Pass Answers From Likely CISO Reading Only

### 1. What is CERG?

CERG is a cybersecurity operating model, not a control catalog or certification checklist. It gives a security function a spine of policies, standards, procedures, roles, records, evidence, metrics, and improvement loops. It is built around three accountable pillars:

- Engineering: builds and operates secure systems.
- Risk: understands exposure and drives treatment.
- Governance: sets rules, records decisions, manages evidence, and reports conformance.

A CISO would likely understand that CERG is meant to make security operational: work enters a flow, gets an owner, creates a record, produces evidence, updates metrics, and feeds improvement.

### 2. What decisions does the CISO own?

From first-pass reading, the CISO appears to own or chair:

- Whether the organization is ready to adopt CERG.
- Adoption path selection: Lite, Standard, Regulated overlay.
- Approval/signature of the Cybersecurity Policy and program direction.
- COG formation and chairing.
- Budget and resource allocation across pillars.
- Risk appetite defaults or calibration schedule.
- High/Critical risk acceptance approval and escalation.
- Board/executive reporting posture.
- Stop-the-line escalation for material policy/regulatory exposure.
- Expansion from MVC to Standard/Regulated scope.
- Resourcing decisions based on metrics/workload.

The CISO also owns making sure CERG is not adopted as shelfware: records, evidence, cadence, and owners must exist.

### 3. What does CERG deliberately not own?

First-pass reading makes this relatively clear in OM-001:

- Security Awareness program ownership.
- Incident Response operations, the IR plan, exercises, and regulatory notification clocks.
- Non-cyber Physical Security.
- Privacy program ownership.
- Non-cyber Business Continuity.
- Legal obligations/certification readiness decisions.

CERG supports those adjacent functions with standards, evidence, asset context, risk records, and post-incident improvement, but it does not command them.

### 4. What is the minimum operating spine?

The first-pass answer is slightly inconsistent depending on which front-door file is read.

README and START-HERE say the minimum viable CERG spine is eight documents:

1. Cybersecurity Policy
2. CERG Framework
3. Operating Model
4. Document Catalog
5. Risk Management Framework
6. Risk Register & Exception Process
7. Risk Register Templates
8. Exposure Management Procedure

FRM-002's system spine is broader and conceptually more complete:

```text
Policy -> Framework -> Operating Model -> RMF -> Control Baseline -> Standards -> Procedures/Plans -> Templates/Records -> Evidence -> Metrics/Oversight -> Program Improvement
```

As a new CISO, I would interpret the eight-document MVC as the first adoption package and FRM-002 as the full operating chain to grow into.

### 5. How does the CISO know whether the program is working?

A CISO is told to look for operating evidence, not activity volume. The key signals are:

- Metrics dashboard and COG brief from MTR-001.
- Risk register health: open High/Critical risks, residual risk score, risk concentration, expired/aging exceptions.
- Exposure metrics: confirmed reachable critical exposures, KEV reachability, SLA misses with/without controls, observation-to-decision time.
- Engineering metrics: architecture reviews before production, baseline drift, backup/restore evidence.
- Governance/regulatory metrics: evidence currency, SOX/CUI/CIP posture, policy/standard currency.
- Service responsiveness: architecture review turnaround, intake disposition, advisory response, time-to-coverage.
- Evidence quality: records and evidence links support metrics.
- Improvement loop: findings, audits, incidents, and metrics create Program Improvement Register items.
- Board/COG reporting: top five risks and trend/comparison over snapshots.

The CISO should also know adoption is working if the first 30/90-day checklists produce named records, role assignments, evidence store decisions, initial risk register, exposure backlog, and improvement backlog.

### 6. What could go wrong in adoption?

The first-pass CISO would identify these failure modes:

- No named security owner or executive sponsor.
- Leadership wants tools, not guardrails/decisions/evidence.
- Scope is unclear: systems, business units, regulators are not named.
- Records and evidence are not maintained.
- The organization forks/approves documents but does not operate the cadence.
- MVC is skipped and the team tries to adopt the whole corpus at once.
- Roles collapse in small teams without preserving the questions/accountability.
- Risk acceptance or exceptions become informal approvals.
- Metrics become shallow activity counts.
- Regulatory alignment is claimed without operational package/evidence.
- Front-door documents are followed literally where stale examples still contain older authority language.

## Corrected Answers After Authoritative Files

| Question | First-pass answer quality | Corrected/confirmed answer |
|---|---|---|
| What is CERG? | Strong | Correct. CERG is an operating model with a policy-to-evidence-to-improvement chain. FRM-002 is the clearest short explanation. |
| What decisions does the CISO own? | Mostly strong, with one risk-acceptance caveat | CISO approves cybersecurity-program side of High/Critical acceptance but does not accept business consequence alone. RMF §9.7 says Business Owner/Executive Sponsor acceptance is required where business impact exists. COG is not risk-acceptance authority. |
| What does CERG not own? | Strong in OM-001 | Correct in OM-001. However, examples/IR docs elsewhere can still blur incident ownership; a first-hour reader who sees only OM gets the right answer. |
| Minimum operating spine | Understandable but split between MVC and full spine | MVC is the first adoption set; FRM-002 is the full operating chain. IMP-005 adds that Record Catalog, FRM-002, checklists, and decision tree are recommended/required-path adoption aids even if not in the eight MVC. |
| How does CISO know program works? | Strong conceptually | Correct. Add authoritative nuance: metrics must have one system of record, evidence links, phase-context during adoption, and source failure handling. Missing DT metrics are a back-office defect but do not block first-pass understanding. |
| What could go wrong? | Strong | Correct and expanded by IMP-005: unsafe tailoring includes deleting the risk register, informal exceptions, Engineering accepting high risk, un-evidenced controls, standards without procedures/records, scans without ownership/SLA/exception handling, optionalizing vendor review, and removing document control. |

## Reader Friction in the First Hour

### H01-F01 High Story 10 teaches stale risk-acceptance authority language to the exact target persona
Affected files:
- `examples/day-in-the-life/story-10-new-ciso-90-days.md`

Problem: Story 10 says: `Exception and risk acceptance authority mapped (Priya for High and Critical, Sara for Medium with Priya notification)` and later says Priya routes a Medium-risk decision `through Priya for acceptance`. The authoritative RMF says the Business Owner accepts business consequence and the CISO/pillar roles approve or document on the cybersecurity side.

Why it matters: Story 10 is the most likely example for a new CISO. A first-hour CISO could copy the stale pattern and build an authority map that omits Business Owner/Executive Sponsor acceptance.

Evidence from corpus:
- Story 10 first 30-day deliverables assign High/Critical authority to Priya and Medium to Sara.
- RMF §9.7 requires Business Owner or Executive Sponsor acceptance where business impact exists.
- IMP-006 says `Confirm exception and risk acceptance authority` but does not itself explain the Business Owner distinction.

Recommended action: Rewrite Story 10's authority language before using it as canonical CISO onboarding material. Suggested pattern: `Cybersecurity approval path mapped: CISO approval for High/Critical, pillar/Governance approval for lower tiers as defined in RMF; Business Owner or Executive Sponsor acceptance required for business consequence.`

Owner/workstream: Examples / G02-R15 or additional Story 10 rewrite item.

### H01-F02 Medium The front door gives two different versions of the minimum spine
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md`

Problem: README/START-HERE define the MVC as eight documents. FRM-002 defines a broader operating spine that includes Control Baseline, FLOW, CAT-002, AUD-001, MTR-001, and IMPREG. IMP-005 says some of those are recommended or Required-Path for adoption projects.

Why it matters: A new CISO may ask, `Do I need 8 documents or the full FRM-002 spine to start?` The distinction is understandable after reading more, but should be explicit up front.

Evidence from corpus:
- README: `The minimum viable CERG spine is eight documents...`
- START-HERE: `Adopt these eight documents first.`
- FRM-002: full spine includes metrics, evidence, improvement, records, control baseline.
- IMP-005: Record Catalog, FRM-002, Role-Based Checklists, and Decision Tree are recommended for all / required-path for first adoption projects.

Recommended action: Add one sentence to README/START-HERE: `The eight MVC documents are the first governed adoption set; FRM-002 shows the full operating chain you build toward. Use CAT-002, IMP-005, and IMP-006 as adoption aids from day one even if they are not part of the MVC approval package.`

Owner/workstream: Front-door adoption clarity.

### H01-F03 Medium START-HERE still says seven day-in-the-life stories
Affected files:
- `START-HERE.md`

Problem: START-HERE says the Day in the Life examples contain `seven narrative walkthroughs`, but the example set includes ten stories and separate files for Stories 8-10.

Why it matters: Low operational risk, but START-HERE is the first page. Visible count drift reduces confidence in the navigation layer.

Evidence from corpus:
- START-HERE helper bullet says `seven narrative walkthroughs`.
- Example set includes Stories 1-7 in README plus standalone Stories 8, 9, and 10.

Recommended action: Update the count or remove the number. Prefer: `Day in the Life examples - narrative walkthroughs showing how the three pillars produce real work...`

Owner/workstream: G03 safe/context-sensitive polish.

### H01-F04 Medium New CISO path does not clearly separate CISO approval from business acceptance early enough
Affected files:
- `START-HERE.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`
- `examples/day-in-the-life/story-10-new-ciso-90-days.md`

Problem: A CISO learns early that they must confirm exception and risk acceptance authority, but the Business Owner/Executive Sponsor distinction appears only after reading RMF. Story 10 then reinforces stale CISO-centered acceptance language.

Why it matters: Risk acceptance is a first-30-days CISO decision. The front-door path should prevent a new CISO from designing an authority map that security owns alone.

Evidence from corpus:
- IMP-006 §3.2 has action `Confirm exception and risk acceptance authority` with output `Authority map recorded`.
- RMF §9.7 explains the distinction clearly.
- Story 10 uses Priya/Sara acceptance language.

Recommended action: In IMP-006 §3.2 or START-HERE, add a parenthetical pointer: `Confirm RMF §9.7 authority: security approves/recommends; Business Owner or Executive Sponsor accepts business consequence.`

Owner/workstream: Adoption clarity / risk authority.

### H01-F05 Medium CISO metrics understanding is strong, but MTR-001 has visible internal defects that may distract a careful executive
Affected files:
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Problem: MTR-001 gives excellent principles and dashboard structure, but a careful reader may notice an orphan revision-history row under the metrics dictionary, an empty `Detection Metrics` section, and malformed `||` rows in the data-source map.

Why it matters: MTR-001 is a CISO-facing artifact. Even if the conceptual model is strong, visible table defects undermine confidence in reporting rigor.

Evidence from corpus:
- §3.1 table begins with a row that looks like revision-history content.
- §3.2b `Detection Metrics` heading has no metric rows.
- §4 includes leading `||` rows in data-source map.
- C02/D02/G02 already queued metric-definition cleanup.

Recommended action: Treat MTR-001 as a priority polish/rewrite target before public CISO onboarding promotion. Add detection metrics and repair table drift via G02-R17/G03.

Owner/workstream: Metrics / CISO-facing polish.

### H01-F06 Low FRM-001 visible duplicate punctuation appears in the first CISO reading path
Affected files:
- `governance/CERG-GOV-FRM-001_CERG_Framework.md`

Problem: FRM-001 contains `NERC-CIP,,` and `800-171,,` in front-door text.

Why it matters: Low severity, but FRM-001 is one of the first credibility artifacts a new CISO reads.

Evidence from corpus:
- Same issue identified in A02 and G03 safe mechanical fixes.

Recommended action: Apply the safe exact punctuation fixes from G03.

Owner/workstream: G03 polish.

### H01-F07 Medium The first-hour path explains what to read, but not the first three decisions in one place
Affected files:
- `README.md`
- `START-HERE.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md`

Problem: The CISO can find the first 48-hour checklist, but the front door does not summarize the first three CISO decisions in a single sentence/table.

Why it matters: A real CISO under time pressure wants decision compression. The documents eventually answer this, but first-hour comprehension would improve if README or START-HERE said: `First decide readiness, adoption path, and role/authority map.`

Evidence from corpus:
- START-HERE lists many first 48-hour actions.
- IMP-006 gives the exact CISO checklist.
- FRM-002 has navigation but not a first-decision summary.

Recommended action: Add a short `First three CISO decisions` callout to START-HERE:
1. Are we ready to adopt CERG, or should we start lighter?
2. Which adoption path and overlays apply?
3. Who holds Engineering, Risk, Governance, Executive Sponsor, Business Owner, and risk-acceptance roles during the first 90 days?

Owner/workstream: H01 front-door improvement.

## Positive Confirmations

- A new CISO can understand CERG's core claim within the first hour: operating model, not control framework.
- FRM-002 is an excellent map and should remain the front-door system guide.
- OM-001 clearly states what CERG does not own, especially Incident Response, Awareness, Privacy, BCP, and Physical Security.
- MTR-001 gives the right executive reporting philosophy: trend, concentration, residual score, source-of-record, and audience altitude.
- IMP-006 is practical and immediately actionable for first 48 hours, first 30 days, and first 90 days.
- START-HERE successfully discourages shelfware adoption and tells teams not to adopt the full library in week one.

## Open Questions

- Should Story 10 remain the primary new-CISO story before its authority language is corrected?
- Should the MVC definition include CAT-002/FRM-002/IMP-005/IMP-006 as `adoption aids required for first implementation` even if not governed MVC documents?
- Should START-HERE include a visible `first three CISO decisions` callout?
- Should MTR-001 receive CISO-facing polish before H01 outputs are used externally?

## Proposed Next Tasks

- H02 practitioner path comprehension test.
- Add Story 10 to the G02 example rewrite queue or amend G02-R15 to include it explicitly.
- Apply G03 safe polish for FRM-001 and START-HERE story count before using front-door docs for public onboarding.
- Prioritize MTR-001 cleanup because it is a CISO-facing confidence artifact.
