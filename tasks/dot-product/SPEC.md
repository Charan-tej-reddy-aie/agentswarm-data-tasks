# dot-product
Implement `dot_product` in `dot_product.py`. Python 3.11+ standard library only.

Require a and b, two exact built-in lists of at most 1000 exact built-in ints each, every int in [-1000000000,1000000000]. Both lists must have the same length; different lengths raise exact ValueError. Return, as an exact built-in int, a[0]*b[0] + a[1]*b[1] + ... using the signed values (no overflow: Python ints are exact). Two empty lists return 0.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[], []]` -> `0`
- `[[2], [3]]` -> `6`
- `[[1, 2, 3], [4, 5, 6]]` -> `32`
- `[[-1, 2], [3, 4]]` -> `5`
- `[[1, -1], [1, 1]]` -> `0`
- `[[0, 0], [5, 7]]` -> `0`
- `[[-2, -3], [-4, -5]]` -> `23`
- `[[10, 0, 1], [0, 10, 2]]` -> `2`
- `[[1, 2], [3, 0]]` -> `3`
- `[[3, 1], [2, 5]]` -> `11`
- `[[True], [1]]` -> `raises TypeError`
- `[[1], None]` -> `raises TypeError`
- `[[1], [1, 2]]` -> `raises ValueError`
- `[[1000000001], [1]]` -> `raises ValueError`

Only edit `dot_product.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/dot-product/check.py --solution "$PWD/tasks/dot-product/dot_product.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
