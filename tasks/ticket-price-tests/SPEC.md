# Write tests for an age-based ticket price function

Write `tests_submission.py` using Python 3.11+ standard library unittest. The
provided `implementation.py` exports `ticket_price(age)`. Do not change it.
Only edit tests_submission.py and optional IMPLEMENTATION.md in this task.
Import `ticket_price` from `implementation`; use unittest.TestCase subclasses.
No third-party packages, files, subprocesses, networking or implementation
source inspection. Tests must assert public behavior, not identify a mutant.
They run without the task checker on their import path.

age must have exact built-in int type. Bool, int subclasses, floats, strings,
None and containers raise TypeError. Check the type before the range, so -1.0
raises TypeError. age below 0 or above 120 raises ValueError; 0 and 120 are
valid. Otherwise return the price as an exact int: 0 for ages 0-3, 5 for ages
4-12, 12 for ages 13-64 and 7 for ages 65-120. Each lower bound is inclusive
(4 pays 5, 13 pays 12, 65 pays 7). Calls are deterministic; no mutable state
or side effects. Exception messages are unconstrained.

Examples: ticket_price(0) == 0; ticket_price(3) == 0; ticket_price(4) == 5;
ticket_price(12) == 5; ticket_price(13) == 12; ticket_price(64) == 12;
ticket_price(65) == 7; ticket_price(120) == 7. ticket_price(-1) and
ticket_price(121) raise ValueError; ticket_price(True) and ticket_price(30.0)
raise TypeError.

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

Run `python3 tasks/ticket-price-tests/check.py --solution "$PWD/tasks/ticket-price-tests/tests_submission.py"`.
The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED
until independent source/scope review.
