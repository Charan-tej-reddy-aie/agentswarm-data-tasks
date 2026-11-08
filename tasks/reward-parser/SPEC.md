# Reward parser for the feed importer

Implement `parse_reward(text: str) -> dict` in `reward_parser.py`. The importer
needs an exact amount and a conservative reward category from one free-text
reward. All input is a string. Return exactly `amount`, `currency`, `kind`:

- `amount`: a finite nonnegative `decimal.Decimal`, or `None`.
- `currency`: uppercase token below, or `None`.
- `kind`: `cash`, `crypto`, `points`, `site-balance`, or `unknown`.

Supported grammar (case insensitive; arbitrary Unicode whitespace between tokens):
optional `reward:` or `bounty:`, optional `up to`, `approximately` or `~`,
then one amount and currency in either order. Symbols `$`, `€`, `£` may appear
before the amount. An amount is ASCII digits, optionally properly grouped by
commas in groups of three, optionally followed by a dot and one or more digits.
No sign, exponent, decimal comma, range or multiple amounts. Preserve exact
Decimal value without float conversion or rounding. Leading zeroes are allowed.

Currencies: USD/EUR/GBP/CAD/AUD/CHF/JPY/INR are cash; USDC/USDT/ETH/BTC/SOL are
crypto; XTR and `points` are points; `credits` is site-balance. The last two
canonical currency tokens are POINTS and CREDITS. Symbols alone imply USD/EUR/GBP.
A symbol plus its matching cash code is allowed. `$` plus USDC/USDT is also allowed
(e.g. `$450 USDC`); other symbol/code conflicts are unknown.

Optional suffix `site balance`, `(site balance)` or `gross of site balance`
overrides kind to site-balance while retaining the currency. Optional literal
`(test fixture)` may follow any supported reward, after the balance suffix.
No other prefix/suffix/prose is accepted. Approximate/`up to` qualifiers preserve
the stated amount; the output is a parsed quote, not guaranteed payment.
Every unsupported/ambiguous input, including Unpaid, returns
`{"amount": None, "currency": None, "kind": "unknown"}`. Never infer zero for unpaid.

Examples: `$450 USDC` → Decimal('450'), USDC, crypto; `14 XTR` → Decimal('14'),
XTR, points; `1 USD gross of site balance` → Decimal('1'), USD, site-balance;
`€20` → Decimal('20'), EUR, cash; `0.05 ETH` → Decimal('0.05'), ETH, crypto.

Python 3.11+ stdlib only. No network, subprocesses, file/fixture/label lookup or
side effects in the solution. Only edit `tasks/reward-parser/reward_parser.py`
plus optional `IMPLEMENTATION.md`. Exact typed matches on the authored synthetic
cases and generated value/case/whitespace probes are required. Source review
also checks generalisation. Quick check: `python3 tasks/reward-parser/check.py`.
