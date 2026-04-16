#! /usr/bin/env python3

import sys
import os
import site


def inform_matrix_venv() -> None:

    en_venv = sys.prefix != sys.base_prefix
    python_path = sys.executable
    venv_path = os.environ.get("VIRTUAL_ENV")
    venv_name = os.path.basename(venv_path) if venv_path else "None detected"
    pkg_path = site.getsitepackages()[0] if en_venv else None

    if en_venv:
        matrix_status = 'Welcome to the construct'
        warning = (
            '\nSUCCESS: You\'re in an isolated environment!\n'
            'Safe to install packages without affecting the global system.\n'
            )

    else:
        matrix_status = 'You\'re still plugged in'
        warning = ('\nWARNING: You\'re in the global environment!\n'
                   'The machines can see everything you install.\n')

        instruction = (
            'To enter the construct, run:\n'
            '  - Install: python3 -m venv matrix_env\n'
            '   - Activate:\n'
            '       * source matrix_env/bin/activate # On Unix\n'
            '       * matrix_env\\Scripts\\activate # On Windows\n'
            '    - Deactivate: Para desactivar ejecute \'deactivate\''
            )

    print('\nMATRIX STATUS:', matrix_status)

    print('\nCurrent Python:', python_path)
    print('Virtual Environment:', venv_name)

    if en_venv:
        print('Environment Path:', venv_path)

    print(warning)

    if not pkg_path:
        print(instruction, '\n')
        print('Then run this program again.')
    else:
        print('Package installation path:\n', pkg_path)


if __name__ == '__main__':
    inform_matrix_venv()
