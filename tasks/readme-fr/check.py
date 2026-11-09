"""Offline structural acceptance; translation meaning needs human/LLM review."""
import argparse
import hashlib
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from translation_check import check_translation, parse, link_targets
HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--solution", type=Path, default=HERE.parents[1], help="candidate repository root")
repo = p.parse_args().solution.resolve()
baseline = (HERE / "fixtures/README.en.md").read_bytes()
assert hashlib.sha256(baseline).hexdigest() == "d37de9a07044dfc2cb62f909f9dffc200f7d2be6d9866cd92e1d30a007a96f53", "pinned English baseline changed"
# Synthetic parser fixture exercises forms beyond the current real README.
sample = (HERE / "fixtures/structure-sample.md").read_text()
headings, fences, blocks = parse(sample)
assert headings == [1, 2] and len(fences) == 1
assert [kind for kind, _ in blocks] == ["heading", "paragraph", "heading", "fence", "table", "table-separator", "table", "list", "quote"]
assert link_targets(sample) == {"https://example.invalid/guide"}
check_translation(repo, {"translation": "README.fr.md", "language": "fr"}, baseline)
print("PASS readme-fr: exact English baseline, ordered blocks/headings, links and code, language plausibility; meaning requires human/LLM review")
