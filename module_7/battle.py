from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    creature_1 = factory.create_base()
    creature_2 = factory.create_evolved()

    print("Testing factory")
    print(creature_1.describe())
    print(creature_1.attack())
    print(creature_2.describe())
    print(creature_2.attack())


def test_battle(
    factory_1: CreatureFactory,
    factory_2: CreatureFactory
) -> None:
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()
    print("Testing battle")
    print(creature_1.describe())
    print("vs.")
    print(creature_2.describe())
    print("fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    crea_1 = FlameFactory()
    crea_2 = AquaFactory()
    test_factory(crea_1)
    test_factory(crea_2)
    test_battle(crea_1, crea_2)


if __name__ == "__main__":
    main()
