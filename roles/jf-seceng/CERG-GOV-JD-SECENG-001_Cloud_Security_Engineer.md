| | |
|---|---|
| **Document ID** | CERG-GOV-JD-SECENG-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

---

# Cloud Security Engineer

**Job Family:** JF-SECENG — Security Engineering
**Job Level Range:** L1-L4 (CERG Grade S1-S4)
**CERG Canonical Role:** Cloud Security Engineer ([CERG-GOV-OM-001](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1)

---

## 1. Role Summary

The Cloud Security Engineer defines cloud and SaaS platform security requirements and reference patterns: infrastructure-as-code content, cloud posture requirements and test cases, landing-zone design, cloud network security, and the security requirements for email and messaging platforms where delivered as SaaS. The engineer is the organization's authority on what a secure cloud deployment looks like, and they validate whether first-line platform owners and their providers delivered it. First-line service owners and operators run the cloud, SaaS, and messaging platforms and their posture tooling.

## 2. NICE Workforce Framework Mapping

| Mapping Level | NICE Work Role | NICE Work Role ID | NICE Work Role Category |
|---------------|----------------|-------------------|-------------------------|
| Primary | Security Architect | SP-ARC-001 | SP |

**NICE Work Role Definition:** See [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) for the official NICE Work Role definition and complete CERG-to-NICE mapping. The NICE TKS database is available at https://www.nist.gov/nice/framework/.

## 3. Job Family & Level Placement

| Family | JF-SECENG — Security Engineering |
|--------|---------------------------|
| Level Range | L1 through L4 |
| CERG Grade Range | S1-S4 |
| Terminal Grade | S4 — see [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) for details |
| Track | SME |

## 4. Key Responsibilities

### 4.1 Core Responsibilities (All Grades)

- Design and maintain cloud security reference architecture, including landing zone controls, network segmentation, identity integration, and logging.
- Define CSPM policy and posture requirements; review first-line triage output and validate remediation evidence. First-line operators run CSPM and triage its alerts.
- Review infrastructure-as-code (Terraform, CloudFormation, Bicep) for security adequacy before deployment, and independently test the deployed posture in approved scope.
- Define SaaS, email, messaging, and collaboration security requirements and configuration baselines; the first-line platform owner configures and operates the tenants.
- Define shadow-IT and shadow-AI discovery requirements and review first-line cloud-signal and CASB output; the first-line operator runs the discovery tooling.
- Partner with IT and DevOps teams, and supply candidate policy-as-code content so requirements are implementable; first-line pipeline owners embed and operate the controls.
- Author and maintain the technical content of the IT / Cloud / SaaS Security Standard, including its cloud-specific requirements; Governance holds approval authority.
- Support architecture review for projects with cloud components, providing cloud-specific threat and control analysis.
- Provide cloud-specific technical input to the standing Incident Response team during cloud incident investigation and response.

### 4.2 Grade-Level Responsibility Differentiation

How responsibility grows by grade is set out in [JA-001 §7](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) (Role-to-Grade Mapping). Grade definitions (S1-S4 SME Track, M1-M4 Management Track) and the leveling dimensions are held in [CERG-GOV-JA-001](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) §4-5. For the behavioral anchors at each grade, see [CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md).

## 5. Required Knowledge, Skills, and Abilities (KSAs)

### 5.1 Domain Expertise

- Deep expertise in at least one major cloud platform (AWS, Azure, GCP); working knowledge of a second - Infrastructure-as-code proficiency: Terraform, CloudFormation, or equivalent - Cloud-native security tooling: CSPM, CWPP, CIEM, cloud network security - Identity and access management in cloud contexts: IAM, federation, service accounts, workload identity - Container and serverless security - SaaS security assessment and configuration management - Scripting and automation (Python, PowerShell, or equivalent)

### 5.2 Technical Skills

The role's technical skills come from the original JD-001 content reproduced here (see §5.1 Domain Expertise). The remaining technical skill definitions, aligned to NICE Skill Statements, are in [JF-002](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md).

### 5.3 CERG-Specific Knowledge

The CERG-specific knowledge requirements for this role sit in [OM-001 §6](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) (Canonical Role Roster) and [RAC-001 §7](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) (Role Descriptions). The full list of relevant standards and procedures is in §12 (Related CERG Documents).

## 6. NICE TKS Statement References

Drawn from the NIST NICE Framework v2.2.0 Work Role [DD-WRL-001 — Cloud Security Engineer primary mapping] and filtered for relevance to this CERG role, these Task, Knowledge, and Skill statements follow. The full TKS database lives at https://www.nist.gov/nice/framework/.

| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |
|---------------|-------------|-------------------|------------------------|
| Task | T1010 | Communicate enterprise information technology architecture | Core work activity for this NICE Work Role |
| Task | T1027 | Integrate organizational goals and objectives into security architecture | Core work activity for this NICE Work Role |
| Task | T1077 | Assess the organization's cybersecurity architecture | Core work activity for this NICE Work Role |
| Task | T1100 | Configure network hubs, routers, and switches | Core work activity for this NICE Work Role |
| Task | T1101 | Optimize network hubs, routers, and switches | Core work activity for this NICE Work Role |
| Knowledge | K0689 | Knowledge of network infrastructure principles and practices | Foundational knowledge for this role |
| Knowledge | K0742 | Knowledge of identity and access management (IAM) principles and practices | Foundational knowledge for this role |
| Knowledge | K0915 | Knowledge of network architecture principles and practices | Foundational knowledge for this role |
| Knowledge | K0055 | Knowledge of microprocessors | Foundational knowledge for this role |
| Knowledge | K0674 | Knowledge of computer networking protocols | Foundational knowledge for this role |
| Skill | S0418 | Skill in applying secure network architectures | Core capability for this role |
| Skill | S0657 | Skill in implementing Public Key Infrastructure (PKI) encryption | Core capability for this role |
| Skill | S0383 | Skill in analyzing an organization's enterprise information technology architecture | Core capability for this role |
| Skill | S0428 | Skill in designing architectures | Core capability for this role |
| Skill | S0465 | Skill in identifying critical infrastructure systems | Core capability for this role |

> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role (SP-ARC-001 → DD-WRL-001) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.

## 7. Typical Qualifications

### 7.1 Education

- 3-12+ years in cybersecurity or cloud engineering, with increasing cloud security focus - Bachelor's degree in a relevant technical field or equivalent experience - Relevant certifications: AWS Certified Security, Azure Security Engineer, CCSP, or equivalent

### 7.2 Certifications

[TRN-001 §3](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) (Certification Matrix) names the certifications for this role. The matrix sorts them into Required, Recommended, and Aspirational, per role and grade.

### 7.3 Experience

Typical experience ranges by grade are in [JA-001 §4-5](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). Education requirements are in §7.1 (Education) above.

## 8. Key Performance Indicators (KPIs)

[MTR-001](../../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (Metrics, Dashboard, and CISO/Board Reporting) carries the KPIs for this role. [PERF-001](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) documents how KPIs are allocated by job family and sets the grade-level thresholds. The per-role JD document structure defined by [JF-001](../CERG-GOV-JF-001_Job_Families_Overview.md) holds each role's evaluation criteria.

## 9. Competency Expectations by Grade

Competency expectations for this role track the Engineering pillar behavioral anchors in [CERG-GOV-CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md). Each cell names observable behavior that demonstrates the competency at that grade. The anchors are cumulative: an L3 expectation includes the L1 and L2 anchors.

| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |
|-----------------------------|----------------|----------------|----------------|----------------|
| Technical Depth | Executes assigned engineering tasks (IaC module, configuration change, architecture review checklist item) from established procedures. Recognizes when a task result does not match expected output and escalates with context. Learning the organization's technology stack: can name the major platforms, their purpose, and their security control points. | Owns a technology domain (e.g., AWS security, Azure AD, Kubernetes admission control). Designs and implements security controls independently within that domain. Performs architecture reviews in their domain and produces findings that require minimal rework from the reviewer. Authors and improves procedures for their domain. | Shapes the organization's technical security strategy in their domain. Designs reference architectures adopted by other engineers. Anticipates how changes in the technology stack will affect security posture before they land. Performs architecture reviews across domains with credibility. | Sets the technical bar for the entire Engineering pillar. Called upon for the hardest cross-domain problems. Represents the organization's engineering position to vendors, industry working groups, and regulators. Can step into any Engineering domain and contribute meaningfully within days. |
| Cross-Pillar Fluency | Understands that Risk and Governance pillars exist and can describe their basic functions. Reads vulnerability reports and compliance findings that affect their work. | Consumes Risk pillar output (vulnerability data, threat intelligence) and incorporates it into engineering decisions. Understands what Governance needs from Engineering for an audit and provides it without being chased. | Anticipates what Risk and Governance will need from an engineering decision before they ask. Participates in cross-pillar working groups as the Engineering voice. Can represent Engineering's position to a regulator or auditor without a Governance handler. | Operates fluently across all three pillars. Contributes to Risk assessments and Governance standards as a peer, not a guest. Is the person a pillar leader calls when a cross-pillar problem does not fit any procedure. |
| Risk Judgment | Follows the risk taxonomy when documenting findings. Can distinguish between a configuration drift alert that needs a ticket and one that needs an incident response page. | Independently assesses the severity and likelihood of findings in their domain. Assigns risk ratings that are consistent with the taxonomy and rarely adjusted by a senior reviewer. | Evaluates risk across domains and articulates the business impact in terms an executive can act on. Identifies compensating controls that reduce risk below what a pure vulnerability score would suggest. | Shapes the organization's risk appetite through technical judgment. Called upon by the CISO for independent risk assessments on material decisions. Their risk evaluation carries the same weight as a pillar leader's. |
| Communication | Writes clear ticket updates and status reports. Explains a technical finding to their immediate team without ambiguity. | Writes architecture review findings that a project manager or business owner can understand and act on. Presents technical topics to their pillar. Authors clear, usable procedures. | Represents Engineering in cross-functional forums with credibility. Writes decision memos that frame technical options in business terms. Presents to senior leadership and external stakeholders. | Communicates complex technical risk to the CISO, the board (as requested), regulators, and industry peers. Writes the organization's public technical positions. Represents the organization at conferences and in industry working groups. |
| Operational Discipline | Follows procedures correctly. Updates tickets and documentation when work is complete. Meets assigned SLAs. Admits when they do not know something rather than guessing. | Owns operational SLAs for their domain work streams. Ensures evidence is collected and stored per the evidence procedure. Improves procedures when they find gaps. Their work is consistently auditable without retroactive cleanup. | Designs procedures that are operationally sustainable, not just technically correct. Ensures the evidence trail for their domain is audit-ready at all times. Identifies and eliminates toil: automates repetitive operational tasks. | Sets operational standards for the pillar. Defines what "good" looks like for procedure compliance, evidence quality, and SLA management. Holds the pillar accountable to its own operational commitments. |
| Influence and Mentorship | Actively learns from senior engineers. Asks good questions. Shares what they learn with peers. | Onboards new Specialists without assistance. Peer-reviews code and configurations with constructive feedback. Their technical opinion is sought by other engineers in their domain. | Mentors Specialists and Sr. Specialists across domains. Leads technical initiatives without formal authority. Their architectural recommendations are rarely overruled. | Shapes the development of the entire Engineering team. Sets the technical bar through their own work and their mentoring. Influences hiring profiles, team composition, and organizational design. |
| Compliance and Regulatory Literacy | Knows which regulatory frameworks apply to their organization. Can describe the security implications of the major ones (NERC-CIP, CMMC, SOX) at a high level. | Understands the specific regulatory requirements that affect their domain. Can explain to an auditor how a control they implemented satisfies a regulatory requirement. | Anticipates regulatory implications of engineering decisions. Advises project teams on compliance requirements before design is complete. Represents Engineering in regulatory audits without a Governance chaperone. | Contributes to the organization's regulatory strategy. Engages with regulators on technical matters. Shapes standards so that compliance is a byproduct of good engineering, not a separate activity. |
| Continuous Learning | Completes assigned training. Pursues foundational certifications relevant to their domain. Learns the organization's technology stack. | Maintains current certifications. Stays current on developments in their domain. Shares what they learn with the team. | Pursues advanced certifications. Contributes to the team's knowledge base through documented research, brown-bag sessions, or internal training. Evaluates new technologies for organizational adoption. | Recognized externally for expertise. Shapes the organization's technology and certification roadmap. The person other engineers go to when they need to understand an emerging technology or threat. |

> **Full Reference:** See [CERG-GOV-CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) for the complete competency model, including the Management Track addendum (§7) and guidance on using the model for hiring, development, and promotion (§8).

## 10. Success Profile

A Cloud Security Engineer is successful when the requirements and reference patterns they produce change what first-line teams deploy, and when independent validation establishes whether first-line evidence supports the stated requirement and design, or exposes a gap. Key indicators: landing-zone and IaC requirements are implementable as written and adopted without a standing exception list; posture requirements catch the misconfiguration classes the standard names; a validated claim states its assessor, scope, and evidence period, and does not outrun the evidence behind it; a triage disposition changes when challenged with evidence; project teams seek cloud security input before the design is fixed. Success is not measured by green posture, findings triaged within SLA, or pipeline adoption, which describe the first-line owners and operators who run the platforms.

## 11. Career Path

### 11.1 Within-Family Progression

Within JF-SECENG, the Security Engineering level ladder in [JF-001 §9.1](../CERG-GOV-JF-001_Job_Families_Overview.md#91-jf-seceng--security-engineering-levels) runs L1 Associate Engineer/S1, L2 Engineer/S2, L3 Senior or Staff Engineer/S3, and L4 Principal Engineer/S4. Promotion evidence should show increasing autonomy in secure design and implementation, ownership of engineering work streams, authorship or improvement of standards and reference architectures, cross-pillar influence, and mentoring of less experienced engineers. [JA-001 §4](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md#4-sme-progression-grade-definitions) holds the grade definitions and progression dimensions.

---

### 11.2 Cross-Family Movement

Cross-family movement options are in the [Family-to-Family Career Lattice (JF-001 §4)](../CERG-GOV-JF-001_Job_Families_Overview.md#4-family-to-family-career-lattice). The Left-Right Knowledge Model ([FRM-001 §9.2](../../governance/CERG-GOV-FRM-001_CERG_Framework.md)) and cross-training expectations ([OM-001 §10.4](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md)) turn that movement into practice.

### 11.3 Management Track Option

At L3+ (SME track), a Management track option may be available per [CERG-GOV-JA-001](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) §8.1 (SME to Management Transition). The readiness markers: junior team members come to them for guidance, they lead cross-functional initiatives without formal authority, and they communicate clearly with non-technical stakeholders. The move is a change of track, not a promotion in grade — an S3 Advisor who becomes an M1 Manager carries their technical credibility into the role. [CERG-GOV-CMP-001](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) §7 defines the management competencies. See [CERG-GOV-JA-001](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) §5 for Management grade definitions (M1-M4) and §9 (Span of Control and Team Design) for when to create a management role.

## 12. Related CERG Documents

| Document | ID | Relevance |
|----------|-----|-----------|
| Operating Model | [`CERG-GOV-OM-001`](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role name; pillar structure |
| RACI Instrument | [`CERG-GOV-RAC-001`](../../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | This role's accountability assignments |
| Job Architecture | [`CERG-GOV-JA-001`](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Grade definitions; progression criteria |
| Competency Model | [`CERG-GOV-CMP-001`](../../governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Full behavioral anchors |
| Performance Framework | [`CERG-GOV-PERF-001`](../../governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Performance review cadence and calibration |
| Training Framework | [`CERG-GOV-TRN-001`](../../governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Certification matrix |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-JD-SECENG-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST SP 800-181r1 (NICE) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed workforce |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Extracted from monolithic JD-001 into enhanced per-role format with NICE mapping, KPI sections, and competency anchor sections. |
| 1.1 | 2026-10-28 | Engineering Pillar Leader | Recast per-activity responsibilities for the second-line boundary: cloud and OT architecture, requirements, review, and validation remain with Engineering; first-line owners and operators run CSPM, CASB, discovery, production configuration, and remediation. |

### Review Triggers

- Change to this role's definition in [CERG-GOV-OM-001](../../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1
- Change to this role's NICE Work Role mapping in JF-002
- Change to this role's grade range in [CERG-GOV-JA-001](../../governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) §7
- Direction from the CISO

Governance owns this document. Reviews begin with the Governance Pillar Leader (Policy & Standards), who runs the revision cycle and obtains approval for every change.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Job Families Overview | [`CERG-GOV-JF-001`](../CERG-GOV-JF-001_Job_Families_Overview.md) | Family structure and level definitions |
| NICE Crosswalk | [`CERG-GOV-JF-002`](../CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Work Role mapping |
