# pyflecs (PRE-ALPHA)

Python bindings for the excellent [flecs](https://www.flecs.dev/flecs/) library.

## Installation and development

pyflecs builds its own shared Flecs library from the source included in this
repository. There is no runtime download, system-library search, or dependency
on a prebuilt Flecs binary. The release is pinned to **Flecs 4.1.0**; updating
Flecs requires regenerating and validating the bindings as part of the port.

Requirements:

- Python 3.13 or newer.
- A C compiler: Apple Command Line Tools on macOS (`xcode-select --install`),
  or a C development toolchain on Linux (for example `build-essential` on Ubuntu).
- The current build targets 64-bit macOS and Linux. Windows and 32-bit builds
  are explicitly rejected until their bindings have been validated.

The distribution proof has been run on macOS ARM64. The Linux CI job is included,
but Linux support should not be treated as verified until that job passes.

Install from a checkout:

```sh
python -m pip install .
```

The installer creates an isolated build environment, obtains the Python build
backend and CMake/Ninja when needed, compiles the bundled Flecs source with your
C compiler, and installs the resulting wheel. No Flecs checkout or manual copy
of a shared library is required. Build dependencies may need network access;
Flecs source is always supplied locally.

For development:

```sh
uv sync --locked
uv run pytest
./run
```

`./run` executes `examples/query_basic.py`: it creates three entities, runs a
movement system, and prints their updated positions. Use the installed/editable
package; setting `PYTHONPATH=src` on an unbuilt checkout is not sufficient.
After changing native sources or CMake settings, rebuild the editable install
with `uv sync --reinstall-package pyflecs`.

To verify distribution independently of the checkout:

```sh
uv run python tools/check_distribution.py
# Retain the archive, wheel, and isolated environment for inspection:
uv run python tools/check_distribution.py --work-dir /tmp/pyflecs-proof
```

The proof builds a source archive with no binaries, checks the vendored source
hashes, builds a platform-tagged wheel from that archive, installs it into a fresh
environment, and runs ABI checks and the test suite outside the checkout. It then
installs directly from the source archive and repeats those checks. The ABI probe
compares 678 sizes, alignments, and offsets across the 12 core native types and
their embedded fields. This validates the core wrapper, not every raw Flecs API.

Explicit world/query cleanup and managed string ownership remain unfinished.

## Design

pyflecs consists of two parts; 1- `cflecs` and 2- `pyflecs`.

### cflecs

Part #1 is the auto-generated C binding which uses [ctypesgen](https://github.com/ctypesgen/ctypesgen). If so desired you can use this binding directly. For more information, see the section on [cflecs](#cflecs).

### pyflecs

pyflecs itself attempts to present a more python-like interface to to the user. See the user guide below for an introduction to the pyflecs API.

## User Guide

### Factory methods

Pyflecs makes heavy use of several factory method conventions:

- Builders
- Kwargs
- Tuples

Tips:
- Use builders whenever assignment of certain fields is conditional, or you need to construct part of the object, perform some logic, and then construct the rest of the fields
- Use kwargs where builder's expressiveness is desired but the assignment is a single expression and does not require any conditional logic or delayed assignment
- Use tuples when you prefer conciseness and only assigning required fields

### Components

Components are described using decorated classes as templates, similar to python's dataclasses.

```python
from pyflecs.component import component
from pyflecs.types import Double

@component
class Position:
    x: Double
    y: Double
```

#### Limitations of python typing

Python's type are much more flexible than C types, but strict data structure sizing is part of how flecs can be efficient and performant. Therefore, it's recommended that you think of the size of your types, and use the type aliases that are provided in the `pyflecs.types` package in place of python native types.

#### Using python native types

In python `int` is not a sized type. Using `int` is a little more natural in python, so we consider it's OK to do so. The same applies to other types, such as `float`, or `str`. The user should be aware of the following:

- When using int, pyflecs assumes you mean CInt64
- When using float, pyflecs assumes you mean CDouble
- When using str, pyflecs assumes you mean CString (char *)

Here's an example of the same code as above, using python `float` instead.

```python
from pyflecs.component import component
from pyflecs.types import Double

@component
class Position:
    x: float
    y: float
```

#### Using strings

Flecs uses utf-8 null terminated C strings. If you specify `str` as the type of your field, in flecs it will be a c_void_p. str allocates data on the heap, so if you want your string to be backed by struct data you'll have to declare a C type character array on your component and then marshal/unmarshal the data to the appropriate type you wish to work with manually. Support for these types of strings may be added in the future.

### Creating components

To create your component, simply call the world method `component`.

```python
from pyflecs.component import component
from pyflecs.types import Double
from pyflecs.world import World

@component
class Position:
    x: Double
    y: Double

def main():
    world = World()
    world.component(Position)
```

The world `component` method returns an `EntityId` which represents the component inside the flecs world. When calling other methods, or interacting with flecs in a way in which you need to provide the component ID, pyflecs also allows you to use the type (`Position`, for instance) as a reference, and the flecs ID will be looked up automatically.


### The component decorator

Because components are decorated using the `@component` decorator, a lot of ritual about preparing components is taken care of for you by pyflecs. However, it should be noted that the returned type is not a subclass of your component class, and therefore any methods, for instance, declared on the original component class will not be carried over. This is by design: you should not be declaring methods on your components, but as it happens, this is also necessary in some instances. For instance, when declaring a component with a field of python type `int`, the returned component will have a property getter and setter that performs autoconversion of the data to its underlying Int64 representation.

## Entities

### Creating an entity

```python
def main():
    world = World()
    e = world.entity()

```

Similarly to as in the component case, `world.entity()` returns an EntityId.

### Setting and getting component data

Register each component class once per world, then set values using an instance:

```python
position_id = world.component(Position)
e = world.entity()
p = Position()
p.x, p.y = 1.0, 2.0
world.set(e, p)

# Explicit class or ID forms are also supported:
world.set(e, Position, p)
world.set(e, position_id, p)
assert world.get(e, Position).x == 1.0
assert world.get(e, position_id).y == 2.0
```

`get()` returns `None` when the entity lacks the component. Returned components
are live views into Flecs storage, not copies; do not retain them across changes
that move or delete that storage. Unregistered classes and mismatched component
types raise Python exceptions. Empty components are tags: use `world.add(e, Tag)`
rather than `set()` or `get()`.

String ownership is not yet managed by the world. Keep the original Python
component instance alive while Flecs uses its string pointers. Robust string
ownership and view lifetime management remain unfinished.

## Queries

In flecs, a query is built off of a prepared template called a query description. Pyflecs provides a wrapper class and builder interface with various methods you can use to easily build instances of query description:

```python
    qd1 = QueryDescriptionBuilder()     # Builder
    qd2 = QueryDescription.builder()    # Convenience method
    qd3 = QueryDescription.kwargs()     # Forward args to builder via kwargs
    qd4 = QueryDescription.tuple()      # Forward term args only via tuple
```

You'll also need to utilize wrapper classes for some struct data contained inside a query description such as terms, term refs, etc. Term is wrapped the same way and provides the same kind of interfaces for construction:

```python
    t = TermBuilder()                   # A term builder object
    t = Term.builder()                  # Convenience method
    t = Term.kwargs()                   # Kwargs shorthand
    t = Term.tuple()                    # Tuple shorthand
```

### Terms

Refer to the flecs manual for an in depth look. In flecs, basically Terms are a set of 4 values, `id`, `src`, `first`, and `second`, and a bit of optional config. Because of this fact it's also very convenient to construct a Term using a tuple. Pyflecs expects you to provide a tuple with 1-4 elements of the form `(id, src, first, second)`.

#### Basic query example

```python
    @component
    class Position:
        x: float
        y: float

    qd = (
        QueryDescription.builder()
        .terms([Term.tuple((Position,))]) # Index 0 of the tuple is always `id`
        .build()
    )
```

### The query description tuple shorthand

If you don't need any additional config, you can construct a simple query with the `QueryDescription.tuple` shorthand, which expects an array of tuple `[(id, src, first, second), ...]`:

```python
    @component
    class Position:
        x: float
        y: float

    qd = QueryDescription.tuple([(Position,)]) 
```

### Creating the query

Creating a query must be done through world. Some convenience methods are also provided.

```python
    @component
    class Position:
        x: float
        y: float

    # Using description
    q = world.query(QueryDescription.tuple([(Position,)]))

    # Kwargs shorthand
    q = world.query_kwargs(
        terms=[Term.tuple((Position,))]
    )

    # Terms (tuple) shorthand
    q = world.query_terms([(Position,)])
```

### Query execution

In the flecs world we have basically only one concept in regards to execution of queries, which is the iterator. Pyflecs wraps iterator in two different objects; the QueryExecutor and the QueryResult. QueryExecutor represents an iterator that is ready to be advanced, while QueryResult represents an iterator that is currently pointing at a distinct result and may not be advanced. Because QueryExecutor performs iteration, it is a python iterable and can be used simply the way the any python iterable may be used, and returns one QueryResult per matching entity, including when Flecs batches multiple entities into a table. Each result has accessor methods on the underlying data. Consume result views inside the loop; they are not snapshots that can be retained after iteration advances.

```python
    executor = q.executor()
    for result in executor:
        print(result) # type QueryResult
```


### Getting the component

```python
    @component
    class Position:
        x: float
        y: float

    # Using description
    q = world.query(QueryDescription.tuple([(Position,)]))

    executor = q.executor()

    for result in executor:
        c = result.component(0, Position) # Instance of component
        print(c.x)
        print(c.y)
```


### Query result access

`result.entity()` returns the current entity ID. `result.component(index, Type)`
uses a zero-based field index and checks the registered component type before
accessing native memory. A mismatched type raises `TypeError`, and an invalid
field index raises `IndexError`. Tags have no component data.

Query descriptions can be reused in different worlds; component classes are
resolved independently against each world's registrations.

## Systems

In flecs, systems are basically processes that execute a `run` method. Flecs also supports _iterative systems_ which bind a query together with a callback that is executed conditionally based on the results of the executed query. See the flecs documentation on systems for more information.

### Defining a basic system

pyflecs provides a declarative template syntax similar to the one used to declare components, which uses a class and a class decorator. You can also create systems in the typical manner, similar to queries, using builders and/or convenience methods, but class syntax is a good starting point for most cases.

```python
@system()
class RunSystem:
    def run(self, executor: QueryExecutor):
        print("I run")
```

Systems with a `run` method may also perform queries, but since they override the default `run` function, iteration must be performed manually with the provided `QueryExecutor` object. An iterative system, on the other hand, performs query execution and provides its callback with a `QueryResult` object.

```python
@system(query=QueryDescription.tuple([(Position,)]))
class IteratingSystem:
    def each(self, result: QueryResult):
        print("I process result")
```

### Creating a system

Creating a system must be done through world, similarly as components.

```python
    run_system_instance = world.system(RunSystem)
    iterating_system_instance = world.system(IteratingSystem)
    print(run_system_instance) # the integer EntityId
```

### Running a system

Systems must be run inside world.

```python
    world.run(system_instance)

```

By default, system callbacks run on the calling thread. Exceptions from Python `run` or
`each` callbacks are re-raised after `world.run()` or `world.progress()` returns
from native execution.

## Native build and generated bindings

`CMakeLists.txt` builds a shared library from the unmodified release files under
`vendor/flecs/`. It changes the static-library define in a build-directory copy
of the header only. The source, bindings, and ABI probe all use `FLECS_NDEBUG`
and the default Flecs addons; changing those settings requires revalidation.
See `vendor/flecs/README.md` for the upstream commit, license, and file hashes.

Maintainers can regenerate the checked-in bindings on macOS with:

```sh
uv run python tools/generate_bindings.py
uv run python tools/check_distribution.py
```

Consumers do not need ctypesgen. The regeneration script integrates the
package-local loader and corrects ctypesgen 1.1.1's handling of zero-argument
function macros, which would otherwise execute native calls during import.
ctypesgen can report parser diagnostics for system headers and unsupported C
macros; successful generation alone is not validation. Review those diagnostics
and require the ABI probe and installed-package tests to pass after a port.

CMake and scikit-build-core are build-time tools; the installed package has no
third-party Python runtime dependencies. The native file is kept inside the
package and the Flecs MIT license is included in both source and wheel artifacts.
