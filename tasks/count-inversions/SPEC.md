# Count the inversions of an integer array

Implement export function countInversions(values) in count_inversions.mjs,
Node 22 standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number;
boxed Number objects (also subclasses), bigints, strings and all other values
raise exact TypeError. Validate ALL types before any length or value check.
Then an array longer than 1000 elements raises exact RangeError, and every
element must be an integer (Number.isInteger) with absolute value at most
1e9, otherwise exact RangeError (this rejects NaN, Infinity and fractions).

Return, as a primitive number, the number of inversions: pairs of positions
i < j with values[i] > values[j]. Equal values are not an inversion (-0 and 0
are equal). Count positions, not distinct values, so repeated values count
once per pair. An empty or sorted array returns 0; a strictly decreasing
array of length n returns n*(n-1)/2. Never return -0: the checker compares
with Object.is, so countInversions([]) must be 0, not -0.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([]) -> 0`
- `([7]) -> 0`
- `([1, 2]) -> 0`
- `([2, 1]) -> 1`
- `([2, 2]) -> 0`
- `([3, 1, 2]) -> 2`
- `([2, 3, 1]) -> 2`
- `([1, 3, 2, 4]) -> 1`
- `([4, 3, 2, 1]) -> 6`
- `([5, 5, 4, 4]) -> 4`
- `([1, 5, 2, 6, 3]) -> 3`
- `([-1, -2, 0]) -> 1`
- `([1000000000, -1000000000]) -> 1`
- `([-0,0]) -> 0`
- `([0,-0]) -> 0`
- `([1,-0]) -> 1`
- `(Array.from({length:1000},(_,i)=>1000-i)) -> 499500`
- `([1e9+1]) -> RangeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([Infinity]) -> RangeError`
- `([-1e9-1]) -> RangeError`
- `(Array(1001).fill(0)) -> RangeError`
- `(['1']) -> TypeError`
- `([1n]) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `([1.5,'x']) -> TypeError`
- `(Array(1001).fill('x')) -> TypeError`
- `(Array(1)) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit count_inversions.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/count-inversions/check.mjs --solution "$PWD/tasks/count-inversions/count_inversions.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
