# is-armstrong
Implement `is_armstrong` in `is_armstrong.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000000000] (0 to 10**15); negative numbers raise exact ValueError. Let k be the number of decimal digits of n (written without leading zeros; 0 has one digit). Return the exact built-in bool True when n equals the sum of each of its decimal digits raised to the power k, otherwise False. So 0 to 9 are all True, 153 = 1**3 + 5**3 + 3**3 is True, 9474 is True and 10 and 100 are False. Use exact integer arithmetic.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `True`
- `[1]` -> `True`
- `[5]` -> `True`
- `[9]` -> `True`
- `[10]` -> `False`
- `[11]` -> `False`
- `[100]` -> `False`
- `[153]` -> `True`
- `[154]` -> `False`
- `[370]` -> `True`
- `[371]` -> `True`
- `[407]` -> `True`
- `[1634]` -> `True`
- `[8208]` -> `True`
- `[9474]` -> `True`
- `[9475]` -> `False`
- `[True]` -> `raises TypeError`
- `[153.0]` -> `raises TypeError`
- `['153']` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1000000000000001]` -> `raises ValueError`

Only edit `is_armstrong.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/is-armstrong/check.py --solution "$PWD/tasks/is-armstrong/is_armstrong.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
