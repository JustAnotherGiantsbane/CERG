# CERG readability audit — brief for batch agents

**Version 5.** This file is the audit's rulebook, versioned in the repo so it
outlives the profile, the machine, and the model that wrote it. Any agent with a
shell can audit against it; `tools/voice-exemptions.json` is its data, and
`tools/cerg-voice-check.py` is its instrument.

| Version | Change |
|---|---|
| v1 | Ground rules, the pass, exemptions, output contract. |
| v2 | The three moves: actorless paragraph, blockquote kill/demote/keep, shortening without losing the working qualifier. |
| v3 | Rule 5 (compression that deletes a verb is a downgrade), rule 6 (set-pronouns name their plural). |
| v4 | Rule 7 (authority before prose), three-value pending vocabulary. |
| v5 | `route` field in every record; rule 8 (near-identity reskin is a failed pass, not a rewrite). |

You are editing Markdown prose in a git worktree. The content is correct. The
language is not: it reads like a consultant with too much coffee — padded,
rhythmless, and hard to say out loud.

## Ground rules

1. **The content is not yours to change.** No new requirements, no removed
   requirements, no reordered obligations, no softened rules. If a sentence
   carries a rule, the rule survives the rewrite or you leave the sentence.
2. **Headings are frozen.** Never reword a `#` line. Anchors in tables of
   contents and cross-document links depend on the exact text.
3. **Links are frozen.** Every `[text](target)` target must still exist in the
   file afterwards. You may reword the link text only if the target is
   unchanged.
4. **Tables are data.** Fix a cell's wording only when it is a sentence; never
   change values, IDs, or ordering.
5. **No invention.** Do not add facts, vendors, numbers, or examples the
   document does not already contain. A concrete noun from the document is
   allowed to move; a new one is not.

## The pass, per file

1. Read the whole file before editing anything.
2. Write down the three sentences that already survive being read aloud. Those
   are the file's voice targets; you are matching them, not replacing them.
   Every file has its own, so your batch must not all sound like one author:
   standards prose may read tighter than a story, a job description more formal
   than a runbook.
3. Work the worst passages first: filler ("in order to", "serves to",
   "leverages", "in accordance with" as habit), nominalizations, passive
   constructions where the actor is known, and sentences whose breath runs
   past 18 words between punctuation.
4. Rewrite to three rules: one idea per sentence; the actor before the verb;
   no sentence you would have to restart to say.
5. Commit per file with the census deltas named in the message.

## Move 1 — the actorless paragraph

Underline every verb; for each ask *whose calendar, whose hands?* If the answer
exists — usually hiding in a `by X` phrase or a Roles row — put the name in
front of the verb: "owned by Governance, populated by Risk, informed by
Engineering" becomes "Governance owns it, Risk populates it, Engineering
informs it."

If there is no so-and-so behind the `by`, the sentence is a **fact**, not an
event. Do not stage it with a fake actor. "Progress between states is gated by
explicit validation, not elapsed time" does not become "the program gates
progress" — that is worse. It becomes "A finding moves when someone validates
it, not when the clock runs," or it stays a definition with the verb clutter
cut.

## Move 2 — blockquote: kill, demote, or keep

Read only the blockquotes aloud, back to back. If the sequence would sound like
a motivational poster for any company in any industry — swap the org name and
nothing changes — it dies; demote its content to ordinary prose in the section
it comments on.

Keep the box only when the sentence is one a reader would quote back, and only
when it kills a misconception the reader actually holds: "A scanner report is
inventory data. It is not the exposure management program." That earns its
shout.

The third case: a blockquote holding a **rule plus a rationale**. Do not delete
and do not shout — the rule becomes the section's first sentence, the rationale
follows as prose, the box goes.

Fleet note: the repo's original disease was one blockquote in the same position
in every document, so the format meant nothing. If your files each leave exactly
one blockquote where they each had exactly one, you pattern-matched instead of
reading.

## Move 3 — shortening without losing the working qualifier

Before cutting a long compliance sentence, label every chunk: **claim** /
**bound** ("at least 30 days", "prior to production deployment") / **scope**
("for CUI scope", "the minimum for CERG compliance") / **authority** (the
citation) / **connective** (everything else).

Only connectives without a job may die. Bounds, scopes and authorities stay,
even when they make the sentence ugly. One word at a time: *does dropping this
change what a compliant employee is allowed to do?* If yes, it is load-bearing.

Timeline bounds take care: "prior to production deployment" marks a moment;
"before deployment" is a mood.

After shortening, run the trace: every content word of the original must be
present in the new file or named in the commit message.

## Two more rules, minted from the fleet's own diffs

**Rule 5 — compression that deletes a verb is a downgrade.** If your shorter
sentence has no conjugated verb where the original had one, it is worse
regardless of what the filler count says. "The principles that govern how
access to network resources is decided" became "the principles that govern
access decisions": fewer words, no tense, a noun in a verb's slot.

**Rule 6 — a set-pronoun must name its plural.** Every "them / these / those"
has to point at a plural named within the two preceding sentences. Substitute
the plural aloud before committing. "This matrix adds the layer between them"
dangled because the sentence before it ended on a singular.

## Rule 7 — authority comes before prose

Before editing any file, read its metadata block. If the **Status** or **Owner**
row contains "External Interface" or "Standing IR Team", the document belongs to
another team. Record `status: skipped`, `why_skipped: not CERG-owned; signpost
routes to it`, and touch nothing. Two files in this tree qualify:
`plans/CERG-PLN-IR-001_Incident_Response_Plan.md` and
`procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md`.

The prohibition is not about the prose. Both documents state that CERG reviews
them for cross-reference accuracy only, so a good sentence in the wrong
document is still a trespass. `tools/cerg-authority-check.py --base main --head
<branch>` enforces this at merge time.

## Pending reasons — three values, not one

When you cannot finish a file, `why_skipped` must start with one of:

- `not yet reached` — you never opened it.
- `read not edited` — you opened it, judged it in voice, and changed nothing.
- `edited but failed its own checks` — you changed it, and the validator,
  checker or census refused the result.

Only the third needs a human. The other two are queue state.

## Do not touch

`tools/voice-exemptions.json` names the constructions this pass must not
alter — normative `shall` lines, flat closing sentences, negations of a named
misconception, builds whose final clause carries the judgment, balanced
semicolon pairs, anaphora inventories, artifact and state names,
citation-bound "in accordance with"/"prior to", and roles/ bullet grammar.
Read it before you start. It is data, not advice: if the checker flags a
sentence the file protects, the sentence stays.

## Verification before every commit

```
python3 tools/cerg-validate.py .                       # links, anchors, catalog
python3 <voicecheck>/cerg-voice-check.py .             # score must not rise
```

Plus the obligation census for the file you touched:

```
for w in shall must required requires; do
  echo "$w main=$(git show main:F -- | grep -o -i "\b$w\b" | wc -l) now=$(grep -o -i "\b$w\b" F | wc -l)"
done
```

Any delta is named in the commit message with the sentence that caused it.
An unexplained delta means the commit is not finished.

## Rule 8 — a near-identity reskin is a failed pass

If your edit changes fewer than one word in twenty (word-level similarity above
0.95 against the original), you have not rewritten the file; you have reskinned
it. "ensures that" → "makes sure" is the specimen. A reskinned file is worse
than an untouched one, because it records as done and nobody looks again.

Record it as `status: pending`, `why_skipped: pending — rule 8: near-identity
reskin`, and either do the real pass or leave it for a route that can.

## Output contract

For each file, append one JSON object to
`<results>/batch-<n>.jsonl`:

```
{"file": "...", "status": "rewritten|skipped|blocked|pending",
 "route": "fast|writer",
 "sentences_in": 0, "sentences_out": 0,
 "census_delta": {"shall": 0, "must": 0, "required": 0, "requires": 0},
 "voice_targets": ["three sentences that already worked"],
 "before_after": [{"before": "...", "after": "..."}],
 "commit": "...", "why_skipped": "...", "needs_owner": "..."}
```

`before_after` carries the two or three sentences you changed most, quoted both
ways. A diff is not evidence of a voice; a human has to read the pair and decide
whether it is better or merely smoother.

`status: blocked` is a real answer. If a file's prose belongs to another team,
or a rule's meaning is ambiguous, say so and touch nothing. `pending` with a
reason is honest; silent omission is not.
