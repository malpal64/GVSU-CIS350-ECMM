import pygame

class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0,0,40,40)
        self.rect.center = (x, y)
        self.health = 100
        self.attack_power = 5
        # add inventory

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def update_player(self):
        pass