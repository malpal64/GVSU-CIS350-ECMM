import pygame
from levelGenerator import LevelGenerator

class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 500))
        self.world = LevelGenerator().generate_level()

    def view_start(self):
        # Render the start screen
        # Example: Draw a start button, background, etc.
        pygame.draw.rect(self.screen, (224, 168, 206), pygame.Rect(50, 50, 25, 25))

    def view_character_select(self):
        # Render the character selection screen
        # Example: Display different characters, let the player choose, etc.
        pass

    def view_level(self):
        # Render the game level
        # Example: Draw the level, characters, obstacles, etc.
        pass

    def view_revive(self):
        # Render the screen when the player can revive
        # Example: Display options for revival, countdown, etc.
        pass

    def view_upgrade_screen(self):
        # Render the upgrade screen
        # Example: Display available upgrades, let the player choose, etc.
        pass

    def view_death(self):
        # Render the death screen
        # Example: Display score, options to restart, etc.
        pass
