---
name: Document improvement
about: Suggest a change to an existing CERG document
title: "[IMPROVE] <document ID or name>"
labels: improvement
assignees: ''

---

**Document:** `CERG-XXX-XXX-XXX` (or file path)

**Current state:**
What the document currently says or does (quote the relevant section if possible).

**Proposed change:**
What should be different and why.

**Which pillar does this affect?** Engineering / Risk / Governance / Cross-cutting

**Does this require a new catalog entry or domain code?** Yes / No

---

**Checklist:**
- [ ] I have read the relevant section of STY-001 (style guide)
- [ ] I have run `python3 tools/cerg-validate.py` on my proposed changes (or will do so in the PR)
- [ ] If this is a new document, I have registered the domain code in CAT-001 §2.1

---

## Before you submit

Read [CONTRIBUTING.md](../CONTRIBUTING.md) for the editing conventions, especially:
- Do NOT use the `patch` tool (it collides with `---` separators)
- Use the full 11-field STY-001 §4 metadata table
- No em dashes in prose (STY-001 §9.2)
