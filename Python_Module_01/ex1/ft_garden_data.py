class Plant:
    def __init__(self, name: str, height: int, old: int):
        self.name = name.capitalize()
        self.height = height
        self.old = old


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.old} days old")
