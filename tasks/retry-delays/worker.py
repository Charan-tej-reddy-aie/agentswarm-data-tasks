import copy,json,runpy,sys
sys.dont_write_bytecode=True
helper=runpy.run_path(sys.argv[1],run_name='candidate')['retry_delays']
results=[]
for row in json.load(sys.stdin):
    args=copy.deepcopy(row['input']);before=copy.deepcopy(args)
    try:
        result=helper(*args)
        assert args==before,'mutation'
        again=helper(*args)
        assert result==again,'repeat'
        assert type(result) is list and all(type(x) is int for x in result) and result is not again
        results.append({'expected':result})
    except (TypeError,ValueError,KeyError) as error:
        assert args==before,'mutation on error'
        results.append({'error':type(error).__name__})

class IntSubclass(int): pass
class StrSubclass(str): pass
for args in [(IntSubclass(1),0,0,None),(0,IntSubclass(0),0,None),(0,0,IntSubclass(0),None),(0,0,0,StrSubclass('0'))]:
    try: helper(*args)
    except TypeError: pass
    else: raise AssertionError('subclass accepted')

print(json.dumps(results))
