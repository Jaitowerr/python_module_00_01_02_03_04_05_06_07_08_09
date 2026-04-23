#! /usr/bin/env python3

from collections.abc import Callable
import time
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f' - Casting {func.__name__}...')
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f' --- Spell completed in {elapsed:.3f} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def func_wrap(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power', args[0] if args else None)
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return 'Insufficient power for this spell'
        return wrapper
    return func_wrap


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def func_wrap(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempts in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        'Spell failed, retrying... '
                        f'(attempt {attempts}/{max_attempts})')
            return f'Spell casting failed after {max_attempts} attempts'
        return wrapper
    return func_wrap


class MageGuild:

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(' ', '').isalpha()


if __name__ == '__main__':
    print('\nTesting spell timer...')

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.101)
        return f'Fireball cast! - {target}'
    result = fireball('Dragon')
    print(f' - Result: {result}')

    print('\nTesting power validator...')

    @power_validator(10)
    def cast_lightning(power: int, target: str) -> str:
        return f'Lightning hits {target} for {power} damage'

    print(f' - Valid: {cast_lightning(15, "Dragon")}')
    print(f' - Invalid: {cast_lightning(5, "Dragon")}')

    print('\nTesting retrying spell...')

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception('Spell backfired!')

    print(unstable_spell())

    print('-' * 20)
    counter = [0]

    @retry_spell(3)
    def lucky_spell() -> str:
        counter[0] += 1
        if counter[0] < 3:
            raise Exception()
        return 'Waaaaaaagh spelled !'

    print(lucky_spell())

    print('\nTesting MageGuild - cast_spell...')
    guild = MageGuild()
    print(guild.cast_spell('Lightning', power=15))
    print(guild.cast_spell('Fireball', power=5))
    print('-' * 20)
    print('Testing power validator...')
    print(cast_lightning(power=15, target='Dragon'))
    print(cast_lightning(power=5, target='Dragon'))
