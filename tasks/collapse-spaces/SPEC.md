# collapse-spaces
Implement `collapse_spaces` in `collapse_spaces.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 1000 Unicode code points. Return, as an exact built-in str, the words of text joined by single ASCII spaces, with no leading or trailing space. A word is a maximal run of non-whitespace characters, where whitespace is exactly what Python's str.split() with no arguments splits on (characters for which str.isspace() is True, including tabs, newlines and Unicode spaces such as U+00A0). Punctuation is part of a word and every word is kept in order, including repeats. Whitespace-only text returns "".

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['']` -> `''`
- `['hello']` -> `'hello'`
- `['hello world']` -> `'hello world'`
- `['  a  b  ']` -> `'a b'`
- `['a\tb\nc']` -> `'a b c'`
- `["don't   stop"]` -> `"don't stop"`
- `['a - b']` -> `'a - b'`
- `['one,two']` -> `'one,two'`
- `['x\xa0y']` -> `'x y'`
- `['go  go']` -> `'go go'`
- `['   ']` -> `''`
- `[' lead']` -> `'lead'`
- `['trail\n']` -> `'trail'`
- `[['a']]` -> `raises TypeError`
- `['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']` -> `raises ValueError`

Only edit `collapse_spaces.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/collapse-spaces/check.py --solution "$PWD/tasks/collapse-spaces/collapse_spaces.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
