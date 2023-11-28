import pygame
import random

from items import Item
from tile import Tile
from enemy import Enemy

class LevelGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_level(self):
        # Create an empty map with all tiles set to 0 (e.g., representing floor)
        level_map = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Place walls (1) around the border of the map
        for x in range(self.width):
            level_map[0][x] = 1
            level_map[self.height - 1][x] = 1

        for y in range(self.height):
            level_map[y][0] = 1
            level_map[y][self.width - 1] = 1

        # Add additional wall placement or room generation logic
        self.generate_rooms(level_map)

        return level_map

    def generate_rooms(self, level_map):
        num_rooms = random.randint(5, 10)  # Adjust the number of rooms as needed

        for _ in range(num_rooms):
            room_width = random.randint(5, 10)
            room_height = random.randint(5, 10)

            # Randomly place the room within the map bounds
            room_x = random.randint(1, self.width - room_width - 1)
            room_y = random.randint(1, self.height - room_height - 1)

            # Check if the chosen area is free from other rooms
            if all(level_map[y][x] == 0 for y in range(room_y, room_y + room_height) for x in range(room_x, room_x + room_width)):
                # Place walls around the room
                for x in range(room_x - 1, room_x + room_width + 1):
                    level_map[room_y - 1][x] = 1
                    level_map[room_y + room_height][x] = 1

                for y in range(room_y - 1, room_y + room_height + 1):
                    level_map[y][room_x - 1] = 1
                    level_map[y][room_x + room_width] = 1

                # You can add more room features or decorations as needed