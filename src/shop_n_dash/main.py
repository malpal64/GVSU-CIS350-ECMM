import pygame
from controller import Controller


pygame.init()
pygame.display.set_caption("Shop 'n Dash")
clock = pygame.time.Clock()

run = True
controller = Controller()

while run:
    # check quit button push
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Display screen based on status
    if controller.current_state == 0:
        action = controller.show_start()
        if action:
            controller.current_state = 1
    elif controller.current_state == 1:
        action = controller.show_character_select()
        # put char_type to player #
        if action:
            controller.current_state = 2
    elif controller.current_state == 2:
        controller.show_level()
    elif controller.current_state == 3:
        controller.show_revive()
    elif controller.current_state == 4:
        controller.show_upgrade_screen()
    elif controller.current_state == 5:
        controller.show_death()

    pygame.display.update()
    clock.tick(60)  # Cap the frame rate at 60 frames per second

pygame.quit()
