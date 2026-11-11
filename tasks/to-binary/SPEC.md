# to-binary
Implement `to_binary` in `to_binary.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,18446744073709551615] (0 to 2**64 - 1); negative numbers raise exact ValueError. Return, as an exact built-in str, the base-2 digits of n using only the characters 0 and 1, most significant digit first, with no 0b prefix, sign, padding, spaces or leading zeros. 0 returns "0".

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `'0'`
- `[1]` -> `'1'`
- `[2]` -> `'10'`
- `[3]` -> `'11'`
- `[5]` -> `'101'`
- `[8]` -> `'1000'`
- `[10]` -> `'1010'`
- `[255]` -> `'11111111'`
- `[256]` -> `'100000000'`
- `[1023]` -> `'1111111111'`
- `[9223372036854775808]` -> `'1000000000000000000000000000000000000000000000000000000000000000'`
- `[18446744073709551615]` -> `'1111111111111111111111111111111111111111111111111111111111111111'`
- `[True]` -> `raises TypeError`
- `[5.0]` -> `raises TypeError`
- `['101']` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[18446744073709551616]` -> `raises ValueError`

Only edit `to_binary.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/to-binary/check.py --solution "$PWD/tasks/to-binary/to_binary.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
