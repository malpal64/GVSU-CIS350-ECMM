import pygame
from levelGenerator import LevelGenerator
from button import Button

class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 960))
        self.world = LevelGenerator().generate_level()

        # loading images from assets
        self.start_background = pygame.image.load("assets/images/background/start_screen.png")
        self.title_icon = pygame.transform.scale(pygame.image.load("assets/images/background/title.png"), (600, 600))
        self.start_icon = pygame.transform.scale(pygame.image.load("assets/images/background/start_button.png"), (500, 500))
        self.boy_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/boy/no_anim_0.png"), (200, 200))
        self.girl_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/girl/no_anim_0.png"),(200, 200))
        self.elderly_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/elderly/no_anim_0.png"),(200, 200))
        self.mad_piggy_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/mad_piggy/no_anim_0.png"),(200, 200))
        self.wizard_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/wizard/no_anim_0.png"),(200, 200))
        self.select_char_icon = pygame.transform.scale(pygame.image.load("assets/images/background/select_char_icon.png"), (600, 600))

        # Buttons
        self.start_button = Button(390, 500, self.start_icon)
        self.boy_button = Button(350, 300, self.boy_icon, 1)
        self.girl_button = Button(650, 300, self.girl_icon, 2)
        self.elderly_button = Button(250, 500, self.elderly_icon, 3)
        self.mad_piggy_button = Button(550, 500, self.mad_piggy_icon, 4)
        self.wizard_button = Button(850, 500, self.wizard_icon, 5)



    def view_start(self):
        # Render the start screen
        # Example: Draw a start button, background, exit button
        self.screen.blit(self.start_background, (0, 0))
        self.screen.blit(self.title_icon, (350, 100))
        action = self.start_button.draw(self.screen)
        return action

    def view_character_select(self):
        # Render the character selection screen
        # Example: Display different characters, let the player choose, etc.
        self.screen.blit(self.start_background, (0, 0))
        self.screen.blit(self.select_char_icon, (350, -20))
        action1, char_type1 = self.boy_button.draw(self.screen)
        action2, char_type2 = self.girl_button.draw(self.screen)
        action3, char_type3 = self.elderly_button.draw(self.screen)
        action4, char_type4 = self.mad_piggy_button.draw(self.screen)
        action5, char_type5 = self.wizard_button.draw(self.screen)

        if action1:
            return action1, 1
        elif action2:
            return action2, 2
        elif action3:
            return action3, 3
        elif action4:
            return action4, 4
        elif action5:
            return action5, 5
        else:
            return False, 0




    def view_level(self):
        # Render the game level
        # Example: Draw the level, characters, obstacles, etc.
        self.screen.blit(self.start_background, (0, 0))

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
