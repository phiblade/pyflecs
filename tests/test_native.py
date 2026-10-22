"""Regressions for the generated binding and installed-library boundary."""

import importlib
from pathlib import Path

from pyflecs import cflecs
from pyflecs._native import library_path


def test_generated_version_matches_vendored_release():
    assert (
        cflecs.FLECS_VERSION_MAJOR,
        cflecs.FLECS_VERSION_MINOR,
        cflecs.FLECS_VERSION_PATCH,
    ) == (4, 1, 0)


def test_zero_argument_macros_are_lazy_functions():
    # ctypesgen previously evaluated these on import, calling null pointers.
    # In particular, never call ecs_os_abort just to test that it is present.
    for name in (
        "ecs_os_thread_self",
        "ecs_os_mutex_new",
        "ecs_os_cond_new",
        "ecs_os_now",
        "ecs_os_abort",
        "ecs_log_push",
        "ecs_log_pop",
    ):
        assert callable(getattr(cflecs, name)), name


def test_all_public_modules_import():
    for name in (
        "builtins",
        "component",
        "entity",
        "inspect",
        "pipeline",
        "query",
        "system",
        "types",
        "world",
    ):
        importlib.import_module(f"pyflecs.{name}")


def test_native_library_exists_at_explicit_path():
    path = Path(library_path())
    assert path.is_absolute()
    assert path.is_file()


def test_missing_packaged_library_has_actionable_error(monkeypatch, tmp_path):
    import pytest

    import pyflecs
    from pyflecs import _native

    monkeypatch.setattr(_native, "files", lambda package: tmp_path)
    monkeypatch.setattr(pyflecs, "__path__", [str(tmp_path)])
    with pytest.raises(ImportError, match="working C compiler"):
        _native.library_path()
