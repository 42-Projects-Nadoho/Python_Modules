import alchemy


def main():
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    tests = ["create_air", "create_earth"]
    for name in tests:
        if name == "create_air":
            print(f"Testing {name}: {getattr(alchemy, name)()}")
        else:
            print("Now show that not all functions can be reached")
            print("This will raise an exception!")
            print(f"Testing the hidden {name}: ", end="")
            print(f"{getattr(alchemy, name)()}")


if __name__ == "__main__":
    main()
