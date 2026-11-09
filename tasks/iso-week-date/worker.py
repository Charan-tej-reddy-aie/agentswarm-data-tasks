import copy,json,runpy,sys
sys.dont_write_bytecode=True
helper=runpy.run_path(sys.argv[1],run_name='candidate')['iso_week_date']
results=[]
for row in json.load(sys.stdin):
    args=copy.deepcopy(row['input']);before=copy.deepcopy(args)
    try:
        result=helper(*args)
        assert args==before,'mutation'
        again=helper(*args)
        assert result==again,'repeat'
        assert type(result) is str
        results.append({'expected':result})
    except (TypeError,ValueError) as error:
        assert args==before,'mutation on error'
        results.append({'error':type(error).__name__})

class IntSubclass(int): pass
for args in [(IntSubclass(2020),1,1),(2020,IntSubclass(1),1),(2020,1,IntSubclass(1)),(0,1,IntSubclass(1))]:
    try: helper(*args)
    except TypeError: pass
    else: raise AssertionError('int subclass accepted')

print(json.dumps(results))
