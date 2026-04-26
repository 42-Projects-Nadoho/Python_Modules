from alchemy import create_air


def main():
    print("=== Alembic 5 ===")
    print(
        "Accessing the alchemy module using 'from alchemy import ...'"
    )
    print(f"Testing {create_air.__name__}: {create_air()}")


if __name__ == "__main__":
    main()
