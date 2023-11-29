import pygame
import math

class Player():
    def __init__(self):
        self.rect = pygame.Rect(0,0,40,40)
        self.x_pos = 50
        self.y_pos = 50
        self.rect.center = (self.x_pos, self.y_pos)
        self.health = 100
        self.attack_power = 5
        self.type = 0
        # add inventory

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move(0, -1)
        elif keys[pygame.K_DOWN]:
            self.move(0, 1)
        if keys[pygame.K_LEFT]:
            self.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.move(1, 0)

    def move(self, dx, dy):
        # control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
        self.x_pos += dx
        self.y_pos += dy

