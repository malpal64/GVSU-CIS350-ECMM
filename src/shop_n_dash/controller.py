from view import View
import pygame

class Controller():
    def __init__(self):
        self.view = View()

    def show_start(self):
        return self.view.view_start()

    def show_character_select(self):
        return self.view.view_character_select()

    def show_level(self):
        return self.view.view_level()

    def show_revive(self):
        return self.view.view_revive()

    def show_upgrade_screen(self):
        return self.view.view_upgrade_screen()

    def show_death(self):
        return self.view.view_death()