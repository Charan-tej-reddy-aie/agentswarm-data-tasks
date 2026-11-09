# Neutralize formula prefixes in authored CSV export rows

Implement `sanitize_csv_rows(rows)` in `csv_sanitizer.py`, a standalone offline
helper for exporting authored marketplace task text to a spreadsheet. Use Python
3.11+ standard library only, without packages, files, network or a wall clock.
Only edit this implementation and optional task-local `IMPLEMENTATION.md`.
No production integration or general spreadsheet security guarantee is claimed.

The input must have exact type list. Each row must have exact type list and each
cell exact type str; reject any other type with TypeError, including tuples,
None, numbers and booleans, even deep in an otherwise valid input. Error messages
are unconstrained. Empty outer lists, empty rows, ragged rows, empty cells and
Unicode strings are valid. Validate the whole input; never silently coerce cells.

Return a new list containing new row lists in the original order. For each cell,
look past only the leading ASCII space, tab, carriage-return and line-feed
characters, in any combination. If the first remaining character is one of
ASCII `=`, `+`, `-`, or `@`, prefix the ORIGINAL cell with one ASCII apostrophe.
Otherwise return its unchanged string value. Do not strip or normalize text,
change newlines, quote fields, add delimiters or append an apostrophe elsewhere.
An existing leading apostrophe is ordinary text and prevents adding another.
Non-ASCII whitespace, including NBSP, is ordinary text and is not skipped.
An all-whitespace string stays unchanged. Minus-prefixed numeric strings are
neutralized too; this helper deliberately does not guess whether they are safe.

Examples: `[['=SUM(A1)', 'ok']]` returns `[["'=SUM(A1)", 'ok']]`.
A cell consisting of space, tab, then `+1` receives an apostrophe BEFORE its
space. A cell beginning with NBSP then `=1` stays unchanged. Applying this
function twice gives the same values as once. Calls must be deterministic and
must not mutate or alias the caller's outer list or row lists, including empty
or repeated row objects. Strings may be shared because they are immutable.

CSV encoding and spreadsheet-specific import policies remain the caller's
responsibility; this contract handles only the stated prefix rule. Run
`python3 tasks/csv-sanitizer/check.py --solution "$PWD/tasks/csv-sanitizer/csv_sanitizer.py"`.
Acceptance uses at least 60 synthetic cases including Unicode and malformed
inputs, repeated calls, idempotence and list independence. Public cases can be
overfit; source/scope review also applies. Checks are not a security sandbox.
