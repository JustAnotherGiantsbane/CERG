# CERG Machine-Readable Artifacts

This directory contains machine-readable YAML specifications generated from the CERG corpus. These files are designed for consumption by LLMs, automation tools, and programmatic validation.

## File Inventory

| File | Purpose | Source |
|------|---------|--------|
| `cerg-manifest.yaml` | Canonical manifest of all 71 CERG artifacts with metadata, hashes, and LLM consumption flags | CAT-001 §5 |
| `cerg-publication-manifest.yaml` | Publication eligibility for each artifact — separates "approved" from "safe to publish" | Document metadata |
| `cerg-content-tags.yaml` | Content type tags for every section heading in the corpus | All CERG documents |
| `cerg-requirements.yaml` | Atomic requirements extracted from 8 spine documents (pilot) | POL-001, STD-AC/IT/LM/RES/CR, CB-001, RMF-001 |
| `cerg-flows.yaml` | Cross-pillar operational flow specifications (7 flows) | FLOW-001 |
| `cerg-record-schemas.yaml` | Record template schemas (5 record types) | FLOW-001 §16 |
| `cerg-runtime-model.yaml` | Core operational objects and their relationships | CERG-ACT-006 |
| `cerg-control-evidence-map.yaml` | Control-to-evidence traceability | CB-001 |
| `cerg-evidence-schema.yaml` | Evidence lifecycle and object schema | CERG-ACT-008 |
| `cerg-metrics-model.yaml` | Decision-grade metrics model and CISO dashboard sections | MTR-001, CERG-ACT-009 |
| `cerg-crown-jewel-schema.yaml` | Crown Jewel register schema and criticality tiers | CERG-ACT-010 |
| `cerg-vulnerability-priority-model.yaml` | Risk-weighted vulnerability prioritization model | CERG-ACT-011 |
| `cerg-control-test-plan.yaml` | Control efficacy test plan schema | CERG-ACT-012 |
| `cerg-ir-interface.yaml` | CERG-to-IR interface contract | CERG-ACT-013 |
| `cerg-vendor-kill-switch.yaml` | Vendor access disablement procedure schema | CERG-ACT-014 |
| `cerg-tier-0-identity-profile.yaml` | Tier 0 identity controls for Crown Jewel systems | CERG-ACT-015 |
| `cerg-segmentation-schema.yaml` | Network segmentation verification schema | CERG-ACT-016 |
| `cerg-ai-system-intake.yaml` | AI/ML system security intake schema | CERG-ACT-017 |
| `cerg-workforce-capacity-model.yaml` | Workforce capacity model schema | CERG-ACT-018 |
| `cerg-decision-log.yaml` | Governance decision log schema | CERG-ACT-019 |

## How These Are Generated

All files are generated from the CERG markdown corpus during the build process. The manifest and content tags are regenerated on every catalog change. The requirement register is regenerated when normative documents change. Schema files are maintained alongside the documents they describe.

## For LLM Consumers

Start with `cerg-manifest.yaml` to understand what artifacts exist and which are safe to include. Then load `cerg-content-tags.yaml` to understand what each section contains. Use `cerg-requirements.yaml` for traceable obligations. Use the individual schema files for structured field definitions.
