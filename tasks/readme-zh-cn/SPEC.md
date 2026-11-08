# Translate README into Simplified Chinese

Add `README.zh-CN.md` at the repository root, translating the complete pinned English
README into Simplified Chinese. This helps contributors read the project's task and credit
instructions. Do not add navigation or edit English: `README.md` must remain
byte-identical to `fixtures/README.en.md` in this task (SHA-256
`e7cf4c790d1629a717f4824f2262530ac2363e62d2f94c8b5d9f203baef1c829`). The baseline includes all seven batch-1/batch-2 task rows.
Only add the root translation; optional notes may go in
`tasks/readme-zh-cn/IMPLEMENTATION.md`. The TODO template in this directory is not
a root translation and intentionally fails acceptance.

Preserve every link target in its original block (translate link labels), all
fenced code byte-for-byte, inline code snippets, heading count/levels/order and
paragraph/list/table-row order. Preserve every paragraph and caveat; do not add
or omit blocks. Paragraph line wrapping may change. Keep the project name and
technical identifiers unchanged. No raw HTML, comments, reference-style links
or newly added links. No indented code/prose outside fenced blocks; preserve
table delimiter rows and column counts. Use the same simple Markdown forms as
the baseline.

The offline Python 3.11+ stdlib check, modeled on agentswarm-examples'
readme-translation check, verifies structure, exact English, links, code,
coverage and lightweight language plausibility. It rejects copied English and
obvious filler. It cannot establish translation accuracy: meaning, naturalness,
and complete coverage are reviewed by a human or LLM reviewer before merge.
Unpaid/credit terms, AI disclosure, registration optionality and check limitations
must retain their meaning. A structural pass alone does not guarantee acceptance.
No installs or network needed; fixtures contain only project-authored English
and an authored synthetic Markdown sample, never member data.

Quick check from repo root: `python3 tasks/readme-zh-cn/check.py --solution "$PWD"`.
Acceptance uses a separate trusted pinned checker with `--solution` pointing to
the candidate repository root. The candidate's English README is checked too.
