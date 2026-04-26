from __future__ import annotations

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())
    except Exception as error:
        print(f"Factory test failed: {error}")


def test_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    print("\nTesting battle")
    try:
        first = first_factory.create_base()
        second = second_factory.create_base()
        print(first.describe())
        print("vs.")
        print(second.describe())
        print("fight!")
        print(first.attack())
        print(second.attack())
    except Exception as error:
        print(f"Battle test failed: {error}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
