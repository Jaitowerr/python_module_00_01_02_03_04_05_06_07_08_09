#! /usr/bin/env python3
import sys


def main() -> None:
    list_argv = sys.argv
    print('======================\n'
          '=== Command Quest ===\n'
          '======================\n'
          '\n'
          f'  - Programa name: {list_argv[0]}')

    len_list = len(list_argv)

    if len_list > 1:
        print(f'  - Arguments received: {len_list - 1}')
        count = 1
        for key in list_argv[1:]:
            print(f'  - Argument {count}: {key}')
            count += 1

    else:
        print('No arguments provided!')

    print('\n--------------------------\n'
          f'------- Total arguments: {len_list}\n'
          '--------------------------')


if __name__ == '__main__':
    main()
