from elements import create_water

try:
    print('=== Alembic 1 ===')
    print('Using: \'from ... import ...\' structure to access elements.py')
    print(f'Testing create_water: {create_water()}\n')

except Exception:
    print(' - ERROR EN FT_ALEMBIC_1')
