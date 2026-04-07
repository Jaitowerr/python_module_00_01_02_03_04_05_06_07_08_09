#! /usr/bin/env python3

import math


def formula_math(tupla1: tuple, tupla2: tuple = (0, 0, 0)) -> float:
    x1, y1, z1 = tupla1[0], tupla1[1], tupla1[2]
    x2, y2, z2 = tupla2[0], tupla2[1], tupla2[2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def get_player_pos() -> tuple:
    input_entrada = input(' - Enter coordinates: ')
    parametres = 0
    try:
        partes_input_entrada = input_entrada.split(',')
        for i in partes_input_entrada:
            parametres += 1
            try:
                i_float = float(i)
            except ValueError:
                raise ValueError(f'''Parametr '{i}' '''
                                 'is not a valid number')
            if i_float < 0 or i_float > 100:
                raise ValueError('Coordinates must be between 0 and 100')
        if parametres != 3:
            raise ValueError('Exactly three coordinates are required')
            # i += 0.00
    except ValueError as e:
        print(f'Invalid syntax: {e}')
        return get_player_pos()
    return (float(partes_input_entrada[0]),
            float(partes_input_entrada[1]),
            float(partes_input_entrada[2]))


def main() -> None:
    print('\n========================================\n'
          '=== Sistema de Coordenadas del Juego ===\n'
          '========================================')
    print('Enter three coordinates separated by a '','' in format x,y,z')

    print('Get a first set of coordinates')
    tupla = get_player_pos()
    print(f'Got a first tuple: {tupla}\n'
          f'It includes: x: {tupla[0]}, y: {tupla[1]}, z: {tupla[2]}')
    distance = formula_math(tupla)
    print(f'---- Distance from center: {round(distance, 4)}')

    print('')

    print('Get a second set of coordinates')
    tupla2 = get_player_pos()
    print(f'Got a second tuple: {tupla2}\n'
          f'It includes: x: {tupla2[0]}, y: {tupla2[1]}, z: {tupla2[2]}')
    distance = formula_math(tupla, tupla2)
    print(f'Distance between the 2 sets of coordinates: {round(distance, 4)}')


if __name__ == '__main__':
    main()
