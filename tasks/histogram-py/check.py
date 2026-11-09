import argparse,copy,importlib.util,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution
spec=importlib.util.spec_from_file_location('candidate',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
helper=m.histogram
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
def check(args,row):
 before=copy.deepcopy(args)
 if 'error' in row:
  try:helper(*args)
  except Exception as e:assert type(e) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],e
  else:raise AssertionError('missing exception')
 else:
  a=helper(*args);b=helper(*args)
  assert a==b==row['expected'],(args,a,row)
  assert type(a) is list and all(type(x) is int for x in a)
  assert a is not b and a is not args[0] and a is not args[1]
  a.append(999);assert helper(*args)==row['expected']
 assert args==before
for row in cases:check(row['args'],row)
class I(int):pass
class L(list):pass
for v in [L([]),(),None,True,1,'',{}]:
 check([v,[0,1]],{'error':'TypeError'});check([[],v],{'error':'TypeError'})
for v in [I(1),True,False,None,1.0,'1',[],{},complex(1)]:
 check([[v],[0,1]],{'error':'TypeError'});check([[],[0,v]],{'error':'TypeError'})
check([[2**100],[0,'x']],{'error':'TypeError'})
check([['x'],[]],{'error':'TypeError'})
for v in [9007199254740992,-9007199254740992,10**100]:
 check([[v],[0,1]],{'error':'ValueError'});check([[],[0,v]],{'error':'ValueError'})
check([[-9007199254740991,9007199254740991],[-9007199254740991,0,9007199254740991]],{'expected':[1,1]})
print(f'PASS histogram-py: {len(cases)} fixtures plus exact types, subclasses and boundary probes')
