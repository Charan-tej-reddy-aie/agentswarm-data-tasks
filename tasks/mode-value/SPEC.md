# mode-value
Implement `mode_value` in `mode_value.py`. Python 3.11+ standard library only.

Require a NONEMPTY exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]; an empty list raises exact ValueError. Return the value that occurs most often, as an exact built-in int. If several values share the highest count, return the SMALLEST of those values (not the first seen and not the largest).

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[7]]` -> `7`
- `[[1, 2, 2, 3]]` -> `2`
- `[[3, 1, 3, 1]]` -> `1`
- `[[5, 4]]` -> `4`
- `[[-1, -1, 2, 2, 2]]` -> `2`
- `[[0, -5, -5, 0]]` -> `-5`
- `[[1000000000, -1000000000]]` -> `-1000000000`
- `[[2, 1, 1, 2, 3]]` -> `1`
- `[[]]` -> `raises ValueError`
- `[[True]]` -> `raises TypeError`

Only edit `mode_value.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/mode-value/check.py --solution "$PWD/tasks/mode-value/mode_value.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
