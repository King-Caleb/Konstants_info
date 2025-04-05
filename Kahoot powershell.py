from KahootAPI import *

run = True


def search_by_number(member_number):
    """Search for a member by their number."""
    try:
        num = int(member_number)
        return Members.get(num, {
            'name': '???',
            'form': '???',
            'visits': '???',
            'points': '???'
        })
    except ValueError:
        return {
            'name': '???',
            'form': '???',
            'visits': '???',
            'points': '???'
        }


def search_by_name(member_name):
    """Search for a member by their name."""
    for member in Members.values():
        if member['name'].lower() == member_name.lower():
            return member
    return Members.get({
        'name': '???',
        'form': '???',
        'visits': '???',
        'points': '???'
    })


def search_by_form(member_form):
    """Search for members by their form and return a list of matching members."""
    matching_members = []
    for member in Members.values():
        if member['form'].lower() == member_form.lower():
            matching_members.append(member)

    # Return the list of matching members, or a placeholder if none are found
    if matching_members:
        return matching_members
    else:
        return [{
            'name': '???',
            'form': '???',
            'visits': '???',
            'points': '???'
        }]


def search_by_house(member_house):
    """Search for members by their form and return a list of matching members."""
    matching_members = []
    house_lower = member_house.lower()

    for member in Members.values():
        # Construct the forms to match (e.g., "7h1" and "7h2" for house "h")
        if member['form'].lower() in (f"7{house_lower}1", f"7{house_lower}2"):
            matching_members.append(member)

    # Return the list of matching members, or a placeholder if none are found
    if matching_members:
        return matching_members
    else:
        return [{
            'name': '???',
            'form': '???',
            'visits': '???',
            'points': '???'
        }]


def menu():
    global run
    if run:
        print('search 1: number(put 1)')
        print('search 2: name(put 2)')
        print('search 3: form(put 3)')
        print('search 4: house letter(put 4)')
        ans = input('>_')
        if ans == '1':
            num = input("input a member's number\n")
            search_num = search_by_number(num)
            print(search_num)
        elif ans == '2':
            name = input("input a member's name\n")
            search_name = search_by_name(name)
            print(search_name)
        elif ans == '3':
            form = input("input a member's form\n")
            search_form = search_by_form(form)
            print(search_form)
        elif ans == '4':
            member_house = input("input a member's house letter\n")
            search_house = search_by_house(member_house)
            print(search_house)

        else:
            run = False
    loop()


def loop():
    global run
    while run:
        print('More searches? (yes or no)')
        ans = input('> ').lower()
        if ans == 'yes':
            menu()
        elif ans == 'no':
            print('\2):')
            run = False


menu()
