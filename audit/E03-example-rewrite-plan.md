# Task E03 Output: Rewrite targets for examples that underperform

## Scope Reviewed
- Files read:
  - `audit/E01-example-quality.md`
  - `audit/E02-missing-stories.md`
  - `examples/day-in-the-life/README.md`
  - `examples/day-in-the-life/story-8-cerg-lite-maria.md`
  - `examples/day-in-the-life/story-9-f-01-control-intent.md`
  - `examples/day-in-the-life/story-10-new-ciso-90-days.md`
- Sections reviewed:
  - E01 story scorecard, keep/rewrite/expand recommendations, and findings E01-F01 through E01-F07.
  - E02 flow coverage map, candidate story decision table, proposed new stories A-D, and findings E02-F01 through E02-F05.
  - Example README sections for Stories 1-7.
  - Standalone Story 8.
  - Standalone Stories 9 and 10 only to confirm they are promotion/linking targets, not rewrite targets.
- Files intentionally not reviewed:
  - Full source procedures. E03 creates rewrite instructions from E01/E02; it does not re-audit source procedure correctness.
  - Governed document source rewrites. This task remains in audit artifact mode.

## Method
- Steps performed:
  1. Selected every story marked rewrite or expand in E01/E02.
  2. Preserved each scenario unless the scenario itself creates a teaching problem.
  3. For each selected story, named exact sections to change and the intended replacement/addition.
  4. Added cross-story conventions for owner, handoff, record, evidence, metric, and improvement closure.
  5. Identified which proposed new-story ideas should be added as new files rather than forced into existing stories.
- Search terms or scripts used:
  - Manual review of `examples/day-in-the-life/README.md` section headings for Stories 1-7.
  - Manual review of `story-8-cerg-lite-maria.md` sections.
  - Reused E01/E02 findings rather than re-running broad corpus search.
- Assumptions avoided:
  - Did not assume all examples must be equally long. Some should remain compact training vignettes.
  - Did not recommend changing authoritative rules inside examples. Examples should point to source rules, not invent them.
  - Did not merge all missing-story ideas into existing stories where that would overload the original scenario.

## Rewrite Targets Summary

| Story | Current action | Rewrite intensity | Primary purpose |
|---|---|---|---|
| Story 1 — New SaaS application | Expand | Light | Add TPRM contract/evidence lifecycle and metric closure. |
| Story 2 — Critical vulnerability | Promote | None/minor | Keep as canonical F-04; optionally add exact metric IDs when source cleanup is ready. |
| Story 3 — Audit request | Expand | Medium | Strengthen evidence-failure path and audit/evidence metric closure. |
| Story 4 — Major cloud workload launch | Rewrite | Medium | Correct residual-risk authority and add improvement/metric closure. |
| Story 5 — Privileged access review | Expand | Light | Add toxic-combination/access-risk variant and metric IDs. |
| Story 6 — Third-party security incident notification | Rewrite | High | Fix IR boundary; decide whether it remains vendor incident story or becomes F-06 canonical story. |
| Story 7 — Enterprise AI assistant rollout | Expand | Light | Add final pilot disposition, AI-specific records, and metric closure. |
| Story 8 — CERG Lite scanner report | Rewrite | High | Fix Critical vendor exception path and role-consolidation map drift. |
| Story 9 — F-01 regulator change | Promote | None/minor | Keep as canonical F-01; link from FLOW-001 later. |
| Story 10 — New CISO first 90 days | Promote | None/minor | Keep as leadership/adoption arc; label clearly as program arc. |

## Global Rewrite Rules for All Example Edits

Apply these rules to every edited story:

1. **Every operational output should name at least one source record.** Use CAT-002 names where available: Project Security Review Record, Finding Record, Risk Register Entry, Security Exception Record, Evidence Index Entry, Program Improvement Record, Detection Coverage Record, Control Change Record, Oversight Decision Record.
2. **Metric closure should be explicit.** Add a final operational-output bullet in this form: `Metric closure: <metric ID/name or planned metric family> updates from <source record>.`
3. **Risk acceptance language must use current authority model.** Risk assesses/recommends; Governance routes/documents; CISO approves High/Critical program acceptance where required; Business Owner accepts business consequence; Executive Sponsor participates for Critical where required.
4. **Incident examples must preserve adjacent-function boundary.** Incident Commander / standing IR team commands active incident response. CERG supplies context, evidence, owners, and post-incident program changes.
5. **Avoid heroics.** Keep stories within normal cadence when possible. If emergency action occurs, show why the flow supports it rather than relying on a special person saving the day.
6. **Do not add generic exposition.** Add steps, records, evidence, and decisions. Avoid paragraphs that merely summarize policy.

## Story-Specific Rewrite Instructions

### Story 1 — New SaaS application

**File / section:** `examples/day-in-the-life/README.md` → `## Story 1: New SaaS application`

**Preserve scenario:** Yes. Keep customer success SaaS, customer contact data, IdP integration, SIEM logs, six-week go-live.

**Exact sections to change:**

1. **Supporting procedures and standards**
   - Add template references after `Third Party and Supply Chain Risk Procedure`:
     - `Vendor Security Questionnaire and Assessment Template` (`CERG-TMPL-TPRM-001`)
     - `SBOM Request and Attestation Template` (`CERG-TMPL-SBOM-001`) only if software/integration component warrants it.
   - Add `Record Catalog` (`CAT-002`) so the reader sees Vendor Risk Assessment Record and Project Security Review Record as canonical records.

2. **Walkthrough table**
   - Revise Step 4 from generic `Vendor assessment file` to `Vendor Risk Assessment Record; evidence request package`.
   - Add a new step after current Step 4:
     - `Risk and Legal/Procurement translate assessment gaps into contract security clauses: breach notification, log availability, subprocessor notification, right-to-audit, and evidence renewal date.`
     - Primary owner: `Vendor Risk Analyst with Legal/Procurement interface`.
     - Record/evidence: `Contract security clause decision; Vendor Risk Assessment Record`.
   - Revise Step 8 so the missing export-log feature becomes either pre-go-live condition, security exception, or business risk acceptance depending residual risk. Avoid `Risk acceptance package` as a vague phrase.

3. **Example day-in-the-life narrative**
   - In the paragraph beginning `The vendor returns a SOC report...`, add that the Vendor Risk Analyst records the SOC report expiration date and next evidence refresh date.
   - Add one sentence that the contract clause decision is stored with the vendor assessment, not left in procurement email.
   - Keep the export-log limitation, but state: `Risk documents the residual exposure; Governance routes the time-bound exception; the Business Owner accepts any residual business consequence if the risk exceeds Low.`

4. **Operational outputs**
   - Replace `Vendor assessment completed and linked` with `Vendor Risk Assessment Record completed, with SOC report, subprocessors, data residency, contract clauses, and evidence renewal date linked.`
   - Add `Approved Provider / SaaS catalog entry updated where applicable.`
   - Add metric closure bullet:
     - `Metric closure: TP-001/TP-004 where applicable and SR-003/SR-004 update from the intake and vendor assessment records; exception metrics update from the exception register.`

**Acceptance check after rewrite:** A reader should understand not just that Risk assesses the vendor, but how assessment output becomes contract/evidence obligations.

---

### Story 3 — Audit request

**File / section:** `examples/day-in-the-life/README.md` → `## Story 3: Audit request`

**Preserve scenario:** Yes. Keep SOX-relevant privileged access review request.

**Exact sections to change:**

1. **Supporting procedures and standards**
   - Add `Metrics Dashboard and Reporting` and note that audit/evidence metrics may require the AE metric family from the D02 rewrite queue.
   - Add `Control Evidence and Test Worksheet` (`CERG-TMPL-AUD-001`) if control testing is part of the response.

2. **Walkthrough table**
   - Current Step 6 is good but broad. Split it into two rows:
     - Step 6: `Governance rejects or returns incomplete evidence when timestamp, source, period, population, or approver is missing.` Record/evidence: `Evidence quality finding or rejected evidence note`.
     - Step 7: `Rejected evidence or repeated control failure becomes Finding Record or Program Improvement Record, not a scramble-folder fix.` Record/evidence: `Finding Record / Program Improvement Record`.
   - Add final step: `Metric closure updates evidence completeness, rejected evidence, audit request aging, and corrective-action closure metrics.`

3. **Example day-in-the-life narrative**
   - Expand the sentence about the IdP export filename not including timestamp. Make it a stronger evidence-quality decision:
     - The Evidence Librarian marks the original export `quality exception: missing generated timestamp`, requests supporting system-generated metadata, and records why the package is still acceptable or why replacement evidence is needed.
   - Add a short paragraph showing what would happen if evidence cannot be cured: control deficiency finding, corrective action owner, due date, and CISO/Governance visibility for SOX impact.

4. **Operational outputs**
   - Add `Evidence quality finding recorded or evidence accepted with documented limitation.`
   - Add `Submitted package archived exactly as sent to auditor.`
   - Add metric closure bullet:
     - `Metric closure: AE metrics once defined in MTR-001; until then, GV/CE metrics and audit request aging update from the audit intake log and evidence index.`

**Acceptance check after rewrite:** The story should teach that weak evidence is not beautified; it is either cured with source support or becomes a finding/improvement.

---

### Story 4 — Major cloud workload launch

**File / section:** `examples/day-in-the-life/README.md` → `## Story 4: Major cloud workload launch`

**Preserve scenario:** Yes. Keep customer-facing API cloud migration.

**Exact sections to change:**

1. **Supporting procedures and standards**
   - Add `Risk Register and Exception Process` and `Evidence Quality Standard`, because the story includes residual launch risk and evidence verification.
   - Add `Record Catalog` if not otherwise referenced.

2. **Walkthrough table**
   - Revise Step 6:
     - Current: `Risk validates residual launch risks... and determines whether an exception is needed.`
     - Replacement: `Risk assesses residual launch risks and recommends treatment; Governance routes any exception or acceptance; the Business Owner accepts residual business consequence where required.`
     - Record/evidence: `Risk Record, Exception Record, or Risk Acceptance Request`.
   - Add Step 8:
     - `If a launch condition is deferred, the Production Handoff Package names the owner, due date, compensating control, and review date.`
     - Primary owner: `Engineering Pillar / Pre-production Reviewer`.
     - Record/evidence: `Production Handoff Package; Evidence Index Entry`.

3. **Example day-in-the-life narrative**
   - Replace the sentence `Risk accepts one low residual risk...` with:
     - `Risk documents the delayed DDoS exercise as a residual launch risk and recommends a 30-day treatment plan. Because the residual impact is Low and the Business Owner owns the launch consequence, Governance records the Business Owner's time-bound acceptance and the due date. Risk does not accept the business consequence; Risk records the analysis and watches for conditions that would raise the rating.`
   - Add one improvement-loop sentence after release:
     - If delayed DDoS exercises recur across launches, Governance opens a Program Improvement Record to add DDoS exercise scheduling to the pre-production checklist.

4. **Operational outputs**
   - Add `Production Handoff Package completed with deferred-risk section populated.`
   - Add `Business Owner acceptance recorded where residual risk remains.`
   - Add metric closure bullet:
     - `Metric closure: CM-002/SR-001/SR-004 update from the review record; asset coverage metrics update from asset records; exception/risk metrics update from PRC-RM records.`

**Acceptance check after rewrite:** No sentence may say Risk accepts residual risk. The story should teach safe go-live with named business accountability.

---

### Story 5 — Privileged access review finds excessive access

**File / section:** `examples/day-in-the-life/README.md` → `## Story 5: Privileged access review finds excessive access`

**Preserve scenario:** Yes. Keep privileged access review with stale users and contractor account.

**Exact sections to change:**

1. **Situation**
   - Add one clause to make toxic combination explicit:
     - `One retained administrator also holds payment approval authority, creating a toxic combination of privileged system access and business transaction authority.`

2. **Walkthrough table**
   - Revise Step 3 to include toxic-combination evaluation:
     - `Risk evaluates whether stale access or toxic combinations created material exposure, whether activity review is needed, and whether the issue is systemic.`
   - Add a row after Engineering removes access:
     - `Governance preserves reviewer decision, before/after access exports, and removal-ticket timestamps in the evidence package.`
   - Add metric closure row naming ID/access metrics where possible.

3. **Example day-in-the-life narrative**
   - Add a paragraph after the contractor account discovery:
     - The application owner also flags that one admin has payment approval authority. Engineering removes the admin role immediately; Risk checks privileged activity for the review period; Governance records the SoD/toxic-combination issue as an evidence note and finding.
   - Keep the recurring mover issue and improvement item; make the improvement item include toxic-combination detection rules or IGA policy review.

4. **Operational outputs**
   - Add `Toxic-combination finding opened where privileged access intersects business approval authority.`
   - Add `Before/after access exports and removal tickets linked to Evidence Index Entry.`
   - Add metric closure bullet:
     - `Metric closure: ID-002 and ID-003 update from IGA/PAM records; AE metrics update after MTR-001 audit/evidence metric family is defined; Program Improvement Record feeds F-07.`

**Acceptance check after rewrite:** The story should teach both stale access cleanup and risk-based interpretation of toxic combinations without needing a separate story.

---

### Story 6 — Third-party security incident notification

**File / section:** `examples/day-in-the-life/README.md` → `## Story 6: Third-party security incident notification`

**Preserve scenario:** Partially. Keep vendor file-transfer compromise. Rewrite the authority and handoff model substantially.

**Decision before rewrite:** Choose one of two options:

- **Option 6A — keep as vendor-incident triage story.** Story 6 remains about third-party incident notification. Add explicit IR-declaration decision and CERG support boundaries.
- **Option 6B — convert into canonical F-06 story.** Story 6 becomes the post-incident detection/control-feedback story proposed in E02 Story C. If this option is chosen, add a separate smaller vendor incident story later only if needed.

**Recommended option:** Option 6A for now, plus add Proposed Story C later. This preserves vendor-risk coverage while filling F-06 with a cleaner incident-to-improvement example.

**Exact sections to change under Option 6A:**

1. **Situation**
   - Add: `The standing Incident Response team is on call; CERG does not decide active incident command.`

2. **CERG flow pattern**
   - Keep F-06 + F-04, but add sentence:
     - `F-06 applies only after the Incident Commander declares or declines incident status; CERG's role during active response is support.`

3. **Walkthrough table**
   - Replace Step 1 owner `Risk Pillar` with `Vendor Risk Analyst / Risk Pillar`.
   - Replace Step 3 text `Governance confirms notification obligations...` with `Governance supplies regulatory mapping and evidence requirements to the Incident Commander and Legal; Governance does not unilaterally start notification clocks.`
   - Replace Step 4 with two rows:
     - `Vendor Risk Analyst and Risk Pillar summarize exposure facts and recommend whether IR activation criteria may be met.` Owner: Risk. Record: Third-party incident triage record.
     - `Incident Commander declares or declines internal incident status and sets severity if activated.` Owner: Incident Commander. Record: Incident Record or documented no-incident decision.
   - Add a row after containment/recovery:
     - `After stand-down or no-incident decision, CERG records residual vendor risk and program improvements.` Owner: Risk Register Owner / Governance. Record: Risk Register Entry; Program Improvement Record.

4. **Example day-in-the-life narrative**
   - Add the Incident Commander decision explicitly after local logs and data scope are known.
   - If the IC declines incident status because vendor confirms no files accessed, say this is a documented no-incident decision, not a Risk-only determination.
   - If data access remains unknown, show the IC activating the IR plan and CERG providing support inputs.
   - Replace `Governance starts the decision log and confirms who will approve customer communications` with `Governance prepares the regulatory/customer obligation map for the IC + Legal + executive communications path.`

5. **Operational outputs**
   - Add `Incident Commander decision recorded: declared incident, no incident, or monitoring pending facts.`
   - Add `CERG support package delivered: data classification, vendor risk record, affected integration list, local log preservation, evidence limitations.`
   - Add `Post-incident/no-incident improvement: vendor evidence floor, contract clause, or exit criterion updated.`
   - Add metric closure bullet:
     - `Metric closure: TP-002 and TP/vendor-risk metrics update from TPRM records; F-06 improvement metrics update from PRC-LL/IMPREG records; incident metrics remain under the standing IR team's reporting unless explicitly shared.`

**Acceptance check after rewrite:** A reader must be able to answer who decides incident status. The answer must be Incident Commander / standing IR team, not Risk or Governance.

---

### Story 7 — Enterprise AI assistant rollout

**File / section:** `examples/day-in-the-life/README.md` → `## Story 7: Enterprise AI assistant rollout`

**Preserve scenario:** Yes. Keep enterprise assistant for summaries, drafting, and internal search.

**Exact sections to change:**

1. **Supporting procedures and standards**
   - Add AI templates:
     - `AI Intake and Sanctioning Template` (`CERG-TMPL-AI-001`)
     - `Sanctioned AI Tools Register Template` (`CERG-TMPL-AI-002`)
     - `AI System and Model Register Template` (`CERG-TMPL-AI-003`) if built/embedded AI is in scope.
   - Add `Metrics Dashboard and Reporting`.

2. **Walkthrough table**
   - Revise Step 1 record from `Project Intake Record` to `Project Intake Record and AI Intake Record`.
   - Revise Step 5 to name the sanctioned tools register / AI system register decision.
   - Add Step 9:
     - `Governance issues pilot disposition: expand, extend with conditions, restrict, or retire.`
     - Record/evidence: `AI disposition record; Sanctioned AI Tools Register update; Risk Record if conditions remain`.

3. **Example day-in-the-life narrative**
   - After 30-day pilot paragraph, add explicit final decision:
     - `The pilot is extended 30 days rather than expanded because repeated Restricted-data attempts show user guidance is not yet effective. Governance updates the conditions; Engineering keeps connector approvals centralized; Risk opens a watchlist item rather than a formal acceptance because no residual business risk has been accepted yet.`
   - If broad rollout is chosen instead, name evidence required before expansion.

4. **Operational outputs**
   - Add `AI Intake Record and sanctioned-tool/register entry created or updated.`
   - Add `Pilot disposition recorded: expand, extend, restrict, or retire.`
   - Add metric closure bullet:
     - `Metric closure: AI review/adoption metrics update where defined; SR-001/SR-003 may update from intake records; risk/exception metrics update only if residual risks or exceptions are opened.`

**Acceptance check after rewrite:** The story must end with a decision, not just a pilot status update.

---

### Story 8 — CERG Lite: Maria and the Tuesday scanner report

**File / section:** `examples/day-in-the-life/story-8-cerg-lite-maria.md`

**Preserve scenario:** Partially. Keep three-person small-team scanner report and portal Critical closure. Rewrite the vendor SFTP branch.

**Core problem to fix:** The current story teaches a Critical public-exploit vendor exposure as a routine 30-day exception approved by the consolidated Governance/CISO person. That conflicts with PRC-RM, PRC-VM PPR rules, and business-owner acceptance.

**Exact sections to change:**

1. **Situation**
   - No major change needed. Optionally add that the COO/Executive Sponsor is available for business-risk decisions.

2. **How the three pillars collapse onto three people**
   - Replace `Priya owns the scanner schedule and the risk register` with `Priya owns scanner triage and exposure management; Maria owns the risk register as the consolidated Governance/Risk Register Owner.`
   - Replace `Maria is the only person who signs exceptions` with a more precise rule:
     - `Maria routes and approves eligible security exceptions within authority, but the Business Owner accepts business consequence and the Executive Sponsor provides the independent view for Critical risk.`
   - Add one sentence: `When Maria wears both CISO and Governance hats, the Decision Log names which hat she is wearing and when the COO/Executive Sponsor must provide the second set of eyes.`

3. **Walkthrough table**
   - Keep Steps 1-5 mostly as-is.
   - Rewrite Step 6. Two acceptable options:
     - **Option 8A, lower-severity teaching path:** Change SFTP finding to High, not Critical/public exploit. Priya opens Third-Party Finding and Security Exception with compensating monitoring and vendor patch date. Maria routes Business Owner approval if residual risk is above Low. This teaches ordinary small-team exception handling.
     - **Option 8B, keep Critical path:** Keep Critical/public exploit but do not permit ordinary 30-day exception. Priya opens Third-Party Finding and immediately escalates to Maria/CISO. Devin implements temporary block/allowlist or alternate transfer path. Maria brings COO/Executive Sponsor and Operations Director into a same-day decision. If business chooses continued operation, create Risk Acceptance Request with Business Owner/Executive Sponsor acceptance and CISO approval; otherwise block/disable SFTP until vendor remediates. Explain PPR analysis.
   - Recommended: **Option 8B** if the story is meant to show CERG under pressure; **Option 8A** if the story is meant to show routine small-team operations. Do not keep current middle path.
   - Rewrite Step 7 so Maria does not simply approve the exception. She either routes an eligible exception or convenes the business/CISO escalation path.
   - Step 10 should say evidence index includes the decision package, not just an exception row.

4. **Narrative**
   - Replace paragraph beginning `Maria joins for the weekly 1-hour meeting...`.
   - New paragraph for Option 8B:
     - `Maria does not wait for Friday's cadence because the SFTP exposure is Critical and public-exploit. Priya documents the exposure and vendor status. Devin confirms whether the SFTP path can be allowlisted, disabled, or replaced with a secure manual transfer. Maria calls the Operations Director and COO. The decision is either to disable the vendor path until patched, or to accept a time-bound business risk with named compensating controls, CISO approval, and Executive Sponsor concurrence. The Decision Log names the business consequence and the expiration; it does not say security accepted the risk.`
   - Replace Decision Log quote `Vendor-side Critical CVE accepted...` with a quote that names business owner / Executive Sponsor and temporary treatment.

5. **Operating under the 5-person rhythm**
   - Change heading or text if using a three-person team. Current heading says 5-person rhythm while story is three people. Suggested heading: `Operating under the small-team rhythm`.
   - Fix the 8-person growth count from D03 or remove exact headcount until IMP-003 map is unified.

6. **Operational outputs**
   - Replace `1 open Exception Record (SFTP Critical...)` with either:
     - Option 8A: `1 open Security Exception Record for vendor SFTP High finding, with Business Owner approval where residual risk exceeds Low.`
     - Option 8B: `1 Critical vendor exposure decision package: Third-Party Finding, temporary treatment, Business Owner/Executive Sponsor decision, and Risk Acceptance Request or blocked-transfer record.`
   - Replace `1 Decision Log entry recording Maria's exception approval` with `1 Decision Log entry recording which hat Maria wore and which business/executive approver accepted residual consequence.`
   - Add metric closure bullet:
     - `Metric closure: EM-001/EM-004/EM-008 update from exposure backlog; TP metrics update from vendor record; exception/risk metrics update from PRC-RM records.`

**Acceptance check after rewrite:** A small-team reader must understand that consolidation does not collapse business acceptance or Critical escalation.

---

## New Story Addition Instructions from E02

If the author approves growing the example set, add four standalone files rather than embedding them in the README:

1. `examples/day-in-the-life/story-11-pre-production-clean-handoff.md`
2. `examples/day-in-the-life/story-12-ot-maintenance-window.md`
3. `examples/day-in-the-life/story-13-post-incident-detection-gap.md`
4. `examples/day-in-the-life/story-14-business-risk-acceptance.md`

For each new story:
- Use the same structure as Stories 8-10: title, purpose note, situation, CERG flow pattern, supporting docs, walkthrough table, narrative, operational outputs, what this story does not cover, and final cross-reference paragraph.
- Add the story to `examples/day-in-the-life/README.md` story table.
- Update `START-HERE.md` story count.
- Update CAT-001 example count if needed.
- Consider adding direct FLOW-001 worked-example links after source rewrite approval.

Detailed content specs are in `audit/E02-missing-stories.md` under Proposed Story A-D.

## Findings

### E03-F01 High Existing examples need targeted risk-authority rewrites before they can be promoted as canonical training material
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`

Problem: Story 4 and Story 8 contain the highest-risk example defects: Risk accepting residual risk and a consolidated small-team CISO/Governance role approving a Critical vendor exception path without full business-owner/Executive Sponsor treatment.

Why it matters: Examples are often the first thing a new adopter reads. Risk authority drift in examples will propagate faster than risk authority drift in source procedures because examples are easier to copy.

Evidence from corpus:
- E01-F01 and E01-F02.
- D01-F02, C03 risk-acceptance findings, and D03 small-team findings.

Recommended action: Apply Story 4 and Story 8 rewrite instructions before promoting them in FRM-002/FLOW-001 links.

Owner/workstream: Examples / Risk authority cleanup.

### E03-F02 High Story 6 requires more than polish; it needs an authority-model rewrite
Affected files:
- `examples/day-in-the-life/README.md`
- `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`
- `plans/CERG-PLN-IR-001_Incident_Response_Plan.md`

Problem: Story 6's scenario is valuable, but it currently lets Risk and Governance sound too close to incident-declaration and notification decision authority.

Why it matters: IR boundary clarity is a repeated cross-workstream issue. A weak incident example can undo the adjacent-function banner.

Evidence from corpus:
- E01-F03 and E02-F02.
- B02/C01/D02 IR boundary findings.

Recommended action: Rewrite Story 6 under Option 6A and add Proposed Story C as the cleaner F-06 post-incident feedback story.

Owner/workstream: Examples / Adjacent IR boundary.

### E03-F03 Medium Several good stories need metric closure, not narrative overhaul
Affected files:
- `examples/day-in-the-life/README.md`
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

Problem: Stories 1, 3, 5, 7, and 8 mostly work as narratives, but their metric closure is generic. Some cannot be fixed fully until MTR-001 receives audit/evidence metrics.

Why it matters: CERG's story strength depends on showing the full chain: record → evidence → metric → oversight/improvement.

Evidence from corpus:
- E01-F04.
- D02-F04 audit/evidence metric gap.

Recommended action: Add story-level metric closure bullets now using existing MTR IDs where possible; mark AE metrics as dependent on MTR source cleanup.

Owner/workstream: Examples / Metrics traceability.

## Positive Confirmations
- No existing story needs to be cut. The current set has a useful purpose and should be repaired/expanded rather than discarded.
- Stories 2, 9, and 10 are strong enough to serve as canonical examples with only minor linking/labeling changes.
- Stories 1, 3, 5, and 7 need targeted expansions, not structural rewrites.
- The proposed four new stories are additive and can be introduced later without blocking existing story repairs.

## Open Questions
- Should Story 8 keep the high-pressure Critical vendor scenario, or should it be softened to High/Medium to teach routine small-team exception handling?
- Should Story 6 be rewritten as a vendor incident triage story and paired with a new F-06 post-incident story, or should it be converted entirely into the post-incident story?
- Should metric IDs be added before or after MTR-001 receives audit/evidence AE metrics?
- Should story-file restructuring happen before example rewrites, or should the current README layout remain until content is stable?

## Proposed Next Tasks
- G02: include all Story 1/3/4/5/6/7/8 rewrite instructions as section-level rewrite queue entries.
- G02: include new-story additions A-D as optional author decisions.
- G03: include START-HERE story count and README/story-file layout as polish/navigation items.
- H reader tests: validate repaired Story 8 with a small-team adopter persona and repaired Story 6 with an incident-support persona.
