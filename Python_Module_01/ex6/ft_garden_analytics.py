class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming!"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int = 0):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def award_points(self, points: int):
        self.prize_points += points


class GardenManager:
    class GardenStats:
        def __init__(self):
            self.total_plants = 0
            self.total_growth = 0
            self.plants_by_type = {"regular": 0, "flowering": 0, "prize": 0}

        def add_plant(self, plant):
            self.total_plants += 1
            if isinstance(plant, PrizeFlower):
                self.plants_by_type["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                self.plants_by_type["flowering"] += 1
            else:
                self.plants_by_type["regular"] += 1

        def record_growth(self, growth_amount):
            self.total_growth += growth_amount

        def get_stats(self):
            return {
                "total_plants": self.total_plants,
                "total_growth": self.total_growth,
                "plants_by_type": self.plants_by_type,
            }

    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.stats = self.GardenStats()
        self.height_valid = True

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")
            self.stats.record_growth(1)

    def validate_height(self):
        for plant in self.plants:
            if plant.height < 0:
                self.height_valid = False
                return False
        return True

    def get_garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                line = f"- {plant.name}: {plant.height}cm, {plant.color} "
                line += f"flowers ({plant.bloom()}), Prize points: "
                line += f"{plant.prize_points}"
                print(line)
            elif isinstance(plant, FloweringPlant):
                line = f"- {plant.name}: {plant.height}cm, {plant.color} "
                line += f"flowers ({plant.bloom()})"
                print(line)
            else:
                print(f"- {plant.name}: {plant.height}cm")

        stats = self.stats.get_stats()
        print(f"Plants added: {stats['total_plants']}, "
              f"Total growth: {stats['total_growth']}cm")
        print(f"Plant types: {stats['plants_by_type']['regular']} regular, "
              f"{stats['plants_by_type']['flowering']} flowering, "
              f"{stats['plants_by_type']['prize']} prize flowers")

    def get_garden_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points * 10
        return score

    @classmethod
    def create_garden_network(self):
        return [self("Alice"), self("Bob")]

    @staticmethod
    def are_gardens_equal(garden1, garden2):
        return garden1.name == garden2.name


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100, 1000))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 45, "yellow", 10))

    alice_garden.grow_all_plants()
    print()

    alice_garden.get_garden_report()
    print()

    height_valid = alice_garden.validate_height()
    print(f"Height validation test: {height_valid}")
    print()

    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Maple", 150, 800))
    bob_garden.add_plant(FloweringPlant("Tulip", 20, 25, "purple"))
    bob_garden.add_plant(PrizeFlower("Dahlia", 60, 90, "pink", 8))

    alice_score = alice_garden.get_garden_score()
    bob_score = bob_garden.get_garden_score()

    print(f"Garden scores - {alice_garden.name}: {alice_score}, "
          f"{bob_garden.name}: {bob_score}")

    gardens = GardenManager.create_garden_network()
    print(f"Total gardens managed: {len(gardens) + 1}")

    test_equals = GardenManager.are_gardens_equal(gardens[0], gardens[2])
    print(f"Are Alice equals too bob ? : {test_equals}")
