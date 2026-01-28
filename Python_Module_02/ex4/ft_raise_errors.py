def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
    """
    Validate plant health parameters and raise errors if invalid.

    Args:
        plant_name: Name of the plant
        water_level: Water level (1-10)
        sunlight_hours: Hours of sunlight per day (2-12)

    Raises:
        ValueError: If any parameter is invalid
    """
    if not plant_name or plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        line = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        raise ValueError(line)
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Test plant health checking with various inputs.
    Demonstrates error raising and handling.
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("carrot", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
