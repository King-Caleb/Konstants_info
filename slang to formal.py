run = True
slangd = {
    "lol": "laugh out loud",
    "idk": "I don't know",
    "hi":"hello"
}

slang = [slangd]


def display_menu():
    print('Menu')
    print('c = convert a sentence')
    print('p = print dictionary')
    print('a = add to dictionary')
    print('q = quit')
    print('r = reset')


def convert_sentence():
    sentence = input('Enter the sentence to translate:\n').lower()
    List_Of_Words = sentence.split()
    translated_sentence = ""
    for word in List_Of_Words:
        if word in slangd:
            translated_sentence += slangd[word] + " "
        else:
            word = word + ''
            translated_sentence += word + " "
    translated_sentence = translated_sentence + '.'
    print(translated_sentence)


def adddictionaryitem():
    global slang  # Referencing the global variable
    texttoad = input('Enter the word you wish to add to the dictionary: ')
    meaning = input('What does that mean? ')
    slangd[texttoad] = meaning
    slang = [slangd]  # Reassigning the global variable


def delete_word():
    global slang  # Assuming 'slang' is a global variable

    if not slang:
        print("The dictionary is empty. No items to remove.")
        return

    word_to_remove = input('Enter the word you want to remove from the dictionary: ').lower()

    if word_to_remove in slangd:
        del slangd[word_to_remove]
        slang = [slangd]  # Reassigning the global variable
        print("Word removed successfully.")
    else:
        print("Word not found in the dictionary.")


def reset():
    global slang  # Referencing the global variable
    slang = [slangd]


display_menu()

while run:
    menuChoice = input(':').lower()
    if menuChoice == 'c':
        convert_sentence()
    elif menuChoice == 'p':
        print(slang)
    elif menuChoice == 'a':
        adddictionaryitem()
    elif menuChoice == 'd':
        delete_word()
    elif menuChoice == 'q':
        run = False
    elif menuChoice == 'r':
        reset()
    else:
        print('Choose a VALID option')
