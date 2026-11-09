"""Candidate worker; not a security boundary."""
import json, runpy, sys
sys.dont_write_bytecode=True
normalize=runpy.run_path(sys.argv[1],run_name='candidate')['normalize_slug']
results=[]
for row in json.load(sys.stdin):
    args=[row['text']]+([row['max_length']] if 'max_length' in row else [])
    try:
        result=normalize(*args)
        assert type(result) is str, 'return str'
        assert normalize(*args)==result, 'nondeterministic'
        results.append({'expected':result})
    except (TypeError,ValueError) as error:
        results.append({'error':type(error).__name__})
print(json.dumps(results))
