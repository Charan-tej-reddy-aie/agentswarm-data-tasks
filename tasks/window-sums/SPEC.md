# window-sums
Implement `window_sums` in `window_sums.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000], and size, an exact built-in int in [1,1000]. Return a fresh exact built-in list with the sum of every contiguous window of exactly size elements, in order: element i is sum(values[i:i+size]) for i from 0 to len(values)-size inclusive. Windows overlap. When size > len(values) there are no complete windows and the result is a fresh []. Never return partial windows.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], 1]` -> `[]`
- `[[1, 2, 3, 4], 2]` -> `[3, 5, 7]`
- `[[1, 2, 3], 3]` -> `[6]`
- `[[1, 2], 3]` -> `[]`
- `[[5, -5, 5], 1]` -> `[5, -5, 5]`
- `[[1, 2, 3, 4, 5], 3]` -> `[6, 9, 12]`
- `[[0, 0, 0], 2]` -> `[0, 0]`
- `[[1000000000, 1000000000], 2]` -> `[2000000000]`
- `[[-1, -2, -3], 2]` -> `[-3, -5]`
- `[[1], 0]` -> `raises ValueError`
- `[[1], True]` -> `raises TypeError`

Only edit `window_sums.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/window-sums/check.py --solution "$PWD/tasks/window-sums/window_sums.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
