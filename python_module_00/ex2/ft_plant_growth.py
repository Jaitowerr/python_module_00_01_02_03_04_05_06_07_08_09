class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self, cm: int) -> None:
        self.height += cm

    def age(self, days: int) -> None:
        self.age_days += days

    def get_info(self) -> str:
        return f'{self.name}: {self.height}cm, {self.age_days} days old'


def main() -> None:
    p1 = Plant('Rose', 25, 30)
    p2 = Plant('Sunflower', 80, 45)
    p3 = Plant('Cactus', 15, 120)

    garden = [p1, p2, p3]

    for plant in garden:
        print(f'====={plant.name}=====')
        day_one_height = plant.height
        for day in range(1, 8):
            if day == 1 or day == 7:
                print(f'  === Day {day} ===')
                print(f'    {plant.get_info()}')
            plant.grow(2)
            plant.age(1)
        total_height = plant.height - day_one_height
        print(f'Growth this week: +{total_height}cm')
        print()


if __name__ == '__main__':
    main()
