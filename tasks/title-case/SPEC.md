# Title-case ASCII words in a string

Implement `pub fn title_case(input: &str) -> String` in `src/lib.rs` (crate
`title_case`). Rust 2021, standard library only, no crates. Only edit
src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change the
checker, Cargo.toml, fixtures or this specification.

Words are separated ONLY by the ASCII space U+0020. Every other character,
including tabs, newlines, no-break spaces, punctuation and digits, is part of a
word. Spaces are copied unchanged: keep leading, trailing and repeated spaces
exactly (never trim or collapse).

For each word: if its FIRST character is an ASCII lowercase letter a-z, make it
uppercase; every LATER ASCII uppercase letter A-Z becomes lowercase. All
non-ASCII characters are copied unchanged in every position (no Unicode case
mapping, no normalization). A word whose first character is not a letter, such
as "123abc" or "'quoted", keeps that first character and still lowercases the
rest. The output has the same number of chars as the input.

Examples (input -> output):
- `""` -> `""`
- `"hello world"` -> `"Hello World"`
- `"hELLO wORLD"` -> `"Hello World"`
- `"  two  spaces "` -> `"  Two  Spaces "`
- `"o'neil mc-donald"` -> `"O'neil Mc-donald"`
- `"123abc DEF"` -> `"123abc Def"`
- `"tab\tsep word"` -> `"Tab\tsep Word"`
- `"élan vital"` -> `"élan Vital"`
- `"ÉCOLE ÉTÉ"` -> `"École ÉtÉ"`
- `"ß straße"` -> `"ß Straße"`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
