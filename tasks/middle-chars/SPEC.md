# middle-chars
Implement `middle_chars` in `middle_chars.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 1000 Unicode code points. Return, as an exact built-in str, the middle of text measured in code points: the single middle character when the length is odd, the two middle characters when the length is even, and "" for the empty string. Every character counts, including spaces, punctuation, emoji and combining marks; there is no trimming or normalization.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['']` -> `''`
- `['a']` -> `'a'`
- `['ab']` -> `'ab'`
- `['abc']` -> `'b'`
- `['abcd']` -> `'bc'`
- `['testing']` -> `'t'`
- `['middle']` -> `'dd'`
- `['a b']` -> `' '`
- `['🚀x🚀']` -> `'x'`
- `['ab🚀cd']` -> `'🚀'`
- `['🚀ab']` -> `'a'`
- `['x🚀']` -> `'x🚀'`
- `['é']` -> `'é'`
- `['  ']` -> `'  '`
- `['12345']` -> `'3'`
- `[['ab']]` -> `raises TypeError`
- `['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']` -> `raises ValueError`

Only edit `middle_chars.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/middle-chars/check.py --solution "$PWD/tasks/middle-chars/middle_chars.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
