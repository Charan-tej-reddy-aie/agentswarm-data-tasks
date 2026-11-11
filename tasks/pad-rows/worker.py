import copy, importlib.util, json, sys
from pathlib import Path
TASK=Path(__file__).parent.name
spec=importlib.util.spec_from_file_location('candidate',sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
f=getattr(m,TASK.replace('-','_'))
rows=json.loads(Path(__file__).with_name('fixtures').joinpath('cases.json').read_text())
class I(int):pass
class S(str):pass
class L(list):pass
class D(dict):pass
def exact(a,b):
    assert type(a) is type(b),(a,b)
    if type(b) is dict:
        assert (list(a)==list(b) if TASK=='merge-counters' else a.keys()==b.keys()),(a,b)
        for k in b: exact(a[k],b[k])
    elif type(b) is list:
        assert len(a)==len(b),(a,b)
        for x,y in zip(a,b):exact(x,y)
    else:assert a==b,(a,b)
def check(args,row):
    before=copy.deepcopy(args)
    if 'error' in row:
        try:f(*args)
        except Exception as e:assert type(e) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],repr(e)
        else:raise AssertionError(('missing exception',args,row))
    else:
        a=f(*args);b=f(*args);exact(a,row['expected']);exact(b,row['expected'])
        if type(a) in (list,dict):
            assert a is not b and all(a is not x for x in args)
            if TASK=='coalesce-ranges':
                assert all(x is not y for x in a for y in args[0])
                if a:a[0].append(999)
            elif TASK=='paginate-items':
                assert a['items'] is not args[0] and a['items'] is not b['items']
                a['items'].append('changed')
            elif type(a) is list:a.append(999)
            else:a['changed']=999
            exact(f(*args),row['expected'])
    assert args==before,('input mutation',args,before)
for row in rows:check(row['args'],row)
bad=[[x,0] for x in [L(),L([[1]]),(),None,'ab',{}]]+[[[x],0] for x in [L([1]),(1,),1,None,'a']]+[[[[x]],0] for x in [True,I(1),1.0,'1',None,[1]]]+[[[[1]],x] for x in [True,False,I(0),0.0,'0',None,[0]]]+[[[[1],[x]],0] for x in [False,I(2)]]+[[[[0]]*101+[[True]],0],[[[10**9+1,True]],0],[[[10**10]],True],[[[1,2],[True]],10**10]]; bounds=[[[[10**9+1]],0],[[[-10**9-1]],0],[[[1]]*101,0],[[[0]*101],0],[[[1]],10**9+1],[[[1]],-10**9-1],[[[1],[1,2]*51],0],[[[],[1]],10**10]]
def fresh_inputs():
    shared=[4]
    return [([[1]],0),([[1,2],[3]],0),([[1,2],[3,4]],9),([[],[]],5),([[5],[]],-1),([[1,2,3]],7),([[1],[2],[3]],0),([[1,2],[3,4,5],[6]],0),([shared,shared,[1,2]],0),([shared,shared],8)]
for rows_in,fill in fresh_inputs():
    snap=copy.deepcopy(rows_in);width=max((len(r) for r in snap),default=0);want=[r+[fill]*(width-len(r)) for r in snap];out=f(rows_in,fill);again=f(rows_in,fill)
    assert out is not rows_in and again is not rows_in and out is not again,('returned the input list',snap)
    assert rows_in==snap,('the call changed the input',snap,rows_in)
    assert all(r is not x for r in out for x in rows_in),('returned row aliases an input row',snap)
    assert all(r is not x for r in out for x in again),('returned row shared between calls',snap)
    assert len({id(r) for r in out})==len(out),('returned rows share a list',snap)
    for r in out:
        r[:]=[99]*len(r);r.append(98)
    out.append([97])
    assert rows_in==snap,('mutating the result changed the input',snap,rows_in)
    exact(again,want);exact(f(rows_in,fill),want)
for args in bad:check(args,{'error':'TypeError'})
for args in bounds:check(args,{'error':'ValueError'})
print('PASS '+TASK+': '+str(len(rows))+' examples plus exact types, bounds and isolation probes')
