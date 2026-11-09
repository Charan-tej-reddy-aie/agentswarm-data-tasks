# Implement a marketplace fee helper and runnable docstring examples
Implement platform_fee(amount) in platform_fee.py, Python 3.11+ standard library.
Require an exact built-in int >=0, in integer cents. Reject bool, int subclasses
and every other type with exact TypeError; negative ints raise exact ValueError.
Return an exact built-in int: ceiling(amount*3/100), using arbitrary precision
integer arithmetic (no floats). Deterministic, no side effects or mutable state.
Add a function docstring on platform_fee containing at least THREE runnable
Python doctest examples. The checker parses and runs that function's docstring
with doctest, requires at least three examples and no failures, then runs its
independent functional cases. Documentation in README does not count.
Examples: 0 -> 0; 1 -> 1; 33 -> 1; 34 -> 2; 100 -> 3; 101 -> 4;
10**100 -> 3*10**98; -1 -> ValueError; True and 1.0 -> TypeError.
Use at least the examples 0, 100 and 101 in your function docstring, with outputs
0, 3 and 4 respectively; the checker requires those calls and outputs explicitly.

Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Exception messages are unconstrained. Every spec example is checked. No files,
network, packages or README-dependent functional checks. This standalone unpaid
exercise makes no production-use claim; public checks need source/scope review.
