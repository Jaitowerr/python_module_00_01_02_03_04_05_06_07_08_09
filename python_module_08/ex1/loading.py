#! /usr/bin/env python3
'''
pip install pandas numpy matplotlib
'''
import importlib


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
    except ModuleNotFoundError:
        print(f'  *** [KO] {name_lib} - Library not found.')
        return False


def check_versions(lib: list[str] | str) -> tuple[bool, list[str]]:
    result = []
    lib_not_version = []

    if isinstance(lib, list):
        for name_lib in lib:
            try:
                # if not isinstance(name_lib, str):
                # raise TypeError(f'{name_lib} is not a valid string.')
                if isinstance(name_lib, str):
                    find_out = print_version(name_lib)
                    result.append(find_out)
                    if not find_out:
                        lib_not_version.append(name_lib)
                else:
                    raise TypeError(f'{name_lib} is not a valid string.')

            except TypeError as e:
                print(f'  *!!* [KO] {e}')

    elif isinstance(lib, str):
        find_out = print_version(lib)
        result.append(find_out)
        if not find_out:
            lib_not_version.append(lib)

    else:
        raise TypeError('Argument must be str or list[str].')

    return all(result), lib_not_version


def help_install(lib_not_version: list[str]) -> None:
    libs = ' '.join(lib_not_version)
    print('\nTo install missing dependencies:')
    print('\n  With pip:')
    for lib in lib_not_version:
        print(f'    pip install {lib}')
    print('\n  With Poetry:')
    for lib in lib_not_version:
        print(f'    poetry add {lib}')


def start_program():
    import pandas as pd
    import numpy as np
    import requests as rq
    import matplotlib.pyplot as mplt

    print("Analyzing Matrix data...")
    data = np.random.randint(0, 100, 1000)

    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=["values"])
    print(df.describe())

    # matplotlib
    print("Generating visualization...")
    # mplt.hist(df["values"], bins=20) #barras
    mplt.hist(df["values"]) #lineal
    mplt.title("Matrix Data Analysis")
    mplt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == '__main__':
    lib = ['pandas', 'numpy', 'requests', 'matplotlib', 444]

    print('\nLOADING STATUS: Loading programs...\n')
    print('Checking dependencies:')
    ok, lib_not_version = check_versions(lib)
    if ok:
        print('All dependencies OK. Starting program...')
        start_program()
    else:
        print('\nMissing dependencies. Aborting.')
        if lib_not_version:
            help_install(lib_not_version)
        # exit(1)
