# Mask ASCII digits

Implement export function maskDigits(text) in mask_digits.mjs,
Node 22 standard library only.

text must be a primitive string; boxed String objects (also subclasses),
numbers, missing arguments and all other values raise exact TypeError. Check
the type before the length. Then a string longer than 1000 UTF-16 code units
(its .length) raises exact RangeError.

Return a primitive string equal to text with every ASCII digit 0-9 replaced
by one asterisk "*". Every other character is kept unchanged and in order,
including letters, spaces, hyphens, newlines, emoji, lone surrogates and
non-ASCII digits such as Arabic-Indic ٠ or fullwidth １. Each digit becomes its
own asterisk (runs are not merged) and there is no trimming. "card
4111-1111" -> "card ****-****", "v1.2.3" -> "v*.*.*" and "" -> "".

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> ''`
- `('abc') -> 'abc'`
- `('0123456789') -> '**********'`
- `('card 4111-1111') -> 'card ****-****'`
- `('x9y') -> 'x*y'`
- `('\u0660\u0661 12') -> '\u0660\u0661 **'`
- `('99 bottles') -> '** bottles'`
- `('v1.2.3') -> 'v*.*.*'`
- `('\uff11\uff12') -> '\uff11\uff12'`
- `('a\ud83d\ude800') -> 'a\ud83d\ude80*'`
- `('00') -> '**'`
- `('  7  ') -> '  *  '`
- `('-1') -> '-*'`
- `('1e9') -> '*e*'`
- `('line1\nline2') -> 'line*\nline*'`
- `('007') -> '***'`
- `('1'.repeat(1000)) -> '*'.repeat(1000)`
- `('a1'.repeat(500)) -> 'a*'.repeat(500)`
- `('\ud83d1') -> '\ud83d*'`
- `('x'.repeat(1000)) -> 'x'.repeat(1000)`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('a1')) -> TypeError`
- `('a'.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit mask_digits.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/mask-digits/check.mjs --solution "$PWD/tasks/mask-digits/mask_digits.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
