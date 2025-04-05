student_data={
    1:'Feyi',
    2:'Momore',
    3:'Caleb'
}
text_speak_dictionary={
    "lol":"laugh out loud ",
    'idk':"I don't know "
    }
sentence=input('Enter the sentene to translate\n').lower()
words_to_translate = sentence.split()
translated_sentence = ""
for word in words_to_translate:
    if word in text_speak_dictionary:
        translated_sentence += text_speak_dictionary[word]+""
    else:
        translated_sentence += word + ""
print (translated_sentence)

def display_menu():
    print('Menu')
    print('c-convert a sentence')
    print('p=print menu')
    print('a=add to dictionary')
    print('q = q')

def convert_sentence():

    sentence=input('Enter the sentene to translate:\n').lower()
    List_Of_Words = sentence.split()
    translated_sentence = ""
    for word in List_Of_Words:
        if word in text_speak_dictionary:
            translated_sentence += text_speak_dictionary[word]+""
            text_speak_dictionary[word]+""
        else:
            translated_sentence += word + ""
    print (translated_sentence)

def adddictionaryitem():
    texttoad = input('Enter the word you wish to add to the dictionary')
    meaning = input('what does that mean?')
    text_speak_dictionary[texttoad] = meaning

running = True
display_menu()
while running:
    menuChoice = input(':').lower()
    if menuChoice == 'c':
        convert_sentence()
    elif menuChoice == 'p':
        print(text_speak_dictionary)
    elif menuChoice == 'a':
        adddictionaryitem()
    else:
        print('Chose a VALID option')
