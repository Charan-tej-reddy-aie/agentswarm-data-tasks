# Write tests for a temperature band function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `temp_band(celsius)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `temp_band` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

celsius must have exact built-in int type. Bool, int subclasses, floats,
strings, None and containers raise TypeError. Check the type before the range,
so -101.0 raises TypeError. celsius below -100 or above 100 raises ValueError;
-100 and 100 are valid. Otherwise return an exact lowercase str: 'freezing'
below 0, 'cold' for 0-9, 'mild' for 10-19, 'warm' for 20-29 and 'hot' for 30
and above. Each lower bound is inclusive (0 is 'cold', 10 is 'mild', 20 is
'warm', 30 is 'hot'). Calls are deterministic; no mutable state or side
effects. Exception messages are unconstrained.

Examples: temp_band(-100) == 'freezing'; temp_band(-1) == 'freezing';
temp_band(0) == 'cold'; temp_band(9) == 'cold'; temp_band(10) == 'mild';
temp_band(20) == 'warm'; temp_band(29) == 'warm'; temp_band(30) == 'hot';
temp_band(100) == 'hot'. temp_band(101) and temp_band(-101) raise ValueError;
temp_band(True) and temp_band(15.0) raise TypeError.

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

Run `python3 tasks/temp-band-tests/check.py --solution "$PWD/tasks/temp-band-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
