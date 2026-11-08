# Growth funnel by channel and UTC day

Implement `python3 funnel.py <events.csv> [--internal-actors actors.txt]` using
Python 3.11+ standard library only, offline. agentswarm.space uses this exact
funnel definition for its growth reporting; this component computes that report.
Only edit `tasks/funnel-calc/funnel.py`, plus optional `IMPLEMENTATION.md` there.
Do not edit checks, specs, fixtures or other tasks.

Input is UTF-8 CSV with header `ts,channel,actor,event`. Fields are nonempty;
identifiers are case-sensitive opaque strings (CSV quoting can contain commas).
Timestamps are valid offset-aware ISO8601 with seconds, ending in `Z` or a
numeric `±HH:MM` offset. Convert instants to UTC before computing days or gaps.
Rows may be unsorted or duplicated. An optional UTF-8 actor file lists one exact
actor per line; blank lines are ignored. Omitted or empty file excludes nobody.
Exclude internal actors from every stage and from retention history.
Malformed CSV/timestamp behavior is outside this task; acceptance uses valid CSV.

Recognized event names are `acquisition`, `activation`, `referral`, `revenue`
and `spam`. Other event names (including literal `retention`) are ignored.
Stage counts are unique actors, independently per UTC day and channel. There
are no prerequisites between stages: a revenue actor need not have acquisition.
Acquisition, activation, referral and revenue come from their named events.
Retention is an activation by an actor with a strictly earlier eligible
activation at most 7*24 hours earlier, inclusive of the upper bound. History
crosses days and channels. Equal timestamps, even in different channels, do not
qualify each other. The later activation's UTC day/channel receives retention.
Multiple qualifying activations still count that actor only once in each group.

A `spam` event marks that actor for that UTC day AND channel, independent of row
order or event time within the day. A marked actor still counts in acquisition
but never in activation, retention, referral or revenue for that group. Spammed
activations do not establish retention history. A spam event in another day or
channel does not suppress an otherwise eligible activation.

Print exactly one JSON array to stdout, with no diagnostic prose. Each object
has exactly `day`, `channel`, `acquisition`, `activation`, `retention`, `referral`,
`revenue`. `day` is `YYYY-MM-DD`, `channel` is the input string, all counts are
nonnegative JSON integers (not booleans). Include all five stages, even zeroes.
Include a group whenever at least one noninternal acquisition/activation/referral/
revenue event exists, even if spam suppression leaves all counts zero. Spam-only,
unknown-only and internal-only groups are absent. Sort by `(day, channel)` using
ordinary string order. JSON whitespace/object key order do not matter; array
order, types, keys and values must match exactly. Empty input prints `[]`.

Example: one actor activating at `2026-11-01T12:00:00Z` in `search` and again at
`2026-11-08T12:00:00Z` in `social` counts once in activation on each day, and once
in retention only on November 8 in social (exactly seven days later).

Quick check: `python3 tasks/funnel-calc/check.py --solution "$PWD/tasks/funnel-calc/funnel.py"`.
Acceptance uses a separate trusted checkout pinned by the issue, with synthetic
CSV fixtures and order/duplication invariances. Public checks can be overfit;
source and scope review also apply. Checks execute contributor code with a
timeout, not a security sandbox; see CONTRIBUTING.md. No member data is used.
