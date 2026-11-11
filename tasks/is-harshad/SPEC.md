# is-harshad
Implement `is_harshad` in `is_harshad.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [1,1000000000000000000] (1 to 10**18); 0 and negative numbers raise exact ValueError. Return the exact built-in bool True when n is divisible by the sum of its decimal digits, otherwise False. So 1 to 10 are True, 12 and 18 are True, 11 and 19 are False. The answer must be exact for every allowed n: never use float division, which is not precise near 10**18; use the integer % operator.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[1]` -> `True`
- `[2]` -> `True`
- `[9]` -> `True`
- `[10]` -> `True`
- `[11]` -> `False`
- `[12]` -> `True`
- `[13]` -> `False`
- `[18]` -> `True`
- `[19]` -> `False`
- `[20]` -> `True`
- `[21]` -> `True`
- `[100]` -> `True`
- `[101]` -> `False`
- `[111]` -> `True`
- `[112]` -> `True`
- `[1729]` -> `True`
- `[True]` -> `raises TypeError`
- `[12.0]` -> `raises TypeError`
- `[0]` -> `raises ValueError`
- `[-12]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `is_harshad.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/is-harshad/check.py --solution "$PWD/tasks/is-harshad/is_harshad.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
