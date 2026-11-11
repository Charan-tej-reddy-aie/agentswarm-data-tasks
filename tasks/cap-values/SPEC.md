# cap-values
Implement `cap_values` in `cap_values.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require items, an exact built-in list of at most 1000 exact built-in ints, and limit, an exact built-in int; every number (including limit) must be in [-1000000000,1000000000]. Return a fresh exact built-in list of the same length where each element of items is replaced by the smaller of that element and limit (min(x, limit)), in the original order. Cap every element, including the last one, such as cap_values([1, 9, 9], 5) == [1, 5, 5]. Never change items, and never return items itself, also when no element is above limit (cap_values(items, limit) must be a new list even if nothing changes). [] returns [].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 5]` -> `[]`
- `[[1], 5]` -> `[1]`
- `[[9], 5]` -> `[5]`
- `[[1, 9, 9], 5]` -> `[1, 5, 5]`
- `[[9, 9, 9], 5]` -> `[5, 5, 5]`
- `[[1, 2, 3], 9]` -> `[1, 2, 3]`
- `[[5, 6, 5], 5]` -> `[5, 5, 5]`
- `[[0, -3, 4], -1]` -> `[-1, -3, -1]`
- `[[7, 1, 7], 0]` -> `[0, 0, 0]`
- `[[-5, 5], -5]` -> `[-5, -5]`
- `[[1, True], 1]` -> `raises TypeError`
- `[None, 1]` -> `raises TypeError`
- `['12', 1]` -> `raises TypeError`
- `[[1], 1.0]` -> `raises TypeError`
- `[[1], 1000000001]` -> `raises ValueError`
- `[[-1000000001], 0]` -> `raises ValueError`

Only edit `cap_values.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/cap-values/check.py --solution "$PWD/tasks/cap-values/cap_values.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
