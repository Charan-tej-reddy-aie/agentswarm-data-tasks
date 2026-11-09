# Deduplicate task tags in first-seen order

Implement unique_tags(values) in unique_tags.py, Python 3.11+ standard library.
Only edit that file and optional IMPLEMENTATION.md. Require an exact built-in
list containing exact built-in strings; reject list and str subclasses, tuples,
numbers, bool, None and every other type with exact TypeError. Exception messages
are unconstrained. Validate every element, including duplicates, before returning.

Return a fresh exact built-in list of exact strings containing each distinct
input string once, in order of first appearance. Preserve opaque string values
exactly: no splitting, trimming, sorting, Unicode normalization or case folding.
Empty strings, spaces, NUL and combining marks are valid. Do not mutate input.
Repeated calls return independent lists, including for empty and unique inputs;
mutating a returned list must not affect later results. No retained mutable state.
Examples: [] -> []; ['a','b','a'] -> ['a','b']; ['',' ',''] -> ['',' '];
['A','a','A'] -> ['A','a']; ['é','é','é'] -> ['é','é'];
('a',) and ['a',1] raise TypeError. Every example is checked.
No dependencies, files, network, clock or production integration; no README
contents participate. Public offline checks require source/scope review.
