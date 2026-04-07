#! /usr/bin/env python3

import sys


def dict_errors(list_argv: list) -> dict:
    dict_argv = dict()
    for i in list_argv:
        try:
            split_i = i.split(':')
            if len(split_i) != 2:
                raise ValueError(f'''- invalid parameter '{i}' '''
                                 '<key>:<value>')
            clave = str(split_i[0])
            valor = int(split_i[1])
            if clave in dict_argv:
                raise ValueError(f'''Redundant item '{clave}' - discarding''')
            if valor <= 0:
                raise ValueError(f'Invalid value for {clave}:'
                                 f'{valor} (must be > 0)')
            dict_argv.update({clave: valor})

        except ValueError as e:
            print(f'******* Error type: {e} *******')
    return dict_argv


def print_values(dict_argv: dict, total_values: int) -> None:
    percentage = 100/total_values
    max_percentage = 0.00
    min_percentage = 100.00

    for clave in dict_argv:
        valor = dict_argv[clave]
        indi_percentage = round(valor * percentage, 2)
        print(f' - Item {clave.capitalize()} represents: {indi_percentage} %')
        if indi_percentage > max_percentage:
            name_max, value_name_max = clave, valor
            max_percentage = indi_percentage
        if indi_percentage <= min_percentage:
            name_min, value_name_min = clave, valor
            min_percentage = indi_percentage

    print(f'Item most abundant: {name_max.capitalize()} with'
          f' quanty {value_name_max}')
    print(f'Item least abundant: {name_min.capitalize()} with'
          f' quantity {value_name_min}')


def main() -> None:
    print('=== Análisis del Sistema de Inventario ===')
    dict_argv = dict()

    if len(sys.argv[1:]) >= 1:
        list_argv = sys.argv[1:]
        dict_argv = dict_errors(list_argv)
        if dict_argv:

            print(f'\nGot inventory: {dict_argv}')

            dict_keys = list(dict.keys(dict_argv))
            print(f'Item list: {dict_keys}')

            total_values = sum(dict.values(dict_argv))
            print(f'\nTotal quantity of the {len(dict_keys)} '
                  f'items: {total_values}')
            print_values(dict_argv, total_values)

    else:
        print('****Enter elements <key>:<value>')
    dict_argv.update({'magic_item': 1})
    print(f'\nUpdated inventory: {dict_argv}')


if __name__ == '__main__':
    main()
