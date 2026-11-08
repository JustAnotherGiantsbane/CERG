# Branch archive

Branches removed on 2026-11-08 once their work was either contained in `main` or already
decided upstream. Every entry records the tip commit, so a branch can be restored with
`git push origin <tip-sha>:refs/heads/<branch>`; PR refs also remain reachable at
`refs/pull/<n>/head`.

## Removed — work already in `main`

These branches are ancestors of `main`, so deleting the ref loses no history.

| Branch | Tip | Where the work went |
|---|---|---|
| `chore/drop-write-only-index-fields` | `2aba40a` | #275 MERGED into experiment/second-line-model-implementation |
| `fix/ar-001-disposition-phases` | `1e2a43e` | #274 MERGED into experiment/second-line-model-implementation |
| `fix/ar-001-golive-decision-owner` | `e2b26c8` | #281 MERGED into experiment/second-line-model-implementation |
| `fix/authority-reconciliation` | `921ace4` | #283 MERGED into experiment/second-line-model-implementation |
| `frm/front-door-second-line` | `61086c9` | #250 MERGED into experiment/second-line-model-implementation |
| `jd/seceng-cloud-ot-boundary` | `f899cbd` | #263 MERGED into experiment/second-line-model-implementation |
| `join/experiment-into-main` | `2262367` | joined into `main` via PR #2 |
| `mtr/reporting-slice` | `6b639ec` | #235 MERGED into experiment/second-line-model-implementation |
| `std/ot-001-risk-pillar-exposure-scope` | `11547fe` | #262 MERGED into experiment/second-line-model-implementation |
| `style/start-here-participant-path` | `1dbfa05` | #278 MERGED into experiment/second-line-model-implementation |
| `tprm/observable-contractual-control` | `55ec6f9` | #233 MERGED into experiment/second-line-model-implementation |

## Removed — decided upstream

The proposal was made and settled. These commits are not in `main`; they stay recoverable through the PR ref.

| Branch | Tip | Upstream PR | Decision |
|---|---|---|---|
| `identity-considerations` | `8b5c500` | #185 MERGED | merged into `main`; branch commits superseded by later rewrites |
| `ciso-cso-executive-briefing` | `3a61e8c` | #186 MERGED | merged into `main`; branch commits superseded by later rewrites |
| `upstream/cb-002-expanded` | `90f61a2` | #191 CLOSED | proposal closed without merge |
| `frm/seceng-cloud-ot-split` | `d68adab` | #256 CLOSED | proposal closed without merge |
| `jd/seceng-appsec-leader-boundary` | `e3fb45e` | #260 CLOSED | proposal closed without merge |
| `jd/seceng-008-authority-completeness` | `0805283` | #270 CLOSED | proposal closed without merge |


## Removed 2026-11-08 — overnight agent run

These branches were created and merged by the overnight run and then deleted. Each tip was checked against `main` before being recorded here.

| Branch | Handle | What it is | State |
|---|---|---|---|
| `audit/batch-1` | `3d7f60c` | merge tip | merged into main |
| `audit/batch-2` | `42562ed` | merge tip | merged into main |
| `audit/batch-3` | `675e3e6` | merge tip | merged into main |
| `audit/batch-4` | `16d98bc` | merge tip | merged into main |
| `audit/batch-5` | `1099baa` | merge tip | merged into main |
| `chore/authority-gate` | `b92b9f9` | merge tip | merged into main |
| `prose/day-in-the-life` | `9637ff8` | merge tip | merged into main |
| `prose/front-door` | `6997d80` | last push head | merged into main (fast-forward, no merge commit) |
| `prose/prc-vm-001` | `b33bf68` | merge tip | merged into main |
| `prose/rmf-001-sec1-9` | `f8eaa92` | merge tip | merged into main |
| `prose/signpost-register` | `33906b8` | merge tip | merged into main |
| `prose/trc-001` | `b627d76` | merge tip | merged into main |
| `prose/incident-signpost` | `07fd0fb` | commit that added CERG-GOV-IR-001 | content is in main; branch tip not recorded |
| `voice/writer-exception-av001` | `954ea2b` | voice(writer-exception) commit | content is in main; tip is this commit if it was a single-commit branch |

## Current branches

| Branch | State |
|---|---|
| `fix/adopter-fit-boundaries` | 6 commits ahead of `main` — Upstream PR #286 merged 2026-11-08, but into the upstream experiment branch, not into this repo's main |
| `feat/practice-improvement-pack` | 26 commits ahead of `main` — never proposed upstream |
| `practice/worked-instance` | 10 commits ahead of `main` — never proposed upstream |