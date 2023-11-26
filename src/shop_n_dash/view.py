import pygame
from levelGenerator import LevelGenerator

class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 960))
        self.world = LevelGenerator().generate_level()
        self.start_background = pygame.image.load("assets/images/background/start_screen.png")
        self.title_icon = pygame.transform.scale(pygame.image.load("assets/images/background/title.png"), (600, 600))
        self.start_icon = pygame.transform.scale(pygame.image.load("assets/images/background/start_button.png"), (500, 500))


    def view_start(self):
        # Render the start screen
        # Example: Draw a start button, background, exit button
        self.screen.blit(self.start_background, (0, 0))
        self.screen.blit(self.title_icon, (350, 100))
        self.screen.blit(self.start_icon, (390, 500))

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
