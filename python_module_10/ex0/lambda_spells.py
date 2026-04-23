#! /usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: -artifact['power'])


def power_filter(
        mages: list[dict[str, Any]], min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    maxx = max(mages, key=lambda x: x['power'])
    minn = min(mages, key=lambda x: x['power'])
    avg = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': maxx['power'],
        'min_power': minn['power'],
        'avg_power': avg}


if __name__ == '__main__':

    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Shadow Cloak', 'power': 60, 'type': 'armor'},
        {'name': 'Thunder Shield', 'power': 78, 'type': 'armor'},
        {'name': 'Ancient Tome', 'power': 5, 'type': 'book'},
    ]
    print('Testing artifact sorter...')

    art_sorted = artifact_sorter(artifacts)
    print(f' - {art_sorted[0]["name"]} ({art_sorted[0]["power"]}'
          f' power) comes before {art_sorted[1]["name"]} '
          f'({art_sorted[1]["power"]} power)')

    print('\n', '-' * 40)
    mages = [
        {'name': 'Alex', 'power': 15, 'element': 'fire'},
        {'name': 'Jordan', 'power': 45, 'element': 'water'},
        {'name': 'Riley', 'power': 70, 'element': 'earth'},
    ]
    print('Testing filter sorter...')
    min_pwr_mg = len(mages) - 1
    mages = artifact_sorter(mages)
    # filtered = power_filter(mages, mages[-1]['power'])
    filtered = power_filter(mages, 50)
    print(' -', filtered)

    print('\n', '-' * 40)
    print('Testing map...')
    spells = ['fireball', 'heal', 'shield']
    spells = spell_transformer(spells)
    print('-', ' '.join(spells))

    print('\n', '-' * 40)
    print('Testing sum, min avg...')
    print(mage_stats(mages))
    print(
        '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', mage_stats(mages).items())))
