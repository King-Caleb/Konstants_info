# API as provided
Members = {
    0: {'name': 'Test',
        'form': '7P1',
        'visits': '5',
        'points': '24', },

    1: {'name': 'Andrew',
        'form': '7P1',
        'visits': '3',
        'points': '9', },

    2: {'name': 'Ivan',
        'form': '7C1',
        'visits': '5',
        'points': '30', },

    3: {'name': 'Andrei',
        'form': '7B1',
        'visits': '2',
        'points': '10', },

    4: {'name': 'Ayaan',
        'form': '7H1',
        'visits': '3',
        'points': '11', },

    5: {'name': 'Shangen',
        'form': '7C1',
        'visits': '7',
        'points': '43', },

    6: {'name': 'Dhyan',
        'form': '7P2',
        'visits': '1',
        'points': '3', },

    7: {'name': 'Aarjun',
        'form': '7P1',
        'visits': '3',
        'points': '9', },

    8: {'name': 'Alex',
        'form': '9P1',
        'visits': '5',
        'points': '26', },

    9: {'name': 'Adam',
        'form': '7B2',
        'visits': '1',
        'points': '3', },

    10: {'name': 'Zhokai',
         'form': '7B1',
         'visits': '1',
         'points': '3', },

    11: {'name': 'Hamza',
         'form': '7B2',
         'visits': '1',
         'points': '1', },

    12: {'name': 'Arlo',
         'form': '7C2',
         'visits': '2',
         'points': '17', },

    13: {'name': 'Ali',
         'form': '7P2',
         'visits': '2',
         'points': '6', },

    14: {'name': 'Arnay',
         'form': '7B2',
         'visits': '2',
         'points': '4', },

    15: {'name': 'Moamen',
         'form': '7P2',
         'visits': '1',
         'points': '5', },

    16: {'name': 'Abu',
         'form': '7B2',
         'visits': '1',
         'points': '3', },

    17: {'name': 'Viaan',
         'form': '7B1',
         'visits': '2',
         'points': '8', },

    18: {'name': 'Musa',
         'form': '7H1',
         'visits': '2',
         'points': '6', },

    19: {'name': 'Fergus',
         'form': '7B1',
         'visits': '3',
         'points': '13', },

    20: {'name': 'Josh',
         'form': '7C1',
         'visits': '3',
         'points': '10', },

    21: {'name': 'Aayush',
         'form': '7?1',
         'visits': '1',
         'points': '0', },

    22: {'name': 'Agastya',
         'form': '7C2',
         'visits': '2',
         'points': '4', },

    23: {'name': 'Dyuti',
         'form': '7C2',
         'visits': '1',
         'points': '4', },

    24: {'name': 'Aaashita',
         'form': '7?1',
         'visits': '1',
         'points': '3', },

    25: {'name': 'Almeer',
         'form': '7P2',
         'visits': '1',
         'points': '5', },

    26: {'name': 'Eric',
         'form': '7H2',
         'visits': '1',
         'points': '4', },

    27: {'name': 'Achillies',
         'form': '7P1',
         'visits': '2',
         'points': '10', },

    28: {'name': 'Hasan',
         'form': '7C1',
         'visits': '2',
         'points': '6', },

    29: {'name': 'Alex',
         'form': '7P1',
         'visits': '2',
         'points': '10', },

    30: {'name': 'Aahana',
         'form': '7P2',
         'visits': '1',
         'points': '5', },

    31: {'name': 'Harythuvaan',
         'form': '7B2',
         'visits': '1',
         'points': '2', },

    32: {'name': 'Sufyan',
         'form': '7B1',
         'visits': '1',
         'points': '5', },

    33: {'name': 'Ahmed',
         'form': '7C2',
         'visits': '2',
         'points': '11', },

    34: {'name': 'Abu Bakr',
         'form': '7C2',
         'visits': '1',
         'points': '5', },
}


def search(Number):
    return Members.get(Number, {
        'name': '???',
        'form': '???',
        'visits': '???',
        'points': '???'
    })
