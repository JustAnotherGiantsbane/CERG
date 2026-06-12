# CERG Living Roadmap

**Created:** 2026-06-11
**Source:** Comprehensive external review — 170+ suggestions across adoption, architecture, evidence, compliance, engineering, and community
**Purpose:** Track all improvement opportunities. Items are not commitments — they are prioritized suggestions for maintainers and contributors.

---

## Priority Model

| Level | Meaning |
|-------|---------|
| **P0** | Contradictions, broken references, unsafe defaults, regulatory overclaims — fix immediately |
| **P1** | Adoption blockers, missing examples, missing small-team guidance, missing evidence guidance |
| **P2** | Nice-to-have: diagrams, additional overlays, tooling integrations, filled templates |
| **P3** | Long-term: community growth, release management, external review board |

---

## 1. Claims & Framing

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 1.1 | Tighten "program in a box" language — add "adopters still need to supply..." disclaimer | P0 | ✓ DONE |
| 1.2 | Add adoption readiness checklist (named CISO, asset scope, tooling, authority, etc.) | P1 | — |
| 1.3 | Split repo into /source-framework/ and adopter packages (/starter-small/, /starter-midmarket/, /example-utility/) | P2 | — |

## 2. Adoption Guidance

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 2.1 | Small-team adoption path with reduced operating rhythm | P1 | ✓ DONE in IMP-003 §3 |
| 2.2 | "What not to adopt yet" guide — which docs to defer until spine is running | P1 | ✓ DONE in IMP-002 §2 |
| 2.3 | Adoption anti-patterns section (forking = complete, deleting roles, etc.) | P1 | ✓ DONE in IMP-002 §3 |
| 2.4 | Decision log template (Decision ID, date, rationale, alternatives, docs affected) | P1 | ✓ DONE in IMP-002 §4 |
| 2.5 | Adoption diff report (tokens changed, docs deferred, placeholders, pending approvals) | P1 | — |
| 2.6 | CERG Lite package for small teams | P1 | ✓ DONE in IMP-003 §2 |
| 2.7 | CERG Regulated Utility package | P2 | — |
| 2.8 | CERG CMMC starter package | P2 | — |
| 2.9 | "When CERG is not a good fit" section | P0 | ✓ DONE |
| 2.10 | "CERG is not a certification scheme" statement | P0 | ✓ DONE |

## 3. Reader Experience

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 3.1 | Reader paths in README (CISO path, Engineering path, Auditor path, etc.) | P0 | ✓ DONE |
| 3.2 | Glossary-only artifact with definitions, synonyms to avoid, source documents | P1 | — |
| 3.3 | One-page adoption map | P2 | — |
| 3.4 | "First 10 records to create" guide | P1 | ✓ DONE in IMP-003 §5 |
| 3.5 | "First month success criteria" | P1 | ✓ DONE in IMP-003 §6 |
| 3.6 | FAQ for skeptical teams | P2 | — |
| 3.7 | Plain-English policy summaries per standard | P2 | — |
| 3.8 | Business owner quick guides (how to accept risk, request exception, etc.) | P2 | — |

## 4. Document Quality & CI

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 4.1 | CI checks: Approved+Pending, Draft+Approved, missing owner, broken x-ref, TBD/placeholder in approved | P0 | Partial — cerg-validate.py exists; needs expansion |
| 4.2 | Mandatory metadata schema validation per artifact type | P1 | — |
| 4.3 | Document orphan report | P2 | — |
| 4.4 | Relationship graph (policy→standards→procedures→templates→evidence) | P2 | — |
| 4.5 | Contradiction tracker (public issue tracker for known conflicts) | P1 | — |
| 4.6 | Stable artifact ID policy — IDs never reused, retired IDs reserved | P0 | ✓ DONE |
| 4.7 | Deprecation policy — superseding docs identify predecessor | P1 | — |
| 4.8 | Generated validation report per commit | P1 | — |

## 5. Release & Migration

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 5.1 | Versioned GitHub releases (v1.0.0, v1.1.0, etc.) | P2 | — |
| 5.2 | Changelog per release | P2 | — |
| 5.3 | Migration guide for upstream changes | P2 | — |
| 5.4 | Breaking-change flag when roles, IDs, statuses, or workflows change | P2 | — |
| 5.5 | Plain-language changelog | P2 | — |

## 6. Architecture & Data Model

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 6.1 | Explicit source-of-truth model (Markdown=policy, GRC=risk, CMDB=assets, IAM=identity) | P1 | — |
| 6.2 | Reference data model with normalized objects and relationships | P2 | — |
| 6.3 | Implementation examples for common tooling stacks | P2 | — |
| 6.4 | Minimum tooling capability matrix (required now, later, optional) | P2 | — |
| 6.5 | Manual fallback schemas for spreadsheets when no GRC exists | P1 | ✓ DONE in IMP-003 §7 |
| 6.6 | Record naming convention (RISK-YYYY-NNN, FIND-YYYY-NNN, etc.) | P1 | — |
| 6.7 | Record retention by record type | P2 | — |
| 6.8 | Human-readable + machine-readable parity validation | P1 | — |
| 6.9 | Stable requirement IDs (CERG-REQ-AC-001, etc.) | P1 | — |

## 7. Evidence & Audit

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 7.1 | Explicit evidence quality rules (who produced, when, tamper-resistant, repeatable, etc.) | P1 | — |
| 7.2 | Bad evidence examples (screenshot no date, email "done," vendor says yes) | P1 | — |
| 7.3 | Sampling methodology for audit/evidence work | P1 | — |
| 7.4 | Control design vs operating effectiveness distinction | P1 | — |
| 7.5 | Evidence freshness rules per evidence type | P1 | — |
| 7.6 | Control test scripts / pseudo-tests per control | P2 | — |
| 7.7 | Minimum viable evidence library structure | P1 | ✓ DONE in IMP-003 §8 |
| 7.8 | Recovery evidence standards (restore test records, RTO/RPO achieved) | P2 | — |

## 8. Controls & Risk

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 8.1 | Control status decision tree (applicable? designed? operating? evidenced?) | P1 | — |
| 8.2 | Control inheritance examples with shared-responsibility analysis | P1 | — |
| 8.3 | Shared-responsibility model for cloud/SaaS/MSP/OT | P1 | — |
| 8.4 | Asset criticality model (Tier 0-4) for SLA/logging/backup/review mapping | P1 | — |
| 8.5 | Crown jewels workflow (identify, map dependencies, map identities, threat scenario) | P2 | — |
| 8.6 | Finding vs risk vs issue vs exception clarity everywhere | P0 | ✓ DONE in FLOW-001 §1 |
| 8.7 | Risk promotion rules (when does vulnerability become risk register entry?) | P1 | — |
| 8.8 | Closure validation rules (who can close, evidence required, retest?) | P1 | — |
| 8.9 | Recurring finding escalation rules | P1 | — |
| 8.10 | Root cause taxonomy | P2 | — |
| 8.11 | Control failure severity classification | P2 | — |
| 8.12 | Business-owner accountability enforcement in templates | P1 | — |

## 9. Risk Appetite & Metrics

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 9.1 | Risk appetite calibration workbook (revenue, downtime cost, fine exposure, etc.) | P1 | — |
| 9.2 | Risk acceptance expiration defaults (Critical 30d, High 90d, Medium 180d, Low 365d) | P1 | ✓ DONE in IMP-002 §5 |
| 9.3 | "Risk acceptance is not remediation" warning | P1 | — |
| 9.4 | Risk appetite exception workflow | P2 | — |
| 9.5 | Materiality guidance for board reporting | P2 | — |
| 9.6 | Metrics that should not be used alone (vanity metrics warning) | P1 | — |
| 9.7 | Quality metrics for the program itself | P1 | — |
| 9.8 | Executive briefing examples (good risk trend slide, bad vanity slide) | P2 | — |
| 9.9 | Stoplight adoption score (Green/Yellow/Red readiness) | P2 | — |
| 9.10 | Program maturity gates (Level 0-5) | P2 | — |

## 10. Engineering & Operations

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 10.1 | Process swimlane diagrams for core workflows | P2 | — |
| 10.2 | Explicit entry/exit criteria per workflow | P1 | — |
| 10.3 | Minimum viable process records per procedure | P1 | — |
| 10.4 | SLA exception logic (false positive, vendor patch unavailable, OT maintenance) | P1 | — |
| 10.5 | Security architecture pattern library | P2 | — |
| 10.6 | Minimum diagrams per system type (context, data flow, trust boundary) | P2 | — |
| 10.7 | Threat model trigger rules | P1 | — |
| 10.8 | Threat model light vs full | P1 | — |
| 10.9 | Secure SDLC depth tiers (Tier A-D by risk) | P1 | — |
| 10.10 | Policy-as-code examples (OPA, Sentinel, Azure Policy) | P2 | — |
| 10.11 | Detection-as-code examples with MITRE mapping | P2 | — |
| 10.12 | Detection coverage matrix | P2 | — |
| 10.13 | Identity as Tier 0 emphasis | P1 | — |
| 10.14 | SaaS governance depth (inventory, SSO, MFA, SCIM, audit log, exit plan) | P1 | — |
| 10.15 | AI system lifecycle guidance expansion | P2 | — |

## 11. Asset & Dependency Management

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 11.1 | Business process mapping requirement | P2 | — |
| 11.2 | Dependency map requirement for critical systems | P2 | — |
| 11.3 | Asset owner accountability matrix (business, app, tech, data, control, risk, evidence) | P1 | — |
| 11.4 | Asset lifecycle integration | P2 | — |
| 11.5 | Decommissioning/offboarding depth | P2 | — |
| 11.6 | Shadow IT/SaaS discovery process | P2 | — |

## 12. Vendor & Supply Chain

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 12.1 | Procurement intake language triggers | P1 | — |
| 12.2 | Model contract clauses for third-party risk | P2 | — |
| 12.3 | Supplier concentration risk tracking | P2 | — |
| 12.4 | Open-source/software supply chain controls | P2 | — |
| 12.5 | Data flow review for vendors | P2 | — |
| 12.6 | Minimum security baseline for all vendors | P1 | — |

## 13. Incident Response & Resilience

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 13.1 | IR boundary unmistakable — "included for interface completeness" banners | P0 | ✓ DONE |
| 13.2 | Tabletop exercise templates (ransomware, BEC, cloud admin compromise, etc.) | P2 | — |
| 13.3 | Lessons learned integration map | P2 | — |
| 13.4 | Privacy breach vs security incident handoff | P2 | — |
| 13.5 | Legal privilege handling for investigations | P2 | — |
| 13.6 | Communications during incident interface | P2 | — |
| 13.7 | Cyber insurance interface | P2 | — |
| 13.8 | Safety impact field for OT risks/findings | P1 | — |

## 14. Compliance & Regulatory

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 14.1 | "Do not accidentally claim" guidance per framework | P1 | ✓ DONE in IMP-002 §6 |
| 14.2 | CMMC realism guidance | P1 | ✓ DONE in IMP-002 §6 |
| 14.3 | NERC-CIP caution guidance | P1 | ✓ DONE in IMP-002 §6 |
| 14.4 | Mapping confidence levels (Direct, Partial, Supports, Not equivalent) | P1 | — |
| 14.5 | Source citations for regulatory mappings | P2 | — |
| 14.6 | Assumptions behind each mapping | P2 | — |
| 14.7 | Regulatory overlay selection wizard | P2 | — |
| 14.8 | Framework comparison table (NIST CSF, ISO 27001, CIS, CERG) | P2 | — |
| 14.9 | "Do not map everything to everything" warning | P1 | — |
| 14.10 | External assessor packet template | P2 | — |

## 15. Roles & Workforce

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 15.1 | Role collision guide for small teams (safe vs risky combinations) | P1 | ✓ DONE in IMP-002 §7 |
| 15.2 | Minimum separation of duties tables per process | P1 | — |
| 15.3 | RACI conflict detection in machine-readable layer | P2 | — |
| 15.4 | Decision rights table (who recommends, decides, consulted, informed) | P2 | — |
| 15.5 | Training plan for adopting CERG | P2 | — |
| 15.6 | Communications plan for rollout | P2 | — |

## 16. Culture & Communication

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 16.1 | Security culture guidance ("yes, and" examples) | P2 | — |
| 16.2 | Language shift examples (not "denied" but "conditions needed") | P2 | — |
| 16.3 | Authority hierarchy diagram (law→contract→policy→standards→procedures→templates) | P2 | — |

## 17. Examples & Templates

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 17.1 | Filled-out artifact examples (risk register entry, acceptance memo, exception) | P1 | — |
| 17.2 | Bad example / good example sections for key processes | P1 | — |
| 17.3 | Sample board risk appetite statement | P2 | — |
| 17.4 | Sample generated validation report output | P2 | — |
| 17.5 | Security team operating calendar examples (5-person, 15-person, 60-person) | P2 | — |
| 17.6 | Meeting agendas for recurring reviews | P2 | — |
| 17.7 | Go-live with open risk checklist | P2 | — |

## 18. Community & Governance

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 18.1 | GitHub issue templates (contradiction report, broken x-ref, etc.) | P2 | — |
| 18.2 | CONTRIBUTING.md | P2 | — |
| 18.3 | SECURITY.md for the repo | P2 | — |
| 18.4 | License/adoption note for commercial use (plain English) | P2 | — |
| 18.5 | "Not legal/regulatory advice" disclaimer | P1 | — |
| 18.6 | Public roadmap | P2 | — |
| 18.7 | Maintainer notes — explain philosophy decisions | P2 | — |
| 18.8 | Known contradictions resolved section | P1 | — |
| 18.9 | Adopter feedback form | P2 | — |
| 18.10 | Public examples of adopters (anonymized case studies) | P3 | — |
| 18.11 | External reviewer model | P3 | — |
| 18.12 | Adopter maturity self-check after 30 days | P2 | — |
| 18.13 | "What to simplify first" guidance | P2 | — |

## 19. Adopter Tooling

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 19.1 | Implementation backlog template | P2 | — |
| 19.2 | Program improvement register examples | P2 | — |
| 19.3 | Local tailoring boundaries (safe vs dangerous changes) | P1 | ✓ DONE in IMP-002 §8 |
| 19.4 | Assumptions register | P2 | — |
| 19.5 | Exception debt reporting | P2 | — |
| 19.6 | Funding/investment linkage template | P2 | — |
| 19.7 | Risk treatment option comparison template | P2 | — |

## 20. Non-Utility Adopter Support

| # | Suggestion | Priority | Status |
|---|-----------|----------|--------|
| 20.1 | Localization guidance for non-utility adopters (personas: SaaS, healthcare, gov, etc.) | P2 | — |
| 20.2 | Manual workaround and operational fallback fields for critical systems | P2 | — |
| 20.3 | Safety/reliability integration for OT | P2 | — |
| 20.4 | Records retention schedule examples | P2 | — |
| 20.5 | Privacy integration handoffs | P2 | — |
