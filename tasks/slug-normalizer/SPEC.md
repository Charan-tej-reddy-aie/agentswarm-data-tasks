# Normalize task titles into bounded ASCII slugs

Implement `normalize_slug(text, max_length=64) -> str` in `slug_normalizer.py`.
This standalone helper turns authored marketplace task titles into predictable
URL path components. It does not allocate URLs or guarantee uniqueness: callers
must handle collisions. No production integration is claimed. Use Python 3.11+
standard library only, without files, network, packages or wall clock.
Only edit this implementation plus optional `IMPLEMENTATION.md` beside it.

Validate both arguments before normalization. `text` must have exact type `str`
and `max_length` exact type `int` (reject bool). Wrong types raise `TypeError`.
The maximum must be from 1 through 128 inclusive; otherwise raise `ValueError`.
Error messages are unconstrained. Omitted max_length means 64.

Apply these operations in order: Unicode `str.casefold()`, Unicode NFKD
normalization, then remove every character whose Unicode general category
starts with M (combining marks). Replace each maximal run outside ASCII
`[a-z0-9]` with one ASCII hyphen. Trim hyphens from both ends. Truncate to the
first max_length ASCII characters, then remove trailing hyphens again. If
nothing remains, return the first max_length characters of literal `task`.
Return exact type str. The result is lowercase ASCII and never exceeds the
maximum. Do not alter the input. Repeat calls must be deterministic.

This deliberately discards nondecomposing non-ASCII letters rather than
transliterating them. For example, `Straße` becomes `strasse`, `Café / API`
becomes `cafe-api`, and an all-Han title becomes `task`. Punctuation and emoji
are separators. A mark between letters is removed, not made a separator.
`('abc def', 4)` returns `abc`; `('', 2)` returns `ta`.

Run `python3 tasks/slug-normalizer/check.py --solution "$PWD/tasks/slug-normalizer/slug_normalizer.py"`.
Acceptance uses at least 60 authored synthetic contract cases, Unicode and
boundary examples, invalid arguments and repeated calls. Checks execute code
with a timeout, not a security sandbox; public fixtures can be overfit.
Source/scope review also applies; see CONTRIBUTING.md.
