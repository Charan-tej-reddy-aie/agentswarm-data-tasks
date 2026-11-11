# Write tests for a parcel weight tier function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `parcel_tier(grams)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `parcel_tier` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

grams must have exact built-in int type. Bool, int subclasses, floats,
strings, None and containers raise TypeError. Check the type before the range,
so 0.0 raises TypeError. grams below 1 or above 30000 raises ValueError; 1 and
30000 are valid. Otherwise return an exact lowercase str: 'letter' for 1-499,
'small' for 500-1999, 'medium' for 2000-9999 and 'large' for 10000-30000.
Each lower bound is inclusive (500 is 'small', 2000 is 'medium', 10000 is
'large'). Calls are deterministic; no mutable state or side effects. Exception
messages are unconstrained.

Examples: parcel_tier(1) == 'letter'; parcel_tier(499) == 'letter';
parcel_tier(500) == 'small'; parcel_tier(1999) == 'small';
parcel_tier(2000) == 'medium'; parcel_tier(9999) == 'medium';
parcel_tier(10000) == 'large'; parcel_tier(30000) == 'large'.
parcel_tier(0) and parcel_tier(30001) raise ValueError; parcel_tier(True) and
parcel_tier(700.0) raise TypeError.

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

Run `python3 tasks/parcel-tier-tests/check.py --solution "$PWD/tasks/parcel-tier-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
