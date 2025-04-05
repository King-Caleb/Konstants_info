import sys

# Flagged words and suspicious words lists
flagged_words = ["meow", "OMG"]
sus_words = ["skibidi", "rizz", "rizzler"]


def check(t):
    # Check each word in the input
    words = t.split()
    for word in words:
        if word in flagged_words:
            print(f"Naughty word detected: {word}")
            sys.exit()  # End the program immediately


def ask_yes_no(question):
    """Helper function to ask Yes/No questions with validation."""
    while True:
        response = input(question).lower()
        if response in ['yes', 'yeah', 'ya']:
            return True
        elif response in ['no', 'nah', 'nope']:
            return False
        else:
            print("Please answer with 'Yes' or 'No'.")


def check_for_sus_words(input_string):
    """Check if any suspicious words are in the input."""
    words = input_string.lower().split()
    for word in words:
        if word in sus_words:
            return True
    return False


# Main program starts here
name = input("What is your name?\n")
check(name)  # Check for flagged words in the name

print(f"Hello {name}, welcome to the chat app")
has_job = ask_yes_no("Do you have a job? Yes or no\n")
check(has_job)  # Check for flagged words in the job answer

if has_job:
    job = input("What is your job, please?\n")
    check(job)  # Check for flagged words in the job description
    if check_for_sus_words(job):
        print("hmmm... strange.")

    went_to_school = ask_yes_no("Did you use to go to school? Yes or no?\n")
    check(went_to_school)  # Check for flagged words in the school answer
    if went_to_school:
        school = input("What school did you go to?\n")
        check(school)  # Check for flagged words in the school name
        if check_for_sus_words(school):
            print("hmmm... such a strange school.")
            print("You have proved to be sus")
            print(f"Bye {name}, rizzler")
            sys.exit()  # End the program
        else:
            print("That is a good school!")
            print(f"Bye {name}")
else:
    input("What do you want to be in the future?\n")
    print("I hope you get there.")

    goes_to_school = ask_yes_no("Do you go to school? Yes or no?\n")
    check(goes_to_school)  # Check for flagged words in the school answer
    if goes_to_school:
        school = input("What school do you go to?\n")
        check(school)  # Check for flagged words in the school name
        print("That is a good school!")
        print(f"Bye {name}")
    else:
        print(f"Goodbye {name}")
