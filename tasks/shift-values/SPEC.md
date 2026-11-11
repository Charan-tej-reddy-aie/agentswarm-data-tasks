# shift-values
Implement `shift_values` in `shift_values.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require items, an exact built-in list of at most 1000 exact built-in ints, and delta, an exact built-in int; every number (including delta) must be in [-1000000000,1000000000]. Return a fresh exact built-in list of the same length where delta is added to each element of items (x + delta), in the original order. Shift every element, including the first one, such as shift_values([1, 2, 3], 10) == [11, 12, 13]. Never change items, and never return items itself, also when delta is 0 (shift_values(items, 0) must be a new list). [] returns [].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 5]` -> `[]`
- `[[1], 0]` -> `[1]`
- `[[1], 5]` -> `[6]`
- `[[1, 2, 3], 10]` -> `[11, 12, 13]`
- `[[1, 2, 3], 0]` -> `[1, 2, 3]`
- `[[5, 5], -5]` -> `[0, 0]`
- `[[0, -3, 4], -1]` -> `[-1, -4, 3]`
- `[[7], 7]` -> `[14]`
- `[[9, 8, 7], -10]` -> `[-1, -2, -3]`
- `[[-1, 1], 1]` -> `[0, 2]`
- `[[1, True], 1]` -> `raises TypeError`
- `[None, 1]` -> `raises TypeError`
- `['12', 1]` -> `raises TypeError`
- `[[1], 1.0]` -> `raises TypeError`
- `[[1], 1000000001]` -> `raises ValueError`
- `[[-1000000001], 0]` -> `raises ValueError`

Only edit `shift_values.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/shift-values/check.py --solution "$PWD/tasks/shift-values/shift_values.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
