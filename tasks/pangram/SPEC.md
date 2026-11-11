# Check whether a string uses every ASCII letter

Implement `pub fn is_pangram(input: &str) -> bool` in `src/lib.rs` (crate
`pangram`). Rust 2021, standard library only, no crates. Only edit src/lib.rs
and optional IMPLEMENTATION.md in this task. Do not change the checker,
Cargo.toml, fixtures or this specification.

Only ASCII letters matter: a-z and A-Z, compared case-insensitively (a and A
are the same letter). Every other character is ignored: digits, spaces,
hyphens, tabs, newlines, punctuation and all non-ASCII characters, including
accented letters such as é, combining marks and non-ASCII letters that
resemble ASCII ones. Return true when each of the 26 letters occurs at least
once, otherwise false. The empty string and strings without ASCII letters
return false. Any input length must work without panic.

Examples (input -> result):
- `"The quick brown fox jumps over the lazy dog"` -> `true`
- `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"` -> `true`
- `"The quick brown fox jumps over the lay dog"` -> `false`
- `"abcdefghijklmnopqrstuvwxyé"` -> `false`
- `"a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z"` -> `true`
- `""` -> `false`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
