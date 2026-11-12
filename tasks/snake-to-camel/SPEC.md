# Convert snake_case to camelCase

Implement export function snakeToCamel(text) in snake_to_camel.mjs,
Node 22 standard library only.

text must be a primitive string; boxed String objects (also subclasses),
missing arguments and all other values raise exact TypeError. Check the type
before the length. Then a string longer than 1000 UTF-16 code units (its
.length) raises exact RangeError.

Return a primitive string built from text by removing every underscore "_"
and, for each character that comes directly after an underscore in text,
changing it to uppercase only when it is an ASCII lowercase letter a-z. Every
other character is copied unchanged and in order: uppercase letters stay
uppercase, there is no lowercasing, digits, hyphens, spaces, emoji, lone
surrogates and non-ASCII letters (such as é or ß) after an underscore are
kept as they are, and the first character is never capitalized unless it
follows an underscore. So "user_id" -> "userId", "HTTP_server" ->
"HTTPServer", "_private" -> "Private", "a__b" -> "aB", "a_1" -> "a1" and
"__" -> "".

Error messages are unconstrained. Keep no state between calls; repeated and
independent calls return the same result.

Examples (arguments -> result); every one is checked:
- `('') -> ''`
- `('user_id') -> 'userId'`
- `('get_http_response') -> 'getHttpResponse'`
- `('_private') -> 'Private'`
- `('private_') -> 'private'`
- `('a__b') -> 'aB'`
- `('__') -> ''`
- `('a_1') -> 'a1'`
- `('a_\u00e9') -> 'a\u00e9'`
- `('a_B') -> 'aB'`
- `('HTTP_server') -> 'HTTPServer'`
- `('already') -> 'already'`
- `('snake_case_words') -> 'snakeCaseWords'`
- `('x_y_z') -> 'xYZ'`
- `('\ud83d\ude80_rocket') -> '\ud83d\ude80Rocket'`
- `('a-b_c') -> 'a-bC'`
- `(' a_b ') -> ' aB '`
- `('a_\u00df') -> 'a\u00df'`
- `('_') -> ''`
- `('a_\u0131') -> 'a\u0131'`
- `('a_b'.repeat(333)) -> 'aB'.repeat(333)`
- `('_'.repeat(1000)) -> ''`
- `('\ud83d_x') -> '\ud83dX'`
- `('a_\ud83d\ude80') -> 'a\ud83d\ude80'`
- `(1) -> TypeError`
- `(null) -> TypeError`
- `(new String('a_b')) -> TypeError`
- `('_'.repeat(1001)) -> RangeError`
- `('\ud83d\ude80'.repeat(501)) -> RangeError`

Only edit snake_to_camel.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/snake-to-camel/check.mjs --solution "$PWD/tasks/snake-to-camel/snake_to_camel.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
