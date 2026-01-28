class SecurePlant:
    def __init__(self, name: str):
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self):
        info = f"Current plant: {self.__name} ({self.__height}cm, "
        info += f"{self.__age} days)"
        print(info)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.get_info()
