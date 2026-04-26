from alchemy.potions import healing_potion, strength_potion


def main():
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    tests = [healing_potion, strength_potion]
    for name in tests:
        print(f"Testing {name.__name__}: {name()}")


if __name__ == "__main__":
    main()
