# Collapse runs of repeated characters

Implement `pub fn squash_repeats(input: &str) -> String` in `src/lib.rs`
(crate `squash-repeats`). Rust 2021, standard library only, no crates. Only
edit src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change
the checker, Cargo.toml, fixtures or this specification.

Treat the input as a sequence of `char`s (Unicode scalar values, not bytes).
Replace every run of two or more equal adjacent chars with a single copy of
that char and keep all other chars unchanged and in order. Chars are equal
only when they are the same `char`: there is no case folding ("Aa" stays
"Aa") and no Unicode normalization. Every char counts the same way, including
spaces, tabs, newlines, punctuation, digits, combining marks and emoji.
Equal chars that are not adjacent are kept ("abba" -> "aba"). There is no
trimming. The empty string returns the empty string. Any input length must
work without panic.

Examples (input -> result):
- `""` -> `""`
- `"aab"` -> `"ab"`
- `"aaabbbaaa"` -> `"aba"`
- `"Aa"` -> `"Aa"`
- `"hello  world"` -> `"helo world"`
- `"éée"` -> `"ée"`
- `"🚀🚀x"` -> `"🚀x"`
- `"mississippi"` -> `"misisipi"`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
