# Story 12: Can Order-to-Cash Withstand Identity Takeover?

## The decision

`ORDER-ERP-01` supports order-to-cash and depends on identity service `IDP-PRD-01`.

`SCN-05` asks one question:

> If an attacker takes over the identity-provider tenant, can they mint administrative access to order-to-cash, and will the organization contain it before privilege spreads?

The load-bearing links are phishing-resistant MFA on privileged identity paths and session/token containment after takeover.

## The proof path

This uses existing records. It is not a new claim packet.

| Record | Decision-useful fact | Boundary |
|---|---|---|
| Crown Jewel Scenario Record: `ORDER-ERP-01` + `SCN-05` | Business service, consequence, SOX scope, owner, sponsor, expected outcome | Does not judge control state or carry service terms. |
| Protected-system SCP: `ORDER-ERP-01` | Local scope and `security_service_references: [IDP-PRD-01]` | Does not copy operator, assessor, rights, or consequence. |
| Service SCP: `IDP-PRD-01` | First-line owner/operator, operating boundary, assurance rights, assessor assignment, evidence-currency rule, and provider reference where applicable | Does not inherit any consumer's consequence or approve effectiveness. |
| RoE and Adversarial Validation Record: `AV-2026-005` | Scenario, asserted identity-tenant scope, method, evidence period, exclusions, and assessor | The operator or state author cannot assess that asserted scope. |
| Evidence Index Entry on the Crown Jewel Scenario Record | Links the challenge evidence, per-link result, decision, and retest trigger | Does not duplicate consequence or create a new record type. |

The protected-system reference is the common-control join. Many systems can reference `IDP-PRD-01`; each keeps its own consequence in its own crown-jewel entry.

## What the challenge found

The signed RoE binds `AV-2026-005` to `SCN-05` and the asserted identity-tenant scope before testing. The assessor is independent of the IdP operator and any state author for that scope.

A service-SCP assessor assignment does not automatically qualify that person for the order-to-cash claim. The claim relies on the assessor-and-asserted-scope pairing in `AV-2026-005`.

| Link | Result | Evidence |
|---|---|---|
| Privileged-path phishing-resistant MFA | Held | Independent challenge recorded in `AV-2026-005`. |
| Session/token containment | Failed | Independent challenge recorded for `T1556` and `T1606`, with method, period, scope, and exclusions. |

The bounded conclusion is direct: order-to-cash is **not fully defensible** for this scope and period because token containment failed.

## Decision and retest

The failed link follows the existing path:

```text
FIND-2026-005: token-containment gap
  -> RISK-2026-005: material residual-risk change
    -> Risk Acceptance Record, only if the authorized business path accepts it
ODR-2026-Q2: funds treatment, assigns action, or routes an acceptance request
```

An Oversight Decision Record does not accept residual risk.

Two clocks apply:

| Clock | Trigger | Outcome |
|---|---|---|
| Remediation retest | A remediation claim. [`PRC-AV-001`](../../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) §10.3 requires 30 days for Critical and 60 days for High findings. | The finding closes only when the retest demonstrates remediation. |
| Scenario claim retest | Threat-model change; material control, identity-path, or crown-jewel-population change; or scheduled scenario review. | The claim is re-walked and re-challenged. |

Closing the finding does not by itself make the scenario claim current.

## The technical-only variant

`CLINICAL-REC-01` also references `IDP-PRD-01` but does not resolve to a crown-jewel entry. CERG can test and report the technical containment gap. The system owner records disposition, date, and closure rationale in the existing Finding Record or Exposure Backlog Item.

CERG cannot use that unjoined claim to state a business outcome, support a compensated-exposure disposition, route an Oversight Decision Record, or obtain a Risk Acceptance Record. Missing business context caps the claim; it does not stop discovery, remediation challenge, or evidence collection.

## What this proves

- First line operates the identity service; CERG independently challenges the claim.
- Provider telemetry can be evidence, but the provider cannot assess or approve effectiveness for its operated scope.
- One security service can support many consumers without inheriting their consequence.
- A control-state walk is not a consequential claim. Independent challenge and bounded evidence are required.
- Missing business context limits what CERG can claim upward without forcing a CMDB or BIA cleanup program.

## Related CERG Artifacts

- [Crown Jewel Register and Loss Scenario Library](../../governance/CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)
- [System Control Profile Template](../../templates/CERG-TMPL-SCP-001_System_Control_Profile_Template.md)
- [Adversarial Validation Procedure](../../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)
- [Record Catalog](../../governance/CERG-GOV-CAT-002_Record_Catalog.md)
- [Risk Register and Exception Process](../../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
