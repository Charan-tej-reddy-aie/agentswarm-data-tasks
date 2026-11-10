# pad-left
Implement `pad_left` in `pad_left.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 64 Unicode code points; width, an exact built-in int in [0,128]; and fill, an exact built-in str of exactly ONE code point (a combining sequence such as e + U+0301 is two code points and is rejected). Return fill repeated (width - len(text)) times followed by text, so the result has width code points. If text already has width or more code points, return it unchanged: never truncate. Widths count code points, not UTF-8 bytes; text is opaque (no trimming or normalization).

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['7', 3, '0']` -> `'007'`
- `['abc', 2, '*']` -> `'abc'`
- `['', 2, '-']` -> `'--'`
- `['ab', 2, 'x']` -> `'ab'`
- `['é', 3, '·']` -> `'··é'`
- `['', 0, ' ']` -> `''`
- `[' a', 4, '.']` -> `'.. a'`
- `['x', 5, 'é']` -> `'ééééx'`
- `['a', 1, '']` -> `raises ValueError`
- `['a', True, '0']` -> `raises TypeError`

Only edit `pad_left.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/pad-left/check.py --solution "$PWD/tasks/pad-left/pad_left.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
