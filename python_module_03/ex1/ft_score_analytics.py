#! /usr/bin/env python3
import sys


def score(list_argv: list) -> None:
    score_processed = list_argv
    total_players = len(score_processed)
    total_score = sum(score_processed)
    avg_score = total_score / total_players
    high_score = max(score_processed)
    low_score = min(score_processed)
    score_range = high_score - low_score

    print(f'  - Scores processed: {score_processed}')
    print(f'  - Total players: {total_players}')
    print(f'  - Total score: {total_score}')
    print(f'  - Average score: {avg_score}')
    print(f'  - High score: {high_score}')
    print(f'  - Low score: {low_score}')
    print(f'  - Score range: {score_range}')


def main() -> None:
    print('\n==============================\n'
          '=== Player Score Analytics ===\n'
          '===============================\n')
    list_argv = sys.argv
    size_list = len(list_argv[1:])
    score_validos = []

    for i in list_argv[1:]:
        try:
            score_validos += [int(i)]
        except ValueError as e:
            print(f'Invalid parameter: {i}')

    if len(score_validos) >= 1:
        score(score_validos)
    else:
        print(f'  *** No scores provided. Usage: python3 {sys.argv[0]} '
        '<score1> <score2> ...')


if __name__ == '__main__':
    main()
