# count-digits
Implement `count_digits` in `count_digits.py`. Python 3.11+ standard library only.

Require text, an exact built-in str of at most 1000 Unicode code points. Return, as an exact built-in int, how many characters of text are ASCII digits 0-9, counting repeats. Every other character is ignored, including letters, signs, decimal points, spaces, superscripts such as ², fullwidth digits such as １ and digits of other scripts such as Arabic-Indic ٣ (even though str.isdigit() is True for them). Return the count of digit characters, not their numeric sum.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `['']` -> `0`
- `['abc']` -> `0`
- `['123']` -> `3`
- `['a1b2c3']` -> `3`
- `['2026-11-11']` -> `8`
- `['-4.5e10']` -> `4`
- `['007']` -> `3`
- `['0 9']` -> `2`
- `['²']` -> `0`
- `['１２']` -> `0`
- `['٣']` -> `0`
- `['x9y9']` -> `2`
- `['99 bottles']` -> `2`
- `[['1']]` -> `raises TypeError`
- `['11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111']` -> `raises ValueError`

Only edit `count_digits.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/count-digits/check.py --solution "$PWD/tasks/count-digits/count_digits.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
