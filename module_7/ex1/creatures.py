from ex0.creatures import Creature
from .capabilities import HealCapability
from .capabilities import TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        name = "Sproutling"
        type = "Grass"
        super().__init__(name, type)

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self) -> str:
        return ("Sproutling heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        name = "Bloomelle"
        type = "Grass/Fairy"
        super().__init__(name, type)

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance!")

    def heal(self) -> str:
        return ("Bloomelle heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if (self.transformed is False):
            return ("Shiftling attacks normally.")
        return ("Shiftling performs a boosted strike!")

    def transform(self) -> str:
        self.transformed = True
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        self.transformed = False
        return ("Shiftling returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if (self.transformed is False):
            return ("Morphagon attacks normally.")
        return ("Morphagon unleashes a devastating morph strike!")

    def transform(self) -> str:
        self.transformed = True
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.transformed = False
        return ("Morphagon stabilizes its form.")
