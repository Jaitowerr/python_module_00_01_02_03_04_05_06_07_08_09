def ft_water_reminder():
    need_water = int(input('Days since last watering: '))
    if need_water > 2:
        print('Water the plants!')
    else:
        print('Plants are fine')

# python3 -c "from ft_water_reminder import
# ft_water_reminder; ft_water_reminder()"
