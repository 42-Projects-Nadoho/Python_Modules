from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None and len(args) > 0 and isinstance(args[0], int):
                power = args[0]
            if power is None and len(args) > 1 and isinstance(args[1], int):
                power = args[1]
            if power is None and len(args) > 2 and isinstance(args[2], int):
                power = args[2]

            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        stripped_name = name.strip()
        if len(stripped_name) < 3:
            return False
        return all(
            character.isalpha() or character.isspace()
            for character in stripped_name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    print("Result:", fireball())

    print("Testing retrying spell...")
    attempts = {"count": 0}

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempts["count"] += 1
        if attempts["count"] < 4:
            raise RuntimeError("Unstable magic")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def eventually_successful_spell() -> str:
        attempts["count"] += 1
        if attempts["count"] < 6:
            raise RuntimeError("Still unstable")
        return "Waaaaaaagh spelled !"

    print(eventually_successful_spell())

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alya Storm"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 8))
