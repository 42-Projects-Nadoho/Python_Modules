import alchemy


def main():
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    tests = ["strength_potion", "heal"]
    for name in tests:
        potion = getattr(alchemy, name)
        print(f"Testing {name}: {potion()}")


if __name__ == "__main__":
    main()
