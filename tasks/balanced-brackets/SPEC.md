# Balanced bracket check

Implement export function balancedBrackets(text) in balanced_brackets.mjs,
Node 22 standard library only.

text must be a primitive string; boxed String objects (also subclasses),
missing arguments and all other values raise exact TypeError. Check the type
before the length. Then a string longer than 1000 UTF-16 code units (its
.length) raises exact RangeError.

Only the six ASCII bracket characters ( ) [ ] { } matter; every other
character is ignored, including < >, letters, spaces, emoji, lone surrogates
and fullwidth brackets such as U+FF08. Return the primitive boolean true when
every closing bracket matches the most recent unmatched opening bracket of
the same kind and no opening bracket is left unmatched, otherwise false. So
"([)]" and ")(" are false, "{[()]}" is true, and the empty string is true.

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> true`
- `('()') -> true`
- `('()[]{}') -> true`
- `('{[()]}') -> true`
- `('([)]') -> false`
- `(')(') -> false`
- `('((') -> false`
- `('())') -> false`
- `('(]') -> false`
- `(']') -> false`
- `('a(b)c') -> true`
- `('<>') -> true`
- `('<') -> true`
- `('f(x[1], {y: 2})') -> true`
- `('\ud83d\ude80(\ud83d\ude80)') -> true`
- `('\uff08') -> true`
- `('('.repeat(500)+')'.repeat(500)) -> true`
- `('()'.repeat(500)) -> true`
- `('\ud83d') -> true`
- `('(\ude80]') -> false`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('()')) -> TypeError`
- `('('.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit balanced_brackets.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/balanced-brackets/check.mjs --solution "$PWD/tasks/balanced-brackets/balanced_brackets.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
