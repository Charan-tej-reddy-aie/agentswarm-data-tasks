"""Offline exact synthetic deadline strings, using fixed aware datetime inputs."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument('--solution', type=Path, default=HERE / 'deadline_parser.py')
source = p.parse_args().solution.resolve()
assert source.is_file(), 'missing implementation'
fixture = json.loads((HERE / 'fixtures/cases.json').read_text())
rows = [dict(row, now=fixture['now']) for row in fixture['cases']] + fixture['calendar_probes']
proc = subprocess.run([sys.executable, '-I', str(HERE / 'worker.py'), str(source)],
    input=json.dumps([{'text': row['text'], 'now': row['now']} for row in rows]), capture_output=True, text=True, timeout=10)
assert proc.returncode == 0, proc.stderr[-2000:]
actual = json.loads(proc.stdout)
assert type(actual) is list and len(actual) == len(rows), 'wrong result count'
for value, row in zip(actual, rows):
    assert value == row['expected'] and type(value) is type(row['expected']), (row, value)
print(f'PASS deadline-parser: {len(fixture["cases"])} exact cases at fixed now + {len(fixture["calendar_probes"])} fixed calendar probes')
