# triangular-number
Implement `triangular_number` in `triangular_number.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000]; negative numbers raise exact ValueError. Return, as an exact built-in int, the nth triangular number 0 + 1 + 2 + ... + n, which equals n*(n+1)/2 computed exactly (never a float). So 0 -> 0, 1 -> 1, 4 -> 10 and 1000000000 -> 500000000500000000.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[1]` -> `1`
- `[2]` -> `3`
- `[3]` -> `6`
- `[4]` -> `10`
- `[5]` -> `15`
- `[10]` -> `55`
- `[36]` -> `666`
- `[100]` -> `5050`
- `[1000]` -> `500500`
- `[1000000000]` -> `500000000500000000`
- `[True]` -> `raises TypeError`
- `[4.0]` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1000000001]` -> `raises ValueError`

Only edit `triangular_number.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/triangular-number/check.py --solution "$PWD/tasks/triangular-number/triangular_number.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
