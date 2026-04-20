#! /usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional, Type, Any


class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':
        errors = []
        if not self.contact_id.startswith('AC'):
            errors.append(' ⚠  Contact ID must start with AC')
        if self.contact_type == ContactType.physical and not self.is_verified:
            errors.append(' ⚠  Physical contact reports must be verified')
        elif (self.contact_type == ContactType.telepathic
              and self.witness_count < 3):
            errors.append(
                ' ⚠  Telepathic contact requires at least 3 witnesses')
        if self.signal_strength > 7.0 and not self.message_received:
            errors.append(
                ' ⚠  Strong signals should include received messages')
        if errors:
            raise ValueError('\n'.join(errors))
        return self


def main(object_space: Type[AlienContact], values: dict[str, Any]) -> None:
    try:
        alien = object_space(**values)
        print('\n', 60 * '=')
        print('Valid contact report:')
        print(f'  ID: {alien.contact_id}')
        print(f'  Type: {alien.contact_type.value}')
        print(f'  Location: {alien.location}')
        print(f'  Signal: {alien.signal_strength}/10')
        print(f'  Duration: {alien.duration_minutes} minutes')
        print(f'  Witnesses: {alien.witness_count}')
        print(f'  Message: {alien.message_received}')

    except ValidationError as e:
        id = values.get('contact_id', 'Unknown id contact')
        print('\n', 60 * '=')
        print(f'Expected validation error for {id}')
        for error in e.errors():
            print(error['msg'].replace('Value error, ', ''))


if __name__ == '__main__':
    print('Alien Contact Log Validation')

    value_valid = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-15T10:30:00',
        'location': 'Area 51, Nevada',
        'contact_type': ContactType.radio,
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }
    main(AlienContact, value_valid)

    value_invalid = {
        'contact_id': 'Ac_2024_002',
        'timestamp': '2024-01-15T11:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': ContactType.telepathic,
        'signal_strength': 5.0,
        'duration_minutes': 30,
        'witness_count': 1,
        'is_verified': False
    }
    main(AlienContact, value_invalid)

    value_invalid2 = {
        'contact_id': 'XX001',
        'timestamp': '2024-01-15T11:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': ContactType.physical,
        'signal_strength': 9.0,
        'duration_minutes': 30,
        'witness_count': 1,
        'is_verified': False
    }

    main(AlienContact, value_invalid2)
