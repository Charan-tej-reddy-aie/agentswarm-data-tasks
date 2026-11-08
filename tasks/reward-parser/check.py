"""Pinned stdlib-only exact reward parsing check; offline synthetic inputs."""
import argparse
from decimal import Decimal
import json
from pathlib import Path
import random
import subprocess
import sys
HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--solution", type=Path, default=HERE / "reward_parser.py")
source = p.parse_args().solution.resolve()
assert source.is_file(), "missing implementation"
cases = json.loads((HERE / "fixtures/cases.json").read_text())
rng = random.Random(146604)
for _ in range(36):
    whole, cents = rng.randrange(1, 100000), rng.randrange(100)
    amount = f"{whole}.{cents:02}"
    token, kind = rng.choice([("USD", "cash"), ("USDC", "crypto"), ("XTR", "points"), ("CREDITS", "site-balance")])
    text = rng.choice([f"{amount} {token}", f"{token.lower()}  {amount}", f"Reward: {amount} {token.lower()} (test fixture)"])
    cases.append(dict(text=text, amount=amount, currency=token, kind=kind))
proc = subprocess.run([sys.executable, "-I", str(HERE / "worker.py"), str(source)],
    input=json.dumps([r["text"] for r in cases]), capture_output=True, text=True, timeout=15)
assert proc.returncode == 0, proc.stderr[-2000:]
actual = json.loads(proc.stdout)
assert type(actual) is list and len(actual) == len(cases), "wrong result count"
for expected, value in zip(cases, actual):
    assert set(value) == {"amount", "currency", "kind"}, "bad output keys"
    target = expected["amount"]
    assert (value["amount"] is None if target is None else value["amount"] is not None and Decimal(value["amount"]) == Decimal(target)), (expected["text"], value, expected)
    assert value["currency"] == expected["currency"] and value["kind"] == expected["kind"], (expected["text"], value, expected)
print(f"PASS reward-parser: {len(cases)} exact typed cases ({len(cases)-36} authored + 36 generated)")
