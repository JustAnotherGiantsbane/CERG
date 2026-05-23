# CERG Document Truncation Remediation Work Plan

## Purpose

This file records all markdown documents in the CERG repository that were identified as **truncated or incomplete** during a systematic completeness review. Each entry describes the affected file, the precise location where content ends abruptly, and the remediation action required.

An LLM performing remediation should:
1. Open the affected file.
2. Locate the truncation point (see `truncation_point` for each item).
3. Reconstruct and append the missing content following the document's established structure and style (see `CERG-GOV-STY-001` for authoring conventions).
4. Ensure the document ends with a complete `## Document Control` section matching the pattern used by completed documents in the repo.
5. Commit the fix with an entry in the document's Revision History table.

---

## Truncated Documents

---

### 1. `CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-MTR-001 |
| **Section affected** | §9 Cadence and Ownership |
| **Severity** | High — document ends mid-table-row; missing Document Control section |
| **Truncation point** | Last line: `\| Board read-out slice \| Quarterly \| CI` |
| **Expected missing content** | Completion of the §9 cadence/ownership table (at minimum one more row: owner cell for "Board read-out slice" and likely 1–2 additional rows); a `Document Control` section with metadata, revision history, review triggers, and related documents table — following the standard template used by all other CERG GOV instruments. |

---

### 2. `CERG-STD-AC-001_Access_Management_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-AC-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; likely missing 1–3 rows and Document Control section |
| **Truncation point** | Last line: `\| CUI Handling Standard \| [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handli` |
| **Expected missing content** | Completion of the CUI Handling Standard row link text and relationship cell; additional related document rows (at minimum: `CERG-PRC-VM-001`, `CERG-PRC-RM-001`, `CERG-GOV-CAT-001`); full `Document Control` section. |

---

### 3. `CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-CFG-001 |
| **Section affected** | §11.1 Drift Detection |
| **Severity** | High — body text ends mid-sentence; sections §11.2 (Exception Handling) and Document Control appear entirely absent |
| **Truncation point** | Last line: `- Material drift on a Critical/High asset is also recorded in the risk register per ` |
| **Expected missing content** | Completion of the sentence (cross-reference to `CERG-PRC-RM-001`); §11.2 Exception Handling content; full Document Control section. |

---

### 4. `CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-CR-001 |
| **Section affected** | §11 Regulatory and Framework Alignment Summary |
| **Severity** | High — regulatory alignment table cut after partial first row; Document Control section absent |
| **Truncation point** | Last line: `\| [NIST 800-53r5] SC family \| SC-8, SC-12, SC-13, SC-17, SC-28 \| All s` |
| **Expected missing content** | Completion of the first table row's "Where in This Standard" cell; additional rows for NIST 800-171r3, NIST CSF 2.0, NERC-CIP CIP-011, CMMC SC domain, and ISO 27001 SC equivalents; full Document Control section. |

---

### 5. `CERG-STD-CUI-001_CUI_Handling_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-CUI-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| Vulnerability Management Procedure \| [CERG-PRC-VM-001](CERG-PRC-VM-001_Vulne` |
| **Expected missing content** | Completion of the VM Procedure row link and relationship cell; remaining related document rows (at minimum: `CERG-PRC-RM-001`, `CERG-PRC-TPRM-001`, `CERG-GOV-CAT-001`); full Document Control section. |

---

### 6. `CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-IT-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| Access Management Standard \| [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) \| Pe` |
| **Expected missing content** | Completion of the Access Management Standard relationship cell; remaining related document rows; full Document Control section. |

---

### 7. `CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-LM-001 |
| **Section affected** | §12 Privileged Session Monitoring |
| **Severity** | High — §12 ends mid-sentence; Document Control section absent |
| **Truncation point** | Last line: `- Session anomalies (long-running, off-hours, off-jurisdiction) raise` |
| **Expected missing content** | Completion of the sentence (likely references to alerting thresholds and escalation); any remaining §12 sub-bullets; full Document Control section. |

---

### 8. `CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-OT-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| NERC-CIP Operational Package \| [CERG-PLN-CIP-001]...\| OT/CIP operational binder - contains the NERC-CIP Evidence Library Procedure (formerly \`CERG-GOV-CIP-001\`), OT Vulnerability Management Procedu` |
| **Expected missing content** | Completion of the NERC-CIP Operational Package relationship cell; remaining related document rows; full Document Control section. |

---

### 9. `CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-RES-001 |
| **Section affected** | §12 Regulatory and Framework Alignment Summary |
| **Severity** | High — regulatory alignment table cut after partial first row; Document Control section absent |
| **Truncation point** | Last line: `\| [NIST 800-53r5] CP family \| CP-2, CP-4` |
| **Expected missing content** | Completion of the first table row's "Where in This Standard" cell; additional rows for NIST 800-171r3, NIST CSF 2.0 RECOVER, NERC-CIP CIP-009, CMMC RE domain, ISO 27001 A.17 equivalents; full Document Control section. |

---

### 10. `CERG-PRC-AC-002_Access_Management_Runbook.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-AC-002 |
| **Section affected** | RACI or roles table near end of document |
| **Severity** | High — table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| HR \| JML triggers; data quality in HRIS. \|§\| Pr` |
| **Expected missing content** | Completion of subsequent role row(s) (likely Procurement or Privacy); full Document Control section. |

---

### 11. `CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-AR-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut at header separator; all rows absent |
| **Truncation point** | Last line: `\|---\|---\|---\|§\| CM` |
| **Expected missing content** | All related document rows starting with the partial `CM` row (likely `CERG-GOV-CB-001` or similar); full Document Control section. |

---

### 12. `CERG-PRC-AV-001_Adversarial_Validation_Procedure.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-AV-001 |
| **Section affected** | §12 Roles and Responsibilities / Document Control |
| **Severity** | High — last table row missing closing pipe; Document Control section entirely absent |
| **Truncation point** | Last line: `\| CISO \| Approves Red-Team Charters and high-impact / cloud / OT engagements.` |
| **Expected missing content** | Closing `\|` on the CISO row; full Document Control section (metadata, revision history, review triggers, related documents). |

---

### 13. `CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-RM-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| Grid and Control System Standard \| [CERG-STD-OT-001]...) \| OT risk and CIP deviation overlay \|§\| I` |
| **Expected missing content** | Completion of subsequent related document rows starting with partial `I` (likely ISO package or IR plan); full Document Control section. |

---

### 14. `CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-TPRM-001 |
| **Section affected** | Cadence/frequency table near end of document |
| **Severity** | High — table row cut mid-cell; Document Control section absent |
| **Truncation point** | Last line: `\| Risk register reconciliation \| Quarterly \| Qua` |
| **Expected missing content** | Completion of the risk register reconciliation row; remaining table rows; full Document Control section. |

---

### 15. `CERG-PRC-VM-001_Vulnerability_Management_Procedure.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-VM-001 |
| **Section affected** | Regulatory alignment or framework crosswalk table near end of document |
| **Severity** | High — table row cut mid-cell; Document Control section absent |
| **Truncation point** | Last line: `\| Prioritization (CVSS / KEV) \| ID.RA \| RA-5(1), RA-5(` |
| **Expected missing content** | Completion of the Prioritization row (additional NIST control IDs, 800-171 ref, NERC-CIP, CMMC); remaining table rows; full Document Control section. |

---

### 16. `CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-CIP-001 |
| **Section affected** | Body prose section near end of document |
| **Severity** | High — body text cut mid-sentence; Document Control section absent |
| **Truncation point** | Last line: `A risk register entry tracks the CIP-015 readiness gap until INSM coverage mat` |
| **Expected missing content** | Completion of sentence (likely: "...matures"); any remaining section content addressing CIP-015 INSM posture; full Document Control section. |

---

### 17. `CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-CUI-001 |
| **Section affected** | Cadence/activity table near end of document |
| **Severity** | High — table row cut mid-cell; Document Control section absent |
| **Truncation point** | Last line: `\| POA&M update \| Monthly \|§\| 800-17` |
| **Expected missing content** | Completion of the POA&M update row; remaining table rows (likely referencing 800-171r3 requirements); full Document Control section. |

---

### 18. `CERG-PLN-IR-001_Incident_Response_Plan.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-IR-001 |
| **Section affected** | Related Documents table (end of document) |
| **Severity** | High — Related Documents table cut mid-row; Document Control section absent |
| **Truncation point** | Last line: `\| CUI Handling Standard \| [CERG-STD-C` |
| **Expected missing content** | Completion of the CUI Handling Standard row; remaining related document rows; full Document Control section. |

---

### 19. `CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-PLN-SOX-001 |
| **Section affected** | Roles and Responsibilities table |
| **Severity** | High — table row cut mid-cell; Document Control section absent |
| **Truncation point** | Last line: `\| CERG - Engineering / Risk / Identity \| Operate the underlying controls; provide evidence on reque` |
| **Expected missing content** | Completion of the Engineering/Risk/Identity row; any additional role rows (e.g., Internal Audit, Finance); full Document Control section. |

---

### 20. `CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md`

| Field | Value |
|---|---|
| **Document ID** | CERG-TMPL-RM-001 |
| **Section affected** | Cadence/reporting table near end of document |
| **Severity** | High — table row cut mid-cell; Document Control section absent |
| **Truncation point** | Last line: `\| Regulatory Posture publication \| Quarterly \| Governance Domain O` |
| **Expected missing content** | Completion of the Regulatory Posture publication row owner; any remaining table rows; full Document Control section. |

---

## Summary

| # | File | Truncation Location | Status |
|---|---|---|---|
| 1 | `CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` | §9 table mid-row | Open |
| 2 | `CERG-STD-AC-001_Access_Management_Standard.md` | Related Documents mid-row | Open |
| 3 | `CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md` | §11.1 mid-sentence | Open |
| 4 | `CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md` | §11 table mid-row | Open |
| 5 | `CERG-STD-CUI-001_CUI_Handling_Standard.md` | Related Documents mid-row | Open |
| 6 | `CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md` | Related Documents mid-row | Open |
| 7 | `CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md` | §12 mid-sentence | Open |
| 8 | `CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md` | Related Documents mid-row | Open |
| 9 | `CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md` | §12 table mid-row | Open |
| 10 | `CERG-PRC-AC-002_Access_Management_Runbook.md` | RACI table mid-row | Open |
| 11 | `CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` | Related Documents mid-row | Open |
| 12 | `CERG-PRC-AV-001_Adversarial_Validation_Procedure.md` | §12 table + missing Doc Control | Open |
| 13 | `CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md` | Related Documents mid-row | Open |
| 14 | `CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` | Cadence table mid-row | Open |
| 15 | `CERG-PRC-VM-001_Vulnerability_Management_Procedure.md` | Framework crosswalk table mid-row | Open |
| 16 | `CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md` | Body prose mid-sentence | Open |
| 17 | `CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md` | Cadence table mid-row | Open |
| 18 | `CERG-PLN-IR-001_Incident_Response_Plan.md` | Related Documents mid-row | Open |
| 19 | `CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md` | Roles table mid-row | Open |
| 20 | `CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md` | Cadence table mid-row | Open |

**Documents confirmed complete (39 of 59):** README.md, CERG - Cybersecurity Policy.md, CERG Compliance Matrix.md, CERG Framework - Cyber Engineering Risk and Governance.md, CERG Risk Taxonomy.md, CERG_Risk_Management_Framework_v1.0.md, CERG-GOV-CAL-001, CERG-GOV-CAT-001, CERG-GOV-CB-001, CERG-GOV-IMP-001, CERG-GOV-MAT-001, CERG-GOV-OM-001, CERG-GOV-RAC-001, CERG-GOV-STY-001, CERG-GOV-TRC-001, CERG-GOV-VAR-001, CERG-STD-AI-001, CERG-STD-AM-001, CERG-STD-DG-001, CERG-STD-EP-001, CERG-STD-MSG-001, CERG-STD-NET-001, CERG-STD-SDL-001, CERG-PRC-AUD-001, CERG-PRC-CHG-001, CERG-PRC-IR-002, CERG-PRC-TI-001, CERG-PRC-TM-001, CERG-PLN-BC-001, CERG-PLN-ISO-001, CERG-PLN-PRIV-001, CERG-TMPL-AR-001, CERG-TMPL-AUD-001, CERG-TMPL-CUI-001, CERG-TMPL-CUI-002, CERG-TMPL-MTR-001, CERG-TMPL-RM-002, CERG-TMPL-RM-003, CERG-TMPL-TPRM-001
