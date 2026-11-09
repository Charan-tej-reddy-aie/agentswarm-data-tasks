# Write tests for an integer clamp

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `clamp(value, lower, upper)`. Do not change
it. Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `clamp` from `implementation`; use unittest.TestCase subclasses. No
third-party packages, files, subprocesses, networking or implementation source
inspection. Tests must assert public behavior, not identify a mutant. They run
without the task checker on their import path. No README-dependent checks.

All three inputs must have exact built-in int type. Bool, int subclasses,
floats, strings, None and containers raise TypeError. Check all input types
before comparing bounds, even if the bounds are reversed. If lower > upper,
raise ValueError. Otherwise return value clipped to the inclusive interval
[lower, upper], as an exact built-in int. Equal bounds are valid. Integers are
arbitrary precision. Calls are deterministic; no mutable state or side effects.
Exception messages are unconstrained.

Examples: clamp(3,1,5) == 3; clamp(-8,-3,4) == -3;
clamp(12,-3,4) == 4; clamp(9,2,2) == 2; clamp(0,-2,2) == 0;
clamp(-5,-9,-2) == -5. clamp(1,5,2) raises ValueError;
clamp(None,5,2) and clamp(True,0,2) raise TypeError.

Acceptance: at least eight discovered test methods, zero skipped tests and all
must pass against the provided reference implementation. The same tests then
run against ten supplied spec-contradicting implementations in fresh isolated
Python subprocesses. At least eight of ten must fail by a unittest assertion
failure or error. Empty suites, imports that fail before tests are discovered,
timeouts and system exits do not count as mutant kills. Never skip or mark
expected failures. The checker names the number of mutants killed; stronger
suites can kill all ten. Only the submitted test file is copied beside the
selected implementation; keep all helpers in that file. Each subprocess has
five seconds. The whole checker runs offline in Docker --network none.

Source/scope review accompanies the public fixtures. Checks must not mutate the
implementation, depend on fixture paths, or print acceptance markers.
