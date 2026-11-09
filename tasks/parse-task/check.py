import argparse, copy, importlib.util, json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution
spec=importlib.util.spec_from_file_location('candidate',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
task=Path(__file__).resolve().parent.name
helper=getattr(module,'parse_task' if task=='parse-task' else 'unique_tags')
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
def check(value,row):
    before=copy.deepcopy(value)
    if 'error' in row:
        try: helper(value)
        except Exception as error: assert type(error) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],error
        else: raise AssertionError('missing exception')
    else:
        first=helper(value);second=helper(value)
        assert first==second==row['expected'],(value,first,row)
        assert type(first) is (dict if task=='parse-task' else list)
        assert first is not second and first is not value
        if task=='parse-task':
            assert all(type(key) is str for key in first)
            assert all(type(first[k]) is type(row['expected'][k]) for k in first)
            first['title']='changed'
        else:
            assert all(type(item) is str for item in first)
            first.append('changed')
        assert helper(value)==row['expected']
    assert value==before
for row in cases:check(row['input'],row)
class S(str):pass
class L(list):pass
if task=='parse-task':
    for value in [S('{"id":"a","title":"x","budget":0}'),b'{}',(),set()]:check(value,{'error':'TypeError'})
else:
    for value in [L(['a']),[S('a')],('a',),[b'a'],[complex(1)],set()]:check(value,{'error':'TypeError'})
    frozen=['a','b','a'];helper(frozen);assert frozen==['a','b','a']
print(f'PASS {task}: {len(cases)} fixtures plus subclass, exact type and independence probes')
