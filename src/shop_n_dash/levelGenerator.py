import pygame
import random

from items import Item
from tile import Tile
from enemy import Enemy

class LevelGenerator:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]
        self.items = []
        self.item_tiles = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.obstacle_tiles = []
        self.wall_tiles = [1]

    def generate_level(self):
        self.generate_rooms()
        self.generate_corridors()
        self.place_items()
        #self.place_enemies()
        self.create_walls()

        return self.tiles, self.items

    def generate_rooms(self):
        num_rooms = random.randint(5, 10)

        for _ in range(num_rooms):
            room_width = random.randint(5, 10)
            room_height = random.randint(5, 10)

            room_x = random.randint(1, self.width - room_width - 1)
            room_y = random.randint(1, self.height - room_height - 1)

            if all(self.tiles[y][x] == 0 for y in range(room_y, room_y + room_height) for x in range(room_x, room_x + room_width)):
                for x in range(room_x, room_x + room_width):
                    for y in range(room_y, room_y + room_height):
                        self.tiles[y][x] = 1  # 1 represents a wall in this example

    def generate_corridors(self):
        for i in range(len(self.tiles) - 1):
            for j in range(len(self.tiles[0]) - 1):
                if self.tiles[i][j] == 1 and self.tiles[i + 1][j] == 1:
                    self.tiles[i][j] = 0
                if self.tiles[i][j] == 1 and self.tiles[i][j + 1] == 1:
                    self.tiles[i][j] = 1
    def create_walls(self):
        for i in range(self.width):
            for y in range(self.height):
                if i == 0 or i == self.width-1:
                    self.tiles[y][i] = 1
                if y == 0 or y == self.height-1:
                    self.tiles[y][i] = 1

    def place_items(self):
        num_items = random.randint(5, 7)

        for x in range(num_items):
            item_x = random.randint(1, self.width - 2)
            item_y = random.randint(1, self.height - 2)

            if self.tiles[item_y][item_x] == 0:
                self.tiles[item_y][item_x] = random.randint(2,15)
                self.items.append(self.tiles[item_y][item_x])

    def place_enemies(self):
        num_enemies = random.randint(3, 5)

        for _ in range(num_enemies):
            enemy_x = random.randint(1, self.width - 1)
            enemy_y = random.randint(1, self.height - 1)

            if self.tiles[enemy_y][enemy_x] == 0:
                # 3 represents an enemy in this example
                self.tiles[enemy_y][enemy_x] = random.randint(15, 20)
