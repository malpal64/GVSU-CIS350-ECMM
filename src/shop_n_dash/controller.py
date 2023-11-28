from view import View
import pygame
from player import Player

class Controller():
    def __init__(self):
        self.view = View()
        self.player_x = 50
        self.player_y = 50
        self.current_state = 0

    def show_start(self):
        return self.view.view_start()

    def show_character_select(self):
        action, char_type = self.view.view_character_select()
        Player.type = char_type
        return action

    def show_level(self):
        return self.view.view_level(self.player_x, self.player_y)

    def show_revive(self):
        return self.view.view_revive()

    def show_upgrade_screen(self):
        return self.view.view_upgrade_screen()

    def show_death(self):
        return self.view.view_death()

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Adjust player position based on key presses
        if keys[pygame.K_UP]:
            self.player_y -= 5
        elif keys[pygame.K_DOWN]:
            self.player_y += 5
        if keys[pygame.K_LEFT]:
            self.player_x -= 5
        elif keys[pygame.K_RIGHT]:
            self.player_x += 5

        # You can add more complex input handling as needed
        # For example, handling other keys for actions, inventory, etc.
