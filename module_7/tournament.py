from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]

            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()

            print("* Battle *")
            print(creature_1.describe())
            print("vs.")
            print(creature_2.describe())
            print("now fight!")

            try:
                actions_1 = strategy_1.act(creature_1)
                actions_2 = strategy_2.act(creature_2)

                for action in actions_1:
                    print(action)

                for action in actions_2:
                    print(action)

            except InvalidStrategyError as error:
                print(
                    "Battle error, aborting tournament: "
                    f"{error}"
                )
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    tournament_0: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame, normal),
        (healing, defensive),
    ]

    battle(tournament_0)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    tournament_1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame, aggressive),
        (healing, defensive),
    ]

    battle(tournament_1)

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )

    tournament_2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive),
    ]

    battle(tournament_2)


if __name__ == "__main__":
    main()
