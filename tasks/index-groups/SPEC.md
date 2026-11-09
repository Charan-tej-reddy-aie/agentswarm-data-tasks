# Can you group the positions of repeated strings?

Implement group_indices(values) in group_indices.py, Python 3.11+ standard
library only. Only edit that file and optional IMPLEMENTATION.md in this task.
Input must have exact built-in list type; reject list subclasses, tuples and
other objects with TypeError. Every element must have exact built-in str type;
reject str subclasses, numbers, bool, None, containers and boxed/other values
with TypeError. Validate all elements before producing a result. Exception
messages are unconstrained. Strings are opaque exact keys, including empty,
whitespace, punctuation, Unicode, combining marks and NUL. Never split, trim,
normalize or fold case. There is no tokenization step.

Return a fresh exact built-in dict mapping each distinct string to a fresh
exact built-in list of its zero-based positions, each an exact built-in int.
Keys follow first-occurrence insertion order; positions ascend. Empty input
returns {}. Do not mutate input or retain mutable shared state. Calls return
independent structures; modifying a returned dict/list cannot affect later calls.
Examples: [] -> {}; ['a','b','a'] -> {'a':[0,2],'b':[1]};
['',' ',''] -> {'':[0,2],' ':[1]}; ['A','a','A'] -> {'A':[0,2],'a':[1]}.
(1,) and ['a',1] raise TypeError. All examples are checked.
No packages, files, network, clock, README checks or production integration.
Public synthetic checks run offline and require source/scope review.
