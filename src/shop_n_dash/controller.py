from view import View
import pygame
from player import Player
from levelGenerator import LevelGenerator
from gameMap import GameMap

class Controller():
    def __init__(self):
        self.view = View()
        self.current_state = 0
        self.player = Player(self.view.gameMap)

    def show_start(self):
        return self.view.view_start()

    def show_character_select(self):
        action, char_type = self.view.view_character_select()
        self.player.type = char_type
        self.player.update()
        return action

    def show_level(self):
        self.player.handle_input()
        self.player.update()
        self.player = self.view.view_level(self.player)


    def show_revive(self):
        return self.view.view_revive()

    def show_upgrade_screen(self):
        return self.view.view_upgrade_screen()

    def show_death(self):
        return self.view.view_death()

