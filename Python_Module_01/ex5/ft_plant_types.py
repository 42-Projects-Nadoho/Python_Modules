class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {shade_area:.0f} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self):
        return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
          f"{rose.color} color")
    print(rose.bloom())

    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    print(oak.produce_shade())

    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
          f"{tomato.harvest_season}")
    print(tomato.get_nutrition())

    tulip = Flower("Tulip", 30, 20, "yellow")
    print(f"{tulip.name} (Flower): {tulip.height}cm, {tulip.age} days, "
          f"{tulip.color} color")
    print(tulip.bloom())

    pine = Tree("Pine", 450, 1200, 40)
    print(f"{pine.name} (Tree): {pine.height}cm, {pine.age} days, "
          f"{pine.trunk_diameter}cm diameter")
    print(pine.produce_shade())

    carrot = Vegetable("Carrot", 20, 60, "fall harvest", "beta-carotene")
    print(f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days, "
          f"{carrot.harvest_season}")
    print(carrot.get_nutrition())
