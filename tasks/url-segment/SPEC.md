# Encode a task identifier as a URL path segment in Rust

Implement pub fn encode_segment(input: &str) -> String in src/lib.rs, Rust 1.89
standard library only. Only edit src/lib.rs and optional IMPLEMENTATION.md.
Do not change Cargo.toml, checker, fixtures or spec. The static input type is
&str (valid UTF-8); Rust's type rules apply, with no dynamic subclass or coercion
contract. Encode UTF-8 bytes individually. Leave only ASCII A-Z, a-z, 0-9 and
-._~ unchanged. Every other byte becomes '%' followed by exactly two UPPERCASE
ASCII hex digits, including leading zeroes. Spaces become %20, never '+'.
Encode existing percent signs too; do not treat input as an already encoded URL.
No splitting, trimming, normalization or path interpretation. Preserve byte
order. Empty input returns empty String. Calls are deterministic and independent,
with no input mutation, files, network, packages or global mutable state.
Examples: "" -> ""; "task-1._~" -> "task-1._~"; "a/b c" -> "a%2Fb%20c";
"%2F" -> "%252F"; "é" -> "%C3%A9"; one NUL (U+0000) -> "%00";
"+?" -> "%2B%3F". Every example and all 128 ASCII bytes are checked.
The checker copies only lib.rs into a temporary crate with trusted tests and
runs cargo test --offline in the batch9 digest-pinned Rust image with network
none. No README-dependent checks. Source/scope review remains required.
