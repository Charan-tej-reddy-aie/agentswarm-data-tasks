# count-runs
Implement `count_runs` in `count_runs.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require an exact built-in list of at most 1000 exact built-in strings, each at most 64 Unicode code points. Return an exact built-in int counting maximal consecutive groups of equal strings. Empty input returns 0. Equality is exact: no trimming, normalization or case folding. Equal values separated by another value start a new run.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `0`
- `[['a']]` -> `1`
- `[['a', 'a', 'b', 'a']]` -> `3`
- `[['a', 'b', 'a']]` -> `3`
- `[['A', 'a', 'a']]` -> `2`
- `[['', ' ', '']]` -> `3`
- `[['é', 'é']]` -> `2`
- `[['éééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééé', 'éééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééé']]` -> `1`

Only edit `count_runs.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/count-runs/check.py --solution "$PWD/tasks/count-runs/count_runs.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
