# Contributing to CERG

CERG is open source (CC BY 4.0) and contributions are welcome. This document explains how to contribute effectively.

## Ways to contribute

**Improve existing documents.** Fix gaps, clarify language, add missing cross-references, or update regulatory citations.

**Propose new documents.** New standards, procedures, templates, or operational packages that fit the CERG model.

**Write example profiles.** Sector-specific or size-specific adaptation examples in `/examples/`.

**Report bugs.** Broken links, catalog errors, metadata inconsistencies, or validation failures.

**Suggest structural improvements.** New workstreams, maturity model domains, or metrics.

## Before you start

1. **Read the framework first.** At minimum: [README](README.md), [START-HERE](START-HERE.md), [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md), and [Operating Model](governance/CERG-GOV-OM-001_CERG_Operating_Model.md). Contributions that don't fit the three-pillar model or the document conventions will need rework.

2. **Check the catalog.** Every document has a `CERG-TYPE-DOMAIN-NNN` ID registered in [CAT-001](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md). New documents need a new domain code registered in §2.1 before the catalog row is added in §5.

3. **Understand the conventions.** Read [STY-001](governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) (metadata tables, section numbering, no em dashes in prose). See [AGENTS.md](AGENTS.md) for editing pitfalls — especially the `patch` tool collision with `---` separators.

## How to submit changes

**For small fixes** (typos, single-link fixes, metadata corrections): open a PR directly. One commit per file edited, short human-readable messages.

**For new documents or structural changes**: open an issue first so the approach can be discussed before you invest in a full draft. Include the proposed Document ID, which pillar owns it, and which existing documents it cross-references.

**For everything**: make sure `python3 tools/cerg-validate.py` passes with 0 errors before submitting. Warnings should be resolved before submitting unless they are intentionally documented and accepted by maintainers; errors are not acceptable.

## Where work happens, and what a pull request is for

**Work in your own fork. `m0dernz/CERG` keeps a single maintainer, and changes reach it as pull requests.** Direct pushes to the canonical repo are not available, by design.

The fork is yours to experiment in. Restructure a standard, rewrite a procedure, prototype an operating asset, try three designs and keep one. None of that needs permission, and none of it needs to look finished before you start. The fork is not a waiting room for approval. It is where the work happens.

A pull request to `m0dernz` is an offer, not an exam. The maintainer decides whether a change belongs in mainline now, given what mainline is already carrying. That is a question about scope, timing, and review load, not a verdict on whether the idea is good. An excellent change can be declined because the maintainer cannot give it the review it deserves, because it targets a generation of the framework under revision, or because similar work is already in flight.

**A rejected pull request is not a finding that the idea is bad.** It means mainline is not the right destination today. The work stays valid in your fork, stays citable, and can be proposed again when the evidence or the mainline has changed.

Slow adoption is the design, not friction to route around. Contributors move fast because they cannot destabilize the canonical repo. The maintainer accepts the maintenance burden along with the authority over what enters it. That trade is the separation of duties, and it is what keeps CERG a reference rather than a running average of whatever arrived most recently.

### What this asks of a contributor

- Open one pull request per idea. A change a reviewer can hold in their head and revert in isolation is a change that can be accepted.
- Make the pull request argue for itself: the problem, the evidence it works, what it costs to maintain, and what breaks if it is declined.
- Do not resubmit a declined change unchanged. New evidence, a narrower scope, or a changed mainline is a reason to try again. Repetition is not.
- Keep your fork's `main` usable. Other people read it, and a branch full of half-merged debris is not a contribution.
- Do not wait on a merge to continue. Build dependent work in your fork against its own branch, and say what it rests on.

## Optional: pre-commit hook

The repo provides a `.pre-commit-config.yaml` that runs the validator, integrity checker, and validator tests on every commit. This is **optional** — the CERG CI workflow runs the same checks on every push and pull request, so pre-commit is a faster local feedback loop, not an additional gate.

To enable:

```bash
pip install pre-commit
pre-commit install
```

To skip on a specific commit when intentional:

```bash
git commit --no-verify
```

The pre-commit hooks run against the full corpus, so every commit triggers a repo-wide check. This is intentional: a link fix in one file can break references in another, and a per-file subset would miss that.

## Document conventions (quick reference)

- **Metadata table**: full 11-field STY-001 §4 format (Document ID, Version, Status, Classification, Owner, Parent Policy, Review Cycle, Frameworks, Regulations, Environments). Copy the shape from [EDG-001](governance/CERG-GOV-EDG-001_Edge_Register.md).
- **Status**: every CERG-owned document pushed to `main` must be `Approved` with `Approved By: CISO` in the Document Control section. (IR docs are the only exception.)
- **Editing**: do NOT use the `patch` tool on CERG docs — the `---` separator and `**Version**`/`**Status**` table headers collide. Use line-targeted Python via `execute_code`, reading with `open(path).read()`.
- **Links**: resolve relative to the source file's directory. Files in `governance/` linking to other `governance/` files use bare filenames. Files in `governance/` linking to `procedures/` use `../procedures/FILENAME.md`.
- **No em dashes** in prose (STY-001 §9.2). Use hyphens or restructure.
- **No bare unfilled values** in Approved documents. Use "preliminary default requiring organizational calibration" with a stated basis, per RMF-001 §12.

## Code of conduct

Be respectful, assume good faith, and keep discussions focused on making the framework better. Disagreements about approach are healthy; personal criticism is not.

## Questions?

Open an issue with the `question` label, or start a [GitHub Discussion](https://github.com/m0dernz/CERG/discussions).
