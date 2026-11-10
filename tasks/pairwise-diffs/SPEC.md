# pairwise-diffs
Implement `pairwise_diffs` in `pairwise_diffs.py`. Python 3.11+ standard library only.

Require an exact built-in list of at most 1000 exact built-in ints, each in [-1000000000,1000000000]. Return a fresh exact built-in list of len(values)-1 differences where element i is values[i+1]-values[i] (later minus earlier, sign kept). Empty and one-element inputs return a fresh []. Do not sort, take absolute values or wrap around.

Reject bool and ALL subclasses of required builtins (including nested values) with exact TypeError. Reject other wrong types with exact TypeError. Validate ALL types before lengths/ranges, which raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies.

Examples (argument lists -> result):
- `[[]]` -> `[]`
- `[[5]]` -> `[]`
- `[[1, 4, 9]]` -> `[3, 5]`
- `[[3, 1]]` -> `[-2]`
- `[[2, 2, 2]]` -> `[0, 0]`
- `[[0, -5, 5]]` -> `[-5, 10]`
- `[[-1000000000, 1000000000]]` -> `[2000000000]`
- `[[1000000000, -1000000000]]` -> `[-2000000000]`
- `[[True]]` -> `raises TypeError`
- `[[1000000001]]` -> `raises ValueError`

Only edit `pairwise_diffs.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/pairwise-diffs/check.py --solution "$PWD/tasks/pairwise-diffs/pairwise_diffs.py"`. The issue supplies the trusted checker pin. A pass remains CHECK_PASS_UNVERIFIED until independent source/scope review.
