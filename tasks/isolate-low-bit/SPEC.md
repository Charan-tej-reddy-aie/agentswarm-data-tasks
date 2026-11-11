# Keep only the lowest set bit of a uint32

Implement `IsolateLowBit(n uint32) uint32` in package `isolatelowbit`, file
`isolate_low_bit.go`. Use Go 1.23 standard library only. The supplied go.mod
has no external modules. Only edit isolate_low_bit.go and optional
IMPLEMENTATION.md in this task. Do not change the checker, module, fixtures
or specification. No file, clock or network access.

Return the uint32 that keeps only the lowest (least significant) 1 bit of n
and clears every other bit, so the result is a power of two. When n is 0
there is no 1 bit and the result is 0. Every uint32 value from 0 to
4294967295 is valid, including values with the top bit set (2147483648
returns 2147483648). Do not return the highest set bit, the lowest clear bit
or a bit position.

Examples: 0 -> 0; 1 -> 1; 2 -> 2; 6 -> 2; 12 -> 4; 40 -> 8; 96 -> 32; 4294967295 -> 1; 2147483648 -> 2147483648; 2147483649 -> 1.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
