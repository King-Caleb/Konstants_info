from foode import *

poss = ""
run = True
act = 0  # Initializing 'act' variable

while run:
    print('To learn a recipe, click 1', 'To quit, click 2', 'To scan ingredients, click 3', sep='\n')
    lui = int(input('>_'))  # Corrected input to integer conversion
    if lui == 1:
        act = 1
    elif lui == 2:
        run = False
    elif lui == 3:
        act = 3  # Corrected the action for scanning
    if act == 1:
        learn()
    elif act == 3:
        scan()
    else:
        run = False
