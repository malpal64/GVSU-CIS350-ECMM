import pygame
from gameMap import GameMap
from button import Button
from items import Item
from player import Player


class View():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 960))
        self.gameMap = GameMap()

        # loading images from assets
        self.start_background = pygame.image.load("assets/images/background/start_screen.png")
        self.title_icon = pygame.transform.scale(pygame.image.load("assets/images/background/title.png"), (600, 600))
        self.start_icon = pygame.transform.scale(pygame.image.load("assets/images/background/start_button.png"), (500, 500))
        self.boy_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/boy/no_anim_0.png"), (200, 200))
        self.girl_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/girl/no_anim_0.png"),(200, 200))
        self.elderly_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/elderly/no_anim_0.png"),(200, 200))
        self.mad_piggy_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/mad_piggy/no_anim_0.png"),(200, 200))
        self.wizard_icon = pygame.transform.scale(pygame.image.load("assets/images/characters/wizard/no_anim_0.png"),(200, 200))
        self.select_char_icon = pygame.transform.scale(pygame.image.load("assets/images/background/select_char_icon.png"), (600, 600))

        # Buttons
        self.start_button = Button(390, 500, self.start_icon)
        self.boy_button = Button(350, 300, self.boy_icon, 1)
        self.girl_button = Button(650, 300, self.girl_icon, 2)
        self.elderly_button = Button(250, 500, self.elderly_icon, 3)
        self.mad_piggy_button = Button(550, 500, self.mad_piggy_icon, 4)
        self.wizard_button = Button(850, 500, self.wizard_icon, 5)

        #self.player_image = pygame.Surface((25, 25))  # Placeholder for the player image
        #self.player_image.fill((255, 0, 0))  # Red player placeholder color

        # tiles
        self.tile_size = 32
        self.floor_image = pygame.transform.scale(pygame.image.load("assets/images/tiles/0.png"), (32, 32))
        self.wall_image = pygame.transform.scale(pygame.image.load("assets/images/tiles/7.png"), (32, 32))
        self.obstacle_list = []
        self.player = Player(self.gameMap)
        self.font = pygame.font.Font("assets/fonts/AtariClassic.ttf", 20)
        self.text = ''
        self.new_level = False
        self.level = 1

    def view_start(self):
        # Render the start screen
        # Example: Draw a start button, background, exit button
        self.screen.blit(self.start_background, (0, 0))
        self.screen.blit(self.title_icon, (350, 100))
        action = self.start_button.draw(self.screen)
        return action

    def view_character_select(self):
        # Render the character selection screen
        # Example: Display different characters, let the player choose, etc.
        self.screen.blit(self.start_background, (0, 0))
        self.screen.blit(self.select_char_icon, (350, -20))
        action1, char_type1 = self.boy_button.draw(self.screen)
        action2, char_type2 = self.girl_button.draw(self.screen)
        action3, char_type3 = self.elderly_button.draw(self.screen)
        action4, char_type4 = self.mad_piggy_button.draw(self.screen)
        action5, char_type5 = self.wizard_button.draw(self.screen)

        if action1:
            self.player.type = 1
            return action1, 1
        elif action2:
            self.player.type = 2
            return action2, 2
        elif action3:
            self.player.type = 3
            return action3, 3
        elif action4:
            self.player.type = 4
            return action4, 4
        elif action5:
            self.player.type = 5
            return action5, 5
        else:
            return False, 0

    def view_level(self, player):
        if self.new_level:
            self.gameMap.new_map()
            self.player.new_player(self.gameMap)
            self.new_level = False
            self.level += 1


        # Render the game level
        # Example: Draw the level, characters, obstacles, etc.
        self.screen.fill((0,0,0))  # Fill the screen with a black background

        # Draw the game level
        for y, row in enumerate(self.gameMap.level_map):
            for x, tile_value in enumerate(row):
                # Calculate the screen position for the tile
                tile_rect = pygame.Rect(x * self.tile_size + ((1280 - (len(self.gameMap.level_map[0]))* 32) / 2), y * self.tile_size + ((960 - (len(self.gameMap.level_map))* 32) / 2), self.tile_size, self.tile_size)
                # Draw the corresponding image based on the tile value
                if tile_value == 0:
                    self.screen.blit(self.floor_image, tile_rect.topleft)
                elif tile_value == 1:
                    self.screen.blit(self.wall_image, tile_rect.topleft)
                    self.obstacle_list.append(tile_rect)
                elif 2 <= tile_value <= 15:
                    self.screen.blit(self.floor_image, tile_rect.topleft)
                    self.screen.blit(Item().list[tile_value-2][2], tile_rect.topleft)
                    self.obstacle_list.append(tile_rect)

        # Draw shopping list
        self.draw_rect_alpha(self.screen, (0, 0, 255, 120), (0, 700, 310, 300))
        shopping_text = self.font.render(' Shopping List:', True, (250, 250, 250))
        self.screen.blit(shopping_text, (0, 710))
        for x in range(len(self.player.items)):
            if self.player.items[x] != 0:
                text = self.font.render(f'-{Item().list[self.player.items[x]-2][1]}', True, (250, 250, 250))
                self.screen.blit(text, (0, 710 + ((x + 1) * 20)))

        # Draw hp
        self.draw_rect_alpha(self.screen, (0, 0, 255, 120), (0, 0, 1280, 80))
        level_text = self.font.render(f'Level: {self.level}', True, (250, 250, 250))
        self.screen.blit(level_text, (550, 30))

        # Draw timer

        # Draw the player
        self.screen.blit(player.draw(self.screen), (player.x_pos, player.y_pos))
        # level end conditions
        if len(self.player.items) == 0:
            self.new_level = True
        return self.player


    def draw_rect_alpha(self, surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def view_revive(self):
        # Render the screen when the player can revive
        # Example: Display options for revival, countdown, etc.
        pass

    def view_upgrade_screen(self):
        # Render the upgrade screen
        # Example: Display available upgrades, let the player choose, etc.
        pass

    def view_death(self):
        # Render the death screen
        # Example: Display score, options to restart, etc.
        pass
