# Find the longest binary gap

Implement `BinaryGap(n uint32) int` in package `binarygap`, file
`binary_gap.go`. Use Go 1.23 standard library only. The supplied go.mod has
no external modules. Only edit binary_gap.go and optional IMPLEMENTATION.md in
this task. Do not change the checker, module, fixtures or specification. No
file, clock or network access.

Write n in binary without leading zeros. A binary gap is a maximal run of
consecutive 0 bits that has a 1 bit on both sides. Return the length of the
longest binary gap, or 0 when there is none. Zeros after the lowest 1 bit
(trailing zeros) are not a gap because no 1 bit follows them, and leading
zeros are never written. Every uint32 value from 0 to 4294967295 is valid,
including values with the top bit set; 0, powers of two and numbers with only
adjacent 1 bits return 0.

Examples: 0 -> 0; 9 (1001) -> 2; 20 (10100) -> 1; 15 (1111) -> 0;
32 (100000) -> 0; 529 (1000010001) -> 4; 1041 (10000010001) -> 5;
2147483649 (1 followed by 30 zeros and a 1) -> 30.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
