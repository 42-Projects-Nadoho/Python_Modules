def garden_operations() -> None:
    """
    Demonstrates different types of errors in garden operations.
    Shows ValueError, ZeroDivisionError, FileNotFoundError and KeyError.
    """
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_inventory = {"tomato": 10}
        print(garden_inventory["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nTesting multiple errors together...")
    try:
        int("oops")
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """
    Tests all garden error types.
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
