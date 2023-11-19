import pygame

class Tile():
    def __init__(self, x, y, content=None):
        self.x = x
        self.y = y
        self.content = content