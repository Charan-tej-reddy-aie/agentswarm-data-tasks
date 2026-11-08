"""Typed adapter; labels stay in the trusted parent check."""
from decimal import Decimal
import json
import runpy
import sys
sys.dont_write_bytecode = True
parse = runpy.run_path(sys.argv[1], run_name="candidate")["parse_reward"]
result = []
for text in json.load(sys.stdin):
    value = parse(text)
    assert type(value) is dict and set(value) == {"amount", "currency", "kind"}, "exact dict keys required"
    amount, currency, kind = value["amount"], value["currency"], value["kind"]
    assert amount is None or (type(amount) is Decimal and amount.is_finite() and amount >= 0), "amount must be a finite nonnegative Decimal or None"
    assert currency is None or type(currency) is str, "currency must be str or None"
    assert type(kind) is str, "kind must be str"
    result.append({"amount": str(amount) if amount is not None else None, "currency": currency, "kind": kind})
print(json.dumps(result, allow_nan=False))
