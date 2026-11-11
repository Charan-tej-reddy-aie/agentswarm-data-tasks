# digit-product
Implement `digit_product` in `digit_product.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000000000000000000] (0 to 10**18); negative numbers raise exact ValueError. Return, as an exact built-in int, the product of all decimal digits of n written without leading zeros. Every digit counts, including zeros, so any n containing a 0 digit returns 0 and digit_product(0) is 0; digit_product(7) is 7 and digit_product(234) is 24. Use exact integer arithmetic, never floats.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[1]` -> `1`
- `[7]` -> `7`
- `[9]` -> `9`
- `[10]` -> `0`
- `[11]` -> `1`
- `[12]` -> `2`
- `[25]` -> `10`
- `[39]` -> `27`
- `[99]` -> `81`
- `[100]` -> `0`
- `[123]` -> `6`
- `[234]` -> `24`
- `[999]` -> `729`
- `[1111]` -> `1`
- `[987654321]` -> `362880`
- `[True]` -> `raises TypeError`
- `[12.0]` -> `raises TypeError`
- `['12']` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1000000000000000001]` -> `raises ValueError`

Only edit `digit_product.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/digit-product/check.py --solution "$PWD/tasks/digit-product/digit_product.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
