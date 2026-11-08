"""Trusted check helpers. Subprocess execution is not a security sandbox."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def solution(default):
    p = argparse.ArgumentParser()
    p.add_argument("--solution", type=Path, default=default)
    path = p.parse_args().solution.resolve()
    if not path.is_file():
        p.error("solution must be a Python source file")
    return path

def call(path, function, rows):
    proc = subprocess.run([sys.executable, "-I", str(ROOT / "checks/worker.py"), str(path)],
        input=json.dumps({"function": function, "rows": rows}), text=True,
        capture_output=True, timeout=10)
    assert proc.returncode == 0, proc.stderr[-1000:]
    return json.loads(proc.stdout)

def load(task, name):
    return json.loads((ROOT / "tasks" / task / "fixtures" / (name + ".json")).read_text())
