#! /usr/bin/env python3

import sys
import importlib


def help_env() -> None:
    print('\nWARNING: Virtual environment not detected!')
    print('It is recommended to use a virtual environment.\n')

    print('  Option 1: With pip:')
    print('    python3 -m venv matrix_env')
    print('    source matrix_env/bin/activate')
    print('    pip install -r requirements.txt')

    print('\n  Option 2: With Poetry:')
    print('     poetry install && poetry run python loading.py')


def print_version(name_lib: str) -> bool:
    sms = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready',
        'requests': 'Network access ready',
    }
    try:
        modulo = importlib.import_module(name_lib)
        version = modulo.__version__
        mensaje = sms.get(name_lib, 'Library installed correctly')
        if mensaje:
            print(f'  - [OK] {name_lib} ({version}) - {mensaje}')
        return True
    except (ModuleNotFoundError, ImportError, AttributeError, Exception):
        print(f'  *** [KO] {name_lib} - Library not found.')
        return False


def check_versions(lib: list[str]) -> tuple[bool, list[str]]:
    result = []
    lib_not_version = []

    if isinstance(lib, list):
        for name_lib in lib:
            try:
                if isinstance(name_lib, str):
                    find_out = print_version(name_lib)
                    result.append(find_out)
                    if not find_out:
                        lib_not_version.append(name_lib)
                else:
                    raise TypeError(f'{name_lib} is not a valid string.')

            except TypeError as e:
                print(f'  *!!* [KO] {e}')

    else:
        raise TypeError('Argument must be str or list[str].')

    return all(result), lib_not_version


def help_install(lib_not_version: list[str]) -> None:
    print('\nTo install missing dependencies:')
    print('\n  With pip:')
    for lib in lib_not_version:
        print(f'    pip install {lib}')
    print('\n  With Poetry:')
    for lib in lib_not_version:
        print(f'    poetry add {lib}')


def start_program() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as mplt

    print("\nAnalyzing Matrix data...")
    data = np.random.randint(0, 100, 1000)

    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=["values"])
    print(df.describe())

    print("Generating visualization...\n")
    # mplt.hist(df["values"], bins=20) #barras
    mplt.plot(sorted(df["values"]))  # lineal
    mplt.title("Matrix Data Analysis")
    mplt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == '__main__':
    lib = ['pandas', 'numpy', 'matplotlib']

    in_venv = sys.prefix != sys.base_prefix

    print('\nLOADING STATUS: Loading programs...\n')
    if not in_venv:
        help_env()
    else:
        print('Checking dependencies:')
        ok, lib_not_version = check_versions(lib)
        if ok:
            print('All dependencies OK. Starting program...')
            start_program()
        else:
            print('\nMissing dependencies. Aborting.')
            if lib_not_version:
                help_install(lib_not_version)
