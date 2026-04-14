import alchemy

print('=== Alembic 4 ===')
print('Accessing the alchemy module using \'import alchemy\'')

try:
    print(f'Testing create_air: {alchemy.create_air()}')
except (Exception, AttributeError) as e:
    print(f' - Exception caught: {e}\n')

print('Now show that not all functions can be reached')
print('This will raise an exception!')

try:
    print(f'Testing the hidden create_earth: {alchemy.create_earth()}')
except AttributeError as e:
    print(f' - Exception caught: {e}\n')
