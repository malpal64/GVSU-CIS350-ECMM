import pygame
import math
from levelGenerator import LevelGenerator
from gameMap import GameMap


class Player():
    def __init__(self, gameMap):
        self.rect = pygame.Rect(0,0,20,20)
        self.x_pos = 400
        self.y_pos = 300
        self.rect.center = (self.x_pos, self.y_pos)
        self.health = 100
        self.attack_power = 4
        self.type = 0
        self.char_list = []
        self.char_type = ["boy", "girl", "elderly", "mad_piggy", "wizard"]
        self.action = 0
        self.frame_index = 0
        self.alive = True
        self.hit = False
        self.last_hit = pygame.time.get_ticks()
        self.update_time = pygame.time.get_ticks()
        self.speed = 6
        self.world = gameMap.level_map
        self.obstacle_list = gameMap.obstacle_list
        self.items = gameMap.items


        self.animation_types = ["idle", "run"]
        for char in self.char_type:
            # load images
            animation_list = []
            for animation in self.animation_types:
                # reset temporary list of images
                temp_list = []
                for i in range(4):
                    img = pygame.transform.scale(pygame.image.load(f"assets/images/characters/{char}/{animation}/{animation}_{i}.png").convert_alpha(), (50, 50))
                    temp_list.append(img)
                animation_list.append(temp_list)
            self.char_list.append(animation_list)

        self.running = False
        self.flip = False
        self.image = self.char_list[self.type - 1][self.action][self.frame_index]

        # add inventory
    def new_player(self, gameMap):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.x_pos = 400
        self.y_pos = 300
        self.rect.center = (self.x_pos, self.y_pos)
        self.health = 100
        self.attack_power = 4
        self.type = 0
        self.char_list = []
        self.char_type = ["boy", "girl", "elderly", "mad_piggy", "wizard"]
        self.action = 0
        self.frame_index = 0
        self.alive = True
        self.hit = False
        self.last_hit = pygame.time.get_ticks()
        self.update_time = pygame.time.get_ticks()
        self.speed = 6
        self.world = gameMap.level_map
        self.obstacle_list = gameMap.obstacle_list
        self.items = gameMap.items

        self.animation_types = ["idle", "run"]
        for char in self.char_type:
            # load images
            animation_list = []
            for animation in self.animation_types:
                # reset temporary list of images
                temp_list = []
                for i in range(4):
                    img = pygame.transform.scale(pygame.image.load(
                        f"assets/images/characters/{char}/{animation}/{animation}_{i}.png").convert_alpha(), (50, 50))
                    temp_list.append(img)
                animation_list.append(temp_list)
            self.char_list.append(animation_list)

        self.running = False
        self.flip = False
        self.image = self.char_list[self.type - 1][self.action][self.frame_index]


    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        return flipped_image

    def update(self):
        # check if character has died
        if self.health <= 0:
            self.health = 0
            self.alive = False

        # timer to reset player taking a hit
        hit_cooldown = 1000
        if self.char_type == 0:
            if self.hit == True and (pygame.time.get_ticks() - self.last_hit) > hit_cooldown:
                self.hit = False

        # check what action the player is performing
        if self.running:
            self.update_action(1)
        else:
            self.update_action(0)

        animation_cooldown = 200
        # handle animation
        # update image
        self.image = self.char_list[self.type - 1][self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # check if animation has finished
        if self.frame_index >= len(self.char_list[self.action]):
            self.frame_index = 0


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
        else:
            self.running = False



    def update_action(self, new_action):
        # check if new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def move(self, dx, dy):
        self.running = False
        if dx != 0 or dy != 0:
            self.running = True
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        # control diagonal speed
        if dx != 0 and dy != 0:
            magnitude = math.sqrt(dx ** 2 + dy ** 2)
            dx = (dx / magnitude) * (math.sqrt(2) / 2)
            dy = (dy / magnitude) * (math.sqrt(2) / 2)
        new_x = self.x_pos + (dx * self.speed)
        new_y = self.y_pos + (dy * self.speed)

        if self.collision(new_x, new_y):
            return
        else:
            self.x_pos = new_x
            self.y_pos = new_y

    def collision(self, x, y):
        rect = pygame.Rect(x, y, 32, 32)
        if self.obstacle_list is not None:
            for obstacle in range(len(self.obstacle_list)):
                if rect.colliderect(self.obstacle_list[obstacle][0]):
                    if self.obstacle_list[obstacle][1] == 1:
                        return True
                    else:
                        for item in range(len(self.items)):
                            if self.obstacle_list[obstacle][1] == self.items[item]:
                                self.items.pop(item)
                                self.obstacle_list.pop(obstacle)
                                return False
                        return False
