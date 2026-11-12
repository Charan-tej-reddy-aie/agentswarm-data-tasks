# Validate a plain ISBN-10

Implement export function isIsbn10(text) in is_isbn10.mjs,
Node 22 standard library only.

text must be a primitive string; boxed String objects (also subclasses),
numbers, missing arguments and all other values raise exact TypeError. Check
the type before the length. Then a string longer than 1000 UTF-16 code units
(its .length) raises exact RangeError.

Return the primitive boolean true when text is a valid plain ISBN-10, otherwise
false. Valid means exactly ten characters: nine ASCII digits 0-9 followed by
one ASCII digit or an uppercase X (which stands for 10), and the weighted sum
10*d1 + 9*d2 + 8*d3 + ... + 2*d9 + 1*d10 is divisible by 11. Nothing else is
accepted: no hyphens, spaces, trailing newline or trimming, no lowercase x, no
X before the last position and no non-ASCII digits. "0306406152" and
"080442957X" are true; "0306406153", "080442957x", "0-306-40615-2" and ""
are false.

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('0306406152') -> true`
- `('0306406153') -> false`
- `('080442957X') -> true`
- `('080442957x') -> false`
- `('0-306-40615-2') -> false`
- `('') -> false`
- `('123456789X') -> true`
- `('X123456789') -> false`
- `('X00000000X') -> false`
- `('0000000000') -> true`
- `('03064061520') -> false`
- `('030640615') -> false`
- `('0306406152 ') -> false`
- `(' 0306406152') -> false`
- `('\uff10306406152') -> false`
- `('1234567890') -> false`
- `('0471958697') -> true`
- `('047195869X') -> false`
- `('0306406152000') -> false`
- `('030640615200X') -> false`
- `('0306406152\n') -> false`
- `('\u0660306406152') -> false`
- `('03064061'+'5'+'2') -> true`
- `('1'.repeat(1000)) -> false`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(306406152) -> TypeError`
- `(new String('0306406152')) -> TypeError`
- `('1'.repeat(1001)) -> RangeError`

Only edit is_isbn10.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/is-isbn10/check.mjs --solution "$PWD/tasks/is-isbn10/is_isbn10.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
