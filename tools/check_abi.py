"""Compare installed ctypes layouts to a C compiler reading vendored flecs.h.

Run this with the Python interpreter containing the installed package, outside
its checkout. Uses CC (default: cc); no native Flecs functions are executed.
"""

import argparse
import ctypes
import json
import os
import shlex
import subprocess
import tempfile
from pathlib import Path

TYPES = (
    "ecs_component_desc_t",
    "ecs_entity_desc_t",
    "ecs_type_info_t",
    "ecs_type_hooks_t",
    "ecs_term_ref_t",
    "ecs_term_t",
    "ecs_query_desc_t",
    "ecs_iter_t",
    "ecs_query_t",
    "ecs_system_desc_t",
    "ecs_pipeline_desc_t",
    "ecs_time_t",
)


def checks(bindings):
    for name in TYPES:
        typ = getattr(bindings, name)
        yield name + ".size", f"sizeof({name})", ctypes.sizeof(typ)
        yield name + ".align", f"_Alignof({name})", ctypes.alignment(typ)

        def fields(struct, prefix="", base=0):
            for field in struct._fields_:
                key, field_type = field[:2]
                path = prefix + key
                offset = base + getattr(struct, key).offset
                yield name + "." + path + ".offset", f"offsetof({name}, {path})", offset
                yield (
                    name + "." + path + ".size",
                    f"sizeof((({name}*)0)->{path})",
                    ctypes.sizeof(field_type),
                )
                if issubclass(field_type, ctypes.Array):
                    path += "[0]"
                    field_type = field_type._type_
                if field_type is not bindings.String and issubclass(
                    field_type, (ctypes.Structure, ctypes.Union)
                ):
                    yield from fields(field_type, path + ".", offset)

        yield from fields(typ)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    from pyflecs import cflecs

    comparisons = list(checks(cflecs))
    lines = [
        '#include "flecs.h"',
        "#include <stdio.h>",
        "#include <stddef.h>",
        "int main(void) {",
    ]
    for label, expr, _ in comparisons:
        lines.append(f'printf("{label} %zu\\n", (size_t)({expr}));')
    lines.append("return 0; }")
    with tempfile.TemporaryDirectory(prefix="pyflecs-abi-") as tmp:
        source = Path(tmp) / "abi.c"
        executable = Path(tmp) / "abi"
        source.write_text("\n".join(lines))
        subprocess.run(
            [
                *shlex.split(os.environ.get("CC", "cc")),
                "-std=gnu11",
                "-DFLECS_NDEBUG",
                "-I",
                str(args.source / "vendor/flecs"),
                str(source),
                "-o",
                str(executable),
            ],
            check=True,
        )
        output = subprocess.check_output([str(executable)], text=True)
    actual = dict(line.split() for line in output.splitlines())
    mismatches = {
        label: {"ctypes": expected, "C": int(actual[label])}
        for label, _, expected in comparisons
        if expected != int(actual[label])
    }
    if mismatches:
        raise SystemExit(json.dumps(mismatches, indent=2))
    print(
        f"ABI verified: {len(comparisons)} sizes, alignments, and offsets across {len(TYPES)} core types"
    )


if __name__ == "__main__":
    main()
