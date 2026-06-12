# CERG Example: Regulated Utility Profile

This is a **sample organization profile** for a regulated electrical utility adopting CERG.
It is provided as a reference example, not the default.

If your organization matches this profile, use it as a starting point for your
[Organization Adaptation Profile](../../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md).

---

## Organization context

| Field | Value |
|-------|-------|
| **Sector** | Electric utility (generation, transmission, distribution) |
| **Employees** | ~14,000 |
| **Contractors** | ~14,000 (roughly equal population) |
| **Protected population** | ~28,000 identities, devices, access relationships |
| **CERG team size** | 60 (14 Engineering, 15 Risk, 13 Governance, plus CISO, pillar leaders, management) |
| **Regulators** | NERC-CIP (dozens of registered entities, hundreds of BES Cyber Systems), CMMC L2, SOX ITGC, state regulatory |
| **Environments** | Enterprise IT, OT/ICS (SCADA, substations, EMS), cloud (IaaS/PaaS/SaaS), owned data centers |
| **Scale tier** | Large |

## VAR-001 token values

| Token | Value |
|-------|-------|
| `{{ORG_NAME}}` | `[Your Utility Name]` |
| `{{ORG_SECTOR}}` | `electric utility` |
| `{{TOTAL_EMPLOYEES}}` | `14,000` |
| `{{PROTECTED_POPULATION}}` | `28,000` |
| `{{CERG_TEAM_SIZE}}` | `60` |
| `{{ENG_STAFF}}` | `14` |
| `{{RISK_STAFF}}` | `15` |
| `{{GOV_STAFF}}` | `13` |
| `{{SCALE_TIER}}` | `large` |
| `{{REGULATORS}}` | `NERC-CIP, CMMC L2, SOX ITGC` |
| `{{PRIMARY_REGULATOR}}` | `NERC-CIP` |

## Operational context

At this scale, the workload is substantial across all three pillars.

**Engineering** carries approximately 125 active project engagements per year with roughly 40 running concurrently, spanning IT infrastructure, enterprise applications, OT modernization, cloud migrations, and third-party integrations. Engineers are aligned to specific business verticals (generation, transmission, distribution, enterprise IT, corporate functions) and develop fluency in the systems they support — a generation-aligned engineer who doesn't understand how a historian feeds an EMS is less effective.

**Risk** operates at equivalent velocity. The vendor risk program covers more than 2,500 active vendors. Vulnerability management covers more than 100,000 assets across enterprise IT, OT networks, substations, and cloud environments, with OT-safe scanning disciplines. Penetration testing and red team operations run on continuous cycles across IT and OT targets. Threat intelligence is a production function with ICS/OT-specific coverage given bulk electric system exposure.

**Governance** operates as a domain-expert function, not a generalist compliance team. The compliance portfolio spans NERC-CIP (across dozens of registered entities and hundreds of categorized BES Cyber Systems), CMMC, SOX ITGC, and state regulatory requirements. Policy and standards are actively maintained, version-controlled, and tied to regulatory citation.

## Key operational packages

- [NERC-CIP Operational Package](../../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
- [CUI / CMMC Operational Package](../../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
- [SOX ITGC Operational Package](../../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)
- [Grid Control Systems Security Standard](../../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)
- [Business Continuity & DR Plan](../../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md)

## See also

- [CERG Framework §9](../../governance/CERG-GOV-FRM-001_CERG_Framework.md) — Team Structure and Talent Model
- [Organization Adaptation Profile](../../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) — Token scheme and render tool
- [Small Team Adoption Path](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) — Contrast with small-scale adoption
