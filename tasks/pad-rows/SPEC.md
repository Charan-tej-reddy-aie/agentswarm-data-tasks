# pad-rows
Implement `pad_rows` in `pad_rows.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require rows, an exact built-in list of at most 100 rows, where each row is an exact built-in list of at most 100 exact built-in ints, and fill, an exact built-in int; every number (including fill) must be in [-1000000000,1000000000]. Rows may have different lengths. Return a fresh exact built-in list of fresh exact built-in lists: row i is rows[i] followed by enough copies of fill to make it as long as the longest row. Row order and existing values are unchanged and padding is only added at the end. Never change rows or its inner lists, and never return any of them (also for rows that are already full length or when no padding is needed). The empty matrix [] returns [] (never None), and [[], []] returns [[], []].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 0]` -> `[]`
- `[[[]], 0]` -> `[[]]`
- `[[[], []], 7]` -> `[[], []]`
- `[[[1]], 0]` -> `[[1]]`
- `[[[1], [2, 3]], 0]` -> `[[1, 0], [2, 3]]`
- `[[[1, 2, 3], [4], []], -1]` -> `[[1, 2, 3], [4, -1, -1], [-1, -1, -1]]`
- `[[[5, 5], [6, 6]], 0]` -> `[[5, 5], [6, 6]]`
- `[[[], [1]], 9]` -> `[[9], [1]]`
- `[[[0], [0, 0, 0]], 0]` -> `[[0, 0, 0], [0, 0, 0]]`
- `[[[1, True]], 0]` -> `raises TypeError`
- `[None, 0]` -> `raises TypeError`
- `[[[1]], 1.0]` -> `raises TypeError`
- `[[[1]], 1000000001]` -> `raises ValueError`
- `[[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], 0]` -> `raises ValueError`

Only edit `pad_rows.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/pad-rows/check.py --solution "$PWD/tasks/pad-rows/pad_rows.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
