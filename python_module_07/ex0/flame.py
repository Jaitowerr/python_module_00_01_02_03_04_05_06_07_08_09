from .creature import Creature
from ex0.creature_factory import CreatureFactory


class Flamering(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", type="Fire")

    def attack(self) -> str:
        return f' - {self.name} uses Ember!'


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type="Fire/Flying")

    def attack(self) -> str:
        return f' - {self.name} uses Flamethrower!'


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flamering()

    def create_evolved(self) -> Creature:
        return Pyrodon()
