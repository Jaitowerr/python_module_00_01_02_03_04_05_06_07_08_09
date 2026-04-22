#! /usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'
    return factory


def memory_vault() -> dict[str, Callable[..., object]]:
    vault = {}

    def store(key: str, value: object) -> None:
        vault[key] = value

    def recall(key: str) -> object:
        return vault.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


if __name__ == '__main__':

    print('\n===== TEST MAGE_COUNTER =====')
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f'counter_a call 1: {counter_a()}')
    print(f'counter_a call 2: {counter_a()}')
    print(f'counter_b call 1: {counter_b()}')
    print(f'counter_b call 1: {counter_b()}')
    print(f'counter_a call 1: {counter_a()}\n')

    print('\n===== TEST SPELL_ACCUMULATOR =====')
    accumulator = spell_accumulator(100)
    print(f'Base 100 + 20: {accumulator(20)}')
    print(f'Base acumulated + 30: {accumulator(30)}\n')

    print('\n===== TEST ENCHANTMENT_FACTORY =====')
    flaming = enchantment_factory('Flaming')
    frozen = enchantment_factory('Frozen')
    print(flaming('Sword'))
    print(frozen('Shield'), '\n')

    print('\n===== TEST MEMORY_VAULT =====')
    my_vault = memory_vault()
    store_func = my_vault['store']
    recall_func = my_vault['recall']
    store_func('secret', 42)
    print(f'Store "secret": {recall_func("secret")}')
    store_func('hero', 'Gandalf')
    print(f'Recall "hero": {recall_func("hero")}')
    print(f'Recall "unknown": {recall_func("unknown")}\n')
