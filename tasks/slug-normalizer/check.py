"""Trusted offline authored contracts; expected values never enter the worker."""
import argparse,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,default=HERE/'slug_normalizer.py')
source=p.parse_args().solution.resolve()
cases=json.loads((HERE/'fixtures/cases.json').read_text())
rows=[{k:v for k,v in row.items() if k not in ('expected','error')} for row in cases]
proc=subprocess.run([sys.executable,'-I',str(HERE/'worker.py'),str(source)],input=json.dumps(rows),capture_output=True,text=True,timeout=10)
assert proc.returncode==0,proc.stderr[-2000:]
actual=json.loads(proc.stdout)
expected=[{k:v for k,v in row.items() if k in ('expected','error')} for row in cases]
assert len(actual)==len(expected),'result count'
for index,(result,want) in enumerate(zip(actual,expected)):
    assert result==want,(index,result,want)
print(f'PASS slug-normalizer: {len(cases)} exact cases and deterministic repeat probes')
