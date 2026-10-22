from ctypes import alignment, c_int32, sizeof

import pytest

from pyflecs.cflecs import ecs_fini, ecs_has_id, ecs_is_alive, ecs_pair, ecs_query_fini
from pyflecs.component import component
from pyflecs.query import QueryDescription, Term, TermRef
from pyflecs.system import SystemDescription, system
from pyflecs.world import World


@component
class Position:
    x: int


@component
class Velocity:
    x: int


@component
class Marker:
    pass


@component
class ArrayComponent:
    values: c_int32 * 3


@pytest.fixture
def world():
    value = World()
    yield value
    ecs_fini(value._value)


def instance(cls, x):
    value = cls()
    value.x = x
    return value


def test_registration_and_round_trip(world):
    cid = world.component(Position)
    assert world.component(Position) == cid
    entity = world.entity()
    assert world.get(entity, cid) is None
    world.set(entity, cid, instance(Position, 12))
    assert world.get(entity, cid).x == 12
    world.set(entity, Position, instance(Position, 23))
    assert world.get(entity, Position).x == 23
    world.set(entity, instance(Position, 34))
    assert world.get(entity, Position).x == 34
    world.clear(entity)
    assert world.get(entity, Position) is None


def test_class_add_and_delete(world):
    cid = world.component(Position)
    entity = world.entity()
    world.add(entity, Position)
    assert ecs_has_id(world._value, entity, cid)
    world.delete(entity)
    assert not ecs_is_alive(world._value, entity)


def test_invalid_component_access(world):
    entity = world.entity()
    with pytest.raises(ValueError, match="registered"):
        world.add(entity, Position)
    cid = world.component(Position)
    world.component(Velocity)
    with pytest.raises(TypeError, match="match"):
        world.set(entity, cid, instance(Velocity, 1))
    with pytest.raises(ValueError, match="registered"):
        world.get(entity, 999999)
    world.component(Marker)
    with pytest.raises(ValueError, match="Tags"):
        world.set(entity, Marker())


def test_array_alignment(world):
    assert alignment(ArrayComponent) == alignment(c_int32)
    assert sizeof(ArrayComponent) == 12
    world.component(ArrayComponent)
    value = ArrayComponent()
    value.values[:] = [3, 4, 5]
    entity = world.entity()
    world.set(entity, value)
    assert list(world.get(entity, ArrayComponent).values) == [3, 4, 5]


@pytest.mark.parametrize("use_classes", [False, True])
def test_pairs(world, use_classes):
    first = world.component(Position)
    second = world.component(Marker)
    entity = world.entity()
    world.add(entity, (Position, Marker) if use_classes else (first, second))
    assert ecs_has_id(world._value, entity, ecs_pair(first, second))


def test_builder_references_are_independent():
    a = Term.tuple((Position,))
    b = Term.tuple((Velocity,))
    assert a.id is Position
    assert b.id is Velocity
    assert Term.copy(a).id is Position
    assert Term.builder().id(Position).id(17).build().id == 17
    assert TermRef.kwargs(id=Position).id is Position
    assert TermRef.tuple((17,)).id == 17
    assert TermRef.kwargs(name="hello").name == "hello"


def populate(world):
    world.component(Position)
    world.component(Velocity)
    world.component(Marker)
    entities = []
    for x in range(4):
        entity = world.entity()
        world.set(entity, instance(Position, x))
        world.set(entity, instance(Velocity, x + 10))
        if x >= 2:
            world.add(entity, Marker)
        entities.append(entity)
    return entities


def test_query_visits_each_entity_across_tables(world):
    entities = populate(world)
    desc = (
        QueryDescription.builder()
        .terms([Term.tuple((Position,)), Term.tuple((Velocity,))])
        .build()
    )
    query = world.query(desc)
    try:
        seen = {}
        for result in query:
            seen[result.entity()] = (
                result.component(0, Position).x,
                result.component(1, Velocity).x,
            )
            result.component(0, Position).x += 100
        assert seen == {e: (x, x + 10) for x, e in enumerate(entities)}
        assert [world.get(e, Position).x for e in entities] == [100, 101, 102, 103]
        assert len(list(query)) == 4
        executor = iter(query)
        list(executor)
        assert list(executor) == []
    finally:
        ecs_query_fini(query._value)


def test_query_rejects_wrong_type_and_index(world):
    populate(world)
    query = world.query_terms([(Position,)])
    try:
        for result in query:
            with pytest.raises(TypeError, match="match"):
                result.component(0, Velocity)
            with pytest.raises(IndexError):
                result.component(1, Position)
    finally:
        ecs_query_fini(query._value)


def test_description_reusable_between_worlds(world):
    other = World()
    desc = QueryDescription.tuple([(Position,)])
    try:
        world.component(Position)
        other.component(Velocity)  # Position gets a different ID in this world.
        other.component(Position)
        assert world.cmptypeid(Position) != other.cmptypeid(Position)
        for value in (world, other, world):
            entity = value.entity()
            value.set(entity, instance(Position, 7))
            query = value.query(desc)
            try:
                assert all(r.component(0, Position).x == 7 for r in query)
            finally:
                ecs_query_fini(query._value)
            value.delete(entity)
        assert desc.terms[0].id is Position
    finally:
        ecs_fini(other._value)


def test_pair_query_with_component_references(world):
    world.component(Marker)
    world.component(Position)
    entity = world.entity()
    world.add(entity, (Marker, Position))
    desc = QueryDescription.tuple([(0, None, Marker, Position)])
    query = world.query(desc)
    try:
        assert [r.entity() for r in query] == [entity]
    finally:
        ecs_query_fini(query._value)


def test_system_each_visits_and_updates_every_entity(world):
    entities = populate(world)
    seen = []

    def each(result):
        seen.append(result.entity())
        result.component(0, Position).x += 1

    sid = world.system_each(QueryDescription.tuple([(Position,)]), each)
    world.run(sid)
    assert set(seen) == set(entities)
    assert len(seen) == 4
    assert [world.get(e, Position).x for e in entities] == [1, 2, 3, 4]
    world.delete(sid)
    assert not ecs_is_alive(world._value, sid)


def test_system_run_can_iterate_query(world):
    entities = populate(world)
    seen = []
    sid = world.system_kwargs(
        query=QueryDescription.tuple([(Position,)]),
        run=lambda executor: seen.extend(r.entity() for r in executor),
    )
    world.run(sid)
    assert set(seen) == set(entities)


def test_decorated_system(world):
    populate(world)
    seen = []

    @system(query=QueryDescription.tuple([(Position,)]))
    class Collector:
        def each(self, result):
            seen.append(result.component(0, Position).x)

    world.run(world.system(Collector))
    assert sorted(seen) == [0, 1, 2, 3]


def test_same_system_description_can_be_registered_twice(world):
    seen = []
    desc = SystemDescription.once(lambda executor: seen.append(True))
    first = world.system(desc)
    second = world.system(desc)
    world.run(first)
    world.run(second)
    assert seen == [True, True]


@pytest.mark.parametrize("mode", ["each", "run"])
def test_callback_exceptions_reach_caller(world, mode):
    populate(world)
    desc = QueryDescription.tuple([(Position,)])

    def fail(result):
        raise ValueError("callback failed")

    def run(executor):
        for result in executor:
            fail(result)

    sid = (
        world.system_each(desc, fail)
        if mode == "each"
        else world.system_kwargs(query=desc, run=run)
    )
    with pytest.raises(ValueError, match="callback failed"):
        world.run(sid)
    world.delete(sid)
    # A callback failure must not leave tables locked or poison later runs.
    entity = world.entity()
    world.set(entity, instance(Position, 9))
    seen = []
    world.run(world.system_once(lambda executor: seen.append(True)))
    assert seen == [True]


def test_system_description_reusable_between_worlds(world):
    other = World()
    seen = []
    desc = SystemDescription.each(
        QueryDescription.tuple([(Position,)]),
        lambda result: seen.append(result.component(0, Position).x),
    )
    try:
        world.component(Position)
        other.component(Velocity)
        other.component(Position)
        world.set(world.entity(), instance(Position, 10))
        other.set(other.entity(), instance(Position, 20))
        a, b = world.system(desc), other.system(desc)
        world.run(a)
        other.run(b)
        world.run(a)
        assert seen == [10, 20, 10]
    finally:
        ecs_fini(other._value)


def test_empty_query(world):
    world.component(Position)
    query = world.query_terms([(Position,)])
    try:
        assert list(query) == []
    finally:
        ecs_query_fini(query._value)


def test_shared_source_field_uses_source_value_for_every_row(world):
    entities = populate(world)
    source = world.entity()
    world.set(source, instance(Velocity, 42))
    query = world.query_terms([(Position,), (Velocity, source)])
    try:
        seen = [(r.entity(), r.component(1, Velocity).x) for r in query]
        assert seen == [(e, 42) for e in entities]
    finally:
        ecs_query_fini(query._value)


def test_optional_query_field(world):
    from pyflecs.cflecs import EcsOptional

    world.component(Position)
    world.component(Velocity)
    entity = world.entity()
    world.set(entity, instance(Position, 3))
    optional = Term.tuple((Velocity,))
    optional._value.oper = EcsOptional
    query = world.query_kwargs(terms=[Term.tuple((Position,)), optional])
    try:
        seen = []
        for result in query:
            seen.append(result.entity())
            with pytest.raises(ValueError, match="not set"):
                result.component(1, Velocity)
        assert seen == [entity]
    finally:
        ecs_query_fini(query._value)
