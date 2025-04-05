import pygame
run = True

width, height = 800, 600
bg_image = pygame.image.load("C:\\Users\\aalamu\\Documents\\__pycache__\\__pycache__\\Kitchen-1.png.png")
background_image = pygame.transform.scale(bg_image, (int(bg_image.get_width() * 3), int(bg_image.get_height() * 3)))
screen = pygame.display.set_mode((width, height))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background_image, (15, 0))
    pygame.display.flip()

pygame.quit()
