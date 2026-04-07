#! /usr/bin/env python3

import random

all_achievements = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
]


def gen_player_achievements() -> set:

    amount = random.randint(6, 14)
    set_achievement = set(random.sample(all_achievements, amount))
    return set_achievement


def main() -> None:
    print('=== Achievement Tracker System ===')
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f'\nPlayer Alice: {alice}'
          f'\nPlayer Bob: {bob}'
          f'\nPlayer Charlie: {charlie}'
          f'\nPlayer Dylan: {dylan}'
          )

    all_distinct_archievements = alice.union(bob).union(charlie).union(dylan)
    print(f'\nAll distinct achievements: {all_distinct_archievements}')

    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f'\nCommon achievements: {common}')

    only_alice = alice.difference(bob.union(charlie).union(dylan))
    only_bob = bob.difference(alice.union(charlie).union(dylan))
    only_charlie = charlie.difference(alice.union(bob).union(dylan))
    only_dylan = dylan.difference(alice.union(bob).union(charlie))

    print(f'\nOnly Alice has: {only_alice}'
          f'\nOnly Bob has: {only_bob}'
          f'\nOnly Charlie has: {only_charlie}'
          f'\nOnly Dylan has: {only_dylan}')

    set_archivements = set(all_achievements)
    missing_alice = set_archivements.difference(alice)
    missing_bob = set_archivements.difference(bob)
    missing_charlie = set_archivements.difference(charlie)
    missing_dylan = set_archivements.difference(dylan)

    print(f'\nAlice is missing: {missing_alice}'
          f'\nBob is missing: {missing_bob}'
          f'\nCharlie is missing: {missing_charlie}'
          f'\nDylan is missing: {missing_dylan}'
          )


if __name__ == '__main__':
    main()
