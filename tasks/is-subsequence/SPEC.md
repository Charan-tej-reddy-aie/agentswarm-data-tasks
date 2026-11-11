# String subsequence check by code points

Implement export function isSubsequence(a, b) in is_subsequence.mjs, Node 22
standard library only.

a and b must both be primitive strings; boxed String objects (also
subclasses), missing arguments and all other values raise exact TypeError.
Validate both types before any length check. Then a string longer than 1000
UTF-16 code units (its .length) raises exact RangeError.

Split each string into Unicode code points (a surrogate pair is one code
point; a lone surrogate is its own code point). Return the primitive boolean
true when a's code points occur in b in the same order, not necessarily next
to each other (a can be made from b by deleting zero or more code points),
otherwise false. Repeated code points in a need as many matching code points
in b. The empty string is a subsequence of every string. Matching is
case-sensitive and spaces and punctuation count. No trimming or normalization
(é and e + U+0301 differ).

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('ace', 'abcde') -> true`
- `('aec', 'abcde') -> false`
- `('', '') -> true`
- `('', 'abc') -> true`
- `('abc', '') -> false`
- `('abc', 'abc') -> true`
- `('abcd', 'abc') -> false`
- `('aa', 'a') -> false`
- `('aa', 'bab') -> false`
- `('aa', 'aba') -> true`
- `('A', 'a') -> false`
- `('a c', 'abc d c') -> true`
- `('\ud83d\ude80', 'x\ud83d\ude80y') -> true`
- `('ba', 'ab') -> false`
- `('\u00e9', 'e\u0301') -> false`
- `('\ude80','\ud83d\ude80') -> false`
- `('\ud83d','\ud83d\ude80') -> false`
- `('\ud83d','x\ud83dy') -> true`
- `('\u00e9','e\u0301') -> false`
- `(1,'a') -> TypeError`
- `('a',null) -> TypeError`
- `(new String('a'),'a') -> TypeError`
- `('a'.repeat(1001),'a') -> RangeError`
- `('a','b'.repeat(1001)) -> RangeError`
- `('a'.repeat(1001),5) -> TypeError`
- `('','\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit is_subsequence.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/is-subsequence/check.mjs --solution "$PWD/tasks/is-subsequence/is_subsequence.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
