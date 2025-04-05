class students:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print('1 = continue', '0= stop', sep='\n')


def work():
    Mike = students('Mike', 4)
    John = students('John', 5)

    register = ['Mike', 'John']
    for i in range(2):
        print(register[i])

    c = input('>_')
    if c == Mike:
        print(Mike.age)
    else:
        print(John.age)


work()

more = int(input('repeat >_'))
while more == 1:
    work()
    more = int(input('repeat >_'))

print('Bye for now...')
print(':- (')
