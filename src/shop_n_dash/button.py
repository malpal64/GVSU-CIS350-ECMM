import pygame


class Button():
    def __init__(self, x, y, image, char_type=None):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.char_type = char_type

    def draw(self, surface):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True

        surface.blit(self.image, self.rect)

        if self.char_type != None:
            return action, self.char_type
        else:
            return action
