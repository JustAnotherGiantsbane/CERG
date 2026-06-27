## IMPLEMENTATION AND ADAPTATION GUIDE — AnyTech Adaptation

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-001 |
| **Version** | 1.0 (AnyTech Adaptation) |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (AnyTech CERG) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy_AnyTech.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On profile token change |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | None currently in scope |
| **Environments** | AnyTech CERG adoption |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The AnyTech Adaptation Profile](#2-the-anytech-adaptation-profile)
3. [Adoption Workflow](#3-adoption-workflow)
4. [Document Adopted vs. Deferred](#4-document-adopted-vs-deferred)
5. [Role Consolidation for AnyTech](#5-role-consolidation-for-anytech)
6. [Provider Integration Points](#6-provider-integration-points)
7. [Key Deployment Decisions](#7-key-deployment-decisions)
8. [First 30-Day Checklist](#8-first-30-day-checklist)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

This guide describes how AnyTech implements the adapted CERG framework. It is a companion to the [AnyTech CERG Lite adoption pack](../../adoption-packs/anytech-lite/README.md) and the [Organization Adaptation Profile](../../cerg-org-profile-anytech.yml).

### 1.1 What This Guide Covers

- How to use the AnyTech profile with the CERG render tool
- Which documents are adopted and which are deferred
- Role consolidation guidance for the 8-person team
- Integration points with MSSP, MSP, and training vendor
- A 30-day implementation checklist

### 1.2 Prerequisites

Before starting adoption, confirm:

- [ ] IT Director confirmed as executive risk acceptance authority
- [ ] Three pillar leaders identified (Engineering, Risk, Governance)
- [ ] MSSP contract in place with SLA commitments
- [ ] MSP contract in place with SLA commitments
- [ ] Training vendor contract in place
- [ ] `cerg-org-profile-anytech.yml` filled with current values

---

## 2. The AnyTech Adaptation Profile

AnyTech's adaptation profile lives at [`/cerg-org-profile-anytech.yml`](../../cerg-org-profile-anytech.yml) in the CERG repository root.

### 2.1 Tokens Set for AnyTech

| Token | AnyTech Value |
|-------|--------------|
| `{{ORG_NAME}}` | AnyTech |
| `{{ORG_LEGAL_NAME}}` | AnyTech, Inc. |
| `{{ORG_SHORT_NAME}}` | AnyTech |
| `{{ORG_SECTOR}}` | technology services |
| `{{CERG_TEAM_SIZE}}` | 8 |
| `{{ENG_STAFF}}` | 3 |
| `{{RISK_STAFF}}` | 3 |
| `{{GOV_STAFF}}` | 2 |
| `{{SCALE_TIER}}` | small |
| `{{IR_TEAM_NAME}}` | AnyTech MSSP IR Team |
| `{{EXEC_BODY_NAME}}` | IT Director |
| `{{COG_NAME}}` | IT Director Review |

### 2.2 Rendering the Corpus

To produce the AnyTech-specific corpus:

```bash
python3 tools/cerg-render.py \
  --profile cerg-org-profile-anytech.yml \
  --source . \
  --out rendered-anytech
```

The adapted documents in `examples/anytech-profile/` use AnyTech-specific content (program office model, MSSP/MSP references, IT Director authority) directly rather than through token substitution. They reference each other using relative paths within the `examples/anytech-profile/` directory.

---

## 3. Adoption Workflow

### Step 1 — Confirm Architecture

Ensure the program-office model is the right fit. AnyTech's architecture (8-person team, MSSP SOC/IR, MSP IT, no CISO) is what drove this adaptation. If any of these elements change, re-evaluate.

### Step 2 — Assign Pillar Leaders

Identify which of the 8 people own Engineering, Risk, and Governance. See §5 for consolidation guidance.

### Step 3 — Map Provider Boundaries

Document what each provider does and where CERG oversight begins and ends. See §6.

### Step 4 — Seed the Risk Register

Create the first 10 risk register entries using [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) and [TMPL-RM-001](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting_AnyTech.md).

### Step 5 — Establish Evidence Collection Cadence

Set up recurring evidence collection from MSSP (monthly SLA report) and MSP (monthly patch report, quarterly access reviews).

### Step 6 — Schedule First Reviews

- Weekly CERG standup
- Monthly risk review with IT Director
- Quarterly provider business review
- Annual policy review

---

## 4. Document Adopted vs. Deferred

### Adopted: 10 Documents

All adopted documents are in `examples/anytech-profile/` and are listed in [CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) §3.

### Deferred: Everything Else

The full CERG corpus contains 135+ documents covering enterprise-scale security functions, regulatory packages, workforce planning, technical standards, and advanced artifacts. These are explicitly deferred with rationale in [CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) §4.

**If a critical need arises for a deferred document** (e.g., an unexpected compliance requirement), adopt it as an incremental addition rather than reopening the full library. The upstream CERG corpus remains available as the authoritative source.

---

## 5. Role Consolidation for AnyTech

An 8-person team covers the three pillar functions by consolidating responsibilities. The canonical CERG role roster describes 27 roles. AnyTech covers them with 8 people.

### 5.1 Recommended Role Map

| Person | Primary Pillar | Consolidated Roles |
|--------|---------------|-------------------|
| **Person 1** | Engineering | Engineering Pillar Leader, Cloud Security, AppSec, Pre-production Reviewer |
| **Person 2** | Engineering | Identity, Endpoint, MSP technical liaison |
| **Person 3** | Engineering | Engineering support, asset register, change reviewer |
| **Person 4** | Risk | Risk Pillar Leader, Exposure Management Lead, MSSP liaison |
| **Person 5** | Risk | Risk Analyst, Threat Intel Consumer, Vendor Risk |
| **Person 6** | Risk | Risk Analyst, Exception Coordinator, Evidence Collector |
| **Person 7** | Governance | Governance Pillar Leader, Policy Manager, SLA Tracker |
| **Person 8** | Governance | Evidence Librarian, Document Control, Training Coordinator |

### 5.2 Authority Guardrail

Heads collapse; business consequence acceptance does not. A small team still needs a Business Owner outside CERG (the IT Director) to acknowledge accepted residual risk. See [PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process_AnyTech.md) §8 for approval authorities.

---

## 6. Provider Integration Points

| Provider | Interface | Cadence | CERG Point of Contact |
|----------|-----------|---------|----------------------|
| **MSSP** | Monthly SLA report, SIEM health, threat intel feed | Monthly | Risk Pillar Leader |
| **MSSP** | Quarterly business review, IR tabletop | Quarterly | Engineering + Risk Pillar Leaders |
| **MSSP** | SOC 2 report, pentest results | Annual | Governance Pillar Leader |
| **MSP** | Patch compliance, vulnerability scan exports | Monthly | Engineering Pillar Leader |
| **MSP** | Access review evidence, change log | Quarterly | Engineering Pillar Leader |
| **MSP** | Asset inventory verification | Quarterly | Engineering Pillar Leader |
| **Training vendor** | Training completion rates, phishing click rates | Monthly | Governance Pillar Leader |
| **Training vendor** | Annual content review | Annual | Governance Pillar Leader |

---

## 7. Key Deployment Decisions

These decisions must be made within the first week of adoption. Document each in the decision log.

| Decision | Options | Recommended for AnyTech |
|----------|---------|------------------------|
| Risk register format | Spreadsheet / Lightweight GRC | Spreadsheet for first 3 months |
| Evidence storage | Shared drive / Cloud storage | SharePoint or equivalent (accessible to all 8) |
| Monthly risk review format | Email brief / Slide deck / Meeting | 1-page email brief + 30-min meeting |
| SLA tracking tool | Spreadsheet / Vendor portal / TPRM tool | Spreadsheet for first 3 months |
| Incident notification path | Email / SMS / Chat app | Email + SMS for critical alerts to all 8 team members |
| Document repository | Git-based / Wiki / Shared drive | Git (with the CERG repo) |

---

## 8. First 30-Day Checklist

### Week 1
- [ ] IT Director confirms authority and risk appetite
- [ ] Three pillar leaders assigned
- [ ] Provider scope boundaries documented
- [ ] Decision log created

### Week 2
- [ ] Risk register seeded with top 10 risks
- [ ] First MSSP monthly report requested
- [ ] First MSP patch report requested
- [ ] Evidence library structure created

### Week 3
- [ ] First exception processed (if applicable)
- [ ] Provider SLA scorecard template created
- [ ] First exposure backlog item created
- [ ] CERG weekly standup cadence established

### Week 4
- [ ] First monthly risk review held with IT Director
- [ ] First 30-day improvement backlog created (5 items)
- [ ] Provider interface points confirmed
- [ ] Adoption status documented in CAT-001

---

## 9. Document Control

### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 1.0 (AnyTech Adaptation) | 2026-06-21 | Governance Pillar Leader | AnyTech adaptation. Program-office model, provider integration, 10-doc adoption. |

### Review Triggers

- Change in AnyTech role assignments
- Provider change (new MSSP, new MSP)
- Change to the token profile
- Annual review cycle

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Organization Adaptation Profile | CERG-GOV-VAR-001 | Token scheme reference |
| AnyTech CERG Lite adoption pack | ../../adoption-packs/anytech-lite/README.md | Companion guide |
| Document Catalog | [CAT-001](CERG-GOV-CAT-001_Document_Catalog_AnyTech.md) | Full document inventory |
| Operating Model | [OM-001](CERG-GOV-OM-001_Operating_Model_AnyTech.md) | Operating description |
