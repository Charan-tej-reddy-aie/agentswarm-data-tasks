# Convert an ISO week date into a calendar date

Implement `iso_week_date(year, week, day)` in `iso_week_date.py` using Python
3.11+ standard library only. This standalone offline helper claims no production
integration. No packages, files, network, clock or locale dependence. Only edit
the implementation and optional task-local `IMPLEMENTATION.md`.

All three arguments must have exact built-in type int (`type(x) is int`). Reject
bool, float, str, None, containers and int subclasses with TypeError. Validate
ALL types before any numeric range: an invalid year together with a wrongly
typed day still raises TypeError. Error messages are unconstrained.

Interpret year as the ISO week-numbering year, NOT the calendar year. Week 1
contains January 4 and starts on Monday. Day is 1 for Monday through 7 for
Sunday. Year must be 1..9999, week 1..53, and day 1..7. Week 53 is allowed only
when that ISO year has 53 weeks. Any invalid numeric value, nonexistent week,
or resulting calendar date outside years 1..9999 raises ValueError. In
particular `(9999, 52, 6)` and `(9999, 52, 7)` overflow and are invalid.

Return an exact built-in str containing the calendar date as `YYYY-MM-DD`, with
four year digits and two month/day digits, including leading zeros. For example
`(2020, 1, 1)` gives `2019-12-30`; `(2020, 53, 7)` gives `2021-01-03`;
`(2021, 1, 1)` gives `2021-01-04`; `(1, 1, 1)` gives `0001-01-01`.
Do not approximate weeks as calendar-year offsets or assume every year has
week 53. There is no timezone, timestamp, parsing or current-date behavior.
Calls are deterministic and inputs are not mutated. The pinned checker uses
only immutable task-local fixtures and never compares changing root files.

Run `python3 tasks/iso-week-date/check.py --solution "$PWD/tasks/iso-week-date/iso_week_date.py"`.
Acceptance covers at least 60 synthetic cases, boundaries and exact types.
Public fixtures can be overfit; source/scope review accompanies the check.
