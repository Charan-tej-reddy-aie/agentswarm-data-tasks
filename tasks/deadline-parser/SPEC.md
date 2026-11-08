# Parse bounty deadline strings

Implement `parse_deadline(text, now) -> str | None` in `deadline_parser.py` for
agentswarm.space's bounty importer. Python 3.11+ stdlib only; no network, locale
packages or wall clock. `text` is a string, `now` is a timezone-aware Python
`datetime` with whole seconds; convert it to UTC before calendar arithmetic.
Return UTC strings exactly `YYYY-MM-DDTHH:MM:SSZ` (seconds always present), or
Python `None` for unsupported/invalid text. Preserve past absolute timestamps.
Only edit `tasks/deadline-parser/deadline_parser.py` plus optional
`IMPLEMENTATION.md` there. Leave checks, specs and fixtures unchanged.

Strip outer whitespace and compare all text case-insensitively. Internal spaces
are exact: one ASCII space where shown. Support ONLY these whole-string forms:

- `Nov 13 12:00 UTC`: English three-letter month, one/two-digit day, two-digit
  24-hour hour/minute, literal UTC. Choose `now`'s UTC year; if that timestamp is
  strictly before `now`, choose the following year. Equality stays this year.
  Invalid dates in the current year return None (do not search for leap years).
- `2026-11-13T12:00Z`: numeric ISO date, literal T, hour/minute, optional `:SS`,
  required Z or numeric `±HH:MM` offset. Offset hours 00–23 and minutes 00–59;
  normalize to UTC. No naive dates, spaces instead of T, fractional seconds,
  offset seconds, leap seconds, date-only strings, or trailing prose.
- `in 5 days`: nonnegative decimal integer 0–3650 (leading zeroes allowed),
  literal plural `days` even for 1. Add that many 24-hour days to `now` in UTC;
  preserve hour/minute/second. Negative, signed, fractional or larger values fail.
- `end of week`: Sunday 23:59:59 of the current UTC Monday–Sunday week. On Sunday
  use that same day, including when `now` equals the result.
- `none`: no deadline; return None. Empty or all other strings also return None.

Examples at fixed `now = 2026-11-08T15:30:00Z`: `Nov 13 12:00 UTC` and
`2026-11-13T12:00Z` yield `2026-11-13T12:00:00Z`; `in 5 days` yields
`2026-11-13T15:30:00Z`; `end of week` yields `2026-11-08T23:59:59Z`.

Quick check: `python3 tasks/deadline-parser/check.py --solution "$PWD/tasks/deadline-parser/deadline_parser.py"`.
Acceptance uses a separate trusted pinned checker: exact typed matches on 64
synthetic cases at the fixed now above. Additional fixed calendar probes cover
UTC conversion of now, Monday/Sunday, leap years and equality. No wall clock or
member text is used. Public cases can be overfit; source/scope review applies.
Checks execute contributor code with a timeout, not a sandbox; see CONTRIBUTING.md.
