#! /usr/bin/env python3

from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print('****** Testing factory')
    factor = factory.create_base()
    print(factor.describe())
    print(factor.attack())
    factory_evol = factory.create_evolved()
    print(factory_evol.describe())
    print(factory_evol.attack())
    print()


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print('****** Testing battle')
    factor1 = factory1.create_base()
    factor2 = factory2.create_base()
    print(factor1.describe())
    print(' vs.')
    print(factor2.describe())
    print(' fight!')
    print(factor1.attack())
    print(factor2.attack())
    print()


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    test_factory(aqua)
    battle(flame, aqua)


if __name__ == "__main__":
    main()
