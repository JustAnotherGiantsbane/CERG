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

## Kept

| Branch | Why it stays |
|---|---|
| `fix/adopter-fit-boundaries` | Live work — upstream PR #286 open |
| `feat/practice-improvement-pack` | 26 commits, never proposed upstream |
| `practice/worked-instance` | 10 commits, never proposed upstream |
| `prose/day-in-the-life` | Active prose work, 2026-11-07 |
| `prose/front-door` | Active prose work, 2026-11-07 |
| `prose/rmf-001-sec1-9` | Active prose work, 2026-11-07 |
