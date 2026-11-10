# merge-counters
Implement `merge_counters` in `merge_counters.py`. Python 3.11+ standard library only.

Require two exact built-in dicts, each at most 1000 entries. All keys must be exact built-in str of length at most 64 code points (empty, whitespace and Unicode keys are valid opaque keys). All counts must be exact built-in int in [0,1000000000]. Return a fresh exact built-in dict: sum shared counts, retain zero totals, preserve left key insertion order then append right-only keys in their insertion order. Sums may reach 2000000000. No sorting, trimming, normalization or case folding.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `[{}, {}]` -> `{}`
- `[{'b': 2, 'a': 0}, {'a': 3, 'c': 4}]` -> `{'b': 2, 'a': 3, 'c': 4}`
- `[{'x': 1000000000}, {'x': 1000000000}]` -> `{'x': 2000000000}`
- `[{}, {'z': 0, 'a': 1}]` -> `{'z': 0, 'a': 1}`
- `[{}, {'Z': 2}]` -> `{'Z': 2}`
- `[{'A': 1}, {'a': 2}]` -> `{'A': 1, 'a': 2}`
- `[{'': 0}, {'': 0}]` -> `{'': 0}`
- `[{'é': 1}, {'é': 2}]` -> `{'é': 1, 'é': 2}`

Only edit `merge_counters.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/merge-counters/check.py --solution "$PWD/tasks/merge-counters/merge_counters.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
