from ctypes import POINTER, _Pointer, alignment, byref, cast, sizeof

from .cflecs import (
    String,
    ecs_add_id,
    ecs_add_pair,
    ecs_clear,
    ecs_component_init,
    ecs_delete,
    ecs_entity_init,
    ecs_get_id,
    ecs_get_pipeline,
    ecs_init,
    ecs_pipeline_init,
    ecs_progress,
    ecs_run,
    ecs_set_id,
    ecs_size_t,
    ecs_system_init,
    struct_ecs_component_desc_t,
    struct_ecs_entity_desc_t,
    struct_ecs_world_t,
)
from .component import Component
from .entity import EntityIdPair
from .patch import patch
from .pipeline import Pipeline
from .query import Query, QueryDescription
from .system import EachAction, OnceAction, SystemDescription
from .types import EntityId

idof = id

patch()  # TODO: Move to init


class World:
    def __init__(self, pipeline: Pipeline | None = None):
        self._value: _Pointer[struct_ecs_world_t] = ecs_init()
        self._callback_errors: list[BaseException] = []
        self._systemdescs: dict[int, SystemDescription] = {}
        self._cmptypes: dict[int, type[Component]] = {}
        self._cmpids: dict[type[Component], int] = {}

    @property
    def pipeline(self):
        """Return the pipeline that this world is using."""
        return Pipeline(ecs_get_pipeline(self._value))

    @pipeline.setter
    def pipeline(self, pipeline: Pipeline):
        """Set the pipeline that this world is using."""
        ecs_pipeline_init(self._value, pipeline.description)

    def component(self, cls: type[Component]):
        """Create a new component in this world."""

        if cls in self._cmpids:
            return self._cmpids[cls]

        desc = struct_ecs_component_desc_t()

        entity_desc = struct_ecs_entity_desc_t()
        entity_desc.id = 0

        byte_name = String(cls._wrapped_.__qualname__.encode("utf-8"))

        entity_desc.name = byte_name
        entity_desc.symbol = byte_name
        entity_desc.use_low_id = True

        entity_id: EntityId = ecs_entity_init(self._value, byref(entity_desc))

        desc.entity = entity_id
        desc.type.size = ecs_size_t(sizeof(cls))
        desc.type.alignment = ecs_size_t(alignment(cls) if sizeof(cls) else 0)
        # desc.type.name = Box(String(component.__name__.encode("utf-8"))).value()

        # TODO: hooks

        component_id = ecs_component_init(self._value, byref(desc))
        self._cmptypes[component_id] = cls
        self._cmpids[cls] = component_id
        return component_id

    def cmptypeid(self, cls: type[Component]) -> int:
        """Look up a component registered in this world."""
        try:
            return self._cmpids[cls]
        except KeyError:
            raise ValueError(
                "Component must be registered in this world first"
            ) from None

    def _component_id(self, component: int | type[Component]) -> int:
        if isinstance(component, int):
            return component
        if isinstance(component, type) and issubclass(component, Component):
            return self.cmptypeid(component)
        raise TypeError("Expected a component class or integer entity ID")

    def entity(self):
        """Create a new entity in this world."""

        desc = struct_ecs_entity_desc_t()
        desc.use_low_id = False

        entity_id: EntityId = ecs_entity_init(self._value, byref(desc))

        return entity_id

    def add(self, e: EntityId, i: EntityId | EntityIdPair):
        """Add a component to the specified entity."""

        if isinstance(i, tuple):
            return self.add_pair(e, i)
        return ecs_add_id(self._value, e, self._component_id(i))

    def add_pair(
        self, entity_id: int, pair: tuple[int | type[Component], int | type[Component]]
    ):
        """Add a relationship pair using entity IDs or registered component classes."""
        ecs_add_pair(
            self._value,
            entity_id,
            self._component_id(pair[0]),
            self._component_id(pair[1]),
        )

    def set(
        self,
        entity_id: int,
        component_id: int | type[Component] | Component,
        component: Component | None = None,
    ):
        """Set a component by ID/class, or infer its ID from the instance."""
        if component is None:
            component = component_id
            component_id = type(component)
        component_id = self._component_id(component_id)
        cls = self._cmptypes.get(component_id)
        if cls is None or type(component) is not cls:
            raise TypeError(
                "Component instance must match the registered component type"
            )
        if not sizeof(cls):
            raise ValueError("Tags have no data; use add() instead")
        ecs_set_id(
            self._value, entity_id, component_id, sizeof(component), byref(component)
        )

    def get(
        self, entity_id: int, component_id: int | type[Component]
    ) -> Component | None:
        """Return a live component view, or None if the entity does not have it."""
        component_id = self._component_id(component_id)
        cls = self._cmptypes.get(component_id)
        if cls is None:
            raise ValueError("Component ID is not registered in this world")
        if not sizeof(cls):
            raise ValueError("Tags have no component data")
        ptr = ecs_get_id(self._value, entity_id, component_id)
        return cast(ptr, POINTER(cls)).contents if ptr else None

    def clear(self, entity_id: EntityId):
        """Clear the specified entity of all components."""

        ecs_clear(self._value, entity_id)

    def delete(self, entity_id: EntityId):
        """Delete the specified entity."""

        ecs_delete(self._value, entity_id)
        self._systemdescs.pop(entity_id, None)
        cls = self._cmptypes.pop(entity_id, None)
        if cls is not None:
            del self._cmpids[cls]

    def query(self, d: QueryDescription):
        """Create a query from a query description object."""

        return Query(self, d)

    def query_kwargs(self, **kwargs):
        """Create a query from a query description built implicitly using the provided kwargs."""

        return Query.kwargs(self, **kwargs)

    def query_terms(self, terms: list[tuple]):
        """Create a simple query, with default configuration, based only on a list of terms."""

        return Query(self, QueryDescription.tuple(terms))

    def system(self, system_desc: SystemDescription) -> EntityId:
        """Create a new system."""

        system_desc = system_desc.resolved(self)
        system_id = ecs_system_init(self._value, byref(system_desc._value))

        # Pyflecs must keep a reference so the object is not garbage collected while flecs is using it
        self._systemdescs[system_id] = system_desc

        return system_id

    def system_kwargs(self, **kwargs):
        """Create a new system from a system description built implicitly using the provided kwargs."""

        return self.system(SystemDescription.kwargs(**kwargs))

    def system_once(self, action: OnceAction):
        """Create a new system, using defaults, with a run action."""

        return self.system(SystemDescription.once(action))

    def system_each(self, query: QueryDescription, action: EachAction):
        """Create a new system, using defaults, with a query and each action."""

        return self.system(SystemDescription.each(query, action))

    def run(self, system_id: EntityId, delta=0.0):
        """Run the specified system once."""

        ecs_run(self._value, system_id, delta, None)
        self._raise_callback_error()

    def progress(self):
        """Move time forward on this world, triggering pipeline processing on the delta time."""

        result = ecs_progress(self._value, 0)
        self._raise_callback_error()
        return result

    def _raise_callback_error(self):
        if self._callback_errors:
            error = self._callback_errors[0]
            self._callback_errors.clear()
            raise error
