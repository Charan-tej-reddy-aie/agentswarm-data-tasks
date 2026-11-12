# collatz-steps
Implement `collatz_steps` in `collatz_steps.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [1,1000000000000] (1 to 10**12); 0 and negative numbers raise exact ValueError. Repeatedly replace n by n // 2 when n is even and by 3*n + 1 when n is odd, until n equals 1. Return, as an exact built-in int, the number of replacements made. collatz_steps(1) is 0. Use exact integer arithmetic (intermediate values can exceed 2**53, so never use floats or the / operator). Every allowed n reaches 1 within a few thousand steps; each call should take well under a second.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[1]` -> `0`
- `[2]` -> `1`
- `[3]` -> `7`
- `[4]` -> `2`
- `[5]` -> `5`
- `[6]` -> `8`
- `[7]` -> `16`
- `[8]` -> `3`
- `[16]` -> `4`
- `[27]` -> `111`
- `[97]` -> `118`
- `[871]` -> `178`
- `[True]` -> `raises TypeError`
- `[6.0]` -> `raises TypeError`
- `[0]` -> `raises ValueError`
- `[-5]` -> `raises ValueError`
- `[1000000000001]` -> `raises ValueError`

Only edit `collatz_steps.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/collatz-steps/check.py --solution "$PWD/tasks/collatz-steps/collatz_steps.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
