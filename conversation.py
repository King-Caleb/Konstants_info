import sys

flagged_words = ["meow", "OMG", "stupid"]
sus_words = ["skibidi", "rizz", "rizzler"]


def check(t):
    x = t.split()
    for p in x:
        if p in flagged_words:
            print(f"Naughty word detected: {p}")
            sys.exit()  # End the program immediately
        if p in sus_words:
            print("hmm... strange.")


name = input("what is your name?\n")
check(name)
yes = "Yes"

print("Hello " + name + ",welcome to the chat app")
iyes = input("Do you have a job? Yes or no\n").lower()
check(iyes)
if iyes == yes or iyes == "yeah" or iyes == "ya":
    gob = input("what is it please?\n")
    check(gob)
    job = (gob.lower()).split()

    edu = input("Did you use to go to school? Yes or no?\n").lower()
    check(edu)
    if edu == yes or "yeah" or "ya":
        idu = input("what school did you go to?\n")
        check(idu)
        for word in idu:
            if word in sus_words:
                print("hmm... such a strange school.")
                print("you have proved to be sus")
                print("bye", name, "rizzler")
            else:
                print("That is a good school!")
                print("Bye " + name)
else:
    input("what do you want to be in the future?\n")
    print("I hope you get there.")
    edu = input("Do you go to school? Yes or no?\n").lower()
    check(edu)
    if edu == yes or "yeah" or "ya":
        idu = input("What school do you go to?\n")
        check(idu)
        print("That is a good school!")
        print("Bye " + name)
    else:
        print("Goodbye " + name)

        print("That is a good school!\nBye " + name)
