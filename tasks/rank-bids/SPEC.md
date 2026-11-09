# Rank marketplace bids with explicit ties
Implement rank_bids(bids) in rank_bids.py, Python 3.11+ standard library only.
Require an exact built-in list of exact built-in dicts, each with exactly the
keys id, bid, score (keys must be exact str). id must be an exact str (opaque, empty allowed); bid and
score must be exact int, excluding bool and subclasses. Validate all record
shapes and field types before bounds; any shape/type violation raises exact
TypeError. Then require bid >=0 and 0<=score<=100, otherwise exact ValueError.
All subclasses, including list, dict, str and int subclasses, are rejected.
Return a fresh exact list of exact string ids, ordered by score descending,
bid ascending, then id by Python Unicode lexicographic order ascending. Keep
duplicates and input order for completely tied rows. No trimming, normalization,
case folding or tokenization; integer arithmetic has arbitrary precision.
Never mutate input. Independent calls return independent lists, including empty.
Examples: [] -> []; [{'id':'b','bid':4,'score':90},
{'id':'a','bid':4,'score':90},{'id':'z','bid':9,'score':100}] -> ['z','a','b'];
[{'id':'x','bid':0,'score':0}] -> ['x'];
[{'id':'x','bid':-1,'score':0}] -> ValueError; [{'id':'x','bid':True,'score':0}]
-> TypeError; [{'id':'x','bid':0,'score':0,'extra':1}] -> TypeError.

Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Exception messages are unconstrained. Every spec example is checked. No files,
network, packages or README-dependent functional checks. This standalone unpaid
exercise makes no production-use claim; public checks need source/scope review.
