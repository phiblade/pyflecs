"""Create components, run a movement system, and read every matching entity."""

from pyflecs.component import component
from pyflecs.query import QueryDescription
from pyflecs.system import system
from pyflecs.world import World


@component
class Position:
    x: float
    y: float


@component
class Velocity:
    x: float
    y: float


@system(query=QueryDescription.tuple([(Position,), (Velocity,)]))
class Move:
    def each(self, result):
        position = result.component(0, Position)
        velocity = result.component(1, Velocity)
        position.x += velocity.x
        position.y += velocity.y


def main():
    world = World()
    world.component(Position)
    world.component(Velocity)

    for x in range(3):
        entity = world.entity()
        position = Position()
        position.x, position.y = float(x), 0.0
        velocity = Velocity()
        velocity.x, velocity.y = 1.0, 2.0
        world.set(entity, position)
        world.set(entity, velocity)

    world.run(world.system(Move))

    for result in world.query_terms([(Position,)]):
        position = result.component(0, Position)
        print(f"Position: ({position.x:.1f}, {position.y:.1f})")


if __name__ == "__main__":
    main()
