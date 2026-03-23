def ft_harvest_total():
    harvest_one = int(input('Day 1 harvest: '))
    harvest_two = int(input('Day 2 harvest: '))
    harvest_three = int(input('Day 3 harvest: '))
    total = harvest_one + harvest_two + harvest_three
    print('Total harvest:', total)

# python3 -c "from ft_harvest_total import ft_harvest_total; ft_harvest_total("
