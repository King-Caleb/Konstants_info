import pygame
import sys


def bggrounds():
    collisions = pygame.sprite.spritecollide(player, home_1, False)
    print("Collisions:", collisions)
    if collisions:
        bg_path = ("C:\\Users\\aalamu\\Pictures\\PycharmProjects\\pythonProject\\pygame\\backgrounds"
                   "\\house1\\living-of-1.jpg")
        try:
            print("Changing background_img to:", bg_path)
            background_img = pygame.image.load(bg_path).convert()
            background_image = pygame.transform.scale(background_img, (width, height))
            # Clear the screen to a specific color (black in this example)
            screen.fill((0, 0, 0))
            screen.blit(background_image, (0, 0))
            pygame.display.flip()
            pygame.display.update()
            print('Done')
        except pygame.error as e:
            print(f"Error loading image: {e}")


pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Create city")

background_image = pygame.image.load(
    "C:\\Users\\aalamu\\Pictures\\PycharmProjects\\pythonProject\\pygame\\backgrounds\\path\\path 1.jpg")
background_image = pygame.transform.scale(background_image, (width, height))


class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, building_type):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(
            f"C:\\Users\\aalamu\\Pictures\\PycharmProjects\\pythonProject\\pygame\\building\\{building_type}\\{building_type} 1.jpg")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, character_type):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(
            f"C:\\Users\\aalamu\\Pictures\\PycharmProjects\\pythonProject\\pygame\\{character_type}\\{character_type} idle\\{character_type} idle 1.jpg")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.jumping = False
        self.falling = False
        self.vertical_velocity = 0

    def handle_events(self, Event):
        global background_image
        if Event.type == pygame.KEYDOWN:
            if Event.key == pygame.K_a:
                self.is_moving_left = True
                self.move_left()
            if Event.key == pygame.K_d:
                self.is_moving_right = True
                self.move_right()
            if Event.key == pygame.K_SPACE:
                self.jumping = True
                self.jump()
            if Event.key == pygame.K_s:
                self.falling = True
                self.fall()
            if event.key == pygame.K_x:
                bggrounds()

            # Corrected line
        if Event.type == pygame.KEYUP:
            if Event.key == pygame.K_a:
                self.is_moving_left = False
            if Event.key == pygame.K_d:
                self.is_moving_right = False
            if Event.key == pygame.K_SPACE:
                self.jumping = False
            if Event.key == pygame.K_s:
                self.falling = False
                self.fall()

    def draw(self):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= 15

    def move_right(self):
        self.rect.x += 15

    def jump(self):
        if self.jumping:
            gravity = 0.5
            self.vertical_velocity += gravity
            self.rect.y -= self.vertical_velocity

            # Simulate gravity
            self.rect.y += gravity
            ground_group = pygame.sprite.Group()

            # Check if the player has reached or gone below the ground level
            collisions = pygame.sprite.spritecollide(self, ground_group, False)
            if collisions:
                # Player is on the ground
                self.vertical_velocity = 0
                self.rect.y = collisions[0].rect.y - self.rect.height
                self.jumping = False

    def fall(self):
        if self.falling:
            self.rect.y += 10


building_instance = Building(540, 330, 0.5, 'house')
home_1 = pygame.sprite.Group()
home_1.add(building_instance)

player = Character(200, 100, 0.3, "player")

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        player.handle_events(event)

    screen.blit(background_image, (0, 0))
    player.move_left()
    player.move_right()
    player.jump()
    player.draw()
    home_1.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
