# Keep only ASCII letters and digits

Implement `pub fn keep_alnum(input: &str) -> String` in `src/lib.rs`
(crate `keep-alnum`). Rust 2021, standard library only, no crates. Only edit
src/lib.rs and optional IMPLEMENTATION.md in this task. Do not change the
checker, Cargo.toml, fixtures or this specification.

Treat the input as a sequence of `char`s (Unicode scalar values, not bytes).
Return a String holding, in their original order and unchanged, only the
chars that are ASCII letters A-Z, a-z or ASCII digits 0-9. Every other char
is dropped, including spaces, tabs, newlines, underscores, hyphens,
punctuation, accented and other non-ASCII letters (such as é), non-ASCII
digits (such as Arabic-Indic ١), combining marks and emoji. There is no case
change, and leading zeros are kept. The empty string returns the empty
string. Any input length must work without panic.

Examples (input -> result):
- `""` -> `""`
- `"Hello, World!"` -> `"HelloWorld"`
- `"snake_case"` -> `"snakecase"`
- `"0042"` -> `"0042"`
- `"café"` -> `"caf"`
- `"١٢"` -> `""`
- `"x🚀y"` -> `"xy"`
- `"\t1\n2 "` -> `"12"`

The checker copies only src/lib.rs into a fresh temporary crate and runs
trusted integration tests with `cargo test --offline`. Preload the
digest-pinned rust Docker image shown in the issue; acceptance runs with
--network none. A cold build may take about a minute. A pass remains
CHECK_PASS_UNVERIFIED until independent source/scope review.
