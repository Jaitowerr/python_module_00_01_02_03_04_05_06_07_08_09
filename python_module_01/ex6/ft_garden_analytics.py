


class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, cm: int) -> None:
        self.height += cm
        print(f'{self.name} grew {cm}cm')

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, point: int) -> None:
        super().__init__(name, height, color)
        self.point = point

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.point}"







class GardenManager:

    total_gardens = 0

    def __init__(self, name_garden: str) -> None:
        self.name_garden = name_garden.capitalize()
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plants(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f'Added {plant.name} to {self.name_garden}')

    def grow_all(self, cm: int) -> None:
        print()
        for plant in self.plants:
            plant.grow(cm)









def main() -> None:
    print('=== Garden Management System Demo ===')
    alice = GardenManager("Alice's garden")

    oak = Plant('Oak Tree', 100)
    rose = FloweringPlant('Rose', 25, 'red')
    sunflower = PrizeFlower('Sunflower', 50, 'yellow', 10)

    alice.add_plants(oak)
    alice.add_plants(rose)
    alice.add_plants(sunflower)

    alice.grow_all(1)

if __name__ == '__main__':
    main()
