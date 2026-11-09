# Normalize CSV headers into unique offline field names

Implement `normalize_headers(headers)` in `csv_headers.py` using Python 3.11+
standard library only. This standalone helper claims no production integration.
No packages, files, network, clock or CSV reading. Only edit the implementation
and optional task-local `IMPLEMENTATION.md`.

Input must have exact built-in type list, containing only exact built-in str
items (`type(headers) is list`, `type(item) is str`). Reject subclasses too,
including list subclasses, str subclasses and bool/numeric elements, with
TypeError. Validate every item before producing output. Empty lists and empty
strings are allowed; there are no other input-value restrictions. Error
messages are unconstrained. Python strings, including lone surrogate code
points and NUL, are accepted. Never coerce values to strings.

For each header in original order, normalize with Unicode NFKC, then casefold
(in that order). Replace each MAXIMAL run of characters outside ASCII lowercase
`a`..`z` and ASCII `0`..`9` with ONE underscore. Strip underscores from both
ends. If empty, use `column`. Non-ASCII letters are removed by this run rule,
not transliterated; casefold can expand letters first. Examples: `First Name`
becomes `first_name`, `ＳＴＲＡＳＳＥ` becomes `strasse`, `Straße` becomes `strasse`,
`café` becomes `caf`, and `東京` becomes `column`. Decomposed `café` also gives
`caf` because NFKC precedes filtering. Punctuation may touch letters; there is
no token splitting beyond the maximal-run rule. Existing underscores count
as replacement characters, so `A__-- B` gives `a_b`.

Make names unique using only names ALREADY emitted. Start with the base name;
if used, try base plus `_2`, `_3`, and so on until the first unused name. Do not
reserve names from later headers. Thus `['A','A','A_2','A']` returns
`['a','a_2','a_2_2','a_3']`. Suffixing uses the entire base unchanged, including
any existing numeric suffix. Return a fresh exact list of exact strings and
never mutate the input. Repeated calls return equal, independent lists.

Run `python3 tasks/csv-headers/check.py --solution "$PWD/tasks/csv-headers/csv_headers.py"`.
Acceptance covers at least 60 immutable synthetic cases including Unicode,
collisions, subclass rejection and mutation. Source/scope review accompanies
checks; fixtures never depend on README.md or changing main files.
