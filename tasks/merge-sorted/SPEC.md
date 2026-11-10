# merge-sorted
Implement `merge_sorted` in `merge_sorted.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require two exact built-in lists, each at most 1000 exact built-in ints in [-1000000000,1000000000]. Each list must already be sorted nondecreasing (duplicates allowed); an unsorted input raises exact ValueError. Return a fresh exact built-in list containing every value from both inputs (duplicates kept), sorted nondecreasing. Its length is len(left)+len(right). The result is a fresh list even when one input is empty.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges/order, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], []]` -> `[]`
- `[[1, 3, 5], [2, 4]]` -> `[1, 2, 3, 4, 5]`
- `[[1, 2], []]` -> `[1, 2]`
- `[[], [0, 0]]` -> `[0, 0]`
- `[[1, 1], [1]]` -> `[1, 1, 1]`
- `[[4, 5, 6], [1, 2, 3]]` -> `[1, 2, 3, 4, 5, 6]`
- `[[2], [1, 3, 3]]` -> `[1, 2, 3, 3]`
- `[[-5, 0, 9], [-7, 10]]` -> `[-7, -5, 0, 9, 10]`
- `[[1000000000], [-1000000000]]` -> `[-1000000000, 1000000000]`
- `[[2, 1], []]` -> `raises ValueError`
- `[[1], [True]]` -> `raises TypeError`

Only edit `merge_sorted.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/merge-sorted/check.py --solution "$PWD/tasks/merge-sorted/merge_sorted.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
