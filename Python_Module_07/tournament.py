from itertools import combinations
from typing import Iterable
from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)
from ex2.strategies import InvalidStrategyCreatureError

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: Iterable[Opponent]) -> None:
    opponent_list = list(opponents)
    print("*** Tournament ***")
    print(f"{len(opponent_list)} opponents involved")

    for first, second in combinations(opponent_list, 2):
        first_factory, first_strategy = first
        second_factory, second_strategy = second

        first_creature = first_factory.create_base()
        second_creature = second_factory.create_base()

        print("\n* Battle *")
        print(first_creature.describe())
        print("vs.")
        print(second_creature.describe())
        print("now fight!")

        for line in first_strategy.act(first_creature):
            print(line)
        for line in second_strategy.act(second_creature):
            print(line)


def run_tournament(title: str, opponents: list[Opponent], legend: str) -> None:
    print(title)
    print(legend)
    try:
        battle(opponents)
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    run_tournament(
        "Tournament 0 (basic)",
        [
            (FlameFactory(), normal),
            (HealingCreatureFactory(), defensive),
        ],
        "[ (Flameling+Normal), (Healing+Defensive) ]",
    )

    run_tournament(
        "\nTournament 1 (error)",
        [
            (FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive),
        ],
        "[ (Flameling+Aggressive), (Healing+Defensive) ]",
    )

    run_tournament(
        "\nTournament 2 (multiple)",
        [
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ],
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]",
    )


if __name__ == "__main__":
    main()
