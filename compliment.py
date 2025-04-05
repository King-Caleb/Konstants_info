from random import*
print('compliment generator')
running = True
adjectives = ['Amazing', 'Exellent', 'intellegent', 'beatiful']
hobbies = ['coding', 'creative writing', 'Arts', 'reading', 'creative writing']
name = input('What is your name?\n')
print('Menu -- get compliment = c, quit = q')
while running:
    menuChoice = input('\n>').lower()
    if menuChoice == 'c':
        print ('Here is your compliment', name, ':')
        print(name, 'you are', choice(adjectives), 'at', choice(hobbies), '.')
        print('you are welcome')
    elif menuChoice == 'q':
        running = False
    else:
        print('Chose a VALID option')
