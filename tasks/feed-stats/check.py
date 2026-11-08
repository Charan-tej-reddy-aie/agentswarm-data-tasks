"""Offline acceptance for the task-feed summary CLI."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "checks"))
from common import load, solution

TASK = "feed-stats"
SOURCE = solution(Path(__file__).with_name("feed_stats.py"))
RUNS = 0

def run_text(text, expected=None):
    global RUNS
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "input.json"
        path.write_text(text)
        proc = subprocess.run([sys.executable, "-I", str(SOURCE), str(path)],
                              capture_output=True, text=True, timeout=5)
    RUNS += 1
    if expected is None:
        assert proc.returncode != 0 and proc.stderr.strip() and not proc.stdout.strip(), "invalid input must fail clearly"
        return
    assert proc.returncode == 0, proc.stderr[-1000:]
    actual = json.loads(proc.stdout)
    assert isinstance(actual, dict) and actual.keys() == expected.keys(), actual
    assert type(actual["total"]) is int, "total must be an integer"
    for key in ("by_status", "reward_buckets"):
        assert isinstance(actual[key], dict) and all(type(v) is int for v in actual[key].values())
    assert isinstance(actual["top_tags"], list)
    assert all(isinstance(t, dict) and type(t.get("count")) is int for t in actual["top_tags"])
    age = expected["median_age_hours"]
    if age is None:
        assert actual["median_age_hours"] is None
    else:
        observed = actual["median_age_hours"]
        assert type(observed) in (int, float) and abs(observed - age) <= 1e-6, actual
    actual["median_age_hours"] = age
    assert actual == expected, f"expected {expected}, got {actual}"

def check(feed, expected=None):
    run_text(json.dumps(feed), expected)

page = load(TASK, "page")
check(page, load(TASK, "summary"))
check({"items": [], "now": page["now"]}, {"total": 0, "by_status": {},
      "reward_buckets": dict.fromkeys(["none", "text", "under_10", "at_least_10"], 0),
      "median_age_hours": None, "top_tags": []})

future = {"items": [{"id": "future-only", "type": "task", "status": "open", "tags": [],
                     "createdAt": "2026-11-09T12:00:00Z"}], "now": page["now"]}
check(future, {"total": 1, "by_status": {"open": 1},
              "reward_buckets": {"none": 1, "text": 0, "under_10": 0, "at_least_10": 0},
              "median_age_hours": 0, "top_tags": []})

# Construct independent oracles from chosen categories and ages, not by summarising input.
rng = random.Random(1466)
for iteration in range(14):
    now = datetime(2026, 11, 8, 12, 30, 30, 123456, tzinfo=timezone.utc)
    counts = dict.fromkeys(["none", "text", "under_10", "at_least_10"], 0)
    statuses = {}
    tag_counts = {}
    age_values = []
    rows = []
    categories = [(None, "none"), ({}, "none"), ({"reward": " \t"}, "none"),
        ({"amountUsd": 0}, "none"), ({"reward": "$500 credit"}, "text"),
        ({"amountUsd": 0, "reward": "credit"}, "text"),
        ({"amountUsd": 0.01}, "under_10"), ({"amountUsd": 9.99}, "under_10"),
        ({"amountUsd": 10, "reward": "unpaid"}, "at_least_10"),
        ({"amountUsd": 100}, "at_least_10")]
    for i in range(iteration + 1):
        bounty, category = categories[(iteration + i) % len(categories)]
        counts[category] += 1
        status = rng.choice(["open", "accepted", "answered", "closed", "future-status"])
        statuses[status] = statuses.get(status, 0) + 1
        tag = rng.choice(["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "écho"])
        tag_counts[tag] = tag_counts.get(tag, 0) + 1
        age = rng.choice([-2, 0, 0.5, 1, 2.25, 14, 42])
        age_values.append(max(0, age))
        offset = timezone(timedelta(hours=rng.choice([-7, 0, 5.5])))
        row = {"id": f"generated-{iteration}-{i}", "type": "task", "status": status,
            "createdAt": (now - timedelta(hours=age)).astimezone(offset).isoformat(),
            "tags": [f" {tag.upper()} ", tag, ""], "bounty": bounty,
            "body": "Synthetic ignored field", "unused": True}
        if bounty is None and i % 2:
            del row["bounty"]
        rows.append(row)
    ages = sorted(age_values)
    mid = len(ages) // 2
    median = ages[mid] if len(ages) % 2 else (ages[mid-1] + ages[mid]) / 2
    expected = {"total": len(rows), "by_status": statuses, "reward_buckets": counts,
        "median_age_hours": median,
        "top_tags": [{"tag": t, "count": n} for t, n in sorted(tag_counts.items(), key=lambda p: (-p[1], p[0]))[:5]]}
    rng.shuffle(rows)
    check({"items": rows, "now": now.isoformat(), "nextCursor": "ignored"}, expected)

for raw in ("not json", "{} trailing", "[]", "null", '{"items":[],"now":"bad"}', "{}"):
    run_text(raw)
for key, bad in [("type", "note"), ("type", None), ("status", ""), ("status", 1),
    ("createdAt", "2026-11-08T10:00:00"), ("createdAt", "tomorrow"), ("createdAt", 0),
    ("tags", "python"), ("tags", [1]), ("tags", ["valid-tag", 1]),
    ("id", ""), ("id", 4), ("bounty", []),
    ("bounty", {"amountUsd": True}), ("bounty", {"amountUsd": -1}),
    ("bounty", {"amountUsd": "10"}), ("bounty", {"amountUsd": None}),
    ("bounty", {"amountUsd": float("inf")}), ("bounty", {"amountUsd": float("nan")}),
    ("bounty", {"reward": None}), ("bounty", {"reward": 4})]:
    bad_page = copy.deepcopy(page)
    bad_page["items"][0][key] = bad
    check(bad_page)
for field in ("id", "type", "status", "createdAt", "tags"):
    bad_page = copy.deepcopy(page)
    del bad_page["items"][0][field]
    check(bad_page)
bad_page = copy.deepcopy(page)
bad_page["items"].append(bad_page["items"][0])
check(bad_page)
for field, bad in [("now", "2026-11-08"), ("now", None), ("items", {}), ("items", [None])]:
    bad_page = copy.deepcopy(page)
    bad_page[field] = bad
    check(bad_page)
for args in ([], ["/nonexistent/synthetic-input.json"], ["one", "two"]):
    proc = subprocess.run([sys.executable, "-I", str(SOURCE), *args], capture_output=True, text=True, timeout=5)
    assert proc.returncode and proc.stderr.strip() and not proc.stdout.strip(), "file/arity error must be clear"
print(f"PASS feed-stats: {RUNS} feed cases + 3 CLI errors")
