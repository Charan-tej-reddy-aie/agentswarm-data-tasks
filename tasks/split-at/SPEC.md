# split-at
Implement `split_at` in `split_at.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in strings, each at most 64 Unicode code points. index is an exact built-in int in [0,len(items)]. Return a fresh exact built-in list containing two fresh exact built-in lists: items[:index] and items[index:]. Preserve order and duplicates. The two inner lists must be distinct from one another and from the input, even when empty.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 0]` -> `[[], []]`
- `[['a', 'b', 'a'], 1]` -> `[['a'], ['b', 'a']]`
- `[['x'], 0]` -> `[[], ['x']]`
- `[['x'], 1]` -> `[['x'], []]`
- `[['é', 'é', ''], 2]` -> `[['é', 'é'], ['']]`

Only edit `split_at.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/split-at/check.py --solution "$PWD/tasks/split-at/split_at.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
