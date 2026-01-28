class Plant:
    def __init__(self, name: str, height: int, old: int):
        self.name = name
        self.height = height
        self.old = old

    def grow(self):
        self.height += 1

    def age(self):
        self.old += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.old} days old"


if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30)]

    print("=== Day 1 ===")
    print(plants[0].get_info())

    initial_height = plants[0].height
    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    print(plants[0].get_info())
    growth = plants[0].height - initial_height
    print(f"Growth this week: +{growth}cm")
