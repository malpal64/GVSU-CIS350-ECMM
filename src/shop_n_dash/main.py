import pygame
from controller import Controller
from player import Player

pygame.init()
pygame.display.set_caption("Shop 'n Dash")

run = True
while run:
    Controller().show_start()


pygame.quit()