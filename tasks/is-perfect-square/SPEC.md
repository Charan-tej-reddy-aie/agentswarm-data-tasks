# is-perfect-square
Implement `is_perfect_square` in `is_perfect_square.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000000000000] (0 to 10**18); negative numbers raise exact ValueError. Return the exact built-in bool True when n equals k*k for some integer k, otherwise False. 0 and 1 are perfect squares. The answer must be exact for every allowed n: a floating-point square root is not precise enough near 10**18 (for example 10**18 - 1 is not a square), so use integer arithmetic such as math.isqrt.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `True`
- `[1]` -> `True`
- `[2]` -> `False`
- `[3]` -> `False`
- `[4]` -> `True`
- `[8]` -> `False`
- `[9]` -> `True`
- `[15]` -> `False`
- `[16]` -> `True`
- `[24]` -> `False`
- `[25]` -> `True`
- `[99]` -> `False`
- `[100]` -> `True`
- `[1000000000000000000]` -> `True`
- `[999999999999999999]` -> `False`
- `[True]` -> `raises TypeError`
- `[16.0]` -> `raises TypeError`
- `[-4]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `is_perfect_square.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/is-perfect-square/check.py --solution "$PWD/tasks/is-perfect-square/is_perfect_square.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
