# coalesce-ranges
Implement `coalesce_ranges` in `coalesce_ranges.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in lists. Each inner list must have exactly two exact built-in int endpoints in [-1000000000,1000000000], start <= end. Input may be unsorted. Discard empty ranges [a,a]. Return a fresh exact built-in list of fresh two-int exact built-in lists representing the union, sorted by start. Merge overlap AND touching endpoints (a next start <= current end). Ranges are half-open [start,end); no +1 adjacency rule. Do not retain nested input lists.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[[4, 7], [1, 3], [3, 4]]]` -> `[[1, 7]]`
- `[[[1, 2], [3, 4]]]` -> `[[1, 2], [3, 4]]`
- `[[[1, 1], [2, 2]]]` -> `[]`
- `[[[1, 8], [2, 3]]]` -> `[[1, 8]]`
- `[[[1, 8], [2, 3], [1, 8]]]` -> `[[1, 8]]`
- `[[[0, 2], [-3, 0], [8, 9]]]` -> `[[-3, 2], [8, 9]]`
- `[[[1000000000, 1000000000], [-1000000000, 0]]]` -> `[[-1000000000, 0]]`

Only edit `coalesce_ranges.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/coalesce-ranges/check.py --solution "$PWD/tasks/coalesce-ranges/coalesce_ranges.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
