from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Sproutling", creature_type="Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str | None = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Bloomelle", creature_type="Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        return f"{self.name} heals {target} and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name="Shiftling", creature_type="Normal")
        TransformCapability.__init__(self)
        self.transformed = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(
            self,
            name="Morphagon",
            creature_type="Normal/Dragon"
        )
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form"
