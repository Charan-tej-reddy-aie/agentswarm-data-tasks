# trailing-zero-bits
Implement `trailing_zero_bits` in `trailing_zero_bits.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [1,1000000000000000000]; 0 and negative numbers raise exact ValueError. Return, as an exact built-in int, how many 0 bits follow the lowest 1 bit in the binary representation of n (so 1 -> 0, 8 -> 3, 12 -> 2, 40 -> 3). Do not count leading bits, all 0 bits, 1 bits or decimal zeros.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[1]` -> `0`
- `[2]` -> `1`
- `[3]` -> `0`
- `[4]` -> `2`
- `[6]` -> `1`
- `[8]` -> `3`
- `[12]` -> `2`
- `[40]` -> `3`
- `[96]` -> `5`
- `[1000]` -> `3`
- `[1024]` -> `10`
- `[576460752303423488]` -> `59`
- `[1000000000000000000]` -> `18`
- `[7696581394432]` -> `40`
- `[True]` -> `raises TypeError`
- `[4.0]` -> `raises TypeError`
- `[0]` -> `raises ValueError`
- `[-8]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `trailing_zero_bits.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/trailing-zero-bits/check.py --solution "$PWD/tasks/trailing-zero-bits/trailing_zero_bits.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
