
# SURGE — Cyber Engineering, Risk & Governance

## DOCUMENT CATALOG AND NAMING CONVENTION
### Authoritative Inventory · ID Scheme · Roadmap

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.0 |
| **Status** | Approved (V1) |
| **Classification** | Internal — Confidential |
| **Owner** | Cyber Governance Manager (Document Control) |
| **Parent Policy** | CERG-POL-001 — Cybersecurity Policy |
| **Review Cycle** | Quarterly — or upon any artifact add/retire |
| **Frameworks** | NIST CSF 2.0 (GOVERN) · ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Naming Convention](#2-naming-convention)
3. [Document Types](#3-document-types)
4. [Authority and Status Lifecycle](#4-authority-and-status-lifecycle)
5. [Authoritative Catalog (V1)](#5-authoritative-catalog-v1)
6. [Cross-Reference Rules](#6-cross-reference-rules)
7. [Artifact Roadmap (V1.x → V2)](#7-artifact-roadmap-v1x--v2)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG-POL-001 establishes a hierarchy of policy, standards, procedures, and guidelines. As the library grows, that hierarchy is only useful if there is a single, authoritative inventory of which artifacts exist, which are planned, which are authoritative, and which are exports of an authoritative artifact for a specific audience. This document is that inventory.

It applies to every CERG-owned artifact — policy, standard, procedure, plan, guideline, template, and operational package — regardless of medium (Markdown source, exported Word/PDF, intranet page, or third-party portal entry).

> **One Source, Many Exports**
>
> The authoritative source for every CERG document is the Markdown file in the CERG content repository. Everything else — Word exports, PDF deliverables, intranet pages, regulator portal uploads — is an export. Exports inherit the ID and version of the source. If the source and an export disagree, the source wins.

---

## 2. Naming Convention

Every CERG artifact has a Document ID of the form:

```
CERG-<TYPE>-<DOMAIN>-<NNN>
```

Where:

| **Element** | **Meaning** | **Examples** |
|---|---|---|
| `CERG` | Program prefix; never changes | — |
| `<TYPE>` | Document type — see Section 3 | `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV` |
| `<DOMAIN>` | Two-to-four-letter domain code | `IT`, `OT`, `CUI`, `AC`, `RM`, `VM`, `CIP`, `LM` |
| `<NNN>` | Three-digit sequence within type+domain | `001`, `002` |

Files are named `<DocumentID>_<Short_Title>.md` using underscore-separated title case (e.g., `CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`).

> **Convention, Not Bureaucracy**
>
> The ID format exists so that a person reading a control reference can tell at a glance what kind of artifact they're being pointed at. A reader who sees `CERG-STD-OT-001` knows it's a standard; a reader who sees `CERG-PRC-VM-001` knows it's a procedure they can execute. Anything that obscures that signal — clever domain codes, free-form titles in the ID — is a mistake.

### 2.1 Domain Codes (V1)

| **Code** | **Domain** |
|---|---|
| `IT` | IT / cloud / SaaS |
| `OT` | Operational technology / grid control systems |
| `CUI` | Controlled Unclassified Information / CMMC |
| `AC` | Access management / identity |
| `VM` | Vulnerability management |
| `RM` | Risk management (register, exceptions, scoring) |
| `IR` | Incident response (CERG-facing artifacts only) |
| `CIP` | NERC-CIP |
| `SOX` | Sarbanes-Oxley ITGC |
| `LM` | Logging, monitoring, detection |
| `CFG` | Secure configuration / hardening |
| `RES` | Cyber resilience and backup |
| `CR` | Cryptography and key management |
| `AR` | Architecture review / project intake |
| `TPRM` | Third-party / supply chain risk |
| `AV` | Adversarial validation |
| `MTR` | Metrics and reporting |
| `OM` | Operating model |
| `CAT` | Catalog / inventory |
| `CB` | Control baseline |

New domains are added only by amendment to this catalog.

---

## 3. Document Types

| **Type Code** | **Type** | **Authority** | **What It Looks Like** |
|---|---|---|---|
| `POL` | Policy | CISO / Executive | Durable principles. Short. Rarely changes. One per program. |
| `STD` | Standard | Cyber Governance Manager | Specific, measurable, technology-aware requirements that implement policy principles. |
| `PRC` | Procedure | Pillar Owner | Step-by-step "how" — workflow, owner, evidence, frequency. |
| `PLN` | Plan / Operational Package | Pillar Owner | Bundled procedure + templates + checklists for a regulated or assessor-facing program (e.g., CIP, CUI, SOX). |
| `GL` | Guideline | Pillar Owner | Recommendations and good practice, not mandatory. |
| `TMPL` | Template | Pillar Owner | A blank artifact to be filled in (intake form, exception request, SSP). |
| `GOV` | Governance Instrument | Cyber Governance Manager | Cross-cutting instruments that aren't a single policy/standard/procedure — catalogs, control baselines, operating model, metrics dictionary. |

> **PLN vs. PRC**
>
> A `PRC` is a single procedure. A `PLN` is an operational package that bundles a procedure with templates, checklists, and registers because the regulator or auditor expects to see the bundle together (NERC-CIP, CUI/CMMC, SOX). When in doubt, prefer `PRC` and add templates as appendices.

---

## 4. Authority and Status Lifecycle

| **Status** | **Meaning** | **In Catalog?** |
|---|---|---|
| `Planned` | Artifact has an ID and an owner but no draft yet. | Yes — Section 7. |
| `Draft` | Work in progress. Not authoritative. | Yes — Section 5, flagged. |
| `For Review` | Out for stakeholder/CISO review. | Yes — Section 5. |
| `Approved` | Signed off and authoritative. | Yes — Section 5. |
| `Retired` | Replaced or no longer in force. Retained for audit. | Yes — appendix to Section 5. |

Approval authority follows CERG-POL-001 Section 7:

- Policy (`POL`) — CISO approves; Executive leadership endorses.
- Standard (`STD`) — Cyber Governance Manager approves; CISO endorses.
- Procedure / Plan / Guideline (`PRC`, `PLN`, `GL`) — Pillar Owner approves; Cyber Governance Manager endorses.
- Template (`TMPL`) — Pillar Owner approves.
- Governance instrument (`GOV`) — Cyber Governance Manager approves.

---

## 5. Authoritative Catalog (V1)

The V1 library is the set below. Every artifact listed has either an approved or for-review source in the CERG content repository.

### 5.1 Policy

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-POL-001` | Cybersecurity Policy | CISO | For Review |

### 5.2 Framework, Operating Model, and Cross-Cutting Instruments

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-GOV-OM-001` | CERG Operating Model | CISO / Pillar Owners | For Review |
| `CERG-GOV-CAT-001` | Document Catalog and Naming Convention | Cyber Governance Manager | Approved (this doc) |
| `CERG-GOV-CB-001` | Unified Control Baseline | Cyber Governance Manager | For Review |
| `CERG-GOV-MTR-001` | Metrics, Dashboard, and CISO/Board Reporting | Cyber Governance Manager | For Review |
| `CERG Framework` | Surge / CERG Framework (narrative) | CISO | For Review |
| `CERG Risk Taxonomy` | Risk Taxonomy | Cyber Risk | For Review |
| `CERG Compliance Matrix` | Compliance Matrix | Cyber Governance Manager | For Review |
| `CERG Risk Management Framework v1.0` | Risk Management Framework | Cyber Governance Manager | For Review |

### 5.3 Standards

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-STD-IT-001` | IT / Cloud / SaaS Security Standard | Cyber Governance — IT/Cloud | For Review |
| `CERG-STD-OT-001` | Grid Control Systems Security Standard | Cyber Governance — OT | For Review |
| `CERG-STD-CUI-001` | CUI Handling Standard | Cyber Governance — CUI/CMMC | For Review |
| `CERG-STD-AC-001` | Access Management Standard | Cyber Governance — Identity | For Review |
| `CERG-STD-CFG-001` | Secure Configuration Baseline Standard (DISH) | Cyber Engineering — Platforms | For Review |
| `CERG-STD-LM-001` | Logging, Monitoring, and Detection Standard | Cyber Risk — Detection | For Review |
| `CERG-STD-RES-001` | Cyber Resilience and Backup Standard | Cyber Engineering — Resilience | For Review |
| `CERG-STD-CR-001` | Cryptography and Key Management Standard | Cyber Engineering — Platforms | For Review |

### 5.4 Procedures

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-PRC-VM-001` | Vulnerability Management Procedure | Cyber Risk | For Review |
| `CERG-PRC-RM-001` | Risk Register and Exception Process | Cyber Governance — Risk Register | For Review |
| `CERG-PRC-AR-001` | Architecture Review and Project Intake Procedure | Cyber Engineering | For Review |
| `CERG-PRC-AC-002` | Access Management Runbook | Cyber Engineering — Identity (or IAM team if external) | For Review |
| `CERG-PRC-TPRM-001` | Third-Party and Supply Chain Risk Procedure | Cyber Risk — Vendor Risk | For Review |
| `CERG-PRC-AV-001` | Adversarial Validation Procedure | Cyber Risk — Offensive Security | For Review |

### 5.5 Plans / Operational Packages

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-PLN-IR-001` | Incident Response Plan (CERG interface) | Incident Response / CERG liaison | For Review |
| `CERG-PLN-CUI-001` | CUI / CMMC Operational Package | Cyber Governance — CUI/CMMC | For Review |
| `CERG-PLN-CIP-001` | NERC-CIP Operational Package | Cyber Governance — OT | For Review |
| `CERG-PLN-SOX-001` | SOX ITGC Operational Package | Cyber Governance — SOX | For Review |

### 5.6 Templates

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-TMPL-RM-001` | Risk Register Templates and Reporting | Cyber Governance — Risk Register | For Review |

Other templates are embedded as appendices of their parent procedure or plan unless they have independent reuse outside that artifact. The Document Catalog references the parent. V2 may promote heavy-use templates to standalone `TMPL` artifacts.

---

## 6. Cross-Reference Rules

These rules govern every "Related Documents" table, every footnote reference, and every link in a CERG artifact.

1. **Link only to artifacts that appear in this catalog.** If the artifact does not appear in Section 5 or Section 7, do not reference it.
2. **Distinguish approved from planned.** When a Related Documents table includes a Planned artifact, mark it `(Planned — V1.x)` or `(Planned — V2)` so the reader knows it does not yet exist.
3. **Use the Document ID, not the file name.** File names change; IDs do not.
4. **Avoid forward references to TMPL artifacts that live inside a parent.** Cite the parent and the appendix (`CERG-PRC-AR-001 Appendix B — Security Project Intake Form`).
5. **External standards (NIST, CIS, IEC, ISO) are cited by short form** — `NIST 800-53r5 AC-2`, `CIS Benchmark Windows Server 2022 L1`, `IEC 62443-3-3 SR 1.1`. Each artifact's metadata table lists the framework set in scope.

> **The Reference Discipline Test**
>
> A new CERG team member opens a standard, follows every "Related Documents" link, and ends up at real, current artifacts — never a 404, never a "TBD." If that test fails for any document in the library, the document fails review.

---

## 7. Artifact Roadmap (V1.x → V2)

The V1 catalog above closes every gap identified in the V1 review. The roadmap below tracks artifacts that were considered, deferred, or queued for promotion in subsequent versions.

### 7.1 Deferred to V1.x (Within 6 Months)

| **ID** | **Title** | **Owner** | **Why Deferred** |
|---|---|---|---|
| `CERG-TMPL-CIP-001` | CIP Deviation and Mitigation Plan Template | Cyber Governance — OT | Currently embedded in CERG-PLN-CIP-001 §9. Promote to standalone TMPL once first deviation is processed end-to-end. |
| `CERG-GL-OT-001` | IT/OT Convergence Security Architecture Guideline | Cyber Engineering — OT | Embedded as CERG-PLN-CIP-001 §10 for V1; promote once architecture patterns stabilize. |
| `CERG-GL-AV-001` | OT Adversarial Assessment Safety Guide | Cyber Risk — Offensive Security | Embedded in CERG-PRC-AV-001 §9; promote once first OT engagement is complete. |

### 7.2 Queued for V2 (Within 12–18 Months)

| **Candidate** | **Trigger to Pull Forward** |
|---|---|
| Cloud-specific landing zone baselines per provider (AWS / Azure / GCP) | First production deployment of provider; current DISH profile in CERG-STD-CFG-001 covers control plane and Tier 1 SaaS at the standard level. |
| Application Security Standard (AppSec / SDLC) | When in-house development volume exceeds the carve-out threshold defined in CERG-PRC-AR-001. |
| Data Classification and Handling Standard | When the enterprise data classification scheme is ratified by Legal/Privacy; the CUI standard and crypto standard reference it today. |
| Privacy / PII Standard (where regulation requires) | When jurisdictional triggers (e.g., new state privacy law applicable to the organization) appear. |

### 7.3 Retired

None in V1.

---

## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.0 |
| **Approved By** | Cyber Governance Manager |
| **Next Review** | Quarterly — Catalog freshness, ID conflicts, status changes |
| **Change Log** | 1.0 — Initial publication. Establishes ID convention, baseline catalog, and roadmap. |

              