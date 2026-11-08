# Short task-title language identification

Implement `detect(text: str) -> str` in `lang_id.py` for en, es, pt, zh, ja, ko,
de and fr. Return an ISO 639-1 code (zh, not zh-CN). This small feed component
can suggest a title language; it does not establish production accuracy.

Use a character n-gram model learned only from `fixtures/train.json` (384 authored
synthetic rows, 48 per language). Any n-gram lengths/weighting/scoring method is
allowed; a count-based cosine or multinomial model is enough. Train lazily once
per process if desired. Python 3.11+ stdlib only, no external corpus, pretrained
model, word/sentence lookup table, hardcoded script routing, network or subprocess.
The training path is `os.environ["LANG_ID_TRAIN"]` during acceptance; for local
development default to `Path(__file__).with_name("fixtures") / "train.json"`.
This is the only input file the implementation may read. The checker provides
the same training rows in a shuffled temporary file as an additional probe.
Do not read heldout/check files, labels, or infer a label from order or IDs.
Source review verifies that predictions actually use the learned character model.

Normalize Unicode with NFKC and casefold, collapse whitespace, and ignore added
edge punctuation `!?.`. Classification must be invariant to these transformations.
Empty/whitespace-only titles return `en` by convention; unrecognizable titles may
return any supported code. Mixed-language titles are outside acceptance scope.

Acceptance: accuracy >= 0.90 over the public held-out synthetic split (128 rows,
16 per language), >= 0.80 for each language, exact invariance on that split and
empty-title probes, and unchanged results after training-row permutation. A label-renaming probe
requires predictions to follow renamed training labels (empty input stays en),
so a detector cannot substitute script rules or a fixed answer table. Train
and heldout have disjoint title strings; heldout recombines the synthetic training
vocabulary into unseen titles. This measures a small compositional baseline,
not general language identification. Public fixtures can be overfit: source and
scope review accompany the score. Do not tune against heldout labels.

Only edit `tasks/lang-id/lang_id.py` plus optional `IMPLEMENTATION.md`.
Quick check: `python3 tasks/lang-id/check.py`.
