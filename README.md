# CERG (surge) · Cybersecurity Operating Model

**A spine, not shelfware.**

CERG gives security teams the policies, standards, procedures, roles, records, and evidence model needed to run a cybersecurity program. It is not a control framework, certification scheme, or compliance checklist. Compliance alignment is a byproduct of operating well.

CERG is built around three accountable pillars:

- **Cyber Engineering** builds security in early.
- **Cyber Risk** understands exposure and drives treatment.
- **Cyber Governance** sets clear rules, records decisions, and keeps evidence usable.

---

## Start here

| If you are... | Start with |
|---|---|
| New to CERG | [START-HERE.md](START-HERE.md) |
| New to GitHub or Markdown | [BEGINNER-GUIDE.md](BEGINNER-GUIDE.md) |
| Using an AI assistant or coding agent | [ADOPT-WITH-AN-AGENT.md](ADOPT-WITH-AN-AGENT.md) |
| A small team adopting the minimum spine | [CERG Lite adoption pack](adoption-packs/cerg-lite/README.md) |
| Looking for operational examples | [Day in the Life examples](examples/day-in-the-life/README.md) |
| Comparing adoption paths | [Adoption Decision Tree](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## Adoption modes

You do not adopt the full library in week one.

- **CERG Lite**: minimum viable program for a small or early security function.
- **CERG Standard**: core operating model for an established security team.
- **CERG Regulated**: Standard plus overlays for CMMC, NERC-CIP, SOX, ISO 27001, privacy, OT, or other regulated scope.

The minimum viable CERG spine is eight documents: Policy, Framework, Operating Model, Document Catalog, Risk Management Framework, Risk Register Procedure, Risk Register Templates, and Exposure Management Procedure.

---

## What is in the repo

- `governance/`: policy, operating model, catalogs, risk framework, RACI, metrics, maturity, workforce governance.
- `standards/`: technical standards for access, asset, cloud/SaaS, logging, resilience, AI, OT, secure development, and related domains.
- `procedures/`: operational workflows for risk, exposure, architecture review, TPRM, audit/evidence, change, threat modeling, and more.
- `plans/`: regulated and operational packages such as CMMC/CUI, NERC-CIP, SOX, ISO 27001, privacy, BCDR, and IR interface.
- `templates/`: practical forms and registers.
- `roles/`: workforce architecture and job descriptions.
- `machine-readable/`: indexes, manifests, schemas, flow models, and agent-friendly metadata.
- `examples/`: adoption examples and day-in-the-life walkthroughs.

The authoritative inventory is the [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md).

---

## LLM and automation use

Use these entry points before loading the full corpus:

- [`machine-readable/cerg-llm-index.json`](machine-readable/cerg-llm-index.json): complete local corpus map.
- [`machine-readable/cerg-document-tiers.yaml`](machine-readable/cerg-document-tiers.yaml): adoption tiers and recommended loading order.
- [`llms.txt`](https://cerg.nexus/llms.txt): public LLM index.
- [`llms-full.txt`](https://cerg.nexus/llms-full.txt): full public corpus mirror.

The GitHub repository is authoritative. The website is a convenience mirror and may lag the repo.

---

## When CERG is not a good fit

Do not adopt CERG yet if there is no named security owner, no executive support for guardrails and evidence, unclear scope, or no willingness to track decisions and exceptions. Start lighter with NIST CSF or CIS Controls, then return when ownership and evidence discipline exist.

CERG does not determine legal obligations or certification readiness. Validate regulatory applicability with qualified counsel, compliance leadership, and assessors.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Fork freely, adapt openly, attribute generously.
