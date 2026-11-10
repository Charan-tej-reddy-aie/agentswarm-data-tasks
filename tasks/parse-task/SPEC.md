# Parse and validate a task payload

Implement parse_task(text) in parse_task.py, Python 3.11+ standard library only.
Only edit that file and optional IMPLEMENTATION.md. text must have exact built-in
str type; reject subclasses and all other objects with exact TypeError. Parse
one JSON document using Python json syntax; leading/trailing JSON whitespace is
allowed. Reject malformed JSON, trailing documents, duplicate object keys at any
level, and NaN/Infinity/-Infinity with exact ValueError. All schema violations
also raise exact ValueError; exception messages are unconstrained.

The root must be an object with exactly three required keys: id, title, budget.
id must be a string fully matching ASCII [a-z][a-z0-9-]{0,31}; title must be a
string of 1..80 Python Unicode code points with at least one non-whitespace
character according to str.strip(); budget must be an exact int >=0 (booleans
and JSON floats such as 1.0 are invalid). No other fields or coercions. Preserve
all values exactly, including title whitespace and Unicode; no trimming,
normalization or tokenization. Return a fresh exact dict of the parsed values;
key order is unconstrained. Independent repeated calls must not share mutable
results. Input string is unchanged. Budget has Python arbitrary precision,
subject to the standard json parser's limits. No files, network or packages.

Examples:
{"id":"task-1","title":" Ship it ","budget":0} -> that exact object;
 {"budget":12,"title":"é","id":"a"} -> that exact object;
{"id":"A","title":"x","budget":0} -> ValueError;
{"id":"a","title":" ","budget":0} -> ValueError;
{"id":"a","title":"x","budget":true} -> ValueError;
{"id":"a","title":"x","budget":1.0} -> ValueError;
{"id":"a","title":"x","budget":0,"extra":1} -> ValueError;
{"id":"a","id":"b","title":"x","budget":0} -> ValueError;
[] and malformed text '{' -> ValueError; non-string None -> TypeError.
Every example is checked. README is not a functional input. Offline public
fixtures require source/scope review and do not establish production use.
