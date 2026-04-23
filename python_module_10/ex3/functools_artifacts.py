#! /usr/bin/env python3

from collections.abc import Callable
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    try:
        if operation == 'add':
            return reduce(add, spells)
        elif operation == 'multiply':
            return reduce(mul, spells)
        elif operation == 'max':
            return reduce(max, spells)
        elif operation == 'min':
            return reduce(min, spells)
        else:
            raise TypeError

    except TypeError as e:
        print(f'** Operation --{operation}-- is unknown {e}:')
        return -1


def partial_enchanter(
        base_enchantment: Callable[..., str]) -> dict[str, Callable[..., str]]:
    return {
        'fire': partial(base_enchantment, power=50, element="fire"),
        'ice': partial(base_enchantment, power=50, element="ice"),
        'thunder': partial(base_enchantment, power=50, element="thunder")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    try:
        if n < 0:
            raise ValueError('n must be a non-negative integer')
        if n <= 1:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except ValueError as e:
        print('** Fibonacci error:', e)
        return -1


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_type(value: Any) -> str:
        return 'Unknown'

    @base_type.register(int)
    def _(value: int) -> str:
        return f"Damage spell cast with power {value}"

    @base_type.register(str)
    def _(value: str) -> str:
        return f"Enchantment spell cast on {value}"

    @base_type.register(list)
    def _(value: list[Any]) -> str:
        return f"Multi-cast spell with {len(value)} spells"

    return base_type


if __name__ == '__main__':

    print('\n===== TEST SPELL_REDUCER =====')
    list_spells = [10, 20, 30, 40]
    print(f' - Sum: {spell_reducer(list_spells, "add")}')
    print(f' - Product: {spell_reducer(list_spells, "multiply")}')
    print(f' - Max: {spell_reducer(list_spells, "max")}')
    print(f' - Min: {spell_reducer(list_spells, "min")}')
    print(f' - Empty: {spell_reducer([], "add")}')
    print(f' - Unknown: {spell_reducer(list_spells, "unknown")}')

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f'{element} hits {target} for {power} damage'

    print('\n===== TEST PARTIAL_ENCHANTER =====')
    enchants = partial_enchanter(base_enchantment)
    try:
        print(f' - Fire: {enchants["fire"](target="Dragon")}')
        print(f' - Ice: {enchants["ice"](target="Goblin")}')
        print(f' - Thunder: {enchants["thunder"](target="Wizard")}')
        print(f' - Water: {enchants["water"](target="Knight")}')
    except KeyError as e:
        print(f'** Element {e} not found')

    print('\n===== TEST MEMOIZED_FIBONACCI =====')
    print(f' - FFib(0): {memoized_fibonacci(0)}')
    print(f' - FFib(1): {memoized_fibonacci(1)}')
    print(f' - FFib(10): {memoized_fibonacci(10)}')
    print(f' - FFib(15): {memoized_fibonacci(15)}')
    print(f' -- FCache info: {memoized_fibonacci.cache_info()}')
    print(f' - FFib(10): {memoized_fibonacci(10)}')
    print(f' -- FCache info: {memoized_fibonacci.cache_info()}')
    print('    -->  Clear  lru_cache <--')
    memoized_fibonacci.cache_clear()
    print(f' -- FCache info: {memoized_fibonacci.cache_info()}')
    print(f' - FFib(1): {memoized_fibonacci(1)}')
    print(f' -- FCache info: {memoized_fibonacci.cache_info()}')

    print('\n===== TEST SPELL_DISPATCHER =====')
    spell = spell_dispatcher()
    print(spell(42))
    print(spell('fireball'))
    print(spell([10, 20, 30]))
    print(spell(3.14))
