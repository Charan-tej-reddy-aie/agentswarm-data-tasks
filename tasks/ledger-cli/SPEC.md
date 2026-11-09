# Sum or count signed integer tokens from the command line

Implement ledger.py, a Python 3.11+ standard-library argparse script. Only edit
ledger.py and optional IMPLEMENTATION.md in this task. This is a CLI exercise:
there is no imported function API and no TypeScript, packages, file I/O, network,
clock or production integration. The checker launches the script as a subprocess.

Arguments: optional --mode with exactly sum or count, default sum, then zero or
more positional integer tokens. Options use standard argparse behavior, including
--help (exit 0, stdout help, no stderr); no abbreviation contract is required.
Use -- before signed positional tokens in portable invocations. Each token is
exactly [+-]?[0-9]{1,100}: one optional ASCII sign and 1..100 ASCII digits. Leading
zeroes and plus signs are allowed. Whitespace within a token, Unicode digits,
hexadecimal, decimals, underscores and empty tokens are invalid. No splitting
inside a token is performed. Each command-line argument is a string; there is
no object coercion or subclass input API. Values are arbitrary precision within
the token length limit. sum prints the exact arithmetic sum; count prints the
number of valid tokens (it still validates every token). An empty input prints
0 in either mode. Result is base-10 canonical integer text plus exactly one LF;
exit 0, stderr empty. No extra stdout. Invalid mode, unknown option, missing
option value or invalid integer token: exit exactly 2, stdout empty and nonempty
stderr (argparse diagnostic wording is unconstrained).

Examples (argument arrays, followed by exact stdout and exit):
[] -> "0\n", 0; ["--","2","-5","+7"] -> "4\n", 0;
["--mode","count","--","02","-0","+3"] -> "3\n", 0;
["--mode","sum","--","0002","-2"] -> "0\n", 0;
["--mode","count","--","x"] -> "", 2;
["--","1_000"] -> "", 2; ["--mode","mean"] -> "", 2.
Repeated invocations have identical results. --help is checked separately.
Every example is a fixture. Docker acceptance uses --network none and a pinned
Python image. No README contents participate. Source/scope review is required.
