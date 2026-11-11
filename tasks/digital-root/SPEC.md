# digital-root
Implement `digital_root` in `digital_root.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000000000000] (0 to 10**18); negative numbers raise exact ValueError. Replace n by the sum of its decimal digits, again and again, until it has a single decimal digit, and return that digit as an exact built-in int. Numbers 0 to 9 are returned unchanged, so digital_root(0) is 0 and digital_root(9) is 9; digital_root(99) is 9 (99 -> 18 -> 9). Use exact integer arithmetic, never floats.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[1]` -> `1`
- `[5]` -> `5`
- `[9]` -> `9`
- `[10]` -> `1`
- `[11]` -> `2`
- `[18]` -> `9`
- `[19]` -> `1`
- `[38]` -> `2`
- `[99]` -> `9`
- `[100]` -> `1`
- `[123]` -> `6`
- `[999]` -> `9`
- `[12345]` -> `6`
- `[987654321]` -> `9`
- `[True]` -> `raises TypeError`
- `[9.0]` -> `raises TypeError`
- `['9']` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `digital_root.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/digital-root/check.py --solution "$PWD/tasks/digital-root/digital_root.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
