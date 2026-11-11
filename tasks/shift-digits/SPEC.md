# Shift ASCII digits by one

Implement export function shiftDigits(text) in shift_digits.ts.
TypeScript, run directly by Node 22 with --experimental-strip-types (the
checker passes that flag): use only erasable type annotations, no enums,
namespaces, parameter properties or imports; no npm packages or tsc build.

text must be a primitive string; boxed String objects (also subclasses),
numbers, missing arguments and all other values raise exact TypeError. Check
the type before the length. Then a string longer than 1000 UTF-16 code units
(its .length) raises exact RangeError.

Return a primitive string equal to text with every ASCII digit 0-9 replaced
by the next digit, wrapping 9 around to 0: 0 -> 1, 1 -> 2, ..., 8 -> 9 and
9 -> 0. Each digit is shifted on its own (there is no carry, "99" -> "00").
Every other character is kept unchanged and in order, including letters,
signs, spaces, emoji, lone surrogates and non-ASCII digits such as
Arabic-Indic ٠ or fullwidth １. "v1.9.9" -> "v2.0.0", "2026-11-12" ->
"3137-22-23" and "" -> "".

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> ''`
- `('abc') -> 'abc'`
- `('0123456789') -> '1234567890'`
- `('9') -> '0'`
- `('99') -> '00'`
- `('v1.9.9') -> 'v2.0.0'`
- `('2026-11-12') -> '3137-22-23'`
- `('\u0660\u0661 12') -> '\u0660\u0661 23'`
- `('\uff11') -> '\uff11'`
- `('a\ud83d\ude809') -> 'a\ud83d\ude800'`
- `('  0  ') -> '  1  '`
- `('-9') -> '-0'`
- `('1e9') -> '2e0'`
- `('x8y') -> 'x9y'`
- `('09:59') -> '10:60'`
- `('2') -> '3'`
- `('9'.repeat(1000)) -> '0'.repeat(1000)`
- `('09'.repeat(500)) -> '10'.repeat(500)`
- `('\ud83d5') -> '\ud83d6'`
- `('x'.repeat(1000)) -> 'x'.repeat(1000)`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('a1')) -> TypeError`
- `('a'.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit shift_digits.ts and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/shift-digits/check.mjs --solution "$PWD/tasks/shift-digits/shift_digits.ts"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
