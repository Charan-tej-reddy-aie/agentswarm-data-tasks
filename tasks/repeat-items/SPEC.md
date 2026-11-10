# Repeat each string a bounded number of times

Implement export function repeatItems(values, times) in repeat_items.mjs, Node
22 standard library only.

values must be a dense normal Array: prototype exactly Array.prototype, not a
Proxy (use types.isProxy from node:util; this includes revoked proxies), and
every index an own property. Reject subclasses, altered prototypes, nonarrays
and holes with exact TypeError. Every element must be a primitive string; boxed
String objects (also subclasses) and all other values raise exact TypeError.
times must be a primitive number (boxed Number objects raise exact TypeError).
Validate values and the type of times before the range of times, so ([1],11)
raises TypeError. Then times must be a safe integer in [0,10] (-0 counts as 0),
otherwise exact RangeError.

Return a fresh normal Array in which each element of values appears times
times IN A ROW, in input order: (['a','b'],2) -> ['a','a','b','b'] (not
['a','b','a','b']). Strings are opaque: no trimming, normalization or case
folding; empty strings and lone surrogates are ordinary values.

Error messages are unconstrained. Never change input values or properties;
frozen arrays are supported. Ignore extra named array properties and never call
user-shadowed array methods or the input's iterator (use index loops). Index
properties are ordinary data properties. Independent calls return independent
results.

Examples (arguments -> result); every one is checked:
- `([], 3) -> []`
- `(['a', 'b'], 2) -> ['a', 'a', 'b', 'b']`
- `(['a'], 0) -> []`
- `(['x', 'y'], 1) -> ['x', 'y']`
- `(['a', 'a'], 2) -> ['a', 'a', 'a', 'a']`
- `(['', ' '], 2) -> ['', '', ' ', ' ']`
- `(['\u00e9'], 3) -> ['\u00e9', '\u00e9', '\u00e9']`
- `(['b', 'a'], 10) -> ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']`
- `(['a'],-0) -> []`
- `(['\ud800'],2) -> ['\ud800','\ud800']`
- `(['a'],11) -> RangeError`
- `(['a'],-1) -> RangeError`
- `(['a'],1.5) -> RangeError`
- `(['a'],'2') -> TypeError`
- `([1],2) -> TypeError`
- `([1],11) -> TypeError`
- `(Array(1),1) -> TypeError`
- `(['a'],new Number(1)) -> TypeError`
- `(new Proxy(['a'],{}),1) -> TypeError`

Only edit repeat_items.mjs and optional IMPLEMENTATION.md in this task directory.
Quick run from the repository root (Node 22):
`node tasks/repeat-items/check.mjs --solution "$PWD/tasks/repeat-items/repeat_items.mjs"`
The issue supplies a separate trusted checker pin and offline Docker command.
A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
