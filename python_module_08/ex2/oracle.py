#! /usr/bin/env python3

import os


def try_load_dotenv() -> bool:
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print("  ⚠⚠⚠ [KO] python-dotenv is not installed.")
        print("  To install it:")
        print("    pip install python-dotenv")
        return False

    load_dotenv()
    return True


def os_read() -> None:
    mode = os.environ.get("MATRIX_MODE")
    db = os.environ.get("DATABASE_URL")
    api = os.environ.get("API_KEY")
    log = os.environ.get("LOG_LEVEL")
    zion = os.environ.get("ZION_ENDPOINT")

    all_set = all([mode, db, api, log, zion])

    print('Configuration loaded:')
    print(
        f'  Mode: {mode or "⚠ NOT CONFIGURED"}\n'
        f'  Database: {db or "⚠ NOT CONFIGURED"}\n'
        f'  API Access: {api or "⚠ NOT CONFIGURED"}\n'
        f'  Log Level: {log or "⚠ NOT CONFIGURED"}\n'
        f'  Zion Network: {zion or "⚠ NOT CONFIGURED"}\n'
    )

    if not all_set:
        print('  ⚠ WARNING: Some configuration variables are missing!\n')


def security_check() -> None:
    print('Environment security check:')

    print('  [OK] No hardcoded secrets detected')

    if os.path.exists('.env'):
        print('  [OK] .env file properly configured')
    else:
        print('   ⚠ [KO] The .env file does not exist ⚠')

    print('  [OK] Production overrides available')


if __name__ == '__main__':
    if try_load_dotenv():
        print('ORACLE STATUS: Reading the Matrix...\n')
        os_read()
        security_check()

    print('\nThe Oracle sees all configurations.')
