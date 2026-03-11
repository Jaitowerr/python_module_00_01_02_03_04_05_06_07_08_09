def ft_recursive(acumulado, total):
    if acumulado <= total:
        print('Day ', acumulado)
        ft_recursive(acumulado + 1, total)


def ft_count_harvest_recursive():
    day_harvest = int(input('Days until harvest: '))
    ft_recursive(1, day_harvest)
    print('Harvest time!')

# python3 -c "from ft_count_harvest_recursive
# import ft_count_harvest_recursive; ft_count_harvest_recursive()"
