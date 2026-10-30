"""Guard the two invariants that let the LLM index drop its absolute line ranges.

The index used to carry `lines: [start, end]` per document. Those are absolute
positions in a virtual concatenation of the corpus, so any document that grew by
one line shifted the range of every document after it and two PRs that both
regenerated the file conflicted at every one of those lines. `total_tokens_estimate`
was the same kind of field: a corpus aggregate nothing read.

Both are gone, and both are still reconstructible from data that stayed:

    ranges  = accumulate `lines_count` in document order, adding two boundary lines
    total   = sum(document["tokens"])

That only works while the layout stays contiguous, which is the property this test
enforces. If a future change makes document positions non-contiguous, the derivation
silently becomes wrong, so the test fails instead.
"""

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "machine-readable" / "cerg-llm-index.json"
BOUNDARY_LINES = 2  # matches the generator's virtual separator between documents


def load_index() -> dict:
    assert INDEX.exists(), f"generated index missing at {INDEX}"
    return json.loads(INDEX.read_text(encoding="utf-8"))


def derive_ranges(documents: list) -> dict:
    """Rebuild the removed absolute ranges from retained per-document data."""
    ranges = {}
    cursor = 1
    for doc in documents:
        ranges[doc["id"]] = [cursor, cursor + doc["lines_count"]]
        cursor = ranges[doc["id"]][1] + BOUNDARY_LINES
    return ranges


def test_write_only_fields_are_not_emitted():
    index = load_index()
    assert "total_tokens_estimate" not in index, (
        "total_tokens_estimate is a corpus aggregate with no consumer; it belongs out of the index"
    )
    offenders = [doc["id"] for doc in index["documents"] if "lines" in doc]
    assert not offenders, (
        f"absolute line ranges make concurrent regenerations conflict: {offenders[:5]}"
    )


def test_every_document_retains_the_data_needed_to_derive_them():
    index = load_index()
    for doc in index["documents"]:
        assert isinstance(doc.get("id"), str) and doc["id"], "document lost its id"
        for field in ("lines_count", "chars", "tokens"):
            assert field in doc, f"{doc['id']} lost {field}, which derivation needs"
            assert isinstance(doc[field], int) and doc[field] > 0, (
                f"{doc['id']} has a non-positive {field}: {doc[field]!r}"
            )


def test_layout_matches_source_and_emission_order():
    """The derivation is true only if `lines_count` matches source and order is preserved.

    An earlier version of this test rebuilt each range from `lines_count` and then asserted the
    rebuild used the same formula, which could never fail: inflating a document's `lines_count` by
    50 and swapping two documents both left it green. These two properties are the ones that
    actually hold the derivation up, and both can fail.
    """
    index = load_index()
    for doc in index["documents"]:
        path = ROOT / doc["path"]
        assert path.exists(), f"{doc['id']}: indexed path does not exist: {doc['path']}"
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert doc["chars"] == len(text), (
            f"{doc['id']}: chars {doc['chars']} but source is {len(text)}"
        )
        assert doc["lines_count"] == len(text.splitlines()), (
            f"{doc['id']}: lines_count {doc['lines_count']} but source has {len(text.splitlines())}"
        )

    # Emission order is part of the contract: re-sorting documents[] by path invalidates every
    # rebuilt range after the first move.
    order = ["README.md", "START-HERE.md", "AGENTS.md", "governance", "standards", "procedures",
             "plans", "templates", "roles", "machine-readable", "examples"]

    def sort_key(doc):
        rel = doc["path"]
        first = rel.split("/", 1)[0]
        rank = order.index(rel) if rel in order else (order.index(first) if first in order else 99)
        return (rank, rel)

    emitted = [doc["id"] for doc in index["documents"]]
    expected = [doc["id"] for doc in sorted(index["documents"], key=sort_key)]
    assert emitted == expected, (
        "documents[] is not in emitter order; rebuilt line ranges would be wrong past the first move"
    )


def test_removed_aggregate_is_reconstructible_from_retained_data():
    """The aggregate is sum(tokens), and tokens is itself a function of chars.

    Comparing sum(tokens) against sum(tokens) would prove nothing, so the check is
    against the generator's own ratio: each document's tokens must still follow from its
    chars, which means the corpus total follows from retained data two ways.
    """
    index = load_index()
    for doc in index["documents"]:
        assert doc["tokens"] == round(doc["chars"] / 3.5), (
            f"{doc['id']}: tokens {doc['tokens']} does not follow from chars {doc['chars']}"
        )
    assert sum(doc["tokens"] for doc in index["documents"]) > 0
    assert index["total_documents"] == len(index["documents"])


def test_generator_no_longer_computes_the_removed_fields():
    module_path = ROOT / "tools" / "regenerate-llm-index.py"
    # Comments may name the removed fields to explain why they are gone; code may not.
    code = "\n".join(
        line for line in module_path.read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("#")
    )
    for gone in ("line_cursor", '"lines":', '"total_tokens_estimate":'):
        assert gone not in code, (
            f"generator still emits {gone!r}; the fields are meant to be gone from the source too"
        )
