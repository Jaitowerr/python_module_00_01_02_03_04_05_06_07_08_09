#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:

    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f'{temp}°C is too cold for plants (min 0°C)')
    if temp > 40:
        raise ValueError(f'{temp}°C is too hot for plants (max 40°C)')

    return temp


def test_temperature() -> None:
    print('=== Garden Temperature ===')
    temp_str = ['25', 'abc', '100', '-50']
    for i in temp_str:
        print(f'''\nInput data is '{i}' ''')
        try:
            temp = input_temperature(i)
            print(f'Temperature is now {temp}°C')
        except ValueError as e:
            print(f'Caught input_temperature error: {e}')

    print('\nAll tests completed - program didn''t crash!')


if __name__ == '__main__':
    test_temperature()
