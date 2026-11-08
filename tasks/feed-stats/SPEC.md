# Summarise one task-feed page

The project needs reproducible task/reward/age/tag metrics without retaining member text. Build `feed_stats.py <feed.json>`, printing exactly one JSON object to stdout, exit 0. Summarise the returned page only; pagination, fetching, authentication and deployment are out of scope.

Input follows the public `GET /api/feed?type=task` envelope: `{"items": [...], "nextCursor": null, "now": "2026-11-08T12:00:00Z"}`. Only field names/types were inspected; all fixture records were authored synthetically. Ignore unknown fields. Each item has `id`, `type` (must be `task`), `status` (nonempty string), `createdAt`, `tags` (list of strings), and optional `bounty` (null or object with optional `amountUsd`, `reward` and other fields). IDs are unique nonempty strings. Do not read `title`, `body` or author data into the summary.

Output keys (and no others):
- `total`: item count.
- `by_status`: object counting observed statuses, including unfamiliar statuses. Empty page: `{}`.
- `reward_buckets`: object with all four keys: `none`, `text`, `under_10`, `at_least_10`. Missing/null/empty bounty, or amount 0, belongs to `none` unless a nonblank textual `reward` is present (then `text`). Positive finite numeric `amountUsd` takes precedence: (0,10) is `under_10`, ≥10 is `at_least_10`. Never parse dollar amounts from text. Missing amount plus a blank/missing reward is `none`.
- `median_age_hours`: median of max(0, (`now` - `createdAt`) in hours), using the envelope's clock and not wall time. Both timestamps must be ISO 8601 with a timezone, support `Z`, offsets and fractional seconds. Even counts average the two middle ages. Empty page: null. Numeric answers within 1e-6 pass.
- `top_tags`: at most five `{"tag": str, "count": int}` objects. Strip whitespace and casefold tags, discard empty tags, count a tag once per item, order by descending count then ascending normalised Unicode tag. Empty page: `[]`.

Reject malformed JSON, missing required fields, wrong types (booleans are not amounts), invalid/naive timestamps, non-task rows, nonfinite/negative amounts, non-string reward, non-object bounty, duplicate/missing IDs and invalid tags. Exit nonzero, put a nonempty diagnostic on stderr and no summary on stdout. `nextCursor` and unrelated fields are ignored. Missing file/wrong CLI arity must also fail clearly. Python 3.11+ stdlib only; no network.

Acceptance from repo root: `python3 tasks/feed-stats/check.py --solution "$PWD/tasks/feed-stats/feed_stats.py"`. For PR review run the separate pinned trusted checkout command in the issue. Scope: implementation file plus optional implementation README. The check tests a synthetic page, empty pages, boundaries, timezones, validation failures, and newly generated synthetic pages.
