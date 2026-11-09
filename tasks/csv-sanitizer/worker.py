import copy,json,runpy,sys
sys.dont_write_bytecode=True
helper=runpy.run_path(sys.argv[1],run_name='candidate')['sanitize_csv_rows']
results=[]
for row in json.load(sys.stdin):
    value=copy.deepcopy(row['input']); before=copy.deepcopy(value)
    try:
        result=helper(value)
        assert type(result) is list and all(type(r) is list and all(type(c) is str for c in r) for r in result)
        assert value==before, 'mutation'
        assert helper(value)==result, 'repeat'
        assert helper(result)==result, 'idempotence'
        assert result is not value and all(out is not src for out in result for src in value), 'alias'
        assert len({id(r) for r in result})==len(result), 'shared output rows'
        results.append({'expected':result})
    except (TypeError,ValueError) as error:
        results.append({'error':type(error).__name__})
# Non-JSON type and alias probes.
for value in [(('x',),), [('x',)], [[b'x']], [[False]]]:
    try: helper(value)
    except TypeError: pass
    else: raise AssertionError('non-list or non-string accepted')
shared=['=1']; value=[shared,shared]; result=helper(value)
assert result==[["'=1"],["'=1"]] and result[0] is not result[1] and value==[['=1'],['=1']]
print(json.dumps(results))
