import pygame
from tile import Tile
from levelGenerator import LevelGenerator
import random

class GameMap():
    def __init__(self):
        self.width = random.randint(20,40)
        self.height = random.randint(20,30)
        self.tiles = [[Tile(x, y) for y in range(self.height)] for x in range(self.width)]
        self.level_map = LevelGenerator(self.width, self.height).generate_level()
        self.obstacle_list = []
        self.tile_size = 32

        for y, row in enumerate(self.level_map):
            for x, tile_value in enumerate(row):
                # Calculate the screen position for the tile
                tile_rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                print(tile_rect)
                if 1 <= tile_value <= 15:
                    self.obstacle_list.append(tile_rect)


    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile


