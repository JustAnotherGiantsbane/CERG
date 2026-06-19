# Story 8: CERG Lite - Maria and the Tuesday scanner report

This story is for the CERG Lite team: 2-8 people running the Minimum Viable CERG (MVC) spine. Every other story in this directory assumes a Standard or Regulated team. Read [CERG-GOV-IMP-003](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) and [CERG-GOV-IMP-006](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) before this story.

## Situation

Northwind Logistics is a 60-person regional distribution company. Last quarter the CEO told the IT Lead, Maria, that she "also owns security now" after the previous security contractor walked off mid-engagement. Maria has two people on her team: Devin (help desk and endpoint) and Priya (network and cloud). None of the three has held a dedicated security role before.

Six weeks ago Maria adopted the MVC. The [Cybersecurity Policy](../../governance/CERG-POL-001_Cybersecurity_Policy.md) is signed by the Executive Sponsor (the COO). Maria is CISO + Governance + Risk Register consolidated. Devin is Engineering Lead. Priya is Risk + Exposure Management + Vendor Risk consolidated. The first 10 records exist (per IMP-003 §5): profile, role assignment map, asset extract, top 10 risks, exposure backlog, exception register, evidence index, control snapshot, regulatory applicability, and 30-day improvement backlog. The first weekly 1-hour cadence meeting ran last Friday.

It is Tuesday at 8:07 a.m. The vulnerability scanner has finished its weekly run against the production subnet, the staging cloud tenant, and the four external IPs. Priya opens the export. There are 47 findings. Two are rated Critical.

## CERG flow pattern

Primary flow: [F-04 Finding to Remediation, Exception, or Residual Risk](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md#12-flow-f-04-finding-to-remediation-exception-or-residual-risk)

Supporting procedures and standards:

- [Small Team Adoption Path](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) - the operating rhythm and role consolidation map for a 3-person team.
- [Role-Based Implementation Checklists](../../governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) - what each consolidated role does in week 1 through month 6.
- [Exposure Management Procedure](../../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) - the observe, validate, classify, treat, verify flow Priya runs.
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - how findings become risks, exceptions, or risk acceptances when treatment cannot meet the required clock.
- [Adoption Safety Guide](../../governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md) - role safety and decision log requirements for consolidated roles.
- [Risk Management Framework](../../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) - canonical risk scoring and Business Owner / Executive Sponsor acceptance authority.
- [Evidence Quality Standard](../../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md) - what "evidence" means on a spreadsheet in a small team.
- [Third Party and Supply Chain Risk Procedure](../../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) - vendor escalation, evidence requests, and alternate-service decisions.

### How the three pillars collapse onto three people

| Pillar | Consolidated role at Northwind | Primary responsibilities today |
|---|---|---|
| Governance | Maria (also CISO) | Decision log, exception routing, evidence index, executive sponsor liaison |
| Risk | Priya | Triage the 47 findings, severity calls, SLA tracking, risk register updates |
| Engineering | Devin | Patch planning, change windows, asset ownership confirmation |

The collapse is intentional and recorded in the [Decision Log](../../governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md#4-the-decision-log) per IMP-002 §4. Maria is the only person who signs exceptions. Priya owns the scanner schedule and the risk register. Devin owns the change record. There is no fourth person to delegate to.

## Walkthrough

| Step | What happens | Primary owner | Record or evidence |
|------|--------------|---------------|--------------------|
| 1 | Priya imports the 47 findings into the exposure backlog spreadsheet and tags each row with asset, reachability, source severity, and PRC-VM classification clock. | Priya (Risk) | Exposure backlog (EVD rows) |
| 2 | Priya validates reachability and asset ownership for the two Critical findings. One is on the customer portal web server; the other is on a legacy SFTP endpoint that hosts a vendor integration. | Priya (Risk) | Triage notes in Finding Record |
| 3 | Priya checks public exploit and KEV status. Both have public exploit code; the Internet-facing portal is classified as **Material Risk — PPR**. The vendor SFTP endpoint is treated as a Third-Party Finding with potential Critical residual risk until the vendor proves containment. | Priya (Risk) | Classification notes; PRC-VM SLA clock |
| 4 | Devin confirms the customer portal web server is in his asset inventory and that the application owner (Operations Director) is named. The SFTP endpoint is vendor-owned, so Devin identifies the integration path, credentials, logs, and whether Northwind can pause transfers safely. | Devin (Engineering) | Asset Record update; integration map; vendor question logged |
| 5 | Devin opens an emergency Change Record for the customer portal patch. He coordinates a same-day maintenance window with the Operations Director because PRC-VM's PPR clock is 48 hours for Internet-facing exposure. | Devin (Engineering) | Change Record |
| 6 | For the SFTP endpoint, Priya opens a Third-Party Finding, sends the vendor the CVE details, requests evidence of containment and patch timing, and references the contract SLA. Devin disables nonessential transfers, rotates credentials, and prepares an alternate encrypted transfer path for sensitive reports. | Priya (Risk) + Devin (Engineering) | Third-Party Finding; containment evidence; vendor evidence request |
| 7 | Maria reviews both Criticals immediately, not at the next weekly meeting. She can approve emergency containment and exception routing as CISO/Governance, but she cannot accept the vendor residual business risk alone. If the business must keep using the SFTP path before vendor remediation, Maria prepares a Risk Acceptance Request for the COO Executive Sponsor under RMF-001 §9.7. | Maria (Governance / CISO) | Decision Log entry; Risk Acceptance Request if continued use is required |
| 8 | The COO chooses the safer business path: pause sensitive SFTP transfers and use the alternate encrypted path until the vendor patches. Because the risky path is not used, no Critical risk acceptance is needed; the open item remains a Third-Party Finding with treatment tracking. | COO Executive Sponsor + Maria | Decision Log entry; business decision; alternate transfer evidence |
| 9 | After the maintenance window, Devin uploads patch output, the change ticket closure, and a service-validation screenshot. Priya rescans the portal and confirms closure. The portal Finding Record moves to Closed. | Devin (Engineering) + Priya (Risk) | Closed Finding Record |
| 10 | Priya leaves the remaining 45 findings in the exposure backlog with PRC-VM clocks running. She flags the 11 High findings for the biweekly exposure review. | Priya (Risk) | Updated exposure backlog |
| 11 | Maria updates the evidence index with the Closed Finding for the portal, the Third-Party Finding for the SFTP endpoint, the vendor evidence request, and the COO decision to use the alternate path. | Maria (Governance) | Evidence index entries |

### Narrative

At 8:07 a.m. Priya's email pings with the scanner export. She has been doing this every Tuesday for six weeks and has the spreadsheet template down. By 8:30 a.m. the two Critical findings are tagged, validated against the asset inventory, and routed. The portal finding goes to Devin and is classified as Material Risk — PPR because it is Internet-facing with public exploit code. The SFTP finding goes back to Priya because the asset is vendor-owned, but Priya does not treat vendor ownership as a reason to slow down.

Devin sees the portal Change Record in his queue at 8:45 a.m. He calls the Operations Director directly - the CERG escalation rule says a PPR exposure bypasses the normal change review queue. The Director approves a 2 p.m. maintenance window and reschedules a customer email blast so users hit the maintenance banner, not a blank page. Devin also applies a temporary WAF rule on the vulnerable path while the patch is prepared.

Maria does not wait for the weekly 1-hour meeting. She opens a 15-minute emergency risk huddle with Priya, Devin, and the COO. Priya explains that the vendor SFTP issue is not something Maria can simply accept as a security exception: if Northwind keeps sending sensitive reports over the exposed path, the COO must accept the business consequence under RMF-001 §9.7, with Maria approving as CISO. Devin offers a safer path: pause sensitive SFTP transfers, rotate credentials, monitor for anomalous SFTP traffic, and use an alternate encrypted transfer method until the vendor patches. The COO chooses the safer path, so no Critical residual-risk acceptance is needed.

Maria adds one Decision Log entry: "Vendor SFTP Critical exposure: sensitive transfers paused; alternate encrypted path approved by COO; vendor patch evidence due before SFTP resumes." Priya opens the Third-Party Finding, sends the vendor the CVE and evidence request, and records the contract SLA. This is still lightweight, but it is not informal.

At 2:15 p.m. the maintenance window opens. Devin deploys the portal patch, validates the service, captures the validation screenshot, and closes the change ticket. Priya rescans at 3 p.m. The portal PPR exposure is closed. The remaining exposure backlog carries the 45 other findings into the biweekly exposure review.

By the end of Tuesday, the team has produced:

- 1 closed Finding Record (portal Material Risk — PPR)
- 1 open Third-Party Finding (SFTP Critical, vendor remediation pending)
- 1 closed Change Record (portal patch)
- 1 Decision Log entry (Maria) recording the COO-approved alternate transfer path
- 1 vendor evidence request and contract-SLA follow-up
- 4 evidence index rows (portal closure, SFTP finding, vendor evidence request, COO decision)
- 11 High findings flagged for biweekly review

The team did not create a new committee or a heavyweight exception package, but it did interrupt the normal rhythm for a real Critical decision. Priya's scanner triage stayed spreadsheet-light. Devin's engineering work was bounded by the emergency change window. Maria's governance work was a short emergency huddle, a Decision Log entry, and the discipline to involve the COO when business consequence could not be accepted by security.

### Operating under the 5-person rhythm

The MVC spine did not break under pressure, but it also did not pretend every decision can wait for the weekly cadence. The emergency huddle protected the PPR clock and the vendor-risk decision without creating a standing committee. The Decision Log made Maria's CISO/Governance decision and the COO's business decision auditable. The exposure backlog spreadsheet gave Priya a place to capture every finding without opening a ticket for each one.

The collapse of the three pillars onto three people is the central design constraint of CERG Lite, not a workaround. Maria is doing CISO, Governance, and Risk Register work in one head. Devin is doing Engineering and Identity work in one head. Priya is doing Risk, Exposure Management, Threat Intel (read-only), and Vendor Risk in one head. The MVC spine fits because the consolidated roles each get one seat at the weekly meeting, and the records are designed to be one-row-per-event in a spreadsheet.

If Northwind grows to 8 people in the next year, the team will deconsolidate. Maria will keep CISO and Governance. Priya will keep Risk and Exposure Management. They will add a dedicated Identity Engineer, a dedicated Compliance person, and two more Engineering roles. The records do not change. The RACI in [OM-001](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) does not change. The cadence expands from weekly 1-hour to weekly 2-hour with sub-pillar owners. That deconsolidation is the documented growth path in IMP-003 §4.

## Operational outputs

- 1 closed Finding Record for the customer portal Material Risk — PPR exposure.
- 1 open Third-Party Finding for the SFTP Critical CVE, with vendor remediation and evidence due dates.
- 1 closed Change Record linked to the portal patch.
- 1 Decision Log entry recording Maria's CISO/Governance decision and the COO's business decision to use the alternate transfer path.
- 4 evidence index rows added (portal closure, SFTP finding, vendor evidence request, COO decision).
- 11 High findings flagged for the biweekly exposure review; remaining 34 findings left in the backlog with PRC-VM clocks running.

## What this story does not cover

- **Internal IR declaration.** Northwind's IR owner is a contracted MSSP. If the portal or SFTP evidence showed active compromise, Maria would call the MSSP / Incident Commander and F-06 would take over. This story covers exposure treatment before incident declaration. See Story 6 for the third-party incident pattern and IR handoff.
- **Audit response.** Northwind is not yet regulated. When their largest customer requests a SOC 2 attestation in six months, Story 3 will be the right reference.
- **AI tooling.** Northwind is not yet piloting AI. When the Operations Director asks about an AI assistant for the customer service team, Story 7 will be the right reference.

For the 5-person operating rhythm used in this story, see [CERG-GOV-IMP-003 §3](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#3-operating-rhythm-for-a-5-person-team). For the role consolidation map, see [CERG-GOV-IMP-003 §4](../../governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md#4-role-consolidation-map).
