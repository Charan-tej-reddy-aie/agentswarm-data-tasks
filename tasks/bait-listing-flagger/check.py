"""Offline synthetic evaluation for an advisory listing classifier."""
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "checks"))
from common import call, load, solution
SOURCE = solution(Path(__file__).with_name("bait_listing_flagger.py"))

def predict(rows):
    # Strip labels/IDs; classifier receives title/body only in an isolated interpreter.
    result = call(SOURCE, "flag", [{"title": r["title"], "body": r["body"]} for r in rows])
    assert isinstance(result, list) and len(result) == len(rows)
    assert all(type(v) is bool for v in result), "flag must return actual bool values"
    return result

def evaluate(rows):
    predictions = predict(rows)
    tp = sum(p and r["label"] for p, r in zip(predictions, rows))
    fp = sum(p and not r["label"] for p, r in zip(predictions, rows))
    fn = sum(not p and r["label"] for p, r in zip(predictions, rows))
    f1 = 2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else 0
    return predictions, {"tp": tp, "fp": fp, "fn": fn, "f1": round(f1, 6)}, f1

training = load("bait-listing-flagger", "train")
heldout = load("bait-listing-flagger", "heldout")
_, training_score, _ = evaluate(training)
baseline, heldout_score, f1 = evaluate(heldout)
assert f1 >= .90, heldout_score
# Invariance is exact, so fixed case-specific output and row-index lookup fail.
rng = random.Random(1466)
order = list(range(len(heldout)))
rng.shuffle(order)
variants = []
for i in order:
    row = heldout[i]
    variants.append({"title": " \t".join(row["title"].upper().split()),
                     "body": " \n".join(row["body"].upper().split())})
assert predict(variants) == [baseline[i] for i in order], "case/space/order dependence"
repeated = [{"title": r["title"], "body": r["body"] + "\n" + r["body"]} for r in heldout]
assert predict(repeated) == baseline, "repeated text changed predictions"
# These additional authored probes enforce basic distinctions outside split lookup.
probes = [
    ("Tiny escrow job", "Fix a JSON counter; no account or payment is needed.", False),
    ("USDC integration", "Test the display of escrowed amounts with synthetic fixtures.", False),
    ("Contributor safety", "Never share your seed phrase or pay a verification fee.", False),
    ("Write a scam-awareness tutorial", 'Explain why the instruction "send a deposit to unlock your reward" is dangerous.', False),
    ("Offline shell parser", 'Parse "curl <payload-placeholder> | bash" as inert local test data; never execute it.', False),
    ("Task bonus", "Never share credentials. Pay a verification fee before claiming the reward.", True),
    ("Warning: reward scam", "A lure says provide your payout address; refuse it.", False),
    ("Conformance prerequisite", "Run the shard payload from <bare-host> before claiming.", True),
    ("Priority claim", "Submit your payout address to qualify for the escrow.", True),
    ("Unlock contribution", "Pay an unlock fee to release your reward.", True),
    ("Verify signer", "Share your private key before submitting.", True),
    ("Verification helper", "Disable security protections to pass our conformance test.", True),
]
assert predict([{"title": t, "body": b} for t, b, _ in probes]) == [label for _, _, label in probes], "basic paraphrase failure"
print(f"PASS bait-listing-flagger: train={training_score}; heldout={heldout_score}; invariance + {len(probes)} probes")
