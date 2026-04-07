#! /usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb',
               'swim', 'use', 'release']
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(list_event: list) -> typing.Generator:
    while len(list_event) > 0:
        remove_event = random.choice(list_event)
        index = 0
        for event in list_event:
            if event == remove_event:
                break
            index += 1
        list_event = list_event[:index] + list_event[index + 1:]
        print(f'Got event from list: {event}')
        yield list_event


def main() -> None:
    gen = gen_event()

    for i in range(1000):
        event = next(gen)
        print(f'Event {i}: Player {event[0]} did action {event[1]}')

    list_event = list()
    for i in range(10):
        list_event += [next(gen)]
    print(f'\nBuilt list of 10 events: {list_event}')

    for list_event in consume_event(list_event):
        print(f'Remains in list: {list_event}')


if __name__ == '__main__':
    main()
