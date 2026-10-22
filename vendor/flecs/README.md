# Vendored Flecs

Upstream: https://github.com/SanderMertens/flecs
Release: v4.1.0
Commit: 9e06477db0fdf9317bf583ff4b1318622283165f
License: MIT (see LICENSE)

The files are unmodified copies of `distr/flecs.h`, `distr/flecs.c`, and `LICENSE`
from that commit. SHA-256:

- flecs.h: 4b422ccd7abd4c691dce1c9296543d99da164d6c9d4149aa3b32779e69a85997
- flecs.c: 49b576dd9a4bbbbef17d593de1e8e65d6f55414bb8c916445b5bdf99b3f180a8
- LICENSE: 5f89f3edd5d1e458cd48509818e23b57d85869f7d57d0ebe31bcfd3a73e5dd60

CMake removes the header's default `flecs_STATIC` definition in a build-directory
copy only, then compiles a shared library with `FLECS_NDEBUG`. The bindings are
generated with the same `FLECS_NDEBUG` setting and default addon configuration.
Do not independently update the source or bindings: regenerate and verify the
ABI and installed-package tests together.
