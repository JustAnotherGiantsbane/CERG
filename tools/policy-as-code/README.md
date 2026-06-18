# Policy-as-Code Examples for CERG

This directory contains reference implementations of **policy-as-code** patterns that map CERG controls to machine-enforceable rules. These examples support the CERG principles described in:

- **FRM-001 §3.2** — Policy-as-code as a core Engineering activity
- **OM-001 §3.1** — Automated enforcement over manual compliance
- **FLOW-001 F-02 T3** — Pipeline gates as admission control

## Contents

| File | What It Shows | CERG Controls Mapped |
|------|--------------|---------------------|
| [`dish-baseline-opa.rego`](./dish-baseline-opa.rego) | DISH secure configuration baseline as OPA/Rego policies for Linux password policy and Windows audit policy | `CERG-STD-CFG-001` §4, §5 |
| [`arch-review-gate.yml`](./arch-review-gate.yml) | Architecture review gate as a GitHub Actions workflow — blocks PRs missing required artifacts | `PRC-AR-001`, `FLOW-001 F-02` |
| [`admission-control.yml`](./admission-control.yml) | Change management admission control as a GitHub Actions workflow — enforces evidence + approval gates | `FLOW-001 F-01`, `RMF-001 §9.7` |

## How to Use

### Prerequisites

- **OPA / Rego**: [`openpolicyagent/opa`](https://www.openpolicyagent.org/docs/latest/) (CLI or deployed as sidecar)
- **GitHub Actions**: A GitHub repository with Actions enabled
- **Alternative engines**: The Rego policies work with [Kyverno](https://kyverno.io/) (via Kyverno JSON mode) and [Conftest](https://www.conftest.dev/)

### Quick Start (OPA)

```bash
# Evaluate all DISH policies against a configuration input
opa eval --data dish-baseline-opa.rego --input input.json "data.dish.auth"

# Test with a specific rule
opa eval --data dish-baseline-opa.rego --input input.json "data.dish.linux.password.min_length"
```

### Quick Start (Conftest)

```bash
# Evaluate DISH policies against a YAML config
conftest test --policy tools/policy-as-code/dish-baseline-opa.rego config.yaml
```

## CERG Control-to-Policy Mapping

Each policy rule references the CERG control baseline (CB-001) and standard it implements:

| Rego Rule | CERG Control / Standard | Adversarial Goal |
|-----------|------------------------|-------------------|
| `dish.linux.password.min_length` | CB-001 AC-7 / STD-CFG-001 §5.1 | Prevent brute-force / weak-password login |
| `dish.linux.password.complexity` | CB-001 IA-5(1) / STD-CFG-001 §5.1 | Enforce password composition |
| `dish.linux.password.expiry` | CB-001 IA-5 / STD-CFG-001 §5.1 | Limit credential lifetime |
| `dish.linux.account.lockout` | CB-001 AC-7 / STD-CFG-001 §5.1 | Throttle repeated auth failures |
| `dish.windows.audit.account_login` | CB-001 AU-3 / STD-CFG-001 §5.2 | Log authentication events |
| `dish.windows.audit.account_management` | CB-001 AU-3 / STD-CFG-001 §5.2 | Log account create/modify/delete |
| `dish.windows.audit.object_access` | CB-001 AU-3 / STD-CFG-001 §5.2 | Log resource access attempts |
| `dish.arch_review.requires_record` | PRC-AR-001 §4 / FLOW-001 F-02 T3 | Every deployment needs a disposition |
| `dish.arch_review.requires_threat_model` | PRC-AR-001 §5 / FLOW-001 F-02 T4 | High-risk changes need threat model |
| `dish.admission.requires_approval` | RMF-001 §9.7 / FLOW-001 F-01 | Changes need risk-acceptance or exception |
| `dish.admission.evidence_complete` | CB-001 §9 / AUD-001 | Evidence must be current |

## Adding New Policies

1. Add the Rego rule with a unique name under the `dish` package
2. Include a comment mapping to the CERG control ID and adversarial goal
3. Add the mapping to the table above
4. Verify with `opa eval` or `conftest test`

## References

- [Open Policy Agent — Policy Language](https://www.openpolicyagent.org/docs/latest/policy-language/)
- [Conftest — Rego for configuration files](https://www.conftest.dev/)
- [CERG STD-CFG-001 — DISH Baseline Standard](../../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)
- [CERG PRC-AR-001 — Architecture Review Procedure](../../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [CERG FLOW-001 — Cross-Pillar Operational Flows](../../governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md)
