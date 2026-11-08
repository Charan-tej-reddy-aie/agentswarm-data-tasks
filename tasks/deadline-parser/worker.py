"""Isolated module import and exact return type boundary; not a sandbox."""
from datetime import datetime
import runpy
import json
import sys
sys.dont_write_bytecode = True
parse_deadline = runpy.run_path(sys.argv[1], run_name='candidate')['parse_deadline']
results = []
for row in json.load(sys.stdin):
    value = parse_deadline(row['text'], datetime.fromisoformat(row['now'].replace('Z', '+00:00')))
    assert value is None or type(value) is str, 'must return str or None'
    results.append(value)
print(json.dumps(results))
