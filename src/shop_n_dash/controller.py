from view import View
import pygame

class Controller():
    def __init__(self):
        pass

    def show_start(self):
        return View().view_start()

    def show_character_select(self):
        return View().view_character_select()

    def show_level(self):
        return View().view_level()

    def show_revive(self):
        return View().view_revive()

    def show_upgrade_screen(self):
        return View().view_upgrade_screen()

    def show_death(self):
        return View().view_death()