# drop-value
Implement `drop_value` in `drop_value.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require items, an exact built-in list of at most 1000 exact built-in ints, and value, an exact built-in int; every number (including value) must be in [-1000000000,1000000000]. Return a fresh exact built-in list holding the elements of items that are not equal to value, in their original order. Remove every match, including adjacent repeated matches such as drop_value([1, 1, 2], 1) == [2]. Never change items, and never return items itself, also when nothing is removed (drop_value(items, value) must be a new list even if value does not occur). [] returns [].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 1]` -> `[]`
- `[[1], 1]` -> `[]`
- `[[1], 2]` -> `[1]`
- `[[1, 1, 2], 1]` -> `[2]`
- `[[1, 2, 1, 3, 1], 1]` -> `[2, 3]`
- `[[2, 2, 2], 2]` -> `[]`
- `[[3, 1, 2], 5]` -> `[3, 1, 2]`
- `[[0, -1, 0, -1], -1]` -> `[0, 0]`
- `[[5, 4, 5, 4, 5], 5]` -> `[4, 4]`
- `[[1, 2, 3], 2]` -> `[1, 3]`
- `[[1, True], 1]` -> `raises TypeError`
- `[None, 1]` -> `raises TypeError`
- `['12', 1]` -> `raises TypeError`
- `[[1], 1.0]` -> `raises TypeError`
- `[[1], 1000000001]` -> `raises ValueError`
- `[[-1000000001], 0]` -> `raises ValueError`

Only edit `drop_value.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/drop-value/check.py --solution "$PWD/tasks/drop-value/drop_value.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
