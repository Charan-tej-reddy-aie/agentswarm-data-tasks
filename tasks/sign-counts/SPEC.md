# sign-counts
Implement `sign_counts` in `sign_counts.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return a fresh exact built-in dict with exactly the keys negative, zero and positive. Each value is an exact built-in int counting the elements < 0, == 0 and > 0 respectively; duplicates count every time. Empty input returns all three counts as 0.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `{'negative': 0, 'zero': 0, 'positive': 0}`
- `[[-1, 0, 1]]` -> `{'negative': 1, 'zero': 1, 'positive': 1}`
- `[[5, 5, -5]]` -> `{'negative': 1, 'zero': 0, 'positive': 2}`
- `[[0, 0]]` -> `{'negative': 0, 'zero': 2, 'positive': 0}`
- `[[-3, -2, -1]]` -> `{'negative': 3, 'zero': 0, 'positive': 0}`
- `[[-1000000000, 1000000000]]` -> `{'negative': 1, 'zero': 0, 'positive': 1}`
- `[[True]]` -> `raises TypeError`
- `[[-1000000001]]` -> `raises ValueError`

Only edit `sign_counts.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/sign-counts/check.py --solution "$PWD/tasks/sign-counts/sign_counts.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
