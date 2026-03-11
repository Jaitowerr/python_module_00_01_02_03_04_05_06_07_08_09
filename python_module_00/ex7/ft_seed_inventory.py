def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == 'packets':
        print(seed_type.capitalize(), 'seeds:', quantity, 'packets available')
    elif unit == 'grams':
        print(seed_type.capitalize(), 'seeds:', quantity, 'grams total')
    elif unit == 'area':
        print(seed_type.capitalize(), 'seeds: covers', quantity,
              'square meters')
    else:
        print('Unknown unit type')

# python3 -c "from ft_seed_inventory import
#  ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"

# python3 -c "from ft_seed_inventory import
#  ft_seed_inventory; ft_seed_inventory('carrot', 8, 'grams')"

# python3 -c "from ft_seed_inventory import
#  ft_seed_inventory; ft_seed_inventory('lettuce', 12, 'area')"
