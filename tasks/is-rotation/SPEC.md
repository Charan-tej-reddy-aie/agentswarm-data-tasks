# String rotation check by code points

Implement export function isRotation(a, b) in is_rotation.mjs, Node 22 standard
library only.

a and b must both be primitive strings; boxed String objects (also
subclasses), missing arguments and all other values raise exact TypeError.
Validate both types before any length check. Then a string longer than 1000
UTF-16 code units (its .length) raises exact RangeError.

Split each string into Unicode code points (a surrogate pair is one code
point; a lone surrogate is its own code point). Return the primitive boolean
true when b's code points equal a's code points rotated left by some k in
[0, n), that is a.slice(k) + a.slice(0, k) measured in code points, otherwise
false. Strings with different code-point counts are never rotations. Matching
is case-sensitive and spaces and punctuation count. No trimming or
normalization (é and e + U+0301 differ). A string is a rotation of itself and
two empty strings are rotations of each other.

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('waterbottle', 'erbottlewat') -> true`
- `('', '') -> true`
- `('a', 'a') -> true`
- `('ab', 'ba') -> true`
- `('abc', 'acb') -> false`
- `('abc', 'abcd') -> false`
- `('aa', 'a') -> false`
- `('Abc', 'bcA') -> true`
- `('abc', 'BCA') -> false`
- `('a b', 'ba ') -> true`
- `('abc', 'cba') -> false`
- `('\ud83d\ude80a', 'a\ud83d\ude80') -> true`
- `('aab', 'aba') -> true`
- `('aab', 'abb') -> false`
- `(' ab', 'ab') -> false`
- `('\ud83d\ude80','\ude80\ud83d') -> false`
- `('\ud83dx','x\ud83d') -> true`
- `('\ud83d\ude80x','\ude80x\ud83d') -> false`
- `('\u00e9','e\u0301') -> false`
- `(1,'a') -> TypeError`
- `('a',null) -> TypeError`
- `(new String('a'),'a') -> TypeError`
- `('a'.repeat(1001),'a') -> RangeError`
- `('a','b'.repeat(1001)) -> RangeError`
- `('a'.repeat(1001),5) -> TypeError`
- `('\ud83d\ude80'.repeat(501),'') -> RangeError`

Only edit is_rotation.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/is-rotation/check.mjs --solution "$PWD/tasks/is-rotation/is_rotation.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
