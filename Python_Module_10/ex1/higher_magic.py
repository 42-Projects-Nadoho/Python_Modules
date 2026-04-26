from collections.abc import Callable


Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Spell,
) -> Spell:
    def cast_if_allowed(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast_if_allowed


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_all


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} strength"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon", 10))

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Golem", 10))
    print("Amplified:", mega_fireball("Golem", 10))

    print("Testing conditional caster...")
    enough_power = conditional_caster(
        lambda _target, spell_power: spell_power >= 15,
        fireball,
    )
    print(enough_power("Wraith", 12))
    print(enough_power("Wraith", 20))

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    print(combo("Phoenix", 25))
