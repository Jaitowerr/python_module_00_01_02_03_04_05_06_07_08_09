# Shiftling, Morphagon, TransformCreatureFactory
from ex0.creature import Creature
from .capability import TransformCapability
from ex0.creature_factory import CreatureFactory


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name='Shiftling', type='Normal')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f'{self.name} performs a boosted strike!'
        return f'{self.name} attacks normally'

    def transform(self) -> str:
        self.transformed = True
        return f'{self.name} shifts into a sharper form!'

    def revert(self) -> str:
        self.transformed = False
        return f'{self.name} returns to normal'


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name='Morphagon', type='Normal/Dragon')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f'{self.name} unleashes a devastating morph strike'
        return f'{self.name} attacks normally'

    def transform(self) -> str:
        self.transformed = True
        return f'{self.name} morphs into a dragonic battle form!'

    def revert(self) -> str:
        self.transformed = False
        return f'{self.name} stabilizes its form'


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
