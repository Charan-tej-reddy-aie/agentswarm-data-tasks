# safe-ratio
Implement `safe_ratio` in `safe_ratio.py`. Python 3.11+ standard library only.

Require two exact built-in ints in [-1000000000,1000000000]. If denominator is zero return None, including (0,0); otherwise return the ordinary Python / result as an exact built-in float. Preserve signs; do not round or floor.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `[6, 3]` -> `2.0`
- `[1, 2]` -> `0.5`
- `[-3, 2]` -> `-1.5`
- `[0, 2]` -> `0.0`
- `[1, 0]` -> `None`
- `[0, 0]` -> `None`
- `[1000000000, -1]` -> `-1000000000.0`
- `[1, -1000000000]` -> `-1e-09`

Only edit `safe_ratio.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/safe-ratio/check.py --solution "$PWD/tasks/safe-ratio/safe_ratio.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
