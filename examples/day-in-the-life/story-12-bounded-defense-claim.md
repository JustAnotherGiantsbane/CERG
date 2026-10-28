# Story 12: Can Order-to-Cash Withstand Identity Takeover?

## Purpose

This illustrative story shows one bounded defense claim from business consequence through independent challenge and decision. It uses existing CERG records; it does not create a new register, template, or approval type.

## Situation

An organization depends on `ORDER-ERP-01` for its order-to-cash service. Its crown-jewel entry identifies the business service, SOX scope, consequence dimensions, owner, and executive sponsor. The application depends on the enterprise identity service `IDP-PRD-01`.

CERG commissions `SCN-05` — identity provider or federation compromise yielding organization-wide privilege — to answer:

> If the identity provider tenant is taken over, can an attacker mint administrative access to order-to-cash, and would the organization detect and contain it before privilege spreads?

The scenario’s load-bearing links are phishing-resistant MFA on privileged identity paths and post-takeover session/token containment.

## Record Trace

| Step | Existing record | What it contributes | What it must not do |
|---|---|---|---|
| 1 | Crown Jewel Scenario Record: `ORDER-ERP-01` + `SCN-05` | Business service, consequence dimensions, regulated scope, owner, sponsor, stable system identifier, scenario and expected outcome | Judge control state or copy service-interface terms |
| 2 | Protected-system SCP: `ORDER-ERP-01` | Local scope and `security_service_references: [IDP-PRD-01]` | Repeat service operator, assessor, rights, or business consequence |
| 3 | Service SCP: `IDP-PRD-01` | First-line Service Owner, operator, service boundaries, assurance rights, service-assessor assignment, evidence-currency rule, and provider-contract reference where applicable | Carry order-to-cash consequence fields or approve effectiveness |
| 4 | Rules of Engagement and Adversarial Validation Record: `AV-2026-005` | `SCN-05`, asserted identity-tenant scope, load-bearing links, ATT&CK techniques, assessor, method, evidence period, exclusions, and scoped independence | Let the operator or state author assess its own asserted scope |
| 5 | Evidence Index Entry attached to the Crown Jewel Scenario Record | References the preceding records, per-link state walk, challenge evidence, decision, and retest trigger | Copy consequence fields or become a new record type |

The protected-system reference is the common-control topology: many protected systems may reference `IDP-PRD-01`. The service SCP carries that service's interface, not the obligation of any consumer. Consequence remains on each protected system's crown-jewel entry.

## Independent Challenge

The signed RoE binds `AV-2026-005` to `SCN-05` and the asserted identity-tenant scope before testing begins. The adversarial assessor is independent of the IdP operator and any state author for that scope.

The identity service SCP may name an independent assessor for a claim about the identity service itself. That assignment does **not** automatically supply the assessor for this order-to-cash claim. The claim relies on the assessor-and-asserted-scope pairing recorded in `AV-2026-005`.

The final Adversarial Validation Record shows:

- privileged-path phishing-resistant MFA was challenged and held;
- session/token containment was challenged and failed; and
- the test used `T1556` and `T1606`, with method, evidence period, scope, exclusions, and assessor recorded.

The pressure-test Evidence Index Entry can therefore state a bounded result: the scenario is not fully defensible for the stated scope and period because token containment failed. It cites the order-to-cash consequence from the crown-jewel record rather than repeating it.

## Path A: Consequential Gap

The failed containment link follows the existing decision chain:

```text
FIND-2026-005: token-containment gap
  -> RISK-2026-005: material residual-risk change
    -> Risk Acceptance Record, only if the authorized business path accepts it
ODR-2026-Q2: fund treatment, assign action, or route an acceptance request
```

The Oversight Decision Record does not accept residual risk. If the business accepts it, the Risk Acceptance Record attaches to `RISK-2026-005` under the RMF authority route.

Two clocks remain separate:

1. The remediation retest verifies that the containment fix works before the finding closes.
2. The scenario claim is re-walked and re-challenged when its threat model changes, a material control/identity change occurs, or the scheduled scenario review arrives.

A closed finding does not by itself make the broader scenario claim current.

## Path B: Technical Claim Cap

The same identity service also supports `CLINICAL-REC-01`. Its protected-system SCP references `IDP-PRD-01`, but its stable identifier does not resolve to a crown-jewel entry.

CERG can still test and report the technical containment gap. The claim is limited to the asserted technical scope, and the system owner records the decision, date, and closure rationale in the Finding Record (or an Exposure Backlog Item where exposure management governs).

CERG cannot use that unjoined claim to assert a business outcome, support a compensated-exposure disposition, route an Oversight Decision Record, or obtain a Risk Acceptance Record based on an unnamed consequence. The missing join caps the assertion; it does not stop discovery, remediation challenge, or evidence collection.

## What This Demonstrates

- First line operates the identity service; CERG challenges the claim.
- Provider-produced telemetry may be evidence, but the provider cannot be the independent assessor for its operated scope.
- One enterprise security service can support many business services without inheriting their consequence fields.
- A control-state walk alone is not a consequential claim; independent challenge and bounded evidence are required.
- Missing business context limits what CERG can claim upward without creating a CMDB or BIA prerequisite.

## Related CERG Artifacts

- [Crown Jewel Register and Loss Scenario Library](../../governance/CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)
- [System Control Profile Template](../../templates/CERG-TMPL-SCP-001_System_Control_Profile_Template.md)
- [Adversarial Validation Procedure](../../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)
- [Record Catalog](../../governance/CERG-GOV-CAT-002_Record_Catalog.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
