import os
import subprocess
import sys
from pathlib import Path


def test_query_example():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(root / "examples/query_basic.py")],
        cwd=root,
        env={**os.environ, "PYTHONPATH": str(root / "src")},
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
    assert result.stdout.splitlines() == [
        "Position: (1.0, 2.0)",
        "Position: (2.0, 2.0)",
        "Position: (3.0, 2.0)",
    ]
    assert result.stderr == ""
