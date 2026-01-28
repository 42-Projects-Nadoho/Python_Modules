def check_temperature(temp_str: str) -> int | None:
    """
    Validate temperature reading from agricultural sensors.

    Args:
        temp_str: String representation of temperature to validate

    Returns:
        Integer temperature if valid, None if error occurs
    """
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """
    Test temperature validation with various inputs.
    Demonstrates that program continues despite errors.
    """
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]

    for test_value in test_cases:
        print(f"\nTesting temperature: {test_value}")
        result = check_temperature(test_value)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
