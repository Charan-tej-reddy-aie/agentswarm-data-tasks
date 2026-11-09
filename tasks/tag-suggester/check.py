"""Exact contracts and public synthetic held-out precision; stdlib, offline."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('--solution',type=Path,default=HERE/'tag_suggester.py')
source=p.parse_args().solution.resolve()
assert source.is_file(), 'missing implementation'
cases=json.loads((HERE/'fixtures/cases.json').read_text())
train=json.loads((HERE/'fixtures/train.json').read_text())
heldout=json.loads((HERE/'fixtures/heldout.json').read_text())
assert not ({doc for docs in train.values() for doc in docs} & {row['title']+' '+row['body'] for row in heldout}), 'split leak'
rows=[{key:value for key,value in row.items() if key not in ('expected','name')} for row in cases]
rows += [dict(title=row['title'],body=row['body'],vocab=train) for row in heldout]
original=len(rows)
rows += [dict(row,vocab=dict(reversed(list(row['vocab'].items())))) for row in rows]
proc=subprocess.run([sys.executable,'-I',str(HERE/'worker.py'),str(source)],input=json.dumps(rows),capture_output=True,text=True,timeout=15)
assert proc.returncode==0,proc.stderr[-2000:]
actual=json.loads(proc.stdout)
assert type(actual) is list and len(actual)==len(rows), 'wrong count'
assert actual[original:]==actual[:original], 'vocabulary insertion order changed result'
for row,result in zip(cases,actual):
    assert result==row['expected'], (row['name'],result,row['expected'])
hits=sum(len(set(result)&set(row['relevant'])) for row,result in zip(heldout,actual[len(cases):original]))
precision=hits/(3*len(heldout))
assert precision>=.90, f'precision@3 {precision:.3f} below .90'
print(f'PASS tag-suggester: {len(cases)} exact cases; {len(heldout)} held-out cases precision@3={precision:.3f}; nonmutation and reversed-vocab probes')
