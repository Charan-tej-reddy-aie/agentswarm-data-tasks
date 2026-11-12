# Reverse the bits of a uint32

Implement `ReverseBits(n uint32) uint32` in package `reversebits`, file
`reverse_bits.go`. Use Go 1.23 standard library only. The supplied go.mod has
no external modules. Only edit reverse_bits.go and optional IMPLEMENTATION.md
in this task. Do not change the checker, module, fixtures or specification. No
file, clock or network access.

Write n as exactly 32 binary digits, including leading zeros. Return the
uint32 whose 32 binary digits are those digits in reverse order: bit 0 (the
lowest) moves to bit 31, bit 1 to bit 30, and so on up to bit 31 moving to
bit 0. Every uint32 value from 0 to 4294967295 is valid. Reversing twice gives
back the original value. Do not reverse bytes or nibbles as units, and do not
drop leading zeros before reversing.

Examples: 0 -> 0; 1 -> 2147483648; 2 -> 1073741824; 2147483648 -> 1;
4294967295 -> 4294967295; 4294967294 -> 2147483647;
43261596 (00000010100101000001111010011100) -> 964176192
(00111001011110000010100101000000).

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
