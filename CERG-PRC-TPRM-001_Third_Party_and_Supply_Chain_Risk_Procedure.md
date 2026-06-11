1|# SURGE: Cyber Engineering, Risk & Governance
2|
3|## THIRD-PARTY AND SUPPLY CHAIN RISK PROCEDURE
4|### Vendor Tiering · Evidence by Tier · Contract Clauses · SBOM · International Access · Supply Chain Compromise Team (SCCT)
5|
6|---
7|
8|| | |
9||---|---|
10|| **Document ID** | CERG-PRC-TPRM-001 |
11|| **Version** | 1.0 |
12|| **Status** | Published |
13|| **Classification** | Public |
14|| **Owner** | Vendor Risk Analyst |
15|| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
16|| **Supporting Documents** | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md) |
17|| **Review Cycle** | Annual / On major TPRM platform change |
18|| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SR) · NIST 800-161r1 · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GV.SC) · ISO 27036 · CSA STAR · NTIA SBOM minimum elements |
19|| **Regulations** | NERC-CIP CIP-013 · DFARS / [CMMC L2](https://dodcio.defense.gov/CMMC/) · SOX ITGC · FedRAMP equivalency |
20|| **Environments** | All third-party-touched scopes - SaaS · IaaS/PaaS · OT vendors · CUI subcontractors · MSPs · software suppliers · hardware suppliers |
21|
22|---
23|
24|## Table of Contents
25|
26|1. [Purpose and Scope](#1-purpose-and-scope)
27|2. [Roles and Interface to Procurement / ERM / BR](#2-roles-and-interface-to-procurement--erm--br)
28|3. [Vendor Tiering](#3-vendor-tiering)
29|4. [Cyber-Specific Score Adjustment](#4-cyber-specific-score-adjustment)
30|5. [Evidence by Tier](#5-evidence-by-tier)
31|6. [Differences by Vendor Type](#6-differences-by-vendor-type)
32|7. [Approved Provider and SaaS Catalog](#7-approved-provider-and-saas-catalog)
33|8. [Contract Security Clause Library](#8-contract-security-clause-library)
34|9. [Shared Responsibility Matrix](#9-shared-responsibility-matrix)
35|10. [International Access, Denied by Default](#10-international-access--denied-by-default)
36|11. [SBOM and Software Integrity](#11-sbom-and-software-integrity)
37|12. [CIP-013 Supply Chain Plan](#12-cip-013-supply-chain-plan)
38|13. [CUI Subcontractor Flow-Down](#13-cui-subcontractor-flow-down)
39|14. [FedRAMP Equivalency Evidence](#14-fedramp-equivalency-evidence)
40|15. [Supply Chain Compromise Team (SCCT)](#15-supply-chain-compromise-team-scct)
41|16. [Continuous Monitoring and Re-Assessment](#16-continuous-monitoring-and-re-assessment)
42|17. [Regulatory and Framework Alignment Summary](#17-regulatory-and-framework-alignment-summary)
43|18. [Document Control](#18-document-control)
44||
45||---
46|
47|## 1. Purpose and Scope
48|
49|The policy makes third-party and supply-chain security Principle 8. Subordinate standards each impose specific requirements: IT/cloud/SaaS approval and attestation tracking, OT vendor assessment and CIP-013, CUI flow-down and FedRAMP equivalency, SBOM and software integrity. Until this procedure, those obligations had no shared operating model.
50|
51|This procedure defines how CERG engages with the broader enterprise vendor program, where CERG's cyber-specific work begins and ends, what evidence is collected at each tier, and how the program responds when a vendor is compromised.
52|
53|> **CERG Doesn't Own Vendor Management, It Owns the Cyber Slice**
54|>
55|> Procurement, Enterprise Risk Management, and Business Resiliency typically own vendor tiering, contract lifecycle, and business continuity. CERG accepts the business tier as the starting point and adjusts only where cyber-specific concerns are material enough to alter it. This boundary is the difference between a TPRM program that ships and one that drowns in vendors.
56|
57|---
58|
59|## 2. Roles and Interface to Procurement / ERM / BR
60|
61|| **Function** | **Owns** | **CERG Interface** |
62||---|---|---|
63|| **Procurement** | Vendor onboarding, contracts, master vendor record. | CERG reviews proposed contracts for security clauses; SCCT escalation routes through Procurement for contractual remedies. |
64|| **Enterprise Risk Management (ERM)** | Enterprise vendor tier, criticality, business-impact rating. | CERG accepts the business tier as input; adjusts only per Section 4. |
65|| **Business Resiliency** | Vendor continuity, exit plans. | CERG cyber-recovery expectations feed BR vendor recovery plans. |
66|| **Legal (external)** | Contract negotiation, regulatory flow-down, privacy notices. | CERG provides cyber clauses (Section 8); Legal owns negotiation. |
67|| **Vendor Risk Analyst** | This procedure. Vendor cyber assessments, SCCT, evidence-by-tier, continuous monitoring. | - |
68|| **Governance Pillar Leader** | Cyber audit interface; regulator-facing artifacts ([CMMC](https://dodcio.defense.gov/CMMC/) SSP, CIP-013 plan). | - |
69|| **Business / Asset Owners** | Vendor relationship; business-side acceptance of vendor-related risk. | Sign off on residual cyber risk per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
70|
71|---
72|
73|## 3. Vendor Tiering
74|
75|CERG uses a 5-tier vendor model that maps to the typical enterprise model. Business rating sets the baseline; CERG adjusts only via Section 4.
76|
77|| **Tier** | **Description** | **Examples** |
78||---|---|---|
79|| **T1 - Critical** | Failure or compromise has material business, safety, regulatory, or financial impact. | Core ERP SaaS, primary cloud provider, OT vendor with operator presence, IDP, EDR. |
80|| **T2 - Significant** | Failure or compromise materially disrupts operations or exposes Restricted/CUI data. | CRM SaaS, Tier 1 SaaS holding sensitive data, financial-system MSP. |
81|| **T3 - Standard** | Failure or compromise is operationally inconvenient but recoverable in days. | Productivity SaaS, secondary tooling. |
82|| **T4 - Limited** | Minor business impact; no Restricted data; bounded blast radius. | Marketing tools, training providers. |
83|| **T5 - Transactional** | One-off purchase, commodity goods, no system access, no data access. | Office supplies, conference services. |
84|
85|### 3.1 Tiering Inputs
86|
87|CERG accepts the **business tier** from ERM / Procurement as the starting point. Inputs include data classification handled, system access granted, regulatory scope, blast radius, and operational dependency.
88|
89|---
90|
91|## 4. Cyber-Specific Score Adjustment
92|
93|CERG adjusts the vendor tier *up* only when one or more cyber-specific concerns are material. Adjustments down (vendor "isn't as critical as Business says") are not permitted, Business owns criticality.
94|
95|### 4.1 Adjustment Triggers
96|
97|| **Cyber Concern** | **Adjustment** |
98||---|---|
99|| Vendor has privileged access to in-scope systems | +1 tier |
100|| Vendor processes / stores Restricted, CUI, or BCSI data | +1 tier (to T1 if CUI/BCSI) |
101|| Vendor handles OT integration or BES Cyber System interaction | +1 tier (to T1 if BCS) |
102|| Vendor has a recent (≤ 12 months) material breach affecting its customers | +1 tier with case-by-case review |
103|| Vendor is operating below the evidence floor for its proposed tier | hold at lower tier until evidence is current |
104|| Vendor's product / service supports a SOX-relevant business process | +1 tier if not already T2+ |
105|| Vendor product is software shipped to be deployed in our environment with elevated privileges | +1 tier |
106|| Vendor relationship requires non-US access to in-scope systems / data | +1 tier (and see Section 10) |
107|
108|> **Adjustments Are Documented, Not Negotiated**
109|>
110|> Every cyber-driven tier adjustment is recorded in the TPRM tool with the trigger, evidence, and reviewer. If a Business Owner disagrees, the resolution path is [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) Section 8, never an off-record handshake.
111|
112|---
113|
114|## 5. Evidence by Tier
115|
116|Evidence requirements grow with tier. The table below names the cyber evidence required *at minimum*; specific subordinate standards may require more (e.g., FedRAMP for CUI scope).
117|
118|| **Evidence** | **T5** | **T4** | **T3** | **T2** | **T1** |
119||---|---|---|---|---|---|
120|| SOC 2 Type II (or ISO 27001) attestation, current | - | optional | required | required | required |
121|| SOC 2 carve-outs and CUECs reviewed | - | - | - | required | required |
122|| ISO 27001 certificate (where SOC 2 not applicable) | - | optional | required | required | required |
123|| FedRAMP authorization (Moderate or High) for CUI / federal scope | - | - | - | required (CUI) | required (CUI) |
124|| FedRAMP equivalency documentation per Section 14 | - | - | - | required (CUI, where applicable) | required (CUI, where applicable) |
125|| [CMMC](https://dodcio.defense.gov/CMMC/) Level (1 or 2) status for CUI subcontractor | - | - | - | required (CUI) | required (CUI) |
126|| Penetration test summary (sanitized) | - | - | - | required | required |
127|| SIG / CAIQ questionnaire (or CERG equivalent) | - | - | optional | required | required |
128|| SBOM for software products in use | - | - | required (software) | required | required |
129|| Hardware Bill of Materials (HBOM) | - | - | - | optional | required (OT / hardware in BES scope) |
130|| Subprocessor list and CUEC review | - | - | required (SaaS) | required | required |
131|| Right-to-audit clause | - | - | optional | required | required |
132|| Breach / incident notification commitment (timing, scope) | - | required | required | required | required |
133|| Insurance: cyber liability, E&O, where contract-appropriate | - | optional | required | required | required |
134|| OT vendor: NERC-CIP CIP-013 plan participation | - | - | - | required (OT) | required (OT / BES) |
135|| Inheritance Evidence Package (per [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 5) for inherited controls | - | - | - | required | required |
136|| Country-of-access disclosure and country-risk rating | - | - | required | required | required |
137|
138|### 5.1 Evidence Currency
139|
140|- T1 evidence is reviewed annually, no later than 30 days before attestation expiry.
141|- T2 evidence is reviewed annually.
142|- T3 evidence is reviewed every 24 months unless conditions change.
143|- T4/T5 evidence is reviewed on contract renewal.
144|
145|Material vendor events (breach, ownership change, regulator action) trigger an out-of-cycle review regardless of tier.
146|
147|---
148|
149|## 6. Differences by Vendor Type
150|
151|Requirements differ by what the vendor *is*. The table below summarizes the most-different requirements; subordinate standards govern detail.
152|
153|| **Vendor Type** | **Distinctive Requirements** |
154||---|---|
155|| **SaaS provider** | Approved Provider Catalog (Section 7); shared responsibility matrix (Section 9); CSPM/SSPM coverage on the consumer side; tenant configuration baseline per [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md). |
156|| **IaaS / PaaS provider** | Landing zone baseline; CMK or BYOK per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md); provider attestation including service-in-scope reconciliation; sub-service organization carve-outs. |
157|| **OT vendor** | CIP-013 plan participation; SBOM; firmware integrity verification; 24-hour incident notification commitment; engineering-controlled remote access; on-site presence vetting. |
158|| **CUI subcontractor** | DFARS / 252.204-7012 flow-down; [CMMC L2](https://dodcio.defense.gov/CMMC/) status; incident notification cooperation (DC3); CUI handling commitment with same controls as us. |
159|| **Managed Service Provider (MSP)** | Privileged access via PAM ([`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md)); session recording; named-individual accounts; geographic-access controls; tenant separation evidence. |
160|| **Software supplier (commercial / open source)** | SBOM (NTIA minimum elements); CVE / advisory subscription; software integrity (signed releases); patch / EOL commitments. |
161|| **Hardware supplier (esp. OT)** | HBOM where in BES scope; chain-of-custody; firmware integrity; tamper-evidence; secure delivery. |
162|
163|---
164|
165|## 7. Approved Provider and SaaS Catalog
166|
167|CERG maintains an Approved Provider and SaaS Catalog as the system-of-record for which third-party services may be procured for which scope.
168|
169|| **Field** | **Definition** |
170||---|---|
171|| Provider Name / Service | - |
172|| Vendor Tier | Per Section 3 + Section 4 adjustments |
173|| Approved Scopes | None / Public / Internal / Restricted / CUI / BCSI / SOX-relevant / BES-relevant |
174|| Data Residency Constraints | Approved regions / regions explicitly prohibited |
175|| Last Evidence Review | Date and reviewer |
176|| Next Required Review | - |
177|| Outstanding Risks | Risk register IDs |
178|| Inheritance Evidence | Y/N - link |
179|| Status | Approved · Approved-with-Conditions · Conditional Use Only · Sunset · Prohibited |
180|
181|Procurement consults the catalog at intake; CERG updates it at each evidence cycle and after each SCCT closure.
182|
183|---
184|
185|## 8. Contract Security Clause Library
186|
187|CERG provides Legal with a clause library; Legal owns negotiation. Clauses below are the minimums to seek; alternative language with equivalent intent is acceptable.
188|
189|| **Clause** | **Required For** | **Substantive Content** |
190||---|---|---|
191|| Security controls baseline | T2+ | Vendor commits to maintain controls aligned to a named standard ([NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [NIST CSF 2.0](https://www.nist.gov/cyberframework), ISO 27001) for the data and access in scope. |
192|| Incident notification | All accessing data/systems | Notification within 24 hours (T1/OT/BES) or 72 hours (T2) of confirmed incident affecting customer data or services. |
193|| Right to audit | T2+ | Documented audit rights, including evidence on request, with reasonable notice; alternatives include current SOC 2/ISO/FedRAMP report. |
194|| Subprocessor consent | SaaS T2+ | Customer-facing list of sub-processors; notification on change. |
195|| Data location | All processing Restricted/CUI/BCSI | Defined regions; no data movement to non-approved regions without consent. |
196|| Encryption | All processing Restricted/CUI | TLS in transit; FIPS-validated where required; CMK / BYOK rights documented per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md). |
197|| Return / destruction of data | All processing customer data | On termination; documented method and timeline; certification. |
198|| Vulnerability and patch | Software / hardware suppliers | Vendor commits to remediation SLAs aligned to severity; advisory publication. |
199|| SBOM | Software suppliers (T1/T2) | SBOM at NTIA minimum elements at delivery and at material update. |
200|| Background checks | MSPs / vendors with privileged access | Background screening; named-individual access; geographic-access controls. |
201|| Insurance | T2+ | Cyber liability and E&O at industry-appropriate levels. |
202|| Cooperation | All accessing data/systems | Cooperation in incident investigations and regulator inquiries. |
203|| Flow-down | CUI subcontractors | DFARS 252.204-7012 / [CMMC](https://dodcio.defense.gov/CMMC/) requirements flowed to sub-tier. |
204|| CIP-013 | OT vendors in BES scope | Participation in supply chain security plan including software integrity, incident notification, coordination of access controls. |
205|| International access | T2+ where international access proposed | Country-of-access disclosure; right to refuse non-approved geographies. |
206|
207|---
208|
209|## 9. Shared Responsibility Matrix
210|
211|Every T2+ cloud / SaaS provider has a Shared Responsibility Matrix on file. Where the vendor publishes one, CERG annotates it; where they don't, CERG produces it and seeks vendor confirmation.
212|
213|| **Control Area** | **Provider Owns** | **Customer Owns** | **Customer-Side Evidence Reference** |
214||---|---|---|---|
215|| Physical security | Provider | - | - |
216|| Hypervisor / base platform | Provider | - | - |
217|| Tenant isolation | Provider | Configuration | DISH scan / SSPM |
218|| Identity / authentication | Provider provides; Customer configures | Customer configures | IdP policy export |
219|| Encryption (rest / transit) | Provider provides; Customer chooses CMK/BYOK | Customer configures | KMS inventory |
220|| Logging | Provider provides; Customer routes | Customer routes | SIEM source inventory |
221|| Detection | Provider provides limited; Customer extends | Customer extends | Detection coverage |
222|| Recovery / backup | Provider depending on service | Customer-driven for CUI / SOX / Tier 1 | Backup config |
223|| Configuration management | Provider for service; Customer for tenant | Customer | DISH scan |
224|| Subprocessor management | Provider | Customer accepts / refuses | Sub-processor list |
225|
226|The matrix is the single source of truth for cross-team conversations about "who handles X."
227|
228|---
229|
230|## 10. International Access: Denied by Default
231|
232|International access to in-scope systems and data is **denied by default**. Where business need requires it, access is treated as a documented exception with conditions.
233|
234|### 10.1 Operating Model
235|
236|- A **Country Risk Register** classifies each country into tiers: Permitted · Restricted · Conditional · Prohibited.
237|- Permitted countries are those with established trust relationships, low geopolitical risk, and acceptable law-enforcement / data-protection regimes; access is allowed without exception (logged, monitored).
238|- Restricted countries require an exception per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), with named controls (managed-device-only, session recording, enhanced detection routing).
239|- Conditional countries require additional senior exec / CISO approval, time-boxed access windows, and possible per-session approval.
240|- Prohibited countries do not get access; business need is resolved by alternative means (US-based delivery, alternate vendor).
241|- The Country Risk Register is reviewed at least quarterly; geopolitical events can trigger reclassification at any time.
242|- All international access is logged to SIEM with country-of-access metadata; the SOC routing pack includes country-tier as a fast-triage field.
243|
244|### 10.2 Vendor Implications
245|
246|- Vendors must disclose all proposed countries of access at onboarding and at any change.
247|- Vendor international-access tier above the country's permitted level triggers a contract addendum and exception.
248|- Vendor non-disclosure of country-of-access discovered post-onboarding is a material event triggering SCCT.
249|
250|---
251|
252|## 11. SBOM and Software Integrity
253|
254|### 11.1 SBOM
255|
256|- Required for T1/T2 software vendors and Tier 1 commercial software products.
257|- Minimum elements: NTIA minimum elements (supplier name, component name, version, dependency relationship, author, timestamp, unique identifier).
258|- SBOM submitted at delivery and at every material update.
259|- SBOMs scanned for known vulnerabilities; findings flow to [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md).
260|- SBOMs reviewed at architecture review for embedded secrets, suspect packages, and license risk.
261|
262|### 11.2 Software Integrity
263|
264|- Releases signed by the vendor; signatures verified before deployment.
265|- Container images signed (cosign / sigstore); admission gate per [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) Section 7.
266|- Firmware (OT) verified per [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md); firmware updates follow CIP-010 process per [`CERG-PLN-CIP-001`](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md).
267|
268|---
269|
270|## 12. CIP-013 Supply Chain Plan
271|
272|For BES Cyber Systems, CERG maintains a CIP-013 Supply Chain Risk Management Plan as a [CERG-PLN-CIP-001](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) component, satisfying CIP-013-2 R1. The plan includes:
273|
274|- Identification of supply chain risks across procurement and installation.
275|- Vendor security controls expectations (incident notification, coordination of access controls, software integrity, vendor remote access management, disclosure of known vulnerabilities).
276|- Procurement controls, clauses, evaluation, approvals.
277|- Implementation and verification, how controls are verified at installation and over time.
278|- Coordination with this procedure: vendor records here are CIP-013 records.
279|
280|---
281|
282|## 13. CUI Subcontractor Flow-Down
283|
284|| **Requirement** | **Source** |
285||---|---|
286|| DFARS 252.204-7012 flow-down to subcontractors handling CUI | DFARS |
287|| [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 third-party assessment status verification | DoD / [CMMC](https://dodcio.defense.gov/CMMC/) |
288|| Incident notification cooperation, including DC3 reporting | DFARS |
289|| Same encryption / handling requirements as the prime | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) + [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
290|| CUI Subcontractor Register maintained | [`CERG-PLN-CUI-001`](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) |
291|
292|---
293|
294|## 14. FedRAMP Equivalency Evidence
295|
296|Where a CUI-relevant SaaS / cloud service is not FedRAMP-authorized but is proposed for use, CERG requires a documented FedRAMP-equivalency package:
297|
298|- SOC 2 Type II with [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Moderate baseline mapping.
299|- 3PAO-equivalent assessment letter or independent assessor attestation.
300|- Customer-side configuration commitments (CUI label, region, key control).
301|- Sub-service organization carve-outs reconciled.
302|- Re-papering trigger documented (FedRAMP authorization issued, attestation lapses, scope change).
303|
304|The package is recorded in the TPRM tool as the vendor's Inheritance Evidence Package for the CUI overlay.
305|
306|---
307|
308|## 15. Supply Chain Compromise Team (SCCT)
309|
310|When a vendor reports, or is publicly disclosed as having, a material cybersecurity incident affecting their service or product, CERG activates the **Supply Chain Compromise Team (SCCT)**.
311|
312|### 15.1 SCCT Membership
313|
314|At minimum:
315|
316|- **SOC / Incident Response lead**: coordinates investigation and customer-side detection / containment.
317|- **CERG, Risk (TPRM)**: vendor liaison; assembles vendor-supplied facts; updates TPRM record.
318|- **CERG, Governance**: regulator notification path; CUI / NERC-CIP / SOX reporting if applicable.
319|- **Legal**: contractual remedies, regulator interface, communications review.
320|- **Procurement**: vendor relationship; commercial leverage.
321|- **Business Owner of the affected service**: operational decision authority; user / customer communications.
322|
323|Other invitees as needed: CISO (declared briefing), Privacy (PII implications), Engineering, OT operations (OT vendors), Communications.
324|
325|### 15.2 SCCT Activation Triggers
326|
327|- Confirmed vendor breach affecting our data, systems, or service.
328|- Material vulnerability in a deployed vendor product (e.g., critical CVE, supply-chain implant).
329|- Vendor's regulator action affecting our reliance on their service.
330|- Public reporting of a vendor compromise where our exposure is plausible.
331|- Vendor non-disclosure of country-of-access discovered.
332|- Discovery of unauthorized vendor sub-processor handling our data.
333|
334|### 15.3 SCCT Workflow
335|
336|1. **Activate.** TPRM declares SCCT, notifies membership within 4 business hours of trigger (1 business hour for T1 vendors).
337|2. **Assemble facts.** Vendor advisory, public reporting, internal exposure analysis (which systems, which data, which scopes).
338|3. **Contain.** Coordinate with SOC / IR on containment, credentials rotation, vendor session termination, IOC sweep, detection tuning.
339|4. **Decide.** Disposition: continue use with conditions / suspend use / terminate. Documented and owned by Business + CISO.
340|5. **Communicate.** Internal user / customer notification per Legal; regulator notification where required (CUI DC3, NERC-CIP O&P, SOX disclosure committee).
341|6. **Remediate.** Risk register entries, exception updates, contract addenda, monitoring uplift.
342|7. **Close.** SCCT after-action with lessons learned; feeds threat intelligence and detection.
343|
344|### 15.4 SCCT Evidence
345|
346|Every SCCT activation produces an SCCT record with: trigger, membership, timeline, decisions, notifications, risk register updates, vendor-side commitments. Records are retained for the longer of the vendor relationship + 3 years or the regulatory retention requirement.
347|
348|> **Why a Named Team Instead of "We'll Pull People In"**
349|>
350|> Naming the team in advance, with a roster, a trigger, and a 4-hour clock, converts vendor compromise from a panicked phone-tree exercise into a procedure. The first SolarWinds-class event tests every assumption about your TPRM program; SCCT is how that test doesn't surprise you.
351|
352|---
353|
354|## 16. Continuous Monitoring and Re-Assessment
355|
356|### 16.1 Automated Monitoring Signals
357|
358|CERG continuously monitors the vendor landscape using automated signals. The following sources are integrated into the TPRM monitoring pipeline:
359|
360|| **Signal Type** | **Source** | **Frequency** | **Action on Alert** |
361||---|---|---|---|
362|| Security ratings service | Third-party security ratings provider | Continuous | Alert Vendor Risk Analyst for any score drop > 50 points or below tier threshold |
363|| Dark web monitoring | Threat intelligence platform | Continuous | Alert if organization credentials, source code, or PII attributed to a vendor appear on dark web sources |
364|| Certificate transparency logs | CT log monitors | Daily | Alert on anomalous certificate issuance for vendor domains |
365|| Vendor breach notifications | Direct notification, media monitoring, ISAC feeds | Continuous | Trigger SCCT activation per Section 15 if the breach affects services consumed by the organization |
366|| Sanctions and adverse media | Sanctions list providers, news monitoring | Weekly | Alert Vendor Risk Analyst; trigger Country Risk Register review if jurisdiction-related |
367|| Financial health indicators | Business credit monitoring | Quarterly | Alert for vendors with deteriorating financial posture (downgrade, bankruptcy filing, going concern opinion) |
368|
369|### 16.2 Periodic Re-Assessment Triggers
370|
371|Vendors are re-assessed on the following cadence based on tier:
372|
373|| **Tier** | **Re-Assessment Cadence** | **Trigger Events (override cadence)** |
374||---|---|---|
375|| T1 (Critical) | Annual | Vendor breach, material change in service, M&A activity, regulatory action against vendor |
376|| T2 (High) | Annual | Vendor breach, material change in service, M&A activity |
377|| T3 (Moderate) | 24 months | Vendor breach affecting the service consumed |
378|| T4 (Low) | Renewal-driven | Re-assess at contract renewal; trigger if service scope expands |
379|| T5 (Business Default) | Renewal-driven | Re-assess if usage crosses into T4 territory |
380|
381|### 16.3 Vendor Performance Metrics
382|
383|The Vendor Risk Analyst tracks the following metrics for each T1 and T2 vendor:
384|
385|| **Metric** | **Description** | **Review Cadence** |
386||---|---|---|
387|| Evidence currency | % of required evidence artifacts that are current (within validity period) | Quarterly |
388|| Assessment completion timeliness | Whether re-assessments complete within the scheduled window | Quarterly |
389|| Finding remediation velocity | Mean time from finding issuance to closure, by severity | Quarterly |
390|| SCCT activation frequency | Number of SCCT activations involving the vendor | Quarterly |
391|| Contractual compliance | Adherence to security obligations, RTO/RPO commitments, and notification SLAs | Annual |
392|
393|### 16.4 Escalation Paths for Deteriorating Vendor Posture
394|
395|| **Condition** | **Escalation** | **Action** |
396||---|---|---|
397|| Security rating drops below tier threshold | Vendor Risk Analyst | Immediate review; request remediation plan from vendor within 10 business days |
398|| Vendor breach with potential organizational impact | SCCT Lead per Section 15 | Activate SCCT; assess containment and exposure |
399|| Critical finding open > 90 days without remediation plan | Vendor Risk Analyst → Governance Pillar Leader | Escalate to vendor executive; consider contract remedies |
400|| Vendor refuses to provide required evidence | Vendor Risk Analyst → Engineering Pillar Leader → CISO | Risk acceptance required; if unacceptable, initiate vendor transition planning |
401|| Financial distress indicators | Vendor Risk Analyst → Governance Pillar Leader | Develop contingency plan; identify alternative vendors |
402|
403|### 16.5 Integration with Approved Provider Catalog
404|
405|Continuous monitoring results directly affect the Approved Provider Catalog (APC) status values:
406|
407|- **Green (Approved)**: All monitoring signals within acceptable thresholds; evidence current.
408|- **Amber (Conditional)**: One or more signals outside Green threshold; remediation plan accepted. Automatic review at 90 days.
409|- **Red (Restricted)**: Critical finding or breach unresolved; new engagements restricted until status returns to Amber or Green.
410|- **Black (Prohibited)**: Vendor determined to pose unacceptable risk; existing services transitioned off per the offboarding procedure.
411|
412|### 16.6 Integration with Threat Intelligence
413|
414|Vendor monitoring is integrated with [CERG-PRC-TI-001](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) for threat intelligence specific to vendors:
415|
416|- The Threat Intelligence Analyst produces a **Vendor Risk Note** (per PRC-TI-001 §6.5) when threat intelligence reveals TTPs, CVEs, or campaign activity relevant to a vendor in the APC.
417|- Vendor-specific IOCs from threat intelligence are deployed to detection tooling per PRC-TI-001 §4.6.
418|- Quarterly threat briefings to the Vendor Risk Analyst summarize the threat landscape affecting the vendor portfolio.
419|
420|### 16.7 Vendor Offboarding
421|
422|When a vendor relationship ends, a structured offboarding process ensures access is revoked, data is retrieved or destroyed, and residual obligations are met.
423|
424|#### Offboarding Triggers
425|
426|| **Trigger** | **Description** |
427||---|---|
428|| Contract expiration | Normal end of contract term; vendor not renewed |
429|| Termination for cause | Vendor breach of contract, security incident, or performance failure |
430|| Vendor bankruptcy / dissolution | Vendor ceases operations |
431|| Strategic replacement | Organization transitions to an alternative vendor |
432|
433|#### Offboarding Checklist
434|
435|| **Step** | **Action** | **Owner** | **Timing** |
436||---|---|---|---|
437|| 1 | Notify vendor; confirm effective date | Business Sponsor | Immediately |
438|| 2 | Disable all vendor user accounts | Identity Engineer | Effective date or within 24 hours |
439|| 3 | Revoke vendor API keys, OAuth grants, service principals | Identity Engineer / Cloud Security Engineer | Effective date |
440|| 4 | Rotate shared secrets vendor had access to | Cryptography Engineer | Within 5 business days |
441|| 5 | Deauthorize SSO / federation | Identity Engineer | Effective date |
442|| 6 | Remove vendor from Approved Provider Catalog (status = Offboarded) | Vendor Risk Analyst | Within 5 business days |
443|| 7 | Confirm data retrieval or destruction per contract | Business Sponsor + Legal | Per contract |
444|| 8 | Update TPRM record | Vendor Risk Analyst | Within 10 business days |
445|
446|#### Post-Termination
447|
448|Surviving contractual clauses (confidentiality, data handling, audit rights) remain in effect. Evidence is retained per [CERG-PRC-AUD-001](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md). Offboarding completion is signed off by the Vendor Risk Analyst and Business Sponsor.
449|
450|### 16.8 Fourth-Party Risk Management
451|
452|Fourth-party risk arises when a critical vendor relies on subcontractors (sub-processors) the organization does not have a direct relationship with.
453|
454|#### Disclosure Requirements
455|
456|- T1 and T2 vendors must disclose all critical sub-processors
457|- Vendors must notify the organization of sub-processor changes at least 30 days before the change
458|- The organization reserves the right to object; the vendor must provide an alternative or allow contract termination without penalty
459|
460|#### Evidence for Critical Sub-Processors
461|
462|| **Evidence** | **When Required** |
463||---|---|
464|| SOC 2 Type II report | Sub-processors hosting or processing the organization's data |
465|| ISO 27001 certification | Acceptable alternative for international sub-processors |
466|| Inheritance evidence | Vendor's own assessment, if methodology is reviewed and approved |
467|
468|#### Concentration Risk
469|
470|The Vendor Risk Analyst monitors for multiple vendors relying on the same sub-processor. If a single sub-processor supports ≥ 3 T1/T2 vendors, a formal concentration risk assessment is conducted.
471|
472|---
473|
474|### 16.9 Business Continuity and Disaster Recovery (BCDR) for Vendors
475|
476|Critical and high-tier vendors must demonstrate BCDR capability proportional to the criticality of the service they provide.
477|
478|#### BCDR Requirements by Tier
479|
480|| **Tier** | **BCDR Requirement** | **Evidence** |
481||---|---|---|
482|| T1 (Critical) | Documented BCDR plan; RTO ≤ 4 hours; RPO ≤ 1 hour; annual functional BCDR test | BCDR plan summary; test results |
483|| T2 (High) | Documented BCDR plan; RTO ≤ 24 hours; RPO ≤ 4 hours; annual tabletop or functional test | BCDR plan summary; test results |
484|| T3 (Moderate) | BCDR plan or equivalent; RTO/RPO appropriate to service | BCDR plan acknowledgment |
485|| T4 (Low) | BCDR capability acknowledged in contract | Contractual commitment |
486|| T5 (Business Default) | None required beyond standard terms | - |
487|
488|#### RTO/RPO Expectations
489|
490|RTO (Recovery Time Objective) and RPO (Recovery Point Objective) expectations are set based on the organization's dependency on the vendor:
491|
492|- If the organization's own Tier 1 service depends on the vendor, the vendor's RTO must be ≤ the organization's RTO for that service.
493|- If the vendor processes regulated data (CUI, SOX), RPO must be ≤ 1 hour.
494|- RTO/RPO commitments are documented in the contract and reviewed at each vendor re-assessment.
495|
496|#### BCDR Assessment
497|
498|During vendor assessment, the Vendor Risk Analyst evaluates:
499|- Does the vendor have a documented BCDR plan?
500|- Has the plan been tested? When? What was the outcome?
501|- Are RTO/RPO commitments compatible with the organization's requirements?
502|- Does the vendor's BCDR plan account for dependencies on its own critical sub-processors?
503|
504|Assessment results are recorded in the TPRM tool and reviewed at each re-assessment cycle.
505|
506|### 16.10 Metrics
507|
508|| **KPI** | **Formula** | **Source** | **Refresh** | **Green** | **Amber** | **Red** |
509||---|---|---|---|---|---|---|
510|| Vendors assessed on time | % of vendors with assessment completed within scheduled window | TPRM tool | Quarterly | ≥ 95% | 85–94% | < 85% |
511|| Average assessment time | Mean calendar days from assessment start to completion | TPRM tool | Quarterly | ≤ 30 days | 31–45 days | > 45 days |
512|| Vendors by tier | Count of active vendors per tier (T1–T5) | TPRM tool | Monthly | - | - | - |
513|| Active exceptions | Count of open vendor-related risk exceptions | Risk register | Monthly | 0 | 1–5 | > 5 |
514|| Vendor risk trend | % of vendors with improving / stable / declining risk posture | TPRM tool | Quarterly | ≥ 80% stable or improving | 60–79% | < 60% |
515|| Evidence currency | % of T1/T2 vendors with all required evidence current | TPRM tool | Monthly | ≥ 95% | 85–94% | < 85% |
516|| SCCT activation frequency | Count of SCCT activations | SCCT log | Quarterly | 0 | 1 | ≥ 2 |
517|| Fourth-party concentration | Count of sub-processors supporting ≥ 3 T1/T2 vendors | TPRM tool | Quarterly | 0 | 1 | ≥ 2 |
518|
519|## 17. Regulatory and Framework Alignment Summary
520|
521|| **Regulation / Framework** | **Where in This Procedure** |
522||---|---|
523|| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SR family | All sections |
524|| NIST 800-161r1 | All sections; especially 11–15 |
525|| [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GV.SC) | Sections 2–6, 15 |
526|| ISO 27036 | Sections 5, 8, 9 |
527|| DFARS 252.204-7012 / [CMMC L2](https://dodcio.defense.gov/CMMC/) | Sections 13, 14 |
528|| NERC-CIP CIP-013 | Section 12 |
529|| FedRAMP / FedRAMP equivalency | Section 14 |
530|| NTIA SBOM minimum elements | Section11 |
531|| SOX ITGC | Cross-cutting; vendor SOC 1 reuse where applicable |
532|
533|---
534|
535|## 18. Document Control
536|
537|| | |
538||---|---|
539|| **Document ID** | CERG-PRC-TPRM-001 |
540|| **Version** | 1.0 |
541|| **Approved By** | Cyber Risk Pillar Leader (Vendor Risk) · CISO endorsement |
542|| **Next Review** | Annual / TPRM platform change |
543|| **Change Log** | 1.0 - Initial publication. Tiering, evidence by tier, shared responsibility, international access denial-by-default, SBOM, CIP-013, CUI flow-down, FedRAMP equivalency, SCCT.