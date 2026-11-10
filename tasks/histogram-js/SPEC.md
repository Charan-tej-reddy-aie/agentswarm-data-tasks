# Count values in exact histogram bins
Implement export function histogram(values, edges) in histogram.mjs.
Require two dense normal Arrays (prototype exactly Array.prototype) of primitive
numbers. Reject all subclasses, altered prototypes, Proxies (including revoked),
holes, boxed numbers and wrong shapes/types with exact TypeError. Fractions,
NaN and infinities raise exact RangeError; accept -0 as zero.
Validate all shapes/types before numeric bounds. Then every integer must be in
[-9007199254740991,9007199254740991], edges must contain at least TWO integers,
and edges must be strictly increasing; otherwise exact RangeError.
Return a fresh normal dense Array of primitive numbers of len(edges)-1 counts. Bin i contains values with
edges[i] <= x < edges[i+1], EXCEPT the final bin also includes its upper edge.
Ignore values below the first or above the last edge; retain duplicates. Counts
are exact nonnegative integers (positive zero in JS). No input mutation,
retained mutable state, sorting, coercion or tokenization.
Examples: ([],[0,10]) -> [0]; ([-1,0,9,10,19,20,21],[0,10,20]) -> [2,3];
([0,0,1,2],[0,1,2]) -> [2,2]; ([5,5],[5,6]) -> [2];
([-3,-2,-1,0],[-3,-1,0]) -> [2,2]; ([0],[]) and ([0],[1,1]) -> RangeError;
([True],[0,1]) -> TypeError (JS uses true); ([1.5],[0,2]) -> RangeError.

Use standard library only. Inputs use ordinary data properties, no accessors or
shadowed Array methods/iterators; extra named Array properties are outside the
contract. Frozen inputs are supported in JS. Exception messages are unconstrained.
Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Every spec example is checked. No README-dependent checks. Public checks need
independent source/scope review. This is a standalone unpaid exercise.

Runtime: Node 22. Quick run from repository root:
`node tasks/histogram-js/check.mjs --solution "$PWD/tasks/histogram-js/histogram.mjs"`
The issue provides a separate trusted checker pin and offline Docker command.
Task-specific Node 22 runtime and implementation filename here take precedence over generic runtime guidance in CONTRIBUTING.md.
