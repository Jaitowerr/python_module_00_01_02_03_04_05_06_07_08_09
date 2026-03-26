#! /usr/bin/env python3

def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int('abc')

    elif operation_number == 1:
        10 / 0

    elif operation_number == 2:
        open('../archivo_que_no_existe.pdf')

    elif operation_number == 3:
        'Hola' + 42  # type: ignore


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===")

    for i in range(5):

        try:
            print(f'  Testing operation {i}...')
            garden_operations(i)
            print('   - Operation completed successfully\n')

        except (ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError) as e:
            print(f'   - Caught {e.__class__.__name__}: {e}\n')

    print('All error types tested successfully!')


if __name__ == '__main__':
    test_error_types()
