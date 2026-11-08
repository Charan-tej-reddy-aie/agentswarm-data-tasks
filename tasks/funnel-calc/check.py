"""Offline exact typed CLI checks; synthetic fixtures, no network or packages."""
import argparse
import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument('--solution', type=Path, default=HERE / 'funnel.py')
source = p.parse_args().solution.resolve()
assert source.is_file(), 'missing implementation'
cases = json.loads((HERE / 'fixtures/cases.json').read_text())
checks = 0
with tempfile.TemporaryDirectory(prefix='funnel-check-') as tmp:
    root = Path(tmp)
    for case in cases:
        for ordering, rows in [('original', case['rows']), ('reversed', list(reversed(case['rows']))), ('duplicated', case['rows'] * 2)]:
            events = root / 'events.csv'
            with events.open('w', newline='', encoding='utf-8') as stream:
                writer = csv.writer(stream)
                writer.writerow(['ts', 'channel', 'actor', 'event'])
                writer.writerows(rows)
            actors = root / 'actors.txt'
            actors.write_text('\n'.join(case['internal']) + '\n', encoding='utf-8')
            command = [sys.executable, '-I', str(source), str(events)]
            if case['option']:
                command += ['--internal-actors', str(actors)]
            proc = subprocess.run(command, text=True, capture_output=True, timeout=5, cwd=root)
            assert proc.returncode == 0, (case['name'], ordering, proc.stderr[-1000:])
            actual = json.loads(proc.stdout)
            assert type(actual) is list, 'output must be a JSON array'
            for item in actual:
                assert type(item) is dict and set(item) == {'day','channel','acquisition','activation','retention','referral','revenue'}, 'exact keys required'
                assert type(item['day']) is str and type(item['channel']) is str
                assert all(type(item[name]) is int and item[name] >= 0 for name in ['acquisition','activation','retention','referral','revenue']), 'counts must be nonnegative integers'
            assert actual == case['expected'], (case['name'], ordering, actual, case['expected'])
            checks += 1
print(f'PASS funnel-calc: {len(cases)} authored datasets; {checks} exact runs including reversal and duplication')
