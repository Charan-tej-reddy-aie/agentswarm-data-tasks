import copy,json,runpy,sys
sys.dont_write_bytecode=True
helper=runpy.run_path(sys.argv[1],run_name='candidate')['json_pointer_get']
results=[]
for row in json.load(sys.stdin):
    args=copy.deepcopy(row['input']);before=copy.deepcopy(args)
    try:
        result=helper(*args)
        assert args==before,'mutation'
        again=helper(*args)
        assert result==again,'repeat'
        assert type(result) in (dict,list,str,int,float,bool,type(None))
        results.append({'expected':result})
    except (TypeError,ValueError,KeyError) as error:
        assert args==before,'mutation on error'
        results.append({'error':type(error).__name__})

class StrSubclass(str): pass
container={'a': []}
assert helper(container,'') is container, 'root identity'
assert helper(container,'/a') is container['a'], 'container identity'
try: helper({},StrSubclass(''))
except TypeError: pass
else: raise AssertionError('pointer subclass accepted')

print(json.dumps(results))
