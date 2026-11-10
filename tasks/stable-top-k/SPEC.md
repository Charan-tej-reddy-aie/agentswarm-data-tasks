# stable-top-k
Implement `stable_top_k` in `stable_top_k.py`. Python 3.11+ standard library only.

Fix the seeded implementation. Require an exact built-in list of at most 1000 exact built-in ints in [-1000000000,1000000000]. k must be an exact built-in int in [0,len(scores)]. Return a fresh exact built-in list of the first k INDICES ranked by descending score, with equal scores ranked by ascending original index. Output indices must be exact built-in ints. k=0 returns []; empty scores accepts only k=0. Do not return score values or sort/mutate input.

Reject bool and ALL subclasses of the required builtins, including nested values, with exact TypeError. Reject other wrong types with exact TypeError. Validate every type before bounds/grammar/shape lengths; those violations raise exact ValueError. Exception messages are unconstrained. No input mutation, retained mutable state, I/O or dependencies. Inputs are ordinary finite builtin data; processing is bounded by the limits above.

Examples (argument lists -> result):
- `[[], 0]` -> `[]`
- `[[5, 5, 9, 5], 3]` -> `[2, 0, 1]`
- `[[1, 3, 2], 0]` -> `[]`
- `[[-3, -1, -1], 3]` -> `[1, 2, 0]`
- `[[0, 0, 0], 2]` -> `[0, 1]`
- `[[1000000000, -1000000000], 2]` -> `[0, 1]`
- `[[4, 2, 3], 1]` -> `[0]`

Only edit `stable_top_k.py` and optional IMPLEMENTATION.md in this task directory.
Run `python3 tasks/stable-top-k/check.py --solution "$PWD/tasks/stable-top-k/stable_top_k.py"`. The issue supplies the trusted pin and offline Docker instructions. Checker completion is CHECK_PASS_UNVERIFIED until independent source/scope review; public checks cannot prove arbitrary candidate behavior.
