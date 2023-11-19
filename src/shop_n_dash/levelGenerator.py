import pygame
import random
from gameMap import GameMap
from items import Item
from tile import Tile
from enemy import Enemy

class LevelGenerator():
    def __init__(self, num_items, num_enemies):
        self.num_items = num_items
        self.num_enemies = num_enemies

    def generate_level(self, width, height):
        game_map = GameMap(width, height)
        self.place_obstacles(game_map)
        self.place_items_and_enemies(game_map)
        return game_map

    def place_obstacles(self, game_map):
        pass



    def place_items_and_enemies(self, game_map):
        #load items into map
        for i in range(self.num_items):
            x = random.randint(0, game_map.width -1)
            y = random.randint(0, game_map.height -1)
            item = Item(0)
            game_map.set_tile(x, y, Tile(x, y, item))

        #load enemies into map
        for i in range(self.num_enemies):
            x = random.randint(0, game_map.width - 1)
            y = random.randint(0, game_map.height - 1)
            enemy = Enemy(50, 10)
            game_map.set_tile(x, y, Tile(x, y, enemy))