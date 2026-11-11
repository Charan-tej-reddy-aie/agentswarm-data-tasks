# last-word-length
Implement `last_word_length` in `last_word_length.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 1000 Unicode code points. A word is a maximal run of non-whitespace characters, where whitespace is exactly what Python's str.split() with no arguments splits on (including tabs, newlines and Unicode spaces such as U+00A0). Return, as an exact built-in int, the number of Unicode code points in the last word of text; trailing whitespace is ignored and punctuation and digits are part of a word. Text with no words (empty or whitespace-only) returns 0.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['']` -> `0`
- `['   ']` -> `0`
- `['hello']` -> `5`
- `['hello world']` -> `5`
- `['fly me   to the moon  ']` -> `4`
- `['a\tbc\n']` -> `2`
- `["don't"]` -> `5`
- `['x y!']` -> `2`
- `['one two3']` -> `4`
- `['a\xa0bcd']` -> `3`
- `['é']` -> `1`
- `['go 🚀🚀']` -> `2`
- `['\n\n']` -> `0`
- `[['a']]` -> `raises TypeError`
- `['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']` -> `raises ValueError`

Only edit `last_word_length.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/last-word-length/check.py --solution "$PWD/tasks/last-word-length/last_word_length.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
