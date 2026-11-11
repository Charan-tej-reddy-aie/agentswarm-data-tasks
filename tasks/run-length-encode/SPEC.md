# Run-length encode a string

Implement `pub fn run_length_encode(input: &str) -> String` in `src/lib.rs`
(crate `run-length-encode`). Rust 2021, standard library only, no crates.
Only edit src/lib.rs and optional IMPLEMENTATION.md in this task. Do not
change the checker, Cargo.toml, fixtures or this specification.

Split the input into runs: maximal sequences of the same `char` (Unicode
scalar value) next to each other. For each run, in order, write its length as
a decimal number (always, also when it is 1; no leading zeros) followed by the
character itself. Every character counts, including spaces, tabs, newlines,
digits, punctuation, accents, combining marks and emoji. Comparison is exact
(a and A are different) and there is no trimming or normalization. Runs of
ten or more characters are written with all their digits ("aaaaaaaaaaaab" ->
"12a1b"). Digits in the input are encoded like any other character, so the
result may be ambiguous to decode; that is expected. The empty string returns
the empty string. Any input length must work without panic.

Examples (input -> result):
- `"aaab"` -> `"3a1b"`
- `"abc"` -> `"1a1b1c"`
- `"aaaaaaaaaaaab"` -> `"12a1b"`
- `"AaA"` -> `"1A1a1A"`
- `"112"` -> `"2112"`
- `"éé"` -> `"1e1́1e1́"`
- `""` -> `""`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
