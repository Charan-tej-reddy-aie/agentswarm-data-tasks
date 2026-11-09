# Plan capped retries with a numeric Retry-After floor

Implement `retry_delays(attempts, base_ms, cap_ms, retry_after)` in
`retry_delays.py`, using Python 3.11+ standard library only. No packages, files,
network, clock, random jitter or actual sleeping. Only edit the implementation
and optional task-local `IMPLEMENTATION.md`. This standalone planning helper
claims no production integration or complete HTTP Retry-After support.

The first three arguments must each have exact built-in type int; bool and int
subclasses are invalid. `retry_after` must be None or have exact built-in type
str; reject subclasses too. Any invalid type raises TypeError before value
validation, even when another argument has an invalid value. Error messages
are unconstrained. The allowed values satisfy `0 <= attempts <= 32` and
`0 <= base_ms <= cap_ms <= 1000000000`. Otherwise raise ValueError.

None means no server-specified minimum (floor zero). For a string, remove only
leading and trailing ASCII space and horizontal tab. The remaining text must
be one or more ASCII digits representing seconds in the inclusive range
0..1000000. Leading zeros are accepted, with no limit on their count. Empty or
all-space text, signs, fractions, exponent notation, dates, CR/LF, NBSP and
non-ASCII digits are invalid and raise ValueError. A million seconds is valid;
a million and one is invalid. Do not expose conversion-limit or overflow errors
for long headers. This deliberately supports ONLY numeric delay seconds, not
HTTP dates. There is no implicit current time or unit guessing.

Return a fresh list of exact integer millisecond delays. For each zero-based
retry index `i` from 0 through attempts-1, compute
`max(server_floor_ms, min(cap_ms, base_ms * 2**i))`.
The server floor is parsed seconds times 1000. Apply the exponential cap BEFORE
the server floor; a server delay can exceed cap_ms. The returned values are
individual delays, not cumulative timestamps. Base zero stays zero unless the
server floor raises it. Cap zero requires base zero. Attempt zero still validates
all types, numeric ranges and the header, then returns an empty list.

For example `(4, 100, 500, None)` returns `[100, 200, 400, 500]`;
`(3, 100, 500, ' 2\t')` returns `[2000, 2000, 2000]`.
Calls must be deterministic, never mutate inputs, and return independent lists.
There is no rounding, jitter, sleep, request execution or header precedence.

Run `python3 tasks/retry-delays/check.py --solution "$PWD/tasks/retry-delays/retry_delays.py"`.
Acceptance uses at least 60 exact synthetic cases covering caps, floors, zero,
large values, Unicode and invalid input. Public fixtures can be overfit;
source/scope review accompanies checks. Checks are not a security sandbox.
