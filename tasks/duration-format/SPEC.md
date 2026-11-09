# Format whole seconds into compact duration text

Implement `FormatSeconds(seconds int64) string` in package `durationformat`, file
`duration.go`. Use Go 1.23 standard library only. The supplied go.mod has no
external modules. Only edit duration.go and optional IMPLEMENTATION.md in this
task. Do not change checker, module, tests or specification. No file, clock or
network access. This is a standalone exercise with no production integration.

Negative seconds return exactly `invalid`. Zero returns exactly `0s`. Positive
values are decomposed greedily into days (86400 seconds), hours (3600), minutes
(60) and seconds (1), in that order. Emit each nonzero component as its base-10
integer immediately followed by lowercase d/h/m/s. Join emitted components with
one ASCII space. Omit zero components, with no leading/trailing spaces. Days
are unbounded; never roll them into weeks, months or years. Every int64 value is
supported; do not convert to nanoseconds or overflow by multiplying. Inputs
have the statically declared exact int64 type: named Go integer types require
explicit conversion by the caller; no dynamic coercions exist in this API.

Examples: -1 -> `invalid`; 0 -> `0s`; 1 -> `1s`; 60 -> `1m`; 61 -> `1m 1s`;
3600 -> `1h`; 3661 -> `1h 1m 1s`; 86400 -> `1d`;
90061 -> `1d 1h 1m 1s`; 172801 -> `2d 1s`.
The largest int64, 9223372036854775807, returns
`106751991167300d 15h 30m 7s`. Minimum int64 returns `invalid`.

The checker is Go code that copies only the candidate into an isolated temporary
module and compiles and runs trusted tests. Preload the digest-pinned golang
Docker image shown in the issue. Acceptance runs with --network none,
GOPROXY=off and GOSUMDB=off; no dependencies are downloaded. A cold Go build
may take about a minute. Checker failures include compile errors. Public
fixtures are synthetic; source/scope review accompanies acceptance. Results
must be deterministic across repeated calls and root documents are not inputs.
