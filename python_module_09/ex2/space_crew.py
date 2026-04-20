#! /usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from typing import List, Type, Any
from datetime import datetime


class Rank(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = 'planned'
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_rules(self) -> 'SpaceMission':
        errors = []
        if not self.mission_id.startswith('M'):
            errors.append(' ⚠  Contact ID must start with M')
        if not any(com_cap.rank in [Rank.commander, Rank.captain]
                   for com_cap in self.crew):
            errors.append(
                ' ⚠  Mission must have at least one Commander or Captain')
        if not all(members.is_active for members in self.crew):
            errors.append(' ⚠  All crew members must be active')
        if self.duration_days > 365:
            experiencie = 0
            for members in self.crew:
                if members.years_experience >= 5:
                    experiencie += 1
            if experiencie < len(self.crew) / 2:
                errors.append(
                    ' ⚠  Long missions need 50% experienced crew (5+ years)')
        if errors:
            raise ValueError('\n'.join(errors))
        return self


def main(object_space: Type[SpaceMission], values: dict[str, Any]) -> None:
    try:
        mission = object_space(**values)
        print('\n', 60 * '=')
        print('Valid mission created:')
        print(f'  Mission: {mission.mission_name}')
        print(f'  ID: {mission.mission_id}')
        print(f'  Destination: {mission.destination}')
        print(f'  Duration: {mission.duration_days} days')
        print(f'  Budget: ${mission.budget_millions}M')
        print(f'  Crew size: {len(mission.crew)}')
        print('  Crew members:')
        for member in mission.crew:
            print(f'    - {member.name} ({member.rank.value})'
                  f' - {member.specialization}')
    except ValidationError as e:
        name = values.get('mission_name', 'Unknown Mission')
        id = values.get('mission_id', 'Unknown ID')
        print('\n', 60 * '=')
        print(f'Expected validation error for {name} ({id}):')
        for error in e.errors():
            print(error['msg'].replace('Value error, ', ' '))


if __name__ == '__main__':
    value_valid = {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': '2024-01-15T10:30:00',
        'duration_days': 900,
        'budget_millions': 2500.0,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Connor',
                'rank': 'commander',
                'age': 45,
                'specialization': 'Mission Command',
                'years_experience': 20,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': 35,
                'specialization': 'Navigation',
                'years_experience': 10,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Engineering',
                'years_experience': 6,
                'is_active': True
            }
        ]
    }
    main(SpaceMission, value_valid)

    value_invalid = {
        'mission_id': 'M2024_FAIL',
        'mission_name': 'Doomed Mission',
        'destination': 'Venus',
        'launch_date': '2024-01-15T10:30:00',
        'duration_days': 30,
        'budget_millions': 100.0,
        'crew': [
            {
                'member_id': 'CM010',
                'name': 'Bob Cadet',
                'rank': 'cadet',
                'age': 22,
                'specialization': 'Cleaning',
                'years_experience': 1,
                'is_active': True
            }
        ]
    }
    main(SpaceMission, value_invalid)

    value_invalid2 = {
        'mission_id': 'M2024_FAIL',
        'mission_name': 'Doomed Mission',
        'destination': 'Venus',
        'launch_date': '2024-01-15T10:30:00',
        'duration_days': 500,
        'budget_millions': 100.0,
        'mission_status': 'planned',
        'crew': [
            {
                'member_id': 'CM010',
                'name': 'Bob Cadet',
                'rank': 'cadet',
                'age': 22,
                'specialization': 'Cleaning',
                'years_experience': 2,
                'is_active': True
            },
            {
                'member_id': 'CM011',
                'name': 'Alice Cadet',
                'rank': 'lieutenant',
                'age': 25,
                'specialization': 'Navigation',
                'years_experience': 1,
                'is_active': False
            }
        ]
    }
    main(SpaceMission, value_invalid2)

    value_invalid3 = {
        'mission_id': 'M2024_CREW',
        'mission_name': 'Broken Crew Mission',
        'destination': 'Mars',
        'launch_date': '2024-01-15T10:30:00',
        'duration_days': 30,
        'budget_millions': 500.0,
        'mission_status': 'planned',
        'crew': [
            {
                'member_id': 'CM020',
                'name': 'A',  # X
                'rank': 'commander',
                'age': 40,
                'specialization': 'Navigation',
                'years_experience': 10,
                'is_active': True
            },
            {
                'member_id': 'CM021',
                'name': 'John Smith',
                'rank': 'captain',
                'age': 15,  # X
                'specialization': 'Engineering',
                'years_experience': 10,
                'is_active': True
            },
            {
                'member_id': 'CM022',
                'name': 'Alice Brown',
                'rank': 'lieutenant',
                'age': 30,
                'specialization': 'AB',  # X
                'years_experience': 10,
                'is_active': True
            },
            {
                'member_id': 'CM023',
                'name': 'Bob Jones',
                'rank': 'officer',
                'age': 35,
                'specialization': 'Research',
                'years_experience': 99,  # X
                'is_active': True
            }
        ]
    }

    main(SpaceMission, value_invalid3)
