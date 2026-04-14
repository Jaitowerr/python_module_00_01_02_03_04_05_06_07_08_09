import alchemy

try:
    print('=== Transmutation 2 ===')
    print('Import alchemy module only')
    print(f'Testing lead to gold: {alchemy.lead_to_gold()}\n')

except Exception as e:
    print(f' - ERROR EN FT_TRANSMUTATION_2: {e}\n')
