# CERG Roadmap

**Where CERG is headed, what's needed, and where contributions help most.**

This is a living document. Items move from "Exploring" to "In Progress" to "Done" as work completes. If something interests you, open an issue and say so.

---

## Adoption and onboarding

### Done
- [x] Three adoption paths (Lite / Standard / Regulated) in README
- [x] START-HERE.md first-48-hours guide
- [x] Small team adoption path (IMP-003) with spreadsheet schemas and role consolidation
- [x] Implementation and adaptation guide (IMP-001)
- [x] Adoption safety guide (IMP-002) — anti-patterns, tailoring boundaries, regulatory honesty
- [x] Organization adaptation profile template (VAR-001)
- [x] Framework system map (FRM-002) for document and operating-loop navigation
- [x] Adoption decision tree and dependency matrix (IMP-005)
- [x] Role-based implementation checklists (IMP-006)
- [x] Record catalog and minimum viable evidence library (CAT-002)
- [x] Five example organization profiles in `/examples/`
- [x] Contributing guide, issue templates, code of conduct

### In progress
- [ ] CONTRIBUTING.md mentioned in README contributor section ### Exploring
- [ ] Interactive adoption checklist (self-assessment before starting)
- [ ] CERG-to-ISO 27001 accelerator (mapping + readiness path for organizations pursuing certification)
- [ ] CERG-to-sMB packaged overlay (pre-configured lightweight profile for organizations under 50 people)

---

## Framework completeness

### Done
- [x] Three-pillar operating model (Engineering / Risk / Governance)
- [x] 11 core capabilities that survive reorgs (OM-001 §6.0)
- [x] 27 canonical roles across 5 job families
- [x] Competency model with behavioral anchors (CMP-001)
- [x] Performance management and promotion framework (PERF-001)
- [x] Maturity self-assessment and scorecard (MAT-001) — 25 domains
- [x] Control effectiveness framework (CEF-001) — implementation vs. effectiveness distinction
- [x] Metrics dashboard and CISO/Board reporting (MTR-001) with anti-vanity guardrails
- [x] Edge register — six organizational edge types (EDG-001)
- [x] Crown jewel register and loss scenario library (CJ-001)
- [x] CERG service-level commitments — reciprocal responsiveness (SLC-001)
- [x] Cross-pillar operational flows (FLOW-001) — 7 flows, each with required inputs and closure criteria

### In progress
- [ ] Wire CEF effectiveness signals into RMF as automatic re-score triggers (currently only event-driven triggers exist)
- [ ] Assume-breach as an explicit design principle in POL-001 / FRM-001 (currently implicit in blast-radius and detection-coverage patterns)
- [ ] Threat-informed detection gap closure loop: TI-001 intel priorities drive LM-001 ATT&CK coverage priorities, validated by PRC-AV-001 purple team, feeding DT coverage metric

### Exploring
- [ ] Automated evidence collection hooks (reduce manual evidence generation burden)
- [ ] Continuous control monitoring (CCM) integration patterns
- [ ] Third-party risk exchange (shared vendor assessment data with peer organizations)

---

## Controls and risk

### Done
- [x] Unified control baseline (CB-001) — 19 NIST families, 6 implementation statuses, 5 overlays
- [x] Inheritance evidence package (CB-001 §5) — 6-element proof for any "we inherit from cloud provider" claim
- [x] Risk management framework (RMF-001) — 6-phase NIST RMF with event-driven re-score triggers
- [x] Risk taxonomy (TAX-001) — 12 risk themes mapped to pillars
- [x] Compliance matrix (CMX-001) — 22 unified intents mapped to every framework simultaneously

### Exploring
- [ ] Quantitative risk analysis templates (loss-exposure scenarios, not just 5x5 heat maps)
- [ ] Supply chain concentration heat map (visualizing vendor and sub-processor dependency risk)
- [ ] Crown jewel scenario library expansion (currently 10 scenarios; sector-specific libraries welcome)

---

## Governance and compliance

### Done
- [x] Compliance matrix (CMX-001) — single baseline, many audiences
- [x] Evidence quality standard (AUD-001) — what admissible evidence looks like
- [x] Annual security and governance calendar (CAL-001) — consolidated cadence instrument
- [x] Training, development, and certification framework (TRN-001)
- [x] Onboarding and integration program (ONB-001)
- [x] Succession planning and talent review framework (SUCC-001)

### Exploring
- [ ] Regulatory change monitoring workflow (automated watch + impact assessment trigger)
- [ ] Cross-framework control mapping update mechanism (when NIST 800-53 rev 6 or CMMC 3.0 arrives)
- [ ] Board reporting narrative generator (draft board deck language from KRI data)

---

## Community and tooling

### Done
- [x] Automated CI validation (cerg-validate.py — links, catalog, metadata, cross-references)
- [x] Machine-readable artifact suite (YAML manifests, requirements, flow specs, schemas)
- [x] LLM corpus (llms.txt and llms-full.txt) for AI tool ingestion
- [x] GitHub issue templates (improvement, new document, validation error)
- [x] Contributing guide with document conventions and review process

### Exploring
- [ ] Pre-commit hooks for common editing mistakes (em dashes, bare `**Version**` matches)
- [ ] Automated stale-review detection (flag documents past their review date)
- [ ] Contribution dashboard (visualize what's changed, what's stale, what needs help)

---

## How to contribute to roadmap items

1. Open an issue referencing the roadmap item (or propose a new one).
2. For new documents: follow the [new document proposal](.github/ISSUE_TEMPLATE/new-document-proposal.md) template.
3. For improvements to existing documents: follow the [document improvement](.github/ISSUE_TEMPLATE/document-improvement.md) template.
4. Make sure `python3 tools/cerg-validate.py` passes with 0 errors before submitting a PR.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.
