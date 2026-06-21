# AnyTech CERG Lite — Adoption Pack

## Who This Is For

This adoption pack is for **AnyTech** — an 8-person cybersecurity team operating as a
**cyber program office** that oversees a federation of providers rather than running
security operations directly.

### AnyTech's Architecture

- **MSSP** handles all SOC/IR functions (US + India offices)
- **MSP** handles all IT operations
- **3rd-party vendor** handles awareness training and phishing simulations
- **No CISO** — Cyber Engineering, Risk, and Governance pillar leaders report to the
  **IT Director**, who carries executive risk acceptance authority
- The 8-person CERG team owns **policy, risk decisions, vendor oversight, exposure
  visibility, and architecture direction**

### When This Pack Fits

Use this pack if your team looks like AnyTech:

- Your security team is small (3-12 people)
- SOC/IR is fully outsourced to an MSSP
- IT operations are fully or largely outsourced to an MSP
- Training/awareness is handled by a third-party provider
- The senior-most security leader reports through IT, not as a C-level executive
- Your team's core competency is **vendor oversight and risk ownership**, not
  hands-on security operations

## What's Included (10 Adapted Documents)

| # | Doc ID | Title | Adapts |
|---|--------|-------|--------|
| 1 | POL-001 | Cybersecurity Policy | IT Director sign-off, stripped to 6 vendor-relevant principles |
| 2 | FRM-001 | CERG Framework | Three pillars reframed for vendor-oversight model |
| 3 | OM-001 | Operating Model | **Full rewrite** — program office, MSSP/MSP as delivery partners |
| 4 | CAT-001 | Document Catalog | Adopted those 10; everything else deferred |
| 5 | RMF-001 | Risk Management Framework | IT Director as acceptance authority, no regulatory packages |
| 6 | PRC-RM-001 | Risk Register + Exception Process | IT Director approval path |
| 7 | TMPL-RM-001 | Risk Register Templates | Cleaned references |
| 8 | PRC-TPRM-001 | Third-Party Risk | **Heavily stripped** — MSSP+MSP core only |
| 9 | PRC-VM-001 | Exposure Management | Oversight model — cyber team tracks, MSP patches |
| 10 | IMP-001 | Implementation Guide | References AnyTech profile |

## What We Cut (50+ Docs, All Deferred)

Job descriptions, workforce planning, succession planning, performance management,
training/competency development (3rd-party owned), incident response plans/playbooks
(MSSP owned), all 15 technical standards (MSP/MSSP bring their own), all 7 regulatory
packages (not in scope), board/CISO reporting decks, maturity self-assessment,
contractor integration guide, stakeholder surveys, most templates, day-in-the-life
stories, machine-readable schemas, the regulated utility example — the entire corpus
except the 10 docs above.

## First 48 Hours for AnyTech

1. Confirm IT Director as executive risk acceptance authority
2. Assign 8 people to Engineering (3), Risk (3), Governance (2)
3. Map MSSP scope — which systems/environments they cover
4. Map MSP scope — which IT functions they deliver
5. Define the escalation path: CERG → MSSP for IR, CERG → MSP for IT issues
6. Fill the org adaptation profile (`cerg-org-profile-anytech.yml`)
7. Run the render tool to produce the working corpus
8. Create the first risk register entry: "Over-reliance on single MSSP"
9. Document the MSSP SLA agreement as an evidence artifact
10. Schedule monthly joint review with MSSP and MSP

## Files in This Pack

- `README.md` — this file
- `agent-prompt.md` — prompt for agent-assisted adoption
- `document-list.yaml` — structured document list
