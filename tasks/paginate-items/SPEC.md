# paginate-items
Implement `paginate_items` in `paginate_items.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require an exact built-in list of at most 1000 exact built-in strings, each at most 64 code points. offset is an exact built-in int in [0,1000000000]; limit an exact built-in int in [1,1000]. Return a fresh exact built-in dict with exactly keys items and next_offset. items is a fresh exact built-in list equal to items[offset:offset+limit]. next_offset is offset+limit as an exact int only when MORE items remain after this page; otherwise None. Empty input, offset at/past the end and an exactly full final page have None. Preserve order and duplicates.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `[[], 0, 2]` -> `{'items': [], 'next_offset': None}`
- `[['a', 'b', 'c'], 0, 2]` -> `{'items': ['a', 'b'], 'next_offset': 2}`
- `[['a', 'b', 'c'], 2, 2]` -> `{'items': ['c'], 'next_offset': None}`
- `[['a', 'b'], 0, 2]` -> `{'items': ['a', 'b'], 'next_offset': None}`
- `[['a'], 1, 1]` -> `{'items': [], 'next_offset': None}`
- `[['a'], 1000000000, 1]` -> `{'items': [], 'next_offset': None}`
- `[['z', 'a'], 0, 2]` -> `{'items': ['z', 'a'], 'next_offset': None}`
- `[['a', 'a', 'b'], 1, 1]` -> `{'items': ['a'], 'next_offset': 2}`

Only edit `paginate_items.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/paginate-items/check.py --solution "$PWD/tasks/paginate-items/paginate_items.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
