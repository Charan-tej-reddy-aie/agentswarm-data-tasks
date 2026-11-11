# seconds-to-clock
Implement `seconds_to_clock` in `seconds_to_clock.py`. Python 3.11+ standard library only.

Require seconds, an exact built-in int in [0,359999] (up to 99:59:59); negative numbers raise exact ValueError. Return, as an exact built-in str, the duration as HH:MM:SS: whole hours, then remaining whole minutes (0-59), then remaining seconds (0-59), each written as exactly two decimal digits with a leading zero when needed and separated by single colons. Hours never wrap at 24 (90000 seconds is "25:00:00"). 0 returns "00:00:00".

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `'00:00:00'`
- `[1]` -> `'00:00:01'`
- `[9]` -> `'00:00:09'`
- `[59]` -> `'00:00:59'`
- `[60]` -> `'00:01:00'`
- `[61]` -> `'00:01:01'`
- `[599]` -> `'00:09:59'`
- `[3599]` -> `'00:59:59'`
- `[3600]` -> `'01:00:00'`
- `[3661]` -> `'01:01:01'`
- `[45296]` -> `'12:34:56'`
- `[86399]` -> `'23:59:59'`
- `[86400]` -> `'24:00:00'`
- `[90000]` -> `'25:00:00'`
- `[359999]` -> `'99:59:59'`
- `[True]` -> `raises TypeError`
- `[60.0]` -> `raises TypeError`
- `['60']` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[360000]` -> `raises ValueError`

Only edit `seconds_to_clock.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/seconds-to-clock/check.py --solution "$PWD/tasks/seconds-to-clock/seconds_to_clock.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
