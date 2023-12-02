import pygame
from tile import Tile
from levelGenerator import LevelGenerator
import random

class GameMap():
    def __init__(self):
        self.width = random.randint(50,70)
        self.height = random.randint(50,70)
        self.tiles = [[Tile(x, y) for y in range(self.height)] for x in range(self.width)]
        self.level_map = LevelGenerator(self.width, self.height).generate_level()

    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile