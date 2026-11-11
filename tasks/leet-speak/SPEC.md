# Leet speak for five lowercase letters

Implement export function leetSpeak(text) in leet_speak.ts.
TypeScript, run directly by Node 22 with --experimental-strip-types (the
checker passes that flag): use only erasable type annotations, no enums,
namespaces, parameter properties or imports; no npm packages or tsc build.

text must be a primitive string; boxed String objects (also subclasses),
numbers, missing arguments and all other values raise exact TypeError. Check
the type before the length. Then a string longer than 1000 UTF-16 code units
(its .length) raises exact RangeError.

Return a primitive string equal to text with exactly five lowercase ASCII
letters replaced by digits: a -> 4, e -> 3, i -> 1, o -> 0 and s -> 5.
Every other character is kept unchanged and in order, including the
uppercase letters A, E, I, O and S, all other letters, digits, spaces,
accented letters such as é, emoji and lone surrogates. There is no trimming
and no case change. "leet speak" -> "l33t 5p34k", "AEIOS" -> "AEIOS" and
"" -> "".

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> ''`
- `('leet speak') -> 'l33t 5p34k'`
- `('aeios') -> '43105'`
- `('AEIOS') -> 'AEIOS'`
- `('hello') -> 'h3ll0'`
- `('password') -> 'p455w0rd'`
- `('Mississippi') -> 'M1551551pp1'`
- `('sos') -> '505'`
- `('tea time') -> 't34 t1m3'`
- `('4a3e') -> '4433'`
- `('caf\u00e9') -> 'c4f\u00e9'`
- `('x\ud83d\ude80s') -> 'x\ud83d\ude805'`
- `('ice') -> '1c3'`
- `('bold') -> 'b0ld'`
- `('  so  ') -> '  50  '`
- `('Oasis') -> 'O4515'`
- `('s'.repeat(1000)) -> '5'.repeat(1000)`
- `('as'.repeat(500)) -> '45'.repeat(500)`
- `('\ud83do') -> '\ud83d0'`
- `('S'.repeat(1000)) -> 'S'.repeat(1000)`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('a1')) -> TypeError`
- `('a'.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit leet_speak.ts and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/leet-speak/check.mjs --solution "$PWD/tasks/leet-speak/leet_speak.ts"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
