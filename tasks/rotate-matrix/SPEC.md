# rotate-matrix
Implement `rotate_matrix` in `rotate_matrix.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require rows, an exact built-in list of at most 100 rows; each row is an exact built-in list of at most 100 exact built-in ints, each in [-1000000000,1000000000]. Every row must have the same length as rows[0]; a ragged matrix raises exact ValueError. Return a fresh exact built-in list of fresh exact built-in lists that is the matrix rotated 90 degrees clockwise: result[j][i] == rows[R-1-i][j] for an R x C matrix, which becomes C x R (the first result row is the first column read from bottom to top). The empty matrix [] returns [] (never None), and rows with zero columns, such as [[], []], also return [].

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[[]]]` -> `[]`
- `[[[], []]]` -> `[]`
- `[[[1]]]` -> `[[1]]`
- `[[[1, 2, 3]]]` -> `[[1], [2], [3]]`
- `[[[1], [2], [3]]]` -> `[[3, 2, 1]]`
- `[[[1, 2], [3, 4]]]` -> `[[3, 1], [4, 2]]`
- `[[[1, 2, 3], [4, 5, 6]]]` -> `[[4, 1], [5, 2], [6, 3]]`
- `[[[-1, 0], [0, -1], [5, 5]]]` -> `[[5, 0, -1], [5, -1, 0]]`
- `[[[7, 7], [7, 7]]]` -> `[[7, 7], [7, 7]]`
- `[[[1, True]]]` -> `raises TypeError`
- `[[None]]` -> `raises TypeError`
- `[[[1, 2], [3]]]` -> `raises ValueError`
- `[[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]` -> `raises ValueError`

Only edit `rotate_matrix.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/rotate-matrix/check.py --solution "$PWD/tasks/rotate-matrix/rotate_matrix.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
