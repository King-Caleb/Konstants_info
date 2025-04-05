"""
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room

    def move(self, direction):
        self.current_room = self.current_room.move(direction)


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = {}

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    def get_details(self):
        print(self.name)
        print(self.description)


# Creating rooms
kitchen = Room('Kitchen', 'The room for making food')
living_room = Room('Living Room', 'A large room with TV')
bedroom = Room('Bedroom', 'A room with a comfortable bed')

# Linking direction
kitchen.link_room(living_room, 'south')
living_room.link_room(kitchen, 'north')
living_room.link_room(bedroom, 'west')
bedroom.link_room(living_room, 'east')

# Creating a player
player1 = Player(kitchen)

while True:
    player1.current_room.get_details()
    command = input("Enter a direction (north, south, west, east) or 'exit' to quit: ").strip().lower()
    if command == 'exit':
        break
    player1.move(command)
"""
import time
import pygame

run = True
pygame.display.set_caption('Room Navigation homework')


class Room(pygame.sprite.Sprite):
    def __init__(self, name, description, frame, neg, pos):
        super().__init__()
        self.names = name
        self.frames = frame
        self.description = description
        self.linked_rooms = {}
        self.pos = pos
        self.neg = neg
        self.bg_image = pygame.image.load(
            f"C:\\Users\\aalamu\\Documents\\__pycache__\\__pycache__\\{name}-{frame}.png.png")
        self.background_image = pygame.transform.scale(self.bg_image,
                                                       (int(self.bg_image.get_width() * 3),
                                                        int(self.bg_image.get_height() * 3)))

    def stabilize(self):
        if self.frames > self.pos:  # Assuming self.pos is the max positive frame
            self.frames = 1  # Reset to the first frame or another valid frame
        elif self.frames < self.neg:  # Assuming self.neg is the max negative frame
            self.frames = 1  # Reset to the first frame or another valid frame

    def load_image(self, frame, name):
        try:
            bg_image = pygame.image.load(f"C:\\Users\\aalamu\\Documents\\__pycache__\\__pycache__\\{name}-{frame}.png")
            return pygame.transform.scale(bg_image, (int(bg_image.get_width() * 3), int(bg_image.get_height() * 3)))
        except pygame.error:
            print("Unable to load image")
            return None

    def update(self, frame, name):
        self.stabilize()
        bg_image = pygame.image.load(f"C:\\Users\\aalamu\\Documents\\__pycache__\\__pycache__\\{name}-{frame}.png.png")
        self.background_image = pygame.transform.scale(bg_image,
                                                       (int(bg_image.get_width() * 3), int(bg_image.get_height() * 3)))

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def draw(self, x, y):
        screen.blit(self.background_image, (x, y))

    def move(self, new_room, needed_frame):
        self.stabilize()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.frames == needed_frame:
                self.names = 'living room'
                self.update(needed_frame, new_room)  # Refresh image if necessary
                print(f"Moved to: {self.names}")

    def rotate(self, name):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.frames += 1
        elif keys[pygame.K_RIGHT]:
            self.frames -= 1
        self.stabilize()
        self.update(self.frames, self.names)
        time.sleep(0.05)

    """def get_details(self):
            print(self.name)
            print(self.description)"""


kitchen = Room('Kitchen', 'room for food', 1, -5, 5)
living_room = Room('living_room', 'TV room', 1, -3, 5)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    kitchen.move('living_room', 1)
    living_room.move('kitchen', 2)
    kitchen.stabilize()
    living_room.stabilize()
    kitchen.draw(15, 0)
    kitchen.rotate('kitchen')
    living_room.rotate('living_room')
    pygame.display.flip()

pygame.quit()
