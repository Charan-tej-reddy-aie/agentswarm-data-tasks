# take-every
Implement `take_every` in `take_every.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in strings, each at most 64 Unicode code points. step is an exact built-in int in [1,1000] (independent of len(items)). Return a fresh exact built-in list of the items at indices 0, step, 2*step, ... in order, i.e. items[::step]. Index 0 is always included when items is nonempty. Preserve duplicates; strings are opaque (no trimming, normalization or case folding). The result is a fresh list even when step is 1.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges/order, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 1]` -> `[]`
- `[['a', 'b', 'c', 'd', 'e'], 2]` -> `['a', 'c', 'e']`
- `[['a', 'b', 'c'], 1]` -> `['a', 'b', 'c']`
- `[['a', 'b', 'c'], 3]` -> `['a']`
- `[['a', 'b', 'c', 'd'], 3]` -> `['a', 'd']`
- `[['a', 'b'], 1000]` -> `['a']`
- `[['A', 'b', 'C'], 2]` -> `['A', 'C']`
- `[['x', 'x', 'y', 'x'], 2]` -> `['x', 'y']`
- `[['é', '', ' ', 'é'], 2]` -> `['é', ' ']`
- `[['a'], 0]` -> `raises ValueError`
- `[['a'], True]` -> `raises TypeError`

Only edit `take_every.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/take-every/check.py --solution "$PWD/tasks/take-every/take_every.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
