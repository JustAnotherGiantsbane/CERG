## DOCUMENT CATALOG AND NAMING CONVENTION — AnyTech Adaptation

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On document status change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech CERG document corpus |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Naming Convention](#2-naming-convention)
3. [Current Document Inventory](#3-current-document-inventory)
4. [Deferred Documents](#4-deferred-documents)
5. [Document Lifecycle](#5-document-lifecycle)
6. [Document Control](#6-document-control)

---

## 1. Purpose and Scope

This document catalogs the AnyTech CERG document corpus. It records what documents have been adopted, what has been deferred, and the status of each artifact. This is the single authoritative inventory for AnyTech's CERG library.

### 1.1 Scope

This catalog covers the AnyTech-adapted CERG corpus: 10 adopted documents plus adoption aids. It does not attempt to catalog the full CERG library — those documents are tracked here as deferred but not individually listed.

---

## 2. Naming Convention

AnyTech retains the standard CERG document ID format:

`CERG-<TYPE>-<DOMAIN>-<NNN>`

Where:
- TYPE ∈ {POL, GOV, PRC, TMPL}
- DOMAIN: policy/function abbreviation
- NNN: sequential number

File naming:
`<DocumentID>_<Short_Title>.md`

AnyTech-adapted documents carry the suffix "(AnyTech Adaptation)" in the document title and version field. The Document ID itself is unchanged to preserve cross-reference compatibility with the upstream CERG corpus.

---

## 3. Current Document Inventory

### Adopted: Core Operating Documents (10)

| # | Document ID | Title | Version | Status | Owner |
|---|-------------|-------|---------|--------|-------|
| 1 | CERG-POL-001 | Cybersecurity Policy | 1.0 (AnyTech) | Approved | Governance Pillar Leader |
| 2 | CERG-GOV-FRM-001 | CERG Framework | 1.0 (AnyTech) | Approved | Engineering Pillar Leader |
| 3 | CERG-GOV-OM-001 | Operating Model | 1.0 (AnyTech) | Approved | Engineering Pillar Leader |
| 4 | CERG-GOV-CAT-001 | Document Catalog | 1.0 (AnyTech) | Approved | Governance Pillar Leader |
| 5 | CERG-GOV-RMF-001 | Risk Management Framework | 1.0 (AnyTech) | Approved | Risk Pillar Leader |
| 6 | CERG-PRC-RM-001 | Risk Register and Exception Process | 1.0 (AnyTech) | Approved | Risk Pillar Leader |
| 7 | CERG-TMPL-RM-001 | Risk Register Templates and Reporting | 1.0 (AnyTech) | Approved | Risk Pillar Leader |
| 8 | CERG-PRC-TPRM-001 | Third-Party and Supply Chain Risk Procedure | 1.0 (AnyTech) | Approved | Governance Pillar Leader |
| 9 | CERG-PRC-VM-001 | Exposure Management Procedure | 1.0 (AnyTech) | Approved | Risk Pillar Leader |
| 10 | CERG-GOV-IMP-001 | Implementation and Adaptation Guide | 1.0 (AnyTech) | Approved | Governance Pillar Leader |

### Adoption Pack

| File | Path | Purpose |
|------|------|---------|
| README.md | `adoption-packs/anytech-lite/README.md` | Human adoption guide |
| agent-prompt.md | `adoption-packs/anytech-lite/agent-prompt.md` | AI-assisted adoption prompt |
| document-list.yaml | `adoption-packs/anytech-lite/document-list.yaml` | Structured document list |
| cerg-org-profile-anytech.yml | Root of CERG repo | Token values for render tool |

### Adoption Aids (from CERG Standard Library)

| Document ID | Title | Use |
|-------------|-------|-----|
| CERG-GOV-IMP-003 | Small Team Adoption Path | Role consolidation patterns |
| CERG-GOV-IMP-006 | Role-Based Implementation Checklists | First-action checklists |
| CERG-GOV-CAT-002 | Record Catalog | Minimum record definitions |

---

## 4. Deferred Documents

The following document categories from the full CERG library are explicitly deferred by AnyTech. The rationale is documented here for traceability.

### Not Adopted — Provider-Owned Function

These documents describe functions that AnyTech has delegated to providers. They are not adopted by AnyTech because the provider maintains equivalent documentation on their side:

- **Incident Response Plan (PLN-IR-001)** — MSSP maintains their own IR plan
- **Incident Response Playbooks (PRC-IR-002)** — MSSP maintains their own playbooks
- **Training Development Framework (TRN-001)** — Training vendor owns this
- **Business Continuity/DR Plan (PLN-BC-001)** — MSP maintains backup/restore; MSSP maintains IR BCP

### Not Adopted — Not in Scope

These documents describe capabilities, roles, or regulatory requirements that do not apply to AnyTech:

- All 7 regulatory packages (CIP, CUI, CMMC, SOX, ISO, Privacy) — no regulatory drivers in scope
- All 15 technical standards (STD-*) — MSSP/MSP bring their own standards; AnyTech sets requirements via contracts and this policy
- Workforce planning (WFP-001) — 8-person team; headcount planning is informal
- Succession planning (SUCC-001) — 8-person team; succession is ad-hoc
- Performance management (PERF-001) — 8-person team; informal
- Maturity self-assessment (MAT-001) — too early; revisit at 6-month mark
- Contractor integration guide (CON-001) — no contractors
- Stakeholder perception survey (TMPL-GOV-001) — no CISO to own it

### Not Adopted — Overhead Without Return

These documents describe practices that require more administrative overhead than they would return for an 8-person program-office team:

- All per-role job descriptions (JD-*) — 8 people wear 5+ hats each
- All job families beyond JF-001 overview
- Board/CISO reporting deck template (TMPL-MTR-001) — report to IT Director via 1-page monthly
- Unified Control Baseline (CB-001) — adopt only when a control framework is required
- Control Effectiveness Framework (CEF-001) — adopt with CB-001
- Cross-Pillar Flows (FLOW-001) — the adopted procedures are sufficient for initial operation
- Competency Model (CMP-001) — no training function
- Performance Management (PERF-001) — not enough people to need a framework
- Edge Register (EDG-001) — not needed at this scale
- Crown Jewel Register (CJ-001) — data lives in MSP-managed systems; treat via identity/access baselines
- Orchestration/Policy-as-Code artifacts — overkill for 8-person team

---

## 5. Document Lifecycle

### Statuses

| Status | Meaning |
|--------|---------|
| **Approved** | Document is current and authoritative |
| **Draft** | Document is being written or revised |
| **Pending Review** | Document awaiting approval or next review cycle |
| **Superseded** | Document replaced by a newer version |
| **Deferred** | Not adopted; documented reason in §4 |

### Review Cycle

- Core operating documents are reviewed annually by the Governance Pillar Leader
- Documents are triggered for early review on: material incident, provider change, regulatory change, or IT Director direction
- The Governance Pillar Leader maintains the review schedule and tracks upcoming reviews

---

## 6. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | CERG Governance | Initial AnyTech catalog. 10 adopted documents, 50+ deferred with rationale. |

### Review Triggers

- Document status changes (new adoption, deferral reversal)
- Annual review cycle
- Change in provider landscape
- Direction from IT Director

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Cybersecurity Policy | [POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) | Parent policy |
| Operating Model | [OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Defines operating context |
| Small Team Adoption Path | CERG-GOV-IMP-003 | Reference for consolidation patterns |
