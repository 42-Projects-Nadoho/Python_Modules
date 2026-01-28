class Plant:
    def __init__(self, name: str, height: int, old: int):
        self.name = name
        self.height = height
        self.old = old

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.old} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {len(plants)}")
