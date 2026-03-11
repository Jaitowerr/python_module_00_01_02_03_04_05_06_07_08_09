def ft_plant_age():
    age = int(input('Enter plant age in days: '))
    if age > 60:
        print('Plant is ready to hardvest!')
    else:
        print('Plan needs more time to grow.')

# python3 -c "from ft_plant_age import
# ft_plant_age; ft_plant_age()"
