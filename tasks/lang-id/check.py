"""Offline character-model benchmark with a public synthetic compositional split."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unicodedata
HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--solution", type=Path, default=HERE / "lang_id.py")
source = p.parse_args().solution.resolve()
assert source.is_file(), "missing implementation"
train = json.loads((HERE / "fixtures/train.json").read_text())
heldout = json.loads((HERE / "fixtures/heldout.json").read_text())
assert not ({r["text"] for r in train} & {r["text"] for r in heldout}), "split leak"
texts = [row["text"] for row in heldout]
# Every evaluated title must retain its prediction across normalized variants.
inputs = list(texts)
for transform in (str.upper, lambda s: "  "+" \n\t ".join(s.split())+"  ",
                  lambda s: "!!!"+s+"???", lambda s: unicodedata.normalize("NFD", s)):
    inputs.extend(transform(s) for s in texts)
inputs.extend(["", " \t\n "])
def predict(training):
    environment = dict(os.environ, LANG_ID_TRAIN=str(training))
    proc = subprocess.run([sys.executable, "-I", str(HERE / "worker.py"), str(source)],
        input=json.dumps(inputs), capture_output=True, text=True, timeout=20, env=environment)
    assert proc.returncode == 0, proc.stderr[-2000:]
    result = json.loads(proc.stdout)
    assert type(result) is list and len(result) == len(inputs), "wrong result count"
    return result
result = predict(HERE / "fixtures/train.json")
size = len(texts)
correct = sum(pred == row["language"] for pred, row in zip(result[:size], heldout))
assert correct / size >= .9, f"accuracy {correct}/{size} below .90"
scores = {}
for lang, total in Counter(r["language"] for r in heldout).items():
    hit = sum(pred == lang for pred, row in zip(result[:size], heldout) if row["language"] == lang)
    assert hit / total >= .8, f"{lang}: {hit}/{total} below .80"
    scores[lang] = f"{hit}/{total}"
for index in range(1, 5):
    assert result[index*size:(index+1)*size] == result[:size], f"invariance {index} failed"
assert result[-2:] == ["en", "en"], "empty titles must return en"
random.Random(146605).shuffle(train)
with tempfile.TemporaryDirectory(prefix="lang-id-training-") as directory:
    shuffled = Path(directory) / "training.json"
    shuffled.write_text(json.dumps(train, ensure_ascii=False), encoding="utf-8")
    assert predict(shuffled) == result, "training order/path affected predictions"
    languages = sorted({r["language"] for r in train})
    renamed = dict(zip(languages, languages[1:]+languages[:1]))
    shuffled.write_text(json.dumps([dict(row, language=renamed[row["language"]]) for row in train], ensure_ascii=False), encoding="utf-8")
    assert predict(shuffled) == [renamed[code] for code in result[:-2]]+["en", "en"], "predictions must follow training labels"
print(f"PASS lang-id: accuracy={correct/size:.3f}; {scores}; 4 invariances/title, empty, shuffled training and label renaming")
