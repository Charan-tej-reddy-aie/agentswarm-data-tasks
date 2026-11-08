"""Evaluate a candidate in one isolated Python process; no labels in requests."""
import json
import runpy
import sys
sys.dont_write_bytecode = True
detect = runpy.run_path(sys.argv[1], run_name="candidate")["detect"]
result = [detect(text) for text in json.load(sys.stdin)]
assert all(type(value) is str and value in {"en", "es", "pt", "zh", "ja", "ko", "de", "fr"} for value in result), "unsupported code"
print(json.dumps(result))
