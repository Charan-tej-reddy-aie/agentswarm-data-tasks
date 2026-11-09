# Bucket marketplace deadlines by urgency
Implement deadline_buckets(deadlines, now) in deadline_buckets.py, Python 3.11+.
Require deadlines to be an exact built-in list of exact built-in ints, and now
an exact built-in int. Reject every other type, bool, and all subclasses
(including list and int subclasses) with exact TypeError. Negative timestamps
and arbitrary precision integers are allowed. Treat timestamps as integer
minutes in one caller-chosen epoch; never consult the clock or parse dates.
Return a fresh exact list of exact strings, in input order, keeping duplicates:
'expired' when deadline<=now; 'soon' when now<deadline<=now+60; 'later' otherwise.
No input mutation, shared mutable result state, normalization or tokenization.
Examples: ([],0) -> []; ([9,10,11,70,71],10) ->
['expired','expired','soon','soon','later']; ([-2,-1,60],-1) ->
['expired','expired','later']; ([1,1],0) -> ['soon','soon'];
([True],0), ((1,),0) and ([1],False) -> TypeError.

Only edit the implementation file and optional IMPLEMENTATION.md in this task.
Exception messages are unconstrained. Every spec example is checked. No files,
network, packages or README-dependent functional checks. This standalone unpaid
exercise makes no production-use claim; public checks need source/scope review.
