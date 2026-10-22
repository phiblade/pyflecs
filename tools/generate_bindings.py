"""Regenerate the checked-in bindings; consumers do not need ctypesgen.

Run with `uv run python tools/generate_bindings.py` on macOS. The generated
bindings target 64-bit macOS/Linux and use the same FLECS_NDEBUG configuration
as CMake. Validate changes with tools/check_distribution.py before release.
"""

import ast
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "cflecs.py"
        subprocess.run(
            [
                sys.executable,
                "-c",
                "from ctypesgen.main import main; main()",
                "-l",
                "flecs",
                "-DFLECS_NDEBUG",
                "--strip-build-path",
                str(ROOT),
                "vendor/flecs/flecs.h",
                "-o",
                str(output),
            ],
            cwd=ROOT,
            check=True,
        )
        text = output.read_text()
        # ctypesgen 1.1.1 mistakes zero-argument function macros for constants,
        # evaluating native calls at import time. Keep them as Python functions.
        macros = set(
            re.findall(
                r"^#define\s+(\w+)\(\)",
                (ROOT / "vendor/flecs/flecs.h").read_text(),
                re.M,
            )
        )
        lines = text.splitlines(keepends=True)
        for node in reversed(ast.parse(text).body):
            if isinstance(node, ast.Try) and len(node.body) == 1:
                statement = node.body[0]
                if (
                    isinstance(statement, ast.Assign)
                    and len(statement.targets) == 1
                    and isinstance(statement.targets[0], ast.Name)
                    and statement.targets[0].id in macros
                ):
                    name = statement.targets[0].id
                    lines[node.lineno - 1 : node.end_lineno] = [
                        f"def {name}():\n    return {ast.unparse(statement.value)}\n"
                    ]
        text = "".join(lines)
        text = text[text.index("__docformat__") :]
        text = (
            '"""Generated from vendored Flecs 4.1.0 by tools/generate_bindings.py.\n'
            'Do not edit by hand; configuration: FLECS_NDEBUG, 64-bit Unix.\n"""\n\n'
            + text
        )
        loader = '_libs["flecs"] = load_library("flecs")'
        if text.count(loader) != 1:
            raise RuntimeError("ctypesgen loader changed; review integration")
        text = text.replace(
            loader,
            "from ._native import library_path as _library_path\n"
            '_libs["flecs"] = load_library(_library_path())',
        )
        (ROOT / "src/pyflecs/cflecs.py").write_text(text)
        subprocess.run(
            [sys.executable, "-m", "ruff", "format", "src/pyflecs/cflecs.py"],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()
