# Largest gap between neighbouring integers

Implement export function maxAdjacentGap(values) in max_adjacent_gap.mjs, Node
22 standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number;
boxed Number objects (also subclasses), bigints, strings and all other values
raise exact TypeError. Validate ALL types before any value check. Then every
element must be an integer (Number.isInteger) with absolute value at most 1e9,
otherwise exact RangeError (this rejects NaN, Infinity and fractions).

Return, as a primitive number, the largest absolute difference
|values[i] - values[i-1]| between two neighbouring elements, keeping the
given order (do not sort; the last and first elements are not neighbours).
Arrays with fewer than two elements return 0. Never return -0:
maxAdjacentGap([-0, 0]) is 0.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([]) -> 0`
- `([5]) -> 0`
- `([1, 4]) -> 3`
- `([4, 1]) -> 3`
- `([1, 3, 8, 9]) -> 5`
- `([10, 2, 7]) -> 8`
- `([-5, 5]) -> 10`
- `([0, 0, 0]) -> 0`
- `([3, -3, 3]) -> 6`
- `([1, 2, 3, 100, 101]) -> 97`
- `([-1000000000, 1000000000]) -> 2000000000`
- `([-0]) -> 0`
- `([-0,0]) -> 0`
- `([0,-0,0]) -> 0`
- `([2**20,-(2**20)]) -> 2**21`
- `([1e9+1]) -> RangeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([Infinity]) -> RangeError`
- `([-1e9-1]) -> RangeError`
- `(['1']) -> TypeError`
- `([1n]) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `([1.5,'x']) -> TypeError`
- `(Array(1)) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit max_adjacent_gap.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/max-adjacent-gap/check.mjs --solution "$PWD/tasks/max-adjacent-gap/max_adjacent_gap.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
