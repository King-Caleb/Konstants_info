money = 500
wood = 100
water = 10
turns = 25
food = 100
population = 15
print('you have ', food, 'food')
print('you have', population, 'population')
print('you have', water, 'water')
print('you have', money, 'pounds\n\n')
welcome_message = 'Welcome to your create city\nIn this game you have the power to create the city of your dreams'
print(welcome_message)
print('These are the buildings of choice')
print('1. Hut\n2. Hospital\n3. Fishery\n4. Restaurant\n5. Hunter\n6. Well\n7. Berry picker\n8. Forester\n9. House')
print('10. Farm\n11. Ranch\n12. Mine\n13. Stone mason\n')
for i in range(50):
    food = food - 1
for q in range(turns):
    if food > 0 and water > 0 and money > 0 and turns > 0 and wood > 0 and population > 0:
        building = input('insert a number that represents a building of your choice\n')
        if building == '1':
            population = population + 2
            water = water - 2
            wood = wood - 5
            money += 20
        if building == '2':
            turns = turns + 5
            wood = wood - 5
        if building == '3':
            food = food + 10
            wood = wood - 5
        if building == '4':
            food = food + 50
            wood = wood - 5
        if building == '5':
            food = food + 10
            wood = wood - 5
        if building == '6':
            water = water + 10
            money = money - 10
        if building == '7':
            food = food + 10
            wood = wood - 5
        if building == '8':
            wood = wood + 20
        if building == '9':
            population = population + 5
            wood = wood - 5
            money = money + 30
        if building == '10':
            water = water - 2
            money = money - 10
            food = food + 20
        if building == '11':
            food = food + 20
            water = water - 2
            wood = wood - 5
        if building == '12':
            population = population - 10
            import random
            money = money + (random.randrange(-100, 100))
            money = money - 10
        if building == '13':
            wood = wood - 5
            money = money + 30
        if building == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13:
            money = money - 10
            turns = turns - 1
            print('you have', food, 'food\nyou have', population, 'population\nyou have', water, 'water')
            print('you have', money, 'pounds\n you have', turns, 'turns left')
    else:
        print(':(')
        print('you have', food, 'food\nyou have', population, 'population\nyou have', water, 'water')
        print('you have', money, 'pounds\n')
