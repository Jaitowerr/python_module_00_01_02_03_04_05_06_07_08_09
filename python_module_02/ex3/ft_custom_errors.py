#! /usr/bin/env python3

class GardenError(Exception):

    def __init__(self, msg: str = 'Unknow garden error') -> None:
        super().__init__(msg)


class PlantError(GardenError):

    def __init__(self, msg: str = 'Unknown plant error') -> None:
        # self.msg = msg
        super().__init__(msg)


class WaterError(GardenError):

    def __init__(self, msg: str = 'Unknown water error') -> None:
        # self.msg = msg
        super().__init__(msg)


def life(name: str, boo: bool) -> None:
    if not boo:
        raise PlantError(f'The {name} plant is wilting')
    else:
        print('The plant is perfect')


def water(boo: bool) -> None:
    if not boo:
        raise WaterError('Not enough water in the tank!')
    else:
        print('The water tank is full')


def test_errors():
    name, bool_life, bool_water = 'Tomato', False, False

    print("=== Custom Garden Errors Demo ===")

    print('\nTesting PlantError...')
    try:
        life(name, bool_life)
    except PlantError as e:
        print(f' **Caught{e.__class__.__name__}: {e}')

    print('\nTesting WaterError...')
    try:
        water(bool_water)
    except WaterError as e:
        print(f' **Caught {e.__class__.__name__}: {e}')

    print('\nTesting catching all garden errors...')

    def test_life() -> None:
        life(name, bool_life)

    def test_water() -> None:
        water(bool_water)

    pack = [test_life, test_water]
    for i in pack:
        try:
            i()
        except GardenError as e:
            print(f' **Caught {e.__class__.__name__}: {e}')

    print('\nAll custom error types work correctly!')


if __name__ == '__main__':
    test_errors()
