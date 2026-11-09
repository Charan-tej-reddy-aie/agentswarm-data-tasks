# Translate README into French

Add `README.fr.md` at the repository root, translating the complete pinned English
README into French. This helps contributors read the project's task and credit
instructions. Do not add navigation or edit English: `README.md` must remain
byte-identical to `fixtures/README.en.md` in this task (SHA-256
`d37de9a07044dfc2cb62f909f9dffc200f7d2be6d9866cd92e1d30a007a96f53`). The baseline is byte-identical to main at 0e04b570 (including the contributors section); batch 5 does not edit the English README.
Only add the root translation; optional notes may go in
`tasks/readme-fr/IMPLEMENTATION.md`. The TODO template in this directory is not
a root translation and intentionally fails acceptance.

Preserve every link target in its original block (translate link labels), all
fenced code byte-for-byte, inline code snippets, heading count/levels/order and
paragraph/list/table-row order. Preserve every paragraph and caveat; do not add
or omit blocks. Paragraph line wrapping may change. Keep the project name and
technical identifiers unchanged. No raw HTML, comments, reference-style links
or newly added links. No indented code/prose outside fenced blocks; preserve
table delimiter rows, outer pipes, column counts and contiguous table rows. Use
the same simple Markdown forms as the baseline.

The offline Python 3.11+ stdlib check, modeled on agentswarm-examples'
readme-translation check, verifies structure, exact English, links, code,
coverage and lightweight language plausibility. It rejects copied English and
obvious filler. It cannot establish translation accuracy: meaning, naturalness,
and complete coverage are reviewed by a human or LLM reviewer before merge.
Unpaid/credit terms, AI disclosure, registration optionality and check limitations
must retain their meaning. A structural pass alone does not guarantee acceptance.
No installs or network needed; fixtures contain only project-authored English
and an authored synthetic Markdown sample, never member data.

Quick check from repo root: `python3 tasks/readme-fr/check.py --solution "$PWD"`.
Acceptance uses a separate trusted pinned checker with `--solution` pointing to
the candidate repository root. The candidate's English README is checked too.
