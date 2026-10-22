"""Locate only the Flecs library built and installed with this package."""

import atexit
import sys
from contextlib import ExitStack
from importlib.resources import as_file, files
from pathlib import Path

import pyflecs

_resources = ExitStack()
atexit.register(_resources.close)


def library_path() -> str:
    if sys.platform == "darwin":
        name = "libflecs.dylib"
    elif sys.platform.startswith("linux"):
        name = "libflecs.so"
    else:
        raise ImportError("pyflecs currently supports 64-bit macOS and Linux")
    resource = files("pyflecs").joinpath(name)
    if resource.is_file():
        return str(_resources.enter_context(as_file(resource)))
    # scikit-build-core editable installs split Python and native files across
    # package paths. Its 0.11 resource reader only exposes the Python directory.
    for directory in pyflecs.__path__:
        candidate = Path(directory) / name
        if candidate.is_file():
            return str(candidate.resolve())
    raise ImportError(
        "The packaged Flecs library is missing. Install pyflecs with "
        "'pip install .' or 'uv sync' using a working C compiler. "
        "Importing directly from an unbuilt source checkout is unsupported."
    )
