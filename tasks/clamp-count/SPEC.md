# clamp-count
Implement `clamp_count` in `clamp_count.py`. Python 3.11+ standard library only.

Inputs value, low and high are exact built-in ints in [-1000000000,1000000000], with low <= high. Return value clamped inclusively to [low,high] as an exact int.

Reject bool and all subclasses, including nested values, with exact TypeError. Validate ALL types first; bounds violations then raise exact ValueError. Exception messages are unconstrained. No input mutation, retained state, I/O or dependencies.

Examples (argument lists -> result):
- `[-3, 0, 10]` -> `0`
- `[5, 0, 10]` -> `5`
- `[20, 0, 10]` -> `10`
- `[0, 0, 0]` -> `0`
- `[-8, -5, -2]` -> `-5`
- `[1000000000, -1000000000, 1000000000]` -> `1000000000`

Only edit `clamp_count.py` and optional IMPLEMENTATION.md.
