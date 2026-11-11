# Convert a uint32 to its Gray code

Implement `GrayCode(n uint32) uint32` in package `graycode`, file
`gray_code.go`. Use Go 1.23 standard library only. The supplied go.mod has
no external modules. Only edit gray_code.go and optional IMPLEMENTATION.md in
this task. Do not change the checker, module, fixtures or specification. No
file, clock or network access.

Return the reflected binary Gray code of n: n XOR (n shifted right by one
bit), computed on all 32 bits. Every uint32 value from 0 to 4294967295 is
valid. The top bit of the result equals the top bit of n, and the codes of
consecutive numbers differ in exactly one bit. Do not decode (this is the
Gray code of n, not the number whose Gray code is n), do not shift left and
do not drop or wrap the top bit.

Examples: 0 -> 0; 1 -> 1; 2 -> 3; 3 -> 2; 4 -> 6; 7 -> 4; 8 -> 12; 15 -> 8; 4294967295 -> 2147483648; 2147483648 -> 3221225472.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
