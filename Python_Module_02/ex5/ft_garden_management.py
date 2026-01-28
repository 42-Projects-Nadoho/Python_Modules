"""
Garden Management System - Comprehensive error handling demonstration.
Combines all error handling techniques learned throughout the project.
"""


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


class GardenManager:
    """Manages a garden with plants and watering system."""

    def __init__(self) -> None:
        """Initialize the garden manager."""
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, plant_name: str) -> None:
        """
        Add a plant to the garden.

        Args:
            plant_name: Name of the plant to add

        Raises:
            PlantError: If plant name is empty
        """
        try:
            if not plant_name or plant_name is None:
                raise PlantError("Plant name cannot be empty!")
            self.plants[plant_name] = {"water": 5, "sun": 8}
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, plant_list: list[str | None]) -> None:
        """
        Water a list of plants with proper cleanup.

        Args:
            plant_list: List of plant names to water
        """
        try:
            print("Opening watering system")
            for plant in plant_list:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str,
                           water_level: int,
                           sunlight_hours: int) -> None:
        """
        Check plant health parameters.

        Args:
            plant_name: Name of the plant
            water_level: Water level (1-10)
            sunlight_hours: Hours of sunlight (2-12)

        Raises:
            PlantError: If parameters are invalid
        """
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            if water_level > 10:
                raise WaterError(
                    f"Water level {water_level} is too high (max 10)")
            if water_level < 1:
                raise WaterError(
                    f"Water level {water_level} is too low (min 1)")
            if sunlight_hours > 12:
                raise PlantError(
                    f"Sunlight hours {sunlight_hours} is too high (max 12)")
            if sunlight_hours < 2:
                raise PlantError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)")
            line = f"{plant_name}: healthy (water:"
            line += f"{water_level}, sun: {sunlight_hours})"
            print(line)
        except GardenError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management() -> None:
    """
    Test the complete garden management system.
    Demonstrates all error handling techniques combined.
    """
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants(["tomato", "lettuce"])

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
