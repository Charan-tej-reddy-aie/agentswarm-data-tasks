# Apply the Atbash cipher to ASCII letters

Implement `Atbash(s string) string` in package `atbash`, file `atbash.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit atbash.go and optional IMPLEMENTATION.md in this task. Do
not change the checker, module, fixtures or specification. No file, clock or
network access.

The Atbash cipher mirrors the alphabet: a <-> z, b <-> y, c <-> x and so on
(the letter at position k from the start becomes the letter at position k
from the end). Replace every ASCII lowercase letter a-z with its lowercase
mirror and every ASCII uppercase letter A-Z with its uppercase mirror, so case
is kept. Every other byte stays exactly as it is, in place: digits, spaces,
punctuation, all non-ASCII characters (é, ß, Σ, fullwidth Ａ, emoji and so on)
and even invalid UTF-8 bytes, which must not become U+FFFD. The result has the
same length in bytes as s, and applying Atbash twice gives back s. The empty
string returns the empty string.

Examples: "" -> ""; "abc" -> "zyx"; "Wizard" -> "Draziw";
"Hello, World!" -> "Svool, Dliow!"; "café" -> "xzué"; "🚀Go🚀" -> "🚀Tl🚀";
"a\xffB" -> "z\xffY".

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
