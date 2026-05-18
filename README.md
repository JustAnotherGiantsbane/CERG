# CERG — Cyber Engineering, Risk & Governance

**One cybersecurity baseline. Many regulators.**

CERG is an open-source governance framework that unifies NIST 800-53, NIST CSF 2.0, NIST 800-171, NERC-CIP, CMMC L2, and SOX ITGC into a single implementation-ready control program. Built once, evidenced once — mapped to every regulator that matters.

→ **[cerg.nexus](https://cerg.nexus)** — control explorer, document catalog, and full rendered docs.

---

## The problem CERG solves

Most security programs maintain a separate control library per regulator — one for NIST, one for CMMC, one for NERC-CIP, one for SOX — then spend every audit cycle reconciling them. CERG inverts that model: one baseline, implemented once, evidenced once. Crosswalks translate the same evidence into the language each regulator expects.

---

## Three pillars. One accountability model.

Ambiguous ownership is the root cause of most control failures. CERG assigns every control to exactly one pillar:

| Pillar | Owns |
|---|---|
| **Cyber Engineering** | Builds and operates controls — identity, access, hardening, encryption, segmentation, configuration management, recovery infrastructure |
| **Cyber Risk** | Finds and validates — vulnerability management, threat monitoring, adversarial testing, third-party risk, supply chain integrity |
| **Cyber Governance** | Defines and proves — policy, standards, evidence, risk register, IR planning, compliance calendar |

Together the three pillars are pronounced **SURGE** — a deliberately operational posture, not a compliance checkbox.

---

## What's in the repo

| ID | Document | Description |
|---|---|---|
| CERG-POL-001 | [Cybersecurity Policy](CERG%20-%20Cybersecurity%20Policy.md) | Durable principles anchoring every standard and procedure |
| CERG-GOV-FRM-001 | [CERG Framework](CERG%20Framework%20-%20Cyber%20Engineering%20Risk%20and%20Governance.md) | Design philosophy, the three-pillar model, and how the pieces fit |
| CERG-GOV-CB-001 | [Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md) | The control set auditors and C3PAOs open first — NIST spine, named evidence, overlays |
| CERG-GOV-CMX-001 | [Compliance Matrix](CERG%20Compliance%20Matrix.md) | 22 security intents mapped row-by-row to NIST, NERC-CIP, CMMC, and SOX |
| CERG-GOV-TAX-001 | [Risk Taxonomy](CERG%20Risk%20Taxonomy.md) | Threat reasoning behind each control and what failure mode it prevents |
| CERG-GOV-OM-001 | [Operating Model](CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar charters, interfaces, and the CERG governance cadence |
| CERG-GOV-MTR-001 | [Metrics & Reporting](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | CISO and board-level metrics dashboard |
| CERG-GOV-CAT-001 | [Document Catalog](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | ID scheme, naming convention, and authoritative artifact inventory |
| CERG-RMF-001 | [Risk Management Framework](CERG_Risk_Management_Framework_v1.0.md) | Risk identification, scoring, treatment, and lifecycle tracking |
| CERG-STD-AC-001 | [Access Management Standard](CERG-STD-AC-001_Access_Management_Standard.md) | |
| CERG-STD-CFG-001 | [Secure Configuration Baseline](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | |
| CERG-STD-CR-001 | [Cryptography & Key Management](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | |
| CERG-STD-CUI-001 | [CUI Handling Standard](CERG-STD-CUI-001_CUI_Handling_Standard.md) | |
| CERG-STD-IT-001 | [IT / Cloud / SaaS Security](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | |
| CERG-STD-LM-001 | [Logging, Monitoring & Detection](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | |
| CERG-STD-OT-001 | [Grid Control Systems Security](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | |
| CERG-STD-RES-001 | [Cyber Resilience & Backup](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | |
| CERG-PRC-AC-002 | [Access Management Runbook](CERG-PRC-AC-002_Access_Management_Runbook.md) | |
| CERG-PRC-AR-001 | [Architecture Review & Project Intake](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | |
| CERG-PRC-AV-001 | [Adversarial Validation Procedure](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | |
| CERG-PRC-RM-001 | [Risk Register & Exception Process](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | |
| CERG-PRC-TPRM-001 | [Third-Party & Supply Chain Risk](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | |
| CERG-PRC-VM-001 | [Vulnerability Management Procedure](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) | |
| CERG-PLN-CIP-001 | [NERC-CIP Operational Package](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | BES Cyber Systems: categorization, ESP/EAP, CIP-007/010/013, CIP-008/009 |
| CERG-PLN-CUI-001 | [CUI / CMMC Operational Package](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | SSP, POA&M, SPRS, FIPS crypto, DFARS flow-down, CMMC L2 readiness |
| CERG-PLN-SOX-001 | [SOX ITGC Operational Package](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | Access, change, operations, backup, interface, and report ITGCs |
| CERG-PLN-IR-001 | [Incident Response Plan](CERG-PLN-IR-001_Incident_Response_Plan.md) | Roles, escalation, regulatory notification timelines, tabletop cadence |
| CERG-TMPL-RM-001 | [Risk Register Templates](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Canonical templates for risk register entries and reporting |

---

## By the numbers

| | |
|---|---|
| **28** | Source documents |
| **22** | Unified control areas |
| **6** | Regulatory frameworks unified |
| **3** | Accountability pillars |

---

## For LLMs and automation

Every document is authored in Markdown. The full corpus is also available at [cerg.nexus](https://cerg.nexus):

- **[/llms.txt](https://cerg.nexus/llms.txt)** — index of every document with stable URLs, designed for AI tools and crawlers
- **[/llms-full.txt](https://cerg.nexus/llms-full.txt)** — full concatenated corpus in one file
- **[Bulk download](https://cerg.nexus/downloads/cerg-docs.zip)** — all 28 documents as a single ZIP

Fork it, adapt it, feed it to your tools.

---

## License

Documentation licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Fork freely. Attribute generously.
