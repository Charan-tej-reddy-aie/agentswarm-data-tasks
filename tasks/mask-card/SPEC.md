# Mask all but the last four characters

Implement `pub fn mask_card(input: &str) -> String` in `src/lib.rs`
(crate `mask-card`). Rust 2021, standard library only, no crates. Only edit
src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change the
checker, Cargo.toml, fixtures or this specification.

Treat the input as a sequence of `char`s (Unicode scalar values, not bytes).
Replace every char except the last four with `#` and keep the last four
unchanged, so the result has exactly as many chars as the input. Inputs of
four chars or fewer are returned unchanged. Every char counts and is masked
the same way, including spaces, tabs, newlines, hyphens, letters,
punctuation, combining marks and emoji. There is no trimming or
normalization. The empty string returns the empty string. Any input length
must work without panic.

Examples (input -> result):
- `"4556364607935616"` -> `"############5616"`
- `"64607935616"` -> `"#######5616"`
- `"1"` -> `"1"`
- `"abcd"` -> `"abcd"`
- `"Skippy"` -> `"##ippy"`
- `""` -> `""`
- `"🚀🚀🚀🚀🚀"` -> `"#🚀🚀🚀🚀"`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
