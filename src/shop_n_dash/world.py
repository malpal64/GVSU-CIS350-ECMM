import pygame
from player import Player
from items import Item
import csv

class World():
    def __init__(self):
        self.level = 0
        self.world_data = []

    def next_level(self):
        self.level += 1
        self.world_data = []
        if self.level <= 4:
            with open(f"levels/level{self.level}_data.csv", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        self.world_data[x][y] = int(tile)
