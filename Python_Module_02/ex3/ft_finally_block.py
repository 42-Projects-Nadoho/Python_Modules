def water_plants(plant_list: list[str | None]) -> None:
    """
    Simulates opening a watering system and watering plants.
    Ensures cleanup with finally block.

    Args:
        plant_list: List of plant names to water
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant} - success")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Tests watering system with valid and invalid plant lists.
    Demonstrates that cleanup always occurs.
    """
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plants: list[str | None] = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plants: list[str | None] = ["tomato", None]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
