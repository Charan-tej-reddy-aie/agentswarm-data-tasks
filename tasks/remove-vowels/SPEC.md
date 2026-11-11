# Remove ASCII vowels

Implement export function removeVowels(text) in remove_vowels.mjs,
Node 22 standard library only.

text must be a primitive string; boxed String objects (also subclasses),
numbers, missing arguments and all other values raise exact TypeError. Check
the type before the length. Then a string longer than 1000 UTF-16 code units
(its .length) raises exact RangeError.

Return a primitive string equal to text with every ASCII vowel removed: the
ten characters a, e, i, o, u, A, E, I, O and U. Every other character is
kept unchanged and in order, including y and Y, accented vowels such as é
or À, digits, spaces, newlines, emoji and lone surrogates. There is no
trimming and no case change. "hello world" -> "hll wrld", "Yay" -> "Yy",
"café" -> "cfé" and "" -> "".

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> ''`
- `('hello world') -> 'hll wrld'`
- `('AEIOU aeiou') -> ' '`
- `('rhythm') -> 'rhythm'`
- `('Yay') -> 'Yy'`
- `('queue') -> 'q'`
- `('Programming') -> 'Prgrmmng'`
- `('caf\u00e9') -> 'cf\u00e9'`
- `('\u00c0\u00e9\u00ee\u00f5\u00fc') -> '\u00c0\u00e9\u00ee\u00f5\u00fc'`
- `('x\ud83d\ude80a') -> 'x\ud83d\ude80'`
- `('a1e2i3o4u5') -> '12345'`
- `('  spaced  ') -> '  spcd  '`
- `('a\nb\tc') -> '\nb\tc'`
- `('A-E_I') -> '-_'`
- `('bcdfg') -> 'bcdfg'`
- `('Ooo!') -> '!'`
- `('a'.repeat(1000)) -> ''`
- `('b'.repeat(1000)) -> 'b'.repeat(1000)`
- `('\ud83d_a') -> '\ud83d_'`
- `('xa'.repeat(500)) -> 'x'.repeat(500)`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('a1')) -> TypeError`
- `('a'.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit remove_vowels.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/remove-vowels/check.mjs --solution "$PWD/tasks/remove-vowels/remove_vowels.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
