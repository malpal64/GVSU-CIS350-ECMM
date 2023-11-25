import pygame
from tile import Tile

class GameMap():
    def __init__(self):
        self.width = 100
        self.height = 200
        self.tiles = [[Tile(x, y) for y in range(height)] for x in range(width)]

    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile