"""Isolated callable evaluation; receives no expected labels; not a sandbox."""
import copy
import json
import runpy
import sys
sys.dont_write_bytecode = True
suggest = runpy.run_path(sys.argv[1], run_name='candidate')['suggest_tags']
results=[]
for row in json.load(sys.stdin):
    before=copy.deepcopy(row)
    args=[row['title'],row['body'],row['vocab']]
    if 'k' in row:
        args.append(row['k'])
    result=suggest(*args)
    assert row == before, 'inputs mutated'
    assert type(result) is list and all(type(tag) is str and tag in row['vocab'] for tag in result), 'return vocabulary strings'
    assert len(set(result)) == len(result) and len(result)<=row.get('k',3), 'duplicates or too many tags'
    results.append(result)
print(json.dumps(results))
