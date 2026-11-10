# Write tests for an inclusive range check

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `is_between(value, lower, upper)`. Do not
change it. Only edit tests_submission.py and optional IMPLEMENTATION.md in this
task. Import `is_between` from `implementation`; use unittest.TestCase
subclasses. No third-party packages, files, subprocesses, networking or
implementation source inspection. Tests must assert public behavior, not
identify a mutant. They run without the task checker on their import path.

All three inputs must have exact built-in int type. Bool, int subclasses,
floats, strings, None and containers raise TypeError. Check all input types
before comparing bounds, even if the bounds are reversed. If lower > upper,
raise ValueError. Otherwise return the exact bool True when
lower <= value <= upper (both ends INCLUSIVE) and False otherwise. Equal bounds
are valid. Integers are arbitrary precision. Calls are deterministic; no
mutable state or side effects. Exception messages are unconstrained.

Examples: is_between(3,1,5) is True; is_between(1,1,5) is True;
is_between(5,1,5) is True; is_between(0,1,5) is False; is_between(6,1,5) is
False; is_between(2,2,2) is True. is_between(1,5,2) raises ValueError;
is_between(None,5,2) and is_between(True,0,2) raise TypeError.

Acceptance: at least eight discovered test methods, zero skipped tests and all
must pass against the provided reference implementation. The same tests then
run against ten supplied spec-contradicting implementations in fresh isolated
Python subprocesses. At least eight of ten must fail by a unittest assertion
failure or error. Empty suites, imports that fail before tests are discovered,
timeouts and system exits do not count as mutant kills. Never skip or mark
expected failures. The checker names the number of mutants killed; stronger
suites can kill all ten. Only the submitted test file is copied beside the
selected implementation; keep all helpers in that file. Each subprocess has
five seconds.

Run `python3 tasks/between-tests/check.py --solution "$PWD/tasks/between-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
