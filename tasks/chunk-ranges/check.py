import argparse, importlib.util, json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution
spec=importlib.util.spec_from_file_location('candidate',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
helper=module.chunk_ranges
cases=json.loads((Path(__file__).resolve().parent/'fixtures/cases.json').read_text())
for i,row in enumerate(cases):
    if 'error' in row:
        try: helper(*row['input'])
        except (TypeError,ValueError) as error: assert type(error).__name__==row['error'],(i,error)
        else: raise AssertionError(('missing exception',i))
    else:
        result=helper(*row['input']);again=helper(*row['input'])
        assert type(result) is list and result is not again
        assert all(type(x) is tuple and len(x)==2 and all(type(v) is int for v in x) for x in result)
        assert result==[tuple(x) for x in row['expected']]==again,(i,result)
class I(int): pass
for args in [(I(2),1),(2,I(1)),(-1,I(1))]:
    try: helper(*args)
    except TypeError: pass
    else: raise AssertionError('subclass accepted')
print(f'PASS chunk-ranges: {len(cases)} full spec cases and subclass probes')
