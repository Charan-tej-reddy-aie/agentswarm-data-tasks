import argparse, importlib.util, json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution
spec=importlib.util.spec_from_file_location('candidate',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
task=Path(__file__).resolve().parent.name
helper=getattr(module,'group_indices' if task=='index-groups' else 'ceil_div')
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
def check(args,row):
    if 'error' in row:
        try: helper(*args)
        except Exception as error: assert type(error) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],error
        else: raise AssertionError('missing exception')
    else:
        import copy
        before=copy.deepcopy(args);first=helper(*args);second=helper(*args)
        assert args==before
        assert first==second==row['expected'],(args,first,row)
        if task=='index-groups':
            assert type(first) is dict and first is not second
            assert list(first)==list(row['expected'])
            for key,value in first.items():
                assert type(key) is str and type(value) is list and value is not second[key]
                assert all(type(n) is int for n in value)
                value.append(99)
            assert helper(*args)==row['expected']
        else: assert type(first) is int
for row in cases: check(row['input'],row)
class I(int): pass
class S(str): pass
class L(list): pass
if task=='index-groups':
    for args in [[L(['a'])],[[S('a')]],[(1,)]]:check(args,{'error':'TypeError'})
else:
    for args in [(I(2),1),(2,I(1)),(I(1),0),(2,()),((),2)]:check(args,{'error':'TypeError'})
print(f'PASS {task}: {len(cases)} cases plus exact subclass and independence probes')
