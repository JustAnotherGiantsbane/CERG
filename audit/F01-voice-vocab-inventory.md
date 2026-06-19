# Task F01 Output: Build the CERG voice and vocabulary inventory

## Scope Reviewed
- Files read:
  - `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`
  - `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
  - `governance/CERG-GOV-FRM-001_CERG_Framework.md`
  - `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
  - `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
  - `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
  - Selected best examples from E01: Story 2, Story 9, Story 10, plus Story 8 for small-team language.
- Sections reviewed:
  - STY-001 §2, §6, §8, §9, §12, and §12.5.
  - GEN-001 §1-6.
  - FRM-001 executive summary, design principles, pillar sections, and examples.
  - OM-001 §2-4 and §6 role/pillar language.
  - FRM-002 §2-4 navigation, execution chain, pillar questions, and small-team collapse principle.
  - FLOW-001 §1-7 operating principles, record definitions, required records, decision classes, and flow structure.
- Files intentionally not reviewed:
  - Every procedure and standard. F01 builds the target voice inventory; F02/F03 will scan drift and weak prose across the wider corpus.
  - All role JDs. D01/D02 already captured role naming and JD readability issues.

## Method
- Steps performed:
  1. Extracted explicit house voice rules from STY-001.
  2. Extracted canonical terms, role names, record types, and conversion terms from GEN-001 and FLOW-001.
  3. Extracted signature phrases and operating principles from FRM-001, OM-001, FRM-002, FLOW-001, and the strongest examples.
  4. Converted the extracted voice into a reusable authoring guide: preferred verbs, discouraged verbs, role names, record names, exact-definition terms, and example sentence patterns.
  5. Identified the difference between CERG's voice and generic GRC/security writing.
- Search terms or scripts used:
  - Targeted reads of the source files named in the F01 task.
  - Manual extraction of vocabulary tables and signature phrases.
- Assumptions avoided:
  - Did not treat every memorable phrase as a slogan to repeat everywhere.
  - Did not convert voice guidance into source edits.
  - Did not resolve all term drift here. F02 is the term-drift task.

## CERG House Voice Inventory

### Core Voice Rule

CERG writing is operational. It should let a reader answer, quickly:

1. What governs this work?
2. Who owns it?
3. What must happen?
4. What record proves it happened?
5. What evidence supports the record?
6. What metric, oversight decision, or improvement follows?

If a paragraph cannot answer at least one of those questions, it probably belongs in a shorter introduction, a table, or nowhere.

### Voice Attributes

| Attribute | What it means in CERG | Test question |
|---|---|---|
| Direct | Uses active sentences and named roles. | Can I tell who acts? |
| Practical | Describes real work, not aspirations. | Could a small team do this on Monday? |
| Declarative | States the rule without hedging. | Does it avoid unnecessary `may`, `should`, and advisory fog? |
| Evidence-oriented | Names records, evidence, source systems, and closure criteria. | What proves this happened? |
| Opinionated where ambiguity creates risk | Chooses a path where vagueness would create accountability failure. | Does this prevent a bad decision? |
| Clear about ownership and handoffs | Shows the primary owner, supporting roles, and next owner. | Where does work go next? |
| Scalable | Preserves role questions even when people consolidate. | Do the questions survive in a five-person team? |

### CERG Is Not Generic GRC

| Generic GRC/security writing | CERG writing |
|---|---|
| Describes intent without workflow. | Converts intent into roles, records, evidence, metrics, and improvement. |
| Says `the security team should review`. | Says `Engineering reviews the design; Risk validates residual exposure; Governance records evidence and routes exceptions`. |
| Treats compliance as a checklist. | Treats compliance as the evidence exhaust of a working program. |
| Uses maturity language as aspiration. | Uses maturity language to define observable operating behavior. |
| Avoids conflict by saying all stakeholders collaborate. | Names the accountable owner and the escalation path. |
| Treats exceptions as approvals. | Treats exceptions as temporary, evidenced deviations with expiration and named accountability. |

## Preferred Verbs

Use these verbs because they create action, ownership, and evidence.

| Verb | Use when | Example pattern |
|---|---|---|
| owns | A role is accountable for an activity or record. | `The Evidence Librarian owns the evidence index.` |
| operates | A role runs a procedure or cadence. | `The Exposure Management Lead operates the exposure pipeline.` |
| records | A role creates durable traceability. | `Governance records the exception decision.` |
| validates | A role tests whether a condition is true. | `Risk validates reachability before severity is finalized.` |
| verifies | A role confirms closure evidence or control operation. | `Risk verifies treatment before the finding closes.` |
| routes | A role sends work to the correct authority. | `Governance routes High risk acceptance to the CISO.` |
| escalates | A missed SLA or material risk moves to higher authority. | `The Risk Register Owner escalates expired exceptions to the Governance Pillar Leader.` |
| links | Evidence or records are connected. | `The change record links to scan evidence and service validation.` |
| updates | A record, metric, register, or dashboard changes. | `Governance updates the CISO dashboard after closure.` |
| closes | A record reaches explicit closure criteria. | `The finding closes after validation evidence is linked.` |
| blocks | A gate prevents unsafe action. | `Engineering blocks go-live until the pre-production finding is resolved or accepted through the proper path.` |
| accepts | Use only for business risk acceptance by the right actor. | `The Business Owner accepts the residual business consequence.` |
| approves | Use only where authority exists. | `The CISO approves High risk acceptance per RMF-001.` |
| concurs | A supporting authority agrees without owning the consequence. | `Risk concurs that the compensating control reduces exposure.` |

## Discouraged Verbs and Phrases

| Avoid | Why | Prefer |
|---|---|---|
| supports, without object | Too vague. | `supplies evidence`, `reviews design`, `validates exposure`. |
| coordinates | Often hides ownership. | Name the exact action: `routes`, `convenes`, `records`, `tracks`. |
| ensures | Can imply impossible control without action. | `verifies`, `checks`, `requires`, `records`. |
| manages | Too broad unless paired with a record/cadence. | `operates the risk register`, `runs monthly review`. |
| reviews, alone | Does not say what decision follows. | `reviews and approves`, `reviews and returns`, `reviews and records finding`. |
| addresses | Hides treatment choice. | `remediates`, `exceptions`, `accepts`, `monitors`, `blocks`. |
| best practice | Generic and unactionable. | State the requirement or evidence rule. |
| robust security | Marketing language. | Name the control, record, or test. |
| industry standard | Decorative unless defined. | Cite the specific standard and implemented requirement. |
| responsible for | Often weaker than RACI language. | `accountable for`, `owns`, `operates`, `approves`. |
| accepted risk, as a casual noun | Blurs authority and record type. | `Risk Acceptance Request`, `Risk Acceptance Memo`, `Business Owner acceptance`. |
| waiver | Blurs exception discipline. | `Security Exception Record` unless the parent process uses waiver. |

## Preferred Role Names

Use canonical role names from OM-001/GEN-001. Do not invent local roles when a canonical role exists.

### Pillar and leadership roles

- Chief Information Security Officer (CISO)
- Executive Sponsor
- Engineering Pillar Leader
- Risk Pillar Leader
- Governance Pillar Leader
- Business Owner
- Asset Owner
- Technical Owner

### Engineering roles

- Cloud Security Engineer
- Identity Engineer
- OT Security Engineer
- Application Security Engineer
- Endpoint Engineer
- Cryptography Engineer
- Pre-production Reviewer

### Risk roles

- Exposure Management Lead
- Adversarial Testing Lead
- Threat Intelligence Analyst
- Vendor Risk Analyst
- OT Risk Analyst
- Identity Risk Analyst
- Detection Engineer

### Governance roles

- NERC-CIP Compliance Manager
- CMMC / Federal Compliance Manager
- SOX ITGC Lead
- Policy & Standards Manager
- Risk Register Owner
- Evidence Librarian

### Adjacent roles

- Incident Commander
- Lead Investigator

### Role terms to avoid or define locally

| Term | Guidance |
|---|---|
| security team | Avoid when assigning work. Name Engineering, Risk, Governance, CISO, or a canonical role. |
| GRC | Avoid as an owner. Use Governance Pillar, Evidence Librarian, Compliance Manager, or Risk Register Owner. |
| system owner | Define as Business Owner, Asset Owner, or Technical Owner depending on accountability. |
| project sponsor | Acceptable as a local project role, but map risk accountability to Business Owner. |
| engineering lead / governance lead in incident context | Use only as incident assignments staffed by canonical roles. Do not make them new CERG roles. |
| risk manager | Replace with Risk Pillar Leader, Risk Register Owner, or Business Owner depending on meaning. |

## Preferred Record Names

Use these exact names when referring to durable CERG records.

| Record name | Use when |
|---|---|
| Project Intake Record | A new project, SaaS, platform, app, integration, or major change enters review. |
| Architecture Review Record | Engineering records design review scope, findings, and disposition. |
| Threat Model Record | A threat model is performed or updated. |
| Project Security Review Record | A project review is stored as the canonical project-security artifact. |
| Production Handoff Package | A system moves from review into production. |
| Asset Record | An asset is registered, classified, owned, or coverage-validated. |
| Asset Coverage Record | Security coverage for logging, scanning, backup, endpoint, identity, or monitoring is validated. |
| Finding Record | An observed condition requires disposition. |
| Exposure Backlog Item | A vulnerability/exposure requires tracking through the exposure pipeline. |
| Risk Register Entry / Risk Record | A loss-event scenario has owner, treatment, and acceptance decision. |
| Security Exception Record | A temporary deviation from a control or requirement is approved. |
| Risk Acceptance Request / Risk Acceptance Memo | Business accepts residual risk through the authority path. |
| Change Record | A security-relevant change is implemented and evidenced. |
| Incident Record | The standing IR team records a declared incident. |
| Incident Action Log | Active incident actions, owners, and timestamps are recorded. |
| Evidence Index Entry / Evidence Record | Evidence is collected, indexed, quality-checked, and retained. |
| Program Improvement Record / Improvement Record | A lesson, metric miss, maturity gap, audit issue, or recurring failure becomes improvement work. |
| Control Change Record | Governance-originated control intent becomes implementation work and validation. |
| Reporting Metric Record | A metric value, source, period, threshold, and assigned action are recorded. |
| Oversight Decision Record | A CISO, COG, board, or executive risk/resource decision is recorded. |

## Terms Requiring Exact Definition

These terms should not be used casually. If they appear, their meaning should match GEN-001/FLOW-001/RMF-001.

| Term | Exact-use rule |
|---|---|
| vulnerability | A technical weakness; raw input that becomes a Finding only after triage. |
| finding | An observed condition requiring disposition. Not automatically a Risk. |
| risk | A loss-event scenario with owner, treatment, and acceptance decision. |
| exception | Temporary deviation from a control or requirement, with compensating controls, expiration, and named approver. |
| risk acceptance | Business Owner decision to operate with known residual risk; security does not accept business consequence. |
| residual risk | Remaining risk after controls/treatment are considered. |
| control gap | Missing or ineffective control, usually systemic. |
| incident | Declared security event under the standing IR team's authority. |
| evidence | Timestamped, attributable artifact demonstrating control operation. |
| record | Durable system-of-record object for work, decision, evidence, or metric. |
| metric | Defined measurement with source record, period, threshold, owner, and action path. |
| implemented | Control is operating with evidence, not merely documented. |
| accepted | Use only with named authority, scope, rationale, expiration/review date, and record. |
| monitor only | Must include guardrails, trigger conditions, owner, and review cadence. |

## Signature Phrases and How to Use Them

These phrases are valuable because they teach CERG's model. Use them sparingly and only when the surrounding text operationalizes them.

| Phrase | Source flavor | Use when | Do not use when |
|---|---|---|---|
| `Consistency is a control.` | STY-001 | Explaining why structure, metadata, links, and role names matter. | As decorative preface without a concrete style or validation rule. |
| `Compliance as exhaust.` / `Evidence is the exhaust of a working program.` | FRM-001 / PRC-AUD voice | Explaining evidence generated by operations. | To imply compliance happens automatically without evidence discipline. |
| `Build securely. Deploy confidently. Consult continuously.` | Engineering mission | Introducing Engineering's role. | Assigning post-production risk ownership to Engineering. |
| `Know your exposure. Manage it deliberately. Never be surprised.` | Risk mission | Introducing Risk's role. | Justifying Risk as risk acceptor. |
| `Set the rules. Track the work. Enable the business to move with confidence.` | Governance mission | Introducing Governance's role. | Making Governance sound like blocker or owner of all decisions. |
| `The questions do not collapse, only the heads.` | FRM-002 small-team principle | Explaining CERG Lite role consolidation. | Avoiding separation-of-duty requirements. |
| `The handoffs are explicit. The records are explicit. The clock is explicit.` | FRM-002 voice | Explaining flow discipline. | Replacing actual handoff, record, or SLA detail. |
| `No issue may remain in an undefined state.` | FLOW-001 | Explaining conversion rules and closure discipline. | Forcing every observation into risk register too early. |
| `Business owns the consequence.` | RMF/PRC-RM voice | Explaining risk acceptance. | Letting business override technical facts or regulatory obligations. |
| `CERG does not command the incident. CERG makes the incident runnable.` | PRC-IR voice | Explaining adjacent IR support. | Making CERG accountable for active IR operations. |

## Good CERG Sentence Patterns

Use these patterns when drafting or rewriting.

| Pattern | Example |
|---|---|
| Owner + action + record | `Risk validates reachability and opens the Finding Record before the SLA clock starts.` |
| Owner + handoff + next owner | `Engineering implements the fix and hands validation evidence to Risk for closure testing.` |
| Rule + evidence | `The exception is not approved until compensating-control evidence is linked.` |
| Decision + authority | `The Business Owner accepts the residual consequence; the CISO approves the High-risk acceptance path.` |
| Trigger + route | `If the exception expires without renewal, the Risk Register Owner creates a High-severity Finding Record.` |
| Small-team clarity | `Maria is one person, but she records whether she is acting as CISO, Governance, or Risk Register Owner.` |
| Adjacent-function boundary | `The Incident Commander directs containment; CERG supplies asset context, logs, evidence, and post-incident improvement actions.` |
| Metric closure | `Governance updates EM-008 from the exposure backlog after Risk records the SLA miss.` |

## Weak Non-CERG Sentence Patterns

| Weak sentence | Why it fails | CERG rewrite |
|---|---|---|
| `The security team should review high-risk changes.` | No owner, no output, weak verb. | `Engineering reviews high-risk changes and records the disposition in the Change Record; Risk participates when exposure thresholds are met.` |
| `Evidence should be collected for audits.` | Passive, vague, no cadence or role. | `The Evidence Librarian collects quarterly access-review evidence and indexes it by control, system, period, and source.` |
| `Risk may be accepted by leadership.` | Vague authority. | `The Business Owner accepts residual business risk; the CISO approves High and Critical acceptance paths per RMF-001.` |
| `Incident response will coordinate with Governance.` | Hides command boundary. | `The Incident Commander commands active response; Governance supplies regulatory mapping, evidence support, and post-incident reporting inputs.` |
| `Exceptions are tracked as needed.` | No owner, no expiration, no record. | `The Risk Register Owner tracks each Security Exception Record with owner, compensating controls, expiration date, and renewal decision.` |
| `The team will improve the process later.` | No trigger, owner, or record. | `Governance opens a Program Improvement Record when the recurring finding is confirmed and assigns an owner and due date.` |

## Findings

### F01-F01 Medium Canonical role spelling differs between GEN-001 and broader workforce usage for Policy & Standards Manager
Affected files:
- `governance/CERG-GOV-GEN-001_CERG_Glossary.md`
- `governance/CERG-GOV-OM-001_CERG_Operating_Model.md`
- `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md`
- `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-004_Policy_and_Standards_Manager.md`

Problem: GEN-001 lists `Policy and Standards Manager`, while OM/RAC/JD usage elsewhere uses `Policy & Standards Manager` as the canonical role. The filename spells out `and`, but the canonical role line and role roster should be consistent.

Why it matters: F01 is building a reusable vocabulary inventory. A small exact-name mismatch in a canonical role list undermines later F02 term-drift scanning and role-set matching.

Evidence from corpus:
- GEN-001 §6 lists `Policy and Standards Manager`.
- STY-001 examples and multiple governance documents use `Policy & Standards Manager`.
- D01 already found role exact-match issues can matter even where the meaning is obvious.

Recommended action: In source cleanup, align GEN-001 to the canonical role name used by OM/RAC/JD, or formally decide that ampersand and `and` are equivalent for this one role and document the alias.

Owner/workstream: Vocabulary / Workforce canonical names.

### F01-F02 Medium The voice guide prefers exact records, but the corpus still uses competing record labels
Affected files:
- `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md`
- `governance/CERG-GOV-CAT-002_Record_Catalog.md`
- `governance/CERG-GOV-FRM-002_Framework_System_Map.md`
- `examples/day-in-the-life/README.md`

Problem: F01's target voice depends on exact record names. Prior C/E work found record-name drift such as control implementation record vs Control Change Record, audit request ticket vs Evidence Index Entry / audit intake log, and generic Reporting Metric Record references without metric IDs.

Why it matters: CERG's voice is record-centered. If record names drift, prose can sound operational while still failing traceability.

Evidence from corpus:
- FLOW-001 uses `Control Change Record`; FRM-002 flow table says F-01 primary output is `Control implementation record`.
- CAT-002 has canonical records, but examples sometimes use generic labels such as `Vendor assessment file` or `Reporting Metric Record`.
- E01/E03 recommended metric and record-name cleanup in examples.

Recommended action: F02 should scan for record-name drift and produce a replacement table. G02 should align FLOW/FRM/CAT/example record labels around CAT-002/FLOW-001 canonical names.

Owner/workstream: Vocabulary / Record catalog alignment.

### F01-F03 Low STY-001's no-em-dash rule is stricter than the established spine voice
Affected files:
- `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md`
- Spine and example documents using conversational emphasis

Problem: STY-001 prohibits em dash characters, but the strongest CERG prose often uses punchy, conversational contrast. Many existing documents use punctuation-driven emphasis, including dash-like separators and direct callout phrasing. The rule is clear, but the actual house voice sometimes leans on that rhythm.

Why it matters: Low severity. This is a style-enforcement issue, not a conceptual defect. If the no-em-dash rule remains, F03 should treat em dashes as polish defects. If the author wants the spine's conversational rhythm preserved, STY-001 may need a narrower rule.

Evidence from corpus:
- STY-001 §9.2: `No em dash characters`.
- FRM/OM/FRM-002 examples use strong contrast and short punchy sentences that sometimes depend on dash-style pacing.

Recommended action: Decide whether `no em dash` is a hard mechanical rule or a general readability preference. If hard, add an automated check and queue replacements. If not hard, revise STY-001 to say avoid overuse rather than prohibit.

Owner/workstream: Style / G03 polish.

## Positive Confirmations
- CERG already has a distinctive and coherent voice: practical, owner-centered, evidence-centered, and skeptical of performative compliance.
- STY-001's five-question test is the right north star for all rewrite work.
- GEN-001 and FLOW-001 provide a strong vocabulary backbone for record types and conversion rules.
- FRM-002 is one of the clearest expressions of the model: policy to evidence to metrics, three pillar questions, explicit handoffs, and small-team collapse without losing accountability.
- The strongest examples already sound like CERG: Story 2, Story 9, and Story 10 show work becoming records, evidence, metrics, and improvement without generic security theater.

## Open Questions
- Should `Policy & Standards Manager` be the single canonical spelling, or should `Policy and Standards Manager` be an accepted alias?
- Should `Control Change Record` replace `Control implementation record` everywhere, or should CAT-002 define both as separate record types?
- Should examples cite exact metric IDs even before the audit/evidence AE metric family is added to MTR-001?
- Is the no-em-dash rule an absolute mechanical gate or a style preference that should allow exceptions in narrative examples?
- Should the signature phrases be centralized in STY-001 as approved house-language patterns?

## Proposed Next Tasks
- F02: run term-drift scans against the vocabulary inventory above and produce context-specific replacements.
- F03: use the weak sentence patterns above to identify prose that violates house voice.
- G02: include source cleanup for role spelling, record-name drift, and Story metric/record specificity.
- G03: include no-em-dash enforcement decision, START-HERE story count, and minor punctuation/readability polish.
