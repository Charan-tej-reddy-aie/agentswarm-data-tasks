import argparse,json,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution.resolve()
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
for index,row in enumerate(cases):
    for repeat in range(2):
        proc=subprocess.run([sys.executable,'-I','-B',str(source),*row['args']],capture_output=True,timeout=3)
        assert proc.returncode==row['exit'],(index,proc.returncode,proc.stderr)
        assert proc.stdout==row['stdout'].encode('utf-8'),(index,proc.stdout)
        assert bool(proc.stderr)==bool(row['exit']),(index,proc.stderr)
help_run=subprocess.run([sys.executable,'-I','-B',str(source),'--help'],capture_output=True,timeout=3)
assert help_run.returncode==0 and b'usage:' in help_run.stdout and not help_run.stderr
print(f'PASS ledger-cli: {len(cases)} subprocess cases repeated plus argparse help')
