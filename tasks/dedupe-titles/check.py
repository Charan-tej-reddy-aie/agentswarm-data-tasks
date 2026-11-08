"""Offline acceptance of connected duplicate-title components."""
import itertools
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "checks"))
from common import call, load, solution
SOURCE = solution(Path(__file__).with_name("dedupe_titles.py"))

def predict(rows):
    result = call(SOURCE, "find_duplicates", rows)
    assert isinstance(result, list), "result must be a list"
    valid = {r["id"] for r in rows}
    seen = set()
    for group in result:
        assert isinstance(group, list) and len(group) >= 2, "only non-singleton groups"
        assert all(isinstance(r, str) and r in valid for r in group), "unknown IDs"
        assert len(set(group)) == len(group) and not seen.intersection(group), "repeated ID"
        seen.update(group)
        assert group == sorted(group), "group IDs must be sorted"
    assert result == sorted(result), "groups must be sorted"
    return result

fixture = load("dedupe-titles", "pairs")
groups = predict(fixture["rows"])
predicted = {tuple(sorted(pair)) for group in groups for pair in itertools.combinations(group, 2)}
positive = {(p["left"], p["right"]) for p in fixture["pairs"] if p["duplicate"]}
all_pairs = {tuple(sorted((a["id"], b["id"]))) for a, b in itertools.combinations(fixture["rows"], 2)}
assert {tuple(sorted((p["left"], p["right"]))) for p in fixture["pairs"]} == all_pairs
true_positive = len(predicted & positive)
precision = true_positive / len(predicted) if predicted else 0
recall = true_positive / len(positive)
assert precision >= .95 and recall >= .95, (precision, recall)

cases = [
    (["Clean CSV #12", " clean csv 99!!!", "unrelated widgets"], [[0, 1]]),
    (["alpha beta gamma delta", "delta gamma beta alpha alpha", "alpha beta gamma delta extra"], [[0, 1, 2]]),
    # A-B and B-C exactly .8, A-C .6: connected components, not greedy cliques.
    (["alpha beta gamma delta", "alpha beta gamma delta epsilon", "beta gamma delta epsilon"], [[0, 1, 2]]),
    (["alpha beta gamma", "alpha beta gamma delta", "other content"], []),
    (["   ", "!!!", "", "unrelated"], []),
    (["ＣＳＶ straße v１２", "csv STRASSE v99", "csv Straße v2!"], [[0, 1, 2]]),
    (["Parse ١٢ CSV rows", "parse 99 csv rows", "parse १२ csv rows"], [[0, 1, 2]]),
    (["a_b-c", "C B A", "x y z", "z y x"], [[0, 1], [2, 3]]),
    ([], []), (["singleton title"], []),
]
rng = random.Random(1466)
checks = 0
for iteration in range(5):
    for titles, indices in cases:
        # Unique opaque IDs change per invocation; title vocabulary also varies.
        nonce = "".join(rng.choice("abcdefghijk") for _ in range(12))
        rows = [{"id": f"id-{rng.randrange(10**12):012}", "title": t.replace("alpha", nonce)} for t in titles]
        expected = sorted(sorted(rows[i]["id"] for i in group) for group in indices)
        rng.shuffle(rows)
        assert predict(rows) == expected, (titles, expected)
        checks += 1
print(f"PASS dedupe-titles: precision={precision:.3f} recall={recall:.3f}; {checks} contract cases")
