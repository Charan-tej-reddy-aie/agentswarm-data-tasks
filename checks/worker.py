"""Subprocess adapter; no fixture labels are passed to candidate functions."""
import copy
import json
import runpy
import sys
sys.dont_write_bytecode = True
module = runpy.run_path(sys.argv[1], run_name="candidate")
request = json.load(sys.stdin)
if request["function"] == "find_duplicates":
    before = copy.deepcopy(request["rows"])
    result = module["find_duplicates"](request["rows"])
    if request["rows"] != before:
        raise ValueError("find_duplicates must not mutate rows")
elif request["function"] == "flag":
    result = [module["flag"](r["title"], r["body"]) for r in request["rows"]]
else:
    raise ValueError("unknown function")
print(json.dumps(result, allow_nan=False))
