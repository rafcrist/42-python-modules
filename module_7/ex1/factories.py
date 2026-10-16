from ex0.factories import CreatureFactory
from ex0.creatures import Creature
from .creatures import Sproutling, Bloomelle, Morphagon, Shiftling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return (Sproutling())

    def create_evolved(self) -> Bloomelle:
        return (Bloomelle())


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return (Shiftling())

    def create_evolved(self) -> Morphagon:
        return (Morphagon())
