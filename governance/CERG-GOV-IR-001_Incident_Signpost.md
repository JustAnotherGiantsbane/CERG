# CERG Incident Signpost — Who Commands the Response, and Where the Procedures Live

| | |
|---|---|
| **Document ID** | CERG-GOV-IR-001 |
| **Version** | 0.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (this page only) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) |
| **Review Cycle** | Annual, and whenever the IR team changes PLN-IR-001 or PRC-IR-002 |

> **During an incident, the standing IR team's procedures and the Incident Commander's authority take precedence over any CERG workflow.**
> — [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md), quoted verbatim. This page cannot and does not change that sentence.

## Start here

There is a live incident. Call the standing IR team. Their plan is [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) and their playbooks are [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md). This page does not tell you how to fight the fire. It tells you who does, and where to find their pages in two seconds instead of twenty minutes.

One fact saves that twenty minutes: **CERG owns no incident-facing document.** The plan and the playbook set belong to the standing IR team. Their metadata says so on their own first page — Owner: Standing IR Team / Incident Commander; CERG Governance reviews them for cross-reference accuracy only. If you arrived here assuming the framework has a procedure for the incident itself, you have the wrong assumption, and this page exists to break it early.

## What CERG does during an incident

CERG's role is supporting. Per [`CERG-GOV-OM-001` §3.4](CERG-GOV-OM-001_CERG_Operating_Model.md#34-what-cerg-is-not-responsible-for) and [`CERG-GOV-FLOW-001` F-06](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md), CERG brings three things to an IR-led incident:

1. **Liaison.** A named CERG contact so the IR team never digs through the standards library for context.
2. **Evidence.** Control state, exposure history, and logs that CERG maintains — delivered as support, not as direction.
3. **The learning loop.** When the response closes, F-06 routes the lessons: a Lessons Learned Record, and a Program Improvement Record wherever CERG itself must change.

What CERG does not bring: direction of the response, ownership of the notification clocks, or the exercise schedule. Those are §3.4's explicit not-responsibilities, and no page in this repository — including this one — can quietly move them.

## Find the playbook fast

All section numbers below live in [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md).

| Scenario | Section |
|---|---|
| Ransomware | §4 |
| Business email compromise | §5 |
| Data breach or exfiltration | §6 |
| Phishing campaign | §7 |
| Distributed denial of service | §8 |
| Insider threat | §9 |
| Cloud account compromise | §10 |
| Supply chain compromise | §11 |
| Web application attack | §12 |

Two CERG pages matter mid-incident, as support: [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) when containment changes what is exposed, and [`CERG-GOV-RMF-001` §9.7](CERG-GOV-RMF-001_Risk_Management_Framework.md) when someone demands a risk acceptance at speed. The authority table in §9.7 does not get faster during an incident. It gets more important.

## Why this page exists, and what it deliberately is not

The incident documents in this repository are complete, tested, and not ours. Editing them to make them read better would be overreach dressed as kindness. So this page does the one thing CERG can do unilaterally: it states where the authority lives, in the IR team's own words, and routes to their documents without touching a word of them.

It is not an IR plan. It is not a procedure. It grants nothing and changes nothing. If it ever appears in an audit answer, the answer should still come from the IR team's pages — this is the signpost, not the road.

**Naming, so nobody has to guess in a hallway.** This page is "the signpost". The plan and the playbooks are always named by their full IDs — `CERG-PLN-IR-001`, `CERG-PRC-IR-002` — because "IR-001" alone could be either document, and the one moment it gets said out loud is the moment there is no time to work out which.
