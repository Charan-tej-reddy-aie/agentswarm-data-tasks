# Implementation notes

- Exact type checks with `type(...) is` reject all subclasses including bool (since `type(True) is bool`).
- Shape and type validation complete before any bound checks.
- Python's stable `sorted` preserves input order for fully tied (score, bid, id) rows.
- Returns a fresh list; input is never mutated.
- Stdlib only.
