#! /usr/bin/env python3

from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        dato1 = spell1(target, power)
        dato2 = spell2(target, power)
        return (dato1, dato2)
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return 'Spell fizzled'
    return caster


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for _ in spells:
            results.append(_(target, power))
        return results
    return sequence


if __name__ == '__main__':
    test_values = [10, 6, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power > 5

    def is_powerful_goblin(target: str, power: int) -> bool:
        return target == 'Goblin' and power > 5

    print('\n===== TEST SPELL_COMBINER =====')
    combined = spell_combiner(fireball, heal)
    result = combined(test_targets[0], test_values[0])
    print(f'Combined spell result: {result[0]}, {result[1]}\n')

    print('\n===== TEST POWER_AMPLIFIER =====')
    multi = 4
    mega_fireball = power_amplifier(fireball, multi)
    print(f'Original: {fireball(test_targets[0], test_values[0])}')
    print(
        f'Amplified {multi}: {mega_fireball(test_targets[0], test_values[0])}')
    print()

    print('\n===== TEST CONDITIONAL_CASTER =====')
    conditional = conditional_caster(is_powerful, fireball)
    print(
        f'Power 10: {conditional(test_targets[0], test_values[0])}')
    print(f'Power 3: {conditional(test_targets[0], 3)}\n')
    conditional2 = conditional_caster(is_powerful_goblin, fireball)
    print(
        f'Power 10, Dragon: {conditional2(test_targets[0], test_values[0])}')
    print(
        f'Power 10, Globin: {conditional2(test_targets[1], test_values[0])}')
    print(f'Power 3, Globin: {conditional2(test_targets[0], 3)}\n')

    print('\n===== TEST SPELL_SEQUENCE =====')
    sequence = spell_sequence([fireball, heal])
    results = sequence(test_targets[0], test_values[0])
    print(f'Sequence results: {results}\n')
