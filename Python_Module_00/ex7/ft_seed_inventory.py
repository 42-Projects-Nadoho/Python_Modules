def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()}: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()}: {quantity} grams total")
    elif unit == "square":
        print(f"{seed_type.capitalize()}: covers {quantity} square meters")
    else:
        print("Unknown unit type")
