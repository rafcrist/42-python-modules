from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")

    healing_factory = HealingCreatureFactory()

    base_healing = healing_factory.create_base()
    evolved_healing = healing_factory.create_evolved()

    print("base:")
    print(base_healing.describe())
    print(base_healing.attack())
    print(base_healing.heal())

    print("evolved:")
    print(evolved_healing.describe())
    print(evolved_healing.attack())
    print(evolved_healing.heal())

    print("Testing Creature with transform capability")

    transform_factory = TransformCreatureFactory()

    base_transform = transform_factory.create_base()
    evolved_transform = transform_factory.create_evolved()

    print("base:")
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())

    print("evolved:")
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())


if __name__ == "__main__":
    main()
