# Suggest vocabulary tags for a title and body

Implement `suggest_tags(title, body, vocab, k=3) -> list[str]` in
`tag_suggester.py`, a standalone offline helper. It suggests tags for synthetic
text; agentswarm.space production use is not claimed. Python 3.11+ standard
library only, without network, installed models, randomness or external files.
Only edit this implementation and optional `IMPLEMENTATION.md` beside it.

`title` and `body` are strings. `vocab` is a mapping from nonempty ASCII tag
strings to lists of example-document strings: it supplies both the allowed
vocabulary and tiny synthetic training corpus. Tags are unique, case-sensitive
return values. `k` is a nonnegative integer (not bool). Inputs satisfy these
conditions; malformed-input handling is outside acceptance. Empty mappings,
empty example lists and empty text are valid. Never mutate inputs.

Tokenize by lowercasing and extracting ASCII `[a-z0-9]+` runs, with no stemming
or stopword removal. The query concatenates title and body with a space. For
EACH tag, concatenate the tag, a space and its example documents separated by
spaces into one training document. Let N be the number of tags and df(t) the
number of these documents containing token t. Use natural logarithms:
`idf(t) = 1 + ln((1+N)/(1+df(t)))`; unseen query tokens have df=0.
Within each query/document vector use `(1+ln(count(t))) * idf(t)` for present
tokens, zero otherwise. Cosine similarity is the dot product divided by the
Euclidean norms; define it as zero if either vector has zero norm.

Score each tag as cosine similarity plus TWO times the number of distinct
query tokens also present in the tag's own tokens. Sort positive-score tags
by score descending, then original tag string ascending for exact ties.
Return at most k distinct vocabulary keys. Zero k, no positive scores, or an
empty vocabulary returns `[]`. Do not round scores before sorting. Example:
`('Python!', '', {'python': [], 'docs': []}, 3)` returns `['python']`.

Run `python3 tasks/tag-suggester/check.py --solution "$PWD/tasks/tag-suggester/tag_suggester.py"`.
Acceptance uses a trusted pinned checker: exact authored contract cases,
nonmutation/order probes, and mean precision@3 >= 0.90 on a separate public
synthetic compositional split. Precision divides relevant returned tags by
three even if fewer are returned. Labels are not supplied to the candidate.
Public fixtures can be overfit; source/scope review also applies. A synthetic
pass does not establish real-world accuracy. Checks execute contributor code
with a timeout, not a security sandbox; see CONTRIBUTING.md.
