# chunk_ranges returns an oversized final range for a partial chunk

Fix `chunk_ranges(length, size)` in chunk_ranges.py, Python 3.11+ standard
library only. The supplied module has three seeded bugs affecting type checks,
empty input and the last endpoint. Only edit chunk_ranges.py and optional
IMPLEMENTATION.md in this task. No packages, file I/O, network, clock, README
checks or production integration. The task checker and fixtures are immutable.

Both arguments must have exact built-in int type (`type(x) is int`), rejecting
bool and int subclasses too. Floats, strings, None and containers raise
TypeError. Validate ALL types before numeric bounds, so (-1, False) raises
TypeError. For exact integers, length must be nonnegative and size positive;
otherwise raise ValueError. Exception messages are unconstrained. The fixture
sizes are modest; no artificial maximum is part of this API.

Return a fresh exact built-in list of exact two-item built-in tuples, whose
items are exact built-in ints. Each tuple is a half-open [start,end) interval.
Starts are 0, size, 2*size, ... strictly below length. End is the smaller of
start+size and length. In particular the final range never exceeds length.
Length zero returns an empty list for every valid positive size. If size
exceeds a positive length, return one tuple (0,length). Preserve order and
never return overlapping ranges, empty intervals, or inclusive end coordinates.

Examples: (10,4) -> [(0,4),(4,8),(8,10)]; (8,4) -> [(0,4),(4,8)];
(0,4) -> []; (3,8) -> [(0,3)]; (1,1) -> [(0,1)].
(-1,2) and (3,0) raise ValueError. (True,2), (3,1.0), and (-1,False)
raise TypeError. The list must be newly allocated on each call so modifying
one result cannot affect another; tuple elements are immutable. Do not retain
inputs or mutable global state. Calls are deterministic and never mutate
caller-owned values. Public synthetic fixtures exercise every example and the
complete type/boundary contract; source/scope review accompanies acceptance.
