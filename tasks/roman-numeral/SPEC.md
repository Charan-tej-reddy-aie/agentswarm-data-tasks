# Convert integers to Roman numerals

Implement `ToRoman(n int) string` in package `romannumeral`, file `roman.go`.
Use Go 1.23 standard library only. The supplied go.mod has no external
modules. Only edit roman.go and optional IMPLEMENTATION.md in this task. Do not
change the checker, module, fixtures or specification. No file, clock or
network access.

For 1 <= n <= 3999 return the standard uppercase Roman numeral, built greedily
from M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9,
V=5, IV=4, I=1 (subtractive forms are required: 4 is IV, never IIII). Any
other n, including 0, negatives, 4000 and the int64 extremes, returns exactly
the lowercase word `invalid`. No spaces, overlines or lowercase numerals.

Examples: 1 -> `I`; 3 -> `III`; 4 -> `IV`; 9 -> `IX`; 14 -> `XIV`;
40 -> `XL`; 90 -> `XC`; 400 -> `CD`; 944 -> `CMXLIV`; 1994 -> `MCMXCIV`;
2024 -> `MMXXIV`; 3999 -> `MMMCMXCIX`; 0 -> `invalid`; -1 -> `invalid`;
4000 -> `invalid`.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. A pass remains CHECK_PASS_UNVERIFIED until independent
source/scope review.
