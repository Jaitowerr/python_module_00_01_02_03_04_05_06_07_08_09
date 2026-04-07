#! /usr/bin/env python3

import random


def main() -> None:
    print('=== Game Data Alchemist ===\n')
    players = ['Alice',
               'bob',
               'Charlie',
               'dylan',
               'Emma',
               'Gregory',
               'john',
               'kevin',
               'Liam']
    print(f'Initial list of players: {players}\n')

    players_capitalize = [player.capitalize() for player in players]
    print(f'New list with all names capitalized: {players_capitalize}\n')

    origin_pyr_capi = [player for player in players
                       if player == player.capitalize()]
    print(f'New list of capitalized names only: {origin_pyr_capi}\n')

    dict_players = {player: random.randint(1, 1000)
                    for player in players_capitalize}
    print(f'Diccionario de puntuaciones: {dict_players}\n')

    average_score = round(sum(dict_players.values()) / len(dict_players), 2)
    print(f'Score average is {average_score}\n')

    high_score = {player: dict_players[player] for player in dict_players
                  if dict_players[player] > average_score}
    print(f'High scores: {high_score}')


if __name__ == '__main__':
    main()
