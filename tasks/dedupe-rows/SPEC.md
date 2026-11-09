# Deduplicate string rows by a key column
Implement export function dedupeRows(rows, keyIndex) in dedupe_rows.mjs.
rows must be a dense normal Array of dense normal Arrays of primitive strings.
Normal means prototype exactly Array.prototype; reject all array subclasses,
altered prototypes, Proxies (including nested/revoked), holes, boxed strings and
other shapes/types with exact TypeError. keyIndex must be a primitive number.
Validate ALL shapes and types before bounds. Then keyIndex must be a nonnegative
safe integer and every row must have an element at that index; otherwise exact
RangeError. Empty rows input accepts any nonnegative safe keyIndex.
Keep the FIRST row for each distinct key string, in original order. Compare keys
by exact JS string equality: no trimming, case folding or normalization; empty
keys and lone surrogates are valid opaque strings. Return a fresh normal dense
Array of fresh normal dense row copies. Preserve every column, including ragged
rows and duplicates outside the key column. Never mutate or retain input.
Examples: ([],0) -> []; ([['a','1'],['b','2'],['a','3']],0) ->
[['a','1'],['b','2']]; ([['x','a'],['y','a'],['z','b']],1) ->
[['x','a'],['z','b']]; ([[''],['']],0) -> [['']]; ([[]],0) -> RangeError;
([], -1) -> RangeError; ([['x',1]],0) -> TypeError.

Use standard library only. Inputs use ordinary data properties, no accessors or
shadowed Array methods/iterators; extra named Array properties are outside the
contract. Frozen inputs are supported in JS. Exception messages are unconstrained.
Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Every spec example is checked. No README-dependent checks. Public checks need
independent source/scope review. This is a standalone unpaid exercise.

Runtime: Node 22. Quick run from repository root:
`node tasks/dedupe-rows/check.mjs --solution "$PWD/tasks/dedupe-rows/dedupe_rows.mjs"`
The issue provides a separate trusted checker pin and offline Docker command.
