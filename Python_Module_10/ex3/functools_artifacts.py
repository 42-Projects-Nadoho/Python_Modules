from functools import lru_cache, partial, reduce, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    values = [10, 20, 30, 40]
    print("Sum:", spell_reducer(values, "add"))
    print("Product:", spell_reducer(values, "multiply"))
    print("Max:", spell_reducer(values, "max"))

    print("Testing partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.title()} enchantment on {target} with {power} power"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"]("Sword"))
    print(enchants["ice"]("Shield"))
    print(enchants["lightning"]("Spear"))

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print("Cache info:", memoized_fibonacci.cache_info())

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["heal", "shield", "boost"]))
    print(dispatcher({"unknown": True}))
