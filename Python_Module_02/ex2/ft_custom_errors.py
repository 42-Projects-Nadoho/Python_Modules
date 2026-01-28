class GardenError(Exception):
    """Base error for all garden-related problems."""
    def __init__(self, message: str = "A garden-related error occurred."):
        super().__init__(message)


class PlantError(GardenError):
    """Error related to plants."""
    def __init__(self, message: str = "A problem occurred with a plant."):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering."""
    def __init__(self, message: str = "A problem occurred with watering."):
        super().__init__(message)


def check_plant_health() -> None:
    """Simulate plant health check that raises PlantError."""
    raise PlantError("The tomato plant is wilting!")


def check_water_level() -> None:
    """Simulate water level check that raises WaterError."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """
    Demonstrates custom error handling.
    Shows how to catch specific and general error types.
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for func in (check_plant_health, check_water_level):
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
