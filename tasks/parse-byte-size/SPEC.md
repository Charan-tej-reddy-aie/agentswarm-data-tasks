# parse-byte-size
Implement `parse_byte_size` in `parse_byte_size.py`. Python 3.11+ standard library only.

Require exact built-in str matching the ENTIRE ASCII grammar (0|[1-9][0-9]{0,8})(B|KiB|MiB|GiB). Units are case-sensitive; no spaces, signs, decimals, leading zeros except zero itself, newline, or Unicode digits. Return an exact built-in int: B multiplier 1, KiB 1024, MiB 1048576, GiB 1073741824. Zero with any unit is valid; the largest count is 999999999.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `['0B']` -> `0`
- `['1B']` -> `1`
- `['2KiB']` -> `2048`
- `['3MiB']` -> `3145728`
- `['1GiB']` -> `1073741824`
- `['0GiB']` -> `0`
- `['999999999GiB']` -> `1073741822926258176`

Only edit `parse_byte_size.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/parse-byte-size/check.py --solution "$PWD/tasks/parse-byte-size/parse_byte_size.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
