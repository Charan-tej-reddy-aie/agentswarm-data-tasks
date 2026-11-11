# Swap the case of ASCII letters

Implement `SwapCase(s string) string` in package `swapcase`, file `swapcase.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit swapcase.go and optional IMPLEMENTATION.md in this task. Do
not change the checker, module, fixtures or specification. No file, clock or
network access.

Return s with every ASCII lowercase letter a-z changed to its uppercase form
and every ASCII uppercase letter A-Z changed to its lowercase form. Every other
byte stays exactly as it is, in place: digits, spaces, punctuation, all
non-ASCII characters (é, ß, Σ, ǅ, fullwidth Ａ, emoji and so on keep their
case) and even invalid UTF-8 bytes, which must not become U+FFFD. The result
has the same length in bytes as s. The empty string returns the empty string.

Examples: "" -> ""; "aB" -> "Ab"; "Hello, World!" -> "hELLO, wORLD!";
"café" -> "CAFé"; "CAFÉ" -> "cafÉ"; "🚀Go🚀" -> "🚀gO🚀";
"a\xffB" -> "A\xffb".

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
