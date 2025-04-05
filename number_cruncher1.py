import math as m

run = True


def how_can_fit():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X // Y)


def powers():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X ** Y)


def times():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X * Y)


def plus():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X + Y)


def minus():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X - Y)


def divide():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X / Y)


def remainder():
    X = int(input('number 1:'))
    Y = int(input('number 2:'))
    # Z = input('number')

    print(X % Y)


def round_to_nearest_tenth(number):
    return round(number * 10) / 10


def pythagorus():
    A = int(input('Enter the length of side A: '))
    B = int(input('Enter the length of side B: '))
    Z = m.sqrt(A ** 2 + B ** 2)
    C = round_to_nearest_tenth(Z)
    print(f'The length of the hypotenuse (side C) is: {C}')


def menu():
    if run:
        print('operation 1: how many can fit')
        print('operation 2: powers')
        print('operation 3: times')
        print('operation 3: plus')
        print('operation 4: divide')
        print('operation 5: remainder')
        print('operation 6: minus')
        print('operation 7: pythagorus')
        print('choose an operation')
        ans = input('>_')
        if ans == 'how can many fit':
            how_can_fit()
        elif ans == 'powers':
            powers()
        elif ans == 'times':
            times()
        elif ans == 'plus':
            plus()
        elif ans == 'divide':
            divide()
        elif ans == 'remainder':
            remainder()
        elif ans == 'minus':
            minus()
        elif ans == 'pythagorus':
            pythagorus()
    loop()


def loop():
    global run
    while run:
        print('More calculations? (yes or no)')
        ans = input('> ').lower()
        if ans == 'yes':
            menu()
        elif ans == 'no':
            print('\2):')
            run = False


print('welcome to number cruncher')
menu()
