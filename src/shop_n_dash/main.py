import pygame
from controller import Controller

pygame.init()
pygame.display.set_caption("Shop 'n Dash")
clock = pygame.time.Clock()

run = True
status = 0
controller = Controller()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if status == 0:
        controller.show_start()
        # Update game state, handle input, etc.


    pygame.display.update()
    clock.tick(60)  # Cap the frame rate at 60 frames per second

pygame.quit()
