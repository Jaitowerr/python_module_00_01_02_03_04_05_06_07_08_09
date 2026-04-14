print('=== Kaboom 1 ===')
print('Access to alchemy/grimoire/dark_spellbook.py directly')
print('Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION')

try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    dark_spell_record("Shadow Curse", "bats and frogs")

except Exception as e:
    print('Traceback (most recent call last):')
    print(f' - Exception caught: {e}\n')
