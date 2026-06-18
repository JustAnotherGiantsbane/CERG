# CERG DISH Baseline — OPA/Rego Policies
#
# Maps CERG-STD-CFG-001 (DISH) controls to machine-enforceable
# Open Policy Agent / Rego rules for Linux & Windows platforms.
#
# CERG Control-to-Policy Mapping:
#   dish.linux.password.*      → CB-001 AC-7, IA-5(1)  / STD-CFG-001 §5.1
#   dish.linux.account.lockout → CB-001 AC-7              / STD-CFG-001 §5.1
#   dish.windows.audit.*       → CB-001 AU-3              / STD-CFG-001 §5.2
#   dish.arch_review.*         → PRC-AR-001 §4-5          / FLOW-001 F-02
#   dish.admission.*           → RMF-001 §9.7             / FLOW-001 F-01
#
# Usage:
#   opa eval --data dish-baseline-opa.rego --input config.json "data.dish.auth"
#   conftest test --policy dish-baseline-opa.rego config.yaml
#
# Each rule returns a structured result with:
#   - rule_name:     Rego rule identifier
#   - cerg_control:  CERG CB-001 control ID
#   - standard_ref:  CERG STD-CFG-001 section reference
#   - status:        PASS / FAIL / SKIP (based on input scope)
#   - message:       Human-readable explanation

package dish

import future.keywords.if
import future.keywords.in

# ─────────────────────────────────────────────
# Defaults
# ─────────────────────────────────────────────

default linux_password_min_length := {"status": "SKIP", "message": "No Linux password policy data"}

# ─────────────────────────────────────────────
# Global helpers
# ─────────────────────────────────────────────

# Determine the OS family from the input
windows_scope    := input.meta.os_family == "windows"
linux_scope      := input.meta.os_family == "linux"
k8s_scope        := input.meta.os_family == "kubernetes"

# Extract the password policy sub-object
linux_pw_policy    := input.linux.password_policy
windows_audit_pols := input.windows.audit_policy

# ─────────────────────────────────────────────
# 1. LINUX PASSWORD POLICY — STD-CFG-001 §5.1
# ─────────────────────────────────────────────

# AC-7 / IA-5(1): Minimum password length ≥ 14 characters
linux_password_min_length = r if {
    linux_scope
    length(linux_pw_policy.min_length) >= 14
    r := {"cerg_control": "CB-001 AC-7 / IA-5(1)", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.min_length", "status": "PASS", "message": sprintf("Minimum password length is %d — meets DISH ≥ 14 requirement", [linux_pw_policy.min_length])}
} else = r if {
    linux_scope
    r := {"cerg_control": "CB-001 AC-7 / IA-5(1)", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.min_length", "status": "FAIL", "message": sprintf("Minimum password length is %d — DISH requires ≥ 14", [linux_pw_policy.min_length])}
}

# IA-5(1): Password must require 3 of 4 character classes (upper, lower, digit, special)
linux_password_complexity = r if {
    linux_scope
    classes := [linux_pw_policy.require_uppercase, linux_pw_policy.require_lowercase, linux_pw_policy.require_digit, linux_pw_policy.require_special]
    enabled := [c | c = classes[_]; c == true]
    count(enabled) >= 3
    r := {"cerg_control": "CB-001 IA-5(1)", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.complexity", "status": "PASS", "message": sprintf("Password complexity requires %d of 4 character classes — meets DISH ≥ 3", [count(enabled)])}
} else = r if {
    linux_scope
    r := {"cerg_control": "CB-001 IA-5(1)", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.complexity", "status": "FAIL", "message": "Password complexity requires fewer than 3 character classes — DISH requires 3 of 4"}
}

# IA-5: Password max age ≤ 90 days (CIS Level 1)
linux_password_max_age = r if {
    linux_scope
    linux_pw_policy.max_age_days <= 90
    r := {"cerg_control": "CB-001 IA-5", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.max_age", "status": "PASS", "message": sprintf("Password max age is %d days — within DISH ≤ 90 requirement", [linux_pw_policy.max_age_days])}
} else = r if {
    linux_scope
    r := {"cerg_control": "CB-001 IA-5", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.password.max_age", "status": "FAIL", "message": sprintf("Password max age is %d days — DISH requires ≤ 90", [linux_pw_policy.max_age_days])}
}

# AC-7: Account lockout after ≤ 5 failed attempts, lockout ≥ 900 seconds (15 min)
linux_account_lockout = r if {
    linux_scope
    lk := linux_pw_policy.lockout
    lk.threshold <= 5
    lk.lockout_duration_seconds >= 900
    r := {"cerg_control": "CB-001 AC-7", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.account.lockout", "status": "PASS", "message": sprintf("Lockout after %d failures, %d sec duration — meets DISH ≤ 5 / ≥ 900", [lk.threshold, lk.lockout_duration_seconds])}
} else = r if {
    linux_scope
    r := {"cerg_control": "CB-001 AC-7", "standard_ref": "STD-CFG-001 §5.1", "rule_name": "dish.linux.account.lockout", "status": "FAIL", "message": sprintf("Lockout threshold/duration (%d/%d) does not meet DISH (≤ 5 attempts, ≥ 900 sec)", [linux_pw_policy.lockout.threshold, linux_pw_policy.lockout.lockout_duration_seconds])}
}

# ─────────────────────────────────────────────
# 2. WINDOWS AUDIT POLICY — STD-CFG-001 §5.2
# ─────────────────────────────────────────────

# AU-3: Audit account logon events (Success + Failure)
windows_audit_account_logon = r if {
    windows_scope
    windows_audit_pols.account_logon == "Success and Failure"
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.account_logon", "status": "PASS", "message": "Account logon auditing is set to 'Success and Failure'"}
} else = r if {
    windows_scope
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.account_logon", "status": "FAIL", "message": sprintf("Account logon auditing is '%s' — DISH requires 'Success and Failure'", [windows_audit_pols.account_logon])}
}

# AU-3: Audit account management events (Success + Failure)
windows_audit_account_management = r if {
    windows_scope
    windows_audit_pols.account_management == "Success and Failure"
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.account_management", "status": "PASS", "message": "Account management auditing is set to 'Success and Failure'"}
} else = r if {
    windows_scope
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.account_management", "status": "FAIL", "message": sprintf("Account management auditing is '%s' — DISH requires 'Success and Failure'", [windows_audit_pols.account_management])}
}

# AU-3: Audit object access events (Success + Failure)
windows_audit_object_access = r if {
    windows_scope
    windows_audit_pols.object_access == "Success and Failure"
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.object_access", "status": "PASS", "message": "Object access auditing is set to 'Success and Failure'"}
} else = r if {
    windows_scope
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.object_access", "status": "FAIL", "message": sprintf("Object access auditing is '%s' — DISH requires 'Success and Failure'", [windows_audit_pols.object_access])}
}

# AU-3: Audit privilege use events (Success + Failure recommended for DISH L2)
windows_audit_privilege_use = r if {
    windows_scope
    windows_audit_pols.privilege_use == "Success and Failure"
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.privilege_use", "status": "PASS", "message": "Privilege use auditing is set to 'Success and Failure'"}
} else = r if {
    windows_scope
    r := {"cerg_control": "CB-001 AU-3", "standard_ref": "STD-CFG-001 §5.2", "rule_name": "dish.windows.audit.privilege_use", "status": "FAIL", "message": sprintf("Privilege use auditing is '%s' — DISH L2 requires 'Success and Failure'", [windows_audit_pols.privilege_use])}
}

# ─────────────────────────────────────────────
# 3. AGGREGATE: Check all rules for a given scope
# ─────────────────────────────────────────────

# Collect all evaluated rule results
all_results[result] {
    result := linux_password_min_length
}
all_results[result] {
    result := linux_password_complexity
}
all_results[result] {
    result := linux_password_max_age
}
all_results[result] {
    result := linux_account_lockout
}
all_results[result] {
    result := windows_audit_account_logon
}
all_results[result] {
    result := windows_audit_account_management
}
all_results[result] {
    result := windows_audit_object_access
}
all_results[result] {
    result := windows_audit_privilege_use
}

# Overall DISH posture assessment
# Returns PASS only if all applicable rules pass
posture = r {
    results := [res | res := all_results[_]; res.status != "SKIP"]
    failures := [res | res := results[_]; res.status == "FAIL"]
    passes   := [res | res := results[_]; res.status == "PASS"]

    r := {
        "framework": "CERG DISH Baseline (STD-CFG-001)",
        "total_checks": count(results),
        "pass": count(passes),
        "fail": count(failures),
        "posture": "PASS" if count(failures) == 0 else "FAIL",
        "failures": [f | f := failures[_]; {"rule": f.rule_name, "message": f.message}],
    }
}
