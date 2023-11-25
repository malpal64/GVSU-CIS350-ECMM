import pygame
from levelGenerator import LevelGenerator

# this class handles what will be displayed for each of the views
class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 500))
        self.world = LevelGenerator().generate_level()

    def view_start(self):
        pass

    def view_character_select(self):
        pass

    def view_level(self):
        pass

    def view_revive(self):
        pass

    def view_upgrade_screen(self):
        pass

    def view_death(self):
        pass