import abc
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability
from ex1.capabilities import HealCapability


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (True)

    def act(self, creature: Creature) -> list[str]:
        clist = [creature.attack()]
        return (clist)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return (True)
        return (False)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        assert isinstance(creature, TransformCapability)

        clist: list[str] = []
        clist.append(creature.transform())
        clist.append(creature.attack())
        clist.append(creature.revert())
        return (clist)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return (True)
        return (False)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )

        assert isinstance(creature, HealCapability)

        clist: list[str] = []
        clist.append(creature.attack())
        clist.append(creature.heal())
        return (clist)
