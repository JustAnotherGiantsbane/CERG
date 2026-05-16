
### Foundational Security Principles: All Systems · All Environments · All Trust Levels

---

| **Document ID**    | CERG-POL-001                                             |
| ------------------ | -------------------------------------------------------- |
| **Version**        | 1.0 DRAFT                                                |
| **Status**         | For Review                                               |
| **Classification** | Internal - Confidential                                  |
| **Owner**          | Chief Information Security Officer                       |
| **Review Cycle**   | Annual / Upon Significant Change                         |
| **Frameworks**     | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r2](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · NIST RMF |
| **Regulations**    | NERC-CIP · [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 · · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC                     |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The CERG Operating Model](#2-the-cerg-operating-model)
3. [Definitions](#3-definitions)
4. [Foundational Security Principles](#4-foundational-security-principles)
5. [Roles and Responsibilities](#5-roles-and-responsibilities)
6. [Regulatory and Framework Alignment](#6-regulatory-and-framework-alignment)
7. [Exceptions and Risk Acceptance](#7-exceptions-and-risk-acceptance)
8. [Compliance and Enforcement](#8-compliance-and-enforcement)
9. [Policy Review and Maintenance](#9-policy-review-and-maintenance)
10. [Related Documents](#10-related-documents)

---

## 1. Purpose and Scope

This document establishes the foundational cybersecurity policy for the organization. It defines the enduring security principles that govern all information and operational technology, regardless of system type, classification, hosting environment, or regulatory regime.

These principles are intentionally durable. They do not change based on whether a system is a bulk electric system (BES) asset, a cloud-hosted SaaS application, a contractor-managed endpoint, or a leased data center facility. The standards, procedures, and implementation guidance derived from this policy will address environment-specific requirements. This policy establishes what is always true.

### 1.1 Scope

This policy applies to:

- All information systems and operational technology owned, operated, leased, or contracted by the organization
- All personnel with access to organizational systems, including employees, contractors, consultants, and third-party vendors
- All environments, including owned data centers, leased facilities, cloud service providers, SaaS platforms, and remote access connections
- All system classifications, including BES Cyber Systems under NERC-CIP, systems handling Controlled Unclassified Information (CUI) under [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems, and general enterprise IT
- All trust levels, from fully managed corporate devices to third-party contractor equipment accessing organizational resources

### 1.2 Policy Hierarchy

This policy sits at the top of the cybersecurity governance hierarchy. Subordinate documents provide the specific requirements and operational detail for implementing these principles:

| Level | Document Type | Purpose |
| --------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **1 - This document** | **Policy (CERG-POL-001)** | Enduring principles. What is always true. Authority for all below. |
| 2 | Standards | Specific, measurable requirements per system type, data class, or regulatory regime (e.g., BES Cyber System Standard, Cloud Security Standard). |
| 3 | Procedures | Step-by-step implementation guidance for specific activities (e.g., vulnerability scanning procedure, access review procedure). |
| 4 | Guidelines | Non-mandatory best practice and implementation advice. Supports engineering and operational teams. |

---

## 2. The CERG Operating Model

Cybersecurity operations are organized into three tightly coupled pillars under the Cyber Engineering, Risk, and Governance (CERG) framework, collectively known as SURGE. This model consolidates the core security work of the organization, eliminates structural silos, and produces Adaptive-tier maturity as defined by the NIST Cybersecurity Framework.

| **Engineering** | **Risk** | **Governance** |
| -------------------------------- | ------------------------ | --------------------- |
| Security architecture and design | Vulnerability management | Policy and standards |
| Pre-production reviews | Penetration testing | Compliance management |
| Control implementation | Threat intelligence | Evidence and audit |
| Configuration baselines | Vendor risk assessment | Risk register |
| IT/OT convergence advisory | Risk treatment support | Regulatory liaison |

These pillars operate simultaneously and continuously, not sequentially. CERG coordinates closely with the Security Awareness and Incident Response functions, which operate under separate charters. All CERG activities are subject to CISO oversight and report to the board through the CISO's risk and compliance reporting function.

> **The "Yes, And…" Standard**
> 
> Governance does not exist to block the business. The default orientation is enabling the business with guardrails, not closing doors. When a risk cannot be eliminated, it is documented, owned, treated, and monitored. Reflexive refusal is not an acceptable risk management strategy.

---

## 3. Definitions

The following terms are used throughout this policy and all subordinate documents.

|Term|Definition|
|---|---|
|**Asset**|Any information system, operational technology device, application, data repository, or network component owned, operated, leased, or contracted by the organization. Includes physical and virtual instances across all environments.|
|**BES Cyber System**|A grouping of BES Cyber Assets that perform one or more reliability tasks for a functional entity, as defined by NERC-CIP CIP-002.|
|**CERG / SURGE**|The Cyber Engineering, Risk, and Governance operating model. The three-pillar security function responsible for building secure systems, managing exposure, and governing the security program.|
|**CUI**|Controlled Unclassified Information. Information the Government creates or possesses, or that an entity creates or possesses for or on behalf of the Government, that law, regulation, or Government-wide policy requires or permits an agency to handle using safeguarding or dissemination controls (32 CFR Part 2002).|
|**Environment**|The hosting and operational context of an asset: owned data center, leased data center, cloud infrastructure (IaaS/PaaS), SaaS platform, or contractor-managed facility.|
|**OT / ICS**|Operational Technology / Industrial Control Systems. Hardware and software that monitors and controls physical devices, processes, and events in industrial environments, including SCADA systems, energy management systems, and substation automation.|
|**Risk Acceptance**|A documented management decision to acknowledge a risk and take no further action to reduce it, subject to approval thresholds defined in subordinate standards.|
|**Risk Treatment**|The process of selecting and implementing controls to modify risk. Includes risk reduction (implement controls), risk transfer (insurance, contract), risk avoidance (cease activity), and risk acceptance.|
|**System Trust Level**|The classification of confidence placed in a system or connection based on its ownership, management, and verification status. Ranges from fully trusted (organization-owned, managed, and monitored) to untrusted (unmanaged third-party or external networks).|
|**Vulnerability**|A weakness in an information system, system security procedure, internal control, or implementation that could be exploited or triggered by a threat source.|

---

## 4. Foundational Security Principles

The following ten principles constitute the enduring security requirements of this organization. They apply universally, to every asset, every environment, every trust level, and every regulatory context. Subordinate standards define how these principles are implemented in specific contexts.

> **How to Read These Principles**
> 
> Each principle states a universal mandate, what must always be true. The rationale explains why. The references identify the NIST controls and regulatory requirements the mandate satisfies. Implementation specifics (thresholds, timelines, approved tools, exceptions) are defined in subordinate standards.

---

### Principle 1: Maintain an Authoritative, Current Inventory of All Assets

**Mandate**

- The organization shall maintain a complete and current inventory of all assets within scope of this policy.
- Each asset record shall include, at minimum: asset identifier, system type (IT or OT), data classification, regulatory designation (BES Cyber System, CUI environment, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant system, or general IT), asset owner, and hosting environment.
- Asset inventory shall be updated upon any addition, modification, or decommission of an in-scope asset.
- Cyber Engineering is responsible for producing asset documentation at project handoff. Cyber Risk is responsible for validating inventory coverage through scan and assessment activities.

**Rationale**

You cannot protect what you do not know you own. An incomplete inventory is not a documentation gap, it is an unmanaged attack surface and, for regulated systems, a compliance gap that may constitute a reportable finding independent of any security event.

**References**

`NIST CSF IDENTIFY` · `NIST 800-53 CM-8` · `NIST 800-171 3.4.1` · `NIST RMF Step 1` · `NERC-CIP CIP-002` · `CMMC CM.2.061` · `Req 2.1, 12.5`

---

### Principle 2: Enforce Least Privilege and Verify Identity for All Access

**Mandate**

- Access to all organizational assets shall be granted on the basis of least privilege, the minimum access required to perform an authorized function.
- Identity shall be verified before access is granted. Multi-factor authentication (MFA) is required for all remote access and all access to privileged functions, regardless of network segment or system type.
- Default, shared, and generic credentials shall be eliminated. Each user, system, and service shall be uniquely identified.
- Accounts shall be provisioned, modified, and deprovisioned through a documented lifecycle process tied to authoritative sources (e.g., HR system, approved request workflow). Access reviews shall be conducted on a frequency defined in subordinate standards.
- Privileged access shall be managed under heightened controls, documented separately from standard user access, and subject to enhanced logging and session controls.

**Rationale**

Credential-based attacks are the leading initial access vector. Excessive privilege is the primary lateral movement enabler. Together, weak authentication and over-provisioned accounts convert every phishing attempt or credential theft into a potential enterprise-wide breach. In OT environments, over-privileged access to control systems may have no detective controls to catch misuse, prevention is the only effective control layer.

**References**

`NIST CSF PROTECT` · `NIST 800-53 AC-2, AC-6, IA-2, IA-5` · `NIST 800-171 3.1.1–3.1.3, 3.5.1–3.5.3` · `NIST RMF Step 3` · `NERC-CIP CIP-004 R4, CIP-005 R2, CIP-007 R5` · `CMMC AC.1.001, AC.2.006, IA.1.076, IA.3.083` · `Req 7, Req 8` · `SOX ITGC access controls`

---

### Principle 3: Harden All Systems to a Documented Baseline

**Mandate**

- All organizational assets shall be configured to a documented, approved security baseline prior to production deployment and maintained against that baseline throughout their operational life.
- Unnecessary services, protocols, ports, and software components shall be disabled or removed. Default configurations shall be replaced with organization-approved secure configurations.
- Configuration baselines shall be documented per asset class and maintained as a living artifact by Cyber Engineering.
- Deviation from an approved baseline requires a documented exception with compensating controls, owner acknowledgment, and a defined remediation timeline. Exceptions shall be tracked in the risk register.

**Rationale**

Default and unrestricted configurations are the attack surface that was never needed. Hardening eliminates exposure that cannot be exploited because it does not exist. In OT environments, unnecessary ports and services are a compliance finding under NERC-CIP CIP-007 R1 independent of whether a vulnerability exists in them, the control obligation is categorical.

**References**

`NIST CSF PROTECT` · `NIST 800-53 CM-6, CM-7` · `NIST 800-171 3.4.6, 3.4.7` · `NIST RMF Step 3` · `NERC-CIP CIP-007 R1, CIP-010 R1` · `CMMC CM.2.061, CM.2.064` · `Req 2`

---

### Principle 4: Segment Networks and Protect Sensitive Data

**Mandate**

- Networks shall be divided into defined security zones. Access between zones shall be explicitly permitted, documented, and enforced by technical controls.
- Environments containing regulated or sensitive data, including BES Cyber Systems, CUI-handling systems, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems, shall be isolated from general-purpose networks through documented, validated controls.
- Data shall be protected in transit using approved encryption standards. Data at rest that is classified as sensitive, regulated, or subject to contractual protection requirements shall be encrypted using organization-approved methods.
- IT and OT network interconnections shall receive heightened architectural scrutiny. All data flows crossing an IT/OT boundary require documented authorization, shall be minimized to operational necessity, and shall be validated through regular assessment.

**Rationale**

Flat networks convert a single compromised endpoint into an enterprise-wide breach. In IT environments, segmentation limits data theft and ransomware propagation. In OT environments, the consequence of inadequate segmentation is not data loss, it is potential manipulation or disruption of physical processes affecting operational reliability. The blast radius is not a technical metric; it is a reliability and safety metric.

**References**

`NIST CSF PROTECT` · `NIST 800-53 SC-7, SC-8, SC-28` · `NIST 800-171 3.13.1, 3.13.8, 3.13.10` · `NIST RMF Step 3` · `NERC-CIP CIP-005 (ESP/EAP), CIP-011` · `CMMC SC.1.175, SC.3.177` · `Req 1, Req 3, Req 4`

---

### Principle 5: Identify and Remediate Vulnerabilities on a Defined Schedule

**Mandate**

- The organization shall maintain continuous visibility into vulnerabilities affecting in-scope assets through a documented vulnerability management program operated by Cyber Risk.
- Vulnerabilities shall be assessed for severity, exploitability, and asset criticality. Findings shall be tracked to remediation or documented risk acceptance within timelines defined in subordinate standards.
- OT and BES Cyber Systems shall be scanned using approved methods that do not introduce operational risk. Timelines for OT remediation shall account for vendor testing requirements and operational windows, with NERC-CIP deviation processes invoked as required.
- Vulnerabilities identified during pre-production assessment shall be remediated or formally risk-accepted prior to production deployment. High and Critical severity findings require documented management authorization before go-live.
- The organization shall conduct periodic adversarial testing, penetration testing and red team operations, to validate that controls function under active attack conditions, not only under passive assessment.

**Rationale**

The majority of successful breaches exploit known vulnerabilities for which patches exist. An unmanaged vulnerability is not a theoretical risk, it is a documented entry point. In OT environments, the risk calculus is more complex: patching too quickly without vendor validation can introduce reliability risk; patching too slowly creates security exposure and regulatory non-compliance. Both failure modes require management.

**References**

`NIST CSF IDENTIFY, DETECT` · `NIST 800-53 SI-2, RA-5, CA-8` · `NIST 800-171 3.11.2` · `NIST RMF Steps 4, 6` · `NERC-CIP CIP-007-6 R2, CIP-010 R3` · `CMMC RM.2.141, SI.2.214, CA.2.157` · `Req 6.3, 11.3, 11.4`

---

### Principle 6: Control, Log, and Monitor All Privileged and Remote Access

**Mandate**

- All privileged access sessions and all remote access connections to organizational assets shall be logged. Log data shall include at minimum: identity, source, target system, session initiation and termination time, and actions performed where technically feasible.
- Session recording shall be applied to high-risk access as defined in subordinate standards.
- Log data shall be protected from modification and retained for periods defined per regulatory requirement. Log review shall occur on a defined cadence with findings escalated through the risk management process.
- Continuous monitoring capabilities, including security information and event management (SIEM) or equivalent, shall be deployed to detect anomalous activity across in-scope systems. OT monitoring shall use passive or approved active methods that do not introduce operational risk.
- Threat intelligence shall be integrated into monitoring to enable detection of known adversary techniques relevant to the organization's industry and system profile.

**Rationale**

Controls that cannot be observed cannot be verified. Privileged and remote access are the primary targets for both external attackers and malicious insiders post-compromise. Without logging, misuse is invisible, incident response is unattributable, and regulatory reporting is inaccurate. NERC-CIP CIP-005 R2 treats unlogged remote access to BES systems as a reportable condition regardless of whether any misuse occurred.

**References**

`NIST CSF PROTECT, DETECT` · `NIST 800-53 AU-2, AU-9, AU-11, AU-12, AC-17, SI-4` · `NIST 800-171 3.3.1, 3.14.6` · `NIST RMF Steps 3, 6` · `NERC-CIP CIP-005 R2, CIP-007 R4` · `CMMC AU.2.041, AU.2.042, SI.2.216` · `Req 8.2, Req 10` · `SOX ITGC access logging`

---

### Principle 7: Manage Configuration Changes Through a Controlled Process

**Mandate**

- All changes to in-scope assets, including software, firmware, configuration, and network changes, shall be authorized, documented, and reviewed prior to implementation.
- Configuration baselines shall be compared before and after changes to verify that only intended modifications were made.
- Unauthorized configuration changes shall be detected through technical controls and treated as security events subject to investigation.
- Change records shall be retained as audit evidence in accordance with applicable regulatory requirements.

**Rationale**

A hardened system that drifts back to an insecure state provides the same exposure as a system that was never hardened. Configuration drift is the primary mechanism by which effective controls degrade. Unauthorized changes are a primary persistence technique for advanced attackers, an adversary who disables a logging agent or opens a firewall rule has bypassed your controls without exploiting a single CVE. [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) treats unauthorized changes to financial systems as a control failure independent of any security event.

**References**

`NIST CSF PROTECT` · `NIST 800-53 CM-3, CM-5` · `NIST 800-171 3.4.3` · `NIST RMF Step 3` · `NERC-CIP CIP-010 R1` · `CMMC CM.2.062` · `Req 6.5` · `SOX ITGC change management`

---

### Principle 8: Extend Security Requirements to Third Parties and the Supply Chain

**Mandate**

- All third-party vendors, contractors, and service providers with access to organizational assets or data shall be assessed for security risk prior to onboarding and on a recurring basis defined in subordinate standards.
- Contractual agreements with third parties shall include security requirements addressing, at minimum: data handling, incident notification, access controls, right-to-audit provisions, and applicable regulatory compliance obligations.
- Software and technology acquired from third parties shall be assessed for supply chain integrity risk. Vendor-provided code and firmware shall be validated through organization-approved integrity verification methods.
- Third-party access shall be subject to the same least privilege, MFA, and logging requirements as organizational users. Remote access by vendors to OT and BES Cyber Systems requires explicit authorization and shall be logged and monitored.

**Rationale**

The organization's security posture extends only as far as its weakest trusted third party. Third parties with legitimate access are a primary attack vector, not because they are adversaries, but because they represent a trusted pathway that may be compromised without the organization's knowledge. The SolarWinds supply chain compromise demonstrated that a trusted, certified vendor can become an unwitting attack delivery mechanism at scale. Vendor questionnaires do not catch compromised software build pipelines.

**References**

`NIST CSF GOVERN` · `NIST 800-53 SA-9, SR-3` · `NIST 800-171 3.1.20` · `NIST RMF Step 2` · `NERC-CIP CIP-013` · `CMMC SR.3.169` · `Req 12.8, 12.9` · `SOX ITGC third-party SOC 2`

---

### Principle 9: Formalize Risk Management and Maintain an Active Risk Register

**Mandate**

- All identified risks to organizational assets and operations shall be documented in the organizational risk register with, at minimum: risk description, affected assets, risk owner, severity, treatment decision, compensating controls, and target closure date.
- Risk treatment decisions, including risk acceptance, require documented approval from the authorized approval authority as defined in subordinate standards. High and Critical risks require CISO or executive sponsor sign-off.
- The risk register shall be reviewed by leadership on a quarterly basis at minimum. Overdue or deteriorating risk items shall be escalated to the CISO.
- Risk management is an organizational function, not a security team function. Business unit owners bear accountability for the risks associated with their systems and processes. Cyber Governance facilitates and tracks; it does not absorb accountability on behalf of the business.

**Rationale**

Risks that are not formally documented are effectively accepted without acknowledgment, compensating controls, or accountability. When an undocumented risk materializes into an incident, there is no audit trail, no owner, and no record of what was understood at the time. Regulatory bodies treat the absence of documented risk decisions as evidence of a deficient risk management program, not as evidence that risk did not exist.

**References**

`NIST CSF GOVERN` · `NIST 800-53 RA-3, PM-9` · `NIST 800-171 3.11.1` · `NIST RMF Steps 4–5` · `NERC-CIP CIP-003` · `CMMC RM.2.141, RM.3.144` · `Req 12.3` · `SOX ERM interface`

---

### Principle 10: Prepare for, Respond to, and Learn from Security Events

**Mandate**

- The organization shall maintain documented, tested incident response and recovery plans that address the full lifecycle of a security event: detection, containment, investigation, notification, recovery, and lessons learned.
- Incident response plans shall include regulatory notification timelines and contact procedures for all applicable frameworks. Responsible parties shall know their roles before an incident occurs.
- Incident response capabilities shall be tested through tabletop exercises and simulated events at a frequency defined in subordinate standards. Untested plans shall not be treated as operational.
- Post-incident reviews shall produce documented lessons learned that are tracked to closure through Engineering (architectural improvements), Risk (threat landscape and assessment updates), and Governance (policy, standard, and playbook revisions).
- Recovery capabilities, including backup restoration, shall be tested on a defined schedule. Restoration of in-scope systems shall follow documented procedures that account for system-specific regulatory and operational constraints.

**Rationale**

An organization that has not practiced its incident response plan has a documented assumption, not an operational capability. The incident itself may be unavoidable; poor response is not. NERC-CIP CIP-008 makes this concrete for BES environments: the regulatory notification clock runs whether or not the organization is ready. The organization that recovers fastest from a significant event, and learns from it most completely, is the one most likely to avoid the next one.

**References**

`NIST CSF RESPOND, RECOVER` · `NIST 800-53 IR-2, IR-4, IR-8, CP-2, CP-9` · `NIST 800-171 3.6.1–3.6.3` · `NIST RMF Step 6` · `NERC-CIP CIP-008, CIP-009` · `CMMC IR.2.092, IR.2.093, RE.2.137` · `Req 12.10`

---

## 5. Roles and Responsibilities

The following table defines accountability for this policy and the principles it establishes. Detailed role descriptions and RACI matrices are maintained in the CERG Operating Model documentation.

|Role|Responsibility|
|---|---|
|**Chief Information Security Officer (CISO)**|Policy owner. Responsible for the cybersecurity program. Approves policy, standards, and High/Critical risk acceptances. Reports compliance posture and material risks to executive leadership and the board.|
|**Cyber Engineering (CERG Pillar)**|Implements security controls through project delivery. Produces asset documentation and configuration baselines. Ensures systems are designed to conform to this policy and subordinate standards prior to production deployment.|
|**Cyber Risk (CERG Pillar)**|Maintains continuous visibility into organizational exposure. Operates the vulnerability management, penetration testing, threat intelligence, and vendor risk programs. Identifies and communicates risk to Engineering, Governance, and leadership.|
|**Cyber Governance (CERG Pillar)**|Develops and maintains the policy and standards library. Tracks compliance posture across all applicable frameworks. Maintains the risk register and evidence library. Coordinates regulatory examinations and audits. Operates the compliance calendar.|
|**Business Unit Leaders / Asset Owners**|Accountable for the security posture of systems within their operational scope. Authorize risk treatment decisions. Support Engineering and Risk engagement. Provide operational context for compliance and risk activities.|
|**IT and OT Operations Teams**|Responsible for implementing and maintaining security controls on systems under their management. Participate in engineering reviews, vulnerability remediation, and change management processes.|
|**All Personnel with System Access**|Responsible for complying with this policy and all applicable subordinate standards and procedures. Required to complete role-appropriate security training. Required to report suspected security events.|

---

## 6. Regulatory and Framework Alignment

This policy is designed to satisfy the foundational policy and governance requirements of all applicable frameworks simultaneously. The table below maps each framework to the principles it addresses. Subordinate standards provide framework-specific implementation requirements.

|Framework / Regulation|Primary Control Families Addressed|Principles Satisfied|
|---|---|---|
|**[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)**|All 6 functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER|All 10 principles|
|**[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Rev 5**|PL, PM, RA, CA, AC, IA, SC, CM, SI, AU, IR, CP, PE, PS, SA, SR|All 10 principles|
|**[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 2**|All 14 domains (CUI environments)|Principles 1–7, 9–10|
|**NIST RMF**|Steps 1–6 (Categorize through Monitor)|All 10 principles|
|**NERC-CIP**|CIP-002 through CIP-014 (BES Cyber Systems)|Principles 1–7, 9–10|
|**[CMMC](https://dodcio.defense.gov/CMMC/) Level 2**|All 110 practices across 14 domains|Principles 1–7, 9–10|
|**[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC**|Change management, access, and availability controls|Principles 3, 4, 5, 7, 8|

> **The CERG Regulatory Advantage**
> 
> Organizations managing multiple regulatory obligations simultaneously, NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), typically suffer from duplicated effort, conflicting timelines, and fragmented evidence. The CERG model centralizes policy and compliance management in Governance while Engineering and Risk produce compliance evidence as a byproduct of their daily work. One policy hierarchy. One evidence library. One compliance posture.

---

## 7. Exceptions and Risk Acceptance

Exceptions to this policy are recognized as operationally necessary in specific, documented circumstances. An exception does not suspend a principle, it documents that a principle cannot be fully satisfied and defines the compensating controls and management accountability that apply in its place.

### 7.1 Exception Process

- Any personnel may initiate an exception request through Cyber Governance using the organization's approved exception request process.
- Exception requests shall document: the principle or requirement subject to exception, the business or operational justification, the affected systems, the proposed compensating controls, the risk owner, and the proposed exception duration.
- Cyber Risk shall assess the risk associated with each exception and provide a written finding to support the approval decision.
- Approval authority is defined by risk severity in subordinate standards. High and Critical risk exceptions require CISO approval at minimum. Exceptions affecting BES Cyber Systems, CUI environments, or [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems may require additional escalation as defined in applicable regulatory deviation procedures.
- Approved exceptions shall be entered into the risk register and tracked to expiration or remediation. Exceptions shall not be renewed without a new approval cycle.

### 7.2 Regulatory Deviations

For regulated environments, exceptions with regulatory implications shall follow the applicable deviation or mitigation plan process in addition to this exception process:

- **NERC-CIP deviations:** Governance initiates the CIP deviation documentation process. Compensating measures are implemented immediately. Regulatory notification is completed per applicable CIP standard timelines.
- **[CMMC](https://dodcio.defense.gov/CMMC/) non-conformances:** Governance maintains the Plan of Action and Milestones (POA&M) in the System Security Plan (SSP). Open POA&M items are tracked to closure with leadership visibility.

---

## 8. Compliance and Enforcement

Compliance with this policy is mandatory for all personnel within scope. Cyber Governance is responsible for tracking compliance posture and reporting material gaps to the CISO.

### 8.1 Compliance Monitoring

- Cyber Governance shall maintain a master compliance calendar covering all applicable frameworks and conduct ongoing monitoring of the organization's posture against each.
- Cyber Risk shall produce vulnerability and exposure data that informs the compliance posture assessment.
- Cyber Engineering shall produce handoff documentation and pre-production confirmations that serve as compliance evidence for Engineering activities.
- Evidence shall be collected as a byproduct of daily operations, not assembled retroactively in anticipation of audits. The evidence library shall be current, organized by control and regulatory citation, and retained per applicable framework requirements.

### 8.2 Non-Compliance

Non-compliance with this policy shall be managed through the risk register and exception process defined in Section 7. Willful or repeated non-compliance by personnel shall be referred to Human Resources and may result in disciplinary action up to and including termination.

Non-compliance findings identified by external regulators or auditors shall be escalated to the CISO immediately and tracked through the Governance risk register. The CISO shall determine whether escalation to executive leadership or the board is required.

---

## 9. Policy Review and Maintenance

This policy shall be reviewed annually by Cyber Governance and updated as needed to reflect changes in the threat environment, organizational structure, or applicable regulatory requirements.

This policy shall also be reviewed and updated upon: material changes to applicable regulations, significant organizational changes affecting scope, a significant security incident that reveals a gap in foundational principles, or direction from the CISO or executive leadership.

Proposed updates shall be reviewed by Cyber Engineering and Cyber Risk to ensure operational practicability before submission for CISO approval. Approved revisions shall be version-controlled and distributed to all personnel with compliance obligations under this policy.

### 9.1 Document History

|Version|Date|Summary|Author / Approver|
|---|---|---|---|
|1.0|TBD|Initial release|CISO|

---

## 10. Related Documents

The authoritative inventory, IDs, owners, status, deferred / planned artifacts, is maintained in `CERG-GOV-CAT-001` Document Catalog and Naming Convention. The summary below reflects the V1 library.

### 10.1 Cross-Cutting Instruments

| Document                                       | ID                       | Owner                 |
| ---------------------------------------------- | ------------------------ | --------------------- |
| Document Catalog and Naming Convention         | CERG-GOV-CAT-001         | Cyber Governance      |
| Unified Control Baseline                       | CERG-GOV-CB-001          | Cyber Governance      |
| Metrics, Dashboard, and CISO/Board Reporting   | CERG-GOV-MTR-001         | Cyber Governance      |
| CERG Operating Model                           | CERG-GOV-OM-001          | CISO                  |
| Risk Management Framework                      | CERG_RMF_v1.0            | Cyber Governance      |
| Compliance Matrix                              | CERG Compliance Matrix   | Cyber Governance      |
| Risk Taxonomy                                  | CERG Risk Taxonomy       | Cyber Risk            |

### 10.2 Standards

| Document                                                  | ID                | Owner                 |
| --------------------------------------------------------- | ----------------- | --------------------- |
| IT (Hosted, Cloud, and SaaS) Security Standard            | CERG-STD-IT-001   | Cyber Governance      |
| Grid Control Systems Security Standard                    | CERG-STD-OT-001   | Cyber Governance      |
| 