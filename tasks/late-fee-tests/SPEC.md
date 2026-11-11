# Write tests for a tiered library late fee function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `late_fee(days)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `late_fee` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

days (how many days a library book is overdue) must have exact built-in int
type. Bool, int subclasses, floats, strings, None and containers raise
TypeError. Check the type before the range, so -1.0 raises TypeError. days
below 0 or above 365 raises ValueError; 0 and 365 are valid. Otherwise return
the fee as an exact int: 0 for 0-2 days (grace period), 3 for 3-9 days, 8 for
10-29 days and 20 for 30-365 days. Each lower bound is inclusive (3 pays 3,
10 pays 8, 30 pays 20). Calls are deterministic; no mutable state or side
effects. Exception messages are unconstrained.

Examples: late_fee(0) == 0; late_fee(2) == 0; late_fee(3) == 3;
late_fee(9) == 3; late_fee(10) == 8; late_fee(29) == 8; late_fee(30) == 20;
late_fee(365) == 20. late_fee(-1) and late_fee(366) raise ValueError;
late_fee(True) and late_fee(5.0) raise TypeError.

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

Run `python3 tasks/late-fee-tests/check.py --solution "$PWD/tasks/late-fee-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
