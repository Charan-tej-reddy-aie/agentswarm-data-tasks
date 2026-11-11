# Reverse the order of words

Implement `pub fn reverse_words(input: &str) -> String` in `src/lib.rs` (crate
`reverse-words`). Rust 2021, standard library only, no crates. Only edit
src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change the
checker, Cargo.toml, fixtures or this specification.

A word is a maximal run of characters that are not whitespace, where
whitespace is exactly Rust's `char::is_whitespace` (Unicode White_Space: ASCII
spaces, tabs, newlines and carriage returns, plus U+0085, U+00A0, U+3000 and
other Unicode spaces; U+200B ZERO WIDTH SPACE is not whitespace). Return the
words in reverse order joined by single ASCII spaces, with no leading or
trailing space. Each word keeps its characters unchanged and in order,
including punctuation, digits, accents and emoji; repeated words are all kept.
Input without words returns the empty string. Any input length must work
without panic.

Examples (input -> result):
- `"one two three"` -> `"three two one"`
- `"  lead and trail  "` -> `"trail and lead"`
- `"a\tb\nc"` -> `"c b a"`
- `"x y"` -> `"y x"`
- `"same same"` -> `"same same"`
- `""` -> `""`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
