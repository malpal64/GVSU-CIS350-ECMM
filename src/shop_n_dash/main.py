import pygame
import constants
from player import Player

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Shop 'n Dash")


# the main class should create the needed objects and run the game


# create player
player = Player(100, 100)

# main game loop
run = True
while run:

    #draw player on screen
    player.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()