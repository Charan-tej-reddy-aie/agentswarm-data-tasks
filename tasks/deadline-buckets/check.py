import argparse, copy, doctest, importlib.util, json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution
spec=importlib.util.spec_from_file_location('candidate',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
task=Path(__file__).resolve().parent.name
helper=getattr(module,task.replace('-','_'))
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
def check(args,row):
 before=copy.deepcopy(args)
 if 'error' in row:
  try:helper(*args)
  except Exception as error:assert type(error) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],error
  else:raise AssertionError('missing exception')
 else:
  first=helper(*args);second=helper(*args)
  assert first==second==row['expected'],(args,first,row)
  if task=='platform-fee':assert type(first) is int
  else:
   assert type(first) is list and all(type(v) is str for v in first)
   assert first is not second and first is not args[0]
   first.append('changed');assert helper(*args)==row['expected']
 assert args==before
for row in cases:check(row['args'],row)
class I(int):pass
class S(str):pass
class L(list):pass
class D(dict):pass
if task=='rank-bids':
 for v in [L([]),(),None,[D(id='x',bid=0,score=1)],[dict(id=S('x'),bid=0,score=1)],[dict(id='x',bid=I(0),score=1)],[dict(id='x',bid=0,score=I(1))],[{S('id'):'x','bid':0,'score':1}]]:check([v],{'error':'TypeError'})
 check([[dict(id='x',bid=-1,score=1),dict(id='y',bid=True,score=1)]],{'error':'TypeError'})
 check([[dict(id='é',bid=10**100,score=100),dict(id='a',bid=10**100+1,score=100)]],{'expected':['é','a']})
elif task=='deadline-buckets':
 for args in [[L([]),0],[[I(1)],0],[[],I(0)],[(1,),0],[[1],False]]:check(args,{'error':'TypeError'})
 check([[10**100,10**100+60,10**100+61],10**100],{'expected':['expired','soon','later']})
else:
 for v in [I(1),True,False,None,1.0,'1',[],{},complex(1)]:check([v],{'error':'TypeError'})
 for v in [10**100,10**100+1,2**53+1]:check([v],{'expected':(v*3+99)//100})
 assert type(helper.__doc__) is str,'function docstring required'
 doc=doctest.DocTestParser().get_doctest(helper.__doc__,dict(vars(module)),'platform_fee',str(source),0)
 assert len(doc.examples)>=3,'at least three runnable examples required'
 for call,want in [('platform_fee(0)','0'),('platform_fee(100)','3'),('platform_fee(101)','4')]:
  assert any(example.source.strip()==call and example.want.strip()==want for example in doc.examples),(call,'required example missing')
 result=doctest.DocTestRunner().run(doc)
 assert result.failed==0 and result.attempted>=3,'doctest failed'
print(f'PASS {task}: {len(cases)} fixtures plus exact type, subclass, independence and doctest probes')
