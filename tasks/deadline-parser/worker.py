"""Isolated module import and exact return type boundary; not a sandbox."""
from datetime import datetime
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('submission', sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
results = []
for row in json.load(sys.stdin):
    value = module.parse_deadline(row['text'], datetime.fromisoformat(row['now'].replace('Z', '+00:00')))
    assert value is None or type(value) is str, 'must return str or None'
    results.append(value)
print(json.dumps(results))
