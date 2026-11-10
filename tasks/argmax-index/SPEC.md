# Index of the first maximum

Implement export function argmaxIndex(values) in argmax_index.mjs, Node 22
standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive number; boxed
Number objects (also subclasses), strings, bigints and all other values raise
exact TypeError. Validate ALL types before numeric checks, so [1.5,'x'] raises
TypeError. Then every element must be a safe integer (Number.isSafeInteger),
otherwise exact RangeError (NaN, infinities, fractions, unsafe integers).
Finally an empty array raises exact RangeError.

Return the index (a primitive number) of the FIRST occurrence of the largest
value. -0 and 0 are equal values, so the earlier one wins.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([5]) -> 0`
- `([1, 3, 2]) -> 1`
- `([3, 1, 3]) -> 0`
- `([-5, -2, -9]) -> 1`
- `([0, 0, 0]) -> 0`
- `([1, 2, 3, 4]) -> 3`
- `([9007199254740991, -9007199254740991]) -> 0`
- `([-9007199254740991, -9007199254740991]) -> 0`
- `([-0,0]) -> 0`
- `([0,-0]) -> 0`
- `([]) -> RangeError`
- `(['1']) -> TypeError`
- `([new Number(1)]) -> TypeError`
- `(Array(1)) -> TypeError`
- `([1.5]) -> RangeError`
- `([NaN]) -> RangeError`
- `([2**53]) -> RangeError`
- `([1.5,'x']) -> TypeError`
- `(new Proxy([1],{})) -> TypeError`

Only edit argmax_index.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/argmax-index/check.mjs --solution "$PWD/tasks/argmax-index/argmax_index.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
