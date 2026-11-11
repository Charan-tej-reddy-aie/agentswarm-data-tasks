# fibonacci-number
Implement `fibonacci_number` in `fibonacci_number.py`. Python 3.11+ standard library only.

Require n, an exact built-in int in [0,1000]; negative numbers raise exact ValueError. Return, as an exact built-in int, the nth Fibonacci number F(n), where F(0) = 0, F(1) = 1 and F(n) = F(n-1) + F(n-2). Results must be exact for every allowed n, including values far beyond 64 bits (F(100) = 354224848179261915075); never use floats or a closed-form approximation. Each call should take well under a second.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[0]` -> `0`
- `[1]` -> `1`
- `[2]` -> `1`
- `[3]` -> `2`
- `[4]` -> `3`
- `[5]` -> `5`
- `[10]` -> `55`
- `[20]` -> `6765`
- `[30]` -> `832040`
- `[50]` -> `12586269025`
- `[90]` -> `2880067194370816120`
- `[100]` -> `354224848179261915075`
- `[True]` -> `raises TypeError`
- `[4.0]` -> `raises TypeError`
- `[-1]` -> `raises ValueError`
- `[1001]` -> `raises ValueError`

Only edit `fibonacci_number.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/fibonacci-number/check.py --solution "$PWD/tasks/fibonacci-number/fibonacci_number.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
