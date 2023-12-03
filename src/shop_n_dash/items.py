import pygame

class Item():
    def __init__(self):
        self.list = [[2, 'Green grapes', pygame.transform.scale(pygame.image.load("assets/images/items/0.png"), (32,32))],
                     [3, 'Eggs', pygame.transform.scale(pygame.image.load("assets/images/items/1.png"), (32,32))],
                     [4, 'Chocolate bar', pygame.transform.scale(pygame.image.load("assets/images/items/2.png"), (32,32))],
                     [5, 'Orange juice', pygame.transform.scale(pygame.image.load("assets/images/items/3.png"), (32,32))],
                     [6, 'Cheese', pygame.transform.scale(pygame.image.load("assets/images/items/4.png"), (32,32))],
                     [7, 'Wine', pygame.transform.scale(pygame.image.load("assets/images/items/5.png"), (32,32))],
                     [8, 'Peppers', pygame.transform.scale(pygame.image.load("assets/images/items/6.png"), (32,32))],
                     [9, 'Bacon', pygame.transform.scale(pygame.image.load("assets/images/items/7.png"), (32,32))],
                     [10, 'Bananas', pygame.transform.scale(pygame.image.load("assets/images/items/8.png"), (32,32))],
                     [11, 'Cereal', pygame.transform.scale(pygame.image.load("assets/images/items/9.png"), (32,32))],
                     [12, 'Coffee beans', pygame.transform.scale(pygame.image.load("assets/images/items/10.png"), (32,32))],
                     [13, 'Milk', pygame.transform.scale(pygame.image.load("assets/images/items/11.png"), (32,32))],
                     [14, 'Strawberry icecream', pygame.transform.scale(pygame.image.load("assets/images/items/12.png"), (32,32))],
                     [15, 'Watermelon', pygame.transform.scale(pygame.image.load("assets/images/items/13.png"), (32,32))]]
