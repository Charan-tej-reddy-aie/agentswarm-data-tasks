# Sum of squares with a safe-integer guard

Implement export function sumSquares(values) in sum_squares.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number;
boxed Number objects (also subclasses), bigints, strings and all other values
raise exact TypeError. Validate ALL types before any value check. Then every
element must be an integer (Number.isInteger) with absolute value at most 1e7,
otherwise exact RangeError (this rejects NaN, Infinity and fractions).

Return, as a primitive number, the exact mathematical sum of the squares of
all elements. The empty array returns 0. When the exact sum is greater than
Number.MAX_SAFE_INTEGER (2**53 - 1), throw exact RangeError; a sum equal to
Number.MAX_SAFE_INTEGER is returned. Never return -0: sumSquares([-0]) is 0.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([]) -> 0`
- `([5]) -> 25`
- `([1, 2, 3]) -> 14`
- `([-3, 4]) -> 25`
- `([0, 0]) -> 0`
- `([-1, -1, -1]) -> 3`
- `([10000000]) -> 100000000000000`
- `([-10000000, 10000000]) -> 200000000000000`
- `([7, 0, -7]) -> 98`
- `([2, 2, 2, 2]) -> 16`
- `([-0]) -> 0`
- `([0,-0]) -> 0`
- `([2**13]) -> 2**26`
- `([-(2**13),2**13]) -> 2**27`
- `([1e7+1]) -> RangeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([Infinity]) -> RangeError`
- `([-1e7-1]) -> RangeError`
- `(['1']) -> TypeError`
- `([1n]) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `([1.5,'x']) -> TypeError`
- `(Array(1)) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit sum_squares.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/sum-squares/check.mjs --solution "$PWD/tasks/sum-squares/sum_squares.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
