"""Build from an sdist, install in a fresh environment, and verify outside the repo.

Requires uv, Python 3.13+, and a C compiler. Build/test dependencies may be
fetched from PyPI; Flecs itself is always built from the bundled source.
Usage: python tools/check_distribution.py [--work-dir /tmp/pyflecs-proof]
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    "flecs.h": "4b422ccd7abd4c691dce1c9296543d99da164d6c9d4149aa3b32779e69a85997",
    "flecs.c": "49b576dd9a4bbbbef17d593de1e8e65d6f55414bb8c916445b5bdf99b3f180a8",
    "LICENSE": "5f89f3edd5d1e458cd48509818e23b57d85869f7d57d0ebe31bcfd3a73e5dd60",
}


def verify(work):
    env = {
        key: value
        for key, value in os.environ.items()
        if key not in {"PYTHONPATH", "PYTHONHOME", "VIRTUAL_ENV"}
    }

    def run(*args, cwd=work):
        print("+", " ".join(map(str, args)), flush=True)
        subprocess.run(list(map(str, args)), cwd=cwd, env=env, check=True)

    dist = work / "dist"
    # Explicitly build the wheel from the archive, not the working tree.
    run("uv", "build", "--python", sys.executable, "--sdist", ROOT, "--out-dir", dist)
    (sdist,) = dist.glob("*.tar.gz")
    with tarfile.open(sdist) as archive:
        assert not any(
            name.endswith((".dylib", ".so", ".dll")) for name in archive.getnames()
        ), "sdist contains a prebuilt library"
        archive.extractall(work / "source", filter="data")
    (source,) = (work / "source").iterdir()
    for name, expected in HASHES.items():
        actual = hashlib.sha256(
            (source / "vendor/flecs" / name).read_bytes()
        ).hexdigest()
        assert actual == expected, f"Vendored {name} differs from the pinned release"
    run("uv", "build", "--python", sys.executable, "--wheel", sdist, "--out-dir", dist)
    (wheel,) = dist.glob("*.whl")
    assert "-py3-none-" in wheel.name and not wheel.name.endswith("-any.whl")
    with zipfile.ZipFile(wheel) as archive:
        native = [
            name
            for name in archive.namelist()
            if name.endswith((".dylib", ".so", ".dll"))
        ]
        assert len(native) == 1, native
        assert "pyflecs/licenses/flecs-LICENSE" in archive.namelist()
        (metadata,) = [
            name for name in archive.namelist() if name.endswith("/METADATA")
        ]
        assert b"Requires-Dist:" not in archive.read(metadata), (
            "Unexpected runtime dependency"
        )

    venv = work / "env"
    run("uv", "venv", "--python", sys.executable, venv)
    python = venv / "bin/python"
    run("uv", "pip", "install", "--python", python, wheel, "pytest==8.4.2")

    checks = work / "checks"
    checks.mkdir()
    for folder in ("tests", "examples"):
        shutil.copytree(source / folder, checks / folder)

    # No src/ directory, repository pytest configuration, or source PYTHONPATH.
    def installed_checks():
        run(
            python,
            "-I",
            "-c",
            "from pathlib import Path; import sys, pyflecs; "
            "from pyflecs._native import library_path; "
            "p = Path(pyflecs.__file__).resolve(); n = Path(library_path()).resolve(); "
            "assert p.is_relative_to(Path(sys.prefix).resolve()), p; "
            "assert n.is_relative_to(Path(sys.prefix).resolve()), n; "
            "print('Installed Python:', p); print('Installed native library:', n)",
        )
        run(python, "-I", source / "tools/check_abi.py", "--source", source)
        run(python, "-I", "-m", "pytest", "-q", "tests", cwd=checks)

    installed_checks()
    # Prove the consumer's source-install path too, not just wheel installation.
    run(
        "uv",
        "pip",
        "install",
        "--python",
        python,
        "--reinstall-package",
        "pyflecs",
        sdist,
    )
    installed_checks()
    print(f"Distribution proof passed. Artifacts and environment: {work}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--work-dir", type=Path, help="New directory for retained evidence"
    )
    args = parser.parse_args()
    if args.work_dir:
        work = args.work_dir.resolve()
        work.mkdir(parents=True, exist_ok=False)
        verify(work)
    else:
        with tempfile.TemporaryDirectory(prefix="pyflecs-dist-") as tmp:
            verify(Path(tmp))
        print("Temporary verification directory removed.")


if __name__ == "__main__":
    main()
