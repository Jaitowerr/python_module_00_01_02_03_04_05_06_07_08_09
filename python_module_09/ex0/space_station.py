#! /usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Type, Any


class SpaceStation(BaseModel):

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main(object_space: Type[SpaceStation], values: dict[str, Any]) -> None:
    try:

        station = object_space(**values)
        print(
            '\n',
            60 * '=')
        print('Valid station created:')
        print(f'  ID: {station.station_id}')
        print(f'  Name: {station.name}')
        print(f'  Crew: {station.crew_size} people')
        print(f'  Power: {station.power_level}%')
        print(f'  Oxygen: {station.oxygen_level}%')
        status = 'Operational' if station.is_operational else 'Offline'
        print(f'  Status: {status}')
    except ValidationError as e:
        name = values.get('name', 'Unknown Name Statio')
        id = values.get('station_id', 'Unknown id station')
        print('\n', 60 * '=')
        print(f'Expected validation error for {name} ({id})')
        for error in e.errors():
            print(error['msg'])


if __name__ == '__main__':

    print('Space Station Data Validation')

    value_valid = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 6,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2024-01-15T10:30:00',
        'notes': 'All systems nominal'
    }
    main(SpaceStation, value_valid)

    value_invalid = {
        'station_id': 'BAD01',
        'name': 'Broken Station',
        'crew_size': 999,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2024-01-15T10:30:00',
    }
    main(SpaceStation, value_invalid)
