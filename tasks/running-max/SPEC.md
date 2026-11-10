# running-max
Implement `running_max` in `running_max.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return a fresh exact built-in list of the same length where element i is the maximum of values[0..i] inclusive (the running maximum). Empty input returns a fresh []. Output elements are exact built-in ints. Do not sort, deduplicate or reorder.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges/order, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[3]]` -> `[3]`
- `[[1, 3, 2, 5]]` -> `[1, 3, 3, 5]`
- `[[-2, -5, -1]]` -> `[-2, -2, -1]`
- `[[2, 2, 1]]` -> `[2, 2, 2]`
- `[[5, 4, 3]]` -> `[5, 5, 5]`
- `[[0, -1, 0, 1]]` -> `[0, 0, 0, 1]`
- `[[1000000000, -1000000000]]` -> `[1000000000, 1000000000]`
- `[[-1000000000]]` -> `[-1000000000]`
- `[[True]]` -> `raises TypeError`
- `[[1000000001]]` -> `raises ValueError`

Only edit `running_max.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/running-max/check.py --solution "$PWD/tasks/running-max/running_max.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
