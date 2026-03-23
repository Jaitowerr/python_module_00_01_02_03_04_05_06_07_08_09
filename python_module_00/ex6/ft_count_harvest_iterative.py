def ft_count_harvest_iterative():
    harvest = int(input('Days until harvest: '))
    for i in range(1, harvest + 1):
        print('Day', i)
    print('Harvest time!')

# python3 -c "from ft_count_harvest_iterative import
# ft_count_harvest_iterative; ft_count_harvest_iterative()"
