from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyCreatureError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(
            creature,
            TransformCapability,
        )

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            message = (
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
            raise InvalidStrategyCreatureError(
                message
            )
        transform_creature = creature
        assert isinstance(transform_creature, TransformCapability)
        return [
            transform_creature.transform(),
            creature.attack(),
            transform_creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(
            creature,
            HealCapability,
        )

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            message = (
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
            raise InvalidStrategyCreatureError(
                message
            )
        heal_creature = creature
        assert isinstance(heal_creature, HealCapability)
        return [
            creature.attack(),
            heal_creature.heal(),
        ]
