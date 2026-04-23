#! /usr/bin/env python3

from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    pass


def power_validator(min_power: int) -> Callable:
    pass


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass












if __name__ == '__main__':
    pass